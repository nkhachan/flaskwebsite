docker build -t webisto .
docker run -d -p 5000:5000 webisto --expose 80
