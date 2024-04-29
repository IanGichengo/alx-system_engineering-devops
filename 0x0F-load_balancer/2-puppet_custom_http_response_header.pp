class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

# Use an ERB template for the Nginx default site configuration
# The template should include the following configuration:
# add_header X-Served-By <%= @hostname %>;

node default {
  include nginx_custom_header
}
