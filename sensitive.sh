#!/bin/bash
#
#Rey Rivera
#
#Objective: 
#Create a user and add to a group named GitAcc
#
#Check for any sensitive information on a file
#After information check, give user ability to commit and add
#
#Functionality 1: User Creation and Addition to GitAcc group
#The script is under the assumption that GitAcc already exists as a group
#The script is also under the assumption that whoever is creating new users, will use proper username syntax; no spaces and no special characters
#The script will fail if a group name does not match the following exactly: GitAcc
#
#The script looks for a file in the directory where the script was ran
#If the script is not ran within the directory where the item is at, it will not find the item and will assume it does not exist
#The script only checks for phone numbers under the following syntax
#
#000-000-0000
#(000)000-0000
#0000000000
#The script only checks for social security numbers under following sytanx
#
#000-00-0000
#000 00 0000
#000000000
#
# Display menu and read input
printf "Security Clearance\n";
printf "\n";
printf "Options\n";
printf "0. Create and/or add user to GitAcc\n";
printf "1. Security File Check\n";
printf "Please Enter 0 or 1\n";
read select;
# If statements for different inputs
if [ $select -eq 0 ]
then
    printf "This will require you to either be a superuser or have sudo priviledges\n";
    printf "\nEnter the user name of the new user\n";
    read userName;
    #check to see if userName already exists
    varUser=$(grep -c $userName /etc/passwd);
    if [ $varUser -eq 1 ] 
    then
        printf "$userName already exists\n";
        printf "Checking to see if $userName is part of group GitAcc\n";
        #Store 1 if account is in GitAcc group or 0 if not
        accountVar=$(id -Gn $userName|grep -c GitAcc);
        if [ $accountVar -eq 0 ]
        then
            printf "$userName is not apart of GitAcc group\n"
            printf "Adding to GitAcc\n";
            #Add to GitAcc group
            sudo usermod -a -G GitAcc $userName;
            printf "$userName added to GitAcc\n";
            printf "Script Terminated\n";           
            exit 0;
        fi
        if [ $accountVar -eq 1 ]
        then
            printf "$userName is apart of GitAcc group\n";
            printf "Script Terminated\n";
            exit 0;
        fi

    fi
    if [ $varUser -eq 0 ] 
    then
        #creates user and adds home directory
        sudo useradd -m $userName;
        printf "$userName created as a user\n";
        #adds the user to the group named GitAcc
        sudo usermod -a -G GitAcc $userName;
        printf "$userName added to group GitAcc\n";
        printf "Script Terminated\n";
        exit 0;
    fi

fi
if [ $select -eq 1 ]
then
    #Display Menu
    printf "Secure File Checker\n"; 
    printf "This is a security checker for files\n";
    printf "Please input the exact name including extension of the file you want commit and add permissions for\n";
    read fileInput;

    if [ -f "$fileInput" ]
    then
        printf "$fileInput exists in this current directory\n";
        printf "The file will be scanned for any potential phone number and/or SSN\n";
        #find phone numbers with syntax of 000-000-0000
        countPhone1=$(grep -c '[0-9]\{3\}\-[0-9]\{3\}\-[0-9]\{4\}' $fileInput);
        #find phone numbers with syntax of (000)000-0000
        countPhone2=$(grep -c '([0-9]\{3\})[0-9]\{3\}\-[0-9]\{4\}' $fileInput);
        #find phone numbers with sytanx of 000 000 0000
        countPhone3=$(grep -c '[0-9]\{3\}\s[0-9]\{3\}\s[0-9]\{4\}' $fileInput);
        #find phone numbers with syntax of 0000000000
        countPhone4=$(grep -c '[0-9]\{10\}' $fileInput);
        totalPhone=$(($countPhone1+$countPhone2+$countPhone3+$countPhone4));

        #find SSN syntax of 000-00-0000
        countSSN1=$(grep -c '[0-9]\{3\}\-[0-9]\{2\}\-[0-9]\{4\}' $fileInput);
        #find SSN syntax of 000 00 0000
        countSSN2=$(grep -c '[0-9]\{3\}\s[0-9]\{2\}\s[0-9]\{4\}' $fileInput);
        #find SSN sytax of 000000000
        countSSN3=$(grep -c '[0-9]\{9\}' $fileInput);
        totalSSN=$(($countSSN1+$countSSN2+$countSSN3));

        #if statement for no errors
        if [ $totalPhone -eq 0 ] && [ $totalSSN -eq 0 ]
        then
            printf "There were no potential phone numbers found\n";
            printf "There were no potential SSN numbers found\n";
            running=true;
            while $running
            do
                #Display menu
                printf "Options:\n";
                printf "0. Add to GitHub\n";
                printf "1. Commit to GitHub\n";
                printf "2. Exit"
                printf "\n\nPlease enter your option. \nIf you enter any option outside of 0, 1, or 2, the program will default exit\n";
                read optionInput;
                    #Git Add
                if [ $optionInput -eq 0 ]
                then
                    printf "Adding file to GitHub\n";
                    git add $fileInput;
                    printf "$fileInput added\n"
                    #Git Commit
                    elif [ $optionInput -eq 1 ]
                    then
                    printf "Commit file to GitHub\n";
                    printf "Please enter the commit message for your commit statement\n";
                    read commitInput;
                    git commit -m "$commitInput" $fileInput;
                    printf "$fileInput committed\n";
                    #Neither Git Commit and Git Add were selected
                    elif [ $optionInput -ne 0 ] || [ $optionInput -ne 1 ]
                    then
                    printf "Exiting the program\n";
                    running=false;
                fi
            done
            exit 0
        else
            if [ $totalPhone -eq 0 ] && [ $totalSSN -gt 0 ]
            then
                #No phone numbers were found, only potential SSNs
                printf "There were only potential SSNs found. $totalSSN found\n";
                printf "Permissions to ADD and COMMIT have been denied\n"
                exit 0;
            fi

            if [ $totalPhone -gt 0 ] && [ $totalSSN -eq 0 ]
            then
                #No SSNs were found, only phone numbers
                printf "There were only potential phone numbers found. $totalPhone found\n";
                printf "Permissions to ADD and COMMIT have been denied\n"
                exit 0;
            fi

            if [ $totalPhone -gt 0 ] && [ $totalSSN -gt 0 ]
            then
                #Both suspected SSN's and Phone numbers were found.
                printf "There were both potential phone numbers and SSNs found. $totalPhone potential phone numbers found and $totalSSN SSNs found\n";
                printf "Permissions to ADD and COMMIT have been denied\n"
                exit 0;
            fi

        fi
    else
        printf "$fileInput does not exist in this directory or there was not an exact match\n";
        printf "Please run this script within the directory you have the file located in\n";
        exit 0;
    fi
fi
#it should not get to this point
exit 1;
