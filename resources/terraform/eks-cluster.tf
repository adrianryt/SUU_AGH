module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "18.30.2"

  cluster_name    = local.cluster_name
  cluster_version = "1.25"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  create_iam_role = false
  iam_role_arn = var.role_arn

  enable_irsa = false

  eks_managed_node_group_defaults = {
    ami_type = "AL2_x86_64"

    attach_cluster_primary_security_group = true

    create_iam_role = false
    iam_role_arn = var.role_arn


    # Disabling and using externally provided security groups
    create_security_group = false
  }

  eks_managed_node_groups = {
    one = {
      name = "node-group-1"

      instance_types = ["t3.large"]

      min_size     = 2
      max_size     = 3
      desired_size = 2

      pre_bootstrap_user_data = <<-EOT
      echo 'foo bar'
      EOT

      vpc_security_group_ids = [
        aws_security_group.node_group_one.id
      ]
    }

  }

}

resource "aws_eks_addon" "add_ebs_csi" {
  cluster_name = local.cluster_name
  addon_name   = "aws-ebs-csi-driver"

  depends_on = [
    module.eks,
  ]
}

resource "null_resource" "kubectl_get_pods" {
  provisioner "local-exec" {
    command = "aws eks update-kubeconfig --region us-east-1 --name ${local.cluster_name} ${var.separator} kubectl create ns kafka ${var.separator} kubectl create -f https://strimzi.io/install/latest?namespace=kafka -n kafka ${var.separator} kubectl apply --wait -f https://raw.githubusercontent.com/adrianryt/SUU_AGH/main/resources/yaml/kafka-ephemeral.yaml -n kafka ${var.separator} kubectl apply --wait -f https://raw.githubusercontent.com/adrianryt/SUU_AGH/main/resources/yaml/kafka-metrics.yaml -n kafka ${var.separator} kubectl apply --wait -f https://raw.githubusercontent.com/adrianryt/SUU_AGH/main/resources/yaml/prometheus-operator-deployment.yaml -n kafka ${var.separator} kubectl apply --wait -f https://raw.githubusercontent.com/adrianryt/SUU_AGH/main/resources/yaml/prometheus-additional.yaml -n kafka ${var.separator} kubectl apply --wait -f https://raw.githubusercontent.com/adrianryt/SUU_AGH/main/resources/yaml/strimzi-pod-monitor.yaml -n kafka ${var.separator} kubectl apply --wait -f https://raw.githubusercontent.com/adrianryt/SUU_AGH/main/resources/yaml/prometheus-rules.yaml -n kafka ${var.separator} kubectl apply --wait --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.63.0/example/prometheus-operator-crd/monitoring.coreos.com_alertmanagerconfigs.yaml ${var.separator} kubectl apply --wait --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.63.0/example/prometheus-operator-crd/monitoring.coreos.com_alertmanagers.yaml ${var.separator} kubectl apply --wait --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.63.0/example/prometheus-operator-crd/monitoring.coreos.com_podmonitors.yaml ${var.separator} kubectl apply --wait --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.63.0/example/prometheus-operator-crd/monitoring.coreos.com_probes.yaml ${var.separator} kubectl apply --wait --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.63.0/example/prometheus-operator-crd/monitoring.coreos.com_prometheuses.yaml ${var.separator} kubectl apply --wait --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.63.0/example/prometheus-operator-crd/monitoring.coreos.com_prometheusrules.yaml ${var.separator} kubectl apply --wait --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.63.0/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml ${var.separator} kubectl apply --wait --server-side -f https://raw.githubusercontent.com/prometheus-operator/prometheus-operator/v0.63.0/example/prometheus-operator-crd/monitoring.coreos.com_thanosrulers.yaml ${var.separator} kubectl apply --wait -f https://raw.githubusercontent.com/adrianryt/SUU_AGH/main/resources/yaml/prometheus.yaml -n kafka ${var.separator} kubectl apply --wait -f https://raw.githubusercontent.com/adrianryt/SUU_AGH/main/resources/yaml/grafana.yaml -n kafka"
  }

  depends_on = [
    aws_eks_addon.add_ebs_csi,
  ]
}
