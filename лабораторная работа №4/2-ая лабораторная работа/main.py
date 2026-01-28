# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
     # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'rt') as f:
        reader = csv.DictReader(f)
        converted_data = []
        for row in reader:
            converted_row = {
                'longitude': float(row['longitude']),
                'latitude': float(row['latitude']),
                'housing_median_age': float(row['housing_median_age']),
                'total_rooms': float(row['total_rooms']),
                'total_bedrooms': float(row['total_bedrooms']),
                'population': float(row['population']),
                'households': float(row['households']),
                'median_income': float(row['median_income']),
                'median_house_value': float(row['median_house_value'])
            }
            converted_data.append(converted_row)
     # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'wt', encoding='utf-8') as f:
        json.dump(converted_data, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
