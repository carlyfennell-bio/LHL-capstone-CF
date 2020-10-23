# The Messi Business of Pitch Control 
### Capstone Project for Lighthouse Labs Data Science Diploma

This is the repo for my capstone project in completion of my Data Science Diploma hosted by Lighthouse Labs.

For this project I worked with a professional soccer team in the MLS. This team recently started using new tracking technology to collect data regarding position, velocity and acceleration of every player (and the ball) on the field for each moment of a match (25 frames per second).  I was tasked with finding a way to better quantify player performance using this data, particularly for players without the ball (most analytics prior was using "on ball" events such as passes, assists, goals, giveaways, etc.).  

In order to achieve this I ended up building a "pitch control" model that predicted the likelihood of possession for point in time (frame). I also built some tools that allowed them to dynamically visualize these pitch surfaces (probability maps) for any sequence of frames they wanted. This was incredibly helpful for them as a tool to understand opponent tendencies and quantify their own player performance more robustly than before.

Technologies I used to complete this included: git, jupyter lab, python, sublime, baysian probability theory, human activity recognition, time series analysis, machine learning, sklearn, pandas, and data visualization using matplotlib, plotly, and other modules to enable gif/mp4 visualization.

This repo holds a collection of notebooks and some additional .py files used to build the models and tools for performance assessment.

**********************NOTE*************************
It is important to acknowledge the contributions of the group "Friends of Tracking".  Their youtube video is below along with their github repo. Their content and information was integral in this project and I used it as the foundation for the model I ended up customizing for the professional team I worked with.  I have included a "TUTORIALS" folder which contains my completed notebooks on the tutorials they present on their youtube channel.

https://github.com/Friends-of-Tracking-Data-FoTD

https://www.youtube.com/channel/UCUBFJYcag8j2rm_9HkrrA7w


**********************Important*************************
The best way to utilize this repo is to work through the notebooks in this order:

1. 1_Parse_Events
2. 2_Parse_Tracking
3. 3_Event_Flagging
4. 4_Data_Exploration
5. 5_Pitch_Control

The FutureWork folder contains some preliminary notebooks related to Human activity recognition, timeseries analysis and the beginning of a notebook meant to combine these together and utlize machine learning/deep learning to predict events only using the tracking data.

********************************************************


Information on Each Notebook:


### 1_Parse_Events

This notebook intakes event files and adjusts the coordinate system and units to match the tracking data. It also normalizes the playing direction such that the home team is always attacking right to left and players are shown in 'red'.  Conversely, the away team is always attacking left to right and players are shown in 'blue'.

The end of the notebook exports a file called "events_cleaned.csv" which is used in subsequent notebooks.

### 2_Parse_Tracking

This notebook intakes tracking data from the company called "second Spectrum". The file format is a pretty big nuisance to parse (it is a huge multiline json file) but this notebook takes care of that. It reads in the file from the json file and flattens it into a dataframe. The other meaty portion of this notebook is how it re-configures the data such that each column is separated per unique player instead of 11 positional columns per team that can track multiple players per column and also simultaneously track various players if they are performing complicated movements on the field such as switching up positions and making runs outside their position.


The notebook exports a file called "tracking_away.csv" and "tracking_home.csv" which is used in subsequent notebooks. 

At the end of the notebook there are some preliminary visualizations utilizing the tracking data.

### 3_Event_Flagging

This notebook takes in the "events_cleaned.csv","tracking_away.csv" and "tracking_home.csv" files previously exported and puts events into 3 categories; "good_events", "good_events_wrong_label", "bad_events".

These categories are decided based on some new calculations:
1. dist = distance between the ball and the event data start coordinates
2. dist_btw = distance between the ball and the player the event is tagged on

There are additional calculations done that are used in the modified pitch control model that allows for the intake of ball speed as well as the an adjusted event plotting tool that adjusts the event vector to start at the position of the ball instead of the coordinates presented in the event file.

Some preliminary analysis was done here to test out the event flagging method. This includes calculating the pass success probability for the home and away team.

Exported files: "good_events_wrong_label.csv", "good_events.csv", "bad_events.csv"

### 4_Data_Exploration & 5_Pitch_Control

Both of these notebooks play around with plotting pitch surface and generating some visuals and clips.
