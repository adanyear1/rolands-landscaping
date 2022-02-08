"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)

    def test_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertContains(response, 'Contact', 3, 200)

    def test_about(self):
        """Tests the about page."""
        response = self.client.get('/about')
        self.assertContains(response, 'About', 3, 200)

    def test_services(self):
        """Tests the about page."""
        response = self.client.get('/services')
        self.assertContains(response, 'Services', 3, 200)

    def test_estimate(self):
        """Tests the about page."""
        response = self.client.get('/estimate')
        self.assertContains(response, 'Estimate', 3, 200)

    def test_gallery(self):
        """Tests the gallery page."""
        response = self.client.get('/gallery')
        self.assertContains(response, 'Gallery', 3, 200)

    def test_projects(self):
        """Tests the projects page"""
        response = self.client.get('/projects')
        self.assertContains(response, 'Projects', 3, 200)

    def test_tree(self):
        """Tests the projects page"""
        response = self.client.get('/tree')
        self.assertContains(response, 'Tree', 3, 200)

    def test_concrete(self):
        """Tests the projects page"""
        response = self.client.get('/concrete')
        self.assertContains(response, 'Concrete', 3, 200)

    def test_zeroscaping(self):
        """Tests the projects page"""
        response = self.client.get('/zeroscaping')
        self.assertContains(response, 'Zeroscaping', 3, 200)
    