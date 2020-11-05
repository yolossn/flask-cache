# flask-cache

A simple flask-cache which uses memcached.

This repository contains the code samples used in the blog which explains about setting the right requests and limits in kubernetes 

[Link to the blog](https://learnk8s.io/setting-cpu-memory-limits-requests)

## Endpoints

1. create

```bash
curl --location --request POST 'localhost:5000/cache/new' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"santhosh"
}'
```

2. retrieve

```bash
curl --location --request GET 'localhost:5000/cache/<id>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"santhosh"
}'
```
