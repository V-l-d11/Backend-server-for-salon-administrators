from django.urls import path
from .views import UserDetail, UserList, helloWorld,WorkerM,WorkerListM,ServiceListM,ServiceM,KlientM,KlientListM,create_appointment,available_staff, RecordListCreateAPIView,RecordCreateAPIView

urlpatterns = [
    path('users/', UserList.as_view(), name='Users'),
    path('user/<int:pk>/', UserDetail.as_view(), name='User'),
    path('hello/', helloWorld, name='hello'),
    path('workers/', WorkerListM.as_view(), name='Workers'),
    path('worker/<int:pk>/', WorkerM.as_view(), name='Worker'),
    path('services/',ServiceListM.as_view(), name='Services'),
    path('service/<int:pk>/',ServiceM.as_view(),name='Service'),
    path('klients/',KlientListM.as_view(), name='Klients'),
    path('klient/<int:pk>/', KlientM.as_view(),name='Klient'),
    path('available_staff/<str:datetime_requested>/<str:service_required>/',available_staff, name='available_staff'),
    path('records/', RecordListCreateAPIView.as_view(), name='record-list-create'),
    path('records/create/', RecordCreateAPIView.as_view(), name='record-create')
]

