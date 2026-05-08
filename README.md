# Pakistan Electricity Demand Forecasting

## About This Project

Electricity demand in Pakistan varies based on time, weather conditions, and seasonal changes. The purpose of this project is to analyze historical electricity consumption data and build forecasting models to predict future energy usage.

In this project, I implemented and compared two time-series forecasting models: ARIMA and Prophet. The main objective is to evaluate which model performs better in capturing trends, seasonality, and fluctuations in electricity demand.

---

## Objectives

- Forecast future electricity consumption in Pakistan  
- Analyze patterns in historical energy usage data  
- Compare ARIMA and Prophet models  
- Study the impact of temperature on electricity demand  
- Evaluate model performance using error metrics  

---

## Dataset

The dataset contains historical electricity usage data with the following features:

- Date  
- Electricity consumption (kWh)  
- Temperature  
- City information  
- Humidity and other environmental factors (if available)  

This data helps understand how time and weather influence electricity demand.

---

## Models Used

### ARIMA
ARIMA is a classical statistical time-series model that uses past values to predict future values. It works well for linear and stationary data but may struggle with complex seasonal patterns.

### Prophet
Prophet is a forecasting model developed by Meta that automatically handles trend changes and seasonality. It performs well on real-world datasets with irregular patterns and missing data.

---

## Evaluation Metrics

The models are evaluated using:

- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  

These metrics measure how close the predicted values are to the actual values.

---

## Tools and Technologies

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Statsmodels (ARIMA)  
- Prophet  

---

## Results and Observations

- Electricity demand increases during high-temperature periods  
- Prophet captures seasonal patterns more effectively than ARIMA  
- ARIMA performs well on short-term linear trends but struggles with fluctuations  
- Real-world electricity data is highly influenced by external environmental factors  

---

## How to Run the Project

Clone the repository:

git clone https://github.com/yourusername/pakistan-electricity-forecasting.git

Install dependencies:

pip install -r requirements.txt

Run the project:

python main.py