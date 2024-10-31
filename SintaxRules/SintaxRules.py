class SintaxRules:
  def __init__(self):
    pass

  @staticmethod
  def parenthesis(message: str) -> bool:

    assert isinstance(message, str), "message must be a string."
    opened_parenthesis_counter: int = 0
    
    for index in range(len(message)):

      not_read = [r"\(", r"\)"]

      if 0 < index <= len(message):
        if message[index - 1:index + 1] in not_read:
          continue
      
      if message[index:index + 1] == "(":
        opened_parenthesis_counter += 1
        continue

      if message[index:index + 1] == ')':
        if opened_parenthesis_counter > 0:
          opened_parenthesis_counter -= 1
          continue
        return False

    return opened_parenthesis_counter == 0


if __name__=="__main__":
  print(SintaxRules.parenthesis("()"))
  print(SintaxRules.parenthesis("("))
  print(SintaxRules.parenthesis(")"))
  print(SintaxRules.parenthesis(")("))
  print(SintaxRules.parenthesis(r"\("))
  print(SintaxRules.parenthesis("())"))
  print(SintaxRules.parenthesis("((()))"))
  print(SintaxRules.parenthesis("((()()()))"))