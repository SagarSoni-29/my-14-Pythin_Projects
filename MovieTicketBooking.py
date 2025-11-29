print(" Welcome to the Movie Ticket Booking System!")

movies = ["Avengers", "Bahubali", "Kantara", "KGF 2"]


print("\nAvailable Movies:")
for i, movie in enumerate(movies, start=1):
    print(f"{i}. {movie}")


choice = int(input("\nEnter the movie number you want to watch: "))

tickets = int(input("How many tickets do you want to book? "))

ticket_price = 150  
total_amount = tickets * ticket_price

print(f"\n Ticket Price: ₹{ticket_price} per ticket")
print(f" Total Amount: ₹{total_amount}")

confirm = input(" Booking Confirmed!\nEnjoy your movie !!!")