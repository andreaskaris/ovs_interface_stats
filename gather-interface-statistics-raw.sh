#!/bin/bash

s=$1
if [ -z "$s" ]; then 
  echo "Provide a delay in seconds"
  exit 1
fi 

while true;do
  echo ""
  date
  ovs-vsctl list interface | egrep '^name|^statistics'
  sleep $s
done >> output/gather-interface-statistics-raw.out
