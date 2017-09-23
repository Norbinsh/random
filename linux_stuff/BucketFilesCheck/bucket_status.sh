#!/bin/bash -
#title           :bucket_status.sh
#description     :This script will retrieve logs metadata for a given directory in the s3 bucket
#author :shay elmualem
#date            :20172309
#version         :0.1
#usage :./bucket_status.sh 12345 8a9e3a81-2131-4f2a-82d1-c934bca9b00s https://logs1.xx.com/254_000000/logs.index
#notes           :Linux/Bash, requires curl
#bash_version    :4.3.11(1)-release
# ==============================================================================

# our temporarily output file, should be in the same directory of the script
temp_out_file="$(dirname $0)/logs_in_bucket.txt"

# empty our output file just in case, create if doesn't already exist
cat /dev/null > $temp_out_file

# allows for clean exit
die () {
    echo -e >&2 "$@"
    exit 1
}

# die if number of arguments doesn't equal 3
[ "$#" -eq 3 ] || die "
#########################################################
Please run the script with the following arguments:
APIID APIKEY LOGURI
Example Usage:
./bucket_status.sh 12345 8a9e3a81-2131-4f2a-82d1-c934bca9b00s https://logs1.xx.com/254_000000/logs.index
#########################################################
"

# retrieve currently available logs for the given URI, output to a file, together with the HTTP response code
bucketStatus() {
    curl --silent --write-out "\nHTTP_RESPONSE_CODE: %{http_code}\n" -k -u $1:$2 $3 > $4
}

# call the bucketStatus function
bucketStatus $1 $2 $3 $temp_out_file

# Grab status code line from the file
http_status_code=$(tail -1 $temp_out_file)

# Return the oldest log file, newest log file, total amount of logs
returnMetaData() {
    metaData[0]=$(head -1 $1) # First (oldest) log file
    metaData[1]=$(tail -3 $1 | head -1) # Last (Newest) log file
    metaData[2]=$(( $(cat $1 | wc -l) -2 )) # Total amount of log files, minus the \n + HTTP code below it
    # metaData[3]=$(tail -1 $1 ) # The request HTTP response code

    echo "OLDEST_LOG:" ${metaData[0]}
    echo "NEWEST_LOG:" ${metaData[1]}
    echo "TOTAL_LOGS:" ${metaData[2]}
}

# Making sure the curl (& Authentication)
if [[ $http_status_code == "HTTP_RESPONSE_CODE: 200" ]];
    then
        returnMetaData $temp_out_file
    else
        echo "Something went wrong, ${http_status_code} (Expecting 200)";
fi


