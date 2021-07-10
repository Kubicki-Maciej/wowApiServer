import csv
import pandas as pd

set_file_name = 'settings.csv'


def load_file_settings(setting_file):
    file = pd.read_csv(setting_file)
    return file


def load_settings(row, setting_file):
    #  by name? or by row?

    temp_df = load_file_settings(setting_file)
    server_name = temp_df.loc[row, 'servers_name']
    value_id = temp_df.loc[row, 'value_id']


def save_settings(df, filename):
    df.to_csv(filename, index=False)


def add_settings(setting_file, df, list_of_settings):
    """ taking list of settings len(4), with paramets: name, int, boolean, str"""

    row = len(df) + 1

    df.loc[row, 'setting name'] = list_of_settings[0]
    df.loc[row, 'int_value'] = list_of_settings[1]

    save_settings(df, setting_file)


def change_setting(set_file_name, df, row, setting_to_change, value_to_change):
    if row <= len(df):
        df.loc[row, setting_to_change] = value_to_change

        # save settings here
        save_settings(df, set_file_name)

        return df
    else:
        print('to high value')


def get_list_to_setting_and_save_them(list_objects):
    temp_list = []
    clear_file()


    for object_in_list in list_objects:
        temp_list.append(object_in_list.return_id_and_name())

    name_list = []
    id_list = []
    counter = 0

    df = load_file_settings(set_file_name)

    for name_and_id in temp_list:
        name_list.append(name_and_id[0])
        id_list.append(name_and_id[1])

        change_setting(set_file_name, df, counter, 'servers_name', name_and_id[0])
        change_setting(set_file_name, df, counter, 'value_id', name_and_id[1])
        counter += 1

    print(name_list)
    print(id_list)


    # df = load_file_settings(set_file_name)
    # change_setting(set_file_name, df, 0, 'servers_name', name_list)
    # change_setting(set_file_name, df, 0, 'value_id', id_list)


def create_file(namefile):
    """ create csv file """
    with open(namefile, 'w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['id','name item','url pict'])
        writer.writerow(['servers_name', 'value_id'])

def load_id_server_and_name_from_csv_file(df):

    col1 = df['servers_name'].to_list()
    col2 = df['value_id'].to_list()
    return col1, col2

def clear_file():
    f = open(set_file_name, "w+")
    f.close()

    with open(set_file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['servers_name', 'value_id'])

#  csv most players in server
# servers_name,value_id
# Draenor,1403
# Kazzak,1305
# Ragnaros,3682
# Twisting Nether,3674
# Al'Akir,3713
# Dentarg,1084
# Silvermoon,3391
# Burning Legion,3713