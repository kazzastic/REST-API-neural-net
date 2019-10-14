# REST-API-neural-net

### What is this?
This is a project I made under the supervision of RCAI lab as my internship project. This project is the implementation of a deep neural network
which can classify the images of NIC building and White-House building which are some of the most famous buildings in NED-UET. Basically this DNN
is the living example of the fact that a DNN can be trained for building/offices structures which look very mediocre and not so unique in their own 
look wise. Even after the mediocrity of building and structures being quite similar, the DNN can be implemented to classify each from the other. 
Another thing that the model was trained on 600 original pictures, which were then augmented to make about 4800 pictures each class. 

### How was this made?
This was made with tears and sweat. Basically this DNN was implemented using tensorflow as the backend and keras methods in order to build the DNN layers. The DNN layers studies and chosen from various classification models and this resulted in a model which is under 60 MB memory. 

#### Layers 
![alt text](https://github.com/kazzastic/REST-API-neural-net/blob/master/misc/Screenshot%20from%202019-10-15%2002-04-04.png)

#### Architecture
The DNN can be further visualized as here,
![alt text](https://github.com/kazzastic/REST-API-neural-net/blob/master/misc/nn.svg)

### Deployment 
This model was deployed as a flask web app on heroku.
can be found [here](https://ned-net.herokuapp.com/) 

### Future
This model can be further expanded by adding building and navigation for entire NED landmarks and buildings!

