from django.test import TestCase
from django.urls import reverse
from core.views import persons, person_detail
from core.models import Person

# Create your tests here.
class All_urls_Test(TestCase):
    def test_personsview_url(self):
        url = reverse('person-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_persondetail_url(self):
        self.person1 = Person.objects.create(name='John Doe', track='backend')

        # if ID exists
        url = reverse('person-detail', kwargs={'id': self.person1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        #if ID doesn't exist
        url = reverse('person-detail', kwargs={'id': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class API_Endpoints(TestCase):
    # CREATE
    def test_valid_Post_data(self):
        data = {
            'name': 'John Doe',
            'track': 'backend',
        }
        url = reverse('person-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Person.objects.filter(name='John Doe', track='backend').exists())

    def test_invalid_Post_data(self):
        data = {
            'name': ' ',
            'track': 'backend',
        }
        url = reverse('person-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(Person.objects.filter(name=' ', track='backend').exists())

    # DELETE
    def test_delete_with_valid_id_api(self):
        self.person1 = Person.objects.create(name='John Doe', track='backend')
        url = reverse('person-detail', kwargs={'id':self.person1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Person.objects.filter(id=self.person1.id).exists())

    def test_delete_with_invalid_id_api(self):
        url = reverse('person-detail', kwargs={'id':100})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 404)

    # READ
    def test_read_details_with_valid_id(self):
        self.person1 = Person.objects.create(name='John Doe', track='backend')
        url = reverse('person-detail', kwargs={'id':self.person1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['name'], 'John Doe')
        self.assertEqual(data['track'], 'backend')
    
    def test_read_details_with_invalid_id(self):
        url = reverse('person-detail', kwargs={'id':100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    # UPDATE
    def test_update_details_with_valid_id(self):
        self.person1 = Person.objects.create(name='John Doe', track='backend')

        data = {
            'name': 'Updated Name',
            'track': 'Mobile',
        }

        url = reverse('person-detail', kwargs={'id':self.person1.id})
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200) 
        updated_person = Person.objects.get(id=self.person1.id)
        self.assertEqual(updated_person.name, 'Updated Name')
        self.assertEqual(updated_person.track, 'Mobile')

    def test_update_details_with_invalid_data(self):
            self.person1 = Person.objects.create(name='John Doe', track='backend')
            data = {
                'name': '',
                'track': 'Mobile',
            }
            url = reverse('person-detail', kwargs={'id':self.person1.id})
            response = self.client.put(url, data, content_type='application/json')
            self.assertEqual(response.status_code, 400)  
            updated_person = Person.objects.get(id=self.person1.id)
            self.assertNotEqual(updated_person.name, '')