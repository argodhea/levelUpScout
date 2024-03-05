<a name="design-top"></a>



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/argodhea">
    <img src="static/logo_pramuka.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Level Up! SCOUT</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/argodhea"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_argodhea/LevelUpScout">View Demo</a>
    ·
    <a href="https://github.com/github_argodhea/LevelUpScout/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_argodhea/LevelUpScout/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#beginning-ideas">Beginning Ideas</a>
      <ul>
        <li><a href="#back-end">Back-End</a></li>
      </ul>
    </li>
    <li><a href="#front-ned">Front-End</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- Beginning Ideas -->
## Beginning Ideas

[![LevelUp! SCOUT]](/screenshoot/welcome_page.jpg)
[LevelUp! SCOUT](https://youtu.be/ZMrU5Imdye4)

This website was inspired by the activity of indonesian scout members who need to make a long line just to validate their level requirements to their scout master. So this website aims to let the Indonesian Scout members to track their advancement records in order to pursue certain levels online. Ratna and I all had the idea to execute this website to meet the needs.`scout`, `Indonesia Scout`, `Scout requirements`, `Scout level`, `Badges`, `email`, `Level Up! SCOUT`, `a website`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Back-End

### SQL and JAVASCRIPT
The first few stages of development consisted of implementing an effective database system. To achieve functionality, we set up five tables:
- users: id, username, password, is_scoutmaster
- user_progress: id, user_id, ramu_progress, rakit_progress, terap_progress
- scout: id, ramu_completed, rakit_completed, terap_completed, user_id
- level_requirements: id, level, requirement
- badges: id, user_id, badge_name

in our table, the only table that works is users table. In users table, we are able to store data from user login activity. So we can proceed to the next step, which render to member homepage. Then, user_progress, scout, level_requirements tables are aimed to store users' progress through the requirements that have been checklisted.  However, this table are not working because we still face difficulty to connect the logic in app.py. Once those tables work properly, we can implement storing data and the badges table can be use to show users' badges after users achieve certain level.

### PYTHON and FLASK
in the app.py file, the app routes implemented are detailed as follow:
- /home: to render to home.html
- /login: to implement the types of user (scout member or scout master) and ask user to login. It handles POST
- /scout_home: to render member's homepage with progress and badge detail
- /scoutmaster_home: to render scout master's homepage with scout member visual achievement
- /delete_scout_member: to delete scout member from the website. it handles POST
- /logout: to clear session or perform other logout-related tasks and then redirect to the login page
- /save_progress: to save scout member's progress after checklist the requirement. it handles POST

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Front End -->
## Front-End


### HTML and CSS
for a tree view of all our functional pages and their accessibility, see below:

- !DOCTYPE html
  - html (lang="en")
    - head
      - meta charset="UTF-8"
      - meta name="viewport" content="width=device-width, initial-scale=1.0"
      - title "Login - Level Up! SCOUT"
      - link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
      - link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}"
      - link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap"
      - link href="/static/favicon.ico" rel="icon"
    - body
      - nav class="navbar navbar-expand-lg navbar-light bg-light"
        - a class="navbar-brand" href="{{ url_for('home') }}" "Level Up! SCOUT"
        - button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"
          - span class="navbar-toggler-icon"
        - div class="collapse navbar-collapse" id="navbarNav"
          - ul class="navbar-nav ml-auto"
            - (Add more navigation items if needed)
      - div class="container mt-5"
        - div class="row justify-content-center"
          - div class="col-md-6"
            - div class="card"
              - div class="card-body"
                - h1 class="card-title text-center" "Login"
                - {% with messages = get_flashed_messages() %}
                    - {% if messages %}
                        - div class="alert alert-danger" role="alert"
                          - {% for message in messages %}
                              - {{ message }}
                  - {% endif %}
              - form id="loginForm" method="post" action="{{ url_for('login') }}"
                - div class="form-group"
                  - label for="username" "Username:"
                  - input type="text" class="form-control" id="username" name="username" required
                - div class="form-group"
                  - label for="password" "Password:"
                  - input type="password" class="form-control" id="password" name="password" required
                - div class="form-group"
                  - label for="userType" "Login as:"
                  - select class="form-control" id="userType" name="user_type" required
                    - option value="scout" "Scout Member"
                    - option value="scoutmaster" "Scoutmaster"
                - button type="submit" class="btn btn-primary btn-block" "Login"
      - script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
      - script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"
      - script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
      
<!-- CONTACT -->
## Author

Ratna Siti Nurhayati - [ratna56ipa@gmail.com](ratna56ipa@gmail.com)
Argo Dhea Galuh Kirana Ardyny - [argodhea.smpn56@gmail.com](argodhea.smpn56@gmail.com)

Project Link: [https://github.com/argodhea](https://github.com/argodhea)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
