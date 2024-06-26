This project is a Python script utilizing Selenium and Pandas to automate the extraction and analysis of spot market price data from the MCX India website. Let's break down the functionality and flow:

### Selenium Automation Script (IMARC Class)
1. **Initialization (`__init__` method):**
   - Initializes a headless Chrome WebDriver using Selenium.
   - Navigates to the MCX India spot market price page.
   - Clicks on the "Archive" button to access historical data.

2. **`send_data` method:**
   - Clicks on the dropdown to select a specific commodity (gold in this case).
   - Selects a session option (likely different trading sessions).
   - Prepares to input the start date.

3. **`send_start_date` method:**
   - Enters the start date into the date picker after enabling it using JavaScript.
   - Clicks on a specific date in the date picker modal.

4. **`send_end_date` method:**
   - Enters the end date into the date picker similarly to the start date.
   - Clicks on a specific date in the date picker modal.
   - Clicks the "Show" button to fetch data for the specified date range.

5. **`get_table_Data` method:**
   - Clicks on a button to export data to a CSV file.

### Pandas Operations (Excel_read, Total_rows_data, Highest_price, new_excel Functions)
1. **`Excel_read` function:**
   - Reads the CSV file (`SpotMarket_20240623192407.csv`) into a Pandas DataFrame (`data_Fram`).

2. **`Total_rows_data` function:**
   - Calculates and prints the total number of rows in the DataFrame.

3. **`Highest_price` function:**
   - Identifies the date with the highest spot price (`Price(Rs.)` column) in the DataFrame and prints it.

4. **`new_excel` function:**
   - Creates a new Excel file (`Final.xlsx`) and writes the DataFrame (`data_Fram`) into a sheet named 'Raw Data'.

### Overall Project Description
- **Purpose:** Automate the retrieval and basic analysis of historical spot market price data for a specific commodity (gold).
- **Tools Used:**
  - **Selenium:** For web scraping and automation of web interactions (navigation, button clicks, data entry).
  - **Pandas:** For data manipulation and analysis (reading CSV, calculating statistics, exporting to Excel).

This project demonstrates the automation of web data extraction and subsequent analysis using Python, Selenium, and Pandas, providing a structured approach to handling web-based data retrieval tasks.
