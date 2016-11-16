import vk
import time
import datetime

from OpenWeatherMap import translate, location, WhatIsCLoudness, typeOfWind
from OpenWeatherMap import weather

session = vk.Session('e86c9064962ffc8ddeeb2cc14ea6c2b62b5b235ef3c4212b5f8ff47008648474ea67587d5a4f340f35343')

api = vk.API(session)

while (True):

    messages = api.messages.get()

    commands = ['Погода', 'стих', 'Privet', 'Poka', '', 'help', 'weather']

    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]

    for m in messages:
        user_id = m[0]
        message_id = m[1]
        comand = m[2]

        date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

        if comand == 'help':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>VKBot v0.1\n>Разработал: Elagin')
        if comand == 'стих':
            api.messages.send(user_id=user_id,
                              message='\nНочь, улица, фонарь, аптека,\nБессмысленный и тусклый свет.\nЖиви еще хоть четверть века —\nВсе будет так. Исхода нет.\nУмрешь — начнешь опять сначала\nИ повторится все, как встарь:\nНочь, ледяная рябь канала,\nАптека, улица, фонарь.\n')
        if comand == 'Privet':
            api.messages.send(user_id=user_id,
                              message='\n>Привет \nРазработал: Elagin')
        if comand == 'Poka':
            api.messages.send(user_id=user_id,
                              message='\n>Пока \nРазработал: Elagin')
        if comand == 'weather':
            api.messages.send(user_id=user_id,
                              message='Погода в городе ' + translate[location.get_name()] + ' (' + translate[
                                  location.get_country()] + ')' +
                                      ' на сегодня в ' + str(datetime.datetime.now().strftime(
                                  '%H:%M')) + ' ' + WhatIsCLoudness() + ', облачность составляет ' +
                                      str(weather.get_clouds()) + '%, давление ' + str(
                                  weather.get_pressure()['press']) + ' мм. рт. ст., температура '
                                      + str(
                                  int(weather.get_temperature('celsius')['temp'])) + ' градусов Цельсия, ночью ' +
                                      str(int(weather.get_temperature('celsius')['temp_min'])) + ', днем ' + str(
                                  int(weather.get_temperature('celsius')['temp_max'])) +
                                      '. Ветер ' + typeOfWind() + ' ' + str(weather.get_wind()['speed']) + ' м.\с.')

    ids = ', '.join([str(m[1]) for m in messages])

    if ids:
        api.messages.markAsRead(message_ids=ids)

    time.sleep(3)
