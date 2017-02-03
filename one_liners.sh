# List all files in the CWD that contains 'X' in their body.
# Redirecting stderr and stdout to /dev/null, then echoing the relevant files by names.
for file in *; do if cat "$file" 2> /dev/null| grep "X" > /dev/null ; then echo "$file"; fi done

# List all files in the CWD whose names starts with 'X.Y'
# CWD, Files, terminate exec with \; 
find . -maxdepth 1 -type f -exec basename {} \; | grep ^X.Y

# Recursive find on all files starting with "X.Y" and contain "S"
find . -type f -name "X.Y*" -exec cat {} \; | grep "S" 





