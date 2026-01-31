# Global Economic Database

A command-line application for managing and visualizing country economic data with integrated Wikipedia information retrieval.

## Overview

This Python application provides an interactive menu-driven interface to query, visualize, and manage economic data for countries around the world. Users can retrieve specific economic metrics, view country information from Wikipedia, add or update records, and generate bar charts for data visualization.

## Features

- **Query Country Data**: Retrieve economic metrics for one or multiple countries
- **Wikipedia Integration**: Fetch country information and summaries directly from Wikipedia
- **Data Management**: Add, update, and remove country records
- **Data Visualization**: Generate bar charts for selected metrics and countries
- **Directory Listing**: View all available countries in the database
- **Interactive Menu**: User-friendly command-line interface

## Economic Metrics Tracked

The database tracks the following metrics for each country:
- **GDP** (Gross Domestic Product)
- **Population**
- **Debt** (National Debt)
- **Unemployment** Rate
- **Literacy** Rate
- **TradeBal** (Trade Balance)
- **Interest** Rate
- **Inflation** Rate

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Required Libraries

```bash
pip install pandas matplotlib wikipedia-api
```

Or use the provided requirements file:

```bash
pip install -r requirements.txt
```

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/global-economic-database.git
cd global-economic-database
```

2. Create a sample `CountryData.csv` file (see Data File Format section below)

3. Run the application:
```bash
python Global_Economic_Database.py
```

## Usage

### Main Menu Options

When you run the program, you'll see an interactive menu with the following options:

- **q** - Query country/countries data
- **i** - Retrieve country information from Wikipedia
- **a** - Add or update a country record
- **r** - Remove a country from the database
- **d** - Display directory of all countries
- **x** - Exit the program

### Example Usage

**Querying Data:**
```
Countries: United States, China
Metrics: GDP, Population
```

**Adding a Country:**
```
Country: Germany
Data: 4000000, 83000000, 2500000, 3.5, 99, 250000, 0.5, 2.1
```

**Viewing Information:**
```
Country: Japan
(Displays Wikipedia summary)
```

## Data File Format

The `CountryData.csv` file should be structured as follows:

```csv
Country,GDP,Population,Debt,Unemployment,Literacy,TradeBal,Interest,Inflation
United States,21000000,331000000,28000000,3.8,99,500000,0.25,2.3
China,14000000,1440000000,5000000,3.9,96,400000,0.5,1.5
```

### Sample Data File

A sample `CountryData.csv` file is included in this repository with data for several countries.

## Features Breakdown

### 1. Data Query (`readData`)
- Select specific countries and metrics
- Press Enter to select all countries or all metrics
- Option to generate bar chart visualization
- Charts are saved as `chart.png`

### 2. Wikipedia Search (`wiki_search`)
- Retrieves country information from Wikipedia API
- Displays first 200 characters of summary
- Verifies page existence

### 3. Add/Update Records (`add_record`)
- Add new countries to the database
- Update existing country data
- Requires all 8 metric values

### 4. Remove Records (`remove_record`)
- Delete country entries from the database
- Automatic confirmation message

### 5. Directory (`directory`)
- Lists all countries currently in the database
- Quick reference for available data

## Important Notes

### API Key Notice
**The Wikipedia API integration does not require an API key.** The code uses the public Wikipedia API through the `wikipedia-api` library. No personal API keys are stored or needed.

### Local Data Storage
The application reads from and writes to `CountryData.csv` in the same directory as the script. Make sure this file exists before running the program.

### Chart Generation
Charts are automatically saved as `chart.png` in the current directory. On Windows systems, the chart will open automatically in Microsoft Paint.

## Error Handling

The application includes error handling for:
- Invalid country names
- Incorrect number of data values when adding records
- Missing metrics or countries
- File read/write errors

## Project Structure

```
global-economic-database/
│
├── Global_Economic_Database.py    # Main application
├── CountryData.csv               # Economic data file (create this)
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── .gitignore                   # Git ignore file
└── LICENSE                      # License file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. See CONTRIBUTING.md for guidelines.

## Future Enhancements

Potential features for future development:
- Export data to different formats (Excel, JSON)
- Time-series data tracking
- Comparative analysis tools
- Web interface
- Database backend integration
- More visualization options

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Wikipedia API for country information
- pandas library for data manipulation
- matplotlib for data visualization

## Contact

For questions or feedback, please open an issue in this repository.
