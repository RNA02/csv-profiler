from pathlib import Path
import json
import sys

import typer
import pandas as pd

app = typer.Typer(help="CSV Profiler (CLI + Streamlit)")

@app.command()
def profile(
    csv_path: str = typer.Argument(..., help="Path to CSV file"),
    out_dir: str = typer.Option("outputs", "--out-dir", help="Output directory"),
    format: str = typer.Option("both", "--format", help="json | md | both"),
):
    df = pd.read_csv(csv_path)

    report = {
        "file": csv_path,
        "shape": {"rows": int(df.shape[0]), "cols": int(df.shape[1])},
        "columns": {},
    }

    for col in df.columns:
        report["columns"][col] = {
            "dtype": str(df[col].dtype),
            "missing": int(df[col].isna().sum()),
            "unique": int(df[col].nunique(dropna=True)),
        }

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    if format in ("json", "both"):
        (out / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    if format in ("md", "markdown", "both"):
        lines = [
            "# CSV Profile Report",
            f"- File: `{csv_path}`",
            f"- Rows: **{report['shape']['rows']}**",
            f"- Columns: **{report['shape']['cols']}**",
            "",
            "## Columns",
        ]
        for col, stats in report["columns"].items():
            lines += [
                f"### {col}",
                f"- dtype: `{stats['dtype']}`",
                f"- missing: **{stats['missing']}**",
                f"- unique: **{stats['unique']}**",
                "",
            ]
        (out / "report.md").write_text("\n".join(lines), encoding="utf-8")

    typer.echo(f"Done ✅ Reports created in {out_dir}")

@app.command()
def web():
    import streamlit.web.cli as stcli
    sys.argv = ["streamlit", "run", "app.py"]
    raise SystemExit(stcli.main())

def main():
    app()