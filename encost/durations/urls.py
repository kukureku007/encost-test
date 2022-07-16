from django.urls import path

from .views import duration_list
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('list/', duration_list, name="product-list")
]