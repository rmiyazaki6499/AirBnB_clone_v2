#!/usr/bin/python3
# Fabric script that deletes out-of-date archives

from fabric.api import env

env.hosts = ['34.74.31.239', '35.237.24.35']
env.user = 'ubuntu'


def do_clean(number=0):
    if number == 0 or number == 1:
        return True
    return False
