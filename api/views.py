from rest_framework import viewsets
from .models import UploadedFile
from .serializers import UploadedFileSerializer


class FileUploadViewSet(viewsets.ModelViewSet):
    queryset=UploadedFile.objects.all()
    serializer_class=UploadedFileSerializer

