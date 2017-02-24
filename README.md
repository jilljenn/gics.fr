GICS
====

Lancer le serveur
-----------------

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    cd gics
    cp secret_template.py secret.py
    # Modifier secret.py (chemins, mails, clé secrète, debug)
    ./manage.py migrate  # Pour mettre à jour la BDD
    ./manage.py collectstatic  # Pour mettre les fichiers statiques dans STATIC_ROOT
    ./manage.py runserver  # Pour lancer le serveur
