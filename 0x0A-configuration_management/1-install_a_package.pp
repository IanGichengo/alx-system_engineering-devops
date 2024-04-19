# install flask from pip3 using puppet
package { 'python3.8':
  ensure => '3.8.10',
}

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  path    => ['/bin', '/usr/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0" && /usr/bin/pip3 show Werkzeug | grep -q "Version: 2.1.1"',
}
