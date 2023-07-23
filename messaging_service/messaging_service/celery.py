# messaging_service/celery.py
import os
from celery import Celery

# Указываем Django, где найти настройки проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messaging_service.settings')

# Создаем экземпляр Celery
app = Celery('messaging_service')

# Загружаем настройки Celery из файла настроек Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически обнаруживаем и регистрируем все задачи приложений Django
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
