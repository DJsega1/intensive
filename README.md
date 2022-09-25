# Getting started
___
**Open your cmd, then clone the project**  
```
cd *your_directory*
git clone https://github.com/DJsega1/intensive.git
cd intensive
```  

**Create and start a virtual environment**  
```
python -m venv venv
venv\Scripts\activate.bat
```

**Install the project dependencies**  
```
pip install -r requirements.txt
```

**To start the development server on**  
```
python manage.py runserver
```  
The project starts on **127.0.0.1:8000** by default.  
If you want to change that, read the docs:  
https://docs.djangoproject.com/en/4.1/ref/django-admin/#runserver  
**Press Ctrl+C in order to stop the server.**