#!/usr/bin/python3
""" script that creates a readme
port via hipporead and uploads it
to the repo passing it a txt with
the urls and the path to the repository
"""
from fabric.api import local
hipporead='python2 /home/holberton/hippo-readme/hipposcraper/hipporead.py'

def Readme():

    with open('readme_file.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            url = line.split(' ')[0]
            path = line.split(' ')[1]
            local("{} {}".format(hipporead, url))
            local("sudo cp README.md /home/holberton/holberton/{}".format(path))
            path2 = line.split(' ')[1].split('/')
            local("cd /home/holberton/holberton/{}/{} && \
                    sudo git add README.md &&\
                    sudo git commit -m 'I am the README' &&\
                    sudo git push \
                    ".format(path2[0], path2[1]))