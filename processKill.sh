#!/bin/bash
#Objective: Create a script that kills specific processes above a threshold
#
#Bugs:Currently the script is reliant on the PID being valid
#
#Script will not function correctly if PID is in invalid input
#Recommended to run as a super user
#
#There is an expected error when a process check happens at line 20
#due to the processes not using enough memory to register in the system
#
#Check system processes and sort, also store the line in input variable to use in a for loop to present necessary information

INPUT=$(ps -o pid,user,%mem,command ax | grep -v PID | sort -bnr -k3 | awk '/[0-9]*/{print $1 ":" $2 ":" $4}');

for i in $INPUT
do
	PID=$(echo $i | cut -d: -f1);
	OWNER=$(echo $i | cut -d: -f2);
	COMMAND=$(echo $i | cut -d: -f3);
	MEMORY=$(sudo pmap $PID | tail -n 1| awk '/[0-9]K/{print $2}');
	#If statement to show valid information and the data is formatted as well
	MEMCON=$((${MEMORY::-1} + 0))
	if [ "$MEMCON" -gt 500000 ]
	then
		echo "PID: $PID";
		echo "OWNER: $OWNER";
		echo "COMMAND: $COMMAND";
		echo "MEMORY: $MEMORY";
		echo "";
	fi

done
	printf "Enter the Process ID that you want to kill: ";
	read VICTIM;
	
	kill -9 $VICTIM;
	printf "\nProcess $VICTIM was killed";
exit 1;
