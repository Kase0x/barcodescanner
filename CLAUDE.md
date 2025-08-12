# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based web inventory management application that tracks barcode-based inventory using ADD/REMOVE operations. The application provides a web interface for data entry, real-time updates, database storage with SQLAlchemy, and Excel export functionality.

## Dependencies

Install all dependencies with:
```bash
pip install -r requirements.txt
```

Main dependencies:
- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Flask-SocketIO**: Real-time WebSocket communication
- **openpyxl**: Excel file operations

## Running the Application

```bash
python app.py
```

The web application will:
1. Start Flask server on http://localhost:5000
2. Create SQLite database (`inventory.db`) if it doesn't exist
3. Migrate existing Excel data (`inventory_log.xlsx`) to database on startup
4. Provide web interface for barcode scanning and inventory management

## Key Features

- **Web Interface**: Modern responsive web UI for barcode operations
- **Real-time Updates**: Live inventory updates using WebSocket connections
- **Operation Modes**: ADD (increase inventory) or REMOVE (decrease inventory)
- **Database Storage**: SQLite database with SQLAlchemy ORM
- **Excel Export**: Download current inventory as Excel file
- **Data Migration**: Automatically imports existing Excel data to database
- **Statistics Dashboard**: Real-time inventory statistics

## Architecture

- **Flask Web Application**: `app.py` contains all backend functionality
- **SQLite Database**: Persistent storage using SQLAlchemy ORM
- **Real-time Communication**: WebSocket support via Flask-SocketIO
- **Web Interface**: HTML template with JavaScript for interactive UI
- **Data Migration**: Automatic import from existing Excel files

## Database Schema

The SQLite database contains an `Inventory` table with:
- **id**: Primary key (auto-increment)
- **barcode**: Unique barcode identifier
- **total_count**: Current inventory count for this barcode
- **last_updated**: Timestamp of last transaction

## API Endpoints

- **GET /**: Main web interface
- **GET /api/inventory**: JSON list of all inventory items
- **POST /api/scan**: Process barcode scan (ADD/REMOVE operations)
- **GET /api/export**: Download Excel export of current inventory

## File Structure

- `app.py`: Main Flask application
- `templates/index.html`: Web interface template
- `requirements.txt`: Python dependencies
- `inventory.db`: SQLite database (created automatically)
- `inventory_log.xlsx`: Legacy Excel file (migrated to database on startup)
- `main.py`: Original command-line version (legacy)

## Development Notes

- No build process required - direct Python execution
- No test framework currently implemented
- Database automatically created on first run
- Legacy Excel data automatically migrated to database
- Inventory counts cannot go below 0 (REMOVE operations are clamped)
- Real-time updates broadcast to all connected web clients
- Excel exports include current timestamp in filename