from firebase import firebase

URL = 'https://mobile-waiter-4ed9f.firebaseio.com/'

fb = firebase.FirebaseApplication(URL, None)
# По хорошему можно сделать аутентификацию с ключом. Вроде делается просто, 2-3 строчки (Но оно нам надо?)
result = fb.get('/Restaurant', '00000001')                  # Чтение.
# Формат /ИМЯ ТАБЛИЦЫ/КЛЮЧ (Для добавления). Данный метод не добавляет копию данных если существуют с таким же ключом,
# а перезаписывает. Используем вместо put и post (ибо странно работают)
fb.patch('/Restaurant/11111111', data={'Name': 'EST'})      # Добавление.
result = fb.get('/Restaurant', '11111111')
# fb.delete('/Restaurant', '111111111')                     # Удаление.
print(result)



