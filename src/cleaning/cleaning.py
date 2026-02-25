import csv

def detect_level(title):
    if title is None:
        return 'Unknown'
    
    cleaning_title = title.strip(' ').lower()

    if 'senior' in cleaning_title or 'старш' in cleaning_title or 'ведущ' in cleaning_title:
        return 'Senior'
    elif 'middle' in cleaning_title or 'мидл' in cleaning_title:
        return 'Middle'
    elif 'junior' in cleaning_title or 'младш' in cleaning_title or 'джуниор' in cleaning_title or 'начинающ' in cleaning_title:
        return 'Junior'
    elif 'intern' in cleaning_title or 'trainee' in cleaning_title or 'стаж' in cleaning_title:
        return 'Intern'

    return 'Unknown'


def clean_data(input_path, output_path):
    with open(input_path, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
            fieldnames = reader.fieldnames + ['level']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            for row in reader:
                title = row['name']
                level = detect_level(title)
                row['level'] = level
                writer.writerow(row)


if __name__ == "__main__":
    clean_data("raw/data.csv", "processed/clean.csv")
