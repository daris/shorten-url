# Shorten URL

This project is a minimal **URL Shortener API** built with **Django REST Framework (DRF)**.

It provides a simple way to create short links for long URLs and to resolve them back to their original form.


## Run project

```sh
docker compose up -d
```

## Generate short URL

### Option 1: Shell command
You can use curl shell command to call a request:

```sh
curl -X POST -H "Content-Type: application/json" http://localhost:8000/api/shorten/ -d '{"url": "http://example.com/very-very/long/url/even-longer"}'
```

Example response:

```json
{"short_url":"http://localhost:8000/short/H2U6ui/"}
```

### Option 2: Django Rest Framework Web UI

* Open http://localhost:8000/api/shorten/ in browser
* Paste in content field:

```json
{"url": "http://example.com/very-very/long/url/even-longer"}
``` 

* And click "POST"

* Example response:
```
POST /api/shorten/
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "short_url": "http://localhost:8000/short/MwNTGm/"
}
```

## Decode short URL back to full URL

Open in browser short_url included in JSON response. You will be redirected to original URL.


## Run tests

```sh
docker compose run --rm server pytest
```


## Lint code

```sh
docker compose run --rm server flake8
```