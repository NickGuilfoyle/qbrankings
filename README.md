# qbrankings
Python file to rank NFL quarterbacks for a given year using a metric I designed to measure entertainment value.


### Statistics  
Quarterbacks are ranked based on how eventful they were in a season.  
This was inspired by 2019 Jameis Winston where Winston threw for 5,000 yards 30 tds and 30 interceptions.  
This ranking tends to have better qbs rise to the top based on throwing for lots of yards and touchdowns, but we also reward interceptions in this metric since I would argue interceptions are one of the more entertaining plays in football. The metric is calculated as such:  
((interceptions * 20 + touchdowns * 20 + yards) / attempts) * (.25 * attempts/game)  
The thought process here was to reward quarterbacks who produced a lot of aciton on their throws, and also to reward quarterbacks who had a high workload. An attempt threshold of 150 is also applied to filter out non qb passers.  


### Usage  
Run with python3 command with optional year parameter.  
Default year is 2020, but year can be changed by user.  
Prints ouput as sorted list of QB Name, entertainment rating pairs.  

### Requirements  
* Python 3  
* BeautifulSoup4  
* requests  
* sys  
