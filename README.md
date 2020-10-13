# Oslo bike sharing analysis

## Overview
Bike sharing systems are a means of renting bicycles where the process of obtaining membership, rental, and bike return is automated via a network of kiosk locations throughout a city. Using these systems, people are able rent a bike from a one location and return it to a different place on an as-needed basis.  

Bike sharing systems  function as a sensor network, which can be used for studying mobility in a city. In my case i am going to look at historical demand in order to try to forcast current demand

### Data fields
<table>
  <tbody>
    <tr>
      <th>Variable</th>
      <th align="center">Format</th>
      <th align="right">Description</th>
    </tr>
    <tr>
      <td>
        <ul>
          <li>started_at</li>
          <li>ended_at</li>
        </ul>
      </td>
      <td align="center">Timestamp</td>
      <td align="right">Starttime and endtime for trip</td>
    </tr>
    <tr>
      <td>duration</td>
      <td align="center">Integer</td>
      <td align="right">Time of trip in seconds</td>
    </tr>
    <tr>
      <td>
        <ul>
          <li>start_station_id</li>
          <li>start_station_name</li>
          <li>start_station_description</li>
          <li>start_station_longitude</li>
          <li>start_station_latitude</li>
        </ul>
      </td>
      <td align="center"><ul>
          <li>String</li>
          <li>String</li>
          <li>String</li>
          <li>WGS84 decimal</li>
          <li>WGS84 decimal</li>
        </ul></td>
      <td align="right">various information for start station</td>
    </tr>
    <tr>
      <td>
        <ul>
          <li>end_station_id</li>
          <li>end_station_name</li>
          <li>end_station_description</li>
          <li>end_station_longitude</li>
          <li>end_station_latitude</li>
        </ul>
      </td>
      <td align="center"><ul>
          <li>String</li>
          <li>String</li>
          <li>String</li>
          <li>WGS84 decimal</li>
          <li>WGS84 decimal</li>
        </ul></td>
      <td align="right">various information for end station</td>
    </tr>
  </tbody>
</table>  

## Feature Engineering
Since my objective is to make a predictive model of demand, i need good features that can make correlations between earlier data and future data. For this i chose to split the started_at column into different columns for  what day in the week, and what hour of the day (rounded down). I did not use the other data because of time constraints, but will come with suggestions for further analysis at the end.

The categorical features (hour and weekday) were one hot encoded to be able to gather the information within the features. Below is an example on what one hot encoding is, read more on it [here!](https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/)
![one hot encoding](https://user-images.githubusercontent.com/45593399/71045856-d133b980-2136-11ea-954f-fde154fb5ea9.PNG)  

## Visualizing and analyzing
Below is a model for the average use per day for the citybikes, It is divided in weekend and weekdays since they have wildly different distributions. The data is gathered from september 2019.
![image](https://user-images.githubusercontent.com/45593399/95861080-3bba8380-0d61-11eb-9c2d-0b1d110e92cf.png)  
Different months have different max users, but they all follow this general shape. One exception to this is march and april 2020 which saw huge reductions because of the corona virus. 
![image](https://user-images.githubusercontent.com/45593399/95861933-6f49dd80-0d62-11eb-8582-965141afae9c.png)  
  
One major contribution to the fluctuation is weather and season. You are more likely to take the bus on days with rain and wind. This makes it currently hard to model on a weekly basis with great accuracy, but if we meassure the demand across the whole month, a lot of these fluctuations will dissapear into the average and we will be left with something that better model the average demand for each month. A stable market without rapid growth is also needed for this last prediction to hold.


## Results and evaluation
A gradient boosting model was used since it has a proven good track record with regression problems on tabular data. The testing metrics don't look exceptionally good, but as im going to discuss under improvements there are a lot of steps we can take to make this better. ![image](https://user-images.githubusercontent.com/45593399/95874773-8ba14680-0d71-11eb-9a66-d8233bb46ba8.png)  
The mean absolute error, which is the average difference between the amount of predicted and real amount of bicycles used, seem pretty high at 73. We can look further into where it predicted wrongly. ![image](https://user-images.githubusercontent.com/45593399/95876131-0c147700-0d73-11eb-8221-7d890271f2a7.png)  When we look at it here, it seems to perform within what i would describe as acceptable. Infact, when the bicycle number is above 50, it is never more tahn 30% away from the real value!  If we graph the predicted number of rides on top of the actual number of rides, we get this graph which is really visually convincing. ![image](https://user-images.githubusercontent.com/45593399/95876650-9230bd80-0d73-11eb-90f1-6ba952b0d450.png)

## Improvements
This was just an introductionary analysis of the data and its aplication, there are a number of steps we can take to make our model bether, and other things we maybe rather want to model.  

The model could be vastly improved by having more relevant data to lean on, especially weather data, and one should take into consideration all previous data so that the model can generalize better by taking the month into consideration. Additionally, in this analysis i have foregone normalizing the data.  

The largest fluctuations seem to occur during the weekends, so an idea for improvement could be to have a scraper for twitter and facebook events for the Oslo area to take into consideration external events as a feature.  

It may be that we are more interested in the amount of bicycles used at each station for each hour of the day. This would certainly require more data, and would be alot more susceptible for variance, but could still be very helpful for the employees which are to move bikes.



