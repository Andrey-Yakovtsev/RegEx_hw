from pprint import pprint
import csv
import re



with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

phone_pattern = re.compile(r'(\+?\d{1})\s*\(?(\d{3})\)?\-?\s?(\s?\d{3})\-?(\d{2})\-?(\d+)')
ext_phone_pattern = re.compile(r'\(?\w+\.\s(\d{4})\)?')
fio_pattern = re.compile(r"\'([а-яёА-ЯЁ]*)\s{1}([а-яёА-ЯЁ]*)\s{1}([а-яёА-ЯЁ]*)\'\,(\s?\'?'?,)?(\s?\'?'?,)?")
# fio_pattern = re.compile(r"([а-яёА-ЯЁ]*)\s?([а-яёА-ЯЁ]*)\s?([а-яёА-ЯЁ]*)\S")
edited_con_list = []

for unique_person_data in contacts_list:
    lastname = unique_person_data[0]
    lastname = lastname.replace(' ', ',')
    lastname = lastname.split(',')
    firstname = unique_person_data[1]
    # firstname = firstname.replace(' ', ',')
    # firstname = firstname.split(',')
    surname = unique_person_data[2]
    organization = unique_person_data[3]
    position = unique_person_data[4]
    phone = unique_person_data[5]
    email = unique_person_data[6]

    phone = phone_pattern.sub(r'+7(\2)\3-\4-\5', phone)
    phone = ext_phone_pattern.sub(r'доб.\1', phone)
    # aggregated_name = fio_pattern.sub(r"'\1', '\2', '\3',", lastname)
    # print(lastname)
    # print(unique_person_data)
    updated_unique_person_data = [
    lastname,
    # firstname,
    # surname,
    organization,
    position,
    phone,
    email]

    edited_con_list.append(updated_unique_person_data)

pprint(edited_con_list)
#
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   datawriter.writerows(edited_con_list)

