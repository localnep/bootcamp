#my_questions.

# Select function for selection sort
def selection(sequence, start):
    min_index = start

    for i in range(start + 1, len(sequence)):
        if sequence[min_index] > sequence[i]:
            min_index = i
    return min_index


#selection = lambda sequence, start: [min_index:= i for i in range(start + 1, len(sequence)) if sequence[min_index] > sequence[i]]

########################################################################################################################
lst = [1, 5, -2, 2, -1, 7, -6, 3, 0]
temp = min(lst)
min_index = [i for i, j in enumerate(lst) if j == temp]
print("orginal list: " + str(lst))
print("the index with min value: " + str(min_index))
########################################################################################################################
def selection_sort(sequence):
    for i in range(len(sequence)):
        min_index = sequence.index(min(sequence[i:]))
        sequence[i], sequence[min_index] = sequence[min_index], sequence[i]

selection_sort(lst)
print("Sorted list is: ", lst)
########################################################################################################################

#https://stackoverflow.com/questions/10291997/how-can-i-do-assignments-in-a-list-comprehension


# selection sort algorithm
def selection_sort(sequence):
    for i in range(len(sequence) - 1):
        min_index = selection(sequence, i)
        temp = sequence[i]
        sequence[i] = sequence[min_index]
        sequence[min_index] = temp


# list to check
lst = [35, 18, 43, 66, 39, 11, 10, 117]

# calling selection_sort algorithm
selection_sort(lst)

# displaying result
print('Sorted list is: ', lst)



selection = lambda sequence, start: [i for i in range(2,5)]
selection([5,10],5)