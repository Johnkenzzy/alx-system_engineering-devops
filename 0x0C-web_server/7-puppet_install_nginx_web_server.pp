# Puppet manifest to install and configure Nginx with the specified requirements

# Install the Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;

    # Serve Hello World at the root
    location / {
        try_files $uri $uri/ =404;
        add_header Content-Type text/html;
        return 200 "Hello World!";
    }

    # Redirect /redirect_me to another page with 301 Moved Permanently
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
  ',
  notify  => Service['nginx'],  # Notify Nginx to reload if this file is updated
}

# Ensure the default Nginx site is enabled
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],  # Notify Nginx to reload if this link is created
}

