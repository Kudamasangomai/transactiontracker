from django.urls import path, include
from .views import transactions, getroutes ,login



urlpatterns = [  
    path('',getroutes,name="api"),
    path('transactions/', transactions, name='transactions'),
     path('login/', login, name='login'),
    # path('api-auth/', include('rest_framework.urls')),

]