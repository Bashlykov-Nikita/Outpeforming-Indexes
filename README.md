# Outperforming the Indexes🚀
### Description:
The purpose of this site is to provide a clear ***visualization*** of investment portfolio ***characteristics*** and to allow for ***comparisons*** between different portfolios and the benchmark index they aimed to surpass.  
📊This site calculates the following metrics:
- Annual Return
- Annual Volatility
- Skewness
- Kurtosis
- Value at Risk
- Conditional Value at Risk
- Sharpe Ratio
- Maximum Drawdown

📈In addition to the metrics, the following graphs are displayed:  
Upon selecting a specific portfolio:
- Growth Plot
- Top Weights
- Probability Distribution
 
The comparison page (Outperform!) shows:  
- Сomparative Growth Plot
- Risk-Return Profiles
- Histograms: Sharpe Ratio, VaR, CVaR, Max Drawdown
- Complete feature comparison table

### Features:
1. **Powered by Streamlit**: A user-friendly interface for seamless exploration.
2. **In-depth Analysis**: Calculates key metrics and visualizes them through informative plots.
3. **Comprehensive Coverage**: Analyzes 168 portfolios, providing insights into a diverse range of investment strategies.
4. **Actionable Insights**: Offers detailed explanations of metrics, portfolio strategies, and potential improvement areas.

### How it Works:
- ```data.py```: Defines constants used throughout the project (stored in dictionaries).
- ```get.py```: Provides functions to retrieve data using constants defined in ```data.py```.
- ```calc.py```: Contains functions to calculate portfolio metrics.
- ```utils.py```: Houses utility functions used across the entire project.
- ```show.py```: Contains functions responsible for displaying results on the website.
- ```texts.py```: Stores all text explanations used on the website.
- ```Outperforming.py```: The main script that serves as the website's homepage.
- ```Data_Showcase.py```: A page dedicated to displaying the data used in the analysis.

### Previous Steps:
Learn about data collection process and portfolio creation techniques in the previous projects:  
[Get Historical Index Profits with Python!](https://github.com/Bashlykov-Nikita/Companies-Returns) 🚀  
[Building and Backtesting Investment Portfolios](https://github.com/Bashlykov-Nikita/Creating-Portfolio)🚀
