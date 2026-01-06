import pandas as pd # this is for loading data from CSV, Excel, SQL etc. PREPARING THE DATA
import matplotlib.pyplot as plt #This is used to convert numbers to visuals like SHOWING THE DATA


# These python libraries contain pre-built functions that run the logic and return
# the result

#------------------------------------------------------------------------------------------------------------------------------
#The first step is to load the data
data=pd.read_csv("sales.csv")

#showing the data
print("The data in sales.csv file :\n")
print(data) #this will have data["Sales"] and data["Days"] they are two parameters like this

#Basic summary
print("\nsummary of the data:")
print(data.describe())


#checking if the sales went up or down overall
average_sales=data["Sales"].mean()
print("Avg sales:",average_sales)

if data["Sales"].iloc[-1] > data["Sales"].iloc[0]:
    print("Sales increased overall")
else:
    print("Sales decreased overall")    

print(data["Sales"].iloc[-1])#the last Sales value
print(data["Sales"].iloc[0])#the first Sales value


#------------------------------------------------------------------------------------------------------------------------------

#this most fun part
from sklearn.linear_model import LinearRegression
import numpy as np

#prepare the data
X=data[["Day"]] #since there could be more than one inputs but in linear just one
y=data["Sales"]

#Train the model
model= LinearRegression()
model.fit(X,y)

#Predict the next day
next_day = pd.DataFrame([[8]], columns=["Day"])
prediction= model.predict(next_day)
print(prediction)
print("\nPredicted sales for Day 8:", int(prediction[0]))

#------------------------------------------------------------------------------------------------------------------------------

#plotting the data to visualize it
plt.plot(data["Day"],data["Sales"])
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Sales(Y) over days(X)")
plt.show()


