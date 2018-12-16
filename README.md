# INSTAGRAM.

This is  an application that represents the famous photo app,Where people can add follow and even comment on other peoples post.

## Getting Started.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

* $ git clone https://github.com/theonilatash/insta/
* $ cd gramzone
* $ source virtual/bin/activate

Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
* $ configure your prefered database provider in the settings.
* $ ./manager.py check
* $ ./manager.py makemigrations stazone
* $ ./manager.py migrate
* $./manager.py runserver

### As a user of the application I should be able to:

* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display  images | **Home page** | Clickable links to open any images in a modal |
| Display single images on click | **On  signup** | All details should be viewed|
| To add an image  | **Through Admin dashboard** |  add  Image|
| To edit image  | **Through Admin dashboard** | Redirected to the  image form details and editing happens|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test images

## Technologies Used
* Python3. /Django
* postgresql
* Bootstrap4

## License

Copyright (c) 2018 Theonilah Owali

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.