---
layout: post
title:  Grabbing NBA Player Tracking Data with R
date: 2014-04-24
---

# NBA Player Tracking

If you haven't heard, the NBA--in collaboration with a company called SportVU--recently implemented a really cool new player data collection system that it calls "Player Tracking". For the official details, you can read more about Player Tracking [here](http://stats.nba.com/playerTracking.html). Essentially, the NBA has installed a bunch of cameras in the catwalks of its arenas. With the help of SportVU's software, the video feeds from these cameras can be processed automatically and used to generate all kinds of really specific player statistics. 

In particular, one of the main benefits of this new system is that it is able to break down a bunch of statistics that were previously only avaialable at an aggregate level. For example, whereas you might previously have looked at a player's overall field goal percentage (i.e. the percentage of shots the player makes), you can now look at the player's FGP broken down by shot type--e.g. their FGP when driving vs. on catch-and-shoot shots vs. on pull up shots etc. Though I'm certainly no NBA stats expert, my sense is that this is a much finer level of statistical resolution than was previously available.   

# Getting the Data

The unfortunate part about all this is that the NBA stats site does not currently have an API set up for retrieving the Player Tracking data, though it can be viewed in full on the stats.nba.com website. Moreover, the data is (oddly) stored in the form of a javascript object ([e.g.](http://stats.nba.com/js/data/sportvu/pullUpShootData.js)) that is resistent to direct processing with R's various json or csv readers. With that in mind, I've worked out a little R hack that grabs the various raw player tracking data sets from the stats.nba.com website, converts them to something readable with R's read.table() function (using a bit of regex), and finally merges them in to one big R data frame (with one row per player).

A few points about this project. The first step was to find the location of the source files for the player tracking data. In general, I don't really know what the best method is for doing something like this. In this case, I got a first step from [this](http://www.reddit.com/r/rstats/comments/1r9nv5/scraping_javascript_from_new_nba_data_source/) thread on reddit. I was then able to locate the other source files just by manually poking around the player tracking site's source code. 

In any case, here's the list of raw data addresses: 


{% highlight r %}
addressList <- list(
pullup_address="http://stats.nba.com/js/data/sportvu/pullUpShootData.js", drives_address = "http://stats.nba.com/js/data/sportvu/drivesData.js",		defense_address="http://stats.nba.com/js/data/sportvu/defenseData.js",	passing_address = "http://stats.nba.com/js/data/sportvu/passingData.js", 
touches_address = "http://stats.nba.com/js/data/sportvu/touchesData.js", 
speed_address = "http://stats.nba.com/js/data/sportvu/speedData.js", rebounding_address = "http://stats.nba.com/js/data/sportvu/reboundingData.js", 
catchshoot_address = "http://stats.nba.com/js/data/sportvu/catchShootData.js", 
shooting_address = "http://stats.nba.com/js/data/sportvu/shootingData.js"
)
{% endhighlight %}

The next step was to write a function to read in the raw data from one of these addresses, and convert it to a form that's readable by one of R's i/o functions. There are a couple of ways to do this, I think, but I found the following approach to be the easiest: 

{% highlight r %}
# function that grabs the data from the website and converts to R data frame
readIt <- function(address) {
    web_page <- readLines(address)
    
    # regex to strip javascript bits and convert to csv
    x1 <- gsub("[\\{\\}\\]]", "", web_page, perl = TRUE)
    x2 <- gsub("[\\[]", "\n", x1, perl = TRUE)
    x3 <- gsub("\"rowSet\":\n", "", x2, perl = TRUE)
    x4 <- gsub(";", ",", x3, perl = TRUE)
    
    # read the resulting csv with read.table()
    nba <- read.table(textConnection(x4), header = T, sep = ",", skip = 2, stringsAsFactors = FALSE)
    return(nba)
}
{% endhighlight %}


The regex essentially just strip out some of the JS headers and convert the nested JSON that actually contains the data into a csv that can be read by read.table(). The obvious alternative approach would be to strip just the very beginning of the JS stuff and read it as a JSON, e.g something like this:


{% highlight r %}
x1 <- gsub("var \\w+Data = (.*);", "\\1", web_page, perl = TRUE)
x2 <- fromJSON(x1)  #from rjson package
{% endhighlight %}


This works fine, but is a bit annoying since it returns a big nested list object to reflect the structure of the original JSON (and I really just wanted a flat file). Either way, with all this in place, grabbing the data is now a simple matter of:


{% highlight r %}
df_list <- lapply(addressList, readIt)
{% endhighlight %}


That's the gist of it anyway. You can look at or download the full script from my github [here](https://github.com/Fossj117/NBAdata.git). The script also has some code for merging the various data sets in to one big data frame (with one listing per player). I also have a fairly recent csv in the github repo that can be opened with excel or whatever, in case you just want the data. 

# Future Plans for this Project: 

* Try and figure out what interesting things can actually be done with this data. Thoughts:
	* How does diversity of shot selection relate to shooting outcomes? (i.e. does "keeping the defense guessing" correlate with a higher shooting percentage?)
    * Aggregate these statistics by team and see how they correlate with team-level outcomes.
* Set up a system for automatically collecting/storing this data periodically (to create a series of snapshots of how a player is performing/changing?)