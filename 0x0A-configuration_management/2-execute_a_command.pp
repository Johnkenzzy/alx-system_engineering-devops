# This manifest kills a process named killmenow
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
  path    => ['/usr/bin', '/bin'],
}
