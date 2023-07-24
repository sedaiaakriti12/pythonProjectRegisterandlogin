import matplotlib.pyplot as plt

# x axis
x= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# y axis
y= [49.72,22.94,54.98,91.67,2.85,19.29,27.9,49.77,30.71,25.4,98.8,73.84,38.03,95.44,85.48,74.81,64.81,34.94,46.12,54.88]

plt.style.use('seaborn')
plt.bar(x=x, height=y, width=0.4)
plt.xticks(x, (2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020))

y2 = [i+3 for i in y]
plt.title('Stock Price Of ABC Company')

plt.plot(x, y2, color='green')
plt.scatter(x, y2)

plt.xlabel('Years')
plt.ylabel('Stock Price($)')

plt.show()
