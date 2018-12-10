# Invisy
Making people disappear since 2018.

## Demo
**This demo was filmed at The 2018 Local Hack Day at University of Manitoba, and this project helped us awarded an Honorable mention at the event**✌️
![](https://github.com/Jarde01/Invisy/blob/master/person_blocker.gif)

## Credit
This [Person-blocker repo](https://github.com/minimaxir/person-blocker) classifies the object in the still image, our implementations were based on this repo and turned its feature into real-time object detection.

## Idea and Techniques
Inspiration was from [**Black Mirror White Christmas Episode**](https://www.youtube.com/watch?v=_dXqugxU1sk&t=44s) and the technique we used is called [**Mask R-CNN**](https://arxiv.org/abs/1703.06870) which predicts an object mask in parallel with the existing branch for bounding box recognition.

## Current Implementation: 
- phone uses ip webcam to set up web service with live video feed.
  - can replace with other video sources
- invisy grabs screenshots and sends them to the model for classification
- display the model output to the screen after processing

