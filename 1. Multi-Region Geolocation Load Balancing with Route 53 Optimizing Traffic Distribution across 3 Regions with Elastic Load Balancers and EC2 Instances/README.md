
## Title: Multi-Region Geolocation Load Balancing with Route 53 Optimizing Traffic Distribution across 3 Regions with Elastic Load Balancers and EC2 Instances

## Created by: John Rivero

## Date: April 6, 2023


## Task

- Set up an AWS Infrastructure with Route 53 Geolocation for three regions (us-east-1, eu-central-1, ap-southeast-1), and configure three Application Load Balancers with two EC2 instances each, connected with Route 53 for inter-regional load balancing.


## Step 1

- Design an infrastructure diagram illustrating the configuration of Route 53 Geolocation for three distinct regions. Each region should include one Application Load Balancer and two EC2 instances.

![2  Route53 Diagram](https://user-images.githubusercontent.com/81208412/230541868-ffcd4d47-8ef0-454c-b27a-31e5996578df.jpg)


## Step 2

- Deploy two EC2 instances and one Application Load Balancer in each of the following regions: us-east-1, eu-central-1, and ap-southeast-1.


- ### us-east-1

![2  EC2-US-East-1](https://user-images.githubusercontent.com/81208412/230542770-b2e63a3a-1ae1-4e31-9bce-af3715efcd49.jpg)

![1  ELB-US-East-1](https://user-images.githubusercontent.com/81208412/230542783-1ffeeafc-ee3d-410d-bb2f-a3bcd763f355.jpg)











## Result
