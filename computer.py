class Computer:

    # What attributes will it need?
    computer_id: str
    description: str 
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, computer_id: str,
                    description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
        self.computer_id = computer_id
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
         # You'll remove this when you fill out your constructor

    # What methods will you need?
    def __str__(self) -> str:
        return "Desc: " + str(self.description) + "\n" + "Processor:" + str(self.processor_type) + "\n"+ "Hard Drive:" + str(self.hard_drive_capacity) + "\n"

def update_price(self, new_price: float):
        """Update the price of the computer"""
        self.price = new_price
        print(f"Updated price for computer ID {self.computer_id} to {self.price}")

def update_os(self, new_os: str):
        """Update the OS of the computer"""
        self.os = new_os
        print(f"Updated OS for computer ID {self.computer_id} to {self.os}")
    
def get_info(self):
        """Get a string representation of the computer's info"""
        return f"ID: {self.computer_id}, Description: {self.description}, Processor: {self.processor}, Memory: {self.memory}GB, Storage: {self.storage}GB, OS: {self.os}, Year: {self.year_made}, Price: ${self.price}"


def main():
    my_computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    print("Description:", my_computer.description)
    
main()