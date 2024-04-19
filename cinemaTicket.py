class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        
        
    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        
        self.__seats[id] = []
        
        for i in range(self.__rows):
            col = []
            for j in range(self.__cols):
                col.append(0)
            self.__seats[id].append(col)
            
    
    def book_seats(self, id, seat_list):
        show = next((show for show in self.__show_list if show[0] == id), None)
        if(show):
            show_id = show[0]
            for seat in seat_list:
                if seat[0] >= self.__rows or seat[1] >= self.__cols:
                    print(f'Sorry! Seat {seat} is out of bound.')
                else:
                    if(self.__seats[show_id][seat[0]][seat[1]] == 0):
                        self.__seats[show_id][seat[0]][seat[1]] = 1
                        print(f'Seat {seat} booked for show {id}')
                    else:
                        print(f'Sorry! Seat {seat} is already booked for show {id}.')
        else:
            print(f'Sorry! Show Id: {id} is not valid.')


    def view_show_list(self):
        print("------------------------")
        for show in self.__show_list:
            print(f'Movie Name: {show[1]} Show Id: {show[0]} Time: {show[2]}')
        print("------------------------")


    def view_available_seats(self, id):
        show = next((show for show in self.__show_list if show[0] == id), None)
        print("------------------------")
        if(show):
            show_id = show[0]
            for i in range(self.__rows):
                for j in range(self.__cols):
                    print(self.__seats[show_id][i][j], end=" ")
            
                print()
                    
        else:
            print(f'Sorry! Show ID: {id} is not valid.')
        print("------------------------")

class Star_Cinema:
    __hall_list = []
    
    def __init__(self) -> None:
        pass
    
    def entry_hall(self, hall):
        self.__hall_list.append(hall)
    
    @property
    def hall_list(self):
        return self.__hall_list

    
hall = Hall(7, 8, 1)
star_cinema = Star_Cinema()
star_cinema.entry_hall(hall)

hall.entry_show(101, "A", "16/04/2024  10:30PM")
hall.entry_show(201, "B", "18/04/2024  9:00PM")
hall.entry_show(301, "C", "18/04/2024  1:00AM")


run = True
while run:
        print("1. View All Show Today")
        print("2. View Available Seats")
        print("3. Book Seat")
        print("4. Exit")
        
        ch = int(input("Enter Option: "))
        
        if ch == 1:
            for hall in star_cinema.hall_list:
                hall.view_show_list()
        elif ch == 2:
            show_id = int(input("Enter Show Id: "))
            hall.view_available_seats(show_id)
        elif ch == 3:
            show_id = int(input("Enter Show Id: "))
            tickets = []
            
            row = int(input('Enter Row : '))
            col = int(input('Enter Col : '))
            tickets.append((row, col))

            hall.book_seats(show_id, tickets)
        elif ch == 4:
            run = False
        else:
            print("Invalid Option")
            
        