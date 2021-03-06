#!/bin/bash

if [ -z "$1" ]; then
    echo "You need to supply a search string..."
else
    processes=$(ps aux | grep $1 -i|grep -v grep | awk -F ' ' '{print $2}' | xargs)
    echo "Processes: "$processes
    while true; do
        read -ep "Are you sure you want kill all '$1' processes? [y/N] " yesno
        case $yesno in
            [Yy]* )
                echo 'Killing processes...'
                for i in $processes; do kill $i; done
                echo "Processes Killed: " $processes
                break;;
            * )
                echo "Skipped killing processes..."
                break;;
        esac
    done
fi

