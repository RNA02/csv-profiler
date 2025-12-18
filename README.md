# CSV Profiler
A simple CSV profiling tool built as part of the SDAIA T5 Bootcamp.
The project provides two ways to analyze CSV files:

1. Command Line Interface (CLI) – generate JSON & Markdown reports
2. Web Application (Streamlit) – interactive browser-based profiling

## Project Structure

csv-profiler/
│
├── data/
│   └── sample.csv
│
├── outputs/
│   ├── report.json
│   └── report.md
│
├── src/
│   └── csv_profiler/
│       ├── __init__.py
│       ├── cli.py
│       └── web.py
│
├── pyproject.toml
├── README.md
└── .gitignore

## Requirements
Python 3.10+
Git
Internet connection (for uvx)

### Option 1: Run Using CLI (Recommended)
This option runs the profiler directly from GitHub without manual setup.
1️⃣ Run the profiler
uvx git+https://github.com/RNA02/csv-profiler profile data/sample.csv --out-dir outputs --format both
2️⃣ Output
After running the command, two files will be created:
outputs/
├── report.json
└── report.md
These contain the CSV profiling results.

### Option 2: Run the Web Application (Streamlit)
This option launches an interactive web interface.
1️⃣ Clone the repository
git clone https://github.com/RNA02/csv-profiler.git
cd csv-profiler
2️⃣ Install dependencies
pip install streamlit pandas
3️⃣ Run the web app
streamlit run src/csv_profiler/web.py
4️⃣ Open in browser
If it does not open automatically, go to:
http://localhost:8501
5️⃣ What you can do in the web app
Upload any CSV file
Preview the data
See dataset overview (rows & columns)
View column-level statistics

### Notes
The CLI generates static reports (JSON / Markdown)
The web app provides interactive exploration
No prior projects are required
The project is fully self-contained

## Author
Abdulrahman Alyami
