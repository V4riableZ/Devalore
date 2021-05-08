#!/usr/bin/env bash

if [ $(id -u) = 0 ];then
echo "root cannot run this script"
exit 1
fi

echo "Hello " $USER; sleep 2; clear
