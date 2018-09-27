#!/bin/bash
echo "Network Administration Panel -- Uptime Monitor "
echo -n "Enter IP address: "
read input >&2
echo "[$(date)] INPUT: $input"
cmd="ping -w 5 -c 2 \"$input\""
output=$(eval $cmd)
echo $output
