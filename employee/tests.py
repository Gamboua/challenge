from django.test import Client, TestCase


class EmployeeTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_employe_create(self):
        response = self.client.post('/employee/', {
            'name': 'nome fulano',
            'email': 'fulano@nome.com.br',
            'department': 'Development'
        })

        self.assertEqual(response.status_code, 201)

    def test_employee_list(self):
        response = self.client.get('/employee/')

        self.assertEqual(response.status_code, 200)
