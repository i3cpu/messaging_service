# messaging/tasks.py
from celery import shared_task
from django.utils import timezone
from .models import Campaign, Client, Message
from .send_msg import send



def send_message(message_data_list):

    for message_data in message_data_list:
        campaign_message = Campaign.objects.get(id=message_data['campaign']).message_text
        client_id = message_data['client']
        client_phone = Client.objects.get(id=client_id).phone_number

        status = (send(client_id, client_phone, campaign_message ))
        return status

@shared_task
def send_scheduled_message(message_data_list):
    if message_data_list:
        send_status = send_message(message_data_list=message_data_list)
        print(send_status)
        if send_status==200:
            for message_data in message_data_list:
                created_datetime = message_data['created_datetime']
                status = message_data['status']
                campaign = Campaign.objects.get(id=message_data['campaign'])
                client = Client.objects.get(id=message_data['client'])
                message = Message(created_datetime=created_datetime, status=status, campaign=campaign, client=client)
                message.save()
                print('Success')
                    

            


