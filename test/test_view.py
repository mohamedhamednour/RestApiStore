from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ProjectApp.models import Product

class ViewTest(TestCase):

    def test_all_product(self):
        response = self.client.get(reverse('allproduct'))
        self.assertEqual(response.status_code, 200)

    def test_serch_name(self):
        # user = User.objects.create_user(id=2, username='hamednour', password='password')
        #
        # product = Product.objects.create(admin=user, name='polo', price=300.0)

        response = self.client.get(reverse('orderby_price'))
        self.assertEqual(response.status_code, 200)