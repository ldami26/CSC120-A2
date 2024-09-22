class Computer:
    # Attributes
    def __init__(self, computer_id: str,
                 description: str,
                 processor_type: str,
                 hard_drive_capacity: int,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: int):
        # Initializing attributes
        self.computer_id = computer_id
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # String representation of the object
    def __str__(self) -> str:
        return (f"Description: {self.description}\n"
                f"Processor: {self.processor_type}\n"
                f"Hard Drive: {self.hard_drive_capacity} GB\n"
                f"Memory: {self.memory} GB\n"
                f"Operating System: {self.operating_system}\n"
                f"Year Made: {self.year_made}\n"
                f"Price: ${self.price}")

    # Method to update the price
    def update_price(self, new_price: float):
        """Update the price of the computer"""
        self.price = new_price
        print(f"Updated price for computer ID {self.computer_id} to ${self.price}")

    # Method to update the operating system
    def update_os(self, new_os: str):
        """Update the OS of the computer"""
        self.operating_system = new_os
        print(f"Updated OS for computer ID {self.computer_id} to {self.operating_system}")

    # Method to get full information about the computer
    def get_info(self):
        """Get a string representation of the computer's info"""
        return (f"ID: {self.computer_id}, Description: {self.description}, "
                f"Processor: {self.processor_type}, Memory: {self.memory} GB, "
                f"Storage: {self.hard_drive_capacity} GB, OS: {self.operating_system}, "
                f"Year: {self.year_made}, Price: ${self.price}")

# Main function to create and test the Computer object
def main():
    # Creating a Computer object
    my_computer = Computer(
        "C001",  # computer_id
        "Mac Pro (Late 2013)",  # description
        "3.5 GHz 6-Core Intel Xeon E5",  # processor_type
        1024,  # hard_drive_capacity
        64,  # memory
        "macOS Big Sur",  # operating_system
        2013,  # year_made
        1500  # price
    )

    # Display the computer description
    print(my_computer)  # using __str__ method

    # Update the price
    my_computer.update_price(1200)

    # Update the operating system
    my_computer.update_os("macOS Monterey")

    # Get the updated computer info
    print(my_computer.get_info())

# Run the main function
main()