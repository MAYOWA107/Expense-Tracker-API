from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView,  RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.timezone import now
from datetime import timedelta
#from django_filters.rest_framework import OrderingFilter
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from .models import Expense
from .serializers import ExpenseSerializer




class ExpenseTrackCreateView(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    



class ExpenseTrackListView(ListAPIView):
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['categotry']
    ordering_fields = ['date', 'id', 'categotry']
    #permission_classes = [IsAuthenticated]
    
    


    def get_queryset(self):
        
        expense = Expense.objects.filter(user=self.request.user)
        #all lists
        if self.request.query_params.get('all'):
            return expense.objects.all()
        
        # list for the last 7 days
        if self.request.query_params.get('past_week'):
            return expense.objects.filter(date__gte=now() - timedelta(weeks=1))

        #list for the last 1 month           
        if self.request.query_params.get('last_month'):
            return expense.objects.filter(date__gt=now() - timedelta(weeks=4))
        
        # list for the last 3 months
        if self.request.query_params.get('last_3_months'):
            return expense.objects.filter(date__gt=now() - timedelta(weeks=12))
         # list for between start date and end date

        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            return expense.objects.filter(date__range=[start_date, end_date])
        
        return expense.objects.all()

class ExpenseTrackDetail(RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

