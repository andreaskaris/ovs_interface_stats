#!/bin/bash

s=$1
if [ -z "$s" ]; then 
  echo "Provide a delay in seconds"
  exit 1
fi 

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

gather_interface_stats() {
  int=$1
  while true; do
    outfile="output/interface_statistics.${int}.out"
    echo "" >> $outfile
    date >> $outfile
    ./interface_statistics.py $int $s >> $outfile
  done
}

for int in `ovs-vsctl show | grep Port | egrep -o 'vhu[a-f0-9-]+'`; do
  gather_interface_stats $int &
done

sleep infinity
