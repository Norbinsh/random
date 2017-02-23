#!/usr/bin/env bash
# List all files in the CWD that contains 'X' in their body.
# Redirecting stderr and stdout to /dev/null, then echoing the relevant files by names.
for file in *; do if cat "$file" 2> /dev/null| grep "X" > /dev/null ; then echo "$file"; fi done

# List all files in the CWD whose names starts with 'X.Y'
# CWD, Files, terminate exec with \; 
find . -maxdepth 1 -type f -exec basename {} \; | grep ^X.Y

# Recursive find on all files starting with "X.Y" and contain "S"
find . -type f -name "X.Y*" -exec cat {} \; | grep "S" 

# Grab all IP addresses recursively from all files in the CWD,
# knowing that there's a single IPv4 address per line
find . -type f -name "access.log*" -exec cat {} \; | grep -oP '(\d{1,3}\.){3}(\d{1,3})'

# Count the number of files in the current
# working directory.

find . -type f | wc | awk '{print $1}'







