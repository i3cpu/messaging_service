from django.shortcuts import render

from django.utils import timezone
from rest_framework.response import Response

from rest_framework import generics, mixins, status
from .models import Client, Campaign, Message
from .serializers import ClientSerializer, CampaignSerializer, MessageSerializer
from .tasks import send_scheduled_message
from .tasks import send_message


class ClientListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClientRetrieveUpdateDeleteView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CampaignListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def get(self, request, *args, **kwargs):
        
        return self.list(request, *args, **kwargs)
    
    def get_message_data_list(self, request_data):
        try:
            serializer = self.get_serializer(data=request_data)
            serializer.is_valid(raise_exception=True)

            client_filter_mobile_operator_code = serializer.validated_data.get('client_filter_mobile_operator_code')
            client_filter_tag = serializer.validated_data.get('client_filter_tag')
            selected_clients = Client.objects.all()
            if client_filter_mobile_operator_code:
                selected_clients = selected_clients.filter(mobile_operator_code=client_filter_mobile_operator_code)
            if client_filter_tag:
                selected_clients = selected_clients.filter(tag=client_filter_tag)
                self.perform_create(serializer)

            message_data_list = []
            for client in selected_clients:
                message_data = {
                        "created_datetime": timezone.localtime(),
                        "status": "Pending",
                        "campaign": serializer.instance.id,
                        "client": client.id,
                    }
                message_data_list.append(message_data)

            return message_data_list
        except:
            return None
            


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        start_datetime = serializer.validated_data.get('start_datetime')
        end_datetime = serializer.validated_data.get('end_datetime')
        
        if timezone.localtime()>=start_datetime and timezone.localtime()<=end_datetime:
            message_data_list = self.get_message_data_list(request_data=request.data)
            if message_data_list:
                send_status=send_message(message_data_list=message_data_list)
                if send_status == 200:
                    for message_data in message_data_list:
                        message_serializer = MessageSerializer(data=message_data)
                        message_serializer.is_valid()
                        message_serializer.save()

                    headers = self.get_success_headers(serializer.data)
                    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) 
                else:
                    context ={
                        'error': f"Message not sent: {send_status}"
                    }
                    return Response(context)
        
        elif timezone.localtime()<start_datetime:

            message_data_list = self.get_message_data_list(request_data=request.data)
            if message_data_list:

                send_scheduled_message.apply_async(args=[message_data_list], eta=start_datetime)
                context = {
                'message':"message will be send"
                }
                return Response(context, status=status.HTTP_201_CREATED)
            
        context = {
            'error':"Wrong data"
            }
        return Response(context, status = status.HTTP_400_BAD_REQUEST)
            

class CampaignRetrieveUpdateDeleteView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class MessageListCreateView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MessageRetrieveUpdateDeleteView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
