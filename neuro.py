import numpy
import scipy
import pandas as pd
import tabulate

raw_data = open("raw_data.txt", "r+", encoding="utf-8")
data = open("data.txt", "w+", encoding="utf-8")
# a = ['Цена', 'Расположение', 'Количество комнат: ', 'Общая площадь: ', 'Площадь кухни: ', 'Жилая площадь: ', 'Этаж: ', 'Балкон или лоджия: ', 'Дополнительно: ', 'Тип комнат: ', 'Высота потолков: ', 'Санузел: ', 'Окна: ', 'Ремонт: ', 'Техника: ', 'Способ продажи: ', 'Вид сделки: ', 'Тип дома: ', 'Год постройки: ', 'Этажей в доме: ', 'Пассажирский лифт: ', 'Грузовой лифт: ', 'Двор: ', 'Парковка: ']
# data_set = set()


#new_data = raw_data.read().replace("'", '"')
#raw_data.truncate(0)
#raw_data.write(new_data)

# loaded_data = pd.read_json("raw_data.txt")

import json

# Read the contents of the file
with open('raw_data.txt', 'r', encoding='utf-8') as file:
    raw = file.readlines()

# Define headers for the table
headers = ["Цена", "Расположение", "Количество комнат: ", "Общая площадь: ", "Площадь кухни: ", "Этаж: ", "Тип комнат: ",
           "Санузел: ", "Ремонт: ", "Способ продажи: ", "Тип дома: ", "Год постройки: ", "Этажей в доме: ", "В доме: "]

# Print table header
data.write("   ".join(headers) + "\n")

# Print each row of the table
s = ""
for line in raw:
    line = line.replace("'", '"')
    # Parse JSON string to dictionary
    property_data = json.loads(line.strip())
    #print(property_data)

    # Extract values for each header, if available, otherwise use empty string
    row_values = [property_data.get(header, "") for header in headers]

    # Print row with values separated by spaces
    s += "   ".join(row_values) + "\n"

data.write(s)

loaded_data = pd.read_table("data.txt", sep="   ", engine="python")
print(loaded_data.to_markdown())
