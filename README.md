# Time-Table-Generator

This repository contains a Python script that generates a timetable for a school with SQL integration.

## Requirements

- Python 3.x
- MySQL

## Features

- Automatically generates a timetable for six days
- Uses MySQL to store the data
- Optimized code for better performance and readability

## Limitations

- Only generates timetable for six days and eight periods

## How to Use

1. Clone or download the file `ttg.py`.
2. Install the required packages by running `pip install pymysql`.
3. Run the script and input the required details such as the number of main subjects and extra subjects.
4. The generated timetable will be saved in the MySQL database.

### Step-by-Step Guide:

1. **Clone the Repository:**
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies:**
   ```sh
   pip install pymysql
   ```

3. **Setup MySQL:**
   Ensure you have MySQL installed and running. Create a database named `okp`:
   ```sql
   CREATE DATABASE okp;
   ```

4. **Run the Script:**
   ```sh
   python ttg.py
   ```
   - Enter the required details when prompted, such as the number of main subjects and extra subjects.

## Note

- Make sure you have MySQL installed on your system.
- This script is intended for educational purposes only and not for commercial use.

## Contribution

If you have any suggestions or found any bugs, feel free to create an issue or submit a pull request.

