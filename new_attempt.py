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
contact_dict = {}
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

'''
Попытка запилить через словарь

    string_dict = {
        lastname:
            {
            'firstname': firstname,
            'surname': surname,
            'organization': organization,
            'position': position,
            'phone': phone,
            'email': email}
    }
    # print(string_dict)
    for key, value in string_dict.items():
        if key in contact_dict.keys():
            if value:
                string_dict[key].update(value)
                print(key, value)
        else:
            contact_dict.update(string_dict)
pprint(contact_dict)
'''

pprint(new_contact_list)

''' Пытаюсь понять как проходя по списку проверять что такое значение уже было получено ранее и 
если поле непустое то заполнить его.
'''
# for item in new_contact_list:
#     for piese in item:
#         if piese:
#             print(piese)
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     datawriter.writerows(new_contact_list)