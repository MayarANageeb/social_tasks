#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello from Jupyter')


# In[2]:


my_str = 'Hello'
my_int = 16

print(my_str)
print(my_int)


# In[3]:


my_str


# In[4]:


my_str
my_int


# In[5]:


number_of_apples = 5

if number_of_apples < 1:
    print('You have no apples')
elif number_of_apples == 1:
    print('You have one apple')
elif number_of_apples < 4:
    print('You have a few apples')
else:
    print('You have many apples!')


# In[6]:


student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_names[1]


# In[7]:


student_names[0]


# In[8]:


student_names[-1]


# In[9]:


student_names[0:2]


# In[10]:


student_names[1:3]


# In[11]:


student_names[:2]


# In[12]:


student_names[2:]


# In[13]:


student_names.append('Esther')
student_names


# In[14]:


student_names.insert(2, 'Xavier')
student_names


# In[15]:


del student_names[2]
student_names


# In[16]:


student_names.append('Esther')
student_names.append('Esther')
student_names


# In[17]:


student_names = ['Alice', 'Bob', 'Carol', 'Dave']

for student_name in student_names:
    print('Hello ' + student_name + '!')


# In[18]:


long_names = []
for student_name in student_names:
    if len(student_name) > 4:
        long_names.append(student_name)

long_names


# In[19]:


student_names = ['Alice', 'Bob', 'Carol', 'Dave']

student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        student_pairs.append(
            (student_name_0, student_name_1)
        )

student_pairs


# In[20]:


student_pairs[0]


# In[21]:


student_pairs[1]


# In[22]:


student_names = ['Alice', 'Bob', 'Carol', 'Dave']
student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        if student_name_0 != student_name_1:
            student_pairs.append(
                (student_name_0, student_name_1)
            )
student_pairs


# In[23]:


student_grade = ('Alice', 'Spanish', 'A-')
student_grade


# In[24]:


student_grade[0]


# In[25]:


student_grade.append('IU Bloomington')


# In[26]:


del student_grade[2]


# In[27]:


student_grade[2] = 'C'


# In[28]:


student_grade = ('Alice', 'Spanish', 'A-')
student_name, subject, grade = student_grade

print(student_name)
print(subject)
print(grade)


# In[29]:


student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]

for student_name, subject, grade in student_grades:
    if grade.startswith('A'):
        print('Congratulations', student_name,
              'on getting an', grade,
              'in', subject)


# In[30]:


for student_grade in student_grades:
    if student_grade[2].startswith('A'):
        print('Congratulations', student_grade[0],
              'on getting an', student_grade[2],
              'in', student_grade[1])


# In[31]:


foreign_languages = {
    'Alice': 'Spanish',
    'Bob': 'French',
    'Carol': 'Italian',
    'Dave': 'Italian',
}


# In[32]:


foreign_languages['Carol']


# In[33]:


foreign_languages['Zeke']


# In[34]:


'Zeke' in foreign_languages


# In[35]:


'Alice' in foreign_languages


# In[36]:


'alice' in foreign_languages


# In[37]:


foreign_languages['Esther'] = 'French'
foreign_languages


# In[38]:


del foreign_languages['Bob']
foreign_languages


# In[39]:


foreign_languages['Esther'] = 'Italian'
foreign_languages


# In[40]:


for key in foreign_languages:
    value = foreign_languages[key]
    print(key, 'is taking', value)


# In[41]:


for key, value in foreign_languages.items():
    print(key, 'is taking', value)


# In[42]:


student_grade = ('Alice', 'Spanish', 'A')
student_name, subject, grade = student_grades[0]
print(student_name, 'got a grade of', grade, 'in', subject)


# In[43]:


record = {
    'name': 'Alice',
    'subject': 'Spanish',
    'grade': 'A',
}
print(record['name'],
      'got a grade of', record['grade'],
      'in', record['subject']


# In[44]:


record = {
    'name': 'Alice',
    'subject': 'Spanish',
    'grade': 'A',
}
print(record['name'],
      'got a grade of', record['grade'],
      'in', record['subject'])


# In[45]:


student_grades = [
    ('Alice', 'Spanish', 'A'),
    ('Bob', 'French', 'C'),
    ('Carol', 'Italian', 'B+'),
    ('Dave', 'Italian', 'A-'),
]
student_grades[1]


# In[46]:


student_grades[1][2]


# In[47]:


student_grade_records = []
for student_name, subject, grade in student_grades:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records


# In[48]:


student_grade_records[1]


# In[49]:


student_grade_records[1]['grade']


# In[50]:


for record in student_grade_records:
    if record['grade'].startswith('A'):
        print('Congratulations', record['name'], 
              'on getting an', record['grade'], 
              'in', record['subject'])


# In[51]:


foreign_language_grades = {}
for student_name, subject, grade in student_grades:
    record = {
        'subject': subject,
        'grade': grade,
    }
    foreign_language_grades[student_name] = record
    
foreign_language_grades


# In[52]:


foreign_language_grades['Alice']


# In[53]:


foreign_language_grades['Alice']['grade']


# In[54]:


student_course_grades = {}
for student_name, subject, grade in student_grades:
    student_course_grades[student_name, subject] = grade
    
student_course_grades


# In[55]:


student_course_grades['Alice', 'Math'] = 'A'
student_course_grades['Alice', 'History'] = 'B'


# In[56]:


student_course_grades


# In[57]:


student_report_cards = {}
for student_name, subject, grade in student_grades:
    if student_name not in student_report_cards:
        student_report_cards[student_name] = {}
    student_report_cards[student_name][subject] = grade


# In[58]:


student_report_cards


# In[59]:


student_report_cards['Alice']['Math'] = 'A'
student_report_cards['Alice']['History'] = 'B'
student_report_cards


# In[60]:


student_report_cards['Alice']


# In[ ]:




