from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from app_kompres.models import wisata
from app_kompres.models import article
from app_kompres.models import hotel
from app_kompres.models import travel
from app_kompres.models import kuliner
from app_kompres.models import RumahSakit
from app_kompres.models import Pendidikan
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.db.models import Q
from django.template import loader,Context
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.views import generic
# Create your views here.

def index(request):

	wis = wisata.objects.filter().order_by('last_modified')[:8]
	kul = kuliner.objects.filter().order_by('last_modified')[:4]	
	art = article.objects.filter().order_by('tgl_buat')[:3]

	return render_to_response('index.html',{'wis':wis,'kul':kul,'art':art})

def func_wisata(request):
    hum = wisata.objects.get(pk=1)
    context = {'hum':hum}
    return render_to_response('index.html',context,context_instance=RequestContext(request))
    
def detail_of_article(request,id_target):
	select_article = article.objects.filter(id=int(id_target))
	related_post = article.objects.filter().exclude(id=id_target).order_by('title')
	recent = article.objects.filter().order_by('tgl_buat')[:3]

	return render_to_response('det_art.html',{'select_article':select_article,'related_post':related_post,'recent':recent})
	
def detail_of_wisata(request,id_wis):
	select_wisata = wisata.objects.filter(id=int(id_wis))
	related_wisata = wisata.objects.filter().exclude(id=id_wis).order_by('title')
	recent_wisata = wisata.objects.filter().order_by('last_modified')[:3]

	return render_to_response('det_art.html',{'select_wisata':select_wisata,'related_wisata':related_wisata,'recent_wisata':recent_wisata})
	
def detail_of_kuliner(request,id_kul):
	select_kuliner = kuliner.objects.filter(id=int(id_kul))
	related_kuliner = kuliner.objects.filter().exclude(id=id_kul).order_by('nama_kuliner')
	recent_kuliner = kuliner.objects.filter().order_by('last_modified')[:3]

	return render_to_response('det_art.html',{'select_kuliner':select_kuliner,'related_kuliner':related_kuliner,'recent_kuliner':recent_kuliner})

def detail_of_hotel(request,id_htl):
	select_hotel = hotel.objects.filter(id=int(id_htl))
	related_hotel = hotel.objects.filter().exclude(id=id_htl).order_by('nama_hotel')
	recent_hotel = hotel.objects.filter().order_by('tgl_pub')[:3]
	
	return render_to_response('det_art.html',{'select_hotel':select_hotel,'related_hotel':related_hotel,'recent_hotel':recent_hotel})

def detail_of_travel(request,id_trvl):
	select_travel = travel.objects.filter(id=int(id_trvl))
	related_travel = travel.objects.filter().exclude(id=id_trvl).order_by('nama_travel')
	recent_travel = travel.objects.filter().order_by('tgl_pub')[:3]

	return render_to_response('det_art.html',{'select_travel':select_travel,'related_travel':related_travel,'recent_travel':recent_travel})

def detail_of_pendidikan(request,id_pend):
	select_pendidikan = Pendidikan.objects.filter(id=int(id_pend))
	related_pendidikan = Pendidikan.objects.filter().exclude(id=id_pend).order_by('institusi')
	recent_pendidikan = Pendidikan.objects.filter().order_by('last_modified')[:3]

	return render_to_response('det_art.html',{'select_pendidikan':select_pendidikan,'related_pendidikan':related_pendidikan,'recent_pendidikan':recent_pendidikan})

def detail_of_rusak(request,id_rusak):
	select_rusak = RumahSakit.objects.filter(id=int(id_rusak))
	related_rusak = RumahSakit.objects.filter().exclude(id=id_rusak).order_by('nama_rumahsakit')
	recent_rusak = RumahSakit.objects.filter().order_by('last_modified')[:3]

	return render_to_response('det_art.html',{'select_rusak':select_rusak,'related_rusak':related_rusak,'recent_rusak':recent_rusak})


def search_pros(request):

	query = request.GET['found']
	t = loader.get_template('result_search.html')
	results = article.objects.filter(Q(title__icontains=query) | Q(isi__icontains=query)) 
	resultw = wisata.objects.filter(Q(title__icontains=query) | Q(info__icontains=query))
	resultk = kuliner.objects.filter(Q(nama_kuliner__icontains=query) | Q(info__icontains=query))
	resultt = travel.objects.filter(Q(nama_travel__icontains=query) | Q(info__icontains=query))
	resulth = hotel.objects.filter(Q(nama_hotel__icontains=query) | Q(info__icontains=query))
	
	paginator = Paginator(results,5)
	page = request.GET.get('page')
	try:
		results = paginator.page(page)
	except PageNotAnInteger:
		results = paginator.page(1)
	except EmptyPage:
		results = paginator.page(paginator.num_pages)
	index = results.number - 1
	limit = 5 #untuk limit range left-right number pages
	max_index = len(paginator.page_range)
	start_index = index - limit if index >= limit else 0
	end_index = index + limit if index <= max_index -limit else max_index
	page_range = paginator.page_range[start_index:end_index]
	c = Context({'query':query,'results':results,'resultw':resultw,'page_range':page_range,'resultk':resultk,'resulth':resulth,'resultt':resultt})
	return HttpResponse(t.render(c))

def handler404(request):
	response = render_to_response('404.html',{},context_instance=RequestContext(request))

	response.status_code = 404
	return response

def handler500(request):
	response = response_to_response('500.html',{},context_instance=RequestContext(request))
	response.status_code=500

	return response

def mysitemap(request):
	load = loader.get_template('sitepage.html')
	site_art = article.objects.all()
	site_wsta = wisata.objects.all()
	site_klnr = kuliner.objects.all()
	site_htl = hotel.objects.all()
	site_trvl = travel.objects.all()

	paginator = Paginator(site_art ,5)
	page = request.GET.get('page')
	try:
		site_art  = paginator.page(page)

	except PageNotAnInteger:
		site_art  = paginator.page(1)
	except EmptyPage:
		site_art = paginator.page(paginator.num_pages)
	index = site_art.number - 1
	limit = 5 #untuk limit range left-right number pages
	max_index = len(paginator.page_range)
	start_index = index - limit if index >= limit else 0
	end_index = index + limit if index <= max_index -limit else max_index
	page_range = paginator.page_range[start_index:end_index]

	c= Context({'site_art':site_art,'page_range':page_range,'site_wsta':site_wsta,'site_klnr':site_klnr,'site_htl':site_klnr,'site_trvl':site_trvl})

	return HttpResponse(load.render(c)) 

def post_related(request,id_target):
	load = loader.get_template('det_art.html')
	related_article = models.article.objects.filter().exclude(id=id_target)[:4]

	related_wisata = models.wisata.objects.filter().exclude(id=id_target)[:4]

	related_kuliner = models.kuliner.objects.filter().exclude(id=id_target)[:4]

	related_hotel = models.hotel.objects.filter().exclude(id=id_target)[:4]

	related_travel = models.travel.objects.filter().exclude(id=id_target)[:4]

	c= Context({'related_article':related_article,'related_wisata':related_wisata,'related_kuliner':related_kuliner,'related_hotel':related_hotel,'related_travel':related_travel})


	return HttpResponse(load.render(c))

def list_lokasi(request):

	load = loader.get_template('det_art.html')
	list_lokasi = wisata.objects.all().order_by('title')
	paginator = Paginator(list_lokasi ,10)
	page = request.GET.get('page')
	try:
		list_lokasi  = paginator.page(page)

	except PageNotAnInteger:
		list_lokasi  = paginator.page(1)
	except EmptyPage:
		list_lokasi = paginator.page(paginator.num_pages)
	index = list_lokasi.number - 1
	limit = 5 #untuk limit range left-right number pages
	max_index = len(paginator.page_range)
	start_index = index - limit if index >= limit else 0
	end_index = index + limit if index <= max_index -limit else max_index
	page_range = paginator.page_range[start_index:end_index]

	c= Context({'list_lokasi':list_lokasi,'page_range':page_range})
	return HttpResponse(load.render(c))

def list_kuliner(request):
	load = loader.get_template('det_art.html')
	list_kuliner = kuliner.objects.all().order_by('nama_kuliner')
	paginator = Paginator(list_kuliner ,10)
	page = request.GET.get('page')
	try:
		list_kuliner  = paginator.page(page)

	except PageNotAnInteger:
		list_kuliner  = paginator.page(1)
	except EmptyPage:
		list_kuliner = paginator.page(paginator.num_pages)
	index = list_kuliner.number - 1
	limit = 5 #untuk limit range left-right number pages
	max_index = len(paginator.page_range)
	start_index = index - limit if index >= limit else 0
	end_index = index + limit if index <= max_index -limit else max_index
	page_range = paginator.page_range[start_index:end_index]

	c= Context({'list_kuliner':list_kuliner,'page_range':page_range})
	return HttpResponse(load.render(c))

def list_hotel(request):
	load = loader.get_template('det_art.html')
	list_hotel = hotel.objects.all()
	paginator = Paginator(list_hotel ,10)
	page = request.GET.get('page')
	try:
		list_hotel  = paginator.page(page)

	except PageNotAnInteger:
		list_hotel  = paginator.page(1)
	except EmptyPage:
		list_hotel = paginator.page(paginator.num_pages)
	index = list_hotel.number - 1
	limit = 5 #untuk limit range left-right number pages
	max_index = len(paginator.page_range)
	start_index = index - limit if index >= limit else 0
	end_index = index + limit if index <= max_index -limit else max_index
	page_range = paginator.page_range[start_index:end_index]

	c= Context({'list_hotel':list_hotel,'page_range':page_range})
	return HttpResponse(load.render(c))

def list_travel(request):
	load = loader.get_template('det_art.html')
	list_travel = travel.objects.all()
	paginator = Paginator(list_travel ,10)
	page = request.GET.get('page')
	try:
		list_travel  = paginator.page(page)

	except PageNotAnInteger:
		list_travel  = paginator.page(1)
	except EmptyPage:
		list_travel = paginator.page(paginator.num_pages)
	index = list_travel.number - 1
	limit = 5 #untuk limit range left-right number pages
	max_index = len(paginator.page_range)
	start_index = index - limit if index >= limit else 0
	end_index = index + limit if index <= max_index -limit else max_index
	page_range = paginator.page_range[start_index:end_index]

	c= Context({'list_travel':list_travel,'page_range':page_range})
	return HttpResponse(load.render(c))

def list_rusak(request):

	load = loader.get_template('det_art.html')
	list_rusak = RumahSakit.objects.all().order_by('nama_rumahsakit')
	paginator = Paginator(list_rusak,10)
	page = request.GET.get('page')
	try:
		list_rusak  = paginator.page(page)

	except PageNotAnInteger:
		list_rusak  = paginator.page(1)
	except EmptyPage:
		list_rusak = paginator.page(paginator.num_pages)
	index = list_rusak.number - 1
	limit = 5 #untuk limit range left-right number pages
	max_index = len(paginator.page_range)
	start_index = index - limit if index >= limit else 0
	end_index = index + limit if index <= max_index -limit else max_index
	page_range = paginator.page_range[start_index:end_index]

	c= Context({'list_rusak':list_rusak,'page_range':page_range})
	return HttpResponse(load.render(c))

def list_pendidikan(request):
	load = loader.get_template('det_art.html')
	list_pendidikan = Pendidikan.objects.all().order_by('institusi')
	paginator = Paginator(list_pendidikan ,10)
	page = request.GET.get('page')
	try:
		list_pendidikan  = paginator.page(page)

	except PageNotAnInteger:
		list_pendidikan  = paginator.page(1)
	except EmptyPage:
		list_pendidikan = paginator.page(paginator.num_pages)
	index = list_pendidikan.number - 1
	limit = 5 #untuk limit range left-right number pages
	max_index = len(paginator.page_range)
	start_index = index - limit if index >= limit else 0
	end_index = index + limit if index <= max_index -limit else max_index
	page_range = paginator.page_range[start_index:end_index]

	c= Context({'list_pendidikan':list_pendidikan,'page_range':page_range})
	return HttpResponse(load.render(c))

def list_article(request):
	load = loader.get_template('det_art.html')
	list_article = article.objects.all().order_by('tgl_buat')
	paginator = Paginator(list_article ,10)
	page = request.GET.get('page')
	try:
		list_article  = paginator.page(page)

	except PageNotAnInteger:
		list_article  = paginator.page(1)
	except EmptyPage:
		list_article = paginator.page(paginator.num_pages)
	index = list_article.number - 1
	limit = 5 #untuk limit range left-right number pages
	max_index = len(paginator.page_range)
	start_index = index - limit if index >= limit else 0
	end_index = index + limit if index <= max_index -limit else max_index
	page_range = paginator.page_range[start_index:end_index]

	c= Context({'list_article':list_article,'page_range':page_range})
	return HttpResponse(load.render(c))
