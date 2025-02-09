# This manifest ensure pip3 is installed
package { 'python3-pip':
  ensure => present,
}

# This manifest installs flask vision 2.1.0 from pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
