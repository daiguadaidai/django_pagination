# Django 自定义分页
-------------
#####项目基本结构

    django_pagination
    ├── common
    │   └── util
    │       ├── pagination.py # 自己实现的分页代码
    ├── db.sqlite3
    ├── django_pagination
    │   ├── settings.py # 配置数据库 和 app
    │   ├── urls.py # 配置转跳链接
    │   ├── wsgi.py
    ├── manage.py
    ├── mysite
    │   ├── admin.py
    │   ├── __init__.py
    │   ├── migrations
    │   ├── models.py # 关联数据库的model
    │   ├── templates
    │   │   ├── index.html # 显示分页的页面
    │   ├── tests.py
    │   ├── views.py # 逻辑代码
    ├── README.md
    └── sql
        └── mysite.sql # 数据库表结构和数据
 
#####导入数据

    mysql -uxxx -pyyy < sql/mysite.sql

#####启动 server

    python manage.py runserver 0.0.0.0:8000

#####访问网页

    http://127.0.0.1:8000/mysite/index

#####看代码顺序
1. 看 mysite/views.py 中的 index 方法
2. 再看 mysite/comm/templates/index.html
3. 最后看分页主逻辑 common/util/pagination.py

#####外来展望
在后期会考虑添加过滤model的条件
