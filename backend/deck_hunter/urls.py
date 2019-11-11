from django.contrib import admin
from rest_framework.routers import DefaultRouter
from metahunter.views import MetahunterViewSet, DeckViewSet, CardViewSet
from django.urls import urls, include

router = DefaultRouter()
router.register(r'', MetahunterViewSet)
router.register(r'', DeckViewSet)
router.register(r'', CardViewSet)


urlpatterns = [
	url(r'^metahunter/', include(router.urls) ),
    url(r'^admin/', admin.site.urls),
]
