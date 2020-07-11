from pprint import pprint
import csv
import re



with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

phone_pattern = re.compile(r'(\+?\d{1})\s*\(?(\d{3})\)?\-?\s?(\s?\d{3})\-?(\d{2})\-?(\d+)')
ext_phone_pattern = re.compile(r'\(?\w+\.\s(\d{4})\)?')

for item in contacts_list:
    # print(item[-2])
    item[-2] = phone_pattern.sub(r'+7(\2)\3-\4-\5', item[-2])
    item[-2] = ext_phone_pattern.sub(r'доб.\1', item[-2])
    print(item[-2])