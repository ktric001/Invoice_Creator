import webbrowser
from fpdf import FPDF


class BillableHours:
    """
    Object that contains the cost of the bill
    """
    def __init__(self, week, hours, month):
        self.week = week
        self.hours = hours
        self.month = month

    def calculate(self, week, hours, month):
        hours_to_bill = self.hours * self.week * self.month
        return hours_to_bill


class Client:
    """
    Object that contains the client information and is to pay the bill.
    """
    def __init__(self, client_name, rate):
        self.client_name = client_name
        self.rate = rate


billed_hours = BillableHours(4,40,1)
ligma = Client('Ligma Inc', 85)

print('The billed rate of ' + ligma.client_name + ' is '+ str(ligma.rate)+ ' dollars an hour.')
print('The weekly rate is ' + str(billed_hours.calculate(billed_hours.week,
                                                         billed_hours.hours,
                                                         billed_hours.month) * ligma.rate/4))
print('And the monthly is therefore '+ str(billed_hours.calculate(billed_hours.week,
                                                                  billed_hours.hours,
                                                                  billed_hours.month)*ligma.rate))