#!/bin/bash

s=$1
if [ -z "$s" ]; then 
  echo "Provide a delay in seconds"
  exit 1
fi 

while true;do
ovs-appctl dpif-netdev/pmd-stats-clear
# wait <x> seconds
sleep $s
echo ""
date
ovs-appctl dpif-netdev/pmd-stats-show
done >> output/gather_pmd_stats.out
