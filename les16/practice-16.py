# Реализуйте систему управления расписанием на Python, используя ООП и наследование.
# Создайте базовый класс Event (событие), от которого наследуются два класса: Meeting (встреча) и Call (звонок). 
# Импортируйте модуль datetime для работы с датой и временем.

# Атрибуты класса Event:

# title — название события
# start_time — время начала (datetime)
# end_time — время окончания (datetime)
# participants — список участников
# location — место проведения
# description — описание события
# Методы класса Event:

# duration() — возвращает длительность события в минутах
# add_participant(name) — добавляет участника
# conflicts_with(other_event) — проверяет, пересекается ли событие с другим по времени
# __str__() — строковое представление события
# Класс Meeting наследует Event и добавляет:

# agenda — список пунктов повестки
# add_agenda_item(item) — добавить пункт к повестке
# send_invites() — имитирует рассылку приглашений участникам (печатает сообщения)
# Класс Call наследует Event и добавляет:

# call_link — ссылка на звонок (строка)
# recording — флаг, будет ли запись звонка
# start_recording() — “начинает” запись (устанавливает флаг и пишет в лог)
# end_recording() — “останавливает” запись
# Внешняя функция schedule_events(events_list) (принимает список событий любого типа):

# Сортирует события по времени начала
# Проверяет, есть ли пересечения между событиями, и сообщает о конфликтах
# Выводит итоговое расписание на день
# Дополнительные условия:

# Проверьте пример: организуйте три события (две встречи с пересечением и один звонок) с разными параметрами
# Например: встреча команды в офисе, плановый звонок по проекту, встреча с клиентом в кафе
# Проверьте методы: добавьте участников, пункты повестки, проверьте конфликтность, начните и завершите запись звонка

from datetime import datetime

start = datetime(2025, 6, 5, 10, 0)
end = datetime(2025, 6, 5, 11, 0)

def duration(start, end):
    delta = end - start
    return int(delta.total_seconds() // 60)

print(duration(start, end))

def conflict_with(self, other_event):
    latest_start = max(self.start_time, other_event.start_time)
    earliest_end = min(self.end_time, other_event.end_time)
    overlap = (earliest_end - latest_start).total_seconds()
    return overlap > 0
