def isPalindrome(x: int) -> bool:
    i, j = 0, len(str(x)) - 1

    string_x = str(x)
    while i != j and (i - j) != 1:
        print(f"i: {i}, j: {j}")
        if string_x[i] != string_x[j]:
            return 'false'
        i += 1
        j -= 1
    print(f"i: {i}, j: {j}")
    return 'true'

v = isPalindrome(x=-121)
print(v)
