FROM nginx

RUN mkdir -p /nginx

#COPY nginx.conf /etc/nginx/conf.d
#COPY nginx.conf /app/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
#COPY nginx.conf /etc/nginx/nginx2.conf
#/etc/nginx/conf.d miejce w kontenerze gdzie jest default.config

#RUN rm /etc/nginx/conf.d/default.conf

#RUN ln -s /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf

#EXPOSE 80

#FROM nginx:1.14

# Remove the default NGINX configuration file
#RUN rm /etc/nginx/conf.d/default.conf

# Create the /app/nginx directory inside the container
#RUN mkdir -p /app/nginx

# Copy nginx.conf from the host to the container
#COPY nginx.conf /app/nginx/nginx.conf

# Link the custom nginx.conf from /app/nginx/nginx.conf
# to the appropriate directory in the container
#RUN ln -s /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf
#RUN ln -s /etc/nginx/conf.d/default.conf /app/ninx/nginx.conf

EXPOSE 80
