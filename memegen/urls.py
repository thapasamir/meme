from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import  views
urlpatterns = [
    path('',views.home,name="home"),
    path('log_in',views.log_in,name="log_in"),
    path('log_out',views.log_out,name="log_out"),
    path('signup',views.signup,name="signup"),
    path('about',views.about,name="about"),
    path('article',views.article,name="article"),
    path('cateogry',views.cateogry,name="cateogry"),
    path('explore/<str:id>',views.explore,name="explore"),
    path('createcateogry',views.createcateogry,name="createcateogry"),
    path('createpost',views.createpost,name="createpost"),
    path('managepost/<str:id>',views.managepost,name="managepost")
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)