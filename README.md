# social-rest-jwt
A simple social network API (Django Rest Framework) and a bot. Authentication via JWT tokens.

## Setup

Install required packages:
```
pip3 install -r requirements.txt
```

Initialize database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Optional

Create an admin user:
```
python3 manage.py createsuperuser
```

Change bot.py settings in bot.ini:
```
vim bot.ini
```

## Populate data

Start server and run the bot.py to populate test data:
```
python3 manage.py runserver
python3  bot.py
```

## API endpoints

Sign up: http://127.0.0.1:8000/api/signup/  
Accepts POST requests.  
Example payload:  
```
{
 "email":"test1@localhost",
 "password":"Pwd123@"
}
```
---
Sign in to get JWT tokens: http://127.0.0.1:8000/api/token/  
Accepts POST requests.  
Example payload:  
```
{
 "email":"test1@localhost",
 "password":"Pwd123@"
}
```
---
Get users' activity: http://127.0.0.1:8000/api/users_activity/  
Accepts GET requests.  
Shows when a user made the last request to the service and the last login time.
 
---
Create a post: http://127.0.0.1:8000/api/posts/  
Accepts POST requests.  
Example payload:  
```
{
 "title":"title2",
 "body":"body1"
}
```
---
Show all posts: http://127.0.0.1:8000/api/posts/  
Accepts GET requests.  

---
Post like: http://127.0.0.1:8000/api/post_like/  
Accepts POST requests.  
Usage: Just send a post ID you wish to like. The Backend automatically adds current date and current user.  
Example payload:
```
{
 "post":"27"
}
```
---
Post unlike: http://127.0.0.1:8000/api/post_unlike/{post_id}  
Accepts DELETE requests.  
Example:
```
http://127.0.0.1:8000/api/post_unlike/40
```
---
Get analytics about likes: http://127.0.0.1:8000/api/analytics?date_from=2020-05-20&date_to=2020-06-09  
Returns count of likes aggregated by day.  
Accepts GET requests.  
