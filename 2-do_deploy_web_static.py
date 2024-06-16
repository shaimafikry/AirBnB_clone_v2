#!/usr/bin/python3
# Fabric script (based on the file 1-pack_web_static.py)
# that distributes an archive to your web servers
# using the function do_deploy:
from fabric.api import *
from datetime import *
from fabric.contrib.files import exists
env.hosts = ['35.175.63.155', '54.226.26.233']


def do_deploy(archive_path):
    """to deploy an archeive"""
    # Returns False if the file at the path archive_path doesn’t exist
    if not exists(archive_path):
        return False
    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, f"/tmp/")
        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        archive = archive_path.split('/')[-1]
        archive_wt_ext = archive.split('.')[0]
        path = "/data/web_static/releases/"
        # create the archive path
        run(f"mkdir -p {path}{archive_wt_ext}/")
        run(f"tar -xzf /tmp/{archive} -c {path}{archive_wt_ext}/")
        # Delete the archive from the web server
        run(f"rm /tmp/{archive}")
        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")
        # Create a new the symbolic link /data/web_static/current
        # on the web server, linked to the new version of
        # your code /data/web_static/releases/archive filame without extension
        run(f"ln -sf {path}{archive_wt_ext}/ /data/web_static/current")
        return True
    except RuntimeError:
        return False
