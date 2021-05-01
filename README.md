# Training-AIHomework
Objective: A script that can query a rest API, parse, and return the output.
After cloning the code Just follow below steps

cd MAC_rest_call
#Build the docker Image

docker build -t pythonapp .
Run the Docker Image
docker run -t -i pythonapp

Then it will promts the user to enter Mac address and Authentication Token

Note: Mac address will accept in these two formats 44:38:39:ff:ef:57 and 44-38-39-ff-ef-57

Note: Enter the inputs when it prompts (Mac Address and Token) If you dont know the Mac Address and Token just press Enter, it will take the default Values of Mac address and token and it will query accordingly and outputs the companyName for that Mac Address.

Objective: 2 service Compose application. Service 1 should be able to send HTTP requests to any URL on the internet. Service 2 should be a basic pingable REST application.
docker-compose up
