import numpy as np

arr = [0] * 10
#arr=[1, 1, 2, 1, 3, 4, 2,1, 3, 2]

arr=[4,2,2,2,1,2,1,2,4,3,3,1,3,3,4,3,3,1,4,5,5,2,1,5,1,4,2,5,3,2,5,3,1,5,3,2,3,2,4,3,3,2,3,1,3,1,3,5,2,1,1,5,5,5,2,5,2,1,4,5,3,3,1,1,3,2,1,4,1,4,3,3,3,5,4,1,5,4,1,2,2,4,1,3,1,2,3,1,3,4,2,3,5,4,1,3,1,3,4]
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

#Values of each moment
print(f"0 Moment: {zero_moment:.2f}")
print(f"First moment: {first_moment:.2f}")
print(f"Second moment: {second_moment:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Variance (numpy): {var2:.2f}")
print(f"Third moment: {third_moment:.2f}")
print(f"Fourth moment: {fourth_moment:.2f}")