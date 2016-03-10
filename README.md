ci-automation
=============

CI (Continuous Integration) setup automation scripts in Google Cloud Platform using [Fabric](http://www.fabfile.org/) and [Docker](https://www.docker.com/).

### Usage:

[TODO] To setup a master instance

`fab -H <master1> master`

[TODO] To setup slave instances

`fab -H <slave1,slave2> slave`

### master/backup

To use this, the instance's built-in service account should have `Read Write` access to Cloud Storage ([more info](https://cloud.google.com/docs/authentication#getting_credentials_for_server-centric_flow) at "Service Running in Compute Engine"; [howto](https://cloud.google.com/compute/docs/authentication#using))

`backup-data.sh` backups data from all master services and upload them to GCS

`download-latest.sh` downloads the latest (`*_data.tar.gz`) archive of all master services from GCS
