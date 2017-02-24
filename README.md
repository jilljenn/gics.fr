GICS
====

Lancer le serveur
-----------------

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    cd gics
    cp secret_template.py secret.py
    ./manage.py migrate
    ./manage.py runserver
