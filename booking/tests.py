from django.contrib.auth.models import User
from django.test import TestCase, LiveServerTestCase
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

from booking.models import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

# class CustomerListTestCase(TestCase):
#     pass








class CustomerPollTest(LiveServerTestCase):

    def testpoll(self):

        driver = webdriver.Firefox(executable_path=r'D:\geckodriver.exe')
        driver.get('http://127.0.0.1:8000/booking/poll/')

        # first_name = driver.find_element_by_name("first_name")
        # surname = driver.find_element_by_name("surname")
        #
        # submit = driver.find_element_by_class_name("submit")

        first_name = driver.find_element(By.NAME, "first_name")
        surname = driver.find_element(By.NAME, "surname")
        phone_number = driver.find_element(By.NAME, "phone_number")
        email = driver.find_element(By.NAME, "email")
        make = driver.find_element(By.NAME, "make")
        model = driver.find_element(By.NAME, "model")
        body_type = driver.find_element(By.NAME, "body_type")
        production_year = driver.find_element(By.NAME, "production_year")
        fuel_type = driver.find_element(By.NAME, "fuel_type")
        engine_displacement = driver.find_element(By.NAME, "engine_displacement")
        transmission = driver.find_element(By.NAME, "transmission")
        horsepower = driver.find_element(By.NAME, "horsepower")
        service = driver.find_element(By.NAME, "service")


        submit = driver.find_element(By.CLASS_NAME, "btn")

        first_name.send_keys('Lucas')
        surname.send_keys('Zimmerman')
        phone_number.send_keys('123456789')
        email.send_keys('lucas.zimmerman@gmail.com')
        make.send_keys('BMW')
        model.send_keys('320i')
        body_type.send_keys('sedan')
        production_year.send_keys('2000')
        fuel_type.send_keys('gasoline')
        engine_displacement.send_keys('1991')
        transmission.send_keys('automatic')
        horsepower.send_keys('150')
        service.send_keys('gearbox oil change')

        submit.send_keys(Keys.RETURN)



















# Create your tests here.
