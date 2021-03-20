from rest_framework import viewsets, status
from .models import Book, Journal
from rest_framework.response import Response
from .serializers import BookSerializer, JournalSerializer


class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"data": serializer})
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
