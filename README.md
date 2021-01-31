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