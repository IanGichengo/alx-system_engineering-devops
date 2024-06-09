# fix the internal error on the server
  $php_rout = '/var/www/html/wp-settings.php'
  exec { 'replace_line':
    command => "sed -i 's/phpp/php/g' ${php_rout}",
    path    => ['/bin','/usr/bin']
  }
