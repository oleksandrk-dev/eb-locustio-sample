#!/bin/bash

echo -e "\n========================================\n\nApplication Configuration\n\n========================================"
eb init
echo -e "\n========================================\n\nEnvironment Configuration\n\n========================================"
eb create -i $1 --scale $2 --instance_profile aws-elasticbeanstalk-locust-role
