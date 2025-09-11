# FrontEnd
A repo with an example front end.

## Prerequisite:

```python
pip install fastapi uvicorn gunicorn orjson
```

## Steps

1. Launch Front End - In a terminal, launch:
```python
python -m http.server 8080
```

Then in a browser, open this URL: http://localhost:8080

2. Launch Back End (Fast API) - In a different terminal, launch:
```python
uvicorn myapp:app --reload --host 0.0.0.0 --port 8000
```

3. Recommender API Base URL - After log in, in the recommender API Base URL space, put:

```
http://localhost:8000/api/recommendation?user_id=u_003
```

Where u_003 is the user ID. (There are three users you may choose to use).

Then click "Fetch from API".


## Alternatives

There is another back end that has more feature added. It is in `Thompson` directory. To launch this back end:

go to Thompson directory and run the following command:

```python
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```


## Cloud Considerations

Deployment in public cloud requires some changes and considerations documented [here](Cloud_Consideration.md). 


## Docker Container

To build this application as a docker container:

```
# Build the Docker image
docker build -t thompson-bandit .

# Run the container
docker run -p 8000:8000 thompson-bandit
```