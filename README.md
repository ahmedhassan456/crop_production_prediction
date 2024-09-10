
# Crop Production Prediction using XGBRegressor

## Project Overview

This project aims to predict crop production in India using the **XGBRegressor** model. The dataset used encompasses a wide array of variables related to crop production across different states and regions of India, spanning multiple years. The goal is to build an accurate predictive model to forecast crop production, offering insights for stakeholders in the agri-food sector.

### Dataset Description

The dataset contains over 246,000 records, capturing a variety of metrics related to crop production. Key columns in the dataset include:

- **State_Name**: Name of the state where the crop data was recorded.
- **District_Name**: District within the state where the crop data was collected.
- **Crop_Year**: Year in which the crop was harvested.
- **Season**: Agricultural season (e.g., Kharif, Rabi) during which the crop was grown.
- **Crop**: Type of crop cultivated.
- **Area**: Total land area used for cultivating the crop.
- **Production**: Total quantity of the crop produced from the specified area.

### Objectives

- **Predictive Modeling**: Forecast crop production using machine learning techniques.
- **Insight Extraction**: Uncover key indicators influencing crop production.
- **Trend Analysis**: Analyze longitudinal data to understand crop production trends over time.

### Machine Learning Model

We used **XGBRegressor** from the XGBoost library to build the predictive model. The model was trained to predict the `Production` based on features such as the `State_Name`, `District_Name`, `Crop_Year`, `Season`, `Crop`, and `Area`.

### Deployment

The model has been deployed using **FastAPI** to provide an easy-to-use RESTful API for crop production prediction. The API accepts input data in JSON format and returns the predicted crop production value.

### Features

- **State_Name**: The name of the state where the crop was grown.
- **District_Name**: The district within the state where the data was recorded.
- **Crop_Year**: The year in which the crop was harvested.
- **Season**: The agricultural season during which the crop was grown.
- **Crop**: Type of crop cultivated.
- **Area**: Total land area used for the crop.
- **Production**: Predicted total crop production.

### Dependencies

- Python 3.x
- XGBoost
- FastAPI
- Pandas
- Scikit-learn
- Uvicorn (for running the FastAPI server)


### Acknowledgements

This project is based on publicly available crop production data and aims to assist stakeholders in the agricultural sector by providing predictive insights.
