# OS configuration so that it is possible to login with the holberton user and open a file

# Increase hard file limit for user holberton.
exec { 'increase-hard':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for user holberton.
exec { 'increase-soft':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
