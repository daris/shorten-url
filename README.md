# Shorten URL

## Run project

```
docker compose up -d
```

## Generate short URL

### Shell command
You can use curl shell command to call a request:
```sh
curl -X POST -H "Content-Type: application/json" http://localhost:8000/api/shorten/ -d '{"url": "http://example.com/very-very/long/url/even-longer"}'
```

Example response:
```
{"short_url":"http://localhost:8000/short/H2U6ui/"}
```

### Django Rest Framework Web UI

* Open http://localhost:8000/api/shorten/ in browser
* Paste in content field:
```
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