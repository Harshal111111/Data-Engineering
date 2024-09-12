import pandas as pd
def filter_dataframe(df, column_name, filter_value):

    return df[df[column_name] == filter_value]
df = pd.read_csv('../QUESTIONS/students.csv')

# 1. How many students are from 'San Francisco'?
san_francisco_students = filter_dataframe(df, 'City', 'San Francisco')
san_francisco_count = len(san_francisco_students)
print(f"Number of students from San Francisco: {san_francisco_count}")

# 2. What is the average age of students from 'Chicago'?
chicago_students = filter_dataframe(df, 'City', 'Chicago')
average_age_chicago = chicago_students['Age'].mean()
print(f"Average age of students from Chicago: {average_age_chicago}")

# 3. Create a new DataFrame with students who are 30 years old or older
students_30_and_older = df[df['Age'] >= 30]
students_30_and_older_count = len(students_30_and_older)
print(f"Number of students 30 years old or older: {students_30_and_older_count}")

# # Save the filtered data for students 30 and older to a new CSV (optional)
# students_30_and_older.to_csv('students_30_and_older.csv', index=False)

