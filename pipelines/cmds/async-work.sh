#!/bin/sh
echo "$1: $(date)"
sleep $2
echo $1 to stdout
echo "$1: to sterr" >&2
echo $1 done
exit 0