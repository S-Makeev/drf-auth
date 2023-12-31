from django.urls import path
from .views import GalleryList, GalleryDetail


urlpatterns = [
    path('', GalleryList.as_view(), name='gallery_list'),
    path('<int:pk>', GalleryDetail.as_view(), name='gallery_list_detail')
]