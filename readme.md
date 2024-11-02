# productivity
This repository has a Python Flask application  which is running through docker container

# [From Setup to Deployment: Running a Flask App in Docker on Mac](https://dev.to/rajnishspandey/from-setup-to-deployment-running-a-flask-app-in-docker-on-mac-2fpp)

- run using Terminal or Docker Desktop
> `docker run -it --name rajnish_python python /bin/bash`

![rajnish_python container](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/27zk9do09ib5kk20tb67.png)

now go to Container in docker desktop and see if it's running.

- Open Container and explore it more by checking python version

![Docker container explore](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5no8zxyca673mgu6c6am.png)

### let's create a basic Python Flask web-app and run it through docker

- either you can create a new web app or just clone my repository [productivity](https://github.com/rajnishspandey/productivity.git)

> `git clone https://github.com/rajnishspandey/productivity.git`

***

Here I have created a project and it's in my local I want to create a new repository on github and push it from my Terminal

> `git init`

~~***in case you want to remove the git initialised you can run below command and do git init again to add.***~~

> ~~***rm -rf git***~~

> `git add .`

> `git commit -m 'Initial Commit'`

- I created a repository called productivity on github and will link it with my local/remote git

> `git remote set-url origin https://github.com/rajnishspandey/productivity.git`

> `git push -u origin master`

- now let's build the app and copy all the files to our container
> `docker build -t productivity-app .`

***command to check how many images we have in docker***
run `docker images` in Terminal

we can see now new images is created in the docker

![Docker New Images](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/wnpyn83h9hyftjenuivh.png)

Now we have to run it through container
- 
![images port assignment](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/19fgom9h573egyvmt3w2.png)

- click on ports 5500:5000
![running container](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/byya77g24o6uwmacln95.png)

it will redirect you to the browser and you should see the app running

***This UI can be different as it's possible that the code is updated***
![output](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qz3bq5fcgatlywx9a6y3.png)

***

# Deployment with docker Compose

### To learn more about Docker images, containers and basic Flask app deployment on docker [read blog](https://dev.to/rajnishspandey/from-setup-to-deployment-running-a-flask-app-in-docker-on-mac-2fpp)

In this blog we are going to deploy our [flask application](https://github.com/rajnishspandey/productivity.git) on Docker using docker compose file.

how to clone, create, deploy everything is already covered [here](https://dev.to/rajnishspandey/from-setup-to-deployment-running-a-flask-app-in-docker-on-mac-2fpp) please read and follow the instructions or you can just start by 

> `git clone https://github.com/rajnishspandey/productivity.git`

- `docker system prune -a` to delete all containers, images and caches.

> `docker compose up`

Docker Images
![Docker Images](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fysvvwijxavcn6tkq32e.png)

Docker Containers
![Docker Containers](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k7nyww2vgq4obssju9ei.png)

Running flask Application
***This UI can be different as it's possible that the code is updated***
![Running Application](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/xaqsqctbqg93hsafe67b.png)

***
# [Share docker image on docker hub](https://dev.to/rajnishspandey/share-docker-image-on-docker-hub-2d6h/edit)

- `docker login` run it in terminal if you are already logged in to [docker-hub](https://hub.docker.com/) it will authenticate if not just provide your credentials in Terminal and get authenticated.

- now run the command we have saved above from docker hub repository in Terminal `docker push rajnishspandey/productivity-docker`.

This will check our image and latest tag of the docker image and if found it will publish the image to docker-hub

Now let's check the image in docker-hub

![rajnishspandey/productivity-docker](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5vbn8xfn405mtz6r27x4.png)

![Image deleted](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2ru1gmsa8ftj4w1u5bus.png)

now run pull request

> `docker pull rajnishspandey/productivity-docker`

![Image created](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/2wsnezdrcdqj641ustpw.png)


### Learn how to 
#### - [From Setup to Deployment: Running a Flask App in Docker](https://dev.to/rajnishspandey/from-setup-to-deployment-running-a-flask-app-in-docker-on-mac-2fpp)

#### - [Deploy Flask app using docker Compose](https://dev.to/rajnishspandey/deploy-flask-app-using-docker-compose-4i81)

#### - [Share docker image on docker hub](https://dev.to/rajnishspandey/share-docker-image-on-docker-hub-2d6h/edit)

# [productivity-docker image on docker-hub for public use](https://hub.docker.com/r/rajnishspandey/productivity-docker)

***"Happy Learning"***

## some useful docker commands
- `docker images` to check all the images 
- `docker build -t <new-image-name>-app .` to build an images from your application
- `docker image rm <image-name>` - to delete image which is not in use
- `docker run -it --name <new_container> <base-image> /bin/bash` to create a new container and run it from base image. (here above we had python as base image)
- `docker image rm <image-name> -f` delete image which is in use forcefully
- `docker ps -a` to see all the containers running
- `docker container rm <container-name>` to delete container which is not running
- `docker container rm <container-name> -f` to delete container forcefully which is running
- `docker system prune -a` to delete all containers, images and caches.
- `docker compose up` to run docker compose file and created image
- `docker pull rajnishspandey/productivity-docker` to pull the latest image from docker-hub
- `docker push rajnishspandey/productivity-docker` - to push the latest image on docker-hub
- `docker login` - to login on docker-hub through terminal