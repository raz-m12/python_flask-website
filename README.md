# PyWeb

This is a website made in Python using [Flask](https://flask.palletsprojects.com/en/2.1.x/). It was inspired by [Migue Grinberg's mega Flask tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world).

# Features

* Deployment on Heroku, using gunicorn
* Posgres for Heroku database storage
* Lightweight SQLite for local development
* Unit tests
* Microsoft translator API
* Ability to register and reset password using flask_mail
* Flask babel, for generating website's language, in English and Italian based on
  browser's current language
* Full text intelligent search using ElasticSearch, including SQLAlchemy events
  for synchronization
* Ability to create users using flask_login
* Bootstrap for displaying web pages, including pop-over support for users' accounts
* Logging via file, terminal and error-handling via email notifications
* Support for private meassaging with dynamic notifications
* Use of different threads and processes for exporting via email user's posts
* Task queues (e.g. Redis Queue) for the communication between different
  processes and to perform tasks asynchronously
* Ability to follow other users' posts
* Pagination of posts
* Custom avatars using [Gravatar.com](https://en.gravatar.com/)

