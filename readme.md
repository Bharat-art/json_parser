Project Title

json parser: 

These app will display the data submitted by user in json format.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

clone or download from github Repository. www.github.com/Bharat-art

Extract file and give move that folder in "/var/www"

Read write permission to folder. sudo chmod 777 json_parser

cd json_parser

find manage.py and run command

sudo python3 manage.py runserver

http://127.0.0.1:8000/ copy these link and open in your local browser.

### Prerequisites

sudo apt install python3.5

Django 2.7

### Installing

clone or download from github Repository. www.github.com/Bharat-art

Extract file and give move that folder in "/var/www"

Read write permission to folder. sudo chmod 777 json_parser

cd json_parser

find manage.py and run command

sudo python3 manage.py runserver

http://127.0.0.1:8000/ copy these link and open in your local browser.

After submittiong the data you will see json formatted data for example:


{
    "model": "json_demo.userdetails",
    "pk": 6,
    "fields": {
        "real_name": "Bharat Pamnani",
        "tz": "Bhopal",
        "start_time": "2020-06-26T14:24:41Z",
        "end_time": "2020-06-26T14:24:41Z"
    }
},
{
    "model": "json_demo.userdetails",
    "pk": 7,
    "fields": {
        "real_name": "Bharat Pamnani",
        "tz": "Bhopal",
        "start_time": "2020-06-26T14:47:51Z",
        "end_time": "2020-06-26T14:47:51Z"
    }
}
]

## Deployment

Instruction for Deploying on pythonanywhere.com

1) If you already deploy in on gihub it will be easy otherwise follow the instruction to deploy on github first.

sudo apt-get install git

on Ubuntu or Mint distros.

Then, login to your Github account and create a new repository, name the repository and add a readme file.

Open terminal and cd to your project directory (to the root of your project).

If you have already initialized this directory as a git repository and you already have all the changes committed locally then do nothing else in terminal type:

git init

This initializes a git repository in your project folder. Then type:

git add . 

'dot' (.) is used to add all files in a directory to a repository. Then type:

git commit -m "some meaningful message goes here"

messages are used to know about what new changes are committed.

Next type in terminal:

git remote add origin https://github.com/your-user-name/name-that-you-gave-to-repository.git 

This creates a remote, named “origin”pointing at the GitHub repository you just created.

This step is sometimes necessary.
Type in terminal:

git pull origin master

Next type in terminal:

git push -u origin master

Then it will ask for your username and password. After you have given correct username and password, your files will be pushed to your Github repository.

Afterwards, for every change(s) you make, you have to add and commit such changes. Then do:

git push

This will push all your changes to your Github repository.

######### After Deploying on Github you can sart with python anywhere ##################

Make sure you have google account which is not register in pythonanywhere

visit www.pythonanywhere.com

In top right corner click on account

Then click on API Token and create new api token for your website

Now visit pythonanywhere.com Dashboard and open Bash command Prompt

Type that command

pip3.6 install --user pythonanywhere

once its successfully done you can see output something like these

Successfully installed (...) pythonanywhere- (...)

Now type that command

pa_autoconfigure_django.py --python=3.6 https://github.com/<your-github-username>/my-first-blog.git


Your username name authentication required of github.

If you want you can create superuser also:

python manage.py createsuperuser

########## End ############################

## Version

Python 3.5
Django 2.7

## Authors

Bharat Pamnani

## License

This project is Dummy of json parser where we can display the user data in json object.

## Acknowledgments

* https://docs.djangoproject.com/en/3.0/
 
## Contact 

If you face any issue at any point in the project please email with screenshot on bharatpamnani53@gmail.com
or you can visit my website https://pythonmyworld.pythonanywhere.com.

Thanks.



