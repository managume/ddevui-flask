# ddev**ui**

### Levantar en entorno virtual
```sh
git clone
cd ddevui
virtualenv -p python3 venv
source /venv/bin/activate.fish
pip install -r requirements.txt
```

### Inicializar base de datos sqlite
```sh
cd ..
python
>>> from ddevui import db,create_app
>>> db.create_all(app=create_app)
```

