googleappengine-djangae-blog
============================

A simple blog running on Google App Engine via Djangae.
Project in development


Install
-------

    ./install_deps
    python manage.py checksecure --settings=blog.settings_live


Run locally
-----------

    python manage.py runserver

* App @ http://localhost:8000
* DevEngine @ http://localhost:8001

Deploy
------

    appcfg.py update .

Test
----

TODO


Local shell
-----------

     python manage.py shell
