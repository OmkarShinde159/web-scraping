import pandas as pd

old_data = {'Emp_id':[100,101,102,103],
            'First_Name':['Ramesh','Suresh','Mukesh','Kamlesh'],
            'Last_Name': ['Sawant','Shinde','Shaikh','Yadav'],
            'Salary':[1000,1200,1150,950]}

df = pd.DataFrame(old_data, index = [1,2,3,4])
df.to_csv('Emp_details.csv')
# print(df)

new_data ={'Emp_id':[100,101,102,103],
            'First_Name':['Rachana','Priyanka','Nikita','Manali'],
            'Last_Name': ['Kadam','Shah','Jain','Parekh'],
            'Salary':[1025,1350,1250,1125]}
    
df1 = pd.DataFrame(new_data,index=[5,6,7,8])
# print(df1)

df = df.append(df1)
df.to_csv("Emp_details.csv")

read = pd.read_csv("Emp_details.csv",index_col=0)
print(read)