import sys

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
except VAlueError:
    print("provide two integers")
    sys.exit(1)

print("inputs:")
print(f"x = {x}")
print(f"y = {y}")
print(f"(x+y)^2 = {(x+y)**2}")
