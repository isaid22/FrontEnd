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


