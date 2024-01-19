# Define a package resource for Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify to refresh the shell so that 'flask' command is available immediately
exec { 'Refresh Shell':
  command     => '/bin/true',
  refreshonly => true,
  subscribe   => Package['Flask'],
}
