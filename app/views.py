"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'year':datetime.now().year,
        }
    )

def services(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/services.html',
        {
            'year':datetime.now().year,
        }
    )

def estimate(request):
    """Renders the estimate page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/estimate.html',
        {
            'year':datetime.now().year,
        }
    )

def gallery(request):
    """Renders the gallery page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/gallery.html',
        {
            'year':datetime.now().year,    
        }
    )

def projects(request):
    """Renders the gallery page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/projects.html',
        {
            'year':datetime.now().year,    
        }
    )

def tree(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tree.html',
        {
            'year':datetime.now().year,
        }
    )

def concrete(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/concrete.html',
        {
            'year':datetime.now().year,
        }
    )

def zeroscaping(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/zeroscaping.html',
        {
            'year':datetime.now().year,
        }
    )