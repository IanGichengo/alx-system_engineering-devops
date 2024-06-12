# Ensure the necessary directory exists for limits.d
file { '/etc/security/limits.d':
  ensure => directory,
}

# Increase file descriptor limits for the holberton user
file { '/etc/security/limits.d/holberton.conf':
  ensure  => 'file',
  content => "holberton soft nofile 4096\nholberton hard nofile 8192\n",
}

# Apply sysctl settings to ensure the system allows a high number of file descriptors
file { '/etc/sysctl.d/60-holberton.conf':
  ensure  => 'file',
  content => "fs.file-max = 100000\n",
}

# Ensure sysctl settings are applied
exec { 'apply_sysctl':
  command => '/sbin/sysctl -p /etc/sysctl.d/60-holberton.conf',
  refreshonly => true,
  subscribe => File['/etc/sysctl.d/60-holberton.conf'],
}

# Ensure pam_limits is configured to use the limits.d configuration
file_line { 'pam_limits':
  path => '/etc/pam.d/common-session',
  line => 'session required pam_limits.so',
  match => '^session\s+required\s+pam_limits.so',
}

file_line { 'pam_limits_noninteractive':
  path => '/etc/pam.d/common-session-noninteractive',
  line => 'session required pam_limits.so',
  match => '^session\s+required\s+pam_limits.so',
}
