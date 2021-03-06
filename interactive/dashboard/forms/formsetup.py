import json
from django.conf import settings
import os
from csv import reader
from mechanism.reactions import reaction_musica_names
from dashboard.save import initial_conditions_file_to_dictionary

config_path = os.path.join(settings.BASE_DIR, "dashboard/static/config")

def option_setup():
    with open(os.path.join(config_path, 'options.json')) as f:
        data = json.loads(f.read())

    return data


def ini_cond_setup():
    with open(os.path.join(config_path, 'initials.json')) as f:
        data = json.loads(f.read())

    return data


def display_evolves():
    with open(os.path.join(config_path, 'my_config.json')) as f:
        config = json.loads(f.read())

    e = config['evolving conditions']
    evolving_conditions_list = e.keys()

    file_header_dict = {} #contains a dictionary w/ key as filename and value as header of file
    for i in evolving_conditions_list:
        if '.csv' in i or '.txt' in i:
            path = os.path.join(os.path.join(settings.BASE_DIR, "dashboard/static/config"), i)
            with open(path, 'r') as read_obj:
                csv_reader = reader(read_obj)
                list_of_rows = list(csv_reader)

            try:
                file_header_dict.update({i:list_of_rows[0]})
            except IndexError:
                file_header_dict.update({i:['EMPTY FILE']})
        elif '.nc' in i:
            file_header_dict.update({i:['NETCDF FILE']})
    return file_header_dict
