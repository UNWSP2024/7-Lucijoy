# Author: Lucia Floan
# Date: March 7, 2025
# Title: Coordinates

# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
def distance_between(coordinate1, coordinate2):
  return ((coordinate2[0] - coordinate1[0])**2 + (coordinate2[1] - coordinate1[1])**2 + (coordinate2[2] - coordinate1[2])**2)**0.5

def main():
  try:
    x1, y1, z1 = map(int, input('Enter the first coordinate (x1, y1, z1): ').split(','))
    x2, y2, z2 = map(int, input('Enter the second coordinate (x2, y2, z2): ').split(','))
    coordinate1 = (x1, y1, z1)
    coordinate2 = (x2, y2, z2)

    distance = distance_between(coordinate1, coordinate2)
    print(f'The distance between the two coordinates is: {distance:.2f} units')

  except ValueError:
    print('Invalid input, please enter the coordinates as integers separated by commas (x, y, z).')

main()
# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 
