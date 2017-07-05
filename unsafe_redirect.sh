#!/bin/bash

# ##########################################
# Iterate over the account sites ->
# Check each if it has redirect active (by status code of either 301, 302 ->
# If so, grab the new location value ->
# Dig it up, see if under the service ->
# Return the relevant site if it's not -> 
# ##########################################

version="1.0"

counter=0

IFS=$'\n'

for domain in $(cat ./domains)
do
  curl -s -I -X GET ${domain} | head -8 > 'temp.txt'

  status_code=$(head -1 'temp.txt' | egrep -o '([0-9]){3}')
  location=$(grep "Location: " 'temp.txt' | cut -d " " -f2)
  
  declare "site$counter=$domain $status_code"
  varName=site$counter
  
  if [[ "$status_code" != "302" && "$status_code" != "301" ]];
  then
    echo "No redirect found on $domain ---- Nothing further to check ---- Response Code == ${status_code}"
    echo "-------------Site ${varName} Ended-------------"
  else
    echo "Found redirect on $domain ---- Gathering new location"
    location=$(grep "Location: " 'temp.txt' | cut -d " " -f2)
    echo "Checking if new location also has redirect, otherwise returning dig values for: $location"

    curl -s -I -X GET ${location} | head -8 > 'temp.txt'
    status_code=$(head -1 'temp.txt' | egrep -o '([0-9]){3}')
    if [[ "$status_code" != "302" && "$status_code" != "301" ]];
    then
        tmp_v=${location#*//}
	t_tmp_v=${tmp_v%%/*}
	echo "No more redirects, dig values for new location: ${t_tmp_v}"
	if dig $t_tmp_v +short | grep -q YourSearchString;
	then
	echo Service CNAME record was found
	else
	echo No Service CNAME record was found
	fi
    else
    echo "Too many redirects, no strict answer - requires manual check"
    fi
  echo "-------------Site ${varName} Ended-------------"
  fi
  ((counter++))
done
