def binary_search(my_list, elem):
   low = 0
   high = len(my_list) - 1
   mid = 0
   while low <= high:
      mid = (high + low) // 2
      if my_list[mid] < elem:
         low = mid + 1
      elif my_list[mid] > elem:
         high = mid - 1
      else:
         return mid
   return -1

my_list = [ 1, 9, 11, 21, 34, 54, 67, 90 ]
elem_to_search = 1
print("The list is")
print(my_list)

my_result = binary_search(my_list, elem_to_search)

if my_result != -1:
   print("Element found at index ", str(my_result))
else:
   print("Element not found!")