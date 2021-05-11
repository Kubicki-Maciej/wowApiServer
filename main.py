from time import sleep
from threading import Thread
import apiconnect as api
import realmlist as rl

def func(list_of_server, directory):
    """
    download files from blizzard api by id in Json
    """
    for realm in list_of_server:
        try:
            api.auction_house_download(realm.id_group, directory)
            print('download json file id:'+str(realm.id_group))
        except:
            print("error with download file id :"+str(realm.id_group))


while True:
    directory = api.create_new_folder()
    Thread(target=func(rl.list_class_server, directory)).start() #download files every 1h:10m

    sleep(4200)

