#!/bin/bash

#Script to update automatically every Friday at 11pm
#Crontab format would be the following:
#0 23 * * 5 /home/happy/scriptsKura/update_script.sh
#The script needs to generate a file with the date appended to file name
#The file needs to contain what was updated

#Script should run without user interactions

#Checks to see if the user is the root user
if [ $UID != 0 ]  
then
	echo "You are not a superuser";
exit 1;
fi

#update and upgrade commands
sudo apt update;
sudo apt upgrade -y;

#set current date to a format to use later
curDate=$(date +"%Y-%m-%d");

#grep the updates and log them into a text file
cat /var/log/dpkg.log | grep "$curDate.*\ installed\ ">log-$curDate.txt

exit 0;
