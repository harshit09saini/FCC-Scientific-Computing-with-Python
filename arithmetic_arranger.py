def calculate(num1: str,num2: str, operator: str) -> str:
  num1, num2 = int(num1), int(num2)
  if operator == '+':
    res = num1 + num2
  else: 
    res = num1 - num2
    
  return str(res)  
  
def arithmetic_arranger(problems, solve=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  
  sum_arr = []
  line_num1, line_num2, line_dash, line_res = "", "", "", ""
  first_sum = True

  for problem in problems:
    numbers = problem.split(' ')
    num1, operator, num2 = numbers[0], numbers[1], numbers[2]
    space_between = " "*4

    # print(f"num1: {num1}\tnum2: {num2}\n")
    # print(num1, num2) # Numbers are given as strings 
    # Find length
    num1_length = len(num1)
    num2_length = len(num2)

    # Error Checking for all digits
    if num1.isdigit() is False or num2.isdigit() is False:
      return "Error: Numbers must only contain digits."

  
    # Error Checking for Number of Digits. Should not be more than 4 for each
    if num1_length > 4 or num2_length > 4: 
      return "Error: Numbers cannot be more than four digits."
    if operator != '+' and operator != '-':
      return "Error: Operator must be '+' or '-'."
    
    # Add Proper Spacing
    # find the bigger
    maxx = max(num1_length, num2_length)
    dash_str = ""
    
    for i in range(0, maxx+2):
      dash_str += "-"
    

    if first_sum:
      line_num1 += num1.rjust(maxx+2) 
      line_num2 += operator + "" + num2.rjust(maxx+1)
      line_dash += dash_str

      if solve: 
        res = calculate(num1, num2, operator)
        line_res +=  res.rjust(maxx+2)
      first_sum = False
    else: 
      line_num1 += num1.rjust(maxx+6) 
      line_num2 += operator.rjust(5) + "" + num2.rjust(maxx+1)
      line_dash += space_between + "-" * (maxx+2)
      if solve: 
        res = calculate(num1, num2, operator)
        line_res += space_between + res.rjust(maxx+2)
        

    if solve: 
      sumstr = f"{line_num1}\n{line_num2}\n{line_dash}\n{line_res}"
    else: 
      sumstr = f"{line_num1}\n{line_num2}\n{line_dash}"

  return sumstr
