import os
import re

username = 'jesualdopc'
file_path = f'/Users/{username}/Documents/Python/Python Bootcamp/Complete-Python-3-Bootcamp-master/12-Advanced Python Modules/08-Advanced-Python-Module-Exercise/extracted_content'
phone = r"\d{3}-\d{3}-\d{4}"


def search(file, lookup):
    f = open(file, 'r')
    text = f.read()

    if re.search(phone, text):
        return re.findall(phone, text)
    else:
        pass


result = []
locations = []

for folder, sub_folders, files in os.walk(file_path):
    for f in files:
        full_path = folder + '/'+f
        if search(full_path, phone) != None:
            result.append(search(full_path, phone))
            locations.append(full_path)


for r in result:
    for l in locations:
        print(f'Location: {l} \nNumber:{r}')
