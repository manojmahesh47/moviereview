from django.contrib import admin
from .models import Movie, Category, Actor, Review

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'category')
    search_fields = ['title', 'category__name', 'actors__name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor)  # Register Actor without specifying Admin options
admin.site.register(Review)