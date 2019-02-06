###Program to find the cubes of N numbers using list comprehensions.

cube = [i**3 for i in range(10)];
print(cube) #Result: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


###Program to convert temp from Fahrenheit to Celsius.

f = [0,23.4,134.233,254.54,112.1]
k = [((i + 459.67)* 5/9) for i in f]
print(k) #Result: [255.3722222222222, 268.3722222222222, 329.9461111111111, 396.78333333333336, 317.65]


###Program to prime numbers under 100.

notprime = [j for i in range(2, 8) for j in range(i*2, 100, i)]
prime = [k for k in range(2,100) if k not in notprime ]
print(prime) #Result: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

