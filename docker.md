# How to save data within a docker container

a) create container from ubuntu image and run a bash terminal.

```
   $ docker run -i -t ubuntu:14.04 /bin/bash   #this is used to get the container terminal
```
b) Inside the terminal install vim
```
   # apt-get update
   # apt-get install vim
```
c) Exit the container terminal
```
   # exit
```
d) Take a note of your container id by executing following command :
```
   $ docker ps -a
```
e) save container as new image
```
   $ docker commit <container_id> new_image_name:tag_name(optional)
```
f) verify that you can see your new image with vim installed.
```
   $ docker images           
   $ docker run -it new_image_name:tag_name bash  
```

# To stop/remove all the docker containers
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

# To remove all the images (removes both unused and dangling images)
``` 
docker system prune -a
```

# How to get shell access to a nginx container

Example 1:
```
docker container run -it --name proxy nginx bash
# proxy is the container name
```
Example 2:
```
docker container run -it --name test1 ubuntu /bin/bash
# test1 is the container name
```

# Copying files to a container

Now let us copy files to the above nginx container
Here the name of the container is proxy

```
docker container run -it --name proxy nginx bash
docker cp ./prosper202/ proxy:/home/
docker start proxy
docker exec -it proxy /bin/bash
docker ps -a           # this lists all the containers
```

# If you want to run a shell script within a container

Create a Dockerfile

```
  FOM alpine:latest
  COPY script.sh /script.sh       #this copies the script file to the container root folder
  CMD ["/script.sh"]     #usually used to run commands within a container. 
                         # CMD is usually used to pass command and parameters that you want to execute in a container
                         # eg CMD ["echo" "How are you"]
```

Next step is to build the above Dockerfile which will convert it into an image

```
> docker build .
```

Next step is to run the docker image. It will run as a container.

```
docker run --name <name_of_the_container> <docker_image>
eg: docker run --name test 2bffd4a8b93a
```

# Creating a Dockerfile - Example

```
 FROM ubuntu:latest
 MAINTAINER Jeril CJ

 WORKDIR /home/site/                   
 RUN apt-get update
 RUN apt-get install -y nginx
 RUN apt-get install -y unzip
  
 ADD demo-site.zip /home/site/
  
 CMD ["date"]

```

To execute the above Dockerfile

```
docker build -t myimage:latest .
docker container run -it --name myimage3 myimage bash
```

# Creating a Dockerfile with Alpine Linux - Example

```
FROM alpine:3.4
MAINTAINER Jeril Jose jerilcj@gmail.com

RUN apk update
RUN apk add vim
RUN apk add curl
```

The above code creates 4 images for each RUN statement, 1 for alpine, next from update, then for vim, then for curl. This can increase the size of the image, so instead you can also write like this

Here there is only a single RUN statement, so it just creates one single image for each RUN statement

```
FROM alpine:3.4
MAINTAINER Jeril Jose jerilcj@gmail.com

RUN apk update && \
    apk add curl && \
    apk add vim && \
    apk add git
```

# Writing docker compose file

Install docker-compose
create a file called ```docker-compose.yml```

```
version: '3'
  
  services:
  
    web:
      image: nginx
      ports:
        - "8080:80"
    database:
      image: redis

```

To run the above docker-compose.yml file

```
docker-compose up -d   - to run the container
docker-compose down    - to stop all the containers
docker-compose up -d --scale database=4  - this will run redis in 4 containers
```

nginx will run on localhost:8080
