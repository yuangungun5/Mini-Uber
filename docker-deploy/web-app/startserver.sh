#!/bin/bash
python3 manage.py makemigrations ride
python3 manage.py makemigrations users
python3 manage.py migrate ride
python3 manage.py migrate users
python3 manage.py migrate
res="$?"
while [ "$res" != "0" ]
do
    sleep 3;
    
    python3 manage.py migrate ride
    python3 manage.py migrate users
    python3 manage.py migrate 
    res="$?"
done
python3 manage.py runserver 0.0.0.0:8000
