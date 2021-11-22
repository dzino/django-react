# Installation

## Django

```bash
pip3 install django
pip3 install djangorestframework
pip3 install django-cors-headers

python3 -m django startproject main
cd main
python3 manage.py runserver
```

`/main/settings.py`

```diff
INSTALLED_APPS = [
    ...
+   'rest_framework',
+   'corsheaders',
]

MIDDLEWARE = [
+    'corsheaders.middleware.CorsMiddleware', # At the top of the list
    ...
]

+ CORS_ORIGIN_WHITELIST = [
+     'http://google.com',
+     'http://hostname.example.com',
+     'http://localhost:8000',
+     'http://127.0.0.1:9000'
+ ]
```

## React

Moving the React project to the Django project. Rename the folder to `frontend`.

```bash
cd frontend
yarn
yarn build
```

`/main/settings.py`

```diff
...
TEMPLATES = [
    {
        ...
-       'DIRS': [],
+       'DIRS': [
+           BASE_DIR / 'frontend/build'
+       ],
        ...
    },
]
...

+ STATICFILES_DIRS = [
+     BASE_DIR / 'frontend/build/static'
+ ]
```

`/main/urls.py`

```diff
from django.contrib import admin
from django.urls import path
+ from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
+   path("", TemplateView.as_view(template_name="index.html"))
]
```

# Applications

Part of the project.

```
Models ─┬─ Serializers ─ Views ─ Urls ─ Main/Urls
        └─ Admin
```

## Add

```bash
python3 manage.py startapp <name>
```

`/main/settings.py`

```diff
INSTALLED_APPS = [
    ...
    'django.contrib.messages',
+   '<name>',
]
```

`/main/urls.py`

```diff
- from django.urls import path
+ from django.urls import path, include

urlpatterns = [
    ...
+   path('<name>/', include('<name>.urls')),
]
```

```bash
touch <name>/urls.py
touch <name>/serializers.py
```

## Models

Working with the database.

`/<name>/models.py`

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Super user:

```bash
python3 manage.py createsuperuser
```

# Stack

- Python3
- Django
- Django REST framework
- TypeScript
- React
- Redux
- Saga
- Jest
- Prototypes
- Material-UI
- React Router DOM

# Sources of

- https://www.youtube.com/watch?v=jCMaO2d6anE
- Models: https://djangodoc.ru/3.2/topics/db/models/
- Doc: https://www.django-rest-framework.org
- React: https://www.youtube.com/watch?v=nJ9BohUzgtM
- https://www.youtube.com/watch?v=6K83dgjkQNw
- https://www.youtube.com/watch?v=F9o4GSkSo40
- React routing: https://youtu.be/jCMaO2d6anE?t=7588
- React-router-dom: https://github.com/remix-run/react-router/blob/main/docs/getting-started/tutorial.md
