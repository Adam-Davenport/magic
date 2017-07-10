from mtgsdk import Set as Mtg_Set
from datetime import datetime
import django
import os


def populate():
    from sets.models import Set
    print('Downloading all set data this will take some time...')
    sets = Mtg_Set.all()
    print('Adding sets')
    for s in sets:
        s.release_date = datetime.strptime(s.release_date, '%Y-%m-%d')
        mtg_set = Set.objects.get_or_create(
            code=s.code,
            name=s.name,
            release_date=s.release_date
        )

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "magic.settings")
    django.setup()
    populate()
