# Team College Bored - Jared Asch, Ryan Aday, Imad Belkebir

## Dependencies
- flask
- wheel
- sqlite3

To install all of these, run:
```bash
$ python3 -m venv <name>
$ . <name>/bin/activate # activate venv
$ pip3 install flask
$ pip3 install wheel
$ pip3 install sqlite
```

## Running our Project
Once all of the dependencies have been installed, all you need to to is create the database and run the main server file

```bash
# while venv is active
$ python3 utils/db_create.py
$ python3 utils/db_populate.py
# For default accounts
$ python3 app.py
```
