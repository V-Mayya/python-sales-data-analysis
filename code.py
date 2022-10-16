import csv
import matplotlib.pyplot as plt
import numpy as np

with open('sales.csv', 'r') as sales_file:
  spreadsheet = csv.DictReader(sales_file)
  sales = []
  months = []
  expenditures = []

  for row in spreadsheet:
    monthly_sales = int(row['sales'])
    month = row['month']
    expenditure = int(row['expenditure'])
    sales.append(monthly_sales)
    months.append(month)
    expenditures.append(expenditure)

print('sales list: {}'.format(sales))

# 3. Output the total sales across all months
total_sales = sum(sales)
print('Total sales: {}'.format(total_sales)) 

#profit
profit = list()
for item1, item2 in zip(sales, expenditures):
  item = item1 - item2
  profit.append(item)
print('Profit: {}'.format(profit))

#min sales
min_sales = min(sales)
min_month = months[sales.index(min_sales)]
print('Min. sales were {} during {}.'.format(min_sales,min_month))

#max sales
max_sales = max(sales)
max_month = months[sales.index(max_sales)]
print('Max. sales were {} during {}.'.format(max_sales,max_month))

#avg.sales in 2018
average_sales = total_sales/len(sales)
print('Average sales during the months were {}.'.format(int(average_sales)))

#plot
#line graph (months and profit)
plt.plot(months, profit, color='green', linestyle='solid', marker='o', markerfacecolor='blue', markersize=5)
plt.xlabel('Months')
plt.ylabel('Profits')
plt.title('Profit over the months in 2018')
plt.axhline(y=0, linewidth = 2, linestyle = '--')
plt.show()

#pie chart (expenditure over the months in 2018)
x = np.array(expenditures)
all_labels = months
plt.pie(x, labels = all_labels, wedgeprops = {'linewidth' : 2, 'edgecolor' : 'white'})
plt.title("Expenditures over the months in 2018")
plt.show()

