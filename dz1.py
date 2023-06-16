def is_palindrom(string):
    return string[::-1] == string

print(is_palindrom('123'))
print(is_palindrom('12321'))
print(is_palindrom('abba'))
print(is_palindrom('abBA'))