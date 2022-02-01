# python-rest-server
Cuurently not a REST server, but following a Flask tutorial to learn the basics of server development.

Created following the [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) tutorial

To run, from `/src/mircoblog`, run the command:
```
flask run
```

## tox
For tox, from the base directory, run the command:
```
tox
```

On the first run, this will set up virtual environments for pytest, pylint, & flake8.

### pytest
pytest will run all the test files defined in the `/tests` folder.

### pylint
pylint will check the codestyle of files defined in both the `/tests` & `/src` folders.

Warnings for ``missing-docstring`` have been excluded in the tox file. Any additional warning suppression can be added to the ``--disable`` line in the ``[testenv:pylint] ... commands = ...`` in the `tox.ini` file or disabled individually on the specific file giving the warning.

### flake8
flake8 with check the codestyle of files defined in both the `/test` & the `/src` folders.