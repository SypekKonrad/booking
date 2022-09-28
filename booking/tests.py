from django.contrib.auth.models import User
from django.test import TestCase
from booking.models import *

class CustomerPollTestCase(TestCase):
    def test_form_erorrs(self):
        response = self.client.post("/booking/poll/", {},)

        # response2 = self.client.post("/booking/poll/", {"surname": "pawlacz"},)
        # print(response.context["form"]["phone_number"].errors)
        # print(response.context["form"]["first_name"].errors)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["form"]["first_name"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["surname"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["phone_number"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["email"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["make"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["model"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["body_type"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["production_year"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["fuel_type"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["engine_displacement"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["transmission"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["horsepower"].errors, ['This field is required.'])
        self.assertEqual(response.context["form"]["service"].errors, ['This field is required.'])

    def test_form_success(self):
        response = self.client.post("/booking/poll/", {
            "first_name": "janusz",
            "surname": "pawlacz",
            "phone_number": "123456789",
            "email": "janusz.pawlacz@gmail.com",
            "make": "Volkswagen",
            "model": "Passat",
            "body_type": "wagon",
            "production_year": "1999",
            "fuel_type": "diesel",
            "engine_displacement": "1998",
            "transmission": "manual",
            "horsepower": "110",
            "service": "oil service",
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'thx' in response.content)
        self.assertEqual(Customer.objects.count(), 1)
        customer=Customer.objects.get()
        self.assertEqual(customer.first_name, 'janusz')
        self.assertTrue(Vehicle.objects.exists())



class CustomerServiceDetailTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user=User.objects._create_user(username='sypek', password='haslohaslo123', email='konrad.sypek@o2.pl')

    def test_customer_list(self):
        customer = Customer.objects.create(
            first_name='Janusz',
            surname='Pawlacz',
            email='janusz.pawlacz@gmail.com',
            phone_number='123456789'
        )
        vehicle = Vehicle.objects.create(
            customer=customer,
            make='Volkswagen',
            model='Passat',
            body_type='wagon',
            production_year=int(1999),
            fuel_type='diesel',
            engine_displacement=int(1998),
            transmission='manual',
            horsepower=int(110),
            service='oil service'
        )
        self.client.force_login(self.user)
        response = self.client.get('/booking/details/'+str(vehicle.id))
        self.assertEqual(response.status_code, 200)
    def test_customer_list_not_logged_in(self):
        response = self.client.get('/booking/details/1')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/booking/login/', fetch_redirect_response=False)

class IndexTestCase(TestCase):
    def test_index(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)

class CustomerListTestCase(TestCase):

# Create your tests here.
