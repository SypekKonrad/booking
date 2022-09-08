from django.test import TestCase

class CustomerPollTestCase(TestCase):
    def test_form(self):
        response = self.client.post("/booking/poll/", {"first_name": "janusz"},)
        # print(response.context["form"]["phone_number"].errors)
        # print(response.context["form"]["first_name"].errors)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["form"]["first_name"].errors, [])
        self.assertEqual(response.context["form"]["phone_number"].errors, ['This field is required.'])


# Create your tests here.
