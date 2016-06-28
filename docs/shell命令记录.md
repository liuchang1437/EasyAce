# 建立 venv
```
$ pyvenv venv
$ source venv/bin/activate
$ pip install django
$ python -c 'import django;print(django.get_version())'
```

# 建立django项目和应用
```
$ django-admin startproject EasyAce
$ python manage.py startapp users #创建users应用
$ python manage.py makemigrations users #创建数据库迁移
$ python manage.py migrate #执行数据库迁移
$ python manage.py startapp main #创建main应用
```