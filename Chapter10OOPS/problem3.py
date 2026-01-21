class Train:
    
    source = "IRCTC"
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def book_ticket(self,passengeName, destination):
        print(f"Ticket booked for {passengeName} from {self.source} to {destination} by train {self.name} ({self.number}).") 
        
    def getStatus(self, seat_number):
        print(f"Seat number {seat_number} is confirmed.")
        
    def getFare(self, distance):
        fare_per_km = 1.5
        total_fare = fare_per_km * distance
        print(f"The fare for {distance} km is ${total_fare}.")
        
    
vande_bharat = Train("Vande Bharat Express", "12345")
vande_bharat.book_ticket("Siddh","Mumbai")
vande_bharat.getStatus(45)
vande_bharat.getFare(500)