from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)

    def test_azamjon_page_status_code(self):
        response = self.client.get('/azamjon/')
        self.assertEqual(response.status_code, 200)

    def test_projects_page_status_code(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)