sudo docker build -t web .
sudo docker run --name my-container -d -p 80:80 web