# docker-demo

ssh keygen -t rsa

python3 -m venv ~/.venv

source ~/.venv/bin/activate

docker rmi -f $(docker images -a -q)

docker build --tag=jarylngan/docker-demo:latest .

docker push jarylngan/docker-demo:latest

docker rmi -f $(docker images -a -q)

docker run -it jarylngan/docker-demo python app.py --sum 5
