
# MVP EDA Airbnb Paris

## Background

When traveling to Europe and booking an Airbnb rental property for a vacation, I try to spend less on lodging to be able to afford good dining and tours.  For Paris specifically, I find that the options close to the centre, that is close to the top attractions i.e. Eiffel tower, Champs Elysees are pricier, and most of the properties are unavailable as well, so I end up staying further from the centre, and when I do, I am always worried that I might have booked a property that is way too far out from the centre of the city, and or far from a metro station -- since actual location is not provided until after you have made the reservation, or unless you contact host and ask.  Distance to the station is relative depending on how far one is willing to walk, but for me, more than a mile to a station is considered far, since I feel I have to save all my energy for the leisurely walking one does around Paris.

## Questions for Exploration / Goals:


1) to be able to explore and answer the following questions:

* How does location influence property rental price, reviews and availability?  

* What other features drive the price of an airbnb rental property?

  i.e. price vs location, price vs distance from a top attraction, etc.


2) recommend Airbnb properties given a certain criteria, and enable a more informed decision for the traveler:

* walking distance to one of the top attractions (within 2 miles)
* walking distance to metro station (within 1 mile)
* rating >= 9

* other user defined criteria i.e.
* number of beds
* number of bedrooms
* price range
* type of property

## Initial Exploration

Plotting the property prices out, shows us that the price of Airbnb rental properties in Paris  have a unimodal distribution, which is right skewed.  We can see from the graph below it shows that majority of the properties are rented out are below \$200, with the average below \$100 which is at \$94.79, with the median only at $75.  We can see that there are some outliers -- properties over \$400, causing a huge difference between the mean and the median price, and for the distribution to be right skewed.

![Price Distribution](images/airbnb_price_dist.png)

The following features below shows the correlation with the Airbnb rental property price:
* It does make sense that the distance between the top attractions and the Airbnb property is negatively correlated with the price, and so is with the Arrondissement.  

* With regards to distance between Le Marais and the Airbnb property being positively correlated, it is possible that those properties which are farther from Le Marais are closer to the other top attractions, giving us that inconsistent correlation as far as distances from top attractions are concerned.  We can add another feature for an indicator if property is within two miles of one of the top attractions, and the top attraction it is closest to and use that for further analysis, instead of the individual distances to the top attraction.

* And as far as the other property features are concerned, we can see that the number of beds, bedrooms, and accomodations are positively correlated with the Airbnb property price.  It is expected that the bigger the accomodation is, the rental price will be higher as well.

![Correlated Features](images/features_corr.png)

As we saw from the correlation graph above --  Arrondissement values are negatively correlated with the price, that is, the Airbnb properties in the lower Arrondissements on average costs more than the properties in the higher arrondissements, which is what the graph below shows.

![By Arr](images/airbnb_price_byArr.png)

If we look at each of our top 10 attractions in Paris, we can see that the attractions are in arrondissements 1 through 8.

With regards to the availability the graphs below shows that the price does have direct relationship on the availability of the Airbnb rental properties in Paris, but the availability by arrondissements seem to be pretty consistent across all arrondissements, with the exception of arrondissements 8 and 16.  

The graph on Prices by Arrondissement shows that property prices are highest in arrondissement 8, which will be consistent with the high availability in that arrondissement.  However, for arrondissement 16, it is possible that the distance to attractions could be a factor, and we can explore that further.

![By Arr](images/airbnb_price_byAvail.png)

![By Arr](images/airbnb_avail_byArr.png)

## Initial Research Findings

Based on initial Exploratory Analysis, we can see that:

* the lower priced Airbnb properties have less availability, this would affect the probability of finding a property for at that lower price range i.e. for a less than \$100/night budget

* the properties in the lower Arrondissements, those closest to the top attractions cost more on average compared to the properties in the higher arrondissements.


## Further Research and Analysis

* Further explore properties in the desired criteria:
<br> properties less than \$100/night
<br> distance within 2 miles of one of the top attractions
<br> properties with 1 bed, accommodates less than or equal to 2

* Determine how the distance to the top attractions affect the price

* Determine how the distance to the metro affects the price

* Recommend top 20 properties given a certain criteria

### Limitations
* the Airbnb data from OpenDataSoft was last updated in 2017
* Historical data for the property prices and availabity are not available, so we are unable to check for variability of price and availability on different seasons/time.


```python

```
