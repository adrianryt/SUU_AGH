# SUU_AGH
Środowiska Udostępniania Usług


Title page: <br>
Acronym - Kafka22 <br>
Authors: <br>
Adrian Ryt <br>
Dawid Grapa <br>
Kamil Kurowski <br>
Ryszard Pręcikowski <br>
Year, Group: 2023 pt, 16:40 <br>

Structure of the report:
Contents list
1. Introduction <br>
Kafka Operators on Kuberentes
Prepare evaluation test suite for kafka running on kuberentes behind the
operator. Select real life uses cases, with real-life workload. Perform test
with different Kafka setting. Select the most meaningful metrics for
evaluation

2. Theoretical background/technology stack <br>

Kafka Operators are software tools that help to automate the deployment, management, and operation of Apache Kafka clusters on Kubernetes platforms. Operators are essentially Kubernetes native controllers that extend the Kubernetes API to manage applications or services that are more complex than simple stateless or stateful workloads. By using Operators, developers and DevOps teams can simplify the deployment and management of Kafka clusters, reduce the operational overhead, and improve the resilience and scalability of their applications.

Kubernetes is a popular container orchestration platform that provides a framework for deploying, scaling, and managing containerized applications. Kubernetes uses a declarative API model to describe the desired state of the system and manages the deployment and operation of the applications based on this specification. Strimzi is a Kubernetes Operator that specializes in managing Apache Kafka clusters on Kubernetes. Strimzi provides a set of Kubernetes Custom Resource Definitions (CRDs) that can be used to define and manage Kafka clusters, topics, users, and other resources.

Amazon Elastic Kubernetes Service (EKS) is a managed Kubernetes service provided by AWS. EKS enables customers to easily deploy and operate Kubernetes clusters on AWS infrastructure without having to manage the underlying infrastructure themselves. EKS provides a fully managed, highly available, and scalable Kubernetes control plane that simplifies cluster deployment and management. EKS also integrates with other AWS services such as Elastic Load Balancing, Amazon S3, and Amazon RDS to provide a seamless experience for deploying and running containerized applications on AWS.

By using Strimzi on EKS, developers and DevOps teams can take advantage of the benefits of both technologies. Strimzi provides the Kafka Operator functionality, which simplifies the deployment and management of Kafka clusters on Kubernetes, while EKS provides a managed Kubernetes platform that eliminates the need to manage the underlying infrastructure. This combination enables developers and DevOps teams to focus on building and operating their applications rather than managing the infrastructure.

In summary, Kafka Operators on Kubernetes, such as Strimzi, provide a powerful way to simplify the deployment and management of Kafka clusters on Kubernetes platforms like EKS. By leveraging these technologies, organizations can improve the scalability and resilience of their applications while reducing the operational overhead of managing complex distributed systems.


To run Kafka on Kubernetes we will use:
Kubernetes deployed on EKS (K8s on EKS)
Kafka
Zookeeper (?) - not needed since 2.8.0 Kafka version
Strimzi (Strimzi) (?)
Grafana (?)

3. Case study concept description
4. Solution architecture
5. Environment configuration description
6. Installation method
7. How to reproduce - step by step
1. Infrastructure as Code approach
8. Demo deployment steps:
1. Configuration set-up
2. Data preparation
3. Execution procedure
4. Results presentation
9. Summary – conclusions
10. References
