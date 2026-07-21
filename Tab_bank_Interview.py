# 2 data sources
# one table from each source
# minor cleaning - nulls, outside of an acceptable range (remove outliers)
# inserting data into single table @ data destination; ETL or ELT process
# data_source_a, data_source_b, data_destination

import pandas

def call_datasource(data_source):
    
    df = data_source_call(data_source).df()

    return(df)

df_a = call_datasource(data_source_a)
df_b = call_datasource(data_source_b)

def data_clearning(df):

    cleaned_df = df.copy()

    cleaned_df = cleaned_df.dropna()

    cleaned_df = cleaned_df[cleaned_df['revenue'] > 0]

    return(cleaned_df)

cleaned_a = data_clearning(df_a)
cleaned_b = data_clearning(df_b)

merged_cleaned_df = cleaned_a.merge(cleaned_b, on='customer_id', how='left')

# check to make sure we don't have CRAZY number of rows added

merged_cleaned_df = merged_cleaned_df.rename(columns={'old_column':'new_column'})

merged_cleaned_df['loss'] = merged_cleaned_df['revenue'] - merged_cleaned_df['cost']

def pass_to_data_table(df):
    data_destination(df)

    try:
        con.execute(""" CREATE TABLE IF NOT EXISTS transformed_customer """)
        RAISEERROR("")
    catch:

    return()
