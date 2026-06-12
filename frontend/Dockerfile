FROM nginx:alpine

# Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom Nginx configuration which includes the reverse proxy logic
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy static frontend files to the Nginx serving directory
COPY index.html style.css app.js /usr/share/nginx/html/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
