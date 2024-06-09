# 0-strace_is_your_friend.pp

# Ensure the /var/www/html directory exists with the correct permissions
file { '/var/www/html':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  require => Class['apache'],
}

# Ensure Apache service is running
service { 'apache2':
  ensure => 'running',
  enable => true,
  require => File['/var/www/html'],
}

# Restart Apache to apply any changes
exec { 'restart_apache':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
  subscribe   => File['/var/www/html'],
}
