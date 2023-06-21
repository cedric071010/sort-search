# sort-search

bubble_sort

Sorting by comparing numbers next to each other and swap them if needed one by one
The largest/smallest number “float” to one side of the array like bubble
It take (n^2-3n+2)/2 steps to sort an array of n numbers resulting that step needed increases exponentially when n grows linearly (each_step = comparing 2 numbers and swap if needed)

merge_sort

Sorting by spliting array to numbers and order them as merging them
Suitable for large datasets
Requires additional memory space for merging the subarrays
It take 2log₂(n) steps to sort an array of n numbers resulting gradually increasing at a decreasing rate as the length of the array (each_step = (a split) or (a merge))

conclusion_sort

Bubble sort is simple but efficient significantly decrease as len(array) increase where merge sort is more efficient as the len(array) increase
Merge sort requires additional memory space but Bubble sort can sort in the array
Merge sort splits and merges many numbers simultaneously, on the other hand bubble sort compare and swap the numbers one by one and go through the array len(arr) times (numbers go through -1 each time it go through)


