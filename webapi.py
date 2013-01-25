#/usr/bin/python
import config
import json
import os
from utils import *


def get_host_info():
    try:
        l = get_server_list()
        ret={"host_id":config.host_id,"server_list":l}
        return json.dumps(ret)
    except:
        return json.dumps({"Error":track()})
def get_server_status(server_id):
    try:    
        info = {"status":"unknown"}
        update_dir= server_update_dir + host_id
        update_version =  get_svn_version(update_dir)
        cmd = 'cat %s | grep end | tail -n 1'
        run_version = get_cmd_display(cmd)
        info["update_version"] = update_version
        info["run_version"] = run_version
        return info    
    except:
        
        return {} 

def get_server_list() :   
    servers = {}
    try:
        server_list = open(server_list_path).readlines()
        server_list = server_list[1:]

        for info in server_list:
            info = info.replace('\t'," ").strip()
            if  info == "":
                continue
            info = info.split()
            if info[0] == host_id:
                servers[info[1]] = get_server_status(info[1])
        return   json.dumps(servers)
    except:

        return json.dumps({"Error":track()})
def update_one(server_id):
    pass

def upgrade_one(server_id):
    pass
if __name__ == "__main__":
    info = get_host_info()
    print info
    print type(info)
