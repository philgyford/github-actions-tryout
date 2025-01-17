from packaging.version import Version

import django
from django.test import TestCase


class VersionTestCase(TestCase):

    def test_django_version(self):
        if Version(django.get_version()) >= Version("5.1.0"):
            self.fail("Django is >= 5.1.0")
