#!/usr/bin/python3
"""This script generates a .tgz archive"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """create a gzip archive"""

    dt = datetime.now()
    archive = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                            dt.month,
                                                            dt.day,
                                                            dt.hour,
                                                            dt.minute,
                                                            dt.second)
    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local("tar -cvzf {} web_static".format(archive)).failed:
        return None
    return archive
