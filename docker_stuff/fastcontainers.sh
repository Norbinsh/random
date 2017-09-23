#!/bin/bash

# Kill all sudo docker kill $(sudo docker ps -aq)
# Spam many ./script <IMAGEID>

COUNTER=10
until [ $COUNTER -eq 0 ]; do
	echo CONTAINER "#"  $COUNTER
	docker run -dit $1 /bin/bash
	let COUNTER-=1
done
