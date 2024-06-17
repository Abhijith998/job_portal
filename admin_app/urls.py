


from django.urls import path

from admin_app import views


urlpatterns = [


    path('checker_register',views.checker,name='checker'),
    path('checker_login',views.checker_login,name='checker_login'),
    path('department',views.department,name='department'),
    path('checker_page',views.checker_page,name='checker_page'),
    path('maker_list',views.maker_list,name='maker_list'),
]