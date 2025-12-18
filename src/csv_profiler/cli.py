from pathlib import Path
import typer

app = typer.Typer()

@app.command()
def profile(
    csv_path: str = typer.Argument(..., help="Path to CSV file"),
    out_dir: str = typer.Option("outputs", "--out-dir", help="Output directory"),
    format: str = typer.Option("both", "--format", help="json|md|both"),
):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    if format in ("json", "both"):
        (out / "report.json").write_text('{"status":"ok"}\n', encoding="utf-8")

    if format in ("md", "markdown", "both"):
        (out / "report.md").write_text("# Report\n\nGenerated.\n", encoding="utf-8")

    print(f"Done ✅ Reports created in {out_dir}")

def main():
    app()

if __name__ == "__main__":
    main()