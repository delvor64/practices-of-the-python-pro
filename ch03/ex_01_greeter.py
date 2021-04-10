import datetime

class Greeter:
    '''
    Greet Customers entering the store based on time of day and store.
    '''

    def __init__(self, name):
        self.name = name


    def greet(self, store):
        '''
        Greet the customer
        '''
        
        return (
            f'Welcome to {store}!\n'
            f"How's your {day()} {part_of_day()} going?\n"
            f"Here's a coupon for 20% off!\n"
        )


def part_of_day():
    '''
    Determine which part of the day to greet the customer with.
    '''

    hour = datetime.datetime.now().hour
    if hour < 12:
        part = 'Morning'
    elif hour < 17:
        part = 'Afternoon'
    else:
        part = 'Evening'
    
    return part


def day():
    '''
    Determine the day of the week.
    '''

    return datetime.datetime.now().strftime('%A')
