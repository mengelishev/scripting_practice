#!/bin/bash

# Считает количество директорий и количество файлов в них

IFS=$'\n'
target_dir="$1"
# Считает кол-во файлов
number_of_files=`find $target_dir -type f | wc -l`
# Считает кол-во директорий    
number_of_dirs=`find $target_dir -type d | wc -l`
echo "Количество файлов - $number_of_files "
echo "Количество директорий - $number_of_dirs "