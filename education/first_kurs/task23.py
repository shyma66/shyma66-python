def are_you_playing_banjo(name):
    # Implement me!
    if name[0].title() == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print(are_you_playing_banjo(name="Roma"))
print(are_you_playing_banjo(name="Maks"))