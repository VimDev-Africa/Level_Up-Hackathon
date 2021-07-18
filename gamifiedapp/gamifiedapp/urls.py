"""gamifiedapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from methods import method

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', method.Badge.as_view()),
    
    path('badge/', method.Badge.as_view()),
    path('reg_player/', method.User_reg.as_view()),
    path('objective/', method.Objective.as_view()),
    path('login/', method.Login.as_view()),
]

