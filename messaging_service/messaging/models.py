from django.db import models

# Create your models here.


from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=11, unique=True)
    mobile_operator_code = models.CharField(max_length=10)
    tag = models.CharField(max_length=255)
    timezone = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.phone_number}'

class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    message_text = models.TextField()
    client_filter_mobile_operator_code = models.CharField(max_length=10, blank=True, null=True)
    client_filter_tag = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.message_text}'

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'client {self.client} - {self.campaign} '
