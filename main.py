import csv

osnova = []
lev1 = []
lev2 = []
lev3 = []
prav = []

qnum = 1

score = []

with open('acc.csv', newline="") as pythontext:
  reader = csv.reader(pythontext, delimiter = ';')
  for row in reader:
    osnova.append(row[0])
    lev1.append(row[1])
    lev2.append(row[2])
    lev3.append(row[3])
    prav.append(row[4])

while qnum < len(osnova):
  print(osnova[qnum])
  print(lev1[qnum])
  print(lev2[qnum])
  print(lev3[qnum])
  option = input('Выберите варивнт ответа: ')

  if option == 'a':
    if lev1[qnum] == prav[qnum]:
      print('Правельно')
      score.append(5)
    else:
      print('Не правельно')
  
  if option == 'b':
    if lev2[qnum] == prav[qnum]:
      print('Правельно')
      score.append(5)
    else:
      print('Не правельно')
  
  if option == 'c':
    if lev3[qnum] == prav[qnum]:
      print('Правельно')
      score.append(5)
    else:
      print('Не правельно') 

  qnum += 1

totalscore = sum(score)
print('Вы набрали ' + str(totalscome) + "баллов")

if totalscore == 100:
  print('Ваша оценка "A"')