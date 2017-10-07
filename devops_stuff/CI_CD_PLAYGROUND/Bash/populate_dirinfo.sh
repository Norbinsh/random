#!/bin/bash - 
#===============================================================================
#
#          FILE: populate_dirinfo.sh
# 
#         USAGE: ./populate_dirinfo.sh dir1/ dir2/ dir3/
# 
#   DESCRIPTION: Quick fill for git to track empty directories
#===============================================================================

set -o nounset                              # Treat unset variables as an error

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for ARGDIR in "$@"
do
    if [ -d "$DIR/../$ARGDIR" ]; 
        then
            echo "Copying into $ARGDIR"
            cp $DIR/../.dirinfo $DIR/../$ARGDIR
        else
            echo "$ARGDIR not a legit directory"
    fi
done

