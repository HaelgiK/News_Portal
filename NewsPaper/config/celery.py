import os
from celery import Celery
# Связываем настройки Django с настройками Celery через переменную окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')
# Создаём экземпляр приложения Celery и устанавливаем для него файл конфигурации.
# Указываем пространство имён, чтобы Celery сам находил все необходимые настройки
# в общем конфигурационном файле settings.py.
# Он их будет искать по шаблону «CELERY_***»
app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Указываем Celery автоматически искать задания в файлах tasks.py
# каждого приложения проекта
app.autodiscover_tasks()
