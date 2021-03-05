# docker-demo

Simple functions that sums all the numbers from 0 to n

## Pull and run the image from dockerhub

docker run -it jarylngan/docker-demo python app.py --sum 5

## To build the image and push to dockerhub from scratch

### Remove all images from docker image ls

docker rmi -f $(docker images -a -q)

### Git clone this repo

git clone <repo>
  
### Build image (use your own account name and path)

docker build --tag=jarylngan/docker-demo:latest .

### Push Image to dockerhub
docker push jarylngan/docker-demo:latest


