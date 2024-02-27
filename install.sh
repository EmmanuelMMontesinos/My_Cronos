#!/bin/bash

# Instalar Python (si no está instalado)
if ! command -v python3 &>/dev/null; then
    sudo apt update
    sudo apt install python3 -y
fi

# Instalar Pipenv (si no está instalado)
if ! command -v pipenv &>/dev/null; then
    sudo apt install pipenv -y
fi

# Instalar las dependencias del proyecto
pipenv install
