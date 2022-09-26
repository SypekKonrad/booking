from django.test import TestCase

class CustomerPollTestCase(TestCase):
    def test_form(self):
        response1 = self.client.post("/booking/poll/", {"first_name": "janusz"},)
                                    # {"surname": "pawlacz"}
                                    # {"phone_number": "12345678"},)
        response2 = self.client.post("/booking/poll/", {"surname": "pawlacz"},)
        # print(response.context["form"]["phone_number"].errors)
        # print(response.context["form"]["first_name"].errors)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.context["form"]["first_name"].errors, [])
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


class CustomerListTestCase(TestCase):
    def test_customer_list(self):
        response = self.client.get('details/<int:vehicle_id')
        self.assertEqual(response.status_code, 404)

class IndexTestCase(TestCase):
    def test_index(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)


# Create your tests here.
