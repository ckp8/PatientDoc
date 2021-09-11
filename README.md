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
As seen above, I have implemented 2 tables which share a one to many relationship. Which allow users to make an appointment (create functionality), change their appointment (update functionality), view their appointments(read functionality), and cancel their appointments (delete functionality). The database for this MVP for this project comprimises of a patients table and an appointments table. With each patient having multiple appointments (one-to-many relationship)


