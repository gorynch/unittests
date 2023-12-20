from tokens import yaToken

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765",
     "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    isTrue = False
    for value in documents:
        if doc_number == value.get('number'):
            isTrue = True
            res = value.get('name')
    if isTrue:
        return res
    else:
        return ('Документ не найден')


def get_directory(doc_number):
    isTrue = False
    for dir in directories:
        if doc_number in directories[dir]:
            isTrue = True
            res = int(dir)
    if isTrue:
        return res
    else:
        return ('Полки с таким документом не найдено')


def add_person(document_type, number, name, shelf_number):
    new_record = {"type": document_type, "number": number, "name": name}
    documents.append(new_record)
    record_s_shelf = [str(number)]
    directories.update({str(shelf_number): record_s_shelf})
    if get_name(number) == name:
        return True
    else:
        return False

import requests
from tokens import yaToken

yaURL = 'https://cloud-api.yandex.net/v1/disk/resources/'

class YaApi:
    def __init__(self, YaToken, YaUrl):
        self.YaToken = YaToken
        self.YaUrl = YaUrl
    def createFolder(self,folderName):
        headers = {'Content-Type': 'application/json',
                  'Accept': 'application/json',
                  'Authorization': f'OAuth {self.YaToken}',
                   "path": folderName
                   }
        response = requests.put(f'{yaURL}?path={folderName}', headers=headers)
        return response.status_code

def yaApi_create_folder(folder_name):
    myYaDisk = YaApi(yaToken, yaURL)
    return myYaDisk.createFolder(folder_name)