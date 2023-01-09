from django.contrib import admin

from .models import Movie, WatchList, StreamPlatForm, Review

# Register your models here.

admin.site.register(Movie)
admin.site.register(WatchList)
admin.site.register(StreamPlatForm)
admin.site.register(Review)