# Week 3 Assignment
# Author: Bikila Keneni

# Function to calculate discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, apply it.
    Otherwise, return the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Main program
if name == "main":
    # Prompt the user for input
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Call the function
        final_price = calculate_discount(price, discount_percent)

        # Display result
        if discount_percent >= 20:
            print(f"Discount applied! Final price is: {final_price:.2f}")
        else:
            print(f"No discount applied. Original price is: {price:.2f}")

    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")