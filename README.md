# Distributed Locust Load Generator
This application is based on the [AWS provided package](https://www.github.com/awslabs/eb-locustio-sample) that utilizes Elastic Beanstalk to set up a distributed load testing infrastructure. There were changes made to make it work with the latest version of Locust. 

Please see the [documentation](https://docs.google.com/document/d/1b24em-IKi-mnuGxZAp-3-r_P6M_uHIYU-Tobj5_77GM/edit?usp=sharing)
## How to use it
### Create an environment
1. ssh to the bastion host
2. run ```cd eb-locustio-sample```
3. run ```./create_environment.sh <instance_type> <number of instances>``` e.g. ```./create_environment.sh c5.xlarge 2```

### Add more worker
1. run ```./scale.sh <number of current instances + number of new worker instances>``` e.g. if you already have 2 instances running and you need to add one more worker instance, you need to run ```./scale.sh 3```

### Terminate an environment
This will clean up all resources to avoid an incurred cost.
1. run ```./terminate_environment.sh```
