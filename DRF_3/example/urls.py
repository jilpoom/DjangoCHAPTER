from django.urls import path, include
from .views import helloAPI, BookAPI, BooksAPI, bookAPI, booksAPI, BookAPIMixins, BooksAPIMixins, BookAPIGenerics, BooksAPIGenerics
from rest_framework import routers
from .views import BookViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls


# urlpatterns = [
#     path('hello/', helloAPI),
#     path('fbv/books/', booksAPI),
#     path('fbv/book/<int:bid>/', bookAPI),
#     path('cbv/books/', BooksAPI.as_view()),
#     path('cbv/book/<int:bid>/', BookAPI.as_view()),
#     path('mixin/books/', BooksAPIMixins.as_view()),
#     path('mixin/book/<int:bid>/', BookAPIMixins.as_view()),
#     path('generic/books/', BooksAPIGenerics.as_view()),
#     path('generic/book/<int:bid>/', BookAPIGenerics.as_view()),

# ]
