### PROJECT NAME
Techland
### DESCRIPTION
This is an application that allows the user to login and verified information/inspiration/advice about the tech space, this information will be in the form of videos, audio, or articles/blogs created by the Moringa school community.
### REQUIRED FEATURES 
* Django-rest framework
* Psycopg2
### ADDITIONAL FEATURES 
* Uploadcare
* Decouple
### PREREQUISITES
* Python3.6 
* Virtual Environment
* Django3
* Django-RESTful
### TECHNOLOGIES & LANGUAGES 
Project management (Agile) https://www.pivotaltracker.com

Version control (Git) https://git-scm.com/

Version control (Python) https://www.python.org/
### INSTALLATION AND SETUP
Clone the repository below

    git clone https://github.com/{username}/{repo_name}.git


Create and activate a virtual environment

    virtualenv venv --python=python3.6

    source venv/bin/activate

Install required Dependencies

    pip install -r requirements.txt

Copy environment variable

    cp env.sample .env

Load/refresh .environment variables  

    source .env

Running the application 

     python manage.py server

### ENDPOINTS AVAILABLE 
| Method | Endpoint                        | Parameters                 |Description                           |     
| ------ | ------------------------------- |-------------------------   | -------------------------------------|
| POST   |        /auth/login              |      --------              | log in user                          |   
| POST   |        /auth/register/          |      --------              | register user                        |                             | GET    |        /api/comments/           |type=post&id=ID             | get comments to a particular post    |
| POST   |        /api/comments/create/    |type=post&id=ID&parent_id=0 | create comment              
| POST   |        posts/api/posts/         |       --------             | displays all posts
| POST   |        posts/api/posts/         |       --------             | creates a post                
| GET    |  posts/api/posts/<int:pk>/      |       --------             | retrieves a post using primary key                
| PUT    |  posts/api/posts/<int:pk>/      |       --------             | updates a post            
| DELETE |  posts/api/posts/<int:pk>/      |       --------             | deletes a post
| GET    |  posts/api/categories/          |       --------             | displays all categories          
| POST   |  posts/api/categories/          |       --------             | creates a category              
| GET    |  posts/api/categories/<int:pk>/ |       --------             | retrieves a category using primary key              
| PUT    |  posts/api/categories/<int:pk>/ |       --------             | updates a category
| DELETE |  posts/api/categories /<int:pk>/|       --------             | deletes a category               
| GET    |        auth/api/profiles/       |       --------             | displays all profiles                                
| GET    |  auth/api/profiles/<int:pk>     |       --------             | retrieves a particular profile              
| PUT    |  auth/api/profiles/<int:pk>     |       --------             | updates a profile                  
| GET    |posts/api/wishlist-detail/<int:pk>|                           | views a wishlist using primarey key
| DELETE |posts/api/wishlist-detail/<int:pk>|                           | delete a wishlist
| PUT    |posts/api/wishlist-detail/<int:pk>|                           | updates a wishlist
| GET    |  posts/api/wishlists/            |                           | views a wishlist 
| POST   |  posts/api/wishlists/            |                           | ceates a wishlist


 
### LICENSE
MIT