---

# Olympic Analysis Dashboard

Welcome to the Olympic Analysis Dashboard! This project provides an interactive web application to explore Olympic data, visualizing medal tallies, overall statistics, country-wise analysis, and athlete performance metrics. 

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)


## Features
- **Medal Tally**: Analyze medal counts for countries over different years.
- **Overall Analysis**: Explore statistics such as the number of editions, cities, events, sports, athletes, and nations participating in the Olympics.
- **Country Wise Analysis**: View medal tallies per country over the years, including a heatmap of sports performance.
- **Athlete Wise Analysis**: Examine athlete performance based on age, height, weight, and gender participation trends.

## Technologies Used
- **Python**: Programming language for data analysis and application development.
- **Pandas**: Library for data manipulation and analysis.
- **Streamlit**: Framework for building web applications easily.
- **Plotly**: Library for creating interactive plots and visualizations.
- **Matplotlib & Seaborn**: Libraries for data visualization.
- **Scipy**: Library used for scientific and technical computing.

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/olympic-analysis.git
   cd olympic-analysis
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure you have the Olympic datasets (`events.csv` and `regions.csv`) in the `Olympic` folder.

## Usage
To run the application, execute the following command:

```bash
streamlit run app.py
```

Once the server is running, open your web browser and go to `http://localhost:8501` to view the dashboard.

## File Structure
```
/olympic-analysis
|-- app.py                     # Main application file
|-- requirements.txt           # Dependencies
|-- Olympic/                   # Directory containing datasets
|   |-- events.csv             # Olympic events data
|   |-- regions.csv            # Regions data for countries
|-- preprocessor.py            # Data preprocessing functions
|-- helper.py                  # Helper functions for data analysis
```

## Contributing
Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

---
