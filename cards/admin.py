from django.contrib import admin
from cards.models import Card, Battle, Battle_Pack

# Register your models here.
admin.site.register(Card)
admin.site.register(Battle)
admin.site.register(Battle_Pack)
