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

[![LevelUp! SCOUT]](/screenshoot/welcome_page.gif)

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
the "user" table, through the login.html, allow the web app to get username and password data from the user and store it into the database. The "scout" table through

### PYTHON and FLASK
in the app.py file, the app routes implemented are detailed as follow:
- /home: to render to home.html
- /login: to implement the types of user (scout member or scout master) and ask user to login
- /scout_home: to render member's homepage with progress and badge detail
- /scoutmaster_home: to render scout master's homepage with scout member visual achievement
- /delete_scout_member: to delete scout member from the website
- /logout: to clear session or perform other logout-related tasks and then redirect to the login page
- /save_progress: to save scout member's progress

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Front End -->
## Front-End


### HTML and CSS
for a tree view of all our functional pages and their accessibility, see below:
- DOCTYPE html
- html (lang="en")
- head
    - meta charset="UTF-8"
    - meta name="viewport" content="width=device-width, initial-scale=1.0"
    - title "Level Up! SCOUT - Scout Home"
    - link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
    - link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}"
    - link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap"
    - link href="/static/favicon.ico" rel="icon"
    - style
        - body
- div class="container mt-5"
  - nav
    - ul
        - li
        - a href="#" class="btn btn-outline-danger" onclick="confirmLogout()" "Logout"
  - div class="row"
    - div class="col-md-12"
        - div class="card"
            - div class="card-body"
                - h2 class="card-title" "Welcome, {{ username }}!"
                - p class="card-text" "Track your advancement records and achieve new levels on Level Up! SCOUT."
  - div class="row mt-4"
    - div class="col-md-4"
        - div class="card"
            - div class="card-body"
                - h3 class="card-title" "Ramu (Level 1)"
                - p class="card-text" "Progress: "
                - div class="progress"
                  - div role="progressbar" style="width: 0%;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"
                - button class="btn btn-secondary requirements-button" "List of RAMU's requirements"
                - div class="modal fade" id="ramuModal" tabindex="-1" aria-labelledby="ramuModalLabel" aria-hidden="true"
                  - div class="modal-dialog"
                      - div class="modal-content"
                        - div class="modal-header"
                            - h5 class="modal-title" "List of RAMU's Requirements"
                      - div class="modal-body"
                      - div class="modal-footer"
                - button id="ramu-button" class="btn btn-primary requirements-button" "View Requirements"
              - div id="ramu-requirements-list" class="requirements-list" style="display: none;"
                - h4 "Requirements:"
                  - ul class="requirements-list"
                    - li class="requirements-list-item"
                      - div class="form-check"
                      - input type="checkbox" id="ramu-requirement1"
                        - label for="ramu-requirement1" "01"
                    - div class="form-check"
                      - input type="checkbox" id="ramu-requirement2"
                      - label for="ramu-requirement2" "02"
          - button class="btn btn-primary requirements-button" "Save Progress"
- script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
- script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"
- script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
- script ()

<!-- CONTACT -->
## Author

Ratna Siti Nurhayati - [ratna56ipa@gmail.com](ratna56ipa@gmail.com)
Argo Dhea Galuh Kirana Ardyny - [argodhea.smpn56@gmail.com](argodhea.smpn56@gmail.com)

Project Link: [https://github.com/argodhea](https://github.com/argodhea)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

