docker build -t webisto-test . -f Dockerfile.test
docker run -d -p 5000:5000 webisto-test --expose 5000