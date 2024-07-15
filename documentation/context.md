# Diabetes
Diabetes is the name of the medical condition when someone has too much sugar on blood along most of the time.

## Disclaimer
This page was written as a part of the research in order to understand better the business problem of Machine Learning project. This document MUST NOT be read as a place to get medical advices. If you want to have reliable information about this medical codition consult your trusted doctor.

## Frequently questions
### What types of diabetes exist?
- T1D (Type 1 Diabetes): Is an autoimune disease which makes the imunologic system attacks the beta cells of pancreas by mistake. We still don't know why that happens but it makes our body fail in the insulin production.
- T2D (Type 2 Diabetes): This type of diabetes exists when the body can generate insulin but the cells can't use it properly. This condition is what we call as "Resistance to insulin".
- Gestational: It's the high blood sugar disorder that is developed during pregnancy, most of the times it ends after the pregnancy (Some people can developt T2D after).

### What is insulin?
Insulin is the hormone responsible to manage the gate between the blood flow and the cells, in other words is the responsible of letting sugar enter in cells.

### What metric we use to measure blood sugar?
Blood sugar (or Blood Glucose in some texts) can be measured by many metrics along the world, all of them are a proportion between how much sugar exists in a given volume of blood.
The most commonly used metric is mg/dl.

## Target Blood Glucose Range
Glycemia (concentration of sugar on blood) can change a lot along the day, because of that the medical comunnity usually uses what we call as "Target Blood Glucose Range".
The Target Blood Glucose Range is a range of blood sugar values that is recommended to have in order to avoid health disorders.

### How a Target Blood Glucose Range works?
![Target Blood Glucose Range Example](/src/img/target_blood_glucose_range.png)
The values on the target blood glucose range can change according to personal health conditions (like age, other conditions) because glycemia is something multifactorial.
In the example above the reference value is 100 mg/dl but values between 70 and 180 mg/dl are also in the acceptable range.
It's okay to have highs and lows along the day, because of that is recommended to check the glycemia 4 or 6 times in the day paying attention if at least 50% or 60% of the checkings are in the acceptable range.
The farthest your glycemia is from the desirable range the highest the risks of having medical conditions like:
- Diabetic ketoacidosis (when the glycemia is high)
- Unconsciousness (when the glycemia is low)
- Seizures (when the glycemia is low)
- Death (when the glycemia is low)

### When is recommended to check the glycemia?
Most of times its recommended to check the glycemia in 4 situations:
- When wake up
- 15 minutes before an meal
- Before sleep
- When you fell symptons of change in the blood glucose

The recommended values of glycemia can vary a bit according to those different scenarios. For example:
- Before meals between 90 and 130 mg/dl
- 2 hours after meals under 180 mg/dl
- Overnight between 90 and 150 mg/dl

### References
[Michigan Medicine youtube channel](https://www.youtube.com/watch?v=Q6rLXPJ6j_I&list=PLNxqP-XbH8BIxZM9bknrNDe3eep5v4zSN).

## Summary of the columns
### Diabetes_012
It shows if the person has diabetes or not.
This feature will be our target.
Expected values:
- o = no diabetes
- 1 = prediabetes
- 2 = diabetes

### HighBP
Shows if the blood pressure is high or not.
Expected values:
- o = no high blood pressure
- 1 = high blood pressure

### HighChol
Shows if the cholesterol is high or not.
Expected values:
- o = no high cholesterol
- 1 = high cholesterol

### CholCheck
Shows if the patient checked the cholesterol in the last 5 years.
Expected values:
- o = Chlesterol not checked in the last 5 years
- 1 = Cholesterol checked in the last 5 yearscho

### BMI
Shows the body mass index, an medical index that has great correlation with some diseases like diabetes.

The formula of this index is:
BMI = Weight (in kilograms) / Height² (in meters)

This is an continuous feature, but we can have help of a range of values to take some conclusions:
- Below 18.5 = Underweight
- 18.5 - 24.9 = Normal weight
- 25.0 - 29.9 = Overweight
- 30.0 - 34.9 = Obesity class I
- 35.0 - 39.9 = Obesity class II
- Above 40 = Obesity class III

### Smoker
Shows if the patient have smoked at least 100 cigarettes [5 packs] in the entire life.
Expected values:
- o = No
- 1 = Yes

### Stroke
Shows if the patient already had a stroke.
Expected values:
- o = No
- 1 = Yes

### HeartDiseaseorAttack
Shows if the patient has Coronary heart disease (CHD) or myocardial infarction (MI).
Expected values:
- o = No
- 1 = Yes

### PhysActivity
Shows if the patient had physical activity in past 30 days (not including job).
Expected values:
- o = No
- 1 = Yes

### Fruits
Shows if the patient consume Fruit 1 or more times per day.
Expected values:
- o = No
- 1 = Yes

### Veggies
Shows if the patient consume Vegetables 1 or more times per day.
Expected values:
- o = No
- 1 = Yes

### HvyAlcoholConsump
Shows if the patient is a heavy drinker.
For this feature heavy drinker was considered when adult men having more than 14 drinks per week and adult women having more than 7 drinks per week.
Expected values:
- o = No
- 1 = Yes

### AnyHealthcare
Shows if the patient Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc.
Expected values:
- o = No
- 1 = Yes

### NoDocbcCost
Shows if the patient Was there a time in the past 12 months when he needed to see a doctor but could not because of cost.
Expected values:
- o = No
- 1 = Yes

### GenHlth
It's the auto perception of the patient about his own general health
Expected values:
- 1 = Excelent
- 2 = Very good
- 3 = Good
- 4 = Fair
- 5 = Poor

### MentHlth
It's the auto perception of the patient about his own mental health, which includes stress, depression, and problems with emotions. For how many days during the past 30 days was the patient mental health not good?
Expected values: Numbers between 1 and 30 to represent the last 30 days.

### PhysHlth
It's the auto perception of the patient about his own physical health, which includes physical illness and injury. For how many days during the past 30 days was the patient physical health not good?
Expected values: Numbers between 1 and 30 to represent the last 30 days.

### DiffWalk
Shows if the patient Have any kind of difficulty walking or climbing stairs.
Expected values:
- o = No
- 1 = Yes

### Sex
Expected values:
- o = female
- 1 = male

### Age
Expected values:
- 1  = 18 to 24
- 2  = 25 to 29
- 3  = 30 to 34
- 4  = 35 to 39
- 5  = 40 to 44
- 6  = 45 to 49
- 7  = 50 to 54
- 8  = 55 to 59
- 9  = 60 to 64
- 10 = 65 to 69
- 11 = 70 to 74
- 12 = 75 to 79
- 13 = 80 or more
- 14 = Don't know/Refused/Missing

### Education
Patient level of education.

Expected values:
- 1  = Never attended school or only kindergarten 
- 2  = Grades 1 through 8 (Elementary)
- 3  = Grades 9 through 11 (Some high school)
- 4  = Grade 12 or GED (High school graduate)
- 5  = College 1 year to 3 years (Some college or technical school)
- 6  = College 4 years or more (College graduate)

### Income
Patient scale of income.

Expected values:
- 1 = Less than $10,000
- 2 = Between $10,000 and $15,000
- 3 = Between $15,000 and $20,000
- 4 = Between $20,000 and $25,000
- 4 = Between $25,000 and $35,000
- 4 = Between $35,000 and $50,000
- 4 = Between $50,000 and $75,000
- 8 = $75,000 or more
- 77 = Don't know/Not sure
- 99 = Refused
- Blank = Not asked or missing