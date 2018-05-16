
# Open-Ended Project MVP

### Goals:

**GTD Terrorism Definition -** <br> acts by non-state actors involving threatened or actual use of illegal force or violence to attain a political, Economic, religious, or social goal through fear, coercion or intimidation. 
<br><br> Mandatory Inclusion Criteria:
Event must be intentional - the results of a conscious calculation on the part of the perpetrator.
If attack fails to take place - recorded as unsuccessful attack.

<br><br>Learn:

- Location of terrorist attacks
- Patterns of terrorism in ?
- How frequent do these types of attack take place
- What groups are commonly perpetrators of terrorism in?
- Targets of terrorism
- Perpetrators most active / most lethal in a single year
- Attacks vs. Fatalities
- Rank countries with most attacks/fatalities
- What weapon is used for the type of attack or target
- Does data show that terrorists incite fear and not kill
- prove/disprove myth that most terrorist attacks are extremely lethal, and that the US is more frequently targeted than any other country

### Initial Data Cleaning Approach and Exploratory Findings

The data was retrieved and is available from the Global Terrorism Database (GTD).
Since these data file is published by University of Maryland, the data was relatively clean.  Data was pre-processed to transform data for the different data visualizations/exploration and analysis needs, and to compute and add data columns, which may be relevant to include in the table/dataframe for the analysis.

Attacktype1, Targtype1 fields are most of the time populated if known, further exploration done on events where more than one Attack or Target exists.

GTD staff based at the START headquarters at the University of Maryland integrated and synthesised data collected across the entire 1970-2016 time span.

*National Consortium for the Study of Terrorism and Responses to Terrorism (START). (2017)
 Global Terrorism Database [globalterrorismdb_0617dist.xlsx].  Retrieved from http://www.start.umd.edu/gtd*
 
 
** BAAD - Big Allied and Dangerous data was scraped and loaded to SQLite database on 4/28, START has modified web pages since then, script for scraping no longer applies.



### Initial Research Findings

#### Exploring Attacks, Fatalities and Perpetrators (terrorist group)

<img src="files/images/attack_vs_fatal_year.png">

The graph above (Attacks vs. Fatalities by Year) shows large numbers of fatalities cumulatively per year, but the graph below shows that average fatalities per attack is less than five for most of the years prior to 1998. On 1998, 2001, 2002, 2004 and 2007 the average fatalities per attack were at its peak.

<img src="files/images/byYear_avgkill.png">

Based on the findings, US is not in the Top 20 countries with most attacks/fatalities, contrary to popular belief that US is more frequently targeted than any other country.

<img src="files/images/bar_kill_by_country.png">

<img src="files/images/bar_top15_kill_byGroup.png">

<img src="files/images/bar_top15_attack_byGroup.png">

<img src="files/images/bar_target_vs_kill.png">

<img src="files/images/bar_fatal_by_attack.png">

### Exploring Attacks and Weapons used
Plot below shows the different attack types for each of the year group, and the weapons used in those attacks

<img src="files/images/out_weaptype_by_attacktyp1.png">

#### The plot below explores the weapon types used for the top five most fatal attack types

### Further Research and Analysis

1. identify perpetrator who is/are has caused the most attacks and or fatalities

2. likelihood that there will be a fatality when a successful attack happens

3. determine trends in terrorism/attacks after 9/11
