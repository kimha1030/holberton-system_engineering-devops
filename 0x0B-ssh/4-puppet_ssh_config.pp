# Task4: Change SSH config via puppet
file_line {
    'Turn off passwd auth':
        ensure => 'absent',
        path   => '/etc/ssh/ssh_config',
        line   => 'PasswordAuthentication no';
    'Declare identity file':
        ensure => 'absent',
        path   => '/etc/ssh/ssh_config',
        line   => 'IdentityFile ~/.ssh/holberton';
}
