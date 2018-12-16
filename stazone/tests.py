from django.test import TestCase
from .models import Profile, Image

# Create your tests here.

class ImageTestClass(TestCase):

    def setUp(self):
        self.profile = Profile(bio='My bio')
        self.profile.save_profile()
        self.image = Image(name='name.jpg',caption='Holiday moments',profile=self.profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_img()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    def test_delete_method(self):
        self.image.save_image()
        self.image.del_image()


class ProfileTestClass(TestCase):

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)


    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.del_profile()


