from .views import FileUploadViewSet
from rest_framework.routers import DefaultRouter



router=DefaultRouter()

router.register('upload',FileUploadViewSet)

urlpatterns=router.urls

