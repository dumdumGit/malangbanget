from django.db import models
from location_field.models.plain import PlainLocationField
import twitter
import os
import urllib,urllib2
from django.conf import settings
from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
# Create your models here.


class wisata(models.Model):
	info = RichTextField(null=True)
	title = models.CharField(max_length=60,null=True)
	last_modified = models.DateTimeField(auto_now=True,null=True)
	kategori_wisata = models.CharField(max_length=25,null=True)
	image = models.ImageField(null=True,upload_to="kotwis")
	tempat = models.CharField(max_length=255,null=True)
	location = PlainLocationField(based_fields=[tempat], zoom=7,null=True)
    
	def __unicode__(self):
		return unicode(self.title)
	class Meta:
		ordering = ['last_modified']   

class kuliner(models.Model):
	info = RichTextField(null=True)
	nama_kuliner = models.CharField(max_length=60,null=True)
	last_modified = models.DateTimeField(auto_now=True,null=True)
	image_kuliner = models.ImageField(null=True,upload_to="kuliner")
	tempat = models.CharField(max_length=255,null=True)
	location = PlainLocationField(based_fields=[tempat], zoom=7,null=True)

	def __unicode__(self):
		return unicode(self.nama_kuliner)

	class Meta:
		ordering = ['last_modified']  		

class article(models.Model):
	title = models.CharField(max_length=60,null=True)
	isi = RichTextField(null=True)
	image_post = models.ImageField(upload_to="post_artikel",null=True)
	image_height = models.PositiveIntegerField(null=True,editable=False,default="190")
	image_width = models.PositiveIntegerField(null=True,editable=False,default="350")
	tgl_buat = models.DateTimeField(auto_now=True,null=True)
	link = models.CharField(max_length=200,null=True)

	def __unicode__(self):
		return u'%s' % self.title
	
	def get_absolute_url(self):
		return self.link
		
	def get_twitter_message(self):
		return u'my-custom-twitter-message: %s - %s '%(self.title,self.link)
	
#TWITTER_MAXLENGTH = getattr(settings,'TWITTER_MAXLENGTH',140)
#def post_to_twitter(sender,instance,*args,**kwargs):

	#if not kwargs.get('created'):
		#return False
		
	#try:
	#	username = settings.TWITTER_USERNAME
	#	password = settings.TWITTER_PASSWORD
	#	consumer_key = 'RlQe94WOyVSrLKxT0n8QiIRli'
	#	consumer_secret = 'D2bzeCgMizJ0y9z8vXlAGbFx8qzvR8wcvWjrUoZqoCFfLC9c4D'
	#	access_token = '400778715-awFHWP3g1sb8CYmQJXE4N5OzNdW63VN6RxjME7d8'
	#	access_token_secret = 'DWCsWSLH2pzHlgG58Zun8LDg3VHOBU8Xtnt0DsiCrmDYL'

	#except AttributeError:
	#	print 'WARNING: Twitter account not configured.'
	#	return False
		
	#url = instance.get_absolute_url()
	#if not url.startswith('http://') and not url.startswith('https://'):
	#	domain =Site.objects.get_current().domain
	#	url = u'http://%s%s' %(domain, url)
		
	#create_api = 'http://tinyurl.com/api-create.php'
	#data = urllib.urlencode(dict(url=url))
	#link = urllib2.urlopen(create_api,data=data).read().strip()
	
	#try:
	#	text = instance.get_twitter_message()
	#except AttributeError:
	#	text = unicode(instance)
		
	#mesg = u'%s - %s' % (text, link)
	#if len(mesg) > TWITTER_MAXLENGTH:
	#	size = len(mesg + '....') - TWITTER_MAXLENGTH
	#	mesg = u'%s... - %s' % (text[:-size], link)
		
	#try:
	#	twitter_api = twitter.Api(username, password)
	#	twitter_api.PostUpdate(mesg)
	#except urllib2.HTTPError, ex:
	#	print 'ERROR:',str(ex)
	#	return False
		
#models.signals.post_save.connect(post_to_twitter, sender=article)

    
class hotel(models.Model):
	nama_hotel = models.CharField(max_length=30)
	no_tlp = models.IntegerField()
	tgl_pub = models.DateTimeField(auto_now=True)
	link_hotel = models.CharField(max_length=150)
	price = models.IntegerField()
	kategori = models.CharField(max_length=35, choices=[('satu', 'satu'), ('dua', 'dua'), ('tiga', 'tiga'), ('empat', 'empat'), ('lima', 'lima')],null=True)
	image = models.ImageField(null=True,upload_to="hotel")
	info = RichTextField()
	tempat = models.CharField(max_length=255,null=True)
	location = PlainLocationField(based_fields=[tempat], zoom=8,null=True)
    
	def __unicode__(self):
		return self.nama_hotel
    
class travel(models.Model):
	nama_travel = models.CharField(max_length=30)
	no_tlp = models.IntegerField()
	tgl_pub = models.DateTimeField(auto_now = True)
	link_travel = models.CharField(max_length=150)
	image = models.ImageField(null=True,upload_to="travel")
	info = RichTextField(null=True)
	tempat = models.CharField(max_length=255,null=True)
	location = PlainLocationField(based_fields=[tempat], zoom=8,null=True)

    
	def __unicode__(self):
		return self.nama_travel

class RumahSakit(models.Model):
	nama_rumahsakit = models.CharField(max_length=50)
	cover = models.ImageField(upload_to="RumahSakit")
	alamat = models.TextField()
	no_telepon = models.IntegerField()
	last_modified = models.DateTimeField(auto_now=True)
	info = RichTextField()
	tempat = models.CharField(max_length=255)
	location = PlainLocationField(based_fields=[tempat], zoom=8)

	def __unicode__(self):
		return unicode(self.nama_rumahsakit)

	class Meta:
		ordering = ['last_modified']  	

class Pendidikan(models.Model):
	institusi = models.CharField(max_length=80)
	kategori = models.CharField(max_length=35, choices=[('formal', 'formal'), ('informal', 'informal')],null=True)
	SD = models.BooleanField(default=False)
	SMP = models.BooleanField(default=False)
	SMA = models.BooleanField(default=False)
	Perguruan_Tinggi = models.BooleanField(default=False)
	cover = models.ImageField(upload_to="Pendidikan")
	link = models.CharField(max_length=100,null=True)
	alamat = models.TextField()
	no_telepon = models.IntegerField()
	last_modified = models.DateTimeField(auto_now=True)
	info = RichTextField()
	tempat = models.CharField(max_length=255)
	location = PlainLocationField(based_fields=[tempat], zoom=8)

	def __unicode__(self):
		return unicode(self.institusi)

	class Meta:
		ordering = ['last_modified']  	
	
