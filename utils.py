#/usr/bin/python
import os
import config

tools_dir=os.path.split(os.path.realpath(__file__))[0] + "/"
cfg_path = tools_dir + "../config.cfg"
config.read_config(cfg_path)    
print "config.game_root:",config.game_root
print "config.svn_root_dir",config.svn_root_dir
pid_file=tools_dir +"tools_pid"
svn_root_dir = config.svn_root_dir
server_update_dir=config.game_root + 'update/server/'
server_run_dir=config.game_root + 'run/server/'
svn_server_list=svn_root_dir + "server_list.txt"
server_list_path=server_update_dir + "server_list.txt"
host_id=config.host_id
upgrade_log_file='update_log.txt'

def get_svn_version(dir):
    cmd = "svn info %s| grep 'Last Changed Rev' | awk -F' '   '{print $4}'" % dir    
    version = get_cmd_display(cmd)[0].strip()
    return version
def get_cmd_display(cmd):
    ret =os.popen(cmd).readlines()
    return ret
def log(info):
    print info

def track():
    
    import StringIO
    fd = StringIO.StringIO()
    import traceback
    traceback.print_exc(file = fd)

    info = fd.getvalue()
    log(info)
def get_server_listinfo():
    server_listinfo = {}
    server_list = open(server_list_path).readlines()
    server_list = server_list[1:]

    print server_list
    for info in server_list:
        info = info.replace('\t'," ").strip()
        if  info == "":
            continue
        info = info.split()
        
        if info[0] == host_id:

            server_id=info[1]
            server_listinfo[server_id] = {"svn_dir":info[2]}
    return server_listinfo
