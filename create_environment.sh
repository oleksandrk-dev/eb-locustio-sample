#!/bin/bash

eb init
eb create -i $1 --scale $2 --instance_profile aws-elasticbeanstalk-locust-role
