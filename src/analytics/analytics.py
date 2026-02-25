import csv
from collections import Counter
CATEGORIES = {

    # ===== Backend Languages =====
    "Python": [
        "python", "питон"
    ],
    "Java": [
        "java", "джава"
    ],
    "Go": [
        "golang", " go ", " го "
    ],
    "C#": [
        "c#", ".net", " asp.net", " asp net"
    ],
    "PHP": [
        "php"
    ],
    "Ruby": [
        "ruby", "руб"
    ],
    "Node.js": [
        "node", "node.js", "nodejs"
    ],

    # ===== Frontend =====
    "JavaScript": [
        "javascript", " js ", "жаваскрипт"
    ],
    "TypeScript": [
        "typescript", "ts "
    ],
    "React": [
        "react", "react.js", "реакт"
    ],
    "Vue": [
        "vue", "vue.js", "вью"
    ],
    "Angular": [
        "angular", "ангуляр"
    ],
    "Frontend": [
        "frontend", "front-end", "фронтенд", "фронт"
    ],

    # ===== Backend Generic =====
    "Backend": [
        "backend", "back-end", "бекенд", "бэкенд"
    ],

    # ===== Mobile =====
    "Flutter": [
        "flutter", "флаттер"
    ],
    "Android": [
        "android", "андроид", "kotlin"
    ],
    "iOS": [
        "ios", "swift", "айос"
    ],
    "React Native": [
        "react native"
    ],

    # ===== Data & AI =====
    "Data Science": [
        "data scientist", "дата саентист"
    ],
    "Data Analyst": [
        "data analyst", "аналитик данных"
    ],
    "Machine Learning": [
        "machine learning", "ml", "машинное обучение"
    ],
    "AI": [
        " ai ", "искусственный интеллект"
    ],
    "Data Engineer": [
        "data engineer", "инженер данных"
    ],

    # ===== QA =====
    "QA": [
        "qa", "тестировщик", "инженер по тестированию"
    ],
    "Automation QA": [
        "automation", "автоматизац"
    ],

    # ===== DevOps & Infra =====
    "DevOps": [
        "devops", "девопс"
    ],
    "Docker": [
        "docker", "докер"
    ],
    "Kubernetes": [
        "kubernetes", "k8s"
    ],
    "Linux": [
        "linux", "линукс"
    ],
    "Cloud": [
        "cloud", "облако"
    ],
    "AWS": [
        "aws"
    ],

    # ===== Databases =====
    "SQL": [
        " sql "
    ],
    "PostgreSQL": [
        "postgres", "postgresql"
    ],
    "MySQL": [
        "mysql"
    ],
    "MongoDB": [
        "mongo", "mongodb"
    ],

    # ===== Management =====
    "Product Manager": [
        "product manager", "продакт"
    ],
    "Project Manager": [
        "project manager", "руководитель проекта", "pm "
    ],
    "Business Analyst": [
        "business analyst", "бизнес-аналитик"
    ],
    "Scrum": [
        "scrum"
    ],

    # ===== Other Tech =====
    "1C": [
        "1c", "1с"
    ],
    "C++": [
        "c++"
    ],
    "Unity": [
        "unity"
    ],
    "Computer Vision": [
        "computer vision", "компьютерное зрение"
    ]
}

def analyze_levels(input_path):
    level_counts = Counter()
    total = 0
    
    with open(input_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            level = row['level']
            level_counts[level] += 1
            total += 1
            
    return level_counts, total

def calculate_percentages(level_counts, total):
    result = {}
    if total == 0:
        return {}
    else:
        for level in level_counts:
            count = level_counts[level]
            percent = round((count / total) * 100, 2 )

            result.update({
                level: {
                    "count": count,
                    "percent": percent
                }
            })
        return result

def print_level_report(stats, total):
    print(f"Total vacancies: {total}\n")

    order = ["Senior", "Middle", "Junior", "Intern", "Unknown"]

    for level in order:
        if level in stats:
            count = stats[level]["count"]
            percent = stats[level]["percent"]
            print(f"{level}: {count} ({percent}%)")

def analyze_activity_by_date(input_path):
    counter = Counter()
    
    with open(input_path, newline='', encoding='utf-8') as data:
        reader = csv.DictReader(data)
        
        for row in reader:
            published_at = row['published_at']
            date = published_at[:10]
            counter[date] += 1

        return counter

def get_most_active_day(date_counts):
    if not date_counts:
        return None, 0

    most_active_day = max(date_counts, key=date_counts.get)
    return most_active_day, date_counts[most_active_day]

def analyze_directions(input_path):
    counts = Counter()

    with open(input_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            title = row['name'].lower()

            for category, keywords in CATEGORIES.items():
                for keyword in keywords:
                    if keyword in title:
                        counts[category] += 1
                        break
    return counts

def build_report(total, level_stats, most_active_day, day_count, direction_counts):
    lines = []

    # Title
    lines.append("# Vacancy Analytics Report")
    lines.append("")

    # Total
    lines.append("## 📊 Overview")
    lines.append("")
    lines.append(f"**Total vacancies:** {total}")
    lines.append("")

    # Level Distribution
    lines.append("## 🎯 Level Distribution")
    lines.append("")
    lines.append("| Level | Count | Percentage |")
    lines.append("|-------|-------|------------|")

    order = ["Senior", "Middle", "Junior", "Intern", "Unknown"]

    for level in order:
        if level in level_stats:
            count = level_stats[level]["count"]
            percent = level_stats[level]["percent"]
            lines.append(f"| {level} | {count} | {percent}% |")

    lines.append("")

    # Most Active Day
    lines.append("## 📅 Most Active Day")
    lines.append("")
    lines.append(f"**{most_active_day}** — {day_count} vacancies")
    lines.append("")

    # Directions
    lines.append("## 🧭 Directions Breakdown")
    lines.append("")
    lines.append("| Direction | Count |")
    lines.append("|-----------|-------|")

    for direction, count in direction_counts.most_common():
        lines.append(f"| {direction} | {count} |")

    return "\n".join(lines)

        
if __name__ == "__main__":
    input_path = "processed/clean.csv"

    # 1️⃣ Level analysis
    level_counts, total = analyze_levels(input_path)
    level_stats = calculate_percentages(level_counts, total)

    # 2️⃣ Activity analysis
    date_counts = analyze_activity_by_date(input_path)
    most_active_day, day_count = get_most_active_day(date_counts)

    # 3️⃣ Direction analysis
    direction_counts = analyze_directions(input_path)

    # 4️⃣ Report build
    report = build_report(
        total=total,
        level_stats=level_stats,
        most_active_day=most_active_day,
        day_count=day_count,
        direction_counts=direction_counts
    )

    # 5️⃣ Print
    print(report)

    # 6️⃣ Save to file
    with open("processed/report.txt", "w", encoding="utf-8") as f:
        f.write(report)