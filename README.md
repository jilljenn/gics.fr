GICS
====

Lancer le serveur
-----------------

    virtualenv -p `which python3` venv
    . venv/bin/activate
    pip install -r requirements.txt
    cd gics
    cp secret_template.py secret.py
    ./manage.py migrate
    ./manage.py runserver
