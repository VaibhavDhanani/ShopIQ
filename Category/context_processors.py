from .models import Category
from django.core.cache import cache


def navbar_data(request):
    print("i am context processor")
    try:
        navbar_categories = cache.get("navbar_categories")
        if navbar_categories is None:
            navbar_categories = category = Category.objects.filter(parent__isnull=True).prefetch_related("subcategories")
            cache.set("navbar_categories", navbar_categories, timeout=3600)

        return {
            "navbar_categories": navbar_categories,
        }
    except Exception as e:
        print(f"Error in navbar_data context processor: {str(e)}")
        return {"navbar_categories": [], "navbar_error": str(e)}
