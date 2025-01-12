# SSH client configuration: Disable password authentication
exec { 'Turn off passwd auth':
  command => 'bash -c "echo PasswordAuthentication no >> /etc/ssh/ssh_config"',
  path    => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
  unless  => 'grep -q "^PasswordAuthentication no$" /etc/ssh/ssh_config',
}

# Set private key file location
exec { 'Declare identity file':
  command => 'bash -c "echo IdentityFile \'~/.ssh/school\' >> /etc/ssh/ssh_config"',
  path    => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
  unless  => 'grep -q "^IdentityFile ~/.ssh/school$" /etc/ssh/ssh_config',
}

# Enable public key authentication
exec { 'Turn on pubkey auth':
  command => 'bash -c "echo PubkeyAuthentication yes >> /etc/ssh/ssh_config"',
  path    => '/usr/bin/sbin:bin:/usr/local/bin',
  unless  => 'grep -q "^PubkeyAuthentication yes$" /etc/ssh/ssh_config',
}
