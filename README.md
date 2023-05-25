<<<<<< auth
<a name="readme-top"></a>

<!--
HOW TO USE:
This is an example of how you may give instructions on setting up your project locally.

Modify this file to match your project and remove sections that don't apply.

REQUIRED SECTIONS:
- Table of Contents
- About the Project
  - Built With
  - Live Demo
- Getting Started
- Authors
- Future Features
- Contributing
- Show your support
- Acknowledgements
- License

OPTIONAL SECTIONS:
- FAQ

After you're finished please remove all the comments and instructions!
-->

<div align="center">
  <!-- You are encouraged to replace this logo with your own! Otherwise you can also remove it. -->
  <br/>

  <h3><b>Microverse README Template</b></h3>

</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
  - [Deployment](#deployment)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [🙏 Acknowledgements](#acknowledgements)
- [❓ FAQ (OPTIONAL)](#faq)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 [Tradex] <a name="about-project"></a>

> Describe your project in 1 or 2 sentences.

**[Tradex]** is a trading software, where traders trade and are able to monitot their trade. It is...

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

> Describe the tech stack and include only the relevant sections that apply to your project.

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://getbootstrap.com/">Bootstrap</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.djangoproject.com/">Django</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.sqlite.org/">SQLite</a></li>
    <li><a href="https://www.mongodb.com/">Mongodb</a></li>
  </ul>
</details>

<!-- Features -->

### Key Features <a name="key-features"></a>

> Describe between 1-3 key features of the application.

- **[Traders Dashboard]**
- **[Admin Dashboard]**
- **[Trade Functionality]**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LIVE DEMO -->

## 🚀 Live Demo <a name="live-demo"></a>

> Add a link to your deployed project.

- [Live Demo Link](http://marvex.pythonanywhere.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

> Describe how a new developer could make use of your project.

To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

To have a computer, a code editor, a github account and some basci understand of git
<!--
Example command:

```sh
 gem install rails
```
 -->

### Setup

Clone this repository to your desired folder:

`git clone https://github.com/Marvel2456/Tradex`

<!--
Example commands:

```sh
  cd my-folder
  git clone git@github.com:myaccount/my-project.git
```
--->

### Install

Install this project with:

cd to the trading folder and the run this command in your terminal
`pip install -r requirements.txt`

or `pip install requirements.txt`
with this, all the lbraries and packages will be fully installed.
<!--
Example command:

```sh
  cd my-project
  gem install
```
--->

### Usage

To run the project, execute the following command:

After installing, make sure your mongodb setup is properly configured, create a database, then go to the settings.py file
in the trading folder and edit the databese name to your database name and run the following command
`python manage.py makemigration` and `python manage.py migrate`
After that is done, run `python manage.py runserver`
and on another terminal, run `celery -A beat Trading -l INFO` and `celery -A worker Trading -l INFO`
<!--
Example command:

```sh
  rails server
```
--->

### Run tests

To run tests, run the following command:

<!--
Example command:

```sh
  bin/rails test test/models/article_test.rb
```
--->

### Deployment

You can deploy this project using:

<!--
Example:

```sh

```
 -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

> Mention all of the collaborators of this project.

👤 **Author1**

- GitHub: [@githubhandle](https://github.com/githubhandle)
- Twitter: [@twitterhandle](https://twitter.com/twitterhandle)
- LinkedIn: [LinkedIn](https://linkedin.com/in/linkedinhandle)

👤 **Author2**

- GitHub: [@githubhandle](https://github.com/githubhandle)
- Twitter: [@twitterhandle](https://twitter.com/twitterhandle)
- LinkedIn: [LinkedIn](https://linkedin.com/in/linkedinhandle)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>

> Describe 1 - 3 features you will add to the project.

- [ ] **[new_feature_1]**
- [ ] **[new_feature_2]**
- [ ] **[new_feature_3]**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

> Write a message to encourage readers to support your project

If you like this project...

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

> Give credit to everyone who inspired your codebase.

I would like to thank...

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FAQ (optional) -->

## ❓ FAQ (OPTIONAL) <a name="faq"></a>

> Add at least 2 questions new developers would ask when they decide to use your project.

- **[Question_1]**

  - [Answer_1]

- **[Question_2]**

  - [Answer_2]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

_NOTE: we recommend using the [MIT license](https://choosealicense.com/licenses/mit/) - you can set it up quickly by [using templates available on GitHub](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository). You can also use [any other license](https://choosealicense.com/licenses/) if you wish._

<p align="right">(<a href="#readme-top">back to top</a>)</p>
======
logo
Microverse README Template
📗 Table of Contents
📖 About the Project
🛠 Built With
Tech Stack
Key Features
🚀 Live Demo
💻 Getting Started
Setup
Prerequisites
Install
Usage
Run tests
Deployment
👥 Authors
🔭 Future Features
🤝 Contributing
⭐️ Show your support
🙏 Acknowledgements
❓ FAQ (OPTIONAL)
📝 License
📖 [your_project_name]
Describe your project in 1 or 2 sentences.

[your_project__name] is a...

🛠 Built With
Tech Stack
Describe the tech stack and include only the relevant sections that apply to your project.

Client
Server
Database
Key Features
Describe between 1-3 key features of the application.

[key_feature_1]
[key_feature_2]
[key_feature_3]
(back to top)

🚀 Live Demo
Add a link to your deployed project.

Live Demo Link
(back to top)

💻 Getting Started
Describe how a new developer could make use of your project.

To get a local copy up and running, follow these steps.

Prerequisites
In order to run this project you need:

Setup
Clone this repository to your desired folder:

Install
Install this project with:

Usage
To run the project, execute the following command:

Run tests
To run tests, run the following command:

Deployment
You can deploy this project using:

(back to top)

👥 Authors
Mention all of the collaborators of this project.

👤 Author1

GitHub: @githubhandle
Twitter: @twitterhandle
LinkedIn: LinkedIn
👤 Author2

GitHub: @githubhandle
Twitter: @twitterhandle
LinkedIn: LinkedIn
(back to top)

🔭 Future Features
Describe 1 - 3 features you will add to the project.

[ ] [new_feature_1]
[ ] [new_feature_2]
[ ] [new_feature_3]
(back to top)

🤝 Contributing
Contributions, issues, and feature requests are welcome!

Feel free to check the issues page.

(back to top)

⭐️ Show your support
Write a message to encourage readers to support your project

If you like this project...

(back to top)

🙏 Acknowledgments
Give credit to everyone who inspired your codebase.

I would like to thank...

(back to top)

❓ FAQ (OPTIONAL)
Add at least 2 questions new developers would ask when they decide to use your project.

[Question_1]

[Answer_1]
[Question_2]

[Answer_2]
(back to top)

📝 License
This project is MIT licensed.

NOTE: we recommend using the MIT license - you can set it up quickly by using templates available on GitHub. You can also use any other license if you wish.

(back to top)
>>>>>> main
