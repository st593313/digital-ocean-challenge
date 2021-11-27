# Deploy scalable NoSQL database cluster
   Created a NoSQL cluster of MongoDB and a python flask backend service (kind of API service) to take the information from user and perform CRUD operations according to the 
   user's need. And then used all the resources to make a PC Software to create a Task Manager which save, Delete and Update Tasks.
  
## Requirements
     - Docker
     - Kubernetes
     - Flask
     - Flask-PyMongo (for conencting MongoDB using python)
     - Python
     
## Prerequisites
  
  - Created a Kubernets cluster on Digital Ocean  panal.
  - Install Kubectl to deploy and access the Kubernetes services.
  - Install Docker to create containers.
  - Install Doctl and helm.
  
## Steps
  - Created a Python-Flask file to make operations on MongoDB database.
  - Created a MongoDB image of docker.
  - Deployed both Flask and MongoDB images on Kubernetes (IP's and other details are invisible for security reasons):
   
      ![Screenshot (572)_LI](https://user-images.githubusercontent.com/90840830/143685329-e271525b-3c94-4736-9410-8f6b0ec355a1.jpg)
      ![Screenshot (573)](https://user-images.githubusercontent.com/90840830/143685528-e8ed50b0-fb88-4d2d-987d-cf26e91c40e2.png)
      ![Screenshot (574)](https://user-images.githubusercontent.com/90840830/143685532-17f25322-57d5-48bc-8d1b-ecf48208bab2.png)


  - Now Access all resources in my PC software created with python (See the screenshots for demo).
  
    ![Screenshot (567)](https://user-images.githubusercontent.com/90840830/143685385-6a794ac3-1434-4279-a816-639f40b45157.png)
    ![Screenshot (568)](https://user-images.githubusercontent.com/90840830/143685396-9093c027-c37b-4340-8705-cc2bed709a2f.png)
    ![Screenshot (569)](https://user-images.githubusercontent.com/90840830/143685398-ce5d5056-50fa-431c-ac6f-4a8756587a95.png)
    ![Screenshot (570)](https://user-images.githubusercontent.com/90840830/143685399-c2f852cc-bcad-42f0-b900-2b60dbccf07d.png)
    ![Screenshot (571)](https://user-images.githubusercontent.com/90840830/143685662-9032f171-4639-4f18-84e6-e49684376e60.png)

  
  - Now I created a Task Manager Software that where we can save Tasks, Delete them when finishes and Update them accordingly.
  - All the operations are done on that Software are done by sending request to the Flask App and then they can be done on MongoDb database 
    running on Kubernetes.
    
  
# Attached a Python script for my Task Manager Software that i have created to save tasks. Url is Hidden for security reasons.

  
  
 






