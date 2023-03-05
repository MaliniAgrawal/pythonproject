# pythonproject

def calculate_total_cost(item_details):
    base_cost = item_details.get("base_cost", 0)
    shipping_cost = item_details.get("shipping_cost", 0)
    tax_rate = item_details.get("tax_rate", 0.0)

    total_cost = base_cost + shipping_cost + (base_cost * tax_rate)
    return total_cost




items = {"base_cost": 100, "shipping_cost": 10, "tax_rate": 0.10}

total_cost = calculate_total_cost(items)
print(total_cost)

# code to see comparison for double two char in two string

def string_match(a, b):
    count = 0
    for i in range(len(a)-1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count
#OR same code in better way
 def string_match(a, b):
    # Figure which string is shorter.
    shorter = min(len(a), len(b))
    count = 0

    # Loop i over every substring starting spot.
    # Use length-1 here, so can use char str[i+1] in the loop
    for i in range(shorter - 1):
        a_sub = a[i:i + 2]
        b_sub = b[i:i + 2]
        if a_sub == b_sub:
            count = count + 1

    return count

#  code for ingnoring num in list
def sum_78(nums):
    sum = 0
    ignore_section = False
    for num in nums:
        if num == 7:
            ignore_section = True
        elif num == 8 and ignore_section:
            ignore_section = False
        elif not ignore_section:
            sum += num
    return sum

