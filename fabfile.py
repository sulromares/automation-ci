#!/usr/bin/env python
# encoding: utf-8

from fabric import cd, run, sudo

# configuration

# main functions
def configure_env():
    create_tools_dir()
    install_jdk_7()
    install_nginx()
    install_nexus()
    install_sonarqube()
    install_jenkins()


def create_tools_dir():
    run('mkdir $HOME/tools')


def install_jdk_7():
    sudo('mkdir /usr/lib/jvm')
    with cd('$HOME/tools'):
        run('wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" \
        http://download.oracle.com/otn-pub/java/jdk/7u80-b15/jdk-7u80-linux-x64.tar.gz')
        run('tar -zxvf jdk-7u80-linux-x64')
        sudo('mv jdk1.7.0_80 /usr/lib/jvm')
    run('printf "%s\n" "JAVA_HOME=/usr/lib/jvm/jdk1.7.0_80" "PATH=$JAVA_HOME:$PATH" >> ~/.bashrc')
    run('. ~/.bashrc')


def install_nginx():
    pass


def install_jenkins():
    pass


def install_nexus():
    pass


def install_sonarqube():
    pass
