@echo off
setlocal EnableDelayedExpansion
set /p texte=< input.txt  
set done=%texte:~0,1%
echo !done!

while:
python