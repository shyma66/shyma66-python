import json

# Read data from cars.json
with open('cars.json', 'r') as file:
    cars_data = json.load(file)

# Read data from cars2.json
with open('cars2.json', 'r') as file:
    car2_data = json.load(file)

# Combine data from both files
combined_data = cars_data + [car2_data]

# Sort the combined data based on max_speed
sorted_data = sorted(combined_data, key=lambda x: x['max_speed'])

# Write the sorted data to result.json
with open('result.json', 'w') as result_file:
    json.dump(sorted_data, result_file, indent=2)



# Sort the combined data by max_speed
# sorted_data = sorted(combined_data, key=lambda x: x['max_speed'])
#
# # Write the sorted data to result.json
# with open('result.json', 'w') as file:
#     json.dump(sorted_data, file)