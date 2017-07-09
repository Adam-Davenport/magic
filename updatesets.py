from mtgsdk import Set as Mtg_Set
import django
import os


def populate():
    from sets.models import Set
    print('Downloading all set data this will take some time...')
    sets = Mtg_Set.all()
    print('Adding sets')
    for s in sets:
        mtg_set = Set.objects.create(
            code=s.code,
            name=s.name,
            gatherer_code=s.gatherer_code,
            release_date=s.release_date
        )

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "magic.settings")
    django.setup()
    populate()
