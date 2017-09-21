

def LayCarpet(mySize, myCoordinate):
   if mySize > 1:
      8_points = setCoordinates(min, max, middle, myCoordinate)
      for coordinate in 8_points:
          LayCarpet(mySize / 2, coordinate)
      drawBox(mySize, myCoordinate)