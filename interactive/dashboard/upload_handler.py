import csv
from django.conf import settings
import os
from .save import load, save, export
import json
from django.conf import settings
from interactive.tools import *
import logging
config_path = os.path.join(settings.BASE_DIR, "dashboard/static/config")


# converts uploaded csv input file to dictionary of values
def handle_uploaded_csv(f):
    content = f.read()
    new = str(content.decode('utf-8'))
    if ',' in new:
        listed = new.split(',')
    for i in listed:
        if '\r\n' in i:
            listed[listed.index(i)] = i.replace('\r\n', '')
    while '' in listed:
        listed.remove('')
    dictFromFile = {}
    fileitems = int(len(listed) / 2)
    for j in listed:
        dictFromFile.update({j: listed[listed.index(j) + fileitems]})
        if len(dictFromFile) == fileitems:
            break
    
    return(dictFromFile)
        
#checks uploaded configuration against current config file
def validate_config(testDict):
    config = open_json('my_config.json')
    requirements = []
    for key in config:
        requirements.append(key)
    
    errors = []

    for item in requirements:
        if item not in testDict:
            errors.append(item)
    
    if len(errors) > 0:
        return {'success': False, 'errors': errors}
    elif len(errors) == 0:
        return {'success': True}

# loads uploaded json file into dictionary, validates, and saves to json file
def handle_uploaded_json(f):
    content = f.read()
    decoded = content.decode('utf-8')
    config = json.loads(decoded)
    validation = validate_config(config)
    print(validation)
    if validation['success']:
        dump_json('my_config.json', config)