from pprint import pprint
import csv
import re



phone_pattern = re.compile(r'(\+?\d{1})\s*\(?(\d{3})\)?\-?\s?(\s?\d{3})\-?(\d{2})\-?(\d+)')
ext_phone_pattern = re.compile(r'\(?\w+\.\s(\d{4})\)?')


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
new_contact_list = [] #'lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
lastnamelist = []
for cell in contacts_list:
    surname = cell[2].split()
    firstname = cell[1].split()
    lastname = cell[0].split()
    organization = cell[3]
    position = cell[4]
    phone = cell[5]
    phone = phone_pattern.sub(r'+7(\2)\3-\4-\5', phone)
    phone = ext_phone_pattern.sub(r'доб.\1', phone)
    email = cell[6]

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
    lastnamelist.append(lastname)
    new_contact_list.append(new_contact_string)
# print(set(lastnamelist))
# pprint(new_contact_list)
upd_contact_string = []
for contact_string in new_contact_list:
    if contact_string[0] in set(lastnamelist):
        for item in contact_string:
            if item:
                upd_contact_string.append(item)
        # upd_contact_string = [contact_string[0], contact_string[1], contact_string[2], contact_string[3]]
pprint(upd_contact_string)
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     datawriter.writerows(new_contact_list)