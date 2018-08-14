### Init
```
pip install -r requirements.txt
django-admin.py startproject magicops
python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser --username=admin --email=admin@admin.com
```
> initial password: test1234

### Run Server
```
python manage.py runserver 0:8000
```

### Test

```
py
pip install httpie
http http://127.0.0.1:8000/
```
