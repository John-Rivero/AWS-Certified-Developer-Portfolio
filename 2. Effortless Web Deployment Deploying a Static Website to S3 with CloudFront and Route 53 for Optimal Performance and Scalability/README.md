
## Title: 2. Effortless Web Deployment: Deploying a Static Website to S3 with CloudFront and Route 53 for Optimal Performance and Scalability

## Created by: John Rivero

## Date: April 8, 2023


## Task

- Set up an AWS Infrastructure with Route 53 Geolocation for three regions (North America, Europe, Asia), and configure three Application Load Balancers with two EC2 instances each, connected with Route 53 for inter-regional load balancing.



## Step 1

- I Established an S3 bucket and upload the website's code.

![1](https://user-images.githubusercontent.com/81208412/230704603-b5f6a106-c56d-48b4-bfd2-1c2a730a6fa2.jpg)

- I Activated static website hosting and granted public access to the S3 bucket.

![2](https://user-images.githubusercontent.com/81208412/230704646-0b4708a6-9757-4a85-8cc6-89c38673b84a.jpg)
![3](https://user-images.githubusercontent.com/81208412/230704647-67a0f56a-30ce-481e-b81f-08ed9715d5d1.jpg)



## Step 2

- I set up the SSL certificate from the Certificate Manager and attached it to CloudFront.

![1](https://user-images.githubusercontent.com/81208412/230704730-fb76568b-f335-44c2-ae6c-55c44c107d03.jpg)

![2](https://user-images.githubusercontent.com/81208412/230704858-0e1b24c4-e7b3-4afa-85b3-0782c0dffffb.jpg)

- I also ensured that CloudFront's origin was directed to the S3 bucket containing the code for the website.

![3](https://user-images.githubusercontent.com/81208412/230704900-ca834b50-e910-4f3d-b18f-5b1c55ca23be.jpg)

















