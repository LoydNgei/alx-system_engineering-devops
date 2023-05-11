# Puppet script to correct the internal server error(500)

$path_to_file = '/var/www/html/wp-settings.php'

exec {'fix_wp':
  provider => shell,
  command  => "sed -i 's/phpp/php/g' ${path_to_file}"
}
