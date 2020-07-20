from pprint import pprint
import csv
import re



phone_pattern = re.compile(r'(\+?\d{1})\s*\(?(\d{3})\)?\-?\s?(\s?\d{3})\-?(\d{2})\-?(\d+)')
ext_phone_pattern = re.compile(r'\(?\w+\.\s(\d{4})\)?')


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_contact_list = []

for string in contacts_list:
    surname = string[2].split()
    firstname = string[1].split()
    lastname = string[0].split()
    organization = string[3]
    position = string[4]
    phone = string[5]
    phone = phone_pattern.sub(r'+7(\2)\3-\4-\5', phone)
    phone = ext_phone_pattern.sub(r'доб.\1', phone)
    email = string[6]

    if len(lastname) == 3:
        surname = lastname[2]
        firstname = lastname[1]
        lastname = lastname[0]
    if len(lastname) == 2:
        firstname = lastname[1]
        lastname = lastname[0]
    if len(lastname) == 1:
        lastname = lastname[0]
    if len(firstname) == 1:
        firstname = firstname[0]
    if len(surname) == 1:
        surname = surname[0]
    if len(firstname) == 2:
        surname = firstname[1]
        firstname = firstname[0]

    new_contact_string = [lastname, firstname, surname, organization, position, phone, email]
    new_contact_list.append(new_contact_string)

for contact_split_1 in new_contact_list:
    for contact_split_2 in new_contact_list:
        if contact_split_1[0] == contact_split_2[0] \
                and contact_split_1[1] == contact_split_2[1] \
                and contact_split_1 != contact_split_2:
            num = 0
            for field in contact_split_1:
                num = contact_split_1.index(field, num)
                if (contact_split_1[num] != contact_split_2[num]) \
                        and (contact_split_1[num] == ''):
                    contact_split_1[num] = contact_split_2[num]
            new_contact_list.remove(contact_split_2)


with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contact_list)