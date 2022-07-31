<div style="font-size: 40px">

|  Submitted By   | Kashif Raza  |
|--------|--------------|

</div >

# Exploratory Data Analysis on Open Food Facts Data
## About the Dataset
- Open Food Facts is a non-profit association of volunteers.
5000+ contributors like you have added 600 000+ products from 150 countries using our Android, iPhone or Windows Phone app or their camera to scan barcodes and upload pictures of products and their labels.
## Important steps performed in the analysis
## 1. Data Shape
Shape of the original datset is:
```
food.shape
```
(356027,163)
- Total number of observations/rows: $356027$
- Total number of columns: $163$

## 2. Data Structure
The data is structured in the following way:
```
food.info()
```
- Data has the range index of : 356027 entries, 0 to 356026
- The columns are:163 starts from `code` to `water-hardness_100g`
- Total memory usage is: 442.8+ MB
- From $163$ columns: $107$ columns has the data type of `float64` and the rest $56$ has the data type of `object`

## 3. Finding Missing Data
To find the missing data, we can use the following code:
```
nan_per=food.isnull().sum().sort_values(ascending=False)/food.shape[0]*100
```
- Plotting the columns with the highest percentage of missing data:
```
plt.figure(dpi=600)
nan_per.plot(kind='bar', title='Percentage of missing values per feature', figsize=(15,5),
             color='red', fontsize=5)  
```

![](Pictures/food_eda/nan1.png)

- Plotting the Nan percentage with features columns:
```
plt.figure(figsize=(10,5))
plt.figure(dpi=600)
sns.distplot(nan_per, bins=100, kde=False)
plt.xlabel("NaN percentage")
plt.ylabel("Number of columns")
plt.title("Percentage of nans per feature column")
```
![](Pictures/food_eda/nan2.png)

### **Key Takeaways**
1. A large percentage of nana data is present in the columns with the highest percentage of missing data. So not all the information seems to be useful. 
2. Most of the featured columns contains 100% nan values
3. There is a group of columns that have the 20% of nan values.
4. Nan values feature is not useful for the analysis.
5. Columns having Nan values can be dropped.

### **Useless features columns**
Useless features columns are:
```
useless_features=nan_per[nan_per==100].index
print('Useless features:', useless_features)
```
![](Pictures/food_eda/useless_features.png)

### **Length of Useless features**
Length of the useless features:
```
print('Length of useless features:', len(useless_features))
```
- Length of useless features: 16

### **Drop the useless features**
Drop the useless features:
```
food.drop(useless_features, axis=1, inplace=True)
print('Shape of the dataset after dropping the useless features:', food.shape)
```
Shape of the food dataset is: (356027, 147)

### **Features with zero nan values**
Features with zero nan values are:
```
zero_nan_features=nan_per[nan_per==0].index
print('Features with zero nan values:', zero_nan_features)
```
Zero NaN features: Index(['last_modified_datetime', 'last_modified_t'], dtype='object')

### **Splitting the data into NaN groups**
Splitting the data into NaN groups:
1. Columns with low Nan values: (0-20%)
2. Columns with medium NaN values: (20-50%)
3. Columns with High NaN values: (50-100%)
```
Low NaN features columns:
 sodium_100g             18.631
salt_100g                18.619
proteins_100g            17.377
energy_100g              17.038
brands_tags               8.165
brands                    8.159
product_name              4.919
countries                 0.077
countries_en              0.077
countries_tags            0.077
states_en                 0.015
states_tags               0.015
states                    0.015
url                       0.007
code                      0.007
created_datetime          0.003
created_t                 0.001
creator                   0.001
last_modified_datetime    0.000
last_modified_t           0.000
dtype: float64
```
Medium NaN features columns:
```
Medium NaN features: 
serving_size                              39.156
fiber_100g                                38.015
nutrition_grade_fr                        28.417
nutrition-score-fr_100g                   28.417
nutrition-score-uk_100g                   28.417
saturated-fat_100g                        25.898
sugars_100g                               21.583
carbohydrates_100g                        21.573
fat_100g                                  21.496
additives                                 20.280
additives_n                               20.268
ingredients_from_palm_oil_n               20.268
ingredients_that_may_be_from_palm_oil_n   20.268
ingredients_text                          20.261
dtype: float64
```
High NaN features columns has the 129 length.

### **Columns with fewest NaN values plot**
```
plt.figure(figsize=(20,5))
lows = sns.barplot(x=low_nan_features.index.values, y=low_nan_features.values, palette="rocket")
lows.set_xticklabels(low_nan_features.index.values,rotation=45)
plt.title("Features with fewest nan-values")
plt.ylabel("% of nans ")
```

![](Pictures/food_eda/low_nan.png)

- Plot shows that there are many features that occurs multiple times like
  - countries
  - coutries_tags
  - countries_en
  - additives
  - additives_n
### **Columns which have NaN values percentage between 20-50%**

```
plt.figure(figsize=(20,5))
lows = sns.barplot(x=med_nan_features.index.values, y=med_nan_features.values, palette="Spectral")
lows.set_xticklabels(med_nan_features.index.values,rotation=45)
plt.title("Features with medium percentage of nan-values")
plt.ylabel("% of nans ")
```
![](Pictures/food_eda/med_nan.png)

### **Columns which have NaN values percentage >50%**
```
plt.figure(figsize=(15,30))
high = sns.barplot(y=high_nan_features.index.values, x=high_nan_features.values, palette="Blues")
plt.title("Features with most nan-values")
plt.ylabel("% of nans ")
```
![](Pictures/food_eda/high_nan.png)

### Dropping the columns with high NaN values
- Dropping the columns that have high NaN values:
```
for i in high_nan_features.index:
    if i in food.columns:
        food.drop(i, axis=1, inplace=True)
print('Shape of the dataset after dropping the high NaN features:', food.shape)
```
(356027, 34)
- Now we have 34 features.

### **Drop the NaN values from the data**
- Drop the nan values from the data and then print the shape of data
```
food.dropna(inplace=True)
print('Shape of the food dataset after dropping NaN values is:', food.shape)
```
Shape of the food dataset after dropping NaN values is: (157157, 34)
## Data Structure of cleaned data
- New cleaned data has the total entries of 157157.
- Total number of features are: 34
- 14 features has the data type of float64.
- 20 features has the data type of object.
- Total memory usage of the cleaned data is: 42.0 MB

## Step 4: Type casting/Conversion the data type of data
- To convert the data type of specific column
```
food['serving_size'] = food['serving_size'].astype(str)
food['product_name'] = food['product_name'].astype(str)
```
- Now we have the data type of serving_size as string and product_name as string also.

## Step5: Summary Statistics of the data
- Summary Statistics of the data:
```
food.describe()
```
![](Pictures/food_eda/summary_statistics.png)
## Step 6: Value Counts
- Value Counts of the data:
```
food.product_name.value_counts()
```
- Ice Cream is the most popular product name. It occurs $405$ forllowed by Potato Chips occurs $276$ times.
- Most products occurs are:

![](Pictures/food_eda/most_occ_prod.png)
- Least occurs products are:
  
![](Pictures/food_eda/least_occ_prod.png)

## Step-7: Deal with Duplicates
- Dropping the duplicates
```
food.drop_duplicates(inplace=True)
print('Shape of Dataset after dropping the duplicates', food.shape)
```
Shape of Dataset after dropping the duplicates (157157, 34)

## Step-8: Check the Normality of Data
- To check the distribution of data whether it is normal or not.
- Distribution of data of `nutrition-score-fr_100g` column
![](Pictures/food_eda/dist_plot.png)

## Step-9: Correlation of Dataset
- Correlation plot tells the relation between the column. Withe the increase or decrease in one quantity how much it affect the 2nd quantity.
![](Pictures/food_eda/corr.png)


