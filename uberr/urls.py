from django.urls import path
from .views import ClientInfoView, DestinationView, MainPageView, AddClientView

urlpatterns = [
    path('', MainPageView.as_view(), name="index"),
    path('client-profile/<int:client_id>', ClientInfoView.as_view(), name="client-profile"),
    path('add-client-profile', AddClientView.as_view(), name="add-client-profile"),
    path('destination', DestinationView.as_view(), name="add-order")

]