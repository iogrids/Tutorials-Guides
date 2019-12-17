## Terraform

Terraform provider      - AWS, AZURE, GOOGLE, CHEF etc..
Resource - security group, ELB (Elastic load balancer) etc..
Terraform provisioner - file provisioner, chef provisioner, local-exec provisioner etc..If you want to execute something in the resource

### commands to execute a terraform
```
- plan 
- execute
- destroy
```
### Declaring variables in terraform
```
variable "image_id" {
  type = string
}
```

### You can declare a variable type of ```list``` like this as shown below
```
variable "azs" {
 type = "list"
 default = ["us-west-2a", "us-west-2b", "us-west-2c"]
}
```

examples:

```
variable "region"{
  default = "us-west-2"
}

variable "vpccidr"{
 default = "190.160.0.0/16"
}

variable "subnet_cidr"{
 default = "190.160.1.0/24"
}

```
To use the above variables declared in another terraform file

Example: To use the ```region``` variable which is declared above

```
provider "aws" {
  region  = "${var.region}"
}
```
### Terraform has a set of built in functions like ```ceil```, ```floor```, ```max```, ```min``` etc. Link shown below
```
https://www.terraform.io/docs/configuration/functions/
```

### Terraform snippets

Save the below file as ```main.tf```

To execute the below code enter the following commands

```
terraform init
terraform plan
terraform apply
```

```
provider "aws" {
  region                  = "us-east-2"
  access_key              = "***"
  secret_key              = "****"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  tags = {
    Name = "HelloWorld"  /*HelloWorld is the name of the ec2 machine */
  }
}
```

Terraform example to run bash scripts

```
############## To generate three VPS instances ###############
# Token variable
variable "hcloud_token" {
default = "hTbMfNee2ojYdFCYMHt49qQQqSGsQrYP7BnoGFWzbyIvZqsVuVKDJwuQ4kZ0DXZF"
}

# Define Hetzner provider
provider "hcloud" {
  token = "${var.hcloud_token}"
}

# Obtain ssh key data
data "hcloud_ssh_key" "ssh_key" {
  fingerprint = "6c:b5:4c:c9:c1:a2:b4:32:36:08:b8:6f:17:63:23:ab"
}

# Create an Ubuntu 16.04 server
resource "hcloud_server" "master" {
  name = "master"
  image = "ubuntu-16.04"
  server_type = "cx31"
  ssh_keys  = ["${data.hcloud_ssh_key.ssh_key.id}"]
  
  connection {
   type = "ssh"
   host = "${hcloud_server.master.ipv4_address}" 
   user = "root" 
   private_key = "${file("~/.ssh/id_rsa")}" 
  }
  
  provisioner "remote-exec" {
    inline = [
    
      "echo sleeping 30s to make sure server has been booted",
      "sleep 30",

      "sudo echo installing docker",
      "sudo apt-get update",
      "sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common",
      "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
      "sudo add-apt-repository \"deb https://download.docker.com/linux/$(. /etc/os-release; echo \"$ID\") $(lsb_release -cs) stable\"",
      "sudo apt-get update && sudo apt-get install -y docker-ce=$(apt-cache madison docker-ce | grep 17.03 | head -1 | awk '{print $3}')",
      
      "echo waiting for 30s...",
      "sleep 30",
      "sudo echo installing kubernetes",
      "sudo apt-get update && sudo apt-get install -y apt-transport-https",
      "curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -",
      "cat << EOF >/etc/apt/sources.list.d/kubernetes.list", 
      "deb http://apt.kubernetes.io/ kubernetes-xenial main", 
      "EOF",
      "sudo apt-get update",
      "sudo apt-get install -y kubelet kubeadm kubectl",

      "echo waiting for 30s...",
      "sleep 30",
      "echo deploying kubernetes with canal...",
      "kubeadm init --pod-network-cidr=10.244.0.0/16",
      "export KUBECONFIG=/etc/kubernetes/admin.conf",
      "kubectl apply -f https://docs.projectcalico.org/v3.1/getting-started/kubernetes/installation/hosted/canal/rbac.yaml",
      "kubectl apply -f https://docs.projectcalico.org/v3.1/getting-started/kubernetes/installation/hosted/canal/canal.yaml",

      "sudo groupadd ubuntu",
      "sudo groupadd admin",
      "sudo useradd -g ubuntu -G admin -s /bin/bash -d /home/ubuntu ubuntu",
      "sudo mkdir -p /home/ubuntu",
      "sudo cp -r /root/.ssh /home/ubuntu/.ssh",
      "sudo chown -R ubuntu:ubuntu /home/ubuntu",
      "echo \"ubuntu ALL=(ALL:ALL) NOPASSWD:ALL\" >> /etc/sudoers",

      "echo creating kube config file...",
      "sudo mkdir -p ~ubuntu/.kube",
      "sudo cp -i /etc/kubernetes/admin.conf ~ubuntu/.kube/config",
      "sudo chown ubuntu:ubuntu ~ubuntu/.kube/config",
    ]
  }
}

# Create an Ubuntu 16.04 server
resource "hcloud_server" "node1" {
  name = "node1"
  image = "ubuntu-16.04"
  server_type = "cx21"
  ssh_keys  = ["${data.hcloud_ssh_key.ssh_key.id}"]

  connection {
   type = "ssh"
   host = "${hcloud_server.node1.ipv4_address}" 
   user = "root" 
   private_key = "${file("~/.ssh/id_rsa")}" 
  }

  provisioner "remote-exec" {
    inline = [ 
      "echo sleeping 30s to make sure server has been booted",
      "sleep 30",
      "echo installing docker",
      "sudo apt-get update",
      "sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common",
      "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
      "sudo add-apt-repository \"deb https://download.docker.com/linux/$(. /etc/os-release; echo \"$ID\") $(lsb_release -cs) stable\"",
      "sudo apt-get update && sudo apt-get install -y docker-ce=$(apt-cache madison docker-ce | grep 17.03 | head -1 | awk '{print $3}')",

      "echo waiting for 30s...",
      "sleep 30",
      "echo installing kubeadm and kubectl",
      "sudo apt-get update && sudo apt-get install -y apt-transport-https",
      "curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -",
      "cat <<EOF >/etc/apt/sources.list.d/kubernetes.list",
      "deb http://apt.kubernetes.io/ kubernetes-xenial main",
      "EOF",
      "sudo apt-get update",
      "sudo apt-get install -y kubelet kubeadm kubectl",

      "echo adding user ubuntu....",
      "sleep 10",
      "sudo groupadd ubuntu",
      "sudo groupadd admin",
      "sudo useradd -g ubuntu -G admin -s /bin/bash -d /home/ubuntu ubuntu",
      "sudo mkdir -p /home/ubuntu",
      "sudo cp -r /root/.ssh /home/ubuntu/.ssh",
      "sudo chown -R ubuntu:ubuntu /home/ubuntu",
      "echo \"ubuntu ALL=(ALL:ALL) NOPASSWD:ALL\" >> /etc/sudoers",
    ]
  }
}

# Create an Ubuntu 16.04 server

/* 
resource "hcloud_server" "node2" {
  name = "node2"
  image = "ubuntu-16.04"
  server_type = "cx21"
  ssh_keys  = ["${data.hcloud_ssh_key.ssh_key.id}"]
} 
*/

# Output server IPs

output "server_ip_master" {
 value = "${hcloud_server.master.ipv4_address}"
}

output "server_ip_node1" {
 value = "${hcloud_server.node1.ipv4_address}"
}

/*
output "server_ip_node2" {
 value = "${hcloud_server.node2.ipv4_address}"
} 
*/


```
