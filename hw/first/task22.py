def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Happy Coding! ;)

    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False

print(zero_fuel(distance_to_pump=64,mpg=65,fuel_left=1))