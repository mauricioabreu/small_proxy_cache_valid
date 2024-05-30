run:
	docker run --rm \
    	-p 8080:80 \
    	--name nginx \
    	-v $(PWD)/nginx.conf:/usr/local/openresty/nginx/conf/nginx.conf \
    	-v /tmp/nginx_cache:/var/cache/nginx \
    	openresty/openresty:alpine

reload:
	docker kill --signal=HUP nginx
