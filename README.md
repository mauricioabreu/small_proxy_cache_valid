# Small Proxy Cache Valid

NGINX [won't let you set a time less than one second for proxy_cache_valid](https://trac.nginx.org/nginx/ticket/1505) and of course they have their reasons.

However, it does not mean you can implement your own workaround, right?

This repository implements an idea by [@lucasrodcosta](https://github.com/lucasrodcosta). It consists in using the time when the request was made, so the cache key is built with the time you would set in the `proxy_cache_valid` directive.

If a request comes at time `t` the cache will be valid for `t + cache_time`.
