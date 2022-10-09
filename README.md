# CarPricePrediction

## Project Description
This project is designed to predict the price of a car given certain attributes/features.  I have always noticed that the car price has fluctuated over the years and wanted to see if it was possible to create a  ML solution for predicting the price of a car and understand what factors attribute to the cost of a car more than other factors.  I started off by scraping Car Data from the Carguru Website.  From there, I followed the preliminary Data Exploration, Feature Engineering, and Model Preparation Steps of the Data Science Life Cycle using the **Python NumPy, Pandas, Matplotlib, and Scikit-Learn Libraries**.  Then, I developed a Machine Learning Model using TensorFlow in Python on AWS Sagemaker.  Furthermore, I deployed the ML Model to **AWS API Gateway** using **AWS Lambda** to create a **Serverless REST API**.


## Installation
=> Need to pip install beautifulsoup
=> need to pip install requests
=> need to install selenium
=> need to install Chrome Selenium Webdriver and add to executable path


## Steps to Run Project
- Run the AWS Sagemaker Notebook called Car_Sagemaker_Model.ipynb on AWS Sagemaker with the conda_tensorflow2_p38 kernel
- Go to AWS API Lambda and add the lambda_handler.py code and Deploy the code
- Go to AWS API Gateway and Create the Necessary Resource and Methods
- Deploy the API Gateway API Endpoint
- Run the test_script.py file

## Resources
- https://www.youtube.com/watch?v=stD47vPDadI 
- https://awstip.com/steps-to-deploy-a-pre-trained-tensorflow-model-using-amazon-sagemaker-hosting-87719e91d8ad
- https://www.youtube.com/watch?v=Lx16T9cl5ng
