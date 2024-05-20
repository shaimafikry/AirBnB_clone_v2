#!/usr/bin/python3
# Fabric script that generates a .tgz archive
# from the contents of the web_static folder
# of your AirBnB Clone repo, using the function do_pack.
from fabric.api import *
from datetime import *


def do_pack():
    """archieve files"""
    # to get the date format
    file_name = "web_static_"+datetime.now().strftime("%Y%m%d%H%M%S")+".tgz"
    # make the versions dir
    local("mkdir -p versions")
    # print(file_name)
    result = local(f"tar -cvzf versions/{file_name} web_static")
    # print(result)
    if result:
        return file_name
    else:
        return None
