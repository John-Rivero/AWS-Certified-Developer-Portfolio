
## Title: Containerized Nginx Deployment Orchestrating Nginx with ECS Fargate

## Created by: John Rivero

## Date: July 8, 2023


## Task

- Create a basic website by deploying the Nginx Docker image stored in the Elastic Container Registry (ECR) using ECS Fargate.


## Step 1

- I have created an ECS infrastructure utilizing Fargate as the launch type. The infrastructure includes a load balancer that evenly distributes traffic among three tasks within a container instance. Additionally, I have set up a Service that retrieves the Nginx Docker image from Amazon ECR. 

![1](https://github.com/John-Rivero/AWS-DevOps-Portfolio/blob/main/6.%20Containerized%20Nginx%20Deployment%20Orchestrating%20Nginx%20with%20ECS%20Fargate/2.%20Result/1.jpg)



## Step 2

- I have set up two security groups: the first one permits all inbound traffic on port 80 for the application load balancer, while the second one allows inbound traffic exclusively from the security group associated with the application load balancer.

![1](https://github.com/John-Rivero/AWS-DevOps-Portfolio/blob/main/6.%20Containerized%20Nginx%20Deployment%20Orchestrating%20Nginx%20with%20ECS%20Fargate/1.%20ECS/1.jpg)



## Step 3

- I have established an ECS Cluster using Fargate as the launch type.

![2](https://github.com/John-Rivero/AWS-DevOps-Portfolio/blob/main/6.%20Containerized%20Nginx%20Deployment%20Orchestrating%20Nginx%20with%20ECS%20Fargate/1.%20ECS/2.jpg)



## Step 4

- I have created a task definition that utilizes the Image URI from the ECR repository for Nginx.

![3](https://github.com/John-Rivero/AWS-DevOps-Portfolio/blob/main/6.%20Containerized%20Nginx%20Deployment%20Orchestrating%20Nginx%20with%20ECS%20Fargate/1.%20ECS/3.jpg)



## Step 5

- I have configured a service that launches three tasks within a container instance.

![4](https://github.com/John-Rivero/AWS-DevOps-Portfolio/blob/main/6.%20Containerized%20Nginx%20Deployment%20Orchestrating%20Nginx%20with%20ECS%20Fargate/1.%20ECS/4.jpg)



## Step 6

- I have configured the Load Balancer, which was created during the service creation, to utilize the security group that permits all inbound traffic on port 80.

![5](https://github.com/John-Rivero/AWS-DevOps-Portfolio/blob/main/6.%20Containerized%20Nginx%20Deployment%20Orchestrating%20Nginx%20with%20ECS%20Fargate/1.%20ECS/5.jpg)



## Step 7

- I obtained the DNS name of the Application Load Balancer to verify if the simple web page served by Nginx is working properly, and it is indeed working correctly.

![3](https://github.com/John-Rivero/AWS-DevOps-Portfolio/blob/main/6.%20Containerized%20Nginx%20Deployment%20Orchestrating%20Nginx%20with%20ECS%20Fargate/2.%20Result/3.jpg)