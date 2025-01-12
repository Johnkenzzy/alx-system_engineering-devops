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
  owner   => 'root',
  group   => 'root',
  mode    => '0600',
  require => File['/root/.ssh'],
}

# Add the configuration to refuse password authentication
file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/root/.ssh/config',
  line    => '    PasswordAuthentication no',
  match   => '^\s*PasswordAuthentication',  # Update if it already exists
  require => File['/root/.ssh/config'],
}

# Add the configuration to use the private key
file_line { 'Declare identity file':
  ensure  => present,
  path    => '/root/.ssh/config',
  line    => '    IdentityFile ~/.ssh/school',
  match   => '^\s*IdentityFile', # Update if it exits already
  require => File['/root/.ssh/config'],
}
