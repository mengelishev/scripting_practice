#!/bin/bash

# Автоматическое разархивирование поддерживаемых архивов

filename="$1"

if [ ! -f $filename ]; then
    echo "File not found"
    exit 1
fi

if [ $filename == *.zip ]; then
    echo "Extracting zip:"
    unzip "$filename"
elif [ $filename == *.rar ]; then
    echo "Extracting rar:"
    unrar "$filename"
elif [ $filename == *.tar.gz ]; then
    echo "Extracting tar.gz:"
    tar -xzf "$filename"
else
    echo "Error: format not supported"
    exit 1
fi