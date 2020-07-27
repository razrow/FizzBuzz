def fizzbuzz(n):
  for nums in range (1, n+1):
    if(nums%3==0 and nums%5==0):
      print("fizzbuzz")
    if(nums%3==0 and nums%5!=0):
      print("fizz")
    if(nums%3!=0 and nums%5==0):
      print("buzz")
    if(nums%3!=0 and nums%5!=0):
      print(str(nums))
# Please do not modify the code below this line.
# When you run your code, you will need to enter 
# an input in the terminal below, where the prompt appears

test_case = int(input("Please enter an input number:"))
fizzbuzz(test_case)