# python_flask-website

flask shell
flask run

The shell command is the second "core" command implemented by Flask,
after run. The purpose of this command is to start a Python interpreter in the
context of the application.

python -m smtpd -n -c DebuggingServer localhost:8025 % python emulated email
                                                     % service


TODO:Sending a Password Reset Email (chp 10)

# Workflow: create new translation repo
# pybabel extract -F babel.cfg -k _l -o messages.pot .
# pybabel init -i messages.pot -d app/translations -l it
# pybabel compile -d app/translations


# Workflow: Updating the current translations
# pybabel extract -F babel.cfg -k _l -o messages.pot .
# pybabel update -i messages.pot -d app/translations
# pybabel compile -d app/translations # generate .mo file

# flask translate init it
# flask translate update
# flask translate compile

# Run elasticsearch server
# To start service at startup see:
# https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html
sudo -i service elasticsearch start
# For server side see:
# https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-16-04


# Install vagrant and virtual box
sudo apt install vagrant
vagrant up
vagrant ssh



Develop unit tests
Microsoft translator API
Reset password feature using flask_mail
Flask babel for english and italian translations
full text search using elasticsearch integrated with SqlALchemy, events to update the two databases
flask_login
bootstrap
logging via file and email
SQLAlchemy events
