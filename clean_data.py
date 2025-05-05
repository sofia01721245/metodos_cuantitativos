import pandas as pd

df = pd.read_csv('dataClean.tsv', sep='\t', engine='python')


# Define a function to get the graduation year or -1 for each student
def compute_graduation_year(group):
    if group['student.isGraduated'].any():
        # Get the term.desc of the first row where the student graduated
        return group.loc[group['student.isGraduated'] == 1, 'term.desc'].iloc[0]
    else:
        return -1

# Create a Series with graduation year per student.id
graduation_years = df.groupby('student.id').apply(compute_graduation_year).rename('graduation_year')

# Merge this Series back into the original DataFrame on student.id
df = df.merge(graduation_years, on='student.id')

# Drop the columns you don't need (e.g., 'subject_LiFE.portfolioCategory')
df = df.drop(columns=['subject_LiFE.portfolioCategory'])
# Drop the specified column
df = df.drop(columns=['subject_LiFE.portfolioClassification'])

# Remove the student because she still has not graduated and can bias results
df = df[df['student.id'] != 3621]

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_data.csv', index=False)

# Remove duplicates based on student.id and term.desc, keeping the first row per term
df = df.drop_duplicates(subset=['student.id', 'term.desc'])

# Done: df now has a new column 'graduation_year' for each row
print(df[['student.id', 'term.desc', 'student.isGraduated', 'graduation_year']])

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
zone_mapping = {'Urban': 0, 'Semiurban': 1, 'Rural': 2, 'No information': -1}
df['student_permAddress.zone_type'] = df['student_permAddress.zone_type'].map(zone_mapping)

# Define a mapping for the age ranges
age_mapping = {'18 and below': 0, '19 to 21': 1,'22 and above': 2}
# Apply the mapping
df['student.age'] = df['student.age'].map(age_mapping)

#Remove no information from student.isForeign
df['student.isForeign'] = df['student.isForeign'].astype(str).str.strip().str.title()
foreign = {'0': 0, '1': 1, 'No Information': -1}
df['student.isForeign'] = df['student.isForeign'].map(foreign)

#Remove no information from student.isForeign
df['student.isFirstGeneration'] = df['student.isFirstGeneration'].astype(str).str.strip().str.title()
firstGen = {'No': 0, 'Yes': 1, 'No Information': -1}
df['student.isFirstGeneration'] = df['student.isFirstGeneration'].map(firstGen)

#Drop test type because its the same for all students
df = df.drop(columns=['student_admission_test.type_desc'])

df['student_admission_test_disc.dominance_score'] = df['student_admission_test_disc.dominance_score'].replace('Does not apply', -1)
df['student_admission_test_disc.influence_score'] = df['student_admission_test_disc.influence_score'].replace('Does not apply', -1)
df['student_admission_test_disc.conscientiousness_score'] = df['student_admission_test_disc.conscientiousness_score'].replace('Does not apply', -1)
df['student_admission_test_disc.steadiness_score'] = df['student_admission_test_disc.steadiness_score'].replace('Does not apply', -1)
df['student_admission_test_valuesIndex.aesthetic_score'] = df['student_admission_test_valuesIndex.aesthetic_score'].replace('Does not apply', -1)
df['student_admission_test_valuesIndex.economic_score'] = df['student_admission_test_valuesIndex.economic_score'].replace('Does not apply', -1)
df['student_admission_test_valuesIndex.individualistic_score'] = df['student_admission_test_valuesIndex.individualistic_score'].replace('Does not apply', -1)
df['student_admission_test_valuesIndex.political_score'] = df['student_admission_test_valuesIndex.political_score'].replace('Does not apply', -1)
df['student_admission_test_valuesIndex.altruistic_score'] = df['student_admission_test_valuesIndex.altruistic_score'].replace('Does not apply', -1)
df['student_admission_test_valuesIndex.regulatory_score'] = df['student_admission_test_valuesIndex.regulatory_score'].replace('Does not apply', -1)
df['student_admission_test_valuesIndex.theoretical_score'] = df['student_admission_test_valuesIndex.theoretical_score'].replace('Does not apply', -1)

#Empty colums probably mean the student did not participate in that term
df = df[df['student.fte'].notna() & (df['student.fte'] != '')]
df = df[df['student.term_gpa'].notna() & (df['student.term_gpa'] != '')]

#Plot status in acending order
df['student.status_academic_desc'] = df['student.status_academic_desc'].astype(str).str.strip().str.title()
academicDesc = {
    'Academic Support, Failed >=10 Courses Before 50% Of The Academic Program': 0,
    'Academic Support, Failed >=2 Courses In Each Of Last 3 Semesters': 1,
    'Academic Support, Failed >=3 Courses In Each Of Last 2 Semesters': 2,
    'Conditioned Student, Failed >=6  Courses Before 50% Of Total Units Of The Academic Program': 3,
    'Conditioned Student, Failed >=3 Courses In The Last Completed Semester': 4,
    'Conditioned Student, Failed 2 Courses In Each Of The Last 2 Completed Semesters': 5,
    'Conditioned Student, Failed 1 Or 2 Courses After Previously Being Conditioned Student': 6,
    'Regular Student': 7,
    'No Status Information': -1     
}
df['student.status_academic_desc'] = df['student.status_academic_desc'].map(academicDesc)

# Save the cleaned DataFrame to a new CSV files
df.to_csv('cleaned_data.csv', index=False)