from .models import Category


def categories_processor(request):
    """Add all categories to the template context as `categories`."""
    return {
        'categories': Category.objects.all()
    }
