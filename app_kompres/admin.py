from django.contrib import admin
from app_kompres.models import wisata
from app_kompres.models import article
from app_kompres.models import hotel
from app_kompres.models import travel
from app_kompres.models import kuliner
from app_kompres.models import RumahSakit
from app_kompres.models import Pendidikan
from django import forms
from ckeditor.widgets import CKEditorWidget
# Register your models here.
	
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title","image_post","link","tgl_buat")
	list_filter = ['tgl_buat']

class WisataAdmin(admin.ModelAdmin):
	list_display = ("title","image","tempat","location","last_modified")
	list_filter = ['last_modified']

class KulinerAdmin(admin.ModelAdmin):
	list_display = ("nama_kuliner","image_kuliner","tempat","location","last_modified")
	list_filter = ['last_modified']
class RSAdmin(admin.ModelAdmin):
	list_display = ("nama_rumahsakit","cover","alamat","no_telepon","info","tempat","location","last_modified")
	list_filter = ['last_modified']

class PendAdmin(admin.ModelAdmin):
	list_display = ("institusi","cover","alamat","no_telepon","info","tempat","location","last_modified")
	list_filter = ['last_modified']

admin.site.register(wisata,WisataAdmin)
admin.site.register(article,ArticleAdmin)
admin.site.register(travel)
admin.site.register(hotel)
admin.site.register(kuliner,KulinerAdmin)
admin.site.register(RumahSakit,RSAdmin)
admin.site.register(Pendidikan,PendAdmin)


