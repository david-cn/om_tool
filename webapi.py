#/usr/bin/python
import config
import json
import os
from utils import *
from update_tools import *
from upgrade_tools import *


def get_host_info():
    try:
        l = get_server_list()
        ret={"RetCode":"success","host_id":config.host_id,"server_list":l}
        return json.dumps(ret)
    except:
        return json.dumps({"Retcode":"fail","Error":track()})
def get_server_status(server_id):
    try:    
        info = {"RetCode":"sucess","status":"unknown"}
        update_dir= server_update_dir + host_id
        update_version =  get_svn_version(update_dir)
        cmd = 'cat %s | grep end | tail -n 1'
        run_version = get_cmd_display(cmd)
        info["update_version"] = update_version
        info["run_version"] = run_version
        return info    
    except:
        return {"RetCode":"fail","Error":track()}

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

        return json.dumps({"RetCode":"fail","Error":track()})
def api_update_one(server_id):
    try:
        servers_info = get_server_listinfo()
        update_one(server_idi,servers_info[server_id].get("svn_dir"))
        return json.dumps({"RetCode":"sucess"})
    except:
        return json.dumps({"RetCode":"fail","Error":track()})
def api_upgrade_one(server_id):
    servers_info = get_server_listinfo()
    upgrade_one(server_idi,servers_info[server_id].get("svn_dir"))
def api_start_server(server_id,cmd):
    if cmd == "start":
        pass
    elif cmd == "stop":
        pass
    elif cmd == "restart":
        pass
    else
        pass

def start_server(server_id):
    pass
def stop_server(server_id):
    pass
def restart_server(server_id):
    pass



if __name__ == "__main__":
    info = get_host_info()
    print info
    print type(info)
