from django.contrib import admin

# Register your models here.
from profile_cv.models import Draco_Profile,Work_Experiences,Draco_Profile_Image,Award_Achievements,Technical_Skills


@admin.register(Draco_Profile)
class Draco_Profile_Admin(admin.ModelAdmin):
    list_display = ('user','location','des','created','updated')
    list_filter = ('user','created')
    search_fields = ['location','des']
    raw_id_fields = ('user','profile_image')
    date_hierarchy = 'created'
    ordering = ['created']


@admin.register(Work_Experiences)
class Work_Experiences_Admin(admin.ModelAdmin):
    list_display = ('time_line','location','job','website','created','updated')
    list_filter = ('created',)
    search_fields = ('time_line','location','job')
    date_hierarchy = 'created'
    ordering = ['created']


@admin.register(Draco_Profile_Image)
class Draco_Profile_Image_Admin(admin.ModelAdmin):
    list_display = ('title','created','created')
    list_filter = ('created',)
    search_fields = ('title',)
    date_hierarchy = 'created'
    ordering = ['created']


@admin.register(Award_Achievements)
class Award_Achievements_Admin(admin.ModelAdmin):
    list_display = ('time_line','des','created')
    list_filter = ('created',)
    search_fields = ('time_line','des')
    date_hierarchy = 'created'
    ordering = ['created']


@admin.register(Technical_Skills)
class Technical_Skills_Admin(admin.ModelAdmin):
    list_display = ('category','skill')
    list_filter = ('created',)
    search_fields = ('category','skill')
    date_hierarchy = 'created'
    ordering = ['created']
