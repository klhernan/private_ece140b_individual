import numpy as np


def question1():
    array1 = np.array([0, 10, 4, 12])
    result = array1 - 20 
    print('Result: ', result)
    print('Shape of array1: ', array1.shape)

    return array1, result



def question2():

    array2 = np.array([0, 10, 4, 12], [1, 20, 3, 41])
    array2_new = array2.reshape(4,2)[1:-1,:]

    print('array2: ', array2)
    print('array2 shape: ', array2.shape)
    print('\narray2_new: ', array2_new)
    print('array2_new shape: ', array2_new.shape)

    print("The methods I used was simply to reshape the array to to be size 4x2 (4 rows, 2 columns) and then only grab the second and third row which would correspond to the values we want.")

    return array2, array2_new


def question3():

    array1, _ = question1()

    # Concatenate array1 with itself along the same row
    hstack_out = np.hstack((array1,array1))

    # Concatenate new hstack with itself along the columns 4 times
    array3 = np.vstack((hstack_out,hstack_out,hstack_out,hstack_out))

    print('array3: \n', array3)

    return array3



def question4():

    array4a = np.arange(-3, 16, 6)
    array4b = np.arange(-7, -20, -2)

    print('array4a: ', array4a)
    print('array4b: ', array4b)

    return array4a, array4b



def question5():

    array5 = np.linspace(0, 100, 49)

    print('array5: ', array5)
    print('\narray5 steps: ', array5.shape)

    print('Linspace gives n number of values in an array equal to the steps specified, with boundaries including the specified values given in the first two arguments for max and min values. Meanwhile, arange returns the number of steps wanted from the specified min boundarie up to but not including the specified max value. ')
    print('\nWhen we need a very precise distribution between the min and max(inclusive) is when I wouls use linespace over arange')

    return array5


def question6():

    array6 = np.zeros((3,4))

    array6[0]= [12, 3, 1, 2]
    array6[:, 1] = [3, 0, 2]
    array6[2, :2] = [4, 2]
    array6[2, 2:] = [3, 1] 
    array6[:, 2] = [1, 1, 3]
    array6[1, 3] = 2

    print('array6[0]: ', array6[0])          # [12 3 1 2]
    print('array6[1, 0]: ', array6[1, 0])    # 0
    print('array6[:, 1]: ', array6[:, 1])    # [3 0 2]
    print('array6[2, :2]: ', array6[2, :2])  # [4 2]
    print('array6[2, 2:]: ', array6[2, 2:])  # [3 1] 
    print('array6[:, 2]: ', array6[:, 2])    # [1 1 3]
    print('array6[1, 3]: ', array6[1, 3])    # 2

    return array6