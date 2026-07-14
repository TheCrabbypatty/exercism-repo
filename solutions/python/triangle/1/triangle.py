def triangle_inequality(sides):
    a,b,c = sides
    if a + b >= c and b + c >= a and a + c >= b and a > 0 and b>0 and c>0:
        result = True
    else:
        result = False
    return result

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
