# CPSC 449 - Project 1: HTTP Clients and Web Servers

## Group Members:

Chaney Chantipaporn

Nhat Nguyen

Tony Nguyen

## Project Requirements
This project will run in Tuffix 2020 using Pythin 3.8.10. 

Visual Studio Code is reccomended but not required.

## Project Description
In this project we are using Python and the HTTP protocol to implement an HTTP client and server. The purpose of this project is to build a version of the FOAAS service which provides the same HTML pages as the original service, but uses language suitable for a professional environment. To accomplish this, the requested URL from FOAAS is retreived and passes its outputs through the PurgoMalum service in order to render the text work-appropriate before returning it to the user as HTML. In addition, a custom HTTP handler is implemented in order to generate the corresponding HTML for users to include in company chats.

## How to Run the Program
To run redact.py, in the terminal type:

python redact.py / "path in FOAAS" / "name"

Example:

python redact.py /because/John

![example 1](/Proj1/images/P1_ex1.png)

To run server.py, in the terminal type:

python server.py

Here you should see 'serving at port 8080'

![example 2](/Proj1/images/P1_ex2.png)

Next, go to your web browser and type:

localhost:8080/ "path in FOAAS" / "name"

Example:

localhost:8080/because/John

The webpage should look like this image below:

![example 3](/Proj1/images/P1_ex3.png)
