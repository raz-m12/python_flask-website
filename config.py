import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # mail notification
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['razfv12@gmail.com']
    LANGUAGES = ['en', 'it']

    # pagination
    POSTS_PER_PAGE = 3
    # translator
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    # eleastic search
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

    # Heroku
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    # Redis
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
