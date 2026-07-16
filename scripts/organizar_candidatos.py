#!/usr/bin/env python3
"""
Organizador de candidatos (Fatia 3b) — zero custo, sem Google Places.

Lê um CSV simples (busca manual Maps/Instagram) e grava o formato canônico
de Candidatos em data/exports/ (gitignored).

Não imprime telefones no stdout por padrão (use --verbose).
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT_DIR = REPO_ROOT / "data" / "exports"
CANONICAL_FIELDS = [
    "place_id",
    "nome",
    "cidade",
    "endereco",
    "telefone",
    "site",
    "maps_url",
    "fonte",
    "coletado_em",
    "status_revisao",
    "observacoes",
]
INPUT_ALIASES = {
    "nome": ("nome", "loja", "name", "estabelecimento"),
    "cidade": ("cidade", "city"),
    "endereco": ("endereco", "endereço", "address", "addr"),
    "telefone": ("telefone", "whatsapp", "phone", "tel"),
    "site": ("site", "website", "url_site"),
    "maps_url": ("maps_url", "maps", "link_maps", "google_maps"),
    "observacoes": ("observacoes", "observações", "obs", "notas"),
    "place_id": ("place_id", "id"),
}


def _norm_key(key: str) -> str:
    return (
        key.strip()
        .lower()
        .replace("ç", "c")
        .replace("ã", "a")
        .replace("á", "a")
        .replace("à", "a")
        .replace("é", "e")
        .replace("ê", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ô", "o")
        .replace("ú", "u")
    )


def map_row(raw: dict[str, str]) -> dict[str, str]:
    normalized = {_norm_key(k): (v or "").strip() for k, v in raw.items() if k}
    out: dict[str, str] = {}
    for field, aliases in INPUT_ALIASES.items():
        for alias in aliases:
            val = normalized.get(_norm_key(alias), "")
            if val:
                out[field] = val
                break
        else:
            out[field] = ""
    return out


def local_place_id(nome: str, endereco: str, cidade: str) -> str:
    basis = f"{nome.strip().upper()}|{endereco.strip().upper()}|{cidade.strip().upper()}"
    digest = hashlib.sha256(basis.encode("utf-8")).hexdigest()[:16]
    return f"LOCAL_{digest}"


def mask_phone(phone: str) -> str:
    if not phone:
        return "(vazio)"
    digits = "".join(c for c in phone if c.isdigit())
    if len(digits) < 4:
        return "(oculto)"
    return f"***{digits[-4:]}"


def organize(
    rows: list[dict[str, str]],
    *,
    cidade_default: str,
    fonte: str,
    status: str,
    max_results: int,
) -> list[dict[str, str]]:
    now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
    seen: set[str] = set()
    result: list[dict[str, str]] = []

    for raw in rows:
        mapped = map_row(raw)
        nome = mapped.get("nome", "").strip()
        if not nome:
            continue
        cidade = (mapped.get("cidade") or cidade_default).strip().upper()
        endereco = mapped.get("endereco", "").strip()
        place_id = mapped.get("place_id", "").strip() or local_place_id(
            nome, endereco, cidade
        )
        if place_id in seen:
            continue
        seen.add(place_id)

        maps_url = mapped.get("maps_url", "").strip()
        if not maps_url:
            maps_url = ""

        result.append(
            {
                "place_id": place_id,
                "nome": nome,
                "cidade": cidade,
                "endereco": endereco,
                "telefone": mapped.get("telefone", "").strip(),
                "site": mapped.get("site", "").strip(),
                "maps_url": maps_url,
                "fonte": fonte,
                "coletado_em": now,
                "status_revisao": status,
                "observacoes": mapped.get("observacoes", "").strip(),
            }
        )
        if len(result) >= max_results:
            break
    return result


def read_input_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit(f"CSV sem cabeçalho: {path}")
        return [dict(row) for row in reader]


def write_output(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CANONICAL_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Organiza rascunho manual em CSV de candidatos (zero custo)."
    )
    parser.add_argument(
        "--input",
        "-i",
        type=Path,
        required=True,
        help="CSV de entrada (nome,cidade,endereco,telefone,...)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="CSV de saída (default: data/exports/candidatos-<cidade>-<data>.csv)",
    )
    parser.add_argument(
        "--cidade",
        default="BRASILIA",
        help="Cidade padrão se a linha não tiver cidade (default: BRASILIA)",
    )
    parser.add_argument("--fonte", default="Maps", help="Valor da coluna fonte")
    parser.add_argument(
        "--status",
        default="Pendente",
        choices=("Pendente", "Qualificado", "Descartado"),
    )
    parser.add_argument(
        "--max",
        type=int,
        default=40,
        help="Cap de linhas de saída (default: 40)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Mostra telefones mascarados (****1234) no resumo",
    )
    args = parser.parse_args(argv)

    if not args.input.is_file():
        print(f"Erro: arquivo não encontrado: {args.input}", file=sys.stderr)
        return 1

    raw_rows = read_input_csv(args.input)
    organized = organize(
        raw_rows,
        cidade_default=args.cidade.strip().upper(),
        fonte=args.fonte,
        status=args.status,
        max_results=max(1, args.max),
    )

    if not organized:
        print("Erro: nenhuma linha válida (precisa de coluna nome/loja).", file=sys.stderr)
        return 1

    out = args.output
    if out is None:
        stamp = datetime.now().strftime("%Y%m%d")
        cidade_slug = args.cidade.strip().upper().replace(" ", "-")
        out = DEFAULT_OUT_DIR / f"candidatos-{cidade_slug}-{stamp}.csv"

    write_output(out, organized)

    print(f"OK: {len(organized)} candidato(s) -> {out}")
    print("status_revisao padrao:", args.status)
    print("LGPD: arquivo em data/exports/ (fora do Git). Triagem: Candidatos-revisao.md")
    for i, row in enumerate(organized[:5], 1):
        phone_bit = (
            f" tel={mask_phone(row['telefone'])}" if args.verbose else ""
        )
        print(f"  {i}. {row['nome']} ({row['cidade']}){phone_bit}")
    if len(organized) > 5:
        print(f"  ... +{len(organized) - 5} linha(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
