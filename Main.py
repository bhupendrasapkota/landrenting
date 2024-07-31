import Operation
import Read

def Start_point():
    mainpageloop = True
    duration_rent = 0  # Declare duration_rent outside the loop

    while mainpageloop:
        print("                                             __________________________________________ ")
        print("                                            ||                                        ||")
        print("                                            ||     WELCOME TO TechnoPropertyNepal     ||")
        print("                                            ||                                        ||")
        print("                                            ||________________________________________||")

        print("Enter 1: [For Renting The Land]")
        print("Enter 2: [For Returning The Land]")
        print("Enter 3: [For Exiting From TechnoPropertyNepal]")

        try:
            choice = int(input("Dear Customer, please pick an option from the list above: "))
            print()
            if choice == 1:
                Read.display_available_land()
                land_id = input("Enter the Kitta number of the land you want to rent: ")
                duration_rent = int(input("\nEnter duration of rent (in months): ")) # Set duration_rent here
                result = Operation.rent_land(land_id, duration_rent)
                if result:
                    print(result)
            elif choice == 2:    
                Read.display_not_available_land()
                land_id = input("Enter the kitta number of the land you want to return: ")
                duration_return = int(input("\nEnter duration of return (in months): ")) # Set duration_rent here

                # Use duration_rent from choice 1
                result = Operation.return_land(land_id, duration_rent, duration_return)
                if result:
                    print(result)
            elif choice == 3:
                mainpageloop = False
            else:
                print("Please input a valid choice from the options listed above.")
        except ValueError:
            print("Please enter a valid integer choice.")

Start_point()

