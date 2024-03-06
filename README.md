# *Customer Lifetime Value* Predictive Model 

This project was created to fulfill the requirements of my 3rd capstone project at Purwadhika (Data science & machine learning course). This project aims to use machine learning to facilitate insurance companies to make informed decisions by accurately predicting the lifetime value of their customers. By identifying high-value customers, companies can tailor their marketing and retention strategies to optimize budget allocation and enhance customer satisfaction.

## Overview
Many companies face the challenge of misallocating their marketing and retention efforts—spending too much on low-value customers and too little on high-value ones. Our goal is to develop a predictive model that accurately forecasts the CLV of customers, enabling targeted strategies and efficient budget allocation towards high-value customers.

## Dataset
| **Columns** | **Type** | **Description** |
| --- | --- | --- |
| Vehicle Class	 | Object | Type of vehicle insured. | 
| Coverage | Object | Level of insurance coverage the policy offers. | 
| Renew Offer Type	 | Object | Type of renewal offer, may reflect different terms, prices, or benefits designed to retain customers. | 
| EmploymentStatus | Object | Employment status of the policyholder. Might correlate with the policyholder's ability to pay premiums or their risk profile. | 
| Marital Status | Object | Indicates whether the policyholder is "Divorced", "Married", or "Single". | 
| Education | Object | Highest level of education attained by the policyholder. | 
| Number of Policies | Float | The number of policies held by a policyholder with the insurance company. Could indicate customer loyalty or the complexity of the customer's insurance needs.|
| Monthly Premium Auto | Float | Represents the monthly premium amount for the auto insurance policy |
| Total Claim Amount | Float | The total amount claimed by the policyholder. |
| Income | Float | The income of the policyholder. |
| Customer Lifetime Value | Float | Represents the total value a customer is expected to bring to the company over the lifetime of their relationship. Used to identify high-value customers for targeted marketing and personalized services. |

## Workflow

1. Data & Domain Understanding
2. Data Preparation:
    - Normality Check
    - Correlation Check (Feature Selection)
    - Outliers Check
    - Preprocessing: Encoding & Scaling
3. Create Pipeline
4. Model Benchmarking
5. Model Tuning (Select 2 best models for tuning)
6. Final Model Selection
7. User Interface/App Creation (For instant simulations by inputting features manually)

## Conclusion
1. The most suitable model in this scenario is RandomForest with default parameters, achieving a MAPE of 4.15% on cross-validation benchmarking.
2. The model is trained on a dataset that excludes CLV (Customer Lifetime Value) outliers, as this significantly improves performance. Consequently, the model's predictions are most reliable for customer CLV values ranging from 0 to 16,500.
3. It is advisable to develop another model using training data that includes the CLV outliers. This approach offers users options:
    - The model trained without CLV outliers demonstrates a lower MAPE (Mean Absolute Percentage Error), indicating higher accuracy but within a limited CLV range.
    - The model trained with CLV outliers might offer lower overall accuracy but is hypothesized to produce better predictions for higher CLV ranges.
4. A user interface has been developed based on this model, allowing users to make quick predictions by manually inputting the features.


## How to use the interface app (capstone3interface.py)
Our project includes an interactive user interface, built with Streamlit, that allows you to easily input features and receive instant CLV predictions. Below are the steps on how to run the interface app on your local machine. Before running the app, ensure you have 'Streamlit' instaled.

`pip install streamlit`

#### *Running The App*
1. Download the Project
First, download or clone this repository to your local machine. Suppose you've saved it to a folder named "MyProjects" on your desktop.

2. Navigate to the Project Directory
Open your terminal or command prompt, and change the directory to where the interface app file is located. If you followed the example above, you would do this by entering:
`cd Desktop/MyProjects/CLV_Prediction`
This command changes your current directory to where the app file is located.

3. Run the Streamlit App
With Streamlit installed and your terminal navigated to the project's directory, you can now run the app by entering:
`streamlit run capstone3interface.py`
This command tells Streamlit to run the capstone3interface.py file, which is your interactive CLV prediction interface.

#### *Using The App*
Once the app is running, your default web browser should automatically open a new tab displaying the interface. If it doesn't, Streamlit will provide a local URL in the terminal, which you can manually copy and paste into your browser.

In the interface, you'll find input fields corresponding to the features described in the dataset section of this README. Fill in the fields with the data for which you'd like to predict the Customer Lifetime Value, and submit your input. The prediction will be displayed on the screen. Should you wish to make another prediction, simply adjust the input values and submit again.
