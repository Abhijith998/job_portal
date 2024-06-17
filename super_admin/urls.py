from django.urls import path

from super_admin import views


urlpatterns = [

 path('super_admin',views.super_admin,name='super_admin'),
  path('total_checkers',views.total_checkers,name='total_checkers'),
   path('total_makers',views.total_makers,name='total_makers'),
   path('total_employees',views.total_employees,name='total_employees'),

]