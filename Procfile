locust-master: /bin/bash -c "exec /usr/local/bin/locust -f locustfile.py --master"
locust-follower: /bin/bash -c "exec /usr/local/bin/locust -f locustfile.py --worker --master-host=$(<.masterIP)"