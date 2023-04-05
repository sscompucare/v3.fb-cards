docker build -t pil-test .
rm -rf app/cards
mkdir app/cards
docker run -it --rm -v $PWD/app:/app -w /app -e token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiU2F2dmFzIiwiaWF0IjoxNjgwNjkyOTk4LCJleHAiOjE2ODMzMjI5OTh9.0lcHIPzrDV-V5g2T0Fg5xih5dE1kaxfsIgYIUreo68o pil-test python main.py