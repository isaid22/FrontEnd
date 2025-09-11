## Considerations for Deployment in AWS Cloud

Cloud deployment requires some major changes. 

### Architecture Components
* Frontend (index.html): Should be deployed as a static website
* Backend (FastAPI/Python): Should be containerized and run as a service
* State persistence: Need to replace file-based storage with a database


### Frontend Deployment

index.html -> S3 + CloudFront

* Host the static files in S3 bucket
* Use CloudFront for global content delivery
* Enable CORS configurations
* Can handle thousands of requests easily


### Backend Deployment

FastAPI -> ECS/EKS -> Application Load Balancer -> Auto Scaling Group

* Containerize the FastAPI application using Docker
* Deploy to ECS (Elastic Container Service) or EKS (Elastic Kubernetes Service)
* Use Application Load Balancer (ALB) for distribution
* Set up auto-scaling based on CPU/memory metrics


### State Management

Replace the current JSON file storage with:
DynamoDB or Amazon RDS

* DynamoDB for serverless, high-throughput scenarios
* RDS (PostgreSQL) for more complex queries and transactions
* This removes the file system dependency and enables scaling


### Cross Account Access
To handle different AWS accounts:

Account A (Frontend):
- S3 + CloudFront
- IAM Role for S3

Account B (Backend):
- ECS/EKS Cluster
- VPC
- ALB
- DynamoDB/RDS
- IAM Role for services

### VPC Connectivity
Options for connecting different VPCs:

a. VPC Peering
b. Transit Gateway
c. API Gateway + Public Endpoints

* For this case, since the frontend is static, you don't need VPC connectivity
* Backend API can be exposed through API Gateway or ALB with proper security

### Scaling Strategy for 100 req/sec

Frontend Scaling:
- CloudFront handles this automatically

Backend Scaling:
- ALB: Set to handle 100+ connections
- ECS/EKS: Auto-scaling group with:
  - Minimum 2 containers
  - Scale up at 70% CPU
  - Scale down at 30% CPU

Database Scaling:
- DynamoDB: Set read/write capacity units
- RDS: Choose appropriate instance size

### Security Considerations

- WAF on CloudFront/ALB
- CORS policies
- SSL/TLS certificates
- Security Groups
- Network ACLs

### Recommended Changes to Current Code
1. State Management:
   - Replace file-based storage with database
   - Add connection pooling
   - Add retries and circuit breakers

2. API Layer:
   - Add rate limiting
   - Add request validation
   - Add proper error handling

3. Monitoring:
   - Add AWS X-Ray tracing
   - CloudWatch metrics
   - Custom metrics for bandit performance

### Deployment Steps

1. Frontend:
   - Create S3 bucket
   - Configure CloudFront
   - Deploy static files

2. Backend:
   - Create ECR repository
   - Build and push Docker image
   - Create ECS cluster
   - Configure ALB
   - Deploy service

3. Database:
   - Set up DynamoDB/RDS
   - Configure access policies

4. Monitoring:
   - Set up CloudWatch dashboards
   - Configure alarms
   - Set up logging