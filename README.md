# SMS SPAM-HAM Classifier Deployment Branch
This is a repository for deploying SMS Spam/Ham Classifier project in Heroku Cloud. You will find the code in [main](https://github.com/Pratik872/NLP/tree/main/E2EProject/SMSClassifier) branch.

This project is deployed at heroku. Check [here](https://sms-classifier-deploy.herokuapp.com/)

## Contents

- ### Folder Structure for Deployment : 

	Some files added for deployment to the existing files which are present in [main](https://github.com/Pratik872/NLP/tree/main/E2EProject/SMSClassifier) branch folder structure are:

	- Procfile : This is basically the file in which you have to mention the Flask application initialized and in which file it is initialised

	- requirements.txt : This file is already present in the 'main' branch folder structure. This file is required for dockerisation of the application and also to deploy it on heroku. While deploying the application on Heroku, this file gets triggered and all the dependencies are downloaded.