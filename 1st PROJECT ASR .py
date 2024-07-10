  #============================AUTOMATIC SPEECH RECOGNITION=========================#

import speech_recognition as sr



operators = {
    "+": "plus",
    "-": "minus",
    "*": "multiply",
    "/": "divided by",
    "**":"power",
    "**(1/2)":"root",
    "(":"open",
    ")":"close"
}

import sympy as sp


def calculate_expression(expression_str):
  """
  This function takes a mathematical expression string and evaluates it using sympy.
  It also handles user input with english operator names.

  Args:
      expression_str: The string containing the mathematical expression.

  Returns:
      The result of evaluating the expression.

  Raises:
      SyntaxError: If the expression string has a syntax error.
  """
  try:
    # Replace english operators with their symbolic counterparts
    for op, english_name in operators.items():
      expression_str = expression_str.replace(english_name, op)
    expression_str = expression_str.replace("x", "*")
    
    print("your expression",expression_str)
    # Parse the expression using sympy
    expr = sp.sympify(expression_str)
    # Evaluate the parsed expression
    result = expr.evalf()
    return result
  except (SyntaxError, ValueError) as e:
    raise SyntaxError(f"Invalid expression: {expression_str}. Error: {e}") from e


def main():
  """
  This function takes user input for the expression and prints the result.
  """


  r = sr.Recognizer()
  with sr.Microphone()  as source:

    print("speak action :\n 1. \"convert to text\" \n 2. \"calculate\" \n ")

    audio = r.listen(source)
    text = r.recognize_google(audio)
    action = '{}'.format(text)
    if(action == "convert text"): 
      print("speak anything :")
      try:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("you said : {}".format(text))
      except:
        print("sorry can not recognize you")

    elif(action == "calculate"):
      print("speak you expression clearly : \n if want square root speak \"square root\" after no. :")
      
      try:
        audio = r.listen(source)
        text = r.recognize_google(audio)        
        expression_str = '{}'.format(text)
        print(expression_str)
        result = calculate_expression(expression_str)
        print(f"The result of '{expression_str}' is: {result}")
      except:
        print("sorry can not recognize you")
  


if __name__ == "__main__":
  main()







