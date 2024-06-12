# Increase ulimits for Nginx process
file { '/etc/security/limits.d/nginx.conf':
  ensure  => 'file',
  content => "nginx soft nofile 100000\nnginx hard nofile 100000\n",
}

# Apply sysctl settings for TCP tuning
file { '/etc/sysctl.d/99-nginx-tuning.conf':
  ensure  => 'file',
  content => "net.core.somaxconn = 65535
              net.core.netdev_max_backlog = 65535
              net.ipv4.tcp_max_syn_backlog = 4096
              net.ipv4.tcp_tw_reuse = 1
              net.ipv4.tcp_tw_recycle = 1\n",
}

# Ensure sysctl settings are applied
exec { 'apply_sysctl':
  command => '/sbin/sysctl -p /etc/sysctl.d/99-nginx-tuning.conf',
  refreshonly => true,
  subscribe => File['/etc/sysctl.d/99-nginx-tuning.conf'],
}

# Nginx configuration template
file { '/etc/nginx/nginx.conf':
  ensure  => 'file',
  content => template('nginx/nginx.conf.erb'),
}

# Service resource to manage Nginx
service { 'nginx':
  ensure     => 'running',
  enable     => true,
  subscribe  => File['/etc/nginx/nginx.conf'],
}

# Nginx configuration template (nginx/nginx.conf.erb)
file { '/etc/puppetlabs/code/environments/production/modules/nginx/templates/nginx.conf.erb':
  ensure  => 'file',
  content => @(EOF)
worker_processes auto;

events {
    worker_connections 1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;
    keepalive_timeout  65;

    # Buffer and timeout settings
    client_body_buffer_size 16k;
    client_header_buffer_size 1k;
    large_client_header_buffers 4 8k;
    client_max_body_size 8m;

    server {
        listen       80;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
EOF
}
