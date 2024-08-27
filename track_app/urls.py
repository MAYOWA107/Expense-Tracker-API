from django.urls import path
from .views import ExpenseTrackCreateView, ExpenseTrackDetail, ExpenseTrackListView




urlpatterns = [
    path('create/', ExpenseTrackCreateView.as_view(), name='create'),
    path('expense/<int:pk>', ExpenseTrackDetail.as_view(), name='detail'),
    path('', ExpenseTrackListView.as_view(), name='list'),
]