import numpy
import scipy
import pandas as pd
import tabulate

raw_data = open("raw_data.txt", "r+", encoding="utf-8")
data = open("data.txt", "w+", encoding="utf-8")

import json

with open('raw_data.txt', 'r', encoding='utf-8') as file:
    raw = file.readlines()

headers = ["Цена", "Расположение", "Количество комнат: ", "Общая площадь: ", "Площадь кухни: ", "Этаж: ",
           "Тип комнат: ",
           "Санузел: ", "Ремонт: ", "Способ продажи: ", "Тип дома: ", "Год постройки: ", "Этажей в доме: ", "В доме: "]

data.write("   ".join(headers) + "\n")

s = ""
for line in raw:
    line = line.replace("'", '"')
    property_data = json.loads(line.strip())
    row_values = [property_data.get(header, "") for header in headers]
    s += "   ".join(row_values) + "\n"

data.write(s)

loaded_data = pd.read_table("data.txt", sep="   ", engine="python")
print(loaded_data.to_markdown())
