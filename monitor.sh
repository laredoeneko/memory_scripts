[root@temip84x ~]# cat monitor.sh

#!/bin/bash

 

 

if [ -z "$1" ]

then

        echo "The first argument is empty ....exit"

        exit 0

fi

 

process=$(pidof $1  )

 

if [ -z "process" ]

then

        echo "Unable to get the pid...exit"

        exit

fi

status=$(ps -q $process -o rss,vsz|tail -1 |sed 's/ /|/g')

now=$(date +'%m/%d/%Y %H:%M')

 

#logging to a file

printf "$now  | $process | $status\n"