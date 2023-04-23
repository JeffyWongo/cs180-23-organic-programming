import json

# Load the JSON data from file
with open('cars.json', 'r') as file:
    cars_data = json.load(file)

# Initialize the search filters
filters = {}

# Create a function to search the data by a specific key and value
def search_data(key, value):
    found_cars = []
    for car in cars_data:
        if car[key] == value:
            found_cars.append(car)
    return found_cars

# Display the menu and get user input
while True:
    print("Please select a search criteria:")
    print("1. Car Name")
    print("2. Car Model")
    print("3. Car Year")
    print("4. Car Cost Range")
    print("5. Filter")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))

    # Update the search filters based on the user's choice
    if choice == 1:
        name = input("Enter the car name: ")
        filters['name'] = name
    elif choice == 2:
        model = input("Enter the car model: ")
        filters['model'] = model
    elif choice == 3:
        year = input("Enter the car year: ")
        filters['year'] = year
    elif choice == 4:
        min_cost = int(input("Enter the minimum car cost: "))
        max_cost = int(input("Enter the maximum car cost: "))
        filters['min_cost'] = min_cost
        filters['max_cost'] = max_cost
    elif choice == 5:
        found_cars = cars_data
        for key, value in filters.items():
            if key == 'name':
                found_cars = search_data('name', value)
            elif key == 'model':
                found_cars = search_data('model', value)
            elif key == 'year':
                found_cars = search_data('year', value)
            elif key == 'min_cost' and 'max_cost' in filters:
                found_cars = []
                for car in cars_data:
                    if filters['min_cost'] <= car['cost'] <= filters['max_cost']:
                        found_cars.append(car)
            elif key == 'min_cost':
                found_cars = [car for car in found_cars if car['cost'] >= value]
            elif key == 'max_cost':
                found_cars = [car for car in found_cars if car['cost'] <= value]

        # Display the results
        if len(found_cars) == 0:
            print("No cars found.")
        else:
            print(f"Found {len(found_cars)} cars:")
            for car in found_cars:
                print(f"Name: {car['name']}, Model: {car['model']}, Year: {car['year']}, Cost: {car['cost']}")

    elif choice == 6:
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
        continue