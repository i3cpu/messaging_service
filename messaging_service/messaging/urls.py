
from django.urls import path
from messaging.views import (
    ClientListCreateView, ClientRetrieveUpdateDeleteView,
    CampaignListCreateView, CampaignRetrieveUpdateDeleteView,
    MessageListCreateView, MessageRetrieveUpdateDeleteView,
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDeleteView.as_view(), name='client-retrieve-update-delete'),

    path('campaigns/', CampaignListCreateView.as_view(), name='campaign-list-create'),
    path('campaigns/<int:pk>/', CampaignRetrieveUpdateDeleteView.as_view(), name='campaign-retrieve-update-delete'),

    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDeleteView.as_view(), name='message-retrieve-update-delete'),
]
