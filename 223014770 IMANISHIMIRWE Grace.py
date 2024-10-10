from collections import deque
trip_queue = []
undo_stack = []
available_flights = []

def undo(flight_id):
    undo_stack.append(flight_id)

def schedule_trip(flight_id):
    trip_queue.append(flight_id)

def undo_booking():
    if undo_stack:
        flight_id = undo_stack.pop()
        available_flights.append(flight_id)
    else:
        print("No trips scheduled.")

def take_trip():
    if trip_queue:
        flight_id = trip_queue.pop(0)
        available_flights.append(flight_id)

        
    else:
        print("No trips scheduled.")

    
    available_flights.remove(flight_id)
undo("Flight 123")
undo("Flight 456")
undo("Flight 1234")
undo("Flight 456")
print("List Available flights for Stack(LIFO):",undo_stack)
schedule_trip("Flight 123")
schedule_trip("Flight 456")
take_trip()
print("List Available flights for queue(FIFO):", trip_queue)
from collections import deque
trip_queue = []
undo_stack = []
available_flights = []

def undo(flight_id):
    undo_stack.append(flight_id)

def schedule_trip(flight_id):
    trip_queue.append(flight_id)

def undo_booking():
    if undo_stack:
        flight_id = undo_stack.pop()
        available_flights.append(flight_id)
    else:
        print("No trips scheduled.")

def take_trip():
    if trip_queue:
        flight_id = trip_queue.pop(0)
        available_flights.append(flight_id)

        
    else:
        print("No trips scheduled.")

    
    available_flights.remove(flight_id)
undo("Flight 123")
undo("Flight 456")
undo("Flight 1234")
undo("Flight 456")
print("List Available flights for Stack(LIFO):",undo_stack)
schedule_trip("Flight 123")
schedule_trip("Flight 456")
take_trip()
print("List Available flights for queue(FIFO):", trip_queue)