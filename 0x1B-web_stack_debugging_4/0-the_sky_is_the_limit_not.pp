# Task1: Change the limit of requests in NGINX
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/1000/g" /etc/default/nginx',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

exec {'change-status-nginx':
  command => 'service nginx restart',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
}

