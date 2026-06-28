from django.contrib import admin
from .models import ProductOffer, FavoriteItem, SearchQuery
# Register your models here.
admin.site.register(ProductOffer)
admin.site.register(FavoriteItem)
admin.site.register(SearchQuery)