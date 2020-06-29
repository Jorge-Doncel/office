# Data Analysis to choose a new office location

![The office](https://github.com/Jorge-Doncel/office/blob/master/input/Captura%20de%20pantalla%20de%202020-06-29%2017-11-09.png)

## Introduction

I will create a new company in the Gaming Industry. My company will have the following scheme:

- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy that loves basketball
- 10 Executives
- 1 CEO/President

I want to choose the best places for the company to grow. After I asked all the employees to show their preferences on where to place the new office, the result was:

- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.

- 30% of the company have at least 1 child.

- Developers like to be near successful tech startups that have raised at least 1 Million dollars.

- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.

- Account managers need to travel a lot

- All people in the company have between 25 and 40 years, so they need some place to go to party.

- I'm Vegan

- The maintenance guy like basketball so a basketball stadium should be around 10 Km.

- The office dog "Pepe" needs a hairdresser every month. 
​
You want to found a place that more or less covers all the  requirements to make them happy.

## Table of Contents


- [Previous analysis](#Previous-analysis)
- [Libraries](#libraries)
- [Resources](#resources)
- [Data Processing](#data-processing)
- [Conclusions](#Conclusions)
- [Study topics](study-topics)

## Previous analysis

I want to locate my company in the most important city for the video game industry in the world. After analyzing the industry, I discovered that the [top country for game development studios in the world is United States](https://www.gameindustrycareerguide.com/best-cities-for-video-game-development-jobs/) and the [top city is San Francisco](https://www.gamedesigning.org/career/cities/)

Regarding the requests of my employees, I want my company to grow in the future, so I want to locate my office as close as possible to other companies related to gaming or design industry so that my designers can improve their knowledge. Also, I want to make the rest of the employees happy so they are happy when they are working (close starbucks and vegan restaurants) and in their free time (Parks for people with kids, Nightclubs and basketball Stadium)


## Libraries

- Pandas
- Numpy
- json
- requests
- re
- pymongo
- os
- dotenv
- folium
- math

## Resources 

I have used [FourSquare Api](https://developer.foursquare.com/docs/places-api/) to obtain all the information I needed.

## Data Processing

I have selected the offices of other companies with near Starbucks, Vegan Resturants, Basketball Stadiums, Parks and NightClubs. I used queries and [categoryID](https://developer.foursquare.com/docs/build-with-foursquare/categories/)

For Starbucks and vegan restaurants, I've selected a 100-meter radius so my employees don't have to go far away from the office. For activities outside working hours, I have selected a radius of 1km. 

Then, I have obtained the location of all the places regarding these offices.

Finally, I have located my future new office in the mean location of all places to be close to all of them. 


## Conclusions

My future office will be in MONTGOMERY ST 44 ('latitude': 37.78931154002931, 'longitude': -122.40202634116092).

![New Office](https://github.com/Jorge-Doncel/office/blob/master/input/the-office-1200.jpg)