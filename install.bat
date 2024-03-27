@echo off



echo Instalando Python
curl -o python-installer.exe https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe || call :Error "Error al descargar Python"
python-installer.exe /quiet TargetDir=C:\Python InstallAllUsers=1 PrependPath=1 || call :Error "Error al instalar Python"
del python-installer.exe

echo -------------------------------------------
echo Instalando Pip
python -m ensurepip --upgrade || call :Error "Error al instalar Pip"
echo -------------------------------------------


echo Instalando dependencias: pillow,bcrypt,reportlab,flask,flask_httpauth
pip install pillow
pip install bcrypt
pip install reportlab
pip install flask
pip install flask_httpauth
echo -------------------------------------------
echo pillow,bcrypt,reportlab,flask,flask_httpauth
echo -------------------------------------------


echo Instalacion completa.
pause
