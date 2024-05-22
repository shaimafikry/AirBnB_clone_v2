#!/usr/bin/python3
from fabric.api import *
do_back = __import__('1-pack_web_static').do_back
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['35.175.63.155', '54.226.26.233']

# Write a Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy:
def deploy():
    # Call the do_pack() function and store the path of the created archive
    path = do_back()
    # Return False if no archive has been created
    if path is None:
        return False
    # Call the do_deploy(archive_path) function, using the new path of the new archive
    result = do_deploy(path)
   # Return the return value of do_deploy
    return result
