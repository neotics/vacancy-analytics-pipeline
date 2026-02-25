# Vacancy Analytics Pipeline

## Overview

Vacancy Analytics Pipeline — bu HeadHunter API asosida ishlaydigan to‘liq data pipeline.

Loyiha quyidagilarni bajaradi:

- API dan vacancy ma’lumotlarini olish
- JSON → CSV konvertatsiya
- Data cleaning
- Level classification (Junior / Middle / Senior / Intern)
- Activity analysis (eng aktiv kun)
- Direction analysis (Python, QA, DevOps va boshqalar)
- Markdown formatda yakuniy report generatsiya qilish

Loyiha modular arxitektura asosida yozilgan va bitta entry-point orqali ishga tushadi.

---

## Project Structure

```
Vacancy_Analytics/
│
├── main.py
├── raw/
│ ├── data.json
│ └── data.csv
├── processed/
│ ├── clean.csv
│ └── report.md
├── src/
│ ├── fetching/
│ │ ├── fetch_vacancies.sh
│ │ └── fetch_data.sh
│ ├── cleaning/
│ │ └── cleaning.py
│ └── analytics/
│   └── analytics.py
```

---

## Pipeline Flow

1. Fetch vacancies from API  
2. Convert JSON to CSV  
3. Clean and enrich data  
4. Run analytics  
5. Generate final Markdown report  

Barcha bosqichlar `main.py` orqali boshqariladi.

---

## Requirements

- Python 3.8+
- Bash
- jq (JSON parsing uchun)

Agar `jq` o‘rnatilmagan bo‘lsa:

```bash
sudo apt install jq
```
## Usage

Root papkadan ishga tushiriladi:

```Bash
python3 main.py --keyword "data science" --limit 100
```

## CLI Arguments

| Argument  | Description                      | Default |
|-----------|----------------------------------|---------|
| --keyword | Vacancy search keyword           | python  |
| --limit   | Number of vacancies to fetch     | 100     |

## Output Files

Pipeline natijasida quyidagi fayllar hosil bo‘ladi:

raw/data.json
raw/data.csv
processed/clean.csv
processed/report.md

## Report Example

Generatsiya qilingan report.md quyidagi ko‘rinishda bo‘ladi:

```Markdown
# Vacancy Analytics Report

## 📊 Overview
Total vacancies: 100

## 🎯 Level Distribution

| Level  | Count | Percentage |
|--------|-------|------------|
| Senior | 18    | 18%        |
| Middle | 25    | 25%        |
| Junior | 30    | 30%        |
| Intern | 7     | 7%         |
| Unknown| 20    | 20%        |

## 📅 Most Active Day
2026-02-17 — 18 vacancies

## 🧭 Directions Breakdown

| Direction | Count |
|-----------|-------|
| Python    | 42    |
| Backend   | 31    |
| QA        | 18    |

```

## Features

- Modular architecture
- Full CLI support
- Russian + English level detection
- Multi-category direction analysis
- Markdown report generation
- Automated end-to-end pipeline

## Skills Demonstrated

- Shell scripting
- API data fetching
- JSON processing
- CSV handling
- Data cleaning
- Classification logic
- Analytics with Python
- CLI design
- Modular project architecture

## Future Improvements

- Logging system
- Execution time tracking
- Data visualization (matplotlib)
- Docker support
- Unit tests

## Author
Sarvar Xalimbetov
Backend & Data Engineering Enthusiast