# Culture Club

'Culture Club' is a vibrant web platform where cultural passions come alive. Designed for lovers of music, movies, books, and podcasts, this is a space where users share, discover, and celebrate the spectrum of cultural arts. It's more than just a website; it's a community where your favorite songs, films, stories, and discussions create a tapestry of shared experiences.
At "Culture Club," users create personalized profiles to showcase their cultural tastes, from the rhythm of music to the allure of cinema, the depth of literature, and the intrigue of podcasts. Interact with fellow enthusiasts, exchange recommendations, and stay updated on new posts.
Inspired by the diversity and unity of the iconic band it's named after, 'Culture Club' is where every melody, scene, story, and voice contributes to the rich, collective journey of cultural exploration. Join us in a world where your cultural explorations know no bounds.

<center> 

![Mockup image](/docs/readme.md/FILENAME) 

</center>


Developer: [Debbie Bergström](https://github.com/DebbieBergstrom) <br>
[Live webpage](https://WEBADDRESS)<br>
[Project Repository](https://github.com/DebbieBergstrom/Culture-Club)<br>


![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=for-the-badge)
![Gitpod Badge](https://img.shields.io/badge/Gitpod-FFAE33?logo=gitpod&logoColor=fff&style=for-the-badge)
![Git Badge](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=for-the-badge)
![Heroku Badge](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=fff&style=for-the-badge)
![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=for-the-badge)

![HTML5 Badge](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=for-the-badge)
![CSS3 Badge](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=fff&style=for-the-badge)
![JSS Badge](https://img.shields.io/badge/JSS-F7DF1E?logo=jss&logoColor=000&style=for-the-badge)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![Markdown Badge](https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=for-the-badge)

![Bootstrap Badge](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=fff&style=for-the-badge)
![Django Badge](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=fff&style=for-the-badge)

---

## Table of Content

- [Project Goals](#project-goals)
    + [User Goals](#user-goals)
    + [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    + [Target Audience](#target-audience)
    + [User Requirements and Expectations](#user-requirements-and-expectations)
    + [User Stories](#user-stories)
      - [Epic 1: User Experience (Visitor)](#epic-1--user-experience--visitor-)
      - [Epic 2: User Engagement and Interaction (Registered User)](#epic-2--user-engagement-and-interaction--registered-user-)
      - [Epic 3: Administration and Content Management (Admin/Content Moderator)](#epic-3--administration-and-content-management--admin-content-moderator-)
- [Database](#database)
    + [Blog Application Database Schema](#blog-application-database-schema)
      - [CultureCategory Table](#culturecategory-table)
      - [UserProfile Table](#userprofile-table)
      - [User Table](#user-table)
      - [Post Table](#post-table)
      - [Comment Table](#comment-table)
- [Design](#design)
    + [Design Choices](#design-choices)
    + [Color](#color)
    + [Fonts](#fonts)
    + [Structure](#structure)
      - [Before User logs in:](#before-user-logs-in-)
      - [After User logged in:](#after-user-logged-in-)
      - [Profile Navigation:](#profile-navigation-)
    + [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Frameworks](#frameworks)
    + [Database](#database-1)
    + [Media management platform](#media-management-platform)
    + [Tools](#tools)
    + [Supporting Libraries and Packages](#supporting-libraries-and-packages)
- [Methodology](#methodology)
    + [Agile Project Management with GitHub Projects](#agile-project-management-with-github-projects)
    + [User Stories as GitHub Issues](#user-stories-as-github-issues)
    + [Bug Tracking for Seamless Development](#bug-tracking-for-seamless-development)
    + [Iterative Development Approach](#iterative-development-approach)
    + [Future Backlog and Progress](#future-backlog-and-progress)
- [Features](#features)
    + [Landing Page:](#landing-page-)
    + [Other Pages:](#other-pages-)
    + [User Account Management:](#user-account-management-)
    + [Navigation:](#navigation-)
    + [Future Features](#future-features)
- [Testing](#testing)
- [Bugs](#bugs)
    + [Known bugs](#known-bugs)
    + [Fixed bugs](#fixed-bugs)
- [Deployment](#deployment)
    + [App Deployment](#app-deployment)
    + [Cloudinary](#cloudinary)
    + [Version Control](#version-control)
    + [Forking the Repository:](#forking-the-repository-)
    + [Clone of the Repository:](#clone-of-the-repository-)
- [Credits](#credits)
    + [Media](#media)
    + [Django Documentation:](#django-documentation-)
    + [Bootstrap docs:](#bootstrap-docs-)
    + [Tutorials and YouTube channels:](#tutorials-and-youtube-channels-)
    + [Content](#content)
- [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


---

# Project Goals 

Culture Club is a Django web application that serves as a vibrant community platform for cultural enthusiasts to share and explore diverse cultural content including movies, books, podcasts, and music. The key objectives of the project include:

- To provide a user-friendly interface where users can easily share and discover cultural experiences.
- To foster a community of cultural exchange, where users can engage in discussions, express their opinions, and connect with like-minded individuals.
- To offer a personal space for users to curate and display their cultural interests and recommendations.
- To ensure secure and straightforward user registration, authentication, and profile management.
- To allow users to actively participate by creating content, and liking and commenting on posts.

### User Goals

- To discover and engage with content that aligns with their cultural interests.
- To find a platform that allows them to express their own cultural narratives and experiences.
- To join a community that values and fosters cultural diversity and exchange.

### Site Owner Goals

- To build a community-driven platform that encourages user interaction and content creation.
- To maintain a high standard of user experience with seamless navigation and responsive design.
- To ensure the website is a safe and welcoming space for all users to share their cultural passions.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# User Experience

### Target Audience

Culture Club is designed for the following target audience:

- Individuals passionate about various cultural domains who are looking for a space to explore and share content.
- Users seeking a platform to keep track of their cultural experiences and get recommendations from a like-minded community.
- Cultural content creators looking for an outlet to publish their work and engage with an audience.

### User Requirements and Expectations

When using Culture Club, users can expect the following features and characteristics to fulfill their needs:

- An aesthetically pleasing and intuitive interface that provides ease of navigation and content discovery.
- A secure registration and login process, ensuring user data protection and privacy.
- Interactive features such as the ability to like, comment, and create posts that facilitate community engagement.
- A personalized user profile where they can showcase their favorite cultural elements and manage their contributions.
- Access to a diverse range of cultural content and the opportunity to contribute their own insights and reviews.


### User Stories

### Epic 1: User Authentication & Profile Management
This epic focuses on user account management, including registration, login/logout, and personal profile customization.
- [User Account Registration (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/2)
- [Log In and Out of User Account (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/3)
- [Edit User Bio and Profile Picture (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/4)
- [Favourite Lists in Personal Bio (COULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/5)

### Epic 2: Blog Interaction & Content Management
This epic deals with the core functionalities of the blog, such as creating, reading, editing, and deleting posts, as well as interacting with posts through comments and likes.
- [User Create & Edit Blog Posts (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/7)
- [Comment Blog Posts + Edit (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/8)
- [Like/ Unlike Blog Posts (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/9)
- [View Other Users' Profiles (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/10)
- [See Post Overview (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/11)
- [Read Full Post Detail (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/12)
- [Save Favourite Articles (COULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/22)
- [Follow Other Users (COULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/23)

### Epic 3: Administration & Analytics
This epic encompasses administrative control over the site, including user account management and content moderation, as well as tracking user engagement.
- [Admin - Full Control Over User Accounts (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/13)
- [Admin - Review and Edit User-Submitted Articles (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/14)
- [Admin - Manage and Categorize Articles (COULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/15)
- [Admin - Track User Engagement and Analytics (COULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/16)

### Epic 4: User Experience & Accessibility
This epic is focused on the overall user experience on the site, such as the appearance of the homepage, ease of navigation, and accessibility of information.
- [Visually Appealing Landing Page (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/17)
- [Navigate to About Us (SHOULD HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/18)
- [Navigate to Join the Club Section (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/19)
- [Easy Login from Landing Page (MUST HAVE)](https://github.com/DebbieBergstrom/Culture-Club/issues/20)


<br>

The user stories and epics are organized into sprints (milestones) to establish a well-defined work structure. You can access the details of these sprints by clicking [here](https://github.com/DebbieBergstrom/Culture-Club//milestones), which will redirect you to the sprint information.

![Sprints](/docs/readme.md/FILEPATH) 

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Database
When creating the database structure schema for this project, I utilized the [dbdiagram.io](https://dbdiagram.io/) website. This online tool allowed me to visually design and document the database schema, making it easier to plan and implement the database for the blog application.

<center> 

![Database Schema image](/docs/readme.md/FILEPATH) 

</center>

### Blog Application Database Schema

#### CultureCategory Table
- Stores categories used for categorizing posts.
- Fields:  culture_category_id (primary key), name (category name), genre (category genre).

#### UserProfile Table
- Extends the User model to store additional user-specific information.
- Fields: userprofile_id (primary key), user (one-to-one relationship with the User model), first_name, last_name, profile_picture (user profile picture), bio (user bio), country (user's country).

#### User Table
- Represents user information. ( Django built In )
- Fields: user_id (primary key), username (user's name), email (user's email address), password (user's password).

#### Post Table
- Represents blog posts created by users.
- Fields: post_id (primary key), title (post title), slug (post slug), author_id (foreign key to User), update_on (post update date), content (post content), featured_image (featured image URL), excerpt (post excerpt), Created_on (post creation date), status (post status), likes (many-to-many relationship with User for post likes), category_id (foreign key to CultureCategory), genre (post genre 'MOVIES', 'BOOKS', 'MUSIC', 'PODCASTS', Charfield).

#### Comment Table
- Represents comments on blog posts.
- Fields: comment_id (primary key), post_id (foreign key to Post), name (commenter's name), email (commenter's email address), body (comment content), created_on (comment creation date), approved (comment approval status), user_id (foreign key to user model).

<br>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Design
Short description...

### Design Choices
Our design choices were made thinking of.....

### Color
short description using 60–30–10 rule for creating balanced interfaces.

![Color Palette image](/docs/FILEPATH)
**Dominant (60%):** 

Choice of a ?color?, represented by #code as the dominant color, reflects...

**Secondary (30%):** 

The secondary color, ?color?, represented by #code ...

**Accent (10%):** 

Accent color...


### Fonts
The Culture Club site embraces the default fonts offered by Bootstrap 5, without any specific alterations, as they significantly enhance the overall aesthetics and user experience.

### Structure

User-friendly structure, ensuring seamless navigation and easy access to the website's content. Here's an overview of the website's structure:

#### Before User logs in:

- **Landing Page:** The landing page... <br>
- **About Us:** The About Us page provides... <br>
- **Sign Up:** For new Users, the Join Us page is ... <br>
- **Log In:** Registered users can securely access their accounts and unlock the full potential of our website through the Log In page.<br>


#### After User logged in:
Once the User is logged in additional features is provided with the following pages:

- **Home Page (Inside the Culture Club):** This is where the latest posts are revealed! The home page of Culture Club brings the User with new exiting posts.<br>
- **Profile Page:** The Users' very own customized profile with profile picture, bio, 
- **Contact Us:** If you encounter any issues or have questions, our friendly admins are just a message away. Feel free to reach out via the "Contact Us" page, and we'll assist you with any concerns or inquiries you may have.<br>


#### Profile Navigation:

Clicking on your profile image in the navigation bar opens up access to specific profile-related features:

- **My Posts:** The "My Posts" page is ...<br>
- **Create Post:** The "Create Post" page is ...<br>
- **Log Out:** The "Log Out" button...<br>


### Wireframes
The wireframes serve as a visual blueprint for our web applicationClick on each page to view the wireframe.

<details><summary>Landing page</summary>
<img src="docs/wireframes/FILEPATH">
</details>
<details><summary>About us</summary>
<img src="docs/wireframes/FILEPATH">
</details>
<details><summary>Join the Club</summary>
<img src="docs/wireframes/FILEPATH">
</details>
<details><summary>Log In</summary>
<img src="docs/wireframes/FILEPATH">
</details>
<details><summary>Home page (Blog articles)</summary>
<img src="docs/wireframes/FILEPATH">
</details>
<details><summary>Contact us</summary>
<img src="docs/wireframes/FILEPATH">
</details>
<details><summary>My Posts(Profile)</summary>
<img src="docs/wireframes/FILEPATH">
</details>
<details><summary>Create Post</summary>
<img src="docs/wireframes/FILEPATH">
</details>
<details><summary>Blog Post View</summary>
<img src="docs/wireframes/FILEPATH">
</details>
<details><summary>Log Out</summary>
<img src="docs/wireframes/FILEPATH">
</details>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Technologies Used

### Languages
- HTML
- CSS
- Python

### Frameworks
- Django: A high-level Python web framework used for building the Culture Club web application.
- Crispy Forms: A Django package used for rendering forms in a more efficient and customizable way.
- Bootstrap v5.0: A popular CSS framework used for creating responsive and visually appealing user interfaces.

### Database
- 

### Media management platform
- Cloudinary: A cloud-based media management platform used for storing and serving images.

### Tools
- **Git**: A distributed version control system used for tracking changes in the project's source code.
- **GitHub**: A web-based hosting service for version control repositories, used for storing and managing the project's source code.
- **Gitpod**: An online integrated development environment (IDE) used for developing and testing the Culture Club project.
- **Heroku**: A cloud platform that enables deployment and hosting of web applications. Heroku was used for deploying the Culture Club project to a live server.
- **Adobe Photoshop**: A professional image editing software used for advanced image manipulation.
- **DB diagram**: An online database design and diagramming tool that simplifies the process of creating and visualizing database schemas. dbdiagram.io was used for designing and documenting the database schema of the Culture Club project.
- **Google Fonts**: A collection of free and open-source fonts used for typography on Culture Club website.
- **Font Awesome**: A library of icons used for adding scalable vector icons to Culture Clubs website.
- **Mailtrap**: In this project, Mailtrap was integrated to power the contact form, providing a secure environment for users to reach out to Culture Club via email.
- **Balsamiq



### Supporting Libraries and Packages
import list of packages from requirements.txt

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Methodology

The Culture Club project follows a methodology inspired by agile principles, fostering collaboration, flexibility, and gradual development. The outlined approach has guided the project's evolution:

### Agile Project Management with GitHub Projects
To streamline project management, GitHub Projects is employed as a central hub. User stories and tasks are structured as GitHub issues, creating an organized workflow. The GitHub project board serves as a visual representation, tracking progress effectively.

### User Stories as GitHub Issues
Transforming user stories into GitHub issues captures user-centric functionalities. These issues interlink with respective user stories, simplifying access to criteria, tasks, and discussions.

### Bug Tracking for Seamless Development
Bugs uncovered during development are documented as GitHub issues, offering insights into each bug's characteristics, impact, and reproduction steps. By hyperlinking these issues in README.md, users can stay updated on bug resolutions and contribute insights.

### Iterative Development Approach
The Culture Club project adheres to an iterative development approach, facilitating continuous enhancements within a predefined timeline. Despite its condensed schedule, the project accommodates future iterations and expansions.

### Future Backlog and Progress
The project board efficiently manages user stories, with the "Not started" column representing upcoming iterations. This backlog previews user stories set for subsequent development phases.

Emphasizing that the project timeline is expedited, the iterative approach maintains adaptability, enabling ongoing refinements and improvements aligned with evolving user needs.

**Labels and User Story Distribution (MoSCoW):**

- **Must-Have:** example 10/15
- **Should-Have:** 
- **Could-Have:** 
- **Wont-Have:**
- **Task:** 

For a comprehensive view of the project's trajectory, user stories, and bug tracking, explore the [Kanban board](https://github.com/users/DebbieBergstrom/URLPATH).
<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Features
### Landing Page:
- Desciption 
<details><summary>See Screenshot **Landingpage**</summary><img src="FILEPATH"></details>


### Other Pages:
- Desciption 
<details><summary>See Screenshot **Landingpage**</summary><img src="FILEPATH"></details>


### User Account Management:
- Desciption
<details><summary>See Screenshot **Landingpage**</summary><img src="FILEPATH"></details>


### Navigation:
- Desciption 
<details><summary>See Screenshot **Landingpage**</summary><img src="FILEPATH"></details>


### Future Features
Here are some exciting features that I would like to add to the Culture Club in the future:

- **Feature:**  
  Description


<br>


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Testing

The Culture Club website went through a comprehensive testing process to guarantee its functionality, accessibility, and performance. This included checking the code, such as code validation, accessibility assessment, performance testing, cross-device testing, verification of browser compatibility, assessment of user stories, and the integration of user feedback to enhance the overall user experience.

All testing, including both manual and automated testing, was carried out and documented in [Testing.md](TESTING.md). 

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Bugs
The bug section descriptions have been linked with the bug issues in my documentation for better visibility, added color coding, and divided the content into sections, all aimed at enhancing readability. The links are clickable for more reading and solution.

### Known bugs

| **Bug** | **Description** |
| ------- | --------------- |
| [Describe the problem.](https://github.com/DebbieBergstrom/FILEPATH) | Description. |




### Fixed bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| 1. Bug to be listed| Solutions to be fixed |


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Deployment

### App Deployment
For deploying Your app, Heroku is used. Follow these steps:

 **Create a New App:**
   - Create a new app on Heroku dashboard.

 **Configure Settings:**
   - Navigate to "Settings" in new app.

 **Config Vars Setup:**
   - In "Config Vars," add `PORT` as the key and `8000` as its value.

 **Add PostgreSQL Database:**
   - Choose PostgreSQL as database.

        Example "ElephantSQL" was used in this project

 **Configure DATABASE_URL:**
   - In "Config Vars," add `DATABASE_URL` and copy the URL from PostgreSQL dashboard.

     Note: If using ElephantSQL as PostgreSQL provider, you can use the URL provided by ElephantSQL.

 **Environment Variable Setup:**
   - Create a new file in workspace called `env.py`.
   - Import the `os` library and set the environment variable for `DATABASE_URL` to the Heroku address (or ElephantSQL URL)
   - Add a secret key using `os.environ["SECRET_KEY"] = "your secret key here"`.

 **Heroku Config Vars:**
   - Add the secret key to the Heroku app's config vars in the settings.

 **Django Settings:**
   - In `settings.py` of Django app, import `Path` from `pathlib`, `os`, and `dj_database_url`.
   - Add `if os.path.isfile("env.py"): import env` to the file.
   - Replace the SECRET_KEY with `SECRET_KEY = os.environ.get('SECRET_KEY')`.
   - Replace the database section with `DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}`.

 **Migrate Models:**
   - In workspace terminal, migrate the models to the new database connection.

### Cloudinary
To integrate Cloudinary into project, follow these steps:

 **Cloudinary Account:**
   - Log in to Cloudinary account or create one.

 **Copy CLOUDINARY_URL:**
   - Copy `CLOUDINARY_URL`.

 **Environment Variable Setup:**
   - In `env.py`, add `os.environ["CLOUDINARY_URL"] = "add cloudinary_url here"`.

 **Heroku Config Vars:**
   - In Heroku settings, add `CLOUDINARY_URL` to config vars.

 **Django Settings:**
   - In `INSTALLED_APPS`, add `cloudinary_storage`, `Django.contrib.staticfiles`, and `cloudinary` in this order.
   - Configure static file settings in `settings.py`: URL, storage path, directory path, root path, media URL, and default file storage.

 **Templates Directory Link:**
   - Link the file to the templates directory in Heroku with `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`.

 **Change Templates Directory:**
   - Change the templates directory to `TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]`.

 **Additional Folders:**
   - Create three new folders: `media`, `static`, and `templates`.

 **Procfile Creation:**
   - Create a `Procfile`.
   - Add the following line inside the Procfile: `web: gunicorn project_name_here.wsgi`.

 **Push Changes:**
    - Push all changes to GitHub.

 **Manual Deployment:**
    - In the Heroku deployment tab, deploy to Heroku manually the first time and closely monitor the process.
    - Once successful, set up automatic deployments.

### Version Control
To manage version control and push code to the main repository on GitHub using GitPod, follow these steps:

 **Add Changes:**
   - In the GitPod terminal, use the command `git add .` to stage changes.

 **Commit Changes:**
   - Commit changes with a descriptive comment using the command:
     ```
     git commit -m "Push comment here"
     ```

 **Push to GitHub:**
   - Push the updates to the repository on GitHub with the command:
     ```
     git push
     ```


 **Migrate Models:**
    - In the terminal, migrate the models to the new database connection.

### Forking the Repository:

By forking the GitHub Repository, can create a copy of the original repository without affecting the original. Follow these steps:

 **GitHub Account Setup:**
   - Log into GitHub account or create one if you don't have one.

 **Locate the Repository:**
   - Find the repository at [https://URLPATH).

 **Fork the Repository:**
   - At the top right of the repository page, click "Fork" to create a copy in your own GitHub repository.

### Clone of the Repository:

Creating a clone allows you to have a local copy of the project. Follow these steps:

 **Repository URL:**
   - Navigate to [https://URLPATH).
   - Click the green "Code" button at the top right.

 **Clone the Repository:**
   - Select the "Clone by HTTPS" option and copy the provided URL to the clipboard.

 **Terminal and Git:**
   - Open your code editor or terminal and navigate to the directory where you want to clone the repository.
   - Run `git clone` followed by the copied URL.
   - Press enter, and Git will clone the repository to your local machine.


To fork the repository, follow these steps:

1. Go to the GitHub repository.
2. Click on the Fork button in the upper right-hand corner.
3. Wait for the forking process to complete. Once done, you will have a copy of the repository in your GitHub account.

To clone the repository, follow these steps:

1. Go to the GitHub repository.
2. Locate the Code button above the list of files and click it.
3. Select your preferred method for cloning: HTTPS, SSH, or GitHub CLI, and click the copy button to copy the repository URL to your clipboard.
4. Open Git Bash (or your preferred terminal).
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Type the command `git clone` followed by the URL you copied in step 3. The command should look like this: `git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`.
7. Press Enter to create your local clone.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Credits
I would like to express my gratitude to the following resources:

### Media
Images are taken from the following page:


### Django Documentation:
The official Django documentation with guidance on models, forms, templates, and various aspects of Django development.

- [Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)


### W3 Schools:
- [Overrite Bootstraps css variables](https://www.w3schools.com/css/css_important.asp)

### Bootstrap docs:
- [Increase knowledge of bootstrap framework](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

### Geeksforgeeks: 
- [Using crisp form](https://www.geeksforgeeks.org/styling-django-forms-with-django-crispy-forms/)

### Tutorials and YouTube channels:


### Content

- Paragraphs/text for the webpage/readme was written together with [ChatGPT](https://chat.openai.com/)


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---

# Acknowledgments
 List of....


<p align="right">(<a href="#table-of-content">back to top</a>)</p>

---