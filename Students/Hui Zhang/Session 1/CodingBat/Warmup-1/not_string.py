def not_string(str):
  if str.find("not") == 0:
      return str
  else:
      return "not" + " " + str
