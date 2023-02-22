from django.test import TestCase
from ProjectApp.models import Product
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(id=2, username='hamednour', password='password')

        Product.objects.create(admin=user, name='polo', price=300.0)

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_product_detils(self):
        author = Product.objects.get(id=1)
        expected_object_name = f'{author.name}'
        self.assertEqual(str(author), expected_object_name)

    # def test_valid_form(self):
    #     user = User.objects.create_user(id=2, username='hamednour', password='password')
    #     validData = Product.objects.create(admin=user, name='zara-shirt', price=250.0)
    #     self.assertTrue(validData)



# class AccountTests(APITestCase):
#     def test_create_product(self):
#         user = User.objects.create_user(id=2, username='hamednour', password='password')
#         data = {'admin': user, 'name': 'Zara', 'price': 260.0}
#         response = self.client.post(reverse('productss'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Product.objects.count(), 1)
#         self.assertEqual(Product.objects.get().name, 'Zara')