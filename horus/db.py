from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


POSTGRES = {

    'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'horus',
            'USER': 'postgres',
            'PASSWORD': 'Avasco10',
            'HOST':  'localhost',
            'POST': 5432
    }

}