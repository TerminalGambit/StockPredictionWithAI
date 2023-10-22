import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import yfinance as yf
import logging
from datetime import datetime
import json

logging.basicConfig(level=logging.INFO)


def fetch_data(company, start, end):
    try:
        data = yf.download(company, start=start, end=end)['Close']
        if data.empty:
            logging.error(
                f'Data is empty for {company}. Check the stock symbol or date range.')
            return None
        return data
    except Exception as e:
        logging.error(f'An error occurred: {e}')
        return None


def feature_engineering(data):
    data = pd.DataFrame(data)
    data['lag_1'] = data['Close'].shift(1)
    data['lag_2'] = data['Close'].shift(2)
    data['lag_3'] = data['Close'].shift(3)
    data.dropna(inplace=True)
    return data


def generate_html(predictions):
    with open('Next_Day_Stock_Predictions.html', 'w') as f:
        f.write('<html><body><h1>Next Day Stock Predictions</h1><table border=1>')
        f.write(
            '<tr><th>Stock</th><th>Next Day Price</th><th>Last Day Price</th><th>Percentage Change</th></tr>')
        for comp in predictions.keys():
            color = 'green' if predictions[comp]['Percentage Change'] >= 0 else 'red'
            f.write(
                f'<tr><td>{comp}</td><td style="color: {color};">{predictions[comp]["Next Day Price"]}</td><td>{predictions[comp]["Last Day Price"]}</td><td style="color: {color};">{predictions[comp]["Percentage Change"]}%</td></tr>')
        f.write('</table></body></html>')


def main():
    portfolio = ['NVDA', 'GOOGL', 'TSLA', 'GCT', 'GM', 'AI', 'SMCI', 'NIO']
    start = '2023-01-01'
    end = datetime.now().strftime('%Y-%m-%d')
    predictions = {}

    for company in portfolio:
        data = fetch_data(company, start, end)
        if data is None:
            continue

        data = feature_engineering(data)

        X = data[['lag_1', 'lag_2', 'lag_3']]
        y = data['Close']

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        next_day_features = np.array([X.iloc[-1].values])
        next_day_price = model.predict(next_day_features)[0]
        last_day_price = data['Close'].iloc[-1]
        percentage_change = (
            (next_day_price - last_day_price) / last_day_price) * 100

        predictions[company] = {'Next Day Price': next_day_price,
                                'Last Day Price': last_day_price, 'Percentage Change': percentage_change}

    generate_html(predictions)
    logging.info('HTML file generated as Next_Day_Stock_Predictions.html')

    with open('stock_data.json', 'w') as f:
        json.dump(predictions, f)


if __name__ == '__main__':
    main()
