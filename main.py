import os, base64, time
from platform import platform
from SimpleQIWI import *
import os, time, os.path
#-*- coding: utf-8 -*-
puk = platform()[0], platform()[1], platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
	delet = 'cls'
	dr = '\\'
else:
	delet = 'clear'
	dr = '/'


print('\nПодождите...')

time.sleep(5)
os.system(delet)


while True:
	token=input('Токен (qiwi.com/api): ')
	phone=input('Номер телефона (без +): ')
	api = QApi(token=token, phone=phone)

	def info():
		try:
			print('Кошелек найден!')
			print('Баланс клиента с номером ', phone, ' равен (RUB): ', api.balance)
		except:
			print('Ошибка 2. Невозможно осуществить поиск из-за проблем с кошельком.')

	def vanish():
		summ = input('Введите сумму (от 1 рубля): ')
		num = input('Номер кошелька (79ххххххххх): ')
		comment = input('Комментарий к переводу: ')
		try:
			api.pay(account = str(num), amount = int(summ), comment = str(comment))
			print('Баланс клиента с номером', phone, 'равен: ', api.balance)
		except QIWIAPIError:
			print("Ошибка 2. Невозможно осуществить поиск из-за проблем с кошельком.")

	def gethis():
		api = QApi(token=token, phone=phone)
		print("Кошелек найден!")
		file_path = 'payments.txt'
		if os.path.exists(file_path):
			os.remove(file_path)
			f = open('payments.txt', 'w')
			f.write(str(api.payments))
			f.close()
			print('Все платежи записаны в файл payments.txt')
		else:
			f = open('payments.txt', 'w')
			f.write(str(api.payments))
			f.close()
			print('Все платежи записаны в файл payments.txt')

	print('Выберите функцию: ')
	print('[1] - Баланс счета')
	print('[2] - Вывод денег')
	print('[3] - Получить историю пополнения')
	print('[4] - Выйти с программы')
	vvod = input("")

	if vvod == "1":
		info()
	elif vvod == "2":
		vanish()
	elif vvod == "3":
		gethis()
	elif vvod == '4':
		print('Ну ладно, буду ждать тебя.')
		exit(0)
	else:
		exit(0)