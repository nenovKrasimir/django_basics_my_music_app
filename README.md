<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
</head>
<body>
  <h1>Django Basic Music Application</h1>
  <h2> How to run </h2>
    <details><summary>Running the project</summary><ol>
  <li>Make sure you have Django installed. If not, you can install it by running:</li>
    <pre><code>pip install django</code></pre>
   <li>Clone the project repository:</li>
  <pre><code>git clone &lt;repository-url&gt;</code></pre>
   <li>Navigate to the project directory:</li>
  <pre><code>cd &lt;project-directory&gt;</code></pre>

  <li>Set up a virtual environment (optional):</li>
 
  <pre><code> <-- On Windows -->
  
    python -m venv venv
    venv\Scripts\activate</pre></code>
  <pre><code>
   <-- On macOS/Linux -->
   
    python3 -m venv venv
    source venv/bin/activate
  </code></pre>
   <li>Configure the database:</li>
  <pre><code>
    Open the `settings.py` file in your project directory. -->
    Modify the database settings according to your setup (engine, host, port, username, password, database name). -->
  </code></pre>

  <li>Apply database migrations:</li>
  <pre><code>python manage.py migrate</code></pre>

  <li>Start the development server:</li>
  <pre><code>python manage.py runserver</code></pre>

  <li>Open your web browser and visit <a href="http://localhost:8000">http://localhost:8000</a> or the URL specified by the Django development server.</li>
</ol>
</details>

  <h2>Project Overview</h2>
  <p>This project is a very basic template project developed as part of my education in <a href="https://softuni.bg/">Software University</a> on Django web basics. It is a music application that allows users to manage albums and profiles, the main porpouse is getting comfortable with working with models, forms and views.</p>
  
  <h2>Project Pages</h2>

<div align="center">
  <p align="center">Home Page - No Profile</p>
  <p allign='center'><a href='http://localhost:8000/'>http://localhost:8000/</a></p>
  <a href="https://ibb.co/ydHJjRk">
    <img src="https://i.ibb.co/n6xSJ01/home-no-profile.png" alt="home-no-profile" border="0">
  </a>
   
  <p allign="center">Home Page - With Profile</p>
   <p allign='center'><a href='http://localhost:8000/'>http://localhost:8000/</a></p>
  <a href="https://ibb.co/HDq6wfR"><img src="https://i.ibb.co/QFMLS3h/home.png" alt="home" border="0"></a>
  
  <p allign="center">Profile Details</p>
   <p allign='center'><a href='http://localhost:8000/profile/details'>http://localhost:8000/profile/details/</a></p>
  <a href="https://ibb.co/BZdmy9d"><img src="https://i.ibb.co/85TJrHT/profile.png" alt="profile" border="0"></a>
  
  <p allign="center">Profile Delete</p>
   <p allign='center'><a href='http://localhost:8000/profile/delete'>http://localhost:8000/profile/delete/</a></p>
  <a href="https://ibb.co/qJSC6KW"><img src="https://i.ibb.co/ph7QqcR/delete-profile.png" alt="delete-profile" border="0"></a>
  
  <p allign="center">Album Add</p>
   <p allign='center'><a href='http://localhost:8000/album/add/'>http://localhost:8000/album/add/</a></p>
<a href="https://ibb.co/DCVbwG0"><img src="https://i.ibb.co/QNbcY8y/album-details.png" alt="album-details" border="0"></a>
  
  <p allign="center">Album Details</p>
   <p allign='center'><a href='http://localhost:8000/album/details/1'>http://localhost:8000/album/details/int:pk/</a></p>
<a href="https://ibb.co/z5Hy7YB"><img src="https://i.ibb.co/mBFLXw2/album-add.png" alt="album-add" border="0"></a>
     
  <p allign="center">Album Delete</p>
   <p allign='center'><a href='http://localhost:8000/album/delete/1'>http://localhost:8000/album/delete/int:pk/</a></p>
<a href="https://ibb.co/Y87fVfN"><img src="https://i.ibb.co/S0XVZV6/album-delete.png" alt="album-delete" border="0"></a>
</div>
      
      
