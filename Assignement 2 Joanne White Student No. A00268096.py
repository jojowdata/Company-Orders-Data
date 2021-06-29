# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:17:16 2019

Assignment 2 Programming for Big Data 
Reading in data from a .csv file processing it and outputting results to the
screen.

@author: Joanne White 
Student Number: A00268096
"""
import csv

FILENAME = "ProjectData.csv"
provinces = ('Munster','Leinster','Connacht','Ulster')
ship_mode = ('Delivery Truck','Express Air','Regular Air')
UNDER_50 = 50
UNDER_100 = 100
UNDER_1000 = 1000
RANGE_30 = 30
RANGE_40 = 40


# Opens the csv data file and reads it into a dictionary
def load_data():
 
    with open (FILENAME,'r') as file_handler:
        reader = csv.DictReader(file_handler)
        
        # Parsing the values for each row and adding to array
        parsed_rows = []
        for row in reader:
            order_id = int(row['Order'])
            order_quantity = int(row['Order Quantity'])
            sales = float(row['Sales'])
            ship_mode = str(row['Ship Mode'])
            profit = float(row['Profit'])
            shipping_cost = float(row['Shipping Cost'])
            province = str(row['Province'])
            
            # Add into a dictoionary
            parsed_rows.append({
                    'order_id':order_id,
                    'order_quantity':order_quantity,
                    'sales':sales,
                    'ship_mode':ship_mode,
                    'profit':profit,
                    'shipping_cost':shipping_cost,
                    'province':province,
            })
     
        # Makes the list of dictionaries available to other functions
        return parsed_rows
    
# Returns the total quantities for each province       
def show_province_totals(data,province):
   
    total_quantity = 0
    total_sales = 0
    total_profit = 0
    total_shipping_costs = 0
    
    print('Totals for ' + province + ':')
    # Loop each row of the dictionary 
    for row in data:
        # Check if province doesn't match
        if row['province'] != province:
            continue
        # Add quantity to province total
        total_quantity += row['order_quantity']
        total_sales += row['sales']
        total_profit+= row['profit']
        total_shipping_costs += row['shipping_cost']
    
    
    # Print the totals required to the screen
    print_totals_to_screen(total_quantity,total_sales,total_profit,total_shipping_costs)  

# Returns the total quantities for each shipping mode
def show_shipping_totals(data,ship_type):
    total_quantity = 0
    total_sales = 0
    total_profit = 0
    total_shipping_costs = 0
    
    print('Totals for ' + ship_type + ':')
    # Loop each row of the dictionary 
    for row in data:
        #Check if ship_mode matches 
        if row['ship_mode'] != ship_type:
            continue
        # Add quantity to shipping mode total
        total_quantity += row['order_quantity']
        # Keep a running total for each required total
        total_quantity += row['order_quantity']
        total_sales += row['sales']
        total_profit+= row['profit']
        total_shipping_costs += row['shipping_cost']
    
    # Print the totals required to the screen
    print_totals_to_screen(total_quantity,total_sales,total_profit,total_shipping_costs)    


# Prints header for the orders under query
def show_number_order_header(under_value,category):
    print('TOTAL NUMBER OF ORDERS UNDER €' + str(under_value) + ' FOR '+ (category))

# Returns the orders under a certain euro value for each province and 
# shipping mode    
def total_orders_under(data,category,under_num):
    # Print("in total orders under")
    total_order = 0
    total_sales = 0
    total_profit = 0
    total_shipping_costs = 0
    
    # Loop each row of the dictionary 
    for row in data:
        # Check if value is less than or equals passed value
        if row['sales'] <= under_num:
            continue
        if row['province'] != category: 
            if row['ship_mode'] != category:
                continue
        # Add quantity to total order
        total_order += row['order_quantity']
         # Keep a running total for each required total
        total_sales += row['sales']
        total_profit+= row['profit']
        total_shipping_costs += row['shipping_cost']
                                                                   
    # Print the totals required to the screen
    print_totals_to_screen(total_order,total_sales,total_profit,total_shipping_costs)     

# Prints header to screen for totals    
def print_totals_to_screen(total_order,total_sales,total_profit,total_shipping_costs):
    # Print the totals required to the screen     
    print("Total order quantities:"+ str(total_order) )
    print("Total sales :€"+ format(total_sales, ",.2f") ) 
    print('Total profit :€' + format(total_profit, ",.2f"))
    print('Total shipping costs :€' + format(total_shipping_costs, ",.2f"))
    print()

def show_orders_given_quantity_range(data,range_num):
    # Printed_row = False
    range_counter = 0
    
    # Loop each row of the dictionary 
    for row in data:
        # Check if passed range is in a row 
        if row['order_quantity'] == range_num:
            range_counter += 1
        
            print (f"Order ID: {row['order_id']}, " 
                                + f"Order Quantity: {row['order_quantity']}, "
                                + f"Sales: €{row['sales']:,.2f},"
                                + f"Shipping Mode:{row['ship_mode']},"
                                + f"Profit: €{row['profit']:,.2f},"
                                + f"Shipping Cost: €{row['shipping_cost']:,.2f},"
                                + f"Province: {row['province']}.")
            
    # If there hasn't been any found print message   
    if range_counter != 0:
        print()
        print('THE TOTAL NUMBER OF RECORDS FOR THE RANGE OF '
              + str(range_num) + ' IS ' + str(range_counter) )
        print()
    else:   
        print ('NO ORDERS OF THAT QUANTITY!')
    
                                                                   

def main():
    # Call the load data function
    data = load_data()
    
    print()
    print('WELCOME TO ANALYSIS OF ORDERS WITHIN '+ FILENAME + ' FILE. \n')
    print('PROVINCIAL STATS \n')
    # Call the show provinces totals function 
    for province in provinces:   
        show_province_totals(data,province)
    print()
    
    print('SHIPPING STATS \n')
    # Call show ships totals function
    for ship_type in ship_mode:
        show_shipping_totals(data,ship_type)
    print()
     
    print('TOTAL NUMBER OF ORDERS UNDER €' + str(UNDER_50) + ' FOR ALL PROVINCES ')
    print()
    
    # Call total orders for 50 euro or less in sales:
    for province in provinces:
        # Print header for this under certain euro value
        show_number_order_header(UNDER_50,province)
        total_orders_under(data,province,UNDER_50,)
    print()
    
    print('TOTAL NUMBER OF ORDERS UNDER  ' + str(UNDER_50) + ' FOR ALL SHIPPING MODES ')
    print()
    
    # Call total orders for 50 euro or less in sales:
    for ship_type in ship_mode:
        # Print out header to the screen
        show_number_order_header(UNDER_50,ship_type)
        total_orders_under(data,ship_type,UNDER_50,)
    print()
    
    # Call total orders for 100 euro or less in sales:
    print('TOTAL NUMBER OF ORDERS UNDER €' + str(UNDER_100) + ' FOR ALL PROVINCES ')
    print()
    
    for province in provinces:
        # Print out header to the screen
        show_number_order_header(UNDER_100,province)
        total_orders_under(data,province,UNDER_100,)
    print()
    
    print('TOTAL NUMBER OF ORDERS UNDER €' + str(UNDER_100) + ' FOR ALL SHIPPING MODES ')
    print()
    
    # Call total orders for 100 euro or less in sales:
    for ship_type in ship_mode:   
        # Print out header to the screen
        show_number_order_header(UNDER_100,ship_type)
        total_orders_under(data,ship_type,UNDER_100,)
    print()
     

    # Call total orders for 1000  euro or less in sales:
    print('TOTAL NUMBER OF ORDERS UNDER €' + str(UNDER_1000) + ' FOR ALL PROVINCES ')
    print()
    
    for province in provinces: 
        # Print out header to the screen
        show_number_order_header(UNDER_1000,province)
        total_orders_under(data,province,UNDER_1000,)
    print()
    
    print('TOTAL NUMBER OF ORDERS UNDER €' + str(UNDER_1000) + ' FOR ALL SHIPPING MODES ')
    print()
    
    # Call total orders for 100 euro or less in sales:
    for ship_type in ship_mode: 
        show_number_order_header(UNDER_1000,ship_type)
        total_orders_under(data,ship_type,UNDER_1000,)
    print()
    
    # Call show orders given quantity range of 30
    show_orders_given_quantity_range(data,RANGE_30)
    print()
    
    # Call show orders given quantity range of 40
    show_orders_given_quantity_range(data,RANGE_40)
    
    
# Main
if __name__== "__main__":
    main()