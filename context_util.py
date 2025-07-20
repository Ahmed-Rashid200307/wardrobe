from home.models import Category

def category_context(request):
    return {'category': Category.objects.all()}

