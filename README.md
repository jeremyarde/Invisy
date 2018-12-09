# Invisy
Making people disappear since 2018.

## Demo
The demo for running the model in the real-time.
![](https://github.com/Jarde01/Invisy/blob/master/person_blocker.gif)

## Credit
This [Person-blocker repo](https://github.com/minimaxir/person-blocker) classifies the object in the still image, out implementations were based on this repo and turned its feature into real-time object detection.

## Current Implementation: 
- phone uses ip webcam to set up webservice with live video feed.
  - can replace with other video sources
- invisy grabs screenshots and sends them to the model for classification
- display the model output to the screen after processing

