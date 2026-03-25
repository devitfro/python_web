from django.urls import path
from . import views

urlpatterns = [
    path('data/item/<int:item_id>/', views.get_item),
    path('restricted-area/', views.restricted_view),
    path('json/', views.process_json),
    path('check-device/', views.check_device),
    path('mobile-page/', views.mobile_page),
    path('data/<str:key>/', views.get_data),
    path('update-data/', views.update_data),
]