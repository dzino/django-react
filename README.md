# Installation

## Django

```bash
pip3 install django
python3 -m django startproject main
cd main
python3 manage.py runserver
```

## React

Moving the React project to the Django project. Rename the folder to `frontend`.

```bash
yarn
yarn build
```

/main/settings.py

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

/main/urls.py

```diff
from django.contrib import admin
from django.urls import path
+ from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
+   path("", TemplateView.as_view(template_name="index.html"))
]
```

# Sources of:

- https://www.youtube.com/watch?v=6K83dgjkQNw
- https://www.youtube.com/watch?v=nJ9BohUzgtM
- https://www.youtube.com/watch?v=F9o4GSkSo40
