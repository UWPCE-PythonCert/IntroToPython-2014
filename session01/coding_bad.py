# warmup exercises 1

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  return False


def diff21(n):
  if n > 21:
    return 2 * abs(n - 21)
  else:
    return abs(n - 21)


def parrot_trouble(talking, hour):
  if 7 <= hour <= 20:
    return False
  elif talking:
    return True
  return False


  def makes10(a, b):
      if a == 10 or b == 10 or a + b == 10:
        return True
      return False


def near_hundred(n):
  if abs(n - 100) <= 10 or abs(n - 200) <= 10:
    return True
  return False

  def pos_neg(a, b, negative):
  a_neg = (a < 0)
  b_neg = (b < 0)
  if negative and (a_neg and b_neg):
    return True
  elif negative:
    return False
  elif (a_neg and not b_neg) or (not a_neg and b_neg):
    return True
  else:
    return False

def not_string(str):
  if str[:3] == "not":
    return str
  else:
    return "not " + str

def missing_char(str, n):
  return str[0:n] + str[n + 1:]


def front_back(str):
  if len(str) > 1:
    return str[-1] + str[1:len(str) - 1] + str[0]
  else:
    return str

def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or (not a_smile and not b_smile):
    return True
  else:
    return False

def sum_double(a, b):
  if a == b:
    return 4 * a
  else:
    return a + b

def front3(str):
  if len(str) < 3:
    return str * 3
  else:
    return str[:3] * 3

# warmup exercises 2

def string_times(str, n):
  return str * n


def front_times(str, n):
  if len(str) < 3:
    return str * n
  else:
    return str[:3] * n


def string_bits(str):
  return str[::2]


def string_splosion(str):
  final_str = ""
  for x in range(1, len(str) + 1):
    final_str += str[:x]
  return final_str

 def last2(str):
  substr = str[-2:]
  substr_count = 0
  for x in range(len(str) - 2):
    if str[x: x + 2] == substr:
      substr_count += 1
  return substr_count

def array_count9(nums):
  return nums.count(9)


def array_front9(nums):
  if len(nums) < 4:
    return 9 in nums
  else:
    return 9 in nums[:4]

def array123(nums):
  if len(nums) <= 3:
    if nums == [1, 2, 3]:
      return True
    else:
      return False
  for x in range(len(nums) - 2):
    if nums[x:x + 3] == [1, 2, 3]:
      return True
  else:
    return False

def string_match(a, b):
  match_count = 0
  for x in range(len(a) - 1):
    substr = a[x:x + 2]
    if b[x:x + 2] == substr:
      match_count += 1
  return match_count
