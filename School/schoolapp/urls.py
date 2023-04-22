from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('login/',views.index1),
    path('login_user/',views.login_user),

    path('data/',views.data),
    path('table/',views.table1),
    path('ragistration/',views.ragistration),
    path('contact/', views.contactdetails),
    path('cont/', views.contact1),
    path('delete/<int:pk>/', views.delete_user, name="delete"),
    path("update/<int:id>/", views.update, name="update"),
    path('update_data/',views.update_data)

]
