# Enhanced-Swiggy-Restaurant-Analysis-with-Data-Manipulation
**Project Structure:**
```
swiggy_analysis_project/
│
├── swiggy.xlsx
│
├── scripts/
│   ├── __init__.py
│   ├── data_processing.py
│   ├── data_analysis.py
│
└── main.py
```

**Documentation: README.md**

Create a `README.md` file in the project root directory to provide an overview of your project, instructions for setup, and explanations of how to use it.

```markdown
# Enhanced Swiggy Restaurant Analysis

This project demonstrates data analysis and manipulation using Pandas and NumPy to analyze Swiggy restaurant data.

## Project Overview

This project performs the following tasks:
- Loads Swiggy restaurant data from 'swiggy.xlsx'.
- Cleans the data by removing missing values and duplicates.
- Analyzes data to provide insights on average price, average ratings, top-rated restaurants, popular food types, delivery time range, and more.
- Filters and sorts restaurants based on specific criteria.
- Saves manipulated data to an Excel file.

## Usage

1. Place the 'swiggy.xlsx' file in the project root directory.
2. Run the main script:
   ```
   python main.py
   ```

The script will load, clean, analyze, filter, sort, and save data into 'manipulated_swiggy_data.xlsx'.

## Automated Execution

To automate the project using Task Scheduler (Windows), follow the instructions in the [Automating with Task Scheduler](#automation-with-task-scheduler-windows) section.

## File Descriptions

- `swiggy.xlsx`: Source data file containing restaurant information.
- `scripts/`: Directory containing data processing and analysis modules.
- `main.py`: Main script to execute the project.
- `README.md`: This documentation file.

## Requirements

- Python 3.x
- Pandas
