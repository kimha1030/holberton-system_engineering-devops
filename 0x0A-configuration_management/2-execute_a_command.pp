# Task2: Execute a command
exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin',
}