from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # Add permission classes as required


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """
        This view should return a list of all reviews
        for the model as determined by the content_type and object_id portion of the URL.
        """
        model_type = self.kwargs['model_type']
        object_id = self.kwargs['object_id']
        # Logic to return reviews based on model_type and object_id
