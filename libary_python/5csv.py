# import csv

# with open("data.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id"])
#     writer.writerow([1000, 1])

import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id"])
    writer.writerow([1000, 1])