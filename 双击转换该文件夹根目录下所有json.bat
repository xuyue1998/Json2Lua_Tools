@echo on

cd tools
%~dp0Python27\python.exe json2luaAll.py %BAT_DIR% %*

pause