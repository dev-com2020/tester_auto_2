import json

# with open('dane.json','r') as file:
#     data = json.load(file)
#
# # print(data['members'][2]['powers'][3])
# print(data['members'][2]['age'])



slownik = {1:"Tomek"}
slownik[2] = "Mariusz"
slownik[1] = "Adam"
slownik["Tomek"] = 2023
slownik['spanie'] = False
slownik['temp'] = 36.6
slownik['jezyki'] = ['C',"python",'java']
slownik['czyPali'] = None
# print(slownik['Tomek'])
# # print(slownik['Adam'])
# print(slownik.get('Adam'))
# print(slownik.keys())
# print(slownik.values())
# print("Tomek" in slownik)
# print(slownik)
with open('assets/baza.json', 'w') as plik:
    json.dump(slownik,plik)