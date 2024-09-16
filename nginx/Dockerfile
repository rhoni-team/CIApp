FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
# COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/vhost.d/default
COPY custom.conf /etc/nginx/conf.d/custom.conf