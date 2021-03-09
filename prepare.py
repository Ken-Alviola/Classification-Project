import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def clean_telco(df):
    '''
    clean_telco will take one argument df, a pandas dataframe, anticipated to be the telco_churn dataset
    and will change the total_charges columns to float and will encode and remove specified columns

    return: a single pandas dataframe with the above operations performed
    '''
    #dealing with blank values in total charges column and changing to float
    df.total_charges.replace(to_replace=' ',value=np.nan,inplace=True)
    df['total_charges'] = df.total_charges.astype(float).fillna(df.monthly_charges)
        
    #dropping redundant columns from sql joins
    df.drop(columns=['payment_type_id', 'internet_service_type_id',
                     'contract_type_id'], inplace=True)
    #encoding str columns
    dummy_df = pd.get_dummies(df[['gender',
                                  'partner',
                                  'dependents',
                                  'phone_service',
                                  'paperless_billing',
                                  'churn'
                                  ]], drop_first=True)
    
    #encoding other string columns but not dropping first class
    dummy_df2 = pd.get_dummies(df[['online_security',
                                   'online_backup',
                                   'device_protection',
                                   'tech_support',
                                   'streaming_tv',
                                   'streaming_movies',
                                   'multiple_lines',
                                   'contract_type',
                                   'internet_service_type',
                                   'payment_type']])
    #dropping extras
    dummy_df2.drop(columns=['online_security_No internet service',
                            'online_backup_No internet service',
                            'device_protection_No internet service',
                            'tech_support_No internet service',
                            'streaming_tv_No internet service',
                            'streaming_movies_No internet service',
                            'multiple_lines_No phone service',
                           
                            ], inplace=True)
    #joining new DFs
    encode_df = pd.concat([df, dummy_df, dummy_df2], axis=1)
    #dropping original columns after encoding
    encode_df.drop(columns=['gender',
                            'partner',
                            'dependents',
                            'phone_service',
                            'multiple_lines',
                            'online_security',
                            'online_backup',
                            'device_protection',
                            'tech_support',
                            'streaming_tv',
                            'streaming_movies',
                            'paperless_billing',
                            'churn',
                            'contract_type',
                            'internet_service_type',
                            'payment_type',
                            'online_security_No',
                            'online_backup_No',
                            'device_protection_No',
                            'tech_support_No',
                            'streaming_tv_No',
                            'streaming_movies_No',
                            'multiple_lines_No',                            
                            ], inplace=True)
    #renaming encoded columns
    encode_df.columns = ['customer_id',
                 'senior_citizen',
                 'tenure',
                 'monthly_charges',
                 'total_charges',
                 'gender_Male',
                 'partner',
                 'dependents',
                 'phone_service',
                 'paperless_billing',
                 'churn',
                 'online_security',
                 'online_backup',
                 'device_protection',
                 'tech_support',
                 'streaming_tv',
                 'streaming_movies',
                 'multiple_lines',
                 'Month_to_month',
                 'One_year_contract',
                 'Two_year_contract',
                 'DSL',
                 'Fiber_optic',
                 'No_internet',
                 'Bank_transfer_(automatic)',
                 'Credit_card_(automatic)',
                 'Electronic_check',
                 'Mailed_check']
    
    return encode_df

def generic_split(df, stratify_by=None):
    """
    Crude train, validate, test split
    To stratify, send in a column name
    """
    
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.2, random_state=123)
        train, validate = train_test_split(df, test_size=.3, random_state=123)
    else:
        train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
        train, validate = train_test_split(train_validate, test_size=.3, random_state=123, stratify=train_validate[stratify_by])
    
    return train, validate, test

def get_metrics(model, X, y):
    '''
    get_metrics_bin will take in a sklearn classifier model, an X and a y variable and utilize
    the model to make a prediction and then gather accuracy, class report evaluations

    return:  a classification report as a pandas DataFrame
    '''
    y_pred = model.predict(X)
    accuracy = model.score(X, y)
    conf = confusion_matrix(y, y_pred)
    print('confusion matrix: \n', conf)
    print()
    class_report = pd.DataFrame(classification_report(y, y_pred, output_dict=True)).T
    tpr = conf[1][1] / conf[1].sum()
    fpr = conf[0][1] / conf[0].sum()
    tnr = conf[0][0] / conf[0].sum()
    fnr = conf[1][0] / conf[1].sum()
    print(f'''
    The accuracy for our model is {accuracy:.4}
    The True Positive Rate is {tpr:.3}, The False Positive Rate is {fpr:.3},
    The True Negative Rate is {tnr:.3}, and the False Negative Rate is {fnr:.3}
    ''')
    return class_report