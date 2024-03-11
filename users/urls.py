from django.urls import path
from .views import UserDetail, UserList, helloWorld,ServiceListM,ServiceM,KlientM,KlientListM,create_appointment,available_staff, RecordListCreateAPIView,RecordCreateAPIView,WorkerRetrieveUpdateDestroyAPIView,WorkerListCreateAPIView

urlpatterns = [
    path('users/', UserList.as_view(), name='Users'),
    path('user/<int:pk>/', UserDetail.as_view(), name='User'),
    path('hello/', helloWorld, name='hello'),
    path('workers/', WorkerListCreateAPIView.as_view(), name='worker-list-create'),
    path('workers/<int:pk>/', WorkerRetrieveUpdateDestroyAPIView.as_view(), name='worker-retrieve-update-destroy'),
    path('services/',ServiceListM.as_view(), name='Services'),
    path('service/<int:pk>/',ServiceM.as_view(),name='Service'),
    path('klients/',KlientListM.as_view(), name='Klients'),
    path('klient/<int:pk>/', KlientM.as_view(),name='Klient'),
    path('available_staff/<str:datetime_requested>/<str:service_required>/',available_staff, name='available_staff'),
    path('records/', RecordListCreateAPIView.as_view(), name='record-list-create'),
    path('records/create/', RecordCreateAPIView.as_view(), name='record-create')
]

