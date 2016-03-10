#!/bin/sh

echo "Backing up jenkins data..."

docker run --rm --volumes-from master_jenkins_1 -v $(pwd):/backup ubuntu tar cvzf /backup/jenkins_data.tar.gz /var/jenkins_home

echo "Backing up nexus data..."

docker run --rm --volumes-from master_nexus_1 -v $(pwd):/backup ubuntu tar cvzf /backup/nexus_data.tar.gz /sonatype-work

echo "Backing up sonar data..."

docker run --rm --volumes-from master_sonar_1 -v $(pwd):/backup ubuntu tar cvzf /backup/sonar_data.tar.gz /opt/sonarqube/extensions /opt/sonarqube/lib/bundled-plugins

echo "Backing up postgres data..."

docker run --rm --volumes-from master_postgres_1 -v $(pwd):/backup ubuntu tar cvzf /backup/postgres_data.tar.gz /var/lib/postgresql

echo "Done!"
