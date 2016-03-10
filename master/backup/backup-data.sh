#!/bin/sh

now=$(date +%Y%m%d%H%M%S)
token=$(python ../../utils/access_token.py)
prefix=${PWD##*/}

echo "Backing up jenkins data..."

docker run --rm --volumes-from ${prefix}_jenkins_1 -v $(pwd):/backup ubuntu tar czf /backup/jenkins_data_${now}.tar.gz /var/jenkins_home

echo "Uploading to GCS..."
curl -s -H "Authorization: Bearer ${token}" -H "Content-Type: application/x-gzip" --data-binary @jenkins_data_${now}.tar.gz https://www.googleapis.com/upload/storage/v1/b/javelin-ci-backup-test/o?uploadType=media&name=jenkins_data_${now}.tar.gz
rm -f jenkins_data_${now}.tar.gz
echo "OK"

echo "Backing up nexus data..."

docker run --rm --volumes-from ${prefix}_nexus_1 -v $(pwd):/backup ubuntu tar czf /backup/nexus_data_${now}.tar.gz /sonatype-work

echo "Uploading to GCS..."
curl -s -H "Authorization: Bearer ${token}" -H "Content-Type: application/x-gzip" --data-binary @nexus_data_${now}.tar.gz https://www.googleapis.com/upload/storage/v1/b/javelin-ci-backup-test/o?uploadType=media&name=nexus_data_${now}.tar.gz
rm -f nexus_data_${now}.tar.gz
echo "OK"

echo "Backing up sonar data..."

docker run --rm --volumes-from ${prefix}_sonar_1 -v $(pwd):/backup ubuntu tar czf /backup/sonar_data_${now}.tar.gz /opt/sonarqube/extensions /opt/sonarqube/lib/bundled-plugins

echo "Uploading to GCS..."
curl -s -H "Authorization: Bearer ${token}" -H "Content-Type: application/x-gzip" --data-binary @sonar_data_${now}.tar.gz https://www.googleapis.com/upload/storage/v1/b/javelin-ci-backup-test/o?uploadType=media&name=sonar_data_${now}.tar.gz
rm -f sonar_data_${now}.tar.gz
echo "OK"

echo "Backing up postgres data..."

docker run --rm --volumes-from ${prefix}_postgres_1 -v $(pwd):/backup ubuntu tar czf /backup/postgres_data_${now}.tar.gz /var/lib/postgresql

echo "Uploading to GCS..."
curl -s -H "Authorization: Bearer ${token}" -H "Content-Type: application/x-gzip" --data-binary @postgres_data_${now}.tar.gz https://www.googleapis.com/upload/storage/v1/b/javelin-ci-backup-test/o?uploadType=media&name=postgres_data_${now}.tar.gz
rm -f postgres_data_${now}.tar.gz
echo "OK"

echo "Done!"
