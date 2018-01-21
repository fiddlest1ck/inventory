"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static


from items_inventory.views import (HomeView, RecordsView, RecordsAddView,
                                   RecordsUploadView, RecordsDeleteView,
                                   ReportView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='authentication/login.html'), name='logout'),
<<<<<<< HEAD
    path('report/', ReportView.as_view(template_name='records/summary.html'), name='report'),
=======
>>>>>>> 0d767704defd996347f24f576fb1c103dd62fa2a
    path('', HomeView.as_view(), name='home'),
    path('records/', RecordsView.as_view(), name='records'),
    path('records/add', RecordsAddView.as_view(), name='record_add'),
    path('records/edit/<int:pk>', RecordsUploadView.as_view(), name='record_edit'),
    path('records/delete/<int:pk>', RecordsDeleteView.as_view(), name='record_delete')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
