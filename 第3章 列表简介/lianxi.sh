#!/bin/bash

# echo -n "Please input the number of chapter where you want to create. -> "
# read int

for (( i=1 ; i<=$2 ; ++i )); do
	echo $i
	temp="练习 $1.$i"
	echo $temp
	mkdir "$temp"
done
