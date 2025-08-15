# Barcode Scanner Inventory Management

A Flask-based web application for managing inventory through barcode scanning with ADD/REMOVE operations. Features real-time updates, database storage, and Excel export functionality. Not gonna lie... I started this project, but I got Claude AI to finish it. At least it works great.

## Features

- **Web Interface**: Modern responsive web UI for barcode operations
- **Real-time Updates**: Live inventory updates using WebSocket connections
- **Operation Modes**: ADD (increase inventory) or REMOVE (decrease inventory)
- **Database Storage**: SQLite database with SQLAlchemy ORM
- **Excel Export**: Download current inventory as Excel file
- **Data Migration**: Automatically imports existing Excel data to database
- **Statistics Dashboard**: Real-time inventory statistics

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access Web Interface**
   Open http://localhost:5000 in your browser

The application will automatically:
- Create SQLite database (`inventory.db`) if it doesn't exist
- Migrate existing Excel data (`inventory_log.xlsx`) to database on startup
- Provide web interface for barcode scanning and inventory management

## Dependencies

- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Flask-SocketIO**: Real-time WebSocket communication
- **openpyxl**: Excel file operations

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

## Architecture

- **Flask Web Application**: Backend API and web server
- **SQLite Database**: Persistent storage using SQLAlchemy ORM
- **Real-time Communication**: WebSocket support via Flask-SocketIO
- **Web Interface**: HTML template with JavaScript for interactive UI
- **Data Migration**: Automatic import from existing Excel files

## Development Notes

- No build process required - direct Python execution
- Database automatically created on first run
- Legacy Excel data automatically migrated to database
- Inventory counts cannot go below 0 (REMOVE operations are clamped)
- Real-time updates broadcast to all connected web clients
- Excel exports include current timestamp in filename