#/usr/bin/python
import  config
import os
from utils import *


def update_one(host_id,svn_dir):
    cur_dir=server_update_dir+ host_id + "/"
    update_pid_file=cur_dir + "update_pid"
    if os.path.exists(update_pid_file):
        log("%s exist"% update_pid_file)
        return
    try:    
        if os.path.exists(cur_dir) == True:
            cmd = "svn up %s" % cur_dir
        else:
            os.chdir(server_update_dir)
            cmd = "svn co %s %s"%(svn_dir,cur_dir) 
            os.system(cmd)
            
        pid=os.getpid()
        os.system("echo %d > %s"%(pid, update_pid_file))
        os.system(cmd)
    except:
        track()     
    os.system("rm %s" % update_pid_file)

def update_all():

    try:
        cmd = 'svn export %s --force %s '%(svn_server_list,server_list_path)
        os.system(cmd)

        server_list = open(server_list_path).readlines()
        server_list = server_list[1:]

        print server_list
        for info in server_list:
            info = info.replace('\t'," ").strip()
            if  info == "":
                continue
            info = info.split()
            print info
            if info[0] == host_id:
                server_id=info[1]
                update_one(server_id, info[2])
    except:
        track()


if __name__=="__main__":
    update_all()
