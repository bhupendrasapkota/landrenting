def check_availability(land_id):
    available_lands = []
    with open('land_data.txt', 'r') as file:
        for line in file:
            col = line.strip().split(', ')
            if col[0] == land_id:
                print("Land ID matched:", land_id)
                if col[-1] == 'Available':
                    print("Land is available:", col)
                    available_lands.append(col)
                    return available_lands
                else:
                    return f"Land with Kitta Number {land_id} is not available"
        return f"\nPlease enter a valid Kitta Number"

def display_available_land():
    available_lands = []
    with open('land_data.txt', 'r') as file:
        for line in file:
            col = line.strip().split(',')
            if col[-1].strip() == 'Available':
                available_lands.append(col)
    if len(available_lands) > 0:
        print("Available Lands:")
        print("---------------------------------------------------------------------")
        print("| Kitta Number | City/District | Land Faced | Area of Land  | Price |")
        print("---------------------------------------------------------------------")
        for land in available_lands:
            print(f"| {land[0]:<12} | {land[1]:<13} | {land[2]:<10} | {land[3]:<13} | {land[4]:<5} |")
        print("---------------------------------------------------------------------")
    else:
        print("No available land.")

def display_not_available_land():
    not_available_lands = []
    with open('land_data.txt', 'r') as file:
        for line in file:
            col = line.strip().split(',')
            if col[-1].strip() != 'Available':
                not_available_lands.append(col)
    if len(not_available_lands) > 0:
        print("Not Available Lands:")
        print("------------------------------------------------------------------------------------")
        print("| Kitta Number | City/District | Land Faced | Area of Land | Price | Availability     |")
        print("------------------------------------------------------------------------------------")
        for land in not_available_lands:
            print(f"| {land[0]:<12} | {land[1]:<13} | {land[2]:<10} | {land[3]:<13} | {land[4]:<5} | {land[5]:<15} |")
        print("------------------------------------------------------------------------------------")
    else:
        print("No not available land.")
