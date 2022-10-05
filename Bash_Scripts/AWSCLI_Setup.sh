#!/bin/bash
#Rey Rivera
#
#
#Install AWS CLI on the Jenkins EC2 and Configure
#
#Curl the zip file and download
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip";
#install unzip dependency just in case you don't have it
sudo apt install unzip;
#unzip the awsclient 
unzip awscliv2.zip;
#install
sudo ./aws/install;
#upgrade
sudo apt upgrade;
#return the version to see if it installed properly
aws --version;
#switch user
sudo su - jenkins -s /bin/bash;
#configure AWS
aws configure;
exit 0;