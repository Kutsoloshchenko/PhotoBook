from django.conf.urls import url
from rest_app_photo_book import views

urlpatterns = [
    url(r"^sign_up/$", views.sign_up),
    url(r"^sign_in/$", views.sign_in),
    url(r'^create_album/$', views.create_album),
    url(r'^create_file/$', views.create_file),
    url(r'^get_albums/$', views.get_albums),
    url(r'^get_files/$', views.get_files_in_album),
    url(r'^change_album_name/$', views.change_album_name),
    url(r'^change_file/$', views.change_file_attribute),
    url(r'^delete_files/$', views.delete_files),
    url(r'^delete_album/$', views.delete_album)
]