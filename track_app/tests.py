from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Expense
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.utils.timezone import now
from datetime import timedelta





class ExpenseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username = 'testing',
            email= 'test@gmail.com',
            last_name = 'test',
            password = 'password',
        )

        cls.expense = Expense.objects.create(
            user= cls.user,
            categotry = 'GROCERIES',
            description= 'Butter',
            amount= 500
        )

    def test_expense_model(self):
        self.assertEqual(self.expense.user.username, 'testing')
        self.assertEqual(self.expense.categotry, 'GROCERIES')
        self.assertEqual(self.expense.description, 'Butter')
        self.assertEqual(self.expense.amount, 500)



#class ExpenseTrackAPITest(TestCase):
 #   @classmethod
  #  def setUpTestData(cls):
   #     cls.client = APIClient()
    #    cls.user = get_user_model().objects.create_user(
     #       username='testing',
      #      password='password'
       # )
        #cls.client.force_authenticate(user=cls.user)
#
 #       cls.expense = Expense.objects.create(
  #          user = cls.user,
   #        description = 'testing groceries',
    #        amount = 50
     #   )
    
    #def test_create_expense(self):

#        self.client.login(username='testing', password='password')
        
 #       data = {
  #          'categotry': 'LEISURE',
   #         'description': 'testing leisure',
    #        'amount': 100,
     #   }

      #  response = self.client.post(reverse('create'))
       # self.assertEqual(response.status_code, status.HTTP_201_CREATED)

   # def test_list_expense(self):

    #    self.client.login(username='testing', password='password')
        
     #   response = self.client.get(reverse('list'))
      #  self.assertEqual(response.status_code, status.HTTP_200_OK)
       # self.assertContains(response, 'testing groceries')

    #def test_filter_by_categotry(self):
        
     #   self.client.login(username='testing', password='password')
      #  response = self.client.get(reverse('list'), {'categotry': 'groceries'})
       # self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertContains(response, 'testing groceries')
        #self.assertEqual(len(response), 1)


    #def test_detail_expense(self):
     #   response = self.client.get(reverse('detail', kwargs = {'pk': self.expense.id}), format='json')
      #  self.assertEqual(response.status_code, status.HTTP_200_OK)
       # self.assertEqual(Expense.objects.count(), 1)
        #self.assertContains(response, 'testing groceries')
