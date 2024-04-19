# a manifest that kills a named killmenow
exec { 'kill_process':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
}
