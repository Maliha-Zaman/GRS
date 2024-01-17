# GRS
Gesture Recognition System (GRS) is a system that detects hand gestures using Google's Mediapipe. It recognizes hand signs and fingers which are stored for learning, simulation, and testing.

## Requirements
- mediapipe 0.8.1
- OpenCV 3.4.2 or Later
- Tensorflow 2.3.0 or Later
- tf-nightly 2.5.0.dev or later (Only when creating a TFLite for an LSTM model)
- scikit-learn 0.23.2 or Later (Only if you want to display the confusion matrix)
- matplotlib 3.3.2 or Later (Only if you want to display the confusion matrix

## Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Demo](#demo)
- [Contributing](#contributing)

## About
- Gesture Recognition System (GRS) is a system that detects hand gestures which is used for helping people to learn the gestures used by deaf-mute people to improve communication.
GRS bridges the gap with the deaf-mute community by making communication easier.

- Google MediaPipe's HandLandmark model is a part of the MediaPipe framework, which is developed by Google for building real-time, cross-platform computer vision applications. The HandLandmark model specifically focuses on hand tracking and landmark estimation, enabling the accurate localization of key points on a user's hand in real time.

## Getting Started
Just clone the whole project and run this: 
```
python mananage.py runserver
```

## Demo
- In GRS, first, we will land on our landing page: 
![Screenshot 2024-01-18 001241](https://github.com/Maliha-Zaman/GRS/assets/95127037/a4c53d24-d53f-4690-8fbc-3dea8e82daf7)
Here we can see all the features of the project like learning gestures, testing, gesture list, etc:
![Screenshot 2024-01-18 001256](https://github.com/Maliha-Zaman/GRS/assets/95127037/43fe9c56-7709-4499-96a5-e7bc55843966)
- In the features list we will first encounter "simulation" In this part we used the the OpenCV to capture and the media pipes hand model for the hand landmarks:
![Screenshot 2024-01-18 001356](https://github.com/Maliha-Zaman/GRS/assets/95127037/11a12f5b-793f-4c45-a242-c3c5db5067e5)
![Screenshot 2024-01-18 001810](https://github.com/Maliha-Zaman/GRS/assets/95127037/17bf1a8a-823a-4b04-a19b-78595a6b4946)
- Then if traverse more in the web we will encounter the features like making sentences in real-time, and testing: 
![Screenshot 2024-01-18 001341](https://github.com/Maliha-Zaman/GRS/assets/95127037/2d2fa714-02a4-4325-a05b-1696b5954842)
![Screenshot 2024-01-18 001413](https://github.com/Maliha-Zaman/GRS/assets/95127037/f3c91bb4-7679-43be-b51a-f7dbc9de1d22)
- Last but not least, we will find a gesture list where every gesture is listed and people can search for gestures and take help from the video card to learn about the gesture:
![Screenshot 2024-01-18 001430](https://github.com/Maliha-Zaman/GRS/assets/95127037/54bcada1-128f-48a6-8e99-923814d0da41)


## Contributing
- **Mohammad Ittehad Rahman Sami**
- **Maliha Zaman Pushpita**
- **Tamim Afnan**

