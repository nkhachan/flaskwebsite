sudo docker build -t web .
sudo docker run --name my-container -d -p 8080:8080 web