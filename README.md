# Automated_Data_Cleaning
A method to mostly clean data in python using automation.

This method requires identifying common data quality issues and then writing solutions that can handle various datasets consistently.

## Step 1: Running Basic Data Quality Checks

Before cleaning the data first we need to understand the quality of the data that is being worked with. This will give you a base understanding of the quality of the data and help to find te specific cleaning task that are needed for a particular dataset

This first step will then indentify cases of:
* Missing values within a column
* Duplicated Rows in the data set
* Some of the basic data characteristics.

## Step 2: Standardize Data Types

One of the common issues with raw data is inconsistent data types related to how the dat was collected in the first instance. A couple of examples of this would be dates being stored as strings, or numeric values included currency symbols.
In this step will then ensure that the fields have the right/expected data types within the dataset, this would include:
* Converting data from strings into datetime,  
* Convering numceric string into actual numbers, 
* Making sure that catagorical variables are proprly encoded.

This is done with the goal a reducing or stopping any errors in further analysis form the data types being incorrect.

## Step 3: Detect and Handle Outliers

Outliers within the data can skew the final analysis so these would need to be confirmed based on the rest of the data. This step does require an amount of domain knowlege in the dataset to make a decision on what if nay lines could be considered as outliers.
This step is one approach to doing a check using the interquartile range of the data. Interquartile range is used as it is a good method to confirm the expected spread of the data. to do this we would:

* Calculate Interquartile Range (IQR) for numeric columns
* Identify values beyond 1.5 * IQR from quartiles ( this can be change for datasets where more varience would be expected ) 
* Potentially apply capping to extreme values rather than removing them where this is appropriate. The other option would be to remove the data with the knowlege of the data being and outlier.

# Step 5: Validate the Results

After the cleaning process, we would then need to verify that the code has worked as expected. To do this we would:

* Confirm no remaining missing values
* Check for any remaining uplicates
* Validata data integrity and consistency
* Generate a cleaning report that can then be

# Wrap up
This type of data cleaning can help to save time with a new dataset and will also help to ensure consistency with data prep processes for each now dataset. This will handle common data quality issues and give a report on the data once completed. The cleaning repot should then be used to validate the results for the specific use case that is required.
