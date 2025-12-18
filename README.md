# CSV Profiler

This project is a simple CSV profiling tool built as part of the SDAIA T5 Bootcamp.

It allows running a CSV profiler directly from GitHub using `uvx`.

---

## What does it do?

- Reads a CSV file
- Generates basic profiling outputs
- Saves results as JSON and Markdown files

---

## How to run (CLI)

```bash
uvx git+https://github.com/RNA02/csv-profiler data/sample.csv --out-dir outputs --format both
