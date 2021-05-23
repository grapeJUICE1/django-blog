# <p style="text-align:center">Blugg</p>

A simple blog made with django 

# Features
Well there aren't a lot of features cause this is my first django application :) , but 

* admin can create post
* user can see posts 
* user can share post through email
* user can search post
* user can comment on a post
* post uses markdown

# Running locally
To run this project simply download this repo, then create a virtual environment in the directory.

more info on virtualenv and how to make one at [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)

then install all dependencies 

```shell
pip install -r requirements.txt --no-index --find-links file:///tmp/packages
```
more info at [here](https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from)

after that create a .env file in the directory

it should have the following things

```env
DB_USER=""
DB_NAME=""
DB_PORT=""
DB_PASSWORD=""
EMAIL_ADRESS=""
EMAIL_HOST=""
EMAIL_PASSWORD=""
```
DB_USER ,DB_NAME,DB_PORT,DB_PASSWORD are database info that u need to provide  , this projects uses postgresql

Also this project uses gmail to send emails , so you have to use a gmail account and put in the credentials here , you can ofcourse use other smtp servers 

The project uses postgresql , you can change it to sqlite or others in settings.py 

then run 
```python
python manage.py makemigrations blog

python manage.py migrate

python manage.py runserver
```
then visit to http://127.0.0.1:8000/blog/ and you should see the website


# Screenshots

![](https://github.com/grapeJUICE1/django-blog/blob/master/screenshots/website.gif?raw=true)

home
![](https://github.com/grapeJUICE1/django-blog/blob/master/screenshots/home.png?raw=true)

single post

![](https://github.com/grapeJUICE1/django-blog/blob/master/screenshots/singlePost.png?raw=true)

comments

![](https://github.com/grapeJUICE1/django-blog/blob/master/screenshots/comments.png?raw=true)

share post

![](https://github.com/grapeJUICE1/django-blog/blob/master/screenshots/sharePost.png?raw=true)