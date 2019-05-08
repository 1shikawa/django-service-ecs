FROM nginx
# RUN rm -f /etc/nginx/conf.d/*
COPY ./nginx.conf /etc/nginx
# COPY ./django_nginx.conf /etc/nginx/conf.d/django_nginx.conf
COPY ./mime.types /etc/nginx/
COPY ./nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled
# RUN echo "daemon off;" >> /etc/nginx/nginx.conf