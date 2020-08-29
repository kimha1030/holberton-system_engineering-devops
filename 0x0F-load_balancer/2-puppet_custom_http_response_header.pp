# Automate the task of create a custom HTTP header response
exec { 'http':
    command     => 'sudo apt-get -y update && sudo apt-get -y install nginx
            && sudo sed -i "27iadd_header X-Served-By: $hostname
always;" /etc/nginx/sites-available/default
            && sudo service nginx restart',
    provider    => shell,
}
