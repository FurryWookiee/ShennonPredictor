import random
#Подготовка данных
History = {}
for a1 in range(2):
	for b1 in range(2):
		for a2 in range(2):
			for b2 in range(2):
				for a3 in range(2):
					Ind = str(a1)+str(b1)+str(a2)+str(b2)+str(a3)
					History[Ind] = 0
print("Введите 3 числа (0 или 1), каждое с новой строки");
Flag = True
k = 0
a1 = random.randint(0,1)
a2 = random.randint(0,1)
b1 = random.randint(0,1)
b2 = random.randint(0,1)
#First 3 moves
for i in range(3):
	a3 = int(input(""))
	b2 = random.randint(0,1)
	Ind = str(a1)+str(b1)+str(a2)+str(b2)+str(a3)
	History[Ind] += 1
	a1 = a2
	a2 = a3
	b1 = b2
Wins = 0
add = 1
Predict = random.randint(0,1)
print("Начнём игру!")
#Predictor mode on
while Flag:
	#Сдвиг предыдущих ходов
	a1 = a2
	a2 = a3
	b1 = b2
	b2 = Predict
	k += 1
	add *= 1.1
	Ind = str(a1)+str(b1)+str(a2)+str(b2)
	#Смотрим, есть ли существенное преимущество нуля или единицы
	d = (History[Ind+'0'] - History[Ind+'1'])/k
	if d<0:
		d *= -1;
	#Принятие решения
	if d < 0.05:
		Predict = random.randint(0,1)
		print("*", end='')
	elif History[Ind+'0'] > History[Ind+'1']:
		Predict = 0
	else:
		Predict = 1
	print("\tПопытка №"+str(k)+"\tУгадано: "+str(Wins)+" раз, точность "+ str((100*Wins/k))+"%", end='')
	input()		
	print("Думаю, это число: "+str(Predict))
	print("Введите ваше число:",end = ' ')
	a3 = int(input())
	if a3<0: 
		Flag = False
	else:
		if a3==Predict:
			Wins += 1
		History[Ind + str(a3)] += 1
print("*****\nИтог игры\n*****\nУгадано: "+str(Wins)+" раз, точность "+ str((100*Wins/k))+"%")		
if Wins/k>0.7:
	print ("Кажется, железка победила.")
	