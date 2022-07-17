#!/bin/bash

echo "Enter your age"
read age
echo $age

if [ "$age" -ge 18 ]; then
	echo "Eligigble"
else
	echo "Not eligible"
fi

# if else statement examples
echo "Please enter the marks"
read marks
echo $marks
if [ "$marks" -ge 90 ]; then
	echo "Distiction"
elif [ "$marks" -le 35 ]; then
	echo "Failed"
else
	echo "Absent"
fi
