DevOps FastAPI Project

DevOps FastAPI Project
======================

Overview
--------

This project is a foundational FastAPI application for experimenting with DevOps tools and practices. It's aimed at
facilitating the integration of DevOps methodologies in a Python environment, serving as a learning and testing base for
DevOps enthusiasts and professionals.

Goals
-----

* Establish a base for DevOps project testing.
* Integrate various DevOps tools and practices.
* Foster learning in DevOps within a Python setting.

Getting Started
---------------

### Prerequisites

* Python 3.x
* Docker (for containerization)

### Installation

Clone the repo:

    git clone https://github.com/maxiplux/api-python-project-devops-fast-api.git

Install dependencies:

    pip install -r requirements.txt

### Running the App

Locally:

    uvicorn main:app --reload

Using Docker:

    docker build -t fastapi-devops .
    docker run -p 8000:8000 -e DB_USERNAME=your_username -e DB_PASSWORD=your_password -e DB_HOST=your_host -e DB_NAME=your_db_name fastapi-devops

#Video with the answer to project 4:
## https://www.youtube.com/watch?v=03fnj4TSAwI
    




Contributing
------------

Feel free to fork, modify, and send a pull request. Contributions are welcome!

License
-------

[MIT License](LICENSE)

Contact
-------

Your Name  
maxiplux@gmail.com
