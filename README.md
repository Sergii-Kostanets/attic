Useful Commands:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
deactivate
```
```
pip3 install 'django<4'
```
```
pip3 show django
```
```
export PATH=$PATH:/Users/sergeykostanets/Library/Python/3.11/bin
```
```
django-admin --version
```
```
django-admin startproject boutique_ado .
```
```
python3 manage.py runserver
```
```
python3 manage.py migrate
```
```
python3 manage.py createsuperuser
```
```
pip3 install django-allauth==0.41.0
```
```
python3 manage.py migrate
```
```
python3 manage.py runserver
```
```
pip3 freeze > requirements.txt
```
```
cp -r /Users/sergeykostanets/Projects/codeinstitute-boutique-ado/venv/lib/python3.11/site-packages/allauth/templates/* ./templates/allauth 
```
```
python3 manage.py startapp home
```
```
mkdir -p home/templates/home
```
```
mkdir static
```
```
mkdir media
```
```
mkdir static/css
```
```
mkdir templates/includes
```
```
python3 manage.py startapp products
```
```
mkdir products/fixtures
```
```
python3 manage.py makemigrations --dry-run
```
```
pip3 install pillow
```
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate --plan
```
```
python3 manage.py migrate
```
```
python3 manage.py loaddata categories
```
```
python3 manage.py loaddata products
```
```
mkdir -p products/templates/products
```
```
python3 manage.py startapp bag
```
```
python3 manage.py makemigrations --dry-run
```
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate --plan
```
```
python3 manage.py migrate
```
```
python3 manage.py shell
from products.models import Product
kdbb = ['kitchen_dining', 'bed_bath']
clothes = Product.objects.exclude(category__name__in=kdbb)
clothes.count()
for item in clothes:
    item.has_sizes = True
    item.save()
Product.objects.filter(has_sizes=True)
Product.objects.filter(has_sizes=True).count()
exit()
```
```
python3 manage.py startapp checkout
```
```
python3 manage.py makemigrations --dry-run
```
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate --plan
```
```
python3 manage.py migrate
```
```
pip3 install django-crispy-forms==1.14.0
```
```
pip3 freeze > requirements.txt
```
```
pip3 install stripe
```
```
export STRIPE_PUBLIC_KEY=
```
```
export STRIPE_SECRET_KEY=
```
```
pip3 install django-countries==7.2.1
```
```
python3 manage.py startapp profiles
```
```
pip3 install dj_database_url==0.5.0 psycopg2
```
```
pip3 freeze > requirements.txt
```
```
python3 manage.py showmigrations
```
```
python3 manage.py migrate
```
```
python3 manage.py loaddata categories
```
```
python3 manage.py loaddata products
```
```
pip3 install 'django<4' gunicorn
```
```
pip3 freeze > requirements.txt
```
```
heroku login
```
```
heroku config:set DISABLE_COLLECTSTATIC=1 --app boutique-ado-codeinstitute
```
```
heroku git:remote -a boutique-ado-codeinstitute
```
```
git push heroku main
```
```
pip3 install boto3
```
```
pip3 install django-storages
```
```
pip3 freeze > requirements.txt
```
```
git add . && git commit -m "commit" && git push
```
```
pip install flake8
```
```
pip install flake8-django
```