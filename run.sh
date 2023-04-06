# docker build -t pil-test .
rm -rf app/cards
docker run -it --rm -v $PWD/app:/app -w /app -e token=<> pil-test python main.py