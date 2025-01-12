# Ensure the .ssh directory exists with correct permissions
file { '/root/.ssh':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0700',
}

# Manage the SSH client configuration file
file { '/root/.ssh/config':
  ensure  => file,
  content => "Host *\n    PasswordAuthentication no\n    IdentityFile ~/.ssh/school\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  require => File['/root/.ssh'],
}
