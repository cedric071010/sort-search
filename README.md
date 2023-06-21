# sort-search

bubble_sort

Sorting by comparing numbers next to each other and swap them if needed one by one
The largest/smallest number “float” to one side of the array like bubble
It take (n^2-3n+2)/2 steps to sort an array of n numbers resulting that step needed increases exponentially when n grows linearly (each_step = comparing 2 numbers and swap if needed)

code

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
note

Step	        arr	      i	 j    arr[j] > arr[j + 1]
1	    [5, 4, 2, 3, 1]	  0	 0	          T		
2	    [4, 5, 2, 3, 1]	  0	 1	          T		
3	    [4, 2, 5, 3, 1]	  0	 2	          T	
4	    [4, 2, 3, 5, 1]	  0	 3	          T
5   	[4, 2, 3, 1, 5]	  1	 0	          T
6	    [2, 4, 3, 1, 5]	  1	 1	          T	
7	    [2, 3, 4, 1, 5]	  1	 2	          T	
8   	[2, 3, 1, 4, 5]	  2	 0	          F	
9	    [2, 3, 1, 4, 5]	  2	 1	          T
10	  [2, 1, 3, 4, 5]	  3	 0	          T	
11	  [1, 2, 3, 4, 5]	  4	 0	          F

merge_sort

Sorting by spliting array to numbers and order them as merging them
Suitable for large datasets
Requires additional memory space for merging the subarrays
It take 2log₂(n) steps to sort an array of n numbers resulting gradually increasing at a decreasing rate as the length of the array (each_step = (a split) or (a merge))

code

def merge_sort(arr):
   if len(arr) <= 1:
       return arr

   mid = len(arr) // 2
   left_half = arr[:mid]
   right_half = arr[mid:]

   left_half = merge_sort(left_half)
   right_half = merge_sort(right_half)

   return merge(left_half, right_half)

def merge(left, right):
   merged = []
   i = j = 0

   while i < len(left) and j < len(right):
       if left[i] <= right[j]:
           merged.append(left[i])
           i += 1
       else:
           merged.append(right[j])
           j += 1

   merged.extend(left[i:])
   merged.extend(right[j:])

   return merged

note

  function	        arr			                Action
merge_sort	[5, 4, 2, 3, 1]	  Split array into [5, 4] and [2, 3, 1]
merge_sort	[5, 4]		        Recursive call to merge_sort with [5, 4]
merge_sort	[2, 3, 1]	        Recursive call to merge_sort with [2, 3, 1]
merge_sort	[5]		            Return [5]
merge_sort	[4]		            Return [4]
merge		    [5], [4]		      Merge [5] and [4] into [4, 5]
merge_sort	[2, 3, 1]	        Split array into [2] and [3, 1]
merge_sort	[2]		            Return [2]
merge_sort	[3, 1]		        Recursive call to merge_sort with [3, 1]
merge_sort	[3]		            Return [3]
merge_sort	[1]		            Return [1]
merge		    [3], [1]		      Merge [3] and [1] into [1, 3]
merge		    [2], [1, 3]	      Merge [2] and [1, 3] into [1, 2, 3]
merge		    [4, 5], [1, 2, 3]	Merge [4, 5] and [1, 2, 3] into [1, 2, 3, 4, 5]

conclusion_sort

Bubble sort is simple but efficient significantly decrease as len(array) increase where merge sort is more efficient as the len(array) increase
Merge sort requires additional memory space but Bubble sort can sort in the array
Merge sort splits and merges many numbers simultaneously, on the other hand bubble sort compare and swap the numbers one by one and go through the array len(arr) times (numbers go through -1 each time it go through)


