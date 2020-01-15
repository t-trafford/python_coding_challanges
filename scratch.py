chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "i am checking thisee stringr for me"

check_string = check_string.lower().replace(' ',  '')
count = {}
for s in check_string:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

for key in count:
  if count[key] == 1:
    print (key, count[key])