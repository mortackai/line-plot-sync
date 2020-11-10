# line-plot-sync
a tool for syncing csv files with line plots and finding standard deviation, mean, etc.


Take a folder of csvs
Allign their times, and output a file of averages etc...

The issue is that thet files aren't recorded the same. When they run the test, they just start it all up pretty randomly -- there might be 10 minutes of nothing sitting at the begginging. We have to deal with /allignment/.

We could take a point right after it drops under 290, call that time 0.
Then generate a new csv where