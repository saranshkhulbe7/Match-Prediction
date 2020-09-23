#implementation of KNN
import math
from operator import itemgetter

def encoder(lst):
  data = []
  for string in lst:
    if string == 'Overcast' or string == 'Cool':
      data.append(0)
    elif string == 'Rainy' or string == 'Hot':
      data.append(1)
    elif string == 'Sunny' or string == 'Mild':
      data.append(2)
    else:
      data.append(string)
  return data

def distance(x1,x2,y1,y2):
  dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  return dist

def predictor(encoded_dataset,training_data_example_encoded,k):
  result_table = []
  for lst in encoded_dataset:
    result = []
    result.append(distance(training_data_example_encoded[0],lst[0],training_data_example_encoded[1],lst[1]))
    result.append(lst[2])
    result_table.append(result)
  print('result_table = ',result_table)
  sorted_result_table = sorted(result_table, key = itemgetter(0))
  print('sorted_result_table = ',sorted_result_table)
  sorted_result_table = sorted_result_table[:k]
  count_of_YesNo = {}
  for lst in sorted_result_table:
    if lst[1] in count_of_YesNo:
      count_of_YesNo[lst[1]] = count_of_YesNo[lst[1]] + 1
    else:
      count_of_YesNo[lst[1]] = 1
  print("YesNo_Count",count_of_YesNo,"as k =",k)
  if count_of_YesNo['Yes'] > count_of_YesNo['No']:
    answer = 'Yes'
  else:
    answer = 'No'
  return answer

weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
k = 5
dataset = [
 ['Sunny','Hot','No'],
 ['Sunny','Hot','No'],
 ['Overcast','Hot','Yes'],
 ['Rainy','Mild','Yes'],
 ['Rainy','Cool','Yes'],
 ['Rainy','Cool','No'],
 ['Overcast','Cool','Yes'],
 ['Sunny','Mild','No'],
 ['Sunny','Cool','Yes'],
 ['Rainy','Mild','Yes'],
 ['Sunny','Mild','Yes'],
 ['Overcast','Mild','Yes'],
 ['Overcast','Hot','Yes'],
 ['Rainy','Mild','No']
]

training_data_example = ["Sunny","Cool"]
training_data_example_encoded = encoder(training_data_example)
encoded_dataset = []

for lst in dataset:
  encoded_dataset.append(encoder(lst))

pridiction = predictor(encoded_dataset,training_data_example_encoded,k)
print("Pridiction is",pridiction)


