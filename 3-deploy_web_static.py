#!/usr/bin/python3
# Fabric script that creates and distributes an archive to your web servers

from os import path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ['34.74.31.239', '35.237.24.35']
env.user = 'ubuntu'


def do_pack():
    """Converts web_static into a .tgz file"""
    time = datetime.now()
    local('mkdir -p versions')
    file = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second
    )
    command = local('tar -cvzf ' + file + ' ./web_static/')
    if command.succeeded:
        return file
    return None


def do_deploy(archive_path):
    """Deploy archive to web servers"""
    if not path.exists(archive_path) and not path.isfile(archive_path):
        return False

    temp = archive_path.split('/')
    temp0 = temp[1].split(".")
    f = temp0[0]

    try:
        put(archive_path, '/tmp')
        run("sudo mkdir -p /data/web_static/releases/" + f + "/")
        run("sudo tar -xzf /tmp/" + f + ".tgz" +
            " -C /data/web_static/releases/" + f + "/")
        run("sudo rm /tmp/" + f + ".tgz")
        run("sudo mv /data/web_static/releases/" + f +
            "/web_static/* /data/web_static/releases/" + f + "/")
        run("sudo rm -rf /data/web_static/releases/" + f + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/" + f +
            "/ /data/web_static/current")
    except Exception:
        return False

    return True

def deploy():
    """Deploy to all servers"""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
