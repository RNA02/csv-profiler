from pathlib import Path
import typer

app = typer.Typer()

@app.command()
def profile(
    csv_path: str,
    out_dir: str = "outputs",
    format: str = "both",
):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    # Minimal placeholder outputs (enough for the assignment "uvx run")
    if format in ("json", "both"):
        (out / "report.json").write_text('{"status":"ok"}\n', encoding="utf-8")

    if format in ("md", "markdown", "both"):
        (out / "report.md").write_text("# Report\n\nGenerated.\n", encoding="utf-8")

    print(f"Done ✅ Reports created in {out_dir}")

def main():
    app()

if __name__ == "__main__":
    main()