import argparse
import subprocess
import sys


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Full Vacancy Analytics Pipeline"
    )

    parser.add_argument(
        "--keyword",
        type=str,
        default="python",
        help="Search keyword"
    )

    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Number of vacancies to fetch"
    )

    return parser.parse_args()


def run_step(command, step_name):
    print(f"\n=== {step_name} ===")

    process = subprocess.run(command)

    if process.returncode != 0:
        print(f"❌ {step_name} failed.\n")
        sys.exit(1)

    print(f"✅ {step_name} completed successfully.\n")


def run_pipeline(keyword, limit):
    # 1️⃣ Fetch vacancies
    run_step(
        ["bash", "src/fetching/fetch_vacancies.sh", keyword, str(limit)],
        "Step 1: Fetch Vacancies"
    )

    # 2️⃣ Fetch data (agar alohida script bo‘lsa)
    run_step(
        ["bash", "src/fetching/fetch_data.sh"],
        "Step 2: Fetch Data"
    )

    # 3️⃣ Cleaning
    run_step(
        ["python3", "src/cleaning/cleaning.py"],
        "Step 3: Cleaning Data"
    )

    # 4️⃣ Analytics
    run_step(
        ["python3", "src/analytics/analytics.py"],
        "Step 4: Running Analytics"
    )

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    args = parse_arguments()
    run_pipeline(args.keyword, args.limit)