# Shorten URL

## Run project

```
docker compose up -d
```

# Generate short URL

```sh
curl -X POST -H "Content-Type: application/json" http://localhost:8000/api/shorten/ -d '{"url": "http://example.com/very-very/long/url/even-longer"}'
```

Open in browser short_url included in JSON response. You will be redirected to original URL.