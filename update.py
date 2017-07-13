from mtgsdk import Card as MagicCard
import django
import os


def populate():
    from cards.models import Card
    print('Downloading all card data this will take some time...')
    cards = MagicCard.all()
    print('Adding cards to database')
    for c in cards:
        card = Card.objects.create(
            name=c.name,
            set=c.set,
            rarity=c.rarity,
            image_url=c.image_url,
            multiverse_id=c.multiverse_id,
        )
        card.save()

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "magic.settings")
    django.setup()
    populate()
