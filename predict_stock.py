import subprocess
import webbrowser
import os


def main():
    # Execute the stock prediction script
    stock_prediction_script = 'stock_prediction.py'
    if not os.path.exists(stock_prediction_script):
        print(f'Error: {stock_prediction_script} does not exist.')
        return
    subprocess.run(['python3', stock_prediction_script])

    # Execute the HTML remodeling script
    html_remodeling_script = 'html_remodeling.py'
    if not os.path.exists(html_remodeling_script):
        print(f'Error: {html_remodeling_script} does not exist.')
        return
    subprocess.run(['python3', html_remodeling_script])

    # Open the enhanced HTML website
    enhanced_html_file = 'Enhanced_Next_Day_Stock_Predictions.html'
    if not os.path.exists(enhanced_html_file):
        print(f'Error: {enhanced_html_file} does not exist.')
        return
    webbrowser.open(f'file://{os.path.abspath(enhanced_html_file)}')


if __name__ == '__main__':
    main()
