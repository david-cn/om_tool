#coding:gbk
import ConfigParser


svn_root_dir = "" 
svn_user = ""
svn_passwd = ""
host_id =""
game_root=""

def read_config(file):
    global svn_root_dir
    global svn_user
    global svn_passwd
    global host_id
    global game_root
    config = ConfigParser.ConfigParser()
    config.readfp(open(file))
    svn_root_dir = config.get("svn","root_dir")
    svn_user = config.get("svn","user")
    svn_passwd = config.get("svn","passwd")
    host_id = config.get("common","host_id")
    game_root=config.get("common","game_root")
    print "game_root:",game_root
