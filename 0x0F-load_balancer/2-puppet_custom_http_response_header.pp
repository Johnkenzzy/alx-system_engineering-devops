# Puppet manifest to configure Nginx with a custom HTTP header
class custom_http_header {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('custom_http_header/nginx_default.erb'),
    notify  => Service['nginx'],
  }
}

node default {
  include custom_http_header
}

server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    server_name _;

    location / {
        add_header X-Served-By '<%= @hostname %>';
        try_files $uri $uri/ =404;
    }
}
