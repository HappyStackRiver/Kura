#!/bin/bash
#Rey Rivera
#
#
#
#connection timeout so ssh doesn't get stuck
timeout=30;

printf "Server testing\n";
printf "Testing server @ ip 174.129.78.68\n"

ssh -i Cali1.pem 174.129.78.68 'exit 0'
if [ $? == 0 ]  
then
	printf "SSH connection is possible\n"
	ssh -i Cali.pem ubuntu@174.129.78.68
	
else
	printf "SSH connection is not possible\n"
fi
exit 0;
