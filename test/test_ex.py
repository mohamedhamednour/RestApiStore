import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

clinet = APIClient
@pytest.mark.django_db
def test_register_user():

    payload = dict(
        username= 'hamed',
        password= '01004228285P@ssw0rd',
        email='mohamedhame2ed@gmail.com',
        first_name="mohamed",
        last_name='hamed',


    )
    responce = clinet.post('/auth/register/' , payload)
    data = responce.data
    assert data['last_name'] == payload['last_name']
@pytest.mark.django_db
def test_login_user():

    payload = dict(
        username= 'hamed',
        password= '01004228285P@ssw0rd',
        email='mohamedhame2ed@gmail.com',
        first_name="mohamed",
        last_name='hamed',


    )
    responce = clinet.post('/auth/login/' , dict(
        username= 'hamed',
        password= '01004228285P@ssw0rd'
    ))

    assert responce.status_code == 200


#
# @pytest.fixture
# def new_user_factory(db):
#
#     def create_app_user(
#
#         username: str = 'hamed',
#         password: str = '01004228285P@ssw0rd',
#         email: str ='mohamedhame2ed@gmail.com',
#         first_name: str ="mohamed",
#         last_name: str = 'hamed' ,
#     ):
#         user = User.objects.create_user(
#             username=username,
#             password=password,
#             email=email,
#             first_name=first_name,
#             last_name=last_name
#     )
#         return user
#     return create_app_user
# @pytest.fixture
# def new_user(db , new_user_factory):
#     return  new_user_factory('mohamedhamednour' , '01005814378' , 'mohamedhaemd@gmail.com' , 'mohamed' , 'hamed')
#
#
#
# def test_user(new_user):
#     print(new_user)
#     assert new_user.first_name == 'mohamed'
