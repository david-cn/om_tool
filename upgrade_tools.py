#/usr/bin/python
import  config
import os
import sys
import time

from utils import *


def upgrade_one(host_id,svn_dir):
    update_dir=server_update_dir+ host_id + "/"
    run_dir = server_run_dir + host_id + "/"
    upgrade_pid_file=update_dir + "upgrade_pid"
    if os.path.exists(upgrade_pid_file):
        log("%s exist"% upgrade_pid_file)
        return
    try:  
        if os.path.exists(run_dir) == False:
            os.mkdir(run_dir)
        os.chdir(run_dir)
        upgrade_log_path = run_dir +  upgrade_log_file
        cmd = "echo %s upgrade begin >> %s" % (time.ctime(), upgrade_log_path)
        os.system(cmd)

        os.chdir(update_dir)
        pid=os.getpid()
  
        os.system("echo %d > %s"%(pid, upgrade_pid_file))
        cmd = "svn export ./ %s --force "%run_dir
       	os.system(cmd)
        cmd = "svn info | grep 'Last Changed Rev' | awk -F' '   '{print $4}'"

        version = get_cmd_display(cmd)[0].strip()
        print "version:",version
        os.chdir(run_dir)
        cmd = 'echo "%s upgrade end, Last Changed verison:%s" >> %s'%(time.ctime(),version,upgrade_log_path)
        os.system(cmd)

    except:
        track()     
    
    os.system("rm %s" % upgrade_pid_file)




def upgrade_all():
    try:
        os.chdir(server_update_dir)
        os.system("pwd")
        cmd = 'svn export %s'%svn_server_list

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
                upgrade_one(server_id, info[2])
    except:
        track()


if __name__=="__main__":
    upgrade_all()
