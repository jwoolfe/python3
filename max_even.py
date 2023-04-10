def highest_even(li):
    for i in li:
        if i % 2 != 0:  # If no remainder. Aka, is divisible by 2.
            li.remove(i)
    return max(li)

print(highest_even([10,2,3,4,8,11]))
