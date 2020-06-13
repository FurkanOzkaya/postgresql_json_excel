# postgresql_json_excel

This API use PostgreSql json type. and This api can use create excel view. You can add column and data. Basic code has been writed it will be improve. Feel free to improve this project. Also check vue excell app. [excel_vue](https://github.com/FurkanOzkaya/excel_vue)

# Instalation Guide

## With VirtualEnv

1.) Clone Project
```
git clone https://github.com/FurkanOzkaya/postgresql_json_excel.git
```
2.) Create Virtualenv and activate
```
virtualenv env
source env/Scripts/activate
```
I use git bash when creating virtualenv if you use Cmd. You can write directly env/Scripts/activate.

3.) Go Project and install requirments.txt
```
cd postgresql_json_excel/
pip install -r requirments.txt
```
Be sure virtualenv is active when you installing requirments.

4.) Run
```
python manage.py runserver 0.0.0.0:9000
```
default [excel_vue](https://github.com/FurkanOzkaya/excel_vue) project use 9000 port.
you can also run this code
```
python manage.py runserver
```


# Design Document

:open_book:[Design_Document](design.md)
