def string_match(a, b):
  count1 = 0
  n = max(len(a),len(b))
  for i in range(n-1):
       if i+1 <= len(a) and i+1 <= len(b):
           if a[i:(i+2)] == b[i:(i+2)]: 
              count1 = count1 + 1
  return(count1)

