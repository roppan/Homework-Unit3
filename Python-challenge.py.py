# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:17:49 2020

@author: ato_o
"""
import os
import csv
    
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0
    
    
csvpath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

    with open(csvpath, newline='') csvfile:
        
    csvreader = csv.reader(svfile, delimiter=',')
        
        csv_header = next(csvreader)
        row = next(csvreader)
        
        previous_row = int(row[1])
        total_months += 1
        net_amount += int(row[1])
        greatest_increase = int(row[1])
        greatest_increase_month = row[0]
        
        row csvreader:
        total_months += 1
        
        net_amount += int(row[1])
        
        reenune_change = int(row[1]) - previois_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        int(row[1]) > greatest_increase:
            greatest_incrase = int(row[1])
            greatest_increase_month = row[0]
            
        int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]
            
    average_change = s(monthly_change)/ (monthly_change)
    
    highest = (monthly_change)
    lowest = (monthly_change)
    
    print(f"Financial Analysis")
    print(f".........................")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_amount}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits:, {greatest_increase_month},(${lowest})")
    
    output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_revised.text')
    (output_file, "w',) as txtfile:
        
        txtfile.write(f"Financial Analysis\n")
        txtfile.write(f"................................\n")
        txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${net_amount}\n")
        txtfile.write(f"Average Change: ${average_change}\n")
        txtfile.write(f"Greatest Inrease in Prifits:, {greatest_increase-month}, ${highest})\n")
        txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease-month}, (${lowest})\n")
        
        
        
        
        
        
        
        
        
        
        
        
                    
            
    