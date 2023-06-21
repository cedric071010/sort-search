# sort-search
google slide - https://docs.google.com/presentation/d/1_jM_78Ax_c2mM-_Yo90Hxjd8nSpwgGDRaqjESs4YUu8/edit#slide=id.g22aa0feea53_0_85


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


linear_search

Search one by one from start to end

Can search unsorted array

Search space is reduced by 1 each step

Maximum n steps, average n/2 steps and minimum 0 step needed to search an n element array (linear graph)


binary_search

Search by repeating (halfing the array, ignore the unwanted half)

Can only search sorted array

Search space is reduced by ½ of the array each step

Maximum log₂(n) steps, average log₂(n+1)-1 steps and minimum 0 step needed to search an n element array


conclusion_search

Linear search is better for small collection of unsorted array where binary search is better for large array and can only search sorted array

Linear search go through every element in the array and compare it with the target number, but binary search ignore most of the element in the array to increase the efficiency by (1/2)^k * 100 %


conclusion

The relatively better way to search a relatively small unsorted array is search with linear search, binary search is faster than linear search but it take a relatively long time to sort and then search

When len(array) (= n) get large to a point where 2(2log₂(n) + log₂(n+1)-1) < n, there’s so much element in the array that it is more efficient to merge sort and binary search the element
