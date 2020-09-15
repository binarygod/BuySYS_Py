from django.contrib import admin
from django.urls import path, include
from decorator_include import decorator_include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.bg_eveonline_auth.urls')),
    path('', decorator_include(login_required, 'apps.bg_buysys.urls')),
    path('oidc/', include('social_django.urls', namespace='social')),
    # path('', include('apps.bg_buysys.urls')),
]
