# Small Proxy Cache Valid

NGINX [won't let you set a time less than one second for proxy_cache_valid](https://trac.nginx.org/nginx/ticket/1505) and of course they have their reasons.

However, it does not mean you can implement your own workaround, right?

This repository implements an idea by [@lucasrodcosta](https://github.com/lucasrodcosta). It consists in using the time when the request was made, so the cache key is built with the time you would set in the `proxy_cache_valid` directive.

If a request comes at time `t` the cache will be valid for `t + cache_time`.

## Why?

In low latency video streaming, some objects like variant manifests get updated in milliseconds, under 500ms. This might be a problem because NGINX does not allow you to set a cache time less than one second.

In scenarios with high load, even a small cache like 250ms will make a huge difference because you don't want to stress your backend with so many requests.

## Running

```sh
make run
```

## Testing

```sh
curl -v localhost:8080/test
```

Check out headers like `X-Cache-Status` and `X-Bucket-Time`.
