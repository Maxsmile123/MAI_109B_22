import os
import argparse

# Задаём отслеживание заданного суффикса
ParserSyn = argparse.ArgumentParser(description = "Synonim")
ParserSyn.add_argument("suffix", type = str, help = "Suffix of file")
args = ParserSyn.parse_args()

# Получаем список всех файлов в текущей директории
files = os.listdir()

# Фильтруем файлы по суффиксу и числу связей
filtered_files = [f for f in files if f.endswith(args.suffix) and os.stat(f).st_nlink <= 1]

# Создаем синонимы для каждого файла
for f in filtered_files:
    # Получаем новое имя файла
    new_name = args.suffix[1:] + f.replace(args.suffix, '')
    # Создаем синоним
    os.symlink(f, new_name)
    
