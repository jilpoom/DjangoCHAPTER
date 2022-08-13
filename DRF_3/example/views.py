from rest_framework import viewsets, permissions, generics, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer


# FBV(Function Based View)
@api_view(['GET'])
def helloAPI(request):
    return Response("hello, World!")

@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) #return Response 200
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
    # POST 요청으로 들어온 데이터, 시리얼라이저에 집어넣기
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED) # 생성 완료 HTTP 201
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 유효한 데이터가 아니라면 400 ERROR

@api_view(['GET'])
def bookAPI(request, bid): #/book/bid/
    book = get_object_or_404(Book, bid=bid) #bid = id 인 데이터를 Book에서 가져오고 없다면 404 에러
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK) # return Response 200
    

# CBV(Class-Based View)
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


# mixins (시리얼라이저와 모델의 결합)

class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all() # 모델 객체 전체를 가져온다
    serializer_class = BookSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all() #모델 객체 전체를 가져온다.
    serializer_class = BookSerializer # Serializer 클래스 가져오기
    lookup_field = 'bid'
    # lookup_field로 Primary key 설정

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Generics(mixins의 조합)

class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'


# Viewset(중복되는 클래스 선언을 한 번에 줄임, 하나의 클래스로 다중 URL 접근이 가능)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer