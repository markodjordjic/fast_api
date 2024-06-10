# fast_api

Examples of how to use FastAPI library.

# Running in Docker
Build the image.
```
docker image build --rm --file Testing.Dockerfile --no-cache --tag fast_api_lessons .
```
Run tests with unittest
```
docker container run --rm fast_api_lessons python -m unittest discover tests
```
Run tests with coverage
```
docker container run --rm fast_api_lessons /bin/bash -c "coverage run -m unittest discover tests; coverage report -m --omit="*/test*""

```