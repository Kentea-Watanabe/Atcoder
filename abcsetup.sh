#!/bin/bash
# ABCの219番を解きたい場合 -> ./abcsetup.sh 219 (Linux)
# ABCの219番を解きたい場合 -> bash abcsetup.sh 219 (Windows)

if [ $# -ne 1 ]; then
  echo "Usage: $0 2xx" 1>&2
  exit 1
fi

if ! [[ "$1" =~ ^[1-9][0-9]{,2}$ ]]; then
  echo "Usage: $0 2xx (x=[0-9])" 1>&2
  exit 1
fi

if [ ! -e ABC ]; then
  echo "Error: directory 'ABC' not exists." 1>&2
  exit 1
fi

mkdir -p ABC/$1
mkdir -p ABC/$1/C
mkdir -p ABC/$1/PY

cp -n template.cpp ABC/$1/C/a.cpp
cp -n template.cpp ABC/$1/C/b.cpp
cp -n template.cpp ABC/$1/C/c.cpp
cp -n template.cpp ABC/$1/C/d.cpp
cp -n template.cpp ABC/$1/C/e.cpp
cp -n template.cpp ABC/$1/C/f.cpp
cp -n template.cpp ABC/$1/C/g.cpp
cp -n template.cpp ABC/$1/C/h.cpp

cp -n template.py ABC/$1/PY/a.py 
cp -n template.py ABC/$1/PY/b.py
cp -n template.py ABC/$1/PY/c.py
cp -n template.py ABC/$1/PY/d.py
cp -n template.py ABC/$1/PY/e.py
cp -n template.py ABC/$1/PY/f.py
cp -n template.py ABC/$1/PY/g.py
cp -n template.py ABC/$1/PY/h.py

exit 0