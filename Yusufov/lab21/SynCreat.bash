#!/bin/bash
# Получаем суффикс из аргументов командной строки
suffix=$1

for file in *$suffix; do # перебираем все файлы с указанным суффиксом
    link_count=$(stat -c %h $file) # получаем количество связей у файла
    if [ $link_count -le 1 ]; then # проверяем, что количество связей больше 1
    # Получаем имя файла без суффикса
    filename=${file%.$suffix}
    # Получаем новое имя файла с переставленным суффиксом
    new_filename=${suffix//./}${filename}
    # Создаём новый файл-синоним
    touch $file $new_filename
    fi
done

echo "Готово!"
