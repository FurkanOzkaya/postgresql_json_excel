from django.urls import path, include
from core.api.views import ColumnView
from core.api.views import DataView

urlpatterns = [
    path('get-data/', DataView.as_view()),
    path('post-data/', DataView.as_view()),
    path('delete-data/<pk>', DataView.as_view()),
    path('update-data/<pk>', DataView.as_view()),
    path('post-column/', ColumnView.as_view()),
]