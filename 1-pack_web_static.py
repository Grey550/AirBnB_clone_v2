#!/usr/bin/python3
# script that distributes an archive to the web servers, using the function do_deploy:
import os
from datetime import datetime
from fabric.api import local

def do_pack():
    """ Archiving static files """
    date = datetime.now()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date.year,
        date.month,
        date.day,
        date.hour,
        date.minute,
        date.second)

    if os.path.isdir("versions") is False:
       if local("mkdir -p versions").failed is True:
            return None

    if local("tar -czvf {} web_static".format(file)).failed is True:
            return None

    return file
