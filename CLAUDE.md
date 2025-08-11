# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python inventory management application that tracks barcode-based inventory using ADD/REMOVE operations. The application logs all transactions to an Excel file and maintains running inventory counts for each barcode.

## Dependencies

- **openpyxl**: Required for Excel file operations
- Install with: `pip install openpyxl`

## Running the Application

```bash
python main.py
```

The application will:
1. Create `inventory_log.xlsx` if it doesn't exist
2. Prompt for operation mode (ADD or REMOVE)
3. Start a continuous barcode scanning loop with 15-second timeout
4. Track inventory counts and log all transactions
5. Return to operation selection after 15 seconds of inactivity (does not exit)
6. Exit only with Ctrl+C

## Key Features

- **Operation modes**: ADD (increase inventory) or REMOVE (decrease inventory)
- **Inventory tracking**: Maintains running counts for each barcode
- **Auto-timeout**: Returns to operation selection after 15 seconds of no input
- **Persistent storage**: Loads existing inventory counts from Excel on startup
- **Cross-platform timeout**: Windows-specific implementation using msvcrt, Unix fallback with signal

## Architecture

- **Single file application**: `main.py` contains all functionality
- **Excel logging**: Uses openpyxl to maintain persistent inventory totals in `inventory_log.xlsx` (updates existing rows instead of appending)
- **In-memory tracking**: Dictionary-based inventory count management
- **Timeout handling**: Platform-specific input timeout implementation
- **Error handling**: KeyboardInterrupt and timeout handling for clean shutdown

## Excel File Structure

The generated `inventory_log.xlsx` contains columns:
- **Barcode**: The scanned barcode (unique identifier)
- **Total Count**: Current total inventory count for this barcode
- **Last Updated**: Timestamp of the last transaction for this barcode

## File Structure

- `main.py`: Main application script
- `inventory_log.xlsx`: Generated Excel file containing inventory logs (created automatically)

## Development Notes

- No build process required - direct Python execution
- No test framework currently implemented
- Application loads existing inventory counts on startup
- Inventory counts cannot go below 0 (REMOVE operations are clamped)
- Each barcode's total count is immediately updated in Excel to prevent data loss
- Excel file maintains one row per unique barcode with running totals