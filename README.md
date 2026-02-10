# Vacancy Analytics Pipeline

## Project Overview

This project analyzes job vacancies data fetched from the HeadHunter API.

Default settings:
- Keyword: "data science"
- Limit: 100 latest vacancies

The analysis focuses on:
- Experience level distribution (Junior / Middle / Senior / Unknown)
- Vacancy activity by date
- Most frequent role keywords

## Data Pipeline

1. Vacancies are fetched from the API
2. Raw data is converted into a structured format
3. Job titles are cleaned and categorized
4. Statistics are calculated
5. A human-readable report is generated
