# BixFinalCode
Garage App - JSON CRUD using Django

In order to test the server application, follow the steps mentioned before:

1. First we have to make some test cases in the tests.py file present in  my project's location in Garage2/GarageApp/ which I have already done in my project.

2. My tests.py file lools like below:
  
from django.contrib.auth.models import User
from GarageApp.models import cars, trucks, boats
from rest_framework.test import APITestCase


class GarageTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username="abc", password="abc")
        self.client.login(username="abc", password="abc")
        cars.objects.create(make="Nissan", model="Altima", year=2017, Seats=5, Color="White", VIN="S245882738910K1",
                            Current_Mileage="51,000", Service_Interval="12,000", Next_Service="49,000")
        trucks.objects.create(make= "Tesla", model= "X", year= 2019, Seats= 2,Bed_Length= "100.1200", Color= "Black",
                              VIN="OJOIHIUG2IUYT871",Current_Mileage= "20,000",Service_Interval= "16,000", Next_Service= "30,000")
        boats.objects.create(make= "MasterCraft",model= "Z",year= 2013,Length= "23.10m",Width= "23.40m", Current_Hours= "3.4",
                             HIN="lkhjkl1jiu2j",Service_Interval="10,000", Next_Service="5,000")

    def test_cget(self):
        ref = cars.objects.all()
        self.assertEqual(ref.count(), 1)
        url = 'http://127.0.0.1:8000/cars/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        ref = cars.objects.filter(VIN="S245882738910K1")
        self.assertEqual(ref.count(), 1)

    def test_cpost(self):
        url = 'http://127.0.0.1:8000/cars/'
        data = {
            "make": "Tesla",
            "model": "X",
            "year": 2020,
            "Seats": 5,
            "Color": "White",
            "VIN": "ZQ458827389erQA",
            "Current_Mileage": "50,000",
            "Service_Interval": "10,000",
            "Next_Service": "45,000"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_cput(self):
        url = 'http://127.0.0.1:8000/cars/1/'
        data = {
            "make": "Tesla",
            "model": "X",
            "year": 2020,
            "Seats": 5,
            "Color": "White",
            "VIN": "ZQ458827389erQA",
            "Current_Mileage": "50,000",
            "Service_Interval": "10,000",
            "Next_Service": "45,000"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_cdel(self):
        url = 'http://127.0.0.1:8000/cars/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_tget(self):
        ref = trucks.objects.all()
        self.assertEqual(ref.count(), 1)
        url = 'http://127.0.0.1:8000/trucks/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        ref = cars.objects.filter(VIN="S245882738910K1")
        self.assertEqual(ref.count(), 1)

    def test_tpost(self):
        url = 'http://127.0.0.1:8000/trucks/'
        data = {

            "make": "Tesla",
            "model": "X",
            "year": 2019,
            "Seats": 2,
            "Bed_Length": "100.1200",
            "Color": "Black",
            "VIN": "OJOIHIUG2IUYT871",
            "Current_Mileage": "20,000",
            "Service_Interval": "16,000",
            "Next_Service": "30,000"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_tput(self):
        url = 'http://127.0.0.1:8000/trucks/1/'
        data = {
            "make": "Tesla",
            "model": "X",
            "year": 2018,
            "Seats": 2,
            "Bed_Length": "100.1200",
            "Color": "Black",
            "VIN": "OJOIHIUG2IUYT871",
            "Current_Mileage": "20,000",
            "Service_Interval": "16,000",
            "Next_Service": "30,000"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_tdel(self):
        url = 'http://127.0.0.1:8000/trucks/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_bget(self):
        ref = boats.objects.all()
        self.assertEqual(ref.count(), 1)
        url = 'http://127.0.0.1:8000/boats/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        ref = cars.objects.filter(VIN="S245882738910K1")
        self.assertEqual(ref.count(), 1)

    def test_bpost(self):
        url = 'http://127.0.0.1:8000/boats/'
        data = {
            "make": "Master12",
            "model": "A",
            "year": 2015,
            "Length": "23.12",
            "Width": "24.10",
            "HIN": "lkhjklWSDAiu2j",
            "Current_Hours": "5.5",
            "Service_Interval": "7,000",
            "Next_Service": "20,000"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_bput(self):
        url = 'http://127.0.0.1:8000/boats/1/'
        data = {
            "make": "Zeb",
            "model": "A",
            "year": 2019,
            "Length": "23.12",
            "Width": "24.10",
            "HIN": "kuhkuhk",
            "Current_Hours": "5.5",
            "Service_Interval": "7,000",
            "Next_Service": "20,000"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, 200)

    def test_bdel(self):
        url = 'http://127.0.0.1:8000/boats/1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)


3. In the command line run (in pycharm while the project is opened): python manage.py test


