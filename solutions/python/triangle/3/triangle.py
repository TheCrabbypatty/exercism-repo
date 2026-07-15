def triangle_inequality(sides):
    side1,side2,side3 = sides
    return side1 + side2 >= side3 and side2 + side3 >= side1 and side1 + side3 >= side2 and 0 not in [side1, side2, side3]

def equilateral(sides):
    side1, side2, side3 = sides
    if side1 == side2 and side2 == side3:
        result = True
    else:
        result = False
    return result and triangle_inequality(sides)
    


def isosceles(sides):
    return not scalene(sides) and triangle_inequality(sides)


def scalene(sides):
    side1, side2, side3 = sides
    if side1 != side2 and side2 != side3 and side1 != side3:
        result = True
    else:
        result = False
    return result and triangle_inequality(sides)
