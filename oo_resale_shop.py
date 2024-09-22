from typing import Dict, Optional

class ResaleShop:
    # How will you set up your constructor?
    def __init__(self):
        """Initialize the resale shop with an empty inventory and item ID counter"""
        self.inventory: Dict[int, Dict] = {}  # Inventory will store computers with their IDs as keys
        self.itemID: int = 0  # Item ID counter

    """
    Takes in a Dict containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """
    def buy(self, computer: Dict):
        self.itemID += 1  # increment itemID
        self.inventory[self.itemID] = computer  # add to inventory
        return self.itemID

    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id]["price"] = new_price
            print(f"Updated price for item {item_id} to ${new_price}")
        else:
            print(f"Item {item_id} not found. Cannot update price.")

    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]  # remove item from inventory
            print(f"Item {item_id} sold!")
        else:
            print(f"Item {item_id} not found. Please select another item to sell.")

    """
    Prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id, computer in self.inventory.items():
                # Print its details
                print(f'Item ID: {item_id} : {computer}')
        else:
            print("No inventory to display.")

    """
    Refurbish a computer: update price based on year made, optionally update the OS
    """
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id]  # locate the computer
            year_made = int(computer["year_made"])

            # Update price based on the year made
            if year_made < 2000:
                computer["price"] = 0  # too old to sell, donation only
            elif year_made < 2012:
                computer["price"] = 250  # heavily-discounted price on machines 10+ years old
            elif year_made < 2018:
                computer["price"] = 550  # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000  # recent stuff

            # Optionally update the OS if a new OS is provided
            if new_os is not None:
                computer["operating_system"] = new_os

            print(f"Item {item_id} has been refurbished. New price: ${computer['price']}")
        else:
            print(f"Item {item_id} not found. Please select another item to refurbish.")

# Main function to test the ResaleShop functionality
def main():
    # Create a new ResaleShop instance
    shop = ResaleShop()

    # Add a computer to the inventory
    item_id = shop.buy({
        "description": "2019 MacBook Pro",
        "processor_type": "Intel",
        "hard_drive_capacity": 256,
        "memory": 16,
        "operating_system": "High Sierra",
        "year_made": 2019,
        "price": 1000
    })

    # Print the inventory
    shop.print_inventory()

    # Update the price of the computer
    shop.update_price(item_id, 900)

    # Refurbish the computer with a new OS
    shop.refurbish(item_id, "macOS Monterey")

    # Sell the computer
    shop.sell(item_id)

    # Try to print the inventory after the sale
    shop.print_inventory()

# Run the main function
main()