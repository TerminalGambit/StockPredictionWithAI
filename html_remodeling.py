from bs4 import BeautifulSoup
import os
import json


def remodel_html(input_file, output_file, stock_data):
    with open(input_file, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Update the title and header
    soup.h1.string = 'Enhanced Next Day Stock Predictions'

    # Style the table
    table = soup.find('table')
    table['style'] = 'border-collapse: collapse; width: 50%; margin: auto;'
    for row in table.find_all('tr'):
        for cell in row.find_all(['td', 'th']):
            cell['style'] = 'border: 1px solid black; padding: 8px; text-align: center;'

    # Color the cells and add previous day price
    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')
        stock = cells[0].text
        if stock_data.get(stock):
            color = 'green' if stock_data[stock]['Percentage Change'] >= 0 else 'red'
            cells[1]['style'] += f' background-color: {color};'
            cells[3]['style'] += f' background-color: {color};'
            cells[1].string = f'{float(cells[1].text):.3f}'
            cells[2].string = f'{float(stock_data[stock]["Last Day Price"]):.3f}'
            cells[3].string = f'{float(cells[3].text.replace("%", "")):.3f}%'

    # Save the remodeled HTML
    with open(output_file, 'w') as f:
        f.write(str(soup))


def main():
    input_file = 'Next_Day_Stock_Predictions.html'
    output_file = 'Enhanced_Next_Day_Stock_Predictions.html'
    stock_data_file = 'stock_data.json'

    if not os.path.exists(input_file) or not os.path.exists(stock_data_file):
        print(f'Error: {input_file} or {stock_data_file} does not exist.')
        return

    with open(stock_data_file, 'r') as f:
        stock_data = json.load(f)

    remodel_html(input_file, output_file, stock_data)
    print(f'Remodeled HTML saved as {output_file}')


if __name__ == '__main__':
    main()
