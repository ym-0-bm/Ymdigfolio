from django.contrib import admin

from portfolio.models import Band

from portfolio.models import Listing

admin.site.register(Band)

admin.site.register(Listing)


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')  # ajouter ‘band' ici
