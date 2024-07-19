from django.contrib import admin
from .models import SearchHistory, City
# Register your models here.




@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('city', 'timestamp')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'longitude', 'latitude')