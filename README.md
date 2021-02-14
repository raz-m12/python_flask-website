# PyWeb

PyWeb is a personal Python project integrating the use of the popular web
development framework 'Flask' to create a simple website and it includes various
featurs such as:

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
* Bootstrap for displaying web pages, including pop-over support for users' account
* Logging via file, terminal and error-handling via email notifications
* Support for private meassaging with dynamic notifications
* Use of different threads and processes for exporting via email user's posts
* Task queues (e.g. Redis Queue) for the communication between different
  processes and to perform tasks asynchronously
* Gravatar for generating avatars for every user
* Ability to follow other user's posts
* Pagination of posts

The website can be found [here](https://pyweb-raz.herokuapp.com/).