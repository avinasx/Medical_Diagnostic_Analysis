#!/bin/bash

export temp_mysql_password="root"
export DEBIAN_FRONTEND=noninteractive 

debconf-set-selections <<< "mysql-server mysql-server/root_password password $temp_mysql_password"
debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $temp_mysql_password"
debconf-set-selections <<< "mysql-server-5.6 mysql-server/root_password password $temp_mysql_password"
debconf-set-selections <<< "mysql-server-5.6 mysql-server/root_password_again password $temp_mysql_password"

apt-get update
apt-get -y install mysql-server