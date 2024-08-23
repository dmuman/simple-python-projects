#!/bin/bash

PYTHON="python3" # версію можна змінити, якщо треба
PROGRAM="folderManipulations.py" # цю змінну змінювати не можна (це назва програми)

# перевірка, чи файл $PROGRAM існує, перед тим, як його викликати
if [ ! -e $PROGRAM ]
then
    echo "Помилка: $PROGRAM не існує."
    exit 1
fi
${PYTHON} ${PROGRAM} $@
