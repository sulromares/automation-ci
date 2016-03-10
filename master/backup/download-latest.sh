#!/bin/sh

token=$(python ../../utils/access_token.py)
bucket="javelin-ci-backup-test"

echo "Fetching jenkins data..."

curl -sO -H "Authorization: Bearer ${token}" "https://storage.googleapis.com/${bucket}/jenkins_data.tar.gz"
echo "OK"

echo "Fetching nexus data..."

curl -sO -H "Authorization: Bearer ${token}" "https://storage.googleapis.com/${bucket}/nexus_data.tar.gz"
echo "OK"

echo "Fetching sonar data..."

curl -sO -H "Authorization: Bearer ${token}" "https://storage.googleapis.com/${bucket}/sonar_data.tar.gz"
echo "OK"

echo "Fetching postgres data..."

curl -sO -H "Authorization: Bearer ${token}" "https://storage.googleapis.com/${bucket}/postgres_data.tar.gz"
echo "OK"

echo "Done!"
