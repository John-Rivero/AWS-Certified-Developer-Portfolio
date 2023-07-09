
## Title: ECS Fargate Deployment: Hosting Nginx with Docker Image from ECR

## Created by: John Rivero

## Date: July 8, 2023


## Task

- Deploy Nginx Docker image from the Elastic Container Registry (ECR) onto Amazon Elastic Container Service (ECS) using the Fargate launch type. Set up a simple webpage using Nginx as the web server.


## Step 1

- I have created an ECS infrastructure utilizing Fargate as the launch type. The infrastructure includes a load balancer that evenly distributes traffic among three tasks within a container instance. Additionally, I have set up a Service that retrieves the Nginx Docker image from Amazon ECR. 

![1](https://github.com/John-Rivero/AWS-DevOps-Portfolio/blob/main/6.%20Containerized%20Nginx%20Deployment%20Orchestrating%20Nginx%20with%20ECS%20Fargate/2.%20Result/1.jpg)


## Step 2

- I deployed two EC2 instances and one Application Load Balancer in each of the following regions: us-east-1, eu-central-1, and ap-southeast-1.


- ### us-east-1

![1](https://github.com/John-Rivero/AWS-DevOps-Portfolio/blob/main/6.%20Containerized%20Nginx%20Deployment%20Orchestrating%20Nginx%20with%20ECS%20Fargate/1.%20ECS/1.jpg)



## Step 3

- I configured three Route 53 records (using Geolocation) that utilize Alias to direct traffic to Application Load Balancers in us-east-1 (North America), eu-central-1 (Europe), and ap-southeast-1 (Asia). I also assigned appropriate locations to each record to align with their respective regions.

![1  Route53](https://user-images.githubusercontent.com/81208412/230543142-1b0248a5-7a13-4f08-8118-e6887a90f415.jpg)



## Step 4

- After setting up the infrastructure, I copied and pasted the record name (route53.johnrivero-projects.com) into a web search to confirm that the infrastructure was working properly.

![1  Result](https://user-images.githubusercontent.com/81208412/230544557-4f4becbf-4b26-4266-8a60-ee6492511bcb.jpg)

