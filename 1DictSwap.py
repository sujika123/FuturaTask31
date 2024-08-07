# 1.Given a dictionary d = {'a': 1, 'b': 2, 'c': 3}, write a function that swaps the keys and values.
# The output should be {'1': 'a', '2': 'b', '3': 'c'}.

dict = {'a': 1, 'b': 2, 'c': 3}
print(dict)

dict = {value:key for key, value in dict.items()}
print(dict)