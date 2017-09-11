# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000

length = 20
width = 10
height = 15

surface_area = 2 * (length * width + width * height + length * height)
volume = length * width * height

print "Surface Area:", surface_area
print "Volume:", volume