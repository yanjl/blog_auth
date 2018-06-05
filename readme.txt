Server2008 R2 sp1
IIS7.0 
pip install Django
pip install wfastcgi
pip install mysqlclient

1.  IIS，“添加角色服务”-》 勾选“应用程序开发（已安装）”下“CGI"
2.  将lib/site-packages/wfastcgi.py 复制至 项目文件下
3.  将项目文件夹整个复制至“c\inetpub\wwwroot\"下
4.  添加网站，设置内容物理路径，端口等，对开发端口，设置防火墙。
5.  “处理程序映射”-> “添加模块映射”，
     请求路径： *
     模块：FastCgiModule
     可执行文件：python.exe路径| 项目下wfastcgi.py文件路径
     名称：DjangoWebHandler
6.   返回主页，进入FastCGI设置 
     环境变量-》集合，添加：
     1）get_wsgi_application()方法的位置，C:\Anaconda3\Lib\site-packages\django\core\wsgi.py
        Name: WSGI_HANDLER
        Value: django.core.wsgi.get_wsgi_application()
     2）Django项目目录
        Name: PYTHONPATH
        Value: C:\inetpub\wwwroot\PowerX
     3）项目settings.py文件的位置
        Name: DJANGO_SETTINGS_MODULE
        Value: 
5.    设置静态文件
      setting.py 添加  STATIC_ROOT = 'static/'
      python manage.py collectstatic
      网站“虚拟目录static”，设置静态文件夹别名和物理路径，
      选中“虚拟目录static”，双击“处理程序映射”，删除DjangoWebHandler，只保留StaticFile映射。 （关键步骤，admin css正常访问）
6.   setting.py
     DEBUG=Fasle
     ALLOWED_HOSTS = ['*']
7.   设置网站文件夹IIS用户访问权限。
8.   启动网站



Sqlite3 数据库向MySQL迁移
pip install mysqlclient

1.在MYSQL建立空的数据库,mysite,  CREATE DATABASE mysite CHARACTER SET utf8 COLLATE utf8_general_ci; 
2.先建立一个SLAVE数据库
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",        
    },
    "slave": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mysite",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

3.python manage.py makemigrations & migrate
4.将SQLITE主库的数据导出   python manage.py dumpdata > mysite_all_data.json
5.切换主库和从库的setting.py设置，将MYSQL设置为主库，导入数据。
python manage.py loaddata mysite_all_data.json


===========================
setting.py

DEBUG = False
ALLOWED_HOSTS = ['202.192.XXX.XXX'] #服务器本机ip

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_TZ = False

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

# LOGIN_URL = '/blog/login/'
LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/blog/list/'

SESSION_COOKIE_AGE = 60 * 30  # 30分钟
# SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 关闭浏览器，则COOKIE失效
