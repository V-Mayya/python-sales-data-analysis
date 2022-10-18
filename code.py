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

#percentage change in sales over the months
percentage = []

for i1, i2 in zip(sales, sales[1:]):
    percentages = ((i2 - i1) / i1)*100
    percentages = round(percentages, 2)
    percentage.append(percentages)

print('Percentage change in sales over the months: {}'.format(percentage))

#---Basic Data Visualisations---
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

#---Advanced Data Visualisations---
#plot
font1 = {'family':'serif','color':'blue','size':15}
font2 = {'family':'serif','color':'darkred','size':20} 

#1. plot profit (bar graph) 
plt.bar(months, profit, label = 'profit', color = 'green')
plt.xlabel('months', fontdict = font1)
plt.ylabel('profit', fontdict = font1)
plt.title('Monthly profit in 2018', fontdict = font2)
plt.grid(axis = 'y')
plt.ylim(min(profit)-1000,max(profit)+1000)
plt.show()

#2. plot sales and expenditure (line graphs)
plt.plot(months, sales, label = "sales", marker = 'o', ms = 2, mec = 'green', mfc = 'green')
plt.plot(months, expenditures, label = "expenditures", marker = 'o', ms = 2, mec = 'red', mfc = 'red')
plt.xlabel('Months', fontdict = font1)
plt.ylabel('Sales/Expenditures', fontdict = font1)
plt.title('Monthly sales and expenditures in 2018', fontdict = font2)
plt.legend(loc='upper right')
plt.text(max_month,max_sales,'Max. sales were {} during {}.'.format(max_sales,max_month),horizontalalignment='center')
plt.ylim((min_sales-2000,max_sales+3000))
plt.show()

#3. scatter 
col = ['blue','orange','green','red','purple','brown','pink','black','olive','cyan','darkblue','gray']

plt.scatter(x = profit, y = expenditures, s = sales, c = col, alpha = 0.5)

plt.xlabel('profit', fontdict = font1)
plt.ylabel('expenditures', fontdict = font1)
plt.title('2018 sales per month', fontdict = font2)

plt.xlim(-3000,8000)
plt.ylim(0,6000)

for i, txt in enumerate(months):
    plt.annotate(txt, (profit[i], expenditures[i]),horizontalalignment='center')

plt.grid(True)

# Show the plot
plt.show()

#4. plot percentage
set1 = [0]
set2 = [0]

for n in range(11):
    if percentage[n]<0:
        set1.append(percentage[n])
        set2.append(0)
    elif percentage[n]>=0:
        set1.append(0)
        set2.append(percentage[n])

plt.bar(months, set1, label = 'decreased', color = 'red')
plt.bar(months, set2, label = 'increased', color = 'darkblue')
plt.xlabel('months', fontdict = font1)
plt.ylabel('Δ sales', fontdict = font1)
plt.title('Percentage change in sales over the months', fontdict = font2)
plt.yticks([-50,0,50,100,150, 200,250], ['-50%','0%','+50%','+100%', '+150%', '+200%','+250%'])
plt.legend(loc='upper right')

plt.grid(axis = 'y')
plt.show()


