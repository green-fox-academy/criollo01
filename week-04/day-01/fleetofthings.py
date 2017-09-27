from fleet import Fleet
from thing import Thing

fleet = Fleet()

milk = Thing("Get milk")
remove_obstacles = Thing("Remove the obstacles")
stand_up = Thing("Stand up")
eat_lunch = Thing("Eat lunch")

stand_up.complete()
eat_lunch.complete()

fleet.add(milk)
fleet.add(remove_obstacles)
fleet.add(stand_up)
fleet.add(eat_lunch)

print(fleet)


