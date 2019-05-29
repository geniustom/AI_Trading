@echo off
echo 開始編譯程式
#cd /d G:\program\python\src
python setup.py install
python setup.py py2exe
pause