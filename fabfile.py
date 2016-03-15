#!/usr/bin/env python
# encoding: utf-8

from fabric.api import cd, run, sudo
from fabric.contrib.files import exists
from fabric.operations import prompt

ARGS = ('NEXUS_RELEASE_SERVER_ID',
        'NEXUS_RELEASE_SERVER_UNAME',
        'NEXUS_RELEASE_SERVER_PASSWD',
        'NEXUS_SNAPSHOT_SERVER_ID',
        'NEXUS_SNAPSHOT_SERVER_UNAME',
        'NEXUS_SNAPSHOT_SERVER_PASSWD',
        'NEXUS_URL',
        'SONAR_LOGIN',
        'SONAR_PASSWD',
        'SONAR_JDBC_URL',
        'SONAR_JDBC_UNAME',
        'SONAR_JDBC_PASSWD',
        'SONAR_HOST_URL',
        'GCLOUD_SERVICE_ACCOUNT_EMAIL',
        'GCLOUD_SERVICE_ACCOUNT_AUTH_URL'
        )


# master instance setup
def master():
    sudo('apt-get install git')
    clone_ci_automation()
    install_deps("master")
    with cd('$HOME/docker-script/ci-automation/master'):
        run('sh backup/backup-data.sh')
        run('docker-compose up -d')


# slave instance setup
def slave():
    sudo('apt-get install git')
    clone_ci_automation()
    install_deps("slave")
    with cd('$HOME/docker-script/ci-automation/slave'):
        run('echo Note: The docker-compose.yml args must have correct values.',
            quiet=True)
        response = prompt('Is the docker-compose.yml already updated (y/N) ?')

        if response not in ['Y', 'y']:
            for arg in ARGS:
                response = prompt("Enter value for %s:" % arg)
                populate_slave_arg(arg + "_VAL", response)

    run('docker-compose up -d')


def clone_ci_automation():
    if not exists('$HOME/docker-script'):
        run('mkdir $HOME/docker-script')
        with cd('$HOME/docker-script'):
            run('git clone https://bitbucket.org/cloudsherpas/ci-automation')


def install_deps(ci_env):
    with cd('$HOME/docker-script/ci-automation'):
        if ci_env == "master":
            run('sh install.sh master')
        elif ci_env == "slave":
            run('sh install.sh')


def populate_slave_arg(arg_key, arg_val):
    run('sed -i "s|%s|%s|g" docker-compose.yml' % (arg_key, arg_val),
        quiet=True)

