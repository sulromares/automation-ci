#!/usr/bin/env python
# encoding: utf-8

from fabric.api import cd, run, sudo
from fabric.contrib.files import exists

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
    run('echo "export JAVA_HOME=/usr/lib/jvm/jdk1.7.0_80" >> $HOME/.bashrc')
    run('echo "PATH=$JAVA_HOME/bin:$PATH" >> $HOME/.bashrc')
    run('. $HOME/.bashrc')


def install_nginx():
    pass


def install_jenkins():
    pass


def install_nexus():
    pass


def install_sonarqube():
    ensure_dir_exists('/opt/sonar', use_sudo=True)
    ensure_dir_exists('$HOME/tools')

    with cd('$HOME/tools'):
        run('wget https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-5.3.zip')
        run('unzip sonarqube-5.3.zip')
        sudo('mv sonarqube-5.3 /opt/sonar')

    run('echo "export SONAR_HOME=/opt/sonar" >> $HOME/.bashrc')
    run('. $HOME/.bashrc')

# helper functions
def ensure_dir_exists(dir_path, use_sudo=False):
    cmd = run
    if use_sudo:
        cmd = sudo

    if not exists(dir_path, use_sudo):
        cmd('mkdir ' + dir_path)

