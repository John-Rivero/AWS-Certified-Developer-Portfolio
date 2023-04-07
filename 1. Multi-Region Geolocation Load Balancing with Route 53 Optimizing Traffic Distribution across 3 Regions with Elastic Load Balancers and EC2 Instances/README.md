
## Title: Multi-Region Geolocation Load Balancing with Route 53 Optimizing Traffic Distribution across 3 Regions with Elastic Load Balancers and EC2 Instances

## Created by: John Rivero

## Date: April 6, 2023


## Task

- Set up an AWS Infrastructure with Route 53 Geolocation for three regions (North America, Europe, Asia), and configure three Application Load Balancers with two EC2 instances each, connected with Route 53 for inter-regional load balancing.


## Step 1

- I designed an infrastructure diagram illustrating the configuration of Route 53 Geolocation for three distinct regions. Each region should include one Application Load Balancer and two EC2 instances.

![2  Route53 Diagram](https://user-images.githubusercontent.com/81208412/230541868-ffcd4d47-8ef0-454c-b27a-31e5996578df.jpg)


## Step 2

- I deployed two EC2 instances and one Application Load Balancer in each of the following regions: us-east-1, eu-central-1, and ap-southeast-1.


- ### us-east-1

![2  EC2-US-East-1](https://user-images.githubusercontent.com/81208412/230542770-b2e63a3a-1ae1-4e31-9bce-af3715efcd49.jpg)

![1  ELB-US-East-1](https://user-images.githubusercontent.com/81208412/230542783-1ffeeafc-ee3d-410d-bb2f-a3bcd763f355.jpg)


- ### eu-central-1

![2  EC2-EU-Central-1](https://user-images.githubusercontent.com/81208412/230542898-2db4957a-2fdc-4aa5-ac7f-04869fb2f413.jpg)

![1  ELB-EU-Central-1](https://user-images.githubusercontent.com/81208412/230542906-8aba542d-5ff7-472a-855e-c514ada127dc.jpg)


- ### ap-southeast-1

![2  EC2-AP-Southeast-1](https://user-images.githubusercontent.com/81208412/230542943-6f5f47b6-894c-4441-a34e-e4c29f3e7b3b.jpg)

![1  ELB-AP-Southeast-1](https://user-images.githubusercontent.com/81208412/230542960-e6a9294e-2e31-4f59-bb91-3d2eea1577ca.jpg)



## Step 3

- I configured three Route 53 records (using Geolocation) that utilize Alias to direct traffic to Application Load Balancers in us-east-1 (North America), eu-central-1 (Europe), and ap-southeast-1 (Asia). I also assigned appropriate locations to each record to align with their respective regions.

![1  Route53](https://user-images.githubusercontent.com/81208412/230543142-1b0248a5-7a13-4f08-8118-e6887a90f415.jpg)



## Step 4

- After setting up the infrastructure, I copied and pasted the record name (route53.johnrivero-projects.com) into a web search to confirm that the infrastructure was working properly.

![1  Result](https://user-images.githubusercontent.com/81208412/230544557-4f4becbf-4b26-4266-8a60-ee6492511bcb.jpg)

