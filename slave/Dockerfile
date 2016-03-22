FROM ubuntu:14.04

# install Oracle JDK 7, SSH, git, unzip, curl (and dependencies)
RUN apt-get install -yq software-properties-common

# mvn settings.xml environment variables
ARG NEXUS_RELEASE_SERVER_ID
ARG NEXUS_RELEASE_SERVER_UNAME
ARG NEXUS_RELEASE_SERVER_PASSWD

ARG NEXUS_SNAPSHOT_SERVER_ID
ARG NEXUS_SNAPSHOT_SERVER_UNAME
ARG NEXUS_SNAPSHOT_SERVER_PASSWD

ARG NEXUS_URL

ARG SONAR_LOGIN
ARG SONAR_PASSWD
ARG SONAR_HOST_URL

ARG GCLOUD_SERVICE_ACCOUNT_EMAIL
ARG GCLOUD_SERVICE_ACCOUNT_AUTH_URL

ARG DOWNLOAD_DIR=/home/jenkins/programs

RUN add-apt-repository -y ppa:webupd8team/java
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections

RUN apt-get update
RUN apt-get install -y openssh-server oracle-java7-installer git-core unzip curl

RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
RUN apt-get install -y nodejs

# create jenkins user
RUN useradd -m jenkins -s /bin/bash
# add password for jenkins user
RUN echo jenkins:jenkins | chpasswd

# set current user to jenkins
USER jenkins

RUN mkdir $DOWNLOAD_DIR
WORKDIR $DOWNLOAD_DIR

# configure gcloud
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-98.0.0-linux-x86_64.tar.gz
RUN tar -zxvf google-cloud-sdk-98.0.0-linux-x86_64.tar.gz -C /home/jenkins/programs
RUN /home/jenkins/programs/google-cloud-sdk/install.sh

ENV PATH $DOWNLOAD_DIR/google-cloud-sdk/bin:$PATH

RUN wget -O /home/jenkins/.service-account-auth.json $GCLOUD_SERVICE_ACCOUNT_AUTH_URL
RUN gcloud auth activate-service-account $GCLOUD_SERVICE_ACCOUNT_EMAIL --key-file /home/jenkins/.service-account-auth.json

# configure java
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle

# configure maven
RUN wget http://ftp.jaist.ac.jp/pub/apache/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz
RUN tar -zxvf apache-maven-3.3.9-bin.tar.gz -C /home/jenkins/programs

ENV M2_HOME /home/jenkins/programs/apache-maven-3.3.9

# create m2 directory and download boilerplate settings.xml
RUN mkdir /home/jenkins/.m2
RUN wget -P /home/jenkins/.m2 https://bitbucket.org/api/2.0/snippets/cloudsherpas/erBRR/HEAD/files/settings.xml

# populate settings.xml with nexus, sonarqube credentials
RUN sed -i "s|{release-server-id}|$NEXUS_RELEASE_SERVER_ID|g" /home/jenkins/.m2/settings.xml && sed -i "s|{release-server-uname}|$NEXUS_RELEASE_SERVER_UNAME|g" /home/jenkins/.m2/settings.xml && sed -i "s|{release-server-passwd}|$NEXUS_RELEASE_SERVER_PASSWD|g" /home/jenkins/.m2/settings.xml && sed -i "s|{snapshot-server-id}|$NEXUS_SNAPSHOT_SERVER_ID|g" /home/jenkins/.m2/settings.xml && sed -i "s|{snapshot-server-uname}|$NEXUS_SNAPSHOT_SERVER_UNAME|g" /home/jenkins/.m2/settings.xml && sed -i "s|{snapshot-server-passwd}|$NEXUS_SNAPSHOT_SERVER_PASSWD|g" /home/jenkins/.m2/settings.xml && sed -i "s|{nexus-url}|$NEXUS_URL|g" /home/jenkins/.m2/settings.xml && sed -i "s|{sonar.login}|$SONAR_LOGIN|g" /home/jenkins/.m2/settings.xml && sed -i "s|{sonar.password}|$SONAR_PASSWD|g" /home/jenkins/.m2/settings.xml && sed -i "s|{sonar.host.url}|$SONAR_HOST_URL|g" /home/jenkins/.m2/settings.xml

# configure sonarqube scanner
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-2.5.zip
RUN unzip sonar-scanner-2.5.zip -d /home/jenkins/programs

ENV SONAR_RUNNER_HOME /home/jenkins/programs/sonar-scanner-2.5

# add java, maven, sonarqube runner to PATH
RUN echo "export PATH=/usr/lib/jvm/java-7-oracle/bin:$DOWNLOAD_DIR/apache-maven-3.3.9/bin:$DOWNLOAD_DIR/sonar-scanner-2.5/bin:$PATH" >> /home/jenkins/.bashrc

# switch to root user for sshd configuration
USER root

# configure ssh
RUN mkdir /var/run/sshd

RUN sed -ri "s/UsePAM yes/#UsePAM yes/g" /etc/ssh/sshd_config
RUN sed -ri "s/Port 22/Port 2222/g" /etc/ssh/sshd_config

EXPOSE 2222

CMD ["/usr/sbin/sshd", "-D"]
