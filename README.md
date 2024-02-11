# memory_scripts


el formato del parametro de entrada en la grafica es este 


11/20/2023 15:50  | SAM.exe | 113285 | 22102624|24895560
11/20/2023 15:55  | SAM.exe | 113285 | 22108696|24895560
11/20/2023 16:00  | SAM.exe | 113285 | 22114764|24895560
11/20/2023 16:05  | SAM.exe | 113285 | 22120044|24895560
11/20/2023 16:10  | SAM.exe | 113285 | 22127624|24895560
11/20/2023 16:15  | SAM.exe | 113285 | 22136856|24895560
11/20/2023 16:20  | SAM.exe | 113285 | 22143720|24895560
11/20/2023 16:25  | SAM.exe | 113285 | 22150584|24895560
11/20/2023 16:30  | SAM.exe | 113285 | 22156392|24895560
11/20/2023 16:35  | SAM.exe | 113285 | 22160352|24895560
11/20/2023 16:40  | SAM.exe | 113285 | 22165104|24895560
11/20/2023 16:45  | SAM.exe | 113285 | 22170872|24961096
11/20/2023 16:50  | SAM.exe | 113285 | 22180904|24961096


obtenido con el script:
PS C:\tmp\git> cat .\monitor.sh    
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
