from django.conf.urls import patterns,include,url
from app_kompres import views

urlpatterns = patterns('app_kompres.views',
	
	url(r'^malang/detail/(\d+)','detail_of_article',name='detail_of_article'),
	url(r'^malang/detail/wisata/(\d+)','detail_of_wisata',name='detail_of_wisata'),
	url(r'^malang/detail/wisata/kuliner/(\d+)','detail_of_kuliner',name='detail_of_kuliner'),
	url(r'^malang/detail/hotel/(\d+)','detail_of_hotel',name='detail_of_hotel'),
	url(r'^malang/detail/travel/(\d+)','detail_of_travel',name='detail_of_travel'),
	url(r'^malang/detail/pendidikan/(\d+)','detail_of_pendidikan',name='detail_of_pendidikan'),
	url(r'^malang/detail/rusak/(\d+)','detail_of_rusak',name='detail_of_rusak'),
	url(r'^search/$', 'search_pros',name='search_pros'),
	url(r'^wisata/lokasi/list/$','list_lokasi', name='list_lokasi'),
	url(r'^kuliner/lokasi/list/$','list_kuliner', name='list_kuliner'),
	url(r'^hotel/lokasi/list/$','list_hotel', name='list_hotel'),
	url(r'^travel/lokasi/list/$','list_travel',name='list_travel'),
	url(r'^rusak/list/$','list_rusak',name='list_rusak'),
	url(r'^pendidikan/list/$','list_pendidikan',name='list_pendidikan'),
	url(r'^news/list/$','list_article',name='list_article')

)
