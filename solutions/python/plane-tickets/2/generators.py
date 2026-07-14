"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    index = 0
    while index < number:
        if index % 4 == 0:
            yield "A"
        elif index % 4 == 1:
            yield "B"
        elif index % 4 == 2:
            yield "C"
        else:
            yield "D"
        index += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    index = 0
    if number > 13:
        number += 4
    while index < number:
        if index % 4 == 0:
            letter = "A"
        elif index % 4 == 1:
            letter = "B"
        elif index % 4 == 2:
            letter = "C"
        else:
            letter = "D"
        if (index+4)//4 == 13:
            index += 4 
        seat_num = (index+4)//4
        yield str(seat_num) + letter
        index += 1
    


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = {}
    generator = generate_seats(len(passengers))
    for _, value in enumerate(passengers):
        seats[value] = next(generator)
    return seats
        


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seats in seat_numbers:
        yield seats + flight_id + ("0" * (12 - len(seats) - len(flight_id)))
