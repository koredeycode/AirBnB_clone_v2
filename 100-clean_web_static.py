#!/usr/bin/python3
"""Distribute an archve to the web servers"""

from fabric.api import local, put, run, env, lcd, cd
import os

env.user = 'ubuntu'
env.hosts = ['54.160.126.209', '54.208.232.134']


def do_clean(number=0):
    """
    Delete out of date archives
    """
    number = 1 if int(number) == 0 else int(number)
    archives = sorted(os.listdir('versions'))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(archive)) for archive in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [arch for arch in archives if "web_static_" in arch]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
