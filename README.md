# PatientDoc

The project brief required us to design and develop a web application of our choice. The app was required to carry out CRUD functionality (create,read,update, and delete data). We were required to use Flask micro framework to develop this application, and required to use MySQL to store data. I have 2 tables sharing a one to many relationship.

## Requirements
• Trello board <br>
• Relational database, consisting of atleast 2 tables sharing a one to many relationship <br>
• documentation of app architecure and risk assessment <br>
• Flask <br>
• Pytest <br>
• Jinja <br>
• Jenkins <br>

## The built application
To fulfull the requirements, I produced an application which allows users to create/delete/update and view their appointments. One patient can have many appointments (one to many relationship
• The user will  be able to <br>
••register using their name and date of birth <br>
••Make an appointment <br>
•• delete an appointment <br>
•• update an appointment <br>

# Architecture
## The Database
![Screenshot 2021-09-11 at 19 56 42](https://user-images.githubusercontent.com/43785332/132958487-d4217d1d-1bba-461c-890e-62e8ad81f678.png)


As seen above, I have implemented 2 tables which share a one to many relationship. The application allows users to make an appointment (create functionality), change their appointment (update functionality), view their appointment(read functionality), and cancel their appointments (delete functionality). The database for the MVP for this project comprimises of a patients table and  appointments table. With each patient having multiple appointments (one-to-many relationship)

# CI Pipeline 
In addition to the above requirements, the project required the implementation of several stages of a typical CI pipeline. Such as project tracking, development environment and build server and version control. To track my project I used a trello board where I priortised each task using the MoSCoW prioritisation.
![Screenshot 2021-09-11 at 20 44 16](https://user-images.githubusercontent.com/43785332/132959705-9f67b99c-3c42-492e-891b-b036a9d483ff.png)


Above you can see my trello board mid-week. I have assigned story points to each of my user stories, in regards to how difficult each task may be relative to eachother.

* user stories - Any functionality which is added to the project starts out as a user story. This helps keep every element of software development focused on user experience <br>
* Project Backlog -  The list of tasks required to do to complete this project <br>
* Sprint backlog - set of tasks to complete in a given sprint. <br>
* In progress- current set of tasks being worked on <br>
* completed - the code and functionalites being completed.(DoD - acceptance criteria met, unit tests passed) <br>


For version control, I used git. The project reposistory was hosted on github.Version control via git allows changes to the project to be made and committed whilst keeping the commit history for access to earlier version. Github also allows the use of  webhooks which sends POST http requests to the build server to automate tests and build.

I used development environment used was Python virtual environment (venv). I used Flask which required me to use Python as flask is python-based. I used Python virtual environment as it allows for pip installs, as well as allowing the app to be run without any conflict with pip installs on the same machone

# Testing
Pytest was used to run the unit tests on this application. With unit testing you are required to test small 'units' of code, with a known output. 
• Unit tests were written for the key functionalties such as "Read','Write','Update and 'Delete', As well as some html pages to much sure they were rendering back the templates. I used jenkins to automate the unit tests via webhooks <br>
• Intergation testing tests the function of the app in an live environment.

![Screenshot 2021-09-13 at 08 46 43](https://user-images.githubusercontent.com/43785332/133044318-5acae765-eb64-47cf-9881-31fd76b075cb.png)



The coverage report highlights the percentage of tests covered.All tests must pass for the build to be successful otherwise the build will fail.

# Risk Assessment.
Some of the  measures were implemented in the project following the risk assessment.
• Users were not asked any sensitive data <br>
• regular pushes to github in case the VM goes down <br>
![Screenshot 2021-09-12 at 19 13 12](https://user-images.githubusercontent.com/43785332/132998263-ad2ac8fd-677b-418d-a319-a415051cc55f.png)


Here is a image of a risk assessment which was carried out at the start of the project.
• risk of jenkins going down is low, but the severity of harm would be high

# The App

![Screenshot 2021-09-12 at 19 16 44](https://user-images.githubusercontent.com/43785332/132998399-5f975050-15c0-4135-90c9-8041cfa9e18c.png)

The image above displays a easy to read and navigate homepage. Where the user will be able to either register/create appointment or delete and update an appointment.

![Screenshot 2021-09-12 at 19 16 53](https://user-images.githubusercontent.com/43785332/132998474-1c870b36-24df-4f36-b6d3-857f8dcb777c.png)

Before a user will be allowed to create an appointment, they will have to create an account and be registered at the "GP practice".

Once this has been done, the user will be able to create an appointment entering in their unique user ID which they will be able to retrieve on the views page.


![Screenshot 2021-09-12 at 19 17 02](https://user-images.githubusercontent.com/43785332/132998546-9dccd6a5-88c9-4b13-9b86-6882753c177d.png)


Using this ID the user will also be able to update and delete their appointment. Every user will be given a unique ID.

# Future Improvements

There are a number of improvements I would like to implement to improve this application.

• Implementation of a login and authentication system. This will allow for greater security <br>
• Make the front-end more aesthetically pleasing, by using bootstrap and css <br>
• ![48cd9d52-ccd1-425c-86b3-636eb32ad879](https://user-images.githubusercontent.com/43785332/132998836-3878098c-28cc-413d-b6e6-74511908cb01.jpg)<br>
To make this app more functional, I would implement more relations and database tables.<br>
• Having a online chat system, for users experiencing problems







