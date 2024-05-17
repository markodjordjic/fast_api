# fast_api

Examples of how to use FastAPI library.

# Running in Docker
```
docker image build --rm --file Dockerfile.testing --no-cache --tag fast_api_lessons .
docker container run --rm fast_api_lessons python -m unittest discover tests
```