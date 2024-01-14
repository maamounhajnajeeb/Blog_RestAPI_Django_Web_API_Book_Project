from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTest(TestCase):
    
    @classmethod
    def setUp(cls) -> None:
        User = get_user_model()
        cls.user = User.objects.create_user(
            username="admin", email="admin@admin.com",
            password="admin1",
        )
    
    def test_user_creation(self):
        user = self.user
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@admin.com")