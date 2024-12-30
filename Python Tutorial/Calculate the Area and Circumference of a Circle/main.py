from math import pi, pow


def main():
    radius = int(input("Enter circle raduis: "))
    circumference = 2 * pi * radius
    area = pi * pow(radius, 2)

    return circumference, area


circumference, area = main()
print(f'Circle circumference= {circumference} and area = {area}')