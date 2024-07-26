import math

def area_of_circle(radius):
    return math.pi * (radius ** 2)

def area_of_triangle(base, height):
    return 0.5 * base * height

def main():
    radius = float(input("Enter the radius of the circle: "))
    circle_area = area_of_circle(radius)
    print(f"The area of the circle with radius {radius} is: {circle_area:.2f}")
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    triangle_area = area_of_triangle(base, height)
    print(f"The area of the triangle with base {base} and height {height} is: {triangle_area:.2f}")
if __name__ == "__main__":
    main()
