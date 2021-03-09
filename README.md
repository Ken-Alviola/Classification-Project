# Classification-Project

### Description and Goals
- Project examining driverss of customer churn using the telco_churn database from Codeup
- The goals are to find drivers of churn and to accurately predict churn using a machine learning model

### Data Dictionary
---
| Column | Definition | Data Type |
| ----- | ----- | ----- |
|customer_id| customer unique identifier | object |
|senior_citizen| 1 if customer is a senior| int|
|tenure| number of months the customer has remained| int|
|monthly_charges| amount in $ the monthly service charge| float|
|total_charges | total $ amount the customer has been charged| float|
|gender_Male| 1 if customer is male| int|
|partner| 1 if customer is married| int|
|dependents| 1 if customer has dependents| int|
|phone_service| 1 if customer has phone service| int|
|paperless_billing| 1 if customer requested paperless billing| int|
|online_security| 1 if customer opted for online security|int|
|online_backup| 1 if customer opted for online backup|int|
|device_protection| 1 if customer opted for device protection| int|
|tech_support| 1 if customer subscribes to tech support| int|
|streaming_tv| 1 if customer has streaming tv| int|
|streaming_movies| 1 if customer included streaming movies| int|
|multiple_lines| 1 if customer has more than 1 phone line| int|
|Month_to_month| 1 if customer is month-to-month contract type| int|
|One_year_contract| 1 if customer has a 1 year contract| int|
|Two_year_contract| 1 if customer has a 2 year contract| int|
|DSL| 1 if customer subscribes to DSL service| int|
|Fiber_optic| 1 if customer has fiber optic internet| int|
|No_internet| 1 if customer does not have internet service| int|
|Bank_transfer_(automatic)| 1 if customer pays through auto bank xfer|int|
|Credit_card_(automatic)|1 if customer pays with credit card|int|
|Electronic_check| 1 if customer pays with e-check|int|
|Mailed_check| 1 if customer mails payment|int|


| Target | Definition | Data Type |
| ----- | ----- | ----- |
|churn|1 if customer has left service| int |

### Hypotheses
**1. Are the monthly charges between churned customers significantly higher from unchurned customers?**
- null_hypothesis = "The means of monthly_charges are the same for churn vs. no churn"
- alternative_hypothesis = "Churned customers had higher monthly_charges than unchurned"

**2. Is Churn independent of the Fiber Optic service?**
- null_hypothesis = "Churn is independent of the Fiber Optic service"
- alternative_hypothesis = "Churn depends on Fiber Optic service subscription"

**3. Is there a correlation between monthly charges and tenure for churned fiber optic customers?**
- null_hypothesis = "There is no correlation between monthly charges and tenure for churned fiber optic customers"
- alternative_hypothesis = "There is a positive correlation between monthly charges and tenure for churned fiber optic customers"

### Project Plan
1. Acquire telco data from telco_churn database using correct joins
2. Prepare data by removing unnecessary/redundant columns, dealing with nulls, and encoding variables for use with ML models
3. Explore data using functions in explore.py
4. Create ML models and choose best performing for test data
5. Create churn predictions and probabilities for each customer and store in .csv file

### How to re-create
- All necessary files are in this repository so the best method would be to git clone
- Run Classification_Project_Telco.ipynb
- Adjust exploration and modeling to your liking
