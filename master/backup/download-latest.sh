#!/bin/sh

token=$(python ../../utils/access_token.py)

echo "Fetching jenkins data..."

curl -s -H "Authorization: Bearer ${token}" "https://storage.googleapis.com/javelin-ci-backup-test/jenkins_data.tar.gz"
echo "OK"

echo "Fetching nexus data..."

curl -s -H "Authorization: Bearer ${token}" "https://storage.googleapis.com/javelin-ci-backup-test/nexus_data.tar.gz"
echo "OK"

echo "Fetching sonar data..."

curl -s -H "Authorization: Bearer ${token}" "https://storage.googleapis.com/javelin-ci-backup-test/sonar_data.tar.gz"
echo "OK"

echo "Fetching postgres data..."

curl -s -H "Authorization: Bearer ${token}" "https://storage.googleapis.com/javelin-ci-backup-test/postgres_data.tar.gz"
echo "OK"

echo "Done!"
