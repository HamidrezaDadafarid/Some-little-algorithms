def test_binary_search():
   # Test with an empty list
   assert binary_search([], 5, 0, 0) == False

   # Test with a list of one element
   assert binary_search([3], 3, 0, 0) == True
   assert binary_search([3], 5, 0, 0) == False

   # Test with a list of multiple elements
   assert binary_search([1, 2, 3, 4, 5], 3, 0, 4) == True
   assert binary_search([1, 2, 3, 4, 5], 6, 0, 4) == False

   # Test with a list of multiple elements that includes the target
   assert binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23, 0, 9) == True

   # Test with a list of multiple elements that does not include the target
   assert binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 100, 0, 9) == False