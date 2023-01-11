import pandas as pd

sal = pd.read_csv('Salaries.csv')
# ** Use the .info() method to find out how many entries there are.**
print(sal.info())
# What is the average BasePay ?
print(sal['BasePay'].mean())
# ** What is the highest amount of OvertimePay in the dataset ? **
print(sal['OvertimePay'].max())
# ** What is the job title of JOSEPH DRISCOLL ?
print(sal[sal["EmployeeName"] == 'JOSEPH DRISCOLL']['JobTitle'])
# ** How much does JOSEPH DRISCOLL make (including benefits)? **
print(sal[sal["EmployeeName"] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
# ** What is the name of highest paid person (including benefits)?**
print("What is the name of highest paid person (including benefits)?")
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()])
print("Another Solution")
print(sal.loc[sal['TotalPayBenefits'].idxmax()])
# ** What is the name of lowest paid person (including benefits)? **
print(sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()])
print(sal.iloc[sal['TotalPayBenefits'].argmin()])
# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **
print(sal.groupby('Year').mean()['BasePay'])
# ** How many unique job titles are there? **
print(sal['JobTitle'].nunique())
print(len(sal['JobTitle'].unique()))
# ** What are the top 5 most common jobs? **
print(sal['JobTitle'].value_counts().head(5))
# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))


# ** How many people have the word Chief in their job title? (This is pretty tricky) **
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False


print(sum(sal['JobTitle'].apply(chief_string)))
print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **
sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['title_len', 'TotalPayBenefits']].corr())
