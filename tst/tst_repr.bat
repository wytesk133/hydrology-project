@echo off

rem %~1 script
rem %~2 input file
rem %~3 expected output
rem %~4 comparator

python %~1 %~2 output.txt
python %~4 %~3 output.txt
