"""
URL configuration for mytest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.urls import path
# from myapp.views import signup, login
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/signup/', signup, name='signup'),
#     path('api/login/', login, name='login'),
# ]
from django.urls import path
from myapp.views import RegisterAPI, LoginAPI, StudentApi,dipesh, add_to_cart, get_cart_items,remove_cart_item
from django.contrib import admin
from django.urls import path
# from django.conf.urls import url
# from store.views import RegisterAPI, LoginAPI
# from store import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
def homepage(request):
    return HttpResponse("Welcome to Veggy Backend API!")

urlpatterns = [
    path("", homepage),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    
    path('student/',StudentApi, name='student'),
    path('dipesh/',dipesh, name='dipesh'),
    # path(r'^student$',views.studentApi),
    # path(r'^student/([0-9]+)$',views.studentApi),
    # path('signup/', views.register, name='register'),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/add-to-cart/', add_to_cart, name='add_to_cart'),
    path('api/cart/', get_cart_items, name='get_cart_items'),
    path('api/cart/<int:item_id>/', remove_cart_item, name='remove_cart_item'),
    path('admin/', admin.site.urls),
    
]





