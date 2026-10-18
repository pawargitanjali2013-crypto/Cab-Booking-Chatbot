import random

# Cab rates per kilometre
cab_rates = {
    1: ("Auto", 12),
    2: ("Sedan", 18),
    3: ("SUV", 25)
}

# Predefined routes: source, destination, distance in kilometres
routes = {
    1: ("Pune Station", "Shivajinagar", 5),
    2: ("Swargate", "Kothrud", 8),
    3: ("Hinjawadi", "Wakad", 10)
}


while True:
    print("\n===== CAB BOOKING CHATBOT =====")
    print("1. Book Ride")
    print("2. Exit")

    try:
        main_choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter 1 or 2.")
        continue

    if main_choice == 1:
        # Choose cab type
        while True:
            print("\nChoose Cab Type:")
            print("1. Auto - ₹12/km")
            print("2. Sedan - ₹18/km")
            print("3. SUV - ₹25/km")

            try:
                cab_choice = int(input("Enter cab type (1-3): "))
            except ValueError:
                print("Invalid choice! Please enter 1, 2, or 3.")
                continue

            if cab_choice in cab_rates:
                cab_type, rate = cab_rates[cab_choice]
                break

            print("Invalid cab choice! Please select 1, 2, or 3.")

        # Choose predefined route
        while True:
            print("\nChoose Route:")
            print("1. Pune Station to Shivajinagar - 5 km")
            print("2. Swargate to Kothrud - 8 km")
            print("3. Hinjawadi to Wakad - 10 km")

            try:
                route_choice = int(input("Enter route number (1-3): "))
            except ValueError:
                print("Invalid route! Please enter 1, 2, or 3.")
                continue

            if route_choice in routes:
                source, destination, distance = routes[route_choice]
                break

            print("Invalid route choice! Please select 1, 2, or 3.")

        # Calculate and display fare
        fare = rate * distance

        print("\n===== RIDE DETAILS =====")
        print("Cab Type:", cab_type)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: ₹" + str(rate) + "/km")
        print("Total Fare: ₹" + str(fare))

        # Confirm or cancel before sharing OTP
        while True:
            print("\n1. Confirm & Share OTP")
            print("2. Cancel Ride")

            try:
                confirm_choice = int(input("Enter your choice (1-2): "))
            except ValueError:
                print("Invalid choice! Please enter 1 or 2.")
                continue

            if confirm_choice == 1:
                otp = random.randint(1000, 9999)
                print("\nYour OTP is:", otp)
                print("Booking confirmed!")
                print("Once the OTP has been shared, the ride cannot be cancelled.")
                break
            elif confirm_choice == 2:
                print("\nRide cancelled. No OTP has been shared.")
                break
            else:
                print("Invalid choice! Please enter 1 or 2.")

    elif main_choice == 2:
        print("\nThank you for using the Cab Booking Chatbot. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1 or 2.")
