# 2-puppet_custom_http_response_header.pp
# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define file paths
$file_nginx_conf = '/etc/nginx/nginx.conf'
$file_nginx_default = '/etc/nginx/sites-available/default'

# Define custom HTTP header configuration
$hostname = $::hostname
$http_header_config = "
    add_header X-Served-By $hostname;
"

# Configure custom HTTP header in Nginx configuration
file { $file_nginx_conf:
  ensure  => present,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

# Configure custom HTTP header in Nginx default site configuration
file { $file_nginx_default:
  ensure  => present,
  content => template('nginx/default_site.conf.erb'),
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => running,
  enable  => true,
}
