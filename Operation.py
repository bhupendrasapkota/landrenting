import datetime

def rent_land(land_id, duration_rent):
    while True:
        customer_firstname = input("\nEnter customer first name: ")
        customer_lastname = input("\nEnter customer last name: ")
        customer_address = input("\nEnter customer address: ")
        customer_age = input("\nEnter customer age: ")
        confirmation = input(f"\nEnter 'yes' to confirm renting land with kitta number {land_id}, or 'no' to return to choices: ")
        
        current_date_and_time = datetime.datetime.now()
        
        confirmation = confirmation.lower()
        
        if confirmation == 'yes' or confirmation == 'y':
            land_info = None
            with open('land_data.txt', 'r') as file:
                lines = file.readlines()
            with open('land_data.txt', 'w') as file:
                for line in lines:
                    land_data = line.strip().split(',')
                    if land_data[0] == land_id:
                        if land_data[-1].strip() == 'Available':
                            rent_cost = duration_rent * int(land_data[4])  # Calculate total rent cost
                            land_data[-1] = 'Rented'
                            land_info = land_data
                        else:
                            print("Land is not available for rent.")
                            return  
                    file.write(','.join(land_data) + '\n')

            if land_info is None or len(land_info) < 5:
                print("Unable to retrieve complete information about the rented land.")
                return 
            
            
            invoice_filename = f'{customer_firstname}_{customer_lastname}_invoice.txt'
            
            # Check if customer has an existing invoice file
            try:
                with open(invoice_filename, 'a') as invoice_file:
                    invoice_text = f"\n\nInvoice for renting land:\n"
                    invoice_text += f"Date and Time of Rent: {current_date_and_time}\n"
                    invoice_text += f"Kitta Number: {land_info[0]}\n"
                    invoice_text += f"Customer Name: {customer_firstname} {customer_lastname}\n"
                    invoice_text += f"Customer Address: {customer_address}\n"
                    invoice_text += f"Customer Age: {customer_age}\n"
                    invoice_text += f"City/District: {land_info[1]}\n"
                    invoice_text += f"Land Faced: {land_info[2]}\n"
                    invoice_text += f"Area of Land: {land_info[3]} anna\n"
                    invoice_text += f"Duration of Rent: {duration_rent} months\n"
                    invoice_text += f"Total Amount: {rent_cost} NPR\n"
                    invoice_file.write(invoice_text)
            except FileNotFoundError:
                with open(invoice_filename, 'w') as invoice_file:
                    invoice_text = f"Invoice for renting land:\n"
                    invoice_text += f"Date and Time of Rent: {current_date_and_time}\n"
                    invoice_text += f"Kitta Number: {land_info[0]}\n"
                    invoice_text += f"Customer Name: {customer_firstname} {customer_lastname}\n"
                    invoice_text += f"Customer Address: {customer_address}\n"
                    invoice_text += f"Customer Age: {customer_age}\n"
                    invoice_text += f"City/District: {land_info[1]}\n"
                    invoice_text += f"Land Faced: {land_info[2]}\n"
                    invoice_text += f"Area of Land: {land_info[3]} anna\n"
                    invoice_text += f"Duration of Rent: {duration_rent} months\n"
                    invoice_text += f"Total Amount: {rent_cost} NPR\n"
                    invoice_file.write(invoice_text)

            return f"\nDate {current_date_and_time}\nLand with Kitta Number {land_id}\nLocation {land_info[1]}\nDirection {land_info[2]}\nAnna {land_info[3]}\nPrice {land_info[4]}"
        elif confirmation == 'no' or confirmation == 'n':
            print("Renting process cancelled.")
            return 
        else:
            return
def return_land(land_id, duration_rent, duration_return):
    while True:
        customer_firstname = input("\nEnter customer first name: ")
        customer_lastname = input("\nEnter customer last name: ")
        customer_address = input("\nEnter customer address: ")
        customer_age = input("\nEnter customer age: ")
        confirmation = input(f"\nEnter 'yes' to confirm returning land with kitta number {land_id}, or 'no' to return to choices: ")

        current_date_and_time = datetime.datetime.now()

        confirmation = confirmation.lower()

        if confirmation == 'yes' or confirmation == 'y':
            fine = 0
            rent_cost = 0  # Initialize rent cost
            if duration_rent is not None:
                duration_difference = duration_return - duration_rent
                fine = duration_difference * 1000  # Calculate fine
            else:
                print("Land is not rented.")
                return

            with open('land_data.txt', 'r') as file:
                lines = file.readlines()

            for line in lines:
                land_data = line.strip().split(',')
                if land_data[0] == land_id and land_data[-1].strip() == 'Rented':
                    rent_cost = duration_rent * int(land_data[4])  # Calculate rent cost
                    break

            for i, line in enumerate(lines):
                land_data = line.strip().split(',')
                if land_data[0] == land_id and land_data[-1].strip() == 'Rented':
                    land_data[-1] = 'Available'
                    lines[i] = ','.join(land_data) + '\n'
                    break

            return_filename = f'{customer_firstname}_{customer_lastname}_invoice.txt'

            try:
                with open(return_filename, 'a') as return_invoice_file:
                    invoice_text = f"\n\nReturn Invoice for returning land:\n"
                    invoice_text += f"Return Date: {current_date_and_time}\n"
                    invoice_text += f"Land Kitta Number: {land_id}\n"
                    invoice_text += f"Customer Name: {customer_firstname} {customer_lastname}\n"
                    invoice_text += f"Customer Address: {customer_address}\n"
                    invoice_text += f"Customer Age: {customer_age}\n"
                    invoice_text += f"Duration of Return: {duration_return} months\n"
                    invoice_text += f"Rent Cost: {rent_cost} NPR\n"  # Include rent cost
                    invoice_text += f"Fine Applied: {fine} NPR\n"
                    return_invoice_file.write(invoice_text)
            except FileNotFoundError:
                with open(return_filename, 'w') as return_invoice_file:
                    invoice_text = f"Return Invoice for returning land:\n"
                    invoice_text += f"Return Date: {current_date_and_time}\n"
                    invoice_text += f"Land Kitta Number: {land_id}\n"
                    invoice_text += f"Customer Name: {customer_firstname} {customer_lastname}\n"
                    invoice_text += f"Customer Address: {customer_address}\n"
                    invoice_text += f"Customer Age: {customer_age}\n"
                    invoice_text += f"Duration of Return: {duration_return} months\n"
                    invoice_text += f"Rent Cost: {rent_cost} NPR\n"  # Include rent cost
                    invoice_text += f"Fine Applied: {fine} NPR\n"
                    return_invoice_file.write(invoice_text)

            return f"\nLand with Kitta Number {land_id} has been returned\nDate {current_date_and_time}\nCustomer Name: {customer_firstname} {customer_lastname}\nCustomer Address: {customer_address}\nCustomer Age: {customer_age}\nRent Cost: {rent_cost} NPR\nFine Applied: {fine} NPR"
        elif confirmation == 'no' or confirmation == 'n':
            print("Returning process cancelled.")
            return
        else:
            return

