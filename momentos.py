import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew

arr = [0] * 10
#arr=[1, 1, 2, 1, 3, 4, 2,1, 3, 2]

arr=[11, 8, 2, 3, 1, 4, 5, 3, 4, 6, 2, 3, 4, 4, 5, 7, 9, 3, 3, 1, 4, 7, 2, 3, 2, 2, 1, 5, 5, 7, 8, 9, 10, 4, 3, 2, 6, 9, 11, 3, 3, 4, 12, 5, 6, 8, 30, 6, 10, 13]
n = len(arr)

#User input n
#n = int(input("Enter the number of elements in the array: "))

#User input arr
#for i in range(n):
    #arr[i] = int(input(f"Enter element {i+1}: "))

#Determine the probability of each element
probabilities = [0] * n
for i in range(n):
    probabilities[i] = arr[i] / sum(arr)
unique_elements = set(arr)
print("List of unique elements and their probabilities:")
for element in unique_elements:
    count = arr.count(element)
    probability = count / n
    print(f"Element {element}: Probability {probability:.2f}")

#Moment zero 
zero_moment = sum(probabilities)

#Determine first moment 
first_moment = sum(arr) / n
#Determine second moment
second_moment = 0
for i in range(n):
    second_moment += (arr[i]**2) # lo adecuado seria la suma de todas las probabilidades por el elemeto^2
second_moment /= n

#Variance
variance = second_moment-(first_moment ** 2)
var2 = np.var(arr)

#Determine third moment
third_moment = 0
for i in range(n):
    third_moment += arr[i] **3
third_moment /= n

#Determine fourth moment
fourth_moment = 0
for i in range(n):
    fourth_moment += arr[i]**4
fourth_moment /= n
kurtos = kurtosis(arr)
kur = fourth_moment/((variance**0.5)**4)

asymetry = skew(arr)

#Values of each moment
print(f"0 Moment: {zero_moment:.2f}")
print(f"First moment: {first_moment:.2f}")
print(f"Second moment: {second_moment:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Variance (numpy): {var2:.2f}")
print(f"Kurtosis: {kurtos:.2f}")
print(f"Kurtosis (manual): {kur:.2f}")
print(f"Asymmetry: {asymetry:.2f}")
print(f"Third moment: {third_moment:.2f}")
print(f"Fourth moment: {fourth_moment:.2f}")