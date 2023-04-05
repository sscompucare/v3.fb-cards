# docker build -t pil-test .
rm -rf app/cards
mkdir app/cards
docker run -it --rm -v $PWD/app:/app -w /app pil-test python main.py