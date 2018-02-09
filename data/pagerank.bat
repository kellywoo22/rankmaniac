@echo off
setlocal EnableDelayedExpansion
set /p texte=< input.txt  
set done=%texte:~0,1%

FOR /L %%A IN (1,1,15) DO (
  python pagerank_map.py < input.txt | sort | python pagerank_reduce.py > temp.txt
  python process_map.py < temp.txt | sort | python process_reduce.py > input.txt
)
