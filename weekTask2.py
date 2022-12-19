user_input = []
for i in range(5):
  user_input.append(int(input("s1: ")))

power_list = []
for num in user_input:
  power_list.append(num*num)

print("s2:", power_list)