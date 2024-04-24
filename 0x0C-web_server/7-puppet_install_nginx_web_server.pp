# manifest.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Start Nginx service
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
}

# Template for Nginx configuration
# /etc/nginx/sites-available/default
# Replace "Hello World!" with the desired content
# Configure redirection for /redirect_me
# Set the return code to 301
# Reference: https://nginx.org/en/docs/http/ngx_http_rewrite_module.html
# Redirect to https://example.com/destination-page
# Replace "example.com/destination-page" with the actual destination URL
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "\
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;

    location /redirect_me {
        return 301 https://example.com/destination-page;
    }

    location / {
        return 200 'Hello World!';
    }
}
",
}
