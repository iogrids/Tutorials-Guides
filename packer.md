# Example 1 - Using Packer, Docker and shell together

First install packer

1. Inside the ```builders``` section you define what base image you are going to work with
2. Inside the ```provisioners``` section you will install the necessary packages
3. Inside the ```post-provisioners``` section you mention the image name, tag etc
4. To run the below code ```packer build template.json```
5. To run the converted image as a container ```docker run -it jerilcj3/packer-demo```

template.json

```
 {
     "builders": [
       {
         "type": "docker",
         "image": "ubuntu",
         "commit": true
       }],
     "provisioners": [
       {
        "type": "shell",
        "inline": [
          "apt-get -y update",
          "apt-get install -y software-properties-common",
          "apt-add-repository ppa:ansible/ansible",
          "apt-get -y update",
          "apt-get install -y ansible"]
      }],
      "post-processors": [
       {
          "type": "docker-tag",
          "repository": "jerilcj3/packer-demo",
          "tag": "0.1"
       }]
  }
```

# Example 2 - Using Packer, Ansible, Docker and shell together

1. create packer file called template.json
2. created ansible file called provision.yml
3. Build the packer file using ```packer build template.json```
4. To run the docker image build by packer ```docker run -i -t jerilcj3/packer-demo:0.1```

template.json

```
  {
      "builders": [
       {
         "type": "docker",
         "image": "nginx",
         "commit": true,
         "changes": [
           "EXPOSE 6379"
         ]
      }],
      "provisioners": [
      {
        "type": "shell",
        "inline": [
            "apt-get update",
            "apt-get install python -yq",
            "apt-get install vim"]
      },
      {
          "type": "ansible",
          "user": "root",
          "playbook_file": "provision.yml"
      }],
      "post-processors": [
       {
          "type": "docker-tag",
          "repository": "jerilcj3/packer-demo",
          "tag": "0.1"
       }]
  }

```

provision.yml

```
 ---
   - name: A demo to run ansible in a docker container
     hosts: all
     tasks:
       - name: Add a file to root's home dir
         copy:
           dest: /root/foo
           content: Hello World!
           owner: root
```
