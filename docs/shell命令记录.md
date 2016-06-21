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
```