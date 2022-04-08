from django.urls import path

from . import views

urlpatterns = [
    path('sgn', views.sgn, name='sgn'),
    path('setRules', views.setRules, name='setRules'),
    path('set', views.setSQLFilter, name='setSQLFilter'),   
    path('<str:black_list_ip>/BlackListRemove', views.BlackListRemove, name='BlackListRemove'), 
    path('<str:white_list_ip>/WhiteListRemove', views.WhiteListRemove, name='WhiteListRemove'), 
    path('<str:sql_filter_rule>/SQLFilterRemove', views.SQLFilterRemove, name='SQLFilterRemove'), 
    path("regi", views.register, name="register"),

    path('', views.setWAF, name='setWAF'),   

    #path('', views.index, name='index'),
]