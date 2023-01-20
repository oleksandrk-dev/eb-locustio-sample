locust-master: exec /usr/local/bin/locust -f locustfile.py --master
locust-follower: exec /usr/local/bin/locust -f locustfile.py --worker --master-host=$(<.masterIP)