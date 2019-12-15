#!/usr/bin/python3
# Fabric script that generates a .tgz archive
# from the contents of the web_static folder

from fabric.api import local
from datetime import datetime


def do_pack():
    """Converts web_static into a .tgz file"""
    time = datetime.now()
    file = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
    )
    local('mkdir -p versions')
    command = local('tar -cvzf ' + file + ' web_static')
    if command.succeeded:
        return file
    return None
