from django.urls import path

from maker_app import views


urlpatterns = [
    path('maker_register',views.maker,name='maker'),
    path('maker_login',views.maker_login,name='maker_login'),
    path('maker_page',views.maker_page,name='maker_page'),
    path('applications_received',views.applications_received,name='applications_received'),
    path('my_applications',views.my_applications,name='my_applications')



]