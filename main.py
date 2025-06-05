import openpyxl
from openpyxl import Workbook
from datetime import datetime
import os

# Define the filename
filename = 'barcode_log.xlsx'

# Check if file exists, otherwise create it with headers
if not os.path.exists(filename):
    wb = Workbook()
    ws = wb.active
    ws.title = "Barcodes"
    ws.append(["Timestamp", "Barcode"])
    wb.save(filename)

# Open the workbook for appending
wb = openpyxl.load_workbook(filename)
ws = wb.active

print("Barcode logger started. Press Ctrl+C to stop.")

try:
    while True:
        barcode = input("Scan or enter barcode: ").strip()
        if barcode:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ws.append([timestamp, barcode])
            wb.save(filename)
            print(f"Saved: {barcode} at {timestamp}")
except KeyboardInterrupt:
    print("\nBarcode logger stopped.")
    wb.save(filename)
