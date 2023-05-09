# Variant 2
# Task:
# Train ticket availability system
# Warning: Very simplified version!

data = (
    {
        'route_number': 1,
        'route': 'Boston - Dallas',
        'departure_time': '13:00',
        'arrival_time': '22:00',
    },
    {
        'route_number': 2,
        'route': 'Boston - Detroit',
        'departure_time': '8:00',
        'arrival_time': '16:30',
    }
)


class Train:
    def __init__(self, route_data):
        self.route_data = route_data
        self.completed = None

    def build(self):
        blank = {
            'coach': [num for num in range(1, 6)],
            'number': self.route_data['route_number'],
            'route': self.route_data['route'],
            'departure_time': self.route_data['departure_time'],
            'arrival_time': self.route_data['arrival_time'],
        }
        self.completed = blank

    def get_completed(self):
        return self.completed


class Ticket:
    def __init__(self, ticket_data):
        self.ticket_data = ticket_data

    def show_ticket(self):
        print('--- TICKET ---')
        print(f'Train number: {self.ticket_data["train_number"]}')
        print(f'Route: {self.ticket_data["route"]}')
        print(f'Seat: {self.ticket_data["seat_number"]}')
        print(f'Time: {self.ticket_data["departure_time"]} - {self.ticket_data["arrival_time"]}')
        print('---')


class Terminal:
    __busy = 'X'

    def __init__(self, trains_data):
        self.trains = trains_data
        self.train_numbers = []
        self.tickets = []
        self.order = {'train_number': 0, 'seat_number': None}

    def train_numbers_parse(self):
        for train in self.trains:
            self.train_numbers.append(train['number'])

    def show_schedule_board(self):
        print('--- Schedule Board ---')
        print('|Train number|Route|Departure time|Arrival time|')
        for train in self.trains:
            number = train['number']
            route = train['route']
            departure_time = train['departure_time']
            arrival_time = train['arrival_time']
            print(f'{number} {route} {departure_time} {arrival_time}')
        print('---')

    def show_coach(self, train_number):
        status = False
        for train in self.trains:
            if train['number'] == train_number:
                for item in train['coach']:
                    if item != self.__busy:
                        status = True
                if status:
                    print(train['coach'])
                    return True
                else:
                    print('There are no empty seats for passengers')
                    return False

    def provide_coach(self, train_number):
        coach = []
        for train in self.trains:
            if train['number'] == train_number:
                for item in train['coach']:
                    if item != self.__busy:
                        coach.append(item)
                    else:
                        continue
        return coach

    def buy_ticket(self):
        ticket_data = {}
        for train in self.trains:
            if train['number'] == self.order['train_number']:
                ticket_data['train_number'] = train['number']
                ticket_data['route'] = train['route']
                ticket_data['departure_time'] = train['departure_time']
                ticket_data['arrival_time'] = train['arrival_time']
                ticket_data['seat_number'] = self.order['seat_number']
                for idx, i in enumerate(train['coach']):
                    if i == self.order['seat_number']:
                        train['coach'][idx] = self.__busy
        ticket = Ticket(ticket_data)
        self.tickets.append(ticket)
        print('$$$ Train ticket bought $$$')

    def get_tickets(self):
        return self.tickets

    def get_train_numbers(self):
        return self.train_numbers

    def set_train_number(self, num):
        self.order['train_number'] = num

    def set_seat_number(self, num):
        self.order['seat_number'] = num


def main():
    trains = []
    for current_data in data:
        train = Train(current_data)
        train.build()
        trains.append(train.get_completed())
    terminal = Terminal(trains)
    terminal.train_numbers_parse()
    while True:
        terminal.show_schedule_board()
        answer = input('Want to buy a train ticket? [Y/N]>')
        if answer.upper() == 'N':
            print('Goodbye')
            break
        if answer.upper() == 'Y':
            while True:
                try:
                    answer = int(input('Enter train number >'))
                    if answer not in terminal.get_train_numbers():
                        raise ValueError
                    break
                except ValueError:
                    print('There is no such train!')
            terminal.set_train_number(answer)
            status = terminal.show_coach(answer)
            if status:
                coach = terminal.provide_coach(answer)
                while True:
                    try:
                        print('To exit 0 enter')
                        answer = int(input('Enter seat number >'))
                        if answer == 0:
                            break
                        if answer not in coach:
                            raise ValueError
                        break
                    except ValueError:
                        print('There is no such seat!')
                terminal.set_seat_number(answer)
                terminal.buy_ticket()
    tickets = terminal.get_tickets()
    for ticket in tickets:
        ticket.show_ticket()


if __name__ == '__main__':
    main()
