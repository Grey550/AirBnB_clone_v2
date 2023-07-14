#!/usr/bin/python3
# script that distributes an archive to the web servers
# using the function do_deploy:
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Archiving static files"""
    date = datetime.now()
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                         date.month,
                                                         date.day,
                                                         date.hour,
                                                         date.minute,
                                                         date.second)    
    try:
        print("Packing web_static to {}".format(file))
        local("tar -cvzf {} web_static".format(file))
        size = os.stat(file).st_size
        print("web_static packed: {} -> {} Bytes".format(file, size))
    except Exception:
        file = None
    return file
