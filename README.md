# pythonhacking: CherryPy
## Stworzenie virtualenv

```bash
mkdir ~/venv/
python3.4 -m virtualenv ~/venv/pythonhacking-cherrypy
source ~/venv/pythonhacking-cherrypy/bin/activate
```

## Klonowanie repozytorium
```bash
mkdir ~/src
cd ~/src
git clone git@github.com:hs3city/pythonhacking-cherrypy.git
```

## Instalacja zależności
```bash
cd ~/src/pythonhacking-cherrypy
pip install --upgrade -r requirements.txt
```

## Uruchomienie
```bash
python index.py
```

Aplikacja jest dostępna Sod adresem http://localhost:8080
