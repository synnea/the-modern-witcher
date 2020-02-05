[![Build Status](https://travis-ci.org/synnea/the-modern-witcher.svg?branch=master)](https://travis-ci.org/synnea/the-modern-witcher)

# The Modern Witcher

### Milestone Project 4: Fullstack Frameworks

![demo](https://github.com/synnea/the-modern-witcher/blob/master/media/design/demo.JPG).

[The Modern Witcher](https://the-modern-witcher.herokuapp.com/) was designed, built and deployed by Carina Pöll as the final project of her diploma in software development. It is an E-Commerce website aimed at fans of the Witcher franchise. Through it, fans can purchase goods that replicate items that exist within the world of the The Witcher novels and video games.

The Witcher copyright is held by Andrzej Sapkowski. No copyright infringement is intended with this website created for educational purposes only, and no money is being made through The Modern Witcher.

The project utilizes Python 3, Django 2.2, JavaScript, and various other frameworks and libraries. Full CRUD functionality is offered throughout features of the project.

## Table of Contents

1. [UX](#UX)
    - [User Stories](#userstories)
    - [Wireframes](#wireframes)

2. [Data](#data)
    - [Items](#items)
    - [Models](#models)

3. [Features](#features)
    - [Current Features](#current-features)
    - [Features Left to Implement](#future-features)

4. [Technologies Used](#technologies)
    - [Programming Languages](#languages)
    - [Frameworks](#frameworks)
    - [Libraries](#libraries)
    - [Databases](#databases)
    - [Other Technologies](#other)

5. [Testing](#testing)
    - [Responsiveness Testing](#responsiveness-testing)
    - [Code Testing](#code-testing)
    - [Unit Testing](#unit-testing)
    - [User Story Testing](#user-stories-testing)

6. [Known Bugs](#bugs)

7. [Deployment](#deployment)
    - [Deployment Writeup](#deployment-writeup)

8. [Credits](#credits)

## UX <a name="UX"></a>

The Modern Witcher's target audience are fans of the The Witcher franchise. In keeping with the target audience, some elements from the game were taken. For example, the product descriptions and even the error messages contain phrases familiar to people who have played the series of the The Witcher RPGs. Visually, a webfont was used to mimic the official The Witcher font.

The main hero image featured on the Modern Witcher features just that: a modern witcher in modern clothes. This image served as the starting point for design considerations, and orange became the defining color of the website.

Overall, the UX design is in line with common e-commerce conventions. The index and shop pages are accessible to the public. To view the account and cart areas, users need to be registered and logged in.

The design features a static navbar which is transparent and appears upon scroll for desktop users on the index page. The navbar and footer elements are not visible in the checkout area to keep consistent with other e-commerce platforms.

FontAwesome icons are provided throughout the website to aid intuitive information input.

### User Stories <a name="userstories"></a>

The following user stories were used to design the website:

- I am a fan of the The Witcher franchise, and I'm specifically interested in buying merchandise.
- I am a fan of the The Witcher franchise, but I'm not specifically interested in buying merchandise.
- I am not a particular fan of the The Witcher franchise, but I am interested in buying unique gifts.
- I want to have an enjoyable online shopping experience.


### Wireframes <a name="wireframes"></a>

Extensive wireframes for both desktop and mobile versions were created with Balsamiq for the project. As an example, here is a wireframe for the index page:

![index-wire](https://github.com/synnea/the-modern-witcher/blob/master/media/design/example-wf.JPG)


The wireframes for every page on the website are available in .pdf format on this github respository: [WIREFRAME](https://github.com/synnea/the-modern-witcher/tree/master/wireframes).

A color palette was created early on, using the colors found in the background image as the basic point of reference. The palette was created using https://coolors.co/. The decision was taken early on that the website would feature a color scheme focused on shades of orange and purple.

The following screenshot features most of the colors used throughout the project:

![COLOR PALETTE](https://github.com/synnea/the-modern-witcher/blob/master/media/design/color_palette.JPG).

For the most part, the wireframes are similar to the finished product. However, some features were taken out due to time restraints and/or practical design concerns. One example is the 'related products' feature, which took page real estate from the review function, and which didn't seem particularly helpful due to the low number of the overall items. Since each category currently holds only about 2 items each, the database currently doesn't hold enough items to make meaningful recommendations.

## Data <a name="data"></a>

### Items <a name="items"></a>

The Modern Witcher is backed by a PostgreSQL database. At the time of writing, there are 7 items in the database.

All item photos were taken from popular shops such as Etsy. Links to the sources of each individual item can be found in the Credits section of this README file.
 

### Models <a name="models"></a>

The Witcher supports full CRUD functionality with its models.

The custom models created for the database are: Profile, Review, Item, Order, and OrderLineItem.

The 'Profile' model saves the users address and displays it in the Account section of the website. It also automatically renders the pre-saved address to the checkout area.

The 'Review' model uses the User and Item as foreign key. When a user has purchased an item, the option to leave a review gets unlocked.

The 'Item' model represents the items which can be bought on The Modern Witcher. 

'Order' and 'OrderLineItem' keep track of the overall orders and the individual items contained therein, respectively. 

The Modern Witcher does not use a 'Cart' model. Instead, the contents of the cart are made available through a global context.

## Features <a name="features"></a>

### Current Features <a name="current-features"></a>

#### Feature 1 - Save Address & view past orders
Users have the option to save their address for future use in the 'Account' section of the website. It is also automatically rendered to checkout. Past orders are also displayed in the same section.

#### Feature 2 - Review Purchased Items
Once an item has been purchased, a review can be left for it. Prompts to leave a review are provided in the confirmation screen after purchase as well as in the 'account' view.

#### Feature 3 - Flexible Navbar design
On the index page, the navbar is transparent and pops into view upon scroll. On the other pages, the navbar fixed. In the checkout pages, the navbar and footer are hidden altogether.

#### Feature 4 - Toggle Items by Category
In the shop section of the website, items can be filtered by category by clicking on the corresponding category button. 

#### Feature 5 - Item Detail View
Each item features a separate, more detailed view after having been selected from the main shop or index views.



### Features Left to Implement <a name="future-features"></a>

#### Password Resetting 
Currently, there is no way for passwords to be reset. This is a feature that I would like to implement in future releases of this project.

#### Favoriting
The option to favorite items and save them in a 'my favorites' area of the account view is also a feature that is missing and which would add a lot of value to the website's UX.

## Technologies Used <a name="technologies"></a>

### Programming Languages  <a name="languages"></a>

 [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML5** to build the structure of the content.
    
 [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS3** to style the content.

 [JavaScript](https://developer.mozilla.org/de/docs/Web/JavaScript)
    - The project uses **JavaScript** for add additional frontend functionality.  

[Python](https://docs.python.org/3/)
    - The project uses **Python** to manage its database backend.
    
### Frameworks <a name="frameworks"></a>
[Bootstrap](https://getbootstrap.com/)
    - The project uses **Bootstrap**, a CSS3 and JavaScript framework.

[Django](https://www.djangoproject.com/)
    - The project uses *Django**, a Python framework.

### Libraries <a name="libraries"></a>

[jQuery.js, version 3.4.1](https://jquery.com/)
    - The project uses **jQuery.js**, a JavaScript library used for event handling.

### Databases <a name="databases"></a>

[PostgreSQL](https://www.postgresql.org/)
    - The project uses **PostgreSQL** as its database.


### Other Technologies <a name="other"></a>

[Font Awesome](https://fontawesome.com/)
    - The project uses **Font Awesome**, free icons for improved UI.

[Google Fonts](https://developers.google.com/fonts/)
     - The project uses **Google Fonts** for its typography.  

[Git](https://git-scm.com/)
    - The project uses **Git** for version control.

 
## Testing <a name="testing"></a>

### Responsiveness Testing <a name="responsiveness-testing"></a>

The responsiveness of the website was tested on Responsinator.

* iPhone eXpensive portrait
* iPhone eXpensive landscape
* Android portrait
* Android landscape
* iPhone 6-8 portrait
* iPhone 6-8 landscape
* iPhone 6-8 Plump landscape
* iPhone 6-8 Plump landscape
* iPad portrait
* iPad landscape

The project is not optimized for all of the above. Landscapes and iPad versions in particular are not optimized.

Since this project's focus is on the design of the backend, I chose not to spend as much time as I did previously on strict responsiveness optimization. 

### Code Testing <a name="code-testing"></a>

**HTML** 
* [HTML Validator](https://www.freeformatter.com/html-validator.html).
    - The project contains a total of 12 html files. Throughout all of them, the HTML Validator did not recognize templating language, such as variable interpolation and functions, as valid HTML, and threw errors. This was ignored throughout all files. The following anomalies remain:
        - in the 'forbidden.html' file, the HTML Validator throws an error that inline style CSS is not allowed in this context. However, moving the CSS to a separate file leads to the CSS not being rendered at all. Thus, I chose to keep the inline styling.
        - in the 'logreg.html' file, the HTML Validator throws the error that tabpanels must be part of a tablist. However, adding a div with the role of tablist disabled the functionality. Thus, the semantic problem remains uncorrected.
        - similarly, the profile pages also throw the tabpanel and tablist error. Not wanting to break the functionality, I chose to leave it alone.
        - for the 'base.html' file, the HTML Validator throws the error that the "|" character is not allowed in a query. However, it has been copied as part of a query to Google Fonts to import several different custom fonts, and was left in.

**CSS**  
* [CSS Validator](https://jigsaw.w3.org/css-validator/).
    - The project contains 1 CSS file (along with several SCSS ones). The file passes validation without any errors.

**JavaScript** 
* [JSHint.com](https://jshint.com/). 
    - The project contains 7 JavaScript files. All of them are semantically correct. The files contain a total of 27 functions, and the most complex function has a cyclomatic complexity value of 2.

**Python**
* [PEP8Online](http://pep8online.com/).
    - The project contains a total of 1 Python file. At the time of writing this readme, the Python code in this project contains a total of 10 lines which exceed the recommended max length of 79 characters. I chose to leave them in because breaking them up resulted in less readability. The PEP8 guide states that its guidelines could be bent on an individual basis when doing so raised readability, hence I chose to do so here. Apart from those 10 lines, the code is fully PEP8-compliant.

### User Story Testing <a name="user-stories-testing"></a>

Here are the results for the user story tests:

**Story 1**

- I am a developer or designer. I heard about tanDev and have an idea what it's about. I am interested in finding out if there are other developers in the city with whom I could exchange my skills with.

Solution: upon landing on the main page, the background picture of the puzzle pieces and the slogan 'exchange your skills with other developers and designers' confirms that I've come to the right place. I click on 'sign up' and am taken to the registration route.


**Story 2**

- I am a developer or designer. I stumble upon tanDev without knowing what it is.

Solution: upon landing on the main page, the imagry and slogan give me an idea about what tanDev is about. Scrolling down the page and seeing the profiles in the carousel gives a further idea. Finally, clicking on the 'about' page clarifies all doubts. Navigating back to the main page, I click on the 'sign up' button and follow the same journey as user story 1 from there on out.

**Story 3**

- I am a tech recruiter interested in contacting available talent.

Solution: upon landing on the main page, the imagry and slogan quickly give me an idea that I've come to a place where I can find relevant tech talent. The 'search' button seems most relevant to me, so I click on it. There, among the search options, I find the 'available for Hire' checkbox. I select it, and search the database for developers and designers who are open to new opportunities.

**Story 4**

- I am a startup entrepreneur interested in finding a co-founder. I am a designer and need a programmer with strong backend skills to bring my product to life.

Solution: upon landing on the main page, the imagry and slogan quickly give me an idea that I've come to a place where I can find someone to help me. The 'search' button seems most relevant to me, so I click on it. There, among the search options, I find the 'looking for Co-Founder' checkbox. I select it, and then select several backend languages in the skills menu. This gives me a list of people who have the skills I need, and who are open to being approached about co-founding opportunities. I decide to send one or several of them a message. The last point is not achieved yet, as tanDev at present does not feature a messaging function.


## Known Bugs <a name="bugs"></a>

On iPhones, the carousel on the index page overlaps with the indicators below. I was not able to find a good fix for it before it was time to submit, but I would like to fix this eventually.

## Deployment <a name="deployment"></a>

### Deployment Writeup <a name="deployment-writeup"></a>
 
To deploy tanDev on heroku, I took the following steps:

1. I created a requirements.txt file using the terminal command pip freeze > requirements.txt.

2. I created a Procfile with the terminal command echo web: python app.py > Procfile.

3. I staged and committed the requirements.txt and Procfile to my project repository. 

4. I went to heroku.com, logged in, and clicked on the "New" button in the dashboard to create a new app. I named it 'tanDev' and set its region to Europe.

5. In the heroku dashboard for the application, I clicked on "Settings" > "Reveal Config Vars". Then, I set the Port, IP, MongoURI and Secret Key variables.

6. From my terminal window, I logged into heroku using "heroku login --interactive." After entering my credentials, I registered heroku as a remote destination for my project with "heroku git remote." I then pushed my project to heroku with "git push heroku."

7. To get the app to run and scale the dynos, I used the command "heroku ps:scale web=1" in my terminal.

8. The app is now successfully deployed!

### Differences between local and deployed versions <a name="deployment-differences"></a>

The project was developed locally with Visual Studio Code. Environment variables, including secret key and Mongo URI, were saved in a settings.json file which was added to .gitignore. For the deployed version, as mentioned in the deployment writeup above, environemnt variables were set in the Config Variables.

## Credits <a name="credits"></a>

Credit for the logo goes to he-who-prefers-to-go-uncredited. You're awesome.

Many thanks to [Tim Nelson](https://github.com/TravelTimN), whose patience helped me to get started on the sever-side development.

Most of the images used on tanDev have been sourced from [Adobe Stock](https://stock.adobe.com/).



