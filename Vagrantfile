#How to write a Vagrant file

This is a sample vagrant file. It installs docker, docker-compose, nodejs, postgresql, mongodb on a ubuntu machine. It also syncs local directory automatically with the directory inside the ubuntu virtual machine 

```
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network "private_network", ip: "10.0.0.3"
  config.vm.provision "shell", inline: <<-SHELL
      
    cd ~
   
    # Common Installations
    sudo apt-get update
    sudo apt-get install software-properties-common -y
    sudo apt-get install unzip -y    
       
    # Install docker
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install -y docker-ce 
    sudo usermod -aG docker ${USER}

    # Install docker-compose
    sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose    

    # Download and setup nodejs
    curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh
    sudo bash nodesource_setup.sh
    sudo apt-get install nodejs -y
    sudo apt-get install build-essential -y
  
    # Download and setup postgresql
    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib -y
   
    # Download and install MongoDB
    sudo apt-get install mongodb -y 
    sudo apt-get update
    sudo service mongodb start

    # Download and install terraform
    wget https://releases.hashicorp.com/terraform/0.12.3/terraform_0.12.3_linux_amd64.zip
    unzip terraform_0.12.3_linux_amd64.zip
    mv terraform /usr/local/bin    

  SHELL
  
  config.vm.synced_folder ".", "/home/vagrant/fullstack", type:"virtualbox"
  config.vm.network "forwarded_port", guest:4466, host:4466
  config.vm.network "forwarded_port", guest:5432, host:5432  
  config.vm.network "forwarded_port", guest: 80, host: 8081

end

```