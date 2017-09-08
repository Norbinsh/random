#!/bin/bash

version="1.0"

counter=0

IFS=$'\n'

for domain in $(cat ./domains)

do

  curl --connect-timeout 5 -s -I -X GET ${domain} | head -8 > 'temp.txt'

  status_code=$(head -1 'temp.txt' | egrep -o '([0-9]){3}')

  location=$(grep "Location: " 'temp.txt' | cut -d " " -f2)

  declare "site$counter=$domain $status_code"

  varName=site$counter

  if [[ "$status_code" != 3* ]];
    then
    echo "No redirect found on $domain Checking if CNAME exists <Response Code == ${status_code}>"
    if dig $domain | grep -q CNAMEVALUE;
        then
            echo Service CNAME record was found
    else
        echo No Service CNAME record was found
    fi
    echo "****${varName} Ended****"
  else
    echo "Found redirect on $domain ---- Gathering new location"
    location=$(grep "Location: " 'temp.txt' | cut -d " " -f2)
    if [[ "$location" == /* ]];
    then
        echo "Internal redirect found, checking for CNAME record for $domain"
        if dig $t_tmp_v +short | grep -q CNAMEVALUE;
            then
                echo Service CNAME record was found
            else
                echo No Service CNAME record was found
        fi
    else
        echo "Checking if new location also has redirect, otherwise returning dig values for: $location"
        curl --connect-timeout 5 -s -I -X GET ${location} | head -8 > 'temp.txt'
        status_code=$(head -1 'temp.txt' | egrep -o '([0-9]){3}')
        if [[ "$status_code" != 3* ]];
        then
            tmp_v=${location#*//}
            t_tmp_v=${tmp_v%%/*}
            echo "No more redirects, dig values for new location: ${t_tmp_v}"
            if dig $t_tmp_v +short | grep -q CNAMEVALUE;
                then
                    echo Service CNAME record was found
            else
                echo No Service CNAME record was found
            fi

        else
            echo "Too many redirects, no strict answer - requires manual check"
        fi
    fi
    echo "****${varName} Ended****"
  fi
  ((counter++))
done
