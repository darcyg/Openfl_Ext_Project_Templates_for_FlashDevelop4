@ECHO OFF
..\cmd\wget.exe http://python-distribute.org/distribute_setup.py 
..\cmd\wget.exe --no-check-certificate https://github.com/pypa/pip/raw/master/contrib/get-pip.py 
python distribute_setup.py
python get-pip.py