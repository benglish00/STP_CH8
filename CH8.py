import math
import random
import statistics
import keyword
import hello
import cubed

# use code from the module by [module name].code
print(math.pow(2,3))
print(random.randint(0,100))
nums = [10, 11, 41, 44]
print(statistics.mean(nums))
print(statistics.median(nums))
print(statistics.stdev(nums))
keyword.iskeyword("for")
keyword.iskeyword("football")
hello.print_hello()
x0 = cubed.cube(nums[0])
x1 = cubed.cube(nums[1])
x2 = cubed.cube(nums[2])

print(x0, x1, x2)