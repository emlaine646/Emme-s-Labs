#----------------------------------Source Code----------------------------------
"""Emme's Lab #10: Makes a class called employee with a subclass of Production Workers.  Each worker should
get a name, emp_number, a shift number,and a pay rate.  The user is then prompted to create an employee
object and if the string inputted is empty the name of the user will be None.  The benefits for this
user is determined by taking their employee number and comparing if it is above or below 500. """

# Constants
MIN_EMP_NUM = 100
MAX_EMP_NUM = 999
BENEFIT_CUTOFF = 500
DEFAULT_NAME = "Jane Doe"

MIN_SHIFT = 1
MAX_SHIFT = 2
MIN_PAY = 3.00
MAX_PAY = 19.99

#define employee class
class Employee:
    def __init__(self, name, emp_number):
        self.__name = None
        self.__emp_number = None
        self.__benefits = False
        self.set_name(name)
        self.set_emp_number(emp_number)
    #determine if user qualifies for benefits
    def determine_benefits(self, emp_number):
        if emp_number < BENEFIT_CUTOFF:
            self.__benefits = True
        else:
            self.__benefits = False

    # Accessors
    def get_name(self):
        return self.__name

    def get_emp_number(self):
        return self.__emp_number

    def get_benefits(self):
        return self.__benefits

    # Mutators
    def set_name(self, name):
        if name and name.replace(" ", "").isalpha():
            self.__name = name
        elif len(name) < 0:
            raise ValueError("Name cannot be empty")
            self.__name = DEFAULT_NAME
        else:
            print("Invalid name. Must contain only alphabetic characters.")

    def set_emp_number(self, emp_number):
        if MIN_EMP_NUM <= emp_number <= MAX_EMP_NUM:
            self.__emp_number = emp_number
            self.determine_benefits(emp_number)
        else:
            print("Invalid employee number. Must be between 100 and 999.")

    def __str__(self):
        if self.__benefits:
            benefit_status = "Benefits"
        else:
            benefit_status = "No benefits"
        return f"{self.__name} #{self.__emp_number}\n{benefit_status}"

class ProductionWorker(Employee):
    #creates subclass
    def __init__(self, name, emp_number, shift_number, pay_rate):
        super().__init__(name, emp_number)
        self.__shift_number = None
        self.__pay_rate = None
        self.set_shift_number(shift_number)
        self.set_pay_rate(pay_rate)

    # Accessors
    def get_shift_number(self):
        return self.__shift_number

    def get_pay_rate(self):
        return self.__pay_rate

    # Mutators
    def set_shift_number(self, shift_number):
        if shift_number in (MIN_SHIFT, MAX_SHIFT):
            self.__shift_number = shift_number
        else:
            print("Invalid shift number. Must be 1 (Day) or 2 (Night).")

    def set_pay_rate(self, pay_rate):
        if MIN_PAY <= pay_rate <= MAX_PAY:
            self.__pay_rate = pay_rate
        else:
            print("Invalid pay rate. Must be between $3.00 and $19.99.")

    def __str__(self):
        base_str = super().__str__()
        if self.__shift_number == 1:
            shift = "Day"
        else:
            shift = "Night"
        return f"{base_str}\nShift: {shift}\nPay Rate: ${self.__pay_rate:.2f}"

# Main function
def main():
    print("=== Enter Production Worker Info ===")
    name = input("Enter name: ")
    try:
        number = int(input("Enter employee number (100-999): "))
        shift = int(input("Enter shift number (1=Day, 2=Night): "))
        pay = float(input("Enter pay rate ($3.00 - $19.99): "))
    except ValueError:
        print("Invalid input. Please try again.")
        return

    worker1 = ProductionWorker(name, number, shift, pay)
    print("\nWorker 1 Info:")
    print(worker1)

    print("\nTesting Validation with Bad Data:")
    worker2 = ProductionWorker("Sandavol", 590, 1, 19.00)
    print("Initial worker2 state:")
    print(worker2)

    print("\nBad Values:")
    worker2.set_name("123Tom")
    worker2.set_emp_number(9999)
    worker2.set_shift_number(3)
    worker2.set_pay_rate(25.00)
    print("\nworker2 after setting bad data:")
    print(worker2)

if __name__ == "__main__":
    main()
    
    
