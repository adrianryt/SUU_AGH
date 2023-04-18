# SUU_AGH
## Środowiska Udostępniania Usług
### Kafka22 <br>
*Authors*: <br>
Adrian Ryt <br>
Dawid Grapa <br>
Kamil Kurowski <br>
Ryszard Pręcikowski <br>
Year, Group: **2023, pt 16:40** <br>

## 1. Introduction <br>
Kafka Operators on Kuberentes
Prepare evaluation test suite for kafka running on kuberentes behind the
operator. Select real life uses cases, with real-life workload. Perform test
with different Kafka setting. Select the most meaningful metrics for
evaluation

## 2. Theoretical background/technology stack <br>

Kafka Operators are software tools that help to automate the deployment, management, and operation of Apache Kafka clusters on Kubernetes platforms. Operators are essentially Kubernetes native controllers that extend the Kubernetes API to manage applications or services that are more complex than simple stateless or stateful workloads. By using Operators, developers and DevOps teams can simplify the deployment and management of Kafka clusters, reduce the operational overhead, and improve the resilience and scalability of their applications.

Kubernetes is a popular container orchestration platform that provides a framework for deploying, scaling, and managing containerized applications. Kubernetes uses a declarative API model to describe the desired state of the system and manages the deployment and operation of the applications based on this specification. Strimzi is a Kubernetes Operator that specializes in managing Apache Kafka clusters on Kubernetes. Strimzi provides a set of Kubernetes Custom Resource Definitions (CRDs) that can be used to define and manage Kafka clusters, topics, users, and other resources.

Amazon Elastic Kubernetes Service (EKS) is a managed Kubernetes service provided by AWS. EKS enables customers to easily deploy and operate Kubernetes clusters on AWS infrastructure without having to manage the underlying infrastructure themselves. EKS provides a fully managed, highly available, and scalable Kubernetes control plane that simplifies cluster deployment and management. EKS also integrates with other AWS services such as Elastic Load Balancing, Amazon S3, and Amazon RDS to provide a seamless experience for deploying and running containerized applications on AWS.

By using Strimzi on EKS, developers and DevOps teams can take advantage of the benefits of both technologies. Strimzi provides the Kafka Operator functionality, which simplifies the deployment and management of Kafka clusters on Kubernetes, while EKS provides a managed Kubernetes platform that eliminates the need to manage the underlying infrastructure. This combination enables developers and DevOps teams to focus on building and operating their applications rather than managing the infrastructure.

In summary, Kafka Operators on Kubernetes, such as Strimzi, provide a powerful way to simplify the deployment and management of Kafka clusters on Kubernetes platforms like EKS. By leveraging these technologies, organizations can improve the scalability and resilience of their applications while reducing the operational overhead of managing complex distributed systems.


To run Kafka on Kubernetes we will use:
- Kubernetes deployed on EKS (K8s on EKS)
- Kafka
- Zookeeper
- Strimzi
- Grafana

## 3. Case study concept description

### Introduction:
Apache Kafka is a popular distributed streaming platform used for real-time data feeds. Deploying and managing Kafka on Kubernetes can be challenging, but the Strimzi operator simplifies the process. In this case study, we will explore the preparation of an evaluation test suite for Kafka running on Kubernetes behind the Strimzi operator. We will select real-life use cases with real-life workloads. Additionally, we will use Grafana to visualize the data.

### Objectives:
The main objectives of this case study are:

- To prepare an evaluation test suite for Kafka running on Kubernetes behind the Strimzi operator.
- To select real-life use cases with real-life workloads and perform tests with different Kafka settings.
- To identify the most meaningful metrics for evaluation.
- To use Grafana to visualize the data and identify any issues or bottlenecks in the performance of Kafka on Kubernetes.

### Methodology:
To achieve the objectives of this case study, we will follow the below methodology:

- Identify the use cases: We will select real-life use cases with real-life workloads that are relevant to the organization's business operations.

- Prepare the test environment: We will set up a test environment consisting of a Kubernetes cluster, the Strimzi operator, Apache Kafka, and Grafana.

- Conduct the tests: We will execute the tests and collect the data on various performance metrics. We will use Grafana to visualize the data and identify any issues or bottlenecks.

- Analyze the results: We will analyze the test results to identify the most meaningful metrics for evaluation and identify any issues or bottlenecks that need to be addressed.

- Present the findings: We will present findings, including recommendations for improving the performance and scalability of Kafka running on Kubernetes behind the Strimzi operator.

### Conclusion:
This case study will provide valuable insights into the preparation of an evaluation test suite for Kafka running on Kubernetes behind the Strimzi operator. By selecting real-life use cases with real-life workloads, we can identify the most meaningful metrics for evaluation and make informed decisions to improve the performance and scalability of Kafka. Using Grafana to visualize the data will help us identify any issues or bottlenecks in the performance of Kafka on Kubernetes and make recommendations for improvement. 

## 4. Solution architecture

![image](https://user-images.githubusercontent.com/72798812/232866823-a0f99f49-7fe9-45b7-8613-97d196777fad.png)
![image](https://user-images.githubusercontent.com/72798812/232867080-74c10be3-e676-47aa-9ad6-2e02c913909a.png)



## 5. Environment configuration description
## 6. Installation method
## 7. How to reproduce - step by step
### 1. Infrastructure as Code approach
## 8. Demo deployment steps:
### 1. Configuration set-up
### 2. Data preparation
### 3. Execution procedure
### 4. Results presentation
## 9. Summary – conclusions
## 10. References
