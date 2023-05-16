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
![image](https://user-images.githubusercontent.com/30171233/232877082-568313d3-db9c-43c8-8a7c-fadc91fdf0d1.png)




## 5. Environment configuration description

To be able to run this project, you are obligatored to have installed:
- AWS cli
- Terrafom
- Kubectl

1. First step is to configure your AWS credentials. Please use `aws configure` and then enter all requested details.
2. Next step is to add session token to `~/.aws/credentials` file. It should look like:
```
[default]
aws_access_key_id = <access_key>
aws_secret_access_key = <secret_access_key>
aws_session_token = <session_token>
```

Now, your environment is prepared to move to the next step.

## 6. Installation method

To install all required packages etc., the best way is to use offical website for each of them.
- AWS cli - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- Terraform - https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
- Kubectl - https://kubernetes.io/docs/tasks/tools/

## 7. How to reproduce - step by step
### 1. Run project with terraform!
Important! Remember to first go through the step 5 and step 6! <br>
First you need to clone the repo.
```
git clone git@github.com:adrianryt/SUU_AGH.git
cd SUU_AGH
```
Next step is to run terraform commands.
```
cd resources/terraform
```
Update the cariables.tf file and run 

```
terraform init
terraform plan
terraform apply
```

Then you need to wait for the cluster and pods to build. <br>
After that check the connection and pods with kubectl.

```
kubectl get pods -n kafka
```

If everythink is running then the next step is to set the port forwarding for graphana

```
kubectl port-forward svc/grafana 3000:3000 -n kafka
```

The last step is to set up Prometheus <br>
 - Go to the localhost:3000 <br>
 - Login with credentials user: admin pass: admin <br>
 - Open 'Source' tab and select 'Data sources' then choose Prometheus <br>
 - In the url write `http://prometheus-operated:9090/` <br>
 - Import all jsons from resources directory  
![image](https://github.com/adrianryt/SUU_AGH/assets/72470330/2f764adf-42ca-4884-9710-7f199b4e4b0a)

## 8. Summary – conclusions

In conclusion, implementing Kafka on Kubernetes with Strimzi, Grafana, and Prometheus proved to be a highly effective solution for managing and monitoring data streaming pipelines. The combination of these technologies provided numerous benefits, such as scalability, resilience, and real-time visibility into the system's performance.

One key advantage of using Strimzi, an open-source Kubernetes Operator for Apache Kafka, was its seamless integration with Kubernetes. Strimzi simplified the deployment, configuration, and management of Kafka clusters on Kubernetes, automating tasks such as scaling, rolling upgrades, and topic management. This streamlined approach significantly reduced the operational overhead and allowed teams to focus on application development and data processing.

Grafana emerged as a powerful tool for visualizing Kafka metrics and monitoring the health of the Kafka clusters. With its intuitive dashboards and extensive plugin ecosystem, Grafana allowed us to gain valuable insights into the throughput, latency, and error rates of the Kafka infrastructure. This enabled us to proactively identify bottlenecks, optimize performance, and troubleshoot issues promptly.

The integration of Prometheus with Kafka, Strimzi, and Grafana further enhanced the observability capabilities of the system. Prometheus effectively collected and stored time-series data, enabling the creation of custom alerts and the analysis of historical trends. By leveraging Prometheus exporters provided by Strimzi, we were able to gather detailed Kafka-specific metrics, including consumer lag, partition health, and network utilization, thereby facilitating proactive monitoring and maintenance.

Overall, the combination of Kafka, Strimzi, Kubernetes, Grafana, and Prometheus provided a comprehensive solution for building and managing robust, scalable, and observable data streaming architectures. The integration of these technologies empowered teams to confidently develop, deploy, and monitor Kafka-based applications, ensuring efficient data processing and reliable messaging within complex distributed systems. The use of Strimzi simplified the management of Kafka clusters on Kubernetes, further enhancing the scalability and resilience of the overall solution.

## 9. References

[https://strimzi.io](Strimzi)
[https://aws.amazon.com/eks/](AWS EKS)
[https://prometheus.io](Prometheus)
[https://grafana.com](Grafana)

