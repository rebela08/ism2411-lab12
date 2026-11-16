#1. Using an ETL pipeline in Python automates repetition, and can be used to sift through extremely large datasets that would cause issues in excels software.
#2. An online order system would benefit greatly from append-mode log files, as it could record customer transactions, status of the transaction, and the time it took place automatically. This would be the correct tool for the job as it would not overwrite old data entries, preserving it for auditing purposes.

import csv

with open('data/sales.csv', mode='r', newline='') as file:
          reader = csv.reader(file)
          for row in reader:
            print(row)

with open('data/sales.csv', mode='r', newline='') as file:
      reader = csv.reader(file)

      header = next(reader)
      print("Header:", header)

      for row in reader:
            print(row)

total_revenue = 0.0

with open('data/sales.csv', mode='r', newline='') as file:
      reader = csv.reader(file)
      header = next(reader)

      for row in reader:
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            line_total = price * quantity
            total_revenue += line_total

            print (f"{product}: {quantity} units * ${price:.2f} = ${line_total:.2f}")

print(f"Total Revenue: ${total_revenue:.2f}")

original_count = 0
written_count = 0

with open('data/sales.csv', mode='r', newline='') as infile, \
    open('data/cleaned.csv', mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    next(reader)
    writer.writerow(['Product', 'Price', 'Quantity', 'Total'])

    for row in reader:
          original_count += 1

          product = row[0]
          price = float(row[1])
          quantity = int(row[2])
          total = price * quantity

          if total > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
                written_count += 1

print(f"Rows Written: {written_count} vs. Original Rows: {original_count}")

total_revenue = 0.0

with open('data/sales.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
          product = row["product"]
          price = float(row["price"])
          quantity = int(row["quantity"])

          total_revenue += price * quantity

print(f"Total Revenue: ${total_revenue:,.2f}")

product_summary = {}

with open('data/sales.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        revenue = float(row["price"]) * int(row["quantity"])

        if product in product_summary:
            product_summary[product] += revenue
        else:
            product_summary[product] = revenue

for product_name in sorted(product_summary):
    print(f"{product_name}: ${product_summary[product_name]:.2f}")

from datetime import datetime

total_revenue = 0.0

with open('data/sales.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_revenue += float(row["price"]) * int(row["quantity"])

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('data/run_log.txt', mode='a', encoding='utf-8') as log_file:
    log_file.write(f"{timestamp} - Total Revenue: ${total_revenue:,.2f}\n")

print("Log Entry Appended Successfully.")