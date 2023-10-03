lidarange
==============================

Range problems

Project Organization
--------------------

    .
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    ├── bin
    ├── config
    ├── data
    │   ├── external
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── docs
    ├── notebooks
    ├── reports
    │   └── figures
    └── src
        ├── data
        ├── external
        ├── models
        ├── tools
        └── visualization

## Problem statement 
 Participants must develop a code to find where two or more time series overlap. The range of each time series is represented as a pair of numbers, which are the time the interval started and ended. The output is the largest range that they all include:
### scenario 1 point
    - Parameters:  [3,0 - 0,4.5]
    - Result: [0,0] Coinciding numbers
### scenario 2
    - Parameters:  [[3,-1], [0,4.5]]
    - Result: "No overlap" 
### scenario 3
    - Parameters:  [[3,-1], [3,-1]]
    - Result: "Equal Range"
### scenario 4
    - Parameters:  [[3,-1]]
    - Result: "Not enough Parameters. Enter atleast 2 ranges"
### scenario 5
    - Parameters:  [[-3,5], [0,4.5], [-1.5,2.0]]
    - Result: [0,2]
