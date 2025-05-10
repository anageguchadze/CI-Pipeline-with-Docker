from django.test import TestCase
from .models import Animal

class AnimalModelTest(TestCase):
    def setUp(self):
        Animal.objects.create(name="Leo", species="Lion", age=5, habitat="Savannah")

    def test_animal_str_method(self):
        animal = Animal.objects.get(name="Leo")
        self.assertEqual(str(animal), "Leo (Lion)")

    def test_animal_fields(self):
        animal = Animal.objects.get(name="Leo")
        self.assertEqual(animal.age, 5)
        self.assertEqual(animal.habitat, "Savannah")
