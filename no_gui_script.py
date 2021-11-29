""" download ah_json_file with out gui """
import downloadFile as dF
import realmlist as rl
import apiconnect as api

list_serv = [1084, 1403, 1305, 3674, 3391, 3713]


def run_all():
    """ run all servers """
    dF.func(rl.list_class_server)


def run_specific_server(list_id):
    
    for id_server in list_id:
        print("pobieram " + str(id_server))
        directory = api.create_new_folder(id_server)
        api.auction_house_download(id_server, directory)


run_specific_server(list_serv)
