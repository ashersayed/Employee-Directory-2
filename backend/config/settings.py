import pymysql

pymysql.install_as_MySQLdb()

SECRET_KEY = "dev-only-secret-key"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "corsheaders",      
    "employees",        
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",   
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "employee_directory",
        "USER": "root",
        "PASSWORD": "put your password", 
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}


CORS_ALLOWED_ORIGINS = ["http://localhost:5173"]

APPEND_SLASH = False   
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True
