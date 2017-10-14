docker build -t flask .
docker tag flask acobley/flask
docker push acobley/flask
docker stop flask
docker rm flask
docker run -p 80:5000 --name flask  acobley/flask