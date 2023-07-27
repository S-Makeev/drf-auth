from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import GallerySerializer
from .models import GalleryInfo
from .permissions import isOwnerOrReadOnly

class GalleryList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = GalleryInfo.objects.all()
    serializer_class = GallerySerializer

class GalleryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, isOwnerOrReadOnly)
    queryset = GalleryInfo.objects.all()
    serializer_class = GallerySerializer