#https://www.codewars.com/kata/58d248c7012397a81800005c

def cube_checker(volume, side):
    cuboid = False
    if volume > 0 and side > 0 and volume % side == 0:
            cuboid = True
    return cuboid
