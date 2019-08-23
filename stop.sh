#! /bin/bash
pid=$(ps x | grep 'alexwang/test/Scripts/python' | grep -v grep | awk '{print $1}')
echo $pid
kill $pid
