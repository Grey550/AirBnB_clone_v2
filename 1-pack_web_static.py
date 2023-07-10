#!/usr/bin/python3
# script that distributes an archive to the web servers, using the function do_deploy:
import os
from datetime import datetim
from fabric.api import local
from fabric import task

@task
def do_pack():
    """ Archiving static files """
    if os.path.isdir(" /versions") is False:
        local("mkdir versions").failed:
            return None

    date = datetime.now()
    file = f"versions/web_static_{date.year}{date.month}{date.day}{date.hour}{date.minute}{date.second}.tgz"

    with cd("versions"):
        if local(f"tar -czvf {file} web_static").failed:
            return None

    return f"versions/{file}"
