# Stock Prediction Project

This project aims to predict the next day's stock prices for a portfolio of companies and present the results in an enhanced HTML format. It consists of multiple Python scripts that fetch stock data, perform predictions, and remodel an HTML file for better visualization.

## Scripts

### 1. `stock_prediction.py`

This script fetches historical stock data and uses machine learning models to predict the next day's stock prices. It generates an HTML file (`Next_Day_Stock_Predictions.html`) and a JSON file (`stock_data.json`) containing the prediction results.

#### How to Run

```bash
python3 stock_prediction.py
```

### 2. `html_remodeling.py`

This script takes the HTML file generated by `stock_prediction.py` and remodels it into a more visually appealing format. It uses the BeautifulSoup library to parse and modify the HTML. The remodeled HTML is saved as `Enhanced_Next_Day_Stock_Predictions.html`.

#### How to Run

```bash
python3 html_remodeling.py
```

### 3. `automate_all.py`

This script automates the entire process by running `stock_prediction.py` and `html_remodeling.py` sequentially. After running both scripts, it opens the enhanced HTML file in the default web browser.

#### How to Run

```bash
python3 automate_all.py
```

## Requirements

- Python 3.x
- Required Python libraries: yfinance, pandas, numpy, matplotlib, statsmodels, sklearn, bs4

## Author

This project was created as a collaborative effort with the user.
