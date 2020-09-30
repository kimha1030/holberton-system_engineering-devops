# Task1: Execute a command to fix a site wordpress
exec { 'fix-wordpress':
    command => 'sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php',
    path    => '/usr/bin',
}
