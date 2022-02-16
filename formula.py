import math as m


def area_of_circle():
   radius = int(input("enter the radius of the circle: "))
   area = m.pi * pow(radius, 2)
   print(f"the area of the circle wit radius {radius} is {area}")
def perimeter_of_circle():
   radius = int(input("enter the radius of the circle: "))
   perimeter = 2 * m.pi * radius
   print(f"the perimeter of the circle with radius {radius} is {perimeter}")
def area_of_triangle():
   base = int(input("enter the base of the triangle: "))
   height = int(input("enter the height of the triangle: "))
   area = 1/2 * base * height
   print(f"the area of the triangle is {area}")
def perimeter_of_triangle():
   side1 = int(input("enter the side1 of the triangle: "))
   side2 = int(input("enter the side2 of the triangle: "))
   side3 = int(input("enter the the side3 of the triangle: "))
   perimeter = side1 + side2 + side3
   print(f"the perimeter of the triangle is {perimeter}")
def length_of_hypotenuse():
   opposite = int(input("enter the oppsite side of the triangle: "))
   adjacent = int(input("enter the adjacent of the triangle: "))
   length = m.sqrt((m.pow(opposite,2) + m.pow(adjacent,2)))
   print(f"the length of the hypotenuse is {length}")
def length_of_oppsite_side_of_triangle():
   hypotenuse = int(input("enter the hypotenuse of the triangle: "))
   adjacent = int(input("enter the adjacent of the triangle: "))
   length = m.sqrt((m.pow(hypotenuse, 2) - m.pow(adjacent, 2)))
   print(f"the length of the opposite side is {length}")
def distance_of_the_point():
   print("if the plane is xy , yz, xz; just enter 0 for the point which you dont want the distance")
   x1 = int(input("enter the point x1: "))
   x2 = int(input("enter the point x2: "))
   y1 = int(input("enter the point y1: "))
   y2 = int(input("enter the point y2: "))
   z1 = int(input("enter the point z1: "))
   z2 = int(input("enter the point z2: "))
   distance = m.sqrt(m.pow(x2 - x1, 2) + m.pow(y2 - y1, 2) + m.pow(z2 - z1, 2))
   print(f"the distance of the given points is {distance}")
def solpe_of_a_line():
   x1 = int(input("enter the point x1: "))
   x2 = int(input("enter the point x2: "))
   y1 = int(input("enter the point y1: "))
   y2 = int(input("enter the point y2: "))
   slope = (y2 - y1)/(x2 - x1)
   print(f"the slope of the given points is {slope}")
def mid_point():
   print("if the plane is xy , yz, xz; just enter 0 for the point which you dont want the distance")
   x1 = int(input("enter the point x1: "))
   x2 = int(input("enter the point x2: "))
   y1 = int(input("enter the point y1: "))
   y2 = int(input("enter the point y2: "))
   z1 = int(input("enter the point z1: "))
   z2 = int(input("enter the point z2: "))
   x = (x2 + x1)/2
   y = (y1 + y2)/2
   z = (z1 + z2)/2
   print(f"the mid point of the points is ({x},{y},{z})")
def volume_of_cylinder():
   radius = int(input("enter the radius of the cylinder: "))
   height = int(input("enter the height of the cylinder: "))
   volume = m.pi * m.pow(radius, 2) * height
   print(f"the volume of the cylinder is {volume}")
def volume_of_cone():
   radius = int(input("enter the radius of the cone: "))
   height = int(input("enter the height of the cone: "))
   volume = m.pi*m.pow(radius, 2)*(height/3)
   print(f"the volume of the cone is {volume}")
def tsa_of_cube():
   side = int(input("enter the side of the cube: "))
   tsa = 6*m.pow(side,2)
   print(f"the TSA of the cube is {tsa}")
def lsa_of_cube():
   side = int(input("enter the side of the cube: "))
   lsa = 4*m.pow(side,2)
   print(f"the LSA of the cube is {lsa}")
def area_of_square():
   side = int(input("enter the side of the cube: "))
   area = m.pow(side, 2)
   print(f"the area of the square is {area}")
def area_of_rectangle():
   length = int(input("enter the length of the rectangle: "))
   breadth = int(input("enter the breadth of the rectangle"))
   area = length * breadth
   print(f"the area of the rectangle is {area}")

choice = 0
while True:
   print("1 --> for calculating the area of the circle")
   print("2 --> for calculating the perimeter of the circle")
   print("3 --> for calculating the area of the triangle")
   print("4 --> for calculating the perimeter of the triangle")
   print("5 --> for calculating the length of the hypotenuse")
   print("6 --> for calculating the length of the opposite side of the triangle")
   print("7 --> for calculating the distance of the point in a 3d plane")
   print("8 --> for calculating the slope of the point")
   print("9 --> for calculating the mid point of two given points")
   print("10 --> for calculating the volume of the cylinder")
   print("11 --> for calculating the volume of cone")
   print("12 --> for calculating the TSA of cube")
   print("13 --> for calculating the LSA of cube")
   print("14 --> for calculating the area of the square")
   print("15 --> for calculating the area of thr rectangle")
   choice = int(input("enter your option within 1 to 15: "))
   if choice == 1:
      area_of_circle()
   elif choice == 2:
      perimeter_of_circle()
   elif choice == 3:
      area_of_triangle()
   elif choice == 4:
      perimeter_of_triangle()
   elif choice == 5:
      length_of_hypotenuse()
   elif choice == 6:
      length_of_oppsite_side_of_triangle()
   elif choice == 7:
      distance_of_the_point()
   elif choice == 8:
      solpe_of_a_line()
   elif choice == 9:
      mid_point()
   elif choice == 10:
      volume_of_cylinder()
   elif choice == 11:
      volume_of_cone()
   elif choice == 12:
      tsa_of_cube()
   elif choice == 13:
      lsa_of_cube()
   elif choice == 14:
      area_of_square()
   elif choice == 5:
      area_of_rectangle()
   else:
      print("INVALID OPTION SELECTED!! :(")
      print("select option between 1 to 15")
   print("-----------------------------------------------------------------------------------------------------------------")




