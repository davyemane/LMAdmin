# culture/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('<int:langue_id>/', ElementCulturelListView.as_view(), name='element_culturel_list'),
    path('<int:langue_id>/element/<int:pk>/', ElementCulturelDetailView.as_view(), name='element_culturel_detail'),
    path('<int:langue_id>/create/', ElementCulturelCreateView.as_view(), name='element_culturel_create'),
    path('<int:langue_id>/element/<int:pk>/update/', ElementCulturelUpdateView.as_view(), name='element_culturel_update'),
]