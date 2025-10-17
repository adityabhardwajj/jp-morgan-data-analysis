# Natural Gas Price Forecasting Project

This project aims to analyze and forecast natural gas prices using historical data. It includes data loading, analysis, visualization, and modeling components.

## Project Structure

```
nat_gas_forecast
├── src
│   ├── data
│   │   └── __init__.py
│   ├── analysis
│   │   ├── __init__.py
│   │   └── models.py
│   ├── visualization
│   │   ├── __init__.py
│   │   └── plots.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── notebooks
│   └── natural_gas_analysis.ipynb
├── requirements.txt
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/adityabhardwajj/nat_gas_forecast.git
cd nat_gas_forecast
pip install -r requirements.txt
```

## Usage

1. **Data Loading**: Use the functions in `src/data/__init__.py` to load historical natural gas price data.
2. **Analysis**: Perform data analysis using the functions in `src/analysis/models.py`.
3. **Visualization**: Create visualizations with the plotting functions in `src/visualization/plots.py`.
4. **Jupyter Notebook**: Explore the analysis interactively in the `notebooks/natural_gas_analysis.ipynb`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.