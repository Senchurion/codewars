#https://www.codewars.com/kata/54edbc7200b811e956000556

def count_sheeps(sheep):
    a = 0
    for i in sheep:
       if i:
        a += 1
    return a
