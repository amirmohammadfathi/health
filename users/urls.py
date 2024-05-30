from django.urls import path
from .views import AthleteAPIView, CompleteInfoAPIView, BodySizeAPIView, DiseaseAPIView, SetPracticesToAthleteAPIView

urlpatterns = [
    path('athletes/', AthleteAPIView.as_view(), name='athlete-list'),
    path('athletes/<int:pk>/', AthleteAPIView.as_view(), name='athlete-detail'),
    path('completeinfo/', CompleteInfoAPIView.as_view(), name='completeinfo-list'),
    path('completeinfo/<int:pk>/', CompleteInfoAPIView.as_view(), name='completeinfo-detail'),
    path('bodysize/', BodySizeAPIView.as_view(), name='bodysize-list'),
    path('bodysize/<int:pk>/', BodySizeAPIView.as_view(), name='bodysize-detail'),
    path('disease/', DiseaseAPIView.as_view(), name='disease-list'),
    path('disease/<int:pk>/', DiseaseAPIView.as_view(), name='disease-detail'),
    path('practice/<int:pk>/', SetPracticesToAthleteAPIView.as_view(), name="get-or-create-practice"),
]
