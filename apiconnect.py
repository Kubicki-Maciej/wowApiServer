#import realmlist  # first realmlist execute then apiconnect !!!
from blizzardapi import BlizzardApi
import json
import os
import datetime
import datainfo as d

api_client = BlizzardApi(d.key, d.secretkey)

def create_new_folder():
    """ create new folder where data from api came in"""
    try:
        directory = current_date()+"_Json_data"
        parent_dir = "E:\serverWowApi\data"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        #print('created file :'+directory)
        return directory

    except FileExistsError as exc:
        print("file with this name exist error :"+exc)

def current_date():
    """ return date m/d/y/h/m/ """
    current_date = datetime.datetime.now()
    string_date = current_date.strftime("%m.%d.%Y_%H;%M")
    return string_date

def save_file_json(file_to_save, id_group_server, directory):
    """ save downlaoded file, taking arg id_group_server """

    with open('data/'+directory+'/'+'ah_' + str(id_group_server) + '_' + current_date() + '.json', 'w') as json_file:
        json.dump(file_to_save, json_file,) #indent=2)


def auction_house_download(id_group_servers, directory, region='eu', dynamic='dynamic-eu'):
    """ send request to get auction house file, saveing it in Json with current date """

    json_ah_file = api_client.wow.game_data.get_auctions(region, dynamic, id_group_servers)
    save_file_json(json_ah_file, id_group_servers, directory)
    print(current_date()+' pobrano auction house')
    return json_ah_file

def download_item_by_id(id_item):
    """
    function connect to blizzard server and download item_data and item_media where is icon of item
    :param id_item:
    :return: information about item, picture item
    """
    item_data = api_client.wow.game_data.get_item('eu', 'static-eu', id_item)
    item_media_data = api_client.wow.game_data.get_item_media('eu', 'static-eu', id_item)
    return item_data, item_media_data