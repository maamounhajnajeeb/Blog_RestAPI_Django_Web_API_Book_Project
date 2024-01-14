from django.test import TestCase

from .models import Post
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your tests here.

class BlogTest(TestCase):
    
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_user(
            username="admin", email="admin@admin.com", 
            password="admin",
        )
        
        cls.post = Post.objects.create(
            author=cls.user, title="2nd title", 
            body="Hello, World!",
        )
    
    def test_post_model(self):
        post = self.post
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.body, "Hello, World!")
        self.assertEqual(post.title, "2nd title")
        self.assertContains(str(post), "2nd title")
        self.assertEqual(str(self.user), "admin@admin.com")