# numbers = [0, 4, 3, 2, 3]                   #numbers = [0, 4, 3, 2, 3]
# doubled_numbers = [n * 2 for n in numbers] # doubled_numbers = []
#                                              # for n in numbers:
# print(doubled_numbers)                      #doubled_numbers.append(n * 2)

# vec1 = ["maks", "sad", 2]
# vec2 = [20, 2, "2"]
# dot_mul = [u*v for u, v in zip(vec1, vec2)]
# print(dot_mul)
vec1 = ["maks", "sad", 2]
vec2 = [20, 2, "2"]
keys = "121"
values ="2121"
dot_mul =   [{key: value} for (key, value) in zip(keys, values)]
print(dot_mul)
#
# vec1 = [3, 10, 2]
# vec2 = [-20, 5, 1]
# dot_mul = [u*v for u, v in zip(vec1, vec2)]
# dot_prod = sum(dot_mul)
# print(dot_prod)
#
# power = [i*i for i in range(10)]
# print(power)
#
#
# readings = [-1.2, 0.5, 12, 1.8, -9.0, 5.3]
# good_readings = [r for r in readings if r > 0]
# print(good_readings)
