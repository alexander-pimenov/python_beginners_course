# Собираем логи и наблюдаем их в Kibana
# Для демонстрации я напишу простое python приложение,
# которое лишь собирает некоторые метрики хоста и складывает в лог-файл в формате json.
import datetime
import json
import os
from time import sleep

import psutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    load1, load5, load15 = psutil.getloadavg()
    ram_usage_percent = psutil.virtual_memory().percent

    log = {
        'load_avg': {
            'load1': load1,
            'load5': load5,
            'load15': load15,
        },
        'ram_usage_percent': ram_usage_percent,
        # это создаст время с учётом часового пояса UTC:
        'asctime': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='milliseconds', sep=' ')
        # 'asctime': datetime.datetime.utcnow().isoformat(timespec='milliseconds', sep=' ')
    }

    with open(os.path.join(BASE_DIR, 'host_metrics_app.log'), 'a') as f:
        f.write(json.dumps(log) + '\n')

    sleep(7)


# Тут ест использование деструктивного присваивание - распаковка кортежа - load1, load5, load15 = psutil.getloadavg(),
# это когда каждый элемент кортежа "ложится" на указанную переменную.
# Вот пример из более ранних проектов:
# user_roles = ("admin", "editor", "viewer")
# role_1, role_2, role_3 = user_roles
# print(role_1)  # Outputs: "admin"
# print(role_2)  # Outputs: "editor"
# print(role_3)  # Outputs: "viewer"

