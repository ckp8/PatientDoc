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
