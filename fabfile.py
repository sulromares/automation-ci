#!/usr/bin/env python
# encoding: utf-8

from fabric.api import cd, run
from fabric.contrib.files import exists
from fabric.operations import prompt


# master instance setup
def master():
    clone_ci_automation()
    with cd('$HOME/docker-script/ci-automation/master'):
        run('docker-compose up -d')


# slave instance setup
def slave():
    clone_ci_automation()
    with cd('$HOME/docker-script/ci-automation/slave'):
        run('echo Note: The docker-compose.yml args must have correct values.', quiet=True)
        response = prompt('Is the docker-compose.yml already updated (y/N) ?')

        if response not in ['Y', 'y']:
            for arg in get_list_of_args():
                response = prompt("Enter value for %s:" % arg)
                populate_slave_arg(arg + "_VAL", response)

    run('docker-compose up -d')


def clone_ci_automation():
    if not exists('$HOME/docker-script'):
        run('mkdir $HOME/docker-script')
        with cd('$HOME/docker-script'):
            run('git clone https://bitbucket.org/cloudsherpas/ci-automation')


def populate_slave_arg(arg_key, arg_val):
    run('sed -i "s|%s|%s|g" docker-compose.yml' % (arg_key, arg_val), quiet=True)


def get_list_of_args():
    return ['NEXUS_RELEASE_SERVER_ID', 'NEXUS_RELEASE_SERVER_UNAME',
            'NEXUS_RELEASE_SERVER_PASSWD', 'NEXUS_SNAPSHOT_SERVER_ID',
            'NEXUS_SNAPSHOT_SERVER_UNAME', 'NEXUS_SNAPSHOT_SERVER_PASSWD',
            'NEXUS_URL', 'SONAR_LOGIN', 'SONAR_PASSWD', 'SONAR_JDBC_URL',
            'SONAR_JDBC_UNAME', 'SONAR_JDBC_PASSWD', 'SONAR_HOST_URL',
            'GCLOUD_SERVICE_ACCOUNT_EMAIL', 'GCLOUD_SERVICE_ACCOUNT_AUTH_URL'
            ]
