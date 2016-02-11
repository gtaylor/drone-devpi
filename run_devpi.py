#!/usr/bin/env python
"""
TODO: Write this.
"""

import drone
import subprocess


def select_server(server):
    subprocess.run(['devpi', 'use', server])


def login(username, password):
    subprocess.run(['devpi', 'login', username, '--password', password])


def select_index(index):
    subprocess.run(['devpi', 'use', index])


def upload_package(path):
    cmd = subprocess.Popen(
        ['devpi', 'upload', '--from-dir', '--no-vcs'],
        cwd=path)
    cmd.wait()


def main():
    payload = drone.plugin.get_input()
    vargs = payload["vargs"]

    print("VARGS", vargs)
    select_server(vargs['server'])
    login(vargs['username'], vargs['password'])
    select_index(vargs['index'])
    upload_package(payload['workspace']['path'])

if __name__ == "__main__":
    main()
