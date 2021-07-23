def arithmetic_arranger(problems, solve=False):
  firstOp = []
  operators = []
  secondOp = []

  if len(problems)>5:
    return 'Error: Too many problems.'
  
  for problem in problems:
    splitOp = problem.split(' ')
    firstOp.append(splitOp[0])
    operators.append(splitOp[1])
    secondOp.append(splitOp[2])
  
  for op in operators:
    if op != '+' and op != '-':
      return "Error: Operator must be '+' or '-'."
  
  for number in firstOp:
    if not number.isdecimal():
      return 'Error: Numbers must only contain digits.'
  
  for number in secondOp:
    if not number.isdecimal():
      return 'Error: Numbers must only contain digits.'

  for number in firstOp:
    if len(number) > 4:
      return 'Error: Numbers cannot be more than four digits.'

  for number in secondOp:
    if len(number) > 4:
      return 'Error: Numbers cannot be more than four digits.'

  first = []
  second = []
  third = []
  fourth = []

  for i in range(len(firstOp)):
    if len(firstOp[i]) > len(secondOp[i]):
      first.append(" "*2 + firstOp[i])
    else:
      first.append(" "*(len(secondOp[i]) - len(firstOp[i]) + 2) + firstOp[i])

  for i in range(len(secondOp)):
    if len(secondOp[i]) > len(firstOp[i]):
      second.append(operators[i] + " " + secondOp[i])
    else:
      second.append(operators[i] + " "*(len(firstOp[i]) - len(secondOp[i]) + 1) + secondOp[i])

  for i in range(len(firstOp)):
    third.append('-'*(max(len(firstOp[i]), len(secondOp[i]))+2))
  
  if solve:
    for i in range(len(firstOp)):
      if operators[i] == "+":
          ans = str(int(firstOp[i]) + int(secondOp[i]))
      else:
          ans = str(int(firstOp[i]) - int(secondOp[i]))
      
      if len(ans) > max(len(firstOp[i]), len(secondOp[i])):
        fourth.append(" " + ans)
      else:
        fourth.append(" "*(max(len(firstOp[i]), len(secondOp[i])) - len(ans) + 2) + ans)
    
    arranged_problems = '    '.join(first)+'\n' + '    '.join(second) + '\n' + '    '.join(third) + '\n' + '    '.join(fourth)
  else:
    arranged_problems = '    '.join(first)+'\n' + '    '.join(second) + '\n' + '    '.join(third)
  
  return arranged_problems
