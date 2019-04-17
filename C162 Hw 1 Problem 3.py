
# coding: utf-8

# ## Problem 3

# ### Plot the radio flux for the full solar cycle 

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import datestr2num

data = np.genfromtxt('noaa_radio_flux(1).csv', delimiter =',', skip_header = 1)#, dtype=(str+str,float))#, converters = {0: datestr2num})
data = np.rot90(data)
#print(data[0])
#print(type(data))
#print(np.shape(data))


# In[4]:


dates_0 = np.loadtxt('noaa_radio_flux(1).csv',skiprows = 1, dtype=(str))
dates = np.rot90(dates_0)

year = dates[2]
month = dates[1]

dates_1 = []
values = []

for i in dates[0]:
        dates_0 = i[0]+ i[1]
        values_0 = np.float(i[3]+i[4]+i[5]+i[6])
        dates_1.append(dates_0)
        values.append(values_0)
    

calendar_dates = []
            
for i in range(len(year)):
    
    date = datetime.strptime(year[i] + '-' + month[i] + '-' +dates_1[i], '%Y-%m-%d')
    calendar_dates.append(date)

remove = []

for i in range(len(values)):
        if values[i] < 0:
            remove.append(i)
            
#print(remove)

for i in sorted(remove, reverse=True):
    del values[i]
    del calendar_dates[i]
            


plt.plot(calendar_dates, values)
plt.title('Solar Cycle 23')
plt.ylabel('F10.7 flux [SFU]')
plt.xlabel('Time [Years]')
plt.rcParams['figure.figsize'] = [15, 5]
plt.show()


# ### Explain what causes this pattern?

# The F10.7 index is a measure of the solar radio flux per unit frequency at a wavelength of 10.7 cm, near the peak of the observed solar radio emission. Emission from the Sun at radio wavelength is due primarily to coronal plasma trapped in the magnetic fields overlying active regions. When observed solar radio emission is plotted as a function of time, as shown, one can discern a roughly gaussian distribution in an 11-year period from 1996-2007. This variation is caused by changes in the solar magnetic field, corresponding with the 11-year reversal of the north and south magnetic poles.

# ### Zoom into the data to resolve about 250 days (e.g.  days 1000 - 1250 since August, 1st 1996).

# In[10]:


plt.plot(calendar_dates[1000:1250], values[1000:1250])
plt.title('Solar Cycle 23')
plt.ylabel('F10.7 flux [SFU]')
plt.xlabel('Time [YYYY-MM]')
plt.rcParams['figure.figsize'] = [15, 5]
plt.show()


# ### Which periodicity can you recognize on shorter time scales?  Explain what causes the pattern.

# On shorter timescales we recognize a roughly sinusoidal pattern, with periods of about a month, which is probably due to the rotation of the sun, has a rotation period of 25 days. 
