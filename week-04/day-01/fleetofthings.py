from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

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


