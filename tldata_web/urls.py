"""tldata_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
import home_page.views as hv
import atlmkt_dash.views as av
import atlmkt_dash.plotly_test

urlpatterns = [
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('', hv.home_view, name="home_page"),
    path('atlmktdash', av.atlmktdash_view, name="atlmkt_dash"),
]
