from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('login/',views.index1),
    path('data/',views.data),
    path('table/',views.table1),
    path('ragistration/',views.ragistration),
    path('contact/', views.contactdetails),
    path('cont/', views.contact1)
  
]
