# Puppet manifest to configure Nginx with a custom HTTP header

# Ensure the system is updated and Nginx is installed
exec { 'update-apt':
  command => '/usr/bin/apt-get update -y',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/bin/test -f /var/lib/apt/periodic/update-success-stamp',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['update-apt'],
}

# Add the custom HTTP header to Nginx configuration
file_line { 'add_custom_http_header':
  path    => '/etc/nginx/nginx.conf',
  match   => '^http {',
  line    => "http {\n    add_header X-Served-By \"${facts['networking']['hostname']}\";",
  require => Package['nginx'],
}

# Restart Nginx service to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File_line['add_custom_http_header'],
}
