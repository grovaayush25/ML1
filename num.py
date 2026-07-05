#20 major functions of numpy

#1. len()
import numpy as np
arr = np.array([4,2,9,6,4,8])
len =0
for _ in arr:
    len = len + 1

print(len)

#2.shape()
import numpy as np
arr = np.array([(4,6,8),(3,5,7),(1,2,3)])
m  = 0
dim = []
while isinstance (arr,np.ndarray):
    for _ in arr:
        m=m+1
    dim.append(m)
    m=0
    arr=arr[0]
print("shape of array:", dim)

#3. size()
n=1
m=0
arr = np.array([(4,6,8),(3,5,7),(1,2,3)])
current = arr
while isinstance (arr,np.ndarray):
    for _ in arr:
        m=m+1
    n=n*m
    m=0
    arr = arr[0]
arr = np.array([(4,6,8),(3,5,7),(1,2,3)])
print ("size of array ",current, "is ", n
       )

#4. sum()


def my_sum(arr):
    if not isinstance (arr, np.ndarray):
       return arr
    sum = 0
    for _ in arr:
       sum = sum +my_sum(_)
    return sum

print("sum of array ",arr, "is ", my_sum(arr))

#5. max
def my_max(arr):
    if not isinstance(arr, np.ndarray):
        return arr
    max = my_max(arr)
    for _ in arr:
        if max  < my_max(_):
            max = my_max(_)
    return max

#6. min
def my_min(arr):
    if not isinstance(arr, np.ndarray):
        return arr
    min = my_min(arr)
    for _ in arr:
        if min  > my_min(_):
            min = my_min(_)
    return min

#7.mean
def my_mean (arr):
    if not isinstance (arr,np.ndarray):
        return arr
    sum = 0
    size = n #from size() function
    for _ in arr:
        sum = sum + my_sum(_)
        
    return sum / size 

#8.product
def my_product(arr):
    if not isinstance (arr,np.ndarray):
        return arr
    product =1
    for _ in arr:
        product = product * my_product(_)
    return product

#9. count_nonzero
def count_nonzero(arr):
    if not isinstance (arr,np.ndarray):
        if arr != 0:
            return 1
        else:
            return 0
    count = 0
    for _ in arr:
        count = count + count_nonzero(_)
    return count

#10. std (standard deviation)
def my_std(arr):
    if not isinstance (arr,np.ndarray):
        return arr
    mean = my_mean(arr)
    sum_sq_diff = 0
    size = n  # from size() function
    
    def flatten_and_sum_sq_diff(arr, mean):
        if not isinstance(arr, np.ndarray):
            return (arr - mean) ** 2
        total = 0
        for _ in arr:
            total = total + flatten_and_sum_sq_diff(_, mean)
        return total
    
    sum_sq_diff = flatten_and_sum_sq_diff(arr, mean)
    return (sum_sq_diff / size) ** 0.5

#11. var (variance)
def my_var(arr):
    if not isinstance (arr,np.ndarray):
        return arr
    mean = my_mean(arr)
    sum_sq_diff = 0
    size = n  # from size() function
    
    def flatten_and_sum_sq_diff(arr, mean):
        if not isinstance(arr, np.ndarray):
            return (arr - mean) ** 2
        total = 0
        for _ in arr:
            total = total + flatten_and_sum_sq_diff(_, mean)
        return total
    
    sum_sq_diff = flatten_and_sum_sq_diff(arr, mean)
    return sum_sq_diff / size

#12. argmax (index of maximum value)
def my_argmax(arr):
    if not isinstance (arr,np.ndarray):
        return 0
    max_val = my_max(arr)
    
    def find_index(arr, max_val, index=0):
        if not isinstance(arr, np.ndarray):
            if arr == max_val:
                return index
            return -1
        for i, _ in enumerate(arr):
            result = find_index(_, max_val, index)
            if result != -1:
                return result
            index = index + 1
        return -1
    
    return find_index(arr, max_val)

#13. argmin (index of minimum value)
def my_argmin(arr):
    if not isinstance (arr,np.ndarray):
        return 0
    min_val = my_min(arr)
    
    def find_index(arr, min_val, index=0):
        if not isinstance(arr, np.ndarray):
            if arr == min_val:
                return index
            return -1
        for i, _ in enumerate(arr):
            result = find_index(_, min_val, index)
            if result != -1:
                return result
            index = index + 1
        return -1
    
    return find_index(arr, min_val)

#14. sort
def my_sort(arr):
    if not isinstance (arr,np.ndarray):
        return arr
    
    def flatten_array(arr):
        if not isinstance(arr, np.ndarray):
            return [arr]
        result = []
        for _ in arr:
            result = result + flatten_array(_)
        return result
    
    flat = flatten_array(arr)
    
    # Bubble sort
    for i in range(len(flat)):
        for j in range(len(flat) - 1 - i):
            if flat[j] > flat[j + 1]:
                temp = flat[j]
                flat[j] = flat[j + 1]
                flat[j + 1] = temp
    
    return flat

#15. unique
def my_unique(arr):
    sorted_arr = my_sort(arr)
    unique_list = []
    
    for i in range(len(sorted_arr)):
        if i == 0 or sorted_arr[i] != sorted_arr[i - 1]:
            unique_list.append(sorted_arr[i])
    
    return unique_list

#16. reshape
def my_reshape(arr, new_shape):
    if not isinstance (arr,np.ndarray):
        return arr
    
    def flatten_array(arr):
        if not isinstance(arr, np.ndarray):
            return [arr]
        result = []
        for _ in arr:
            result = result + flatten_array(_)
        return result
    
    flat = flatten_array(arr)
    result_size = 1
    for dim in new_shape:
        result_size = result_size * dim
    
    if result_size != len(flat):
        return None  # Cannot reshape
    
    def build_nested(flat, shape, index):
        if len(shape) == 1:
            return flat[index[0]:index[0] + shape[0]]
        else:
            result = []
            for i in range(shape[0]):
                result.append(build_nested(flat, shape[1:], [index[0] + i * (result_size // shape[0])]))
            return result
    
    return np.array(build_nested(flat, new_shape, [0]))

#17. flatten
def my_flatten(arr):
    if not isinstance (arr,np.ndarray):
        return [arr]
    result = []
    for _ in arr:
        if isinstance(_, np.ndarray):
            result = result + my_flatten(_)
        else:
            result.append(_)
    return result

#18. concatenate
def my_concatenate(arr1, arr2):
    def flatten_array(arr):
        if not isinstance(arr, np.ndarray):
            return [arr]
        result = []
        for _ in arr:
            result = result + flatten_array(_)
        return result
    
    flat1 = flatten_array(arr1)
    flat2 = flatten_array(arr2)
    
    return np.array(flat1 + flat2)

#19. dot (matrix multiplication / dot product)
def my_dot(arr1, arr2):
    result = 0
    
    if isinstance(arr1, np.ndarray) and isinstance(arr2, np.ndarray):
        # Simple dot product for 1D arrays
        if len(arr1) == len(arr2):
            for i in range(len(arr1)):
                result = result + (arr1[i] * arr2[i])
    
    return result

#20. transpose
def my_transpose(arr):
    if not isinstance (arr,np.ndarray):
        return arr
    
    # For 2D array
    rows = len(arr)
    cols = len(arr[0]) if isinstance(arr[0], np.ndarray) or isinstance(arr[0], (list, tuple)) else 1
    
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            if isinstance(arr[i], np.ndarray):
                new_row.append(arr[i][j])
            else:
                new_row.append(arr[i])
        result.append(new_row)
    
    return np.array(result)































