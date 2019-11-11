from django.contrib import admin
from rest_framework.routers import DefaultRouter
from metahunter.views import MetahunterViewSet, DeckViewSet, CardViewSet
from django.conf.urls import url, include
from django.urls import path

router = DefaultRouter()
router.register(r'metahunter', MetahunterViewSet)
router.register(r'deck', DeckViewSet)
router.register(r'card', CardViewSet)


urlpatterns = [
	path('metahunter/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
