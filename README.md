# Custom Artist

‘The online supply and demand platform for artists and clients’
Custom Artist joins creates opportunities for artists to get in touch with clients. These clients could be companies or private clients who are looking for an artist to create a particular form of artwork. The client uploads an assignment. Artists respond to assignments they’re interested in with an artwork proposal. Through a logical and clear step-by-step process the artist and client can come to an agreement.
Custom Artist supports artists who are struggling to find assignments to earn money. At the same time it saves companies and private clients time to find the art they are – in whatever form – looking for. 

## UX

### Process

#### Step 1

Without any obligations, clients register, login and place an assignment on the website. They should add a detailed description of the assignment, substantiated with pictures. The client can use many different variables to define the ‘feeling’ of the artwork they are looking for. They can also add a target price they are offering the artist.

#### Step 2

The artist registers, logs in and looks for assignments from their dashboard. They can propose an artwork for an assignment they like. With this proposal they add a full description along with sketches. Proposals can only be viewed by the client who posted the assignment and by the artist.

#### Step 3

Clients can view the proposals from artists for their assignments in their dashboard. The client chooses the artwork proposal they like best and they can contact the artist. The client deletes the assignment once it is done or if they don’t see much point continuing with it.

### Sitemap

![Sitemap](https://github.com/MarthGimenzo/CustomArtist/blob/master/static/images/readme_images/Sitemap.png)
 
### User Stories

1.	A user wants a clear explanation of the website’s purpose so that they can find out if it fits their needs;
1.	A user wants to register to the site so they can log in to their personal dashboard and manage their assignments and proposals;
3.	Artists want to get an overview of assignments so that they can find an assignment that fits them;
4.	Artists want to add a proposal for an artwork to an assignment so that they will have a chance in getting the job for the assignment;
5.	Clients want to post detailed assignments for a specific type of artwork – either for business or private – so they can find an artist that is suited to fulfil the assignment;
6.	Clients want to get an overview of proposals from artists for their assignments.
7.	Clients want to get in touch with the artist of a certain proposal.

### Mockups

In this pdf file you can find the mockups that were created for Custom Artist

[PDF of Mockups of Custom Artist](https://github.com/MarthGimenzo/CustomArtist/blob/master/static/pdf/Customartist_mockups.pdf)

### Design

The website has an overall ‘black’ feeling with a white font. This is to symbolize a blackboard. To give the page color, pictures of different artist fade in and out on the background. 

Two fonts were used on the website:

* ‘BeatsterOutline’, which was bought from MyFonts.com. It is used in the slogan on the index page.
* ‘Montserrat’, which was retrieved from Google Fonts. It is used in the headers and paragraphs on the website.
* The Custom Artist logo and mascot was designed by Jo-Soulever (nickname) through the website 99designs.com. 

## Features

### Existing Features

* An index page, including a ‘How Does It Work’ section;
* Two different Register and Login systems: one for Artists and one for Clients;
* A navbar with a dropdown menu. The navbar contains the dashboard items and differs on the index page, artist index page and client index page;

#### Features for Artist Users

* An overview of all assignments available for the artist to make a proposal for;
* A detailed description of an assignment with a button to make a proposal for the current assignment;
* The ability to input a full description of a proposal for a specific assignment and upload it.
* An overview of all the proposals the artist has done;
* The ability to delete, or edit the currently viewed proposal;
* The ability to logout.

#### Features for Client Users

* An overview of all assignments the client has posted;
* A detailed description of a specific assignment and the ability to delete it;
* The ability to see all proposals by artists that have been done for a specific assignment.
* The ability to create a new assignment and upload it. There are many different types of input types the user can make use of, to specify the assignment very clearly.
* The ability to logout.

#### Other features

* Documentation: The ReadMe file and Mockups;
* Responsive design;
* Accessibility: Simple transactions of information;
* Data is stored in MongoDB databases using four collections: Artists, Clients, Assignments and Proposals. The website makes use of all CRUD functions.
* Git Version Control;
* Hosted on GitHub pages and Heroku.

### Features Left to Implement

* The ability for users to add pictures to their assignments and proposals;
* The ability for users to add more information to their user account, which would be represented in the assignments and proposals;
* The ability for users to edit and delete their profile and credentials;
* The ability for clients to be notified when an artist has submitted a proposal for their assignment.

## Technologies Used

### Languages

* HTML
* CSS
* Javascript. Javascript was used the fading backgrounds, toggling themes when a client adds an assignment, validating forms before modals appear, and a smooth scroll function on the index page.
* Python

### Tools

* Google Chrome Developer Tools
* Balsamiq, for creating mockups
* Photoshop, for editing pictures
* GitPod, the IDE the website was built in
* PIP, for the installation of tools
* Git, for version control
* GitHub, for storing the project repository
* Heroku, for hosting the website Libraries
* jQuery for DOM manipulation
* Bootstrap, used for frameworks
* Google Fonts, for styling the website fonts
* MyFonts.com, for styling the website slogan and navbar items

### Databases

* MongoDB for storing Artists, Clients, Assignments and Proposals data

#### Database Structure

![Database Structure](https://github.com/MarthGimenzo/CustomArtist/blob/master/static/images/readme_images/Databases.png)

## Testing

### Navbar Functions

#### Index Page Navbar (base)

##### An artist wants to login

1. When clicked on the ‘Artists’ item a modal appears;
2. When the user enters false credentials, they are redirected to the index page and the modal reappears mentioning the credentials are invalid;
3. When the user enters correct credentials, they are redirected to the ‘available assignments’ page;
4. If the user does not want to log in, clicking the area around the modal, will close the modal.

##### An artist wants to register

1. When clicked on the ‘Artists’ item a modal appears;
2. When clicked on ‘Register as new Artist’, the user is logged in and they are redirected to the ‘register artist’ page.
3. If the user does not want to register, clicking the area around the modal, will close the modal.

##### A client wants to login

1. When clicked on the ‘Clients’ item a modal appears;
2. When the user enters false credentials, they are redirected to the index page and the modal reappears mentioning the credentials are invalid;
3. When the user enters correct credentials, the user is logged in and they are redirected to the ‘my assignments’ page.
4. If the user does not want to log in, clicking the area around the modal, will close the modal.

##### A client wants to register

1. When clicked on the ‘Client’ item a modal appears;
2. When clicked on ‘Register as new Client’, they are redirected to the ‘register client’ page.
3. If the user does not want to register, clicking the area around the modal, will close the modal.

##### A user wants to see how the website works

1. When clicked on the ‘How does it work’ item, the page scrolls to the ‘How Does It Work’ section on the index page.

#### A user wants to get back to the top of the index page

1. When clicked on the logo, the user is redirected to the index page.

#### Register Page Navbar (base)

#####  An artist wants to login

1. When clicked on the ‘Artists’ item a modal appears;
2. When the user enters false credentials, they are redirected to the index page and the modal reappears mentioning the credentials are invalid;
3. When the user enters correct credentials, they are redirected to the ‘available assignments’ page;
4. If the user does not want to log in, clicking the area around the modal, will close the modal.

#####  An artist wants to register

1. When clicked on the ‘Artists’ item a modal appears;
2. When clicked on ‘Register as new Artist’, the user is logged in and they are redirected to the ‘register artist’ page.
3. If the user does not want to register, clicking the area around the modal, will close the modal.

##### A client wants to login

1. When clicked on the ‘Clients’ item a modal appears;
2. When the user enters false credentials, they are redirected to the index page and the modal reappears mentioning the credentials are invalid;
3. When the user enters correct credentials, the user is logged in and they are redirected to the ‘my assignments’ page.
4. If the user does not want to log in, clicking the area around the modal, will close the modal.

##### A client wants to register

1. When clicked on the ‘Client’ item a modal appears;
2. When clicked on ‘Register as new Client’, they are redirected to the ‘register client’ page.
3. If the user does not want to register, clicking the area around the modal, will close the modal.

##### A user wants to get back to the index page

1. When clicked on the logo, the user is redirected to the index page.

#### Artist Index Navbar (base)

##### An artist wants to see all available assignments

1. When clicked on the ‘Assignments’ item, the artist is redirected to the ‘Available Assignments’ page.
2. When clicked on the logo,  the artist is redirected to the ‘Available Assignments’ page.

##### An artist wants to see all the proposals he has done

1. When clicked on the ‘My Proposals’ item, the artist is redirected to the ‘My Proposals’ page.

##### An artist wants to log out

1. When clicked on the ‘Log Out: <username>’ item, a modal appears asking if the user really wants to log out.
2. When clicked on ‘Log Out’, the session is ended and the user is redirected to the index page.
3. If the user does not want to log out, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

#### Client Index Navbar (base)

##### A client wants to see all their own posted assignments

1. When clicked on the ‘My Assignments’ item, the client is redirected to the ‘My Assignments’ page.
2. When clicked on the logo,  the client is redirected to the ‘My Assignments’ page.

##### A client wants to post a new assignment

1. When clicked on the ‘New Assignment’ item, the client is redirected to the ‘New Assignment’ page.

##### A client wants to log out

1. When clicked on the ‘Log Out: username’ item, a modal appears asking if the user really wants to log out.
2. When clicked on ‘Log Out’, the session is ended and the user is redirected to the index page.
3. If the user does not want to log out, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

### Main Pages

#### Index page

#####  A user wants to get back to the top of the index page

1. When clicked on the logo, the user is redirected to the index page.

### Artist Pages

#### Available Assignments

##### An artist wants to see all available assignments

1. The ‘Available Assignments’ page offers a list with all assignments that were posted by all clients correctly;
2. All data of the assignment is viewed correctly. If a client has left out some input data, that data does not appear.
3. If there are no available assignments, a message will be visible saying there are no assignments available.

#####  An artist wants to see the details of a specific assignment

1. When clicked on the ‘View Details’ button of an assignment, the artist is redirected to the ‘Assignment Details’ page of that specific assignment correctly.

#### Assignment Details

##### An artist wants to see all details of an assignment

1. All data of the specified assignment is viewed correctly. All data appears as it should. If a client has left out some input data, that data does not appear.

##### An artist wants to get back to see all available assignments

1. When clicked on the ‘Back to Assignments’ button, the artist is redirected to the ‘Available Assignments’ page.

##### An artist wants to add a proposal to an assignment

1. When clicked on the ‘Submit a Proposal’ button, the artist is redirected to the ‘Add a Proposal’ page.

#### Add a Proposal

##### An artist wants to submit a proposal

1. The artist should fill in all forms;
2. When clicked on the ‘Submit Proposal’ button, all forms are validated correctly;
3. If all forms are valid, a modal appears which asks if the artist really wants to submit the proposal;
4. When clicked on ‘Submit Proposal, proposal is correctly created in the database and the artist is redirected to the ‘Available Assignments’ page;
5. If the artist does not want to submit the proposal, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

##### An artist wants to get back to see all available assignments

1. When clicked on the ‘Back to Assignments’ button, the artist is redirected to the ‘Available Assignments’ page.

#### My Proposals

##### An artist wants to see all his proposals

1. The ‘My Proposals’ page offers a list with all proposals that were posted by the current artist correctly;
2. If the artist has done no proposals yet, a message will be visible saying the artist has done no proposals yet.

##### An artist wants to edit or delete a proposal

1. When clicked on the ‘Edit Proposal’ button, the artist is redirected to the ‘Edit Proposal’ page.

#### Edit Proposal

##### An artist wants to edit the proposal

1. All forms are filled in with the values of the proposal correctly;
2. An artist can edit these fields;
3. When clicked on the ‘Save Changes’ button, the proposal is correctly edited in the database and the artist is redirected to the ‘My Proposals’ page.

##### An artist wants to delete the proposal

1. When clicked on ‘Delete Proposal’, a modal appears which asks if the artist really wants to delete the proposal;
2. When clicked on ‘Delete Proposal, the proposal is correctly deleted from the database and the artist is redirected to the ‘My Proposals’ page;
3. If the artist does not want to delete the proposal, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

##### An artist wants to get back to see all available assignments

1. When clicked on the ‘Back to Assignments’ button, the artist is redirected to the ‘Available Assignments’ page.

### Client Pages

#### My Assignments

##### A client wants to see all his posted assignments

1. The ‘My Assignments’ page offers a list with all assignments that were posted by the current user correctly;
2. If the client has no running assignments, a message will be visible saying the client has no running assignments.

##### A client wants to see the details of a specific assignment

1. When clicked on the ‘View Details’ button of an assignment, the artist is redirected to the ‘My Assignment Details’ page of that specific assignment correctly.

#### My Assignment Details

##### A client wants to see all details of an assignment

1. All data of the specified assignment is viewed correctly. All data appears as it should. If the client has left out some input data, that data does not appear.

##### A client wants to get back to see all his posted assignments

1. When clicked on the ‘Back to Assignments’ button, the client is redirected to the ‘My Assignments’ page.

##### A client wants to delete the assignment

1. When clicked on ‘Delete Assignment’, a modal appears which asks if the client really wants to delete the assignment;
2. When clicked on ‘Delete Assignment’, the assignment and all corresponding proposals for that assignment are correctly deleted from the database and the client is redirected to the ‘My Assignments’ page;
3. If the client does not want to delete the assignment, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

##### A client wants to see if he has any proposals from artists for his assignment

1. At the bottom of the page the proposals of artists are displayed. If the assignment has no proposals yet, a message will be visible saying the client has received no proposals yet.

#### New Assignment

##### A client wants to submit a new assignment

1. The client should fill in the required forms;
2. When clicked on the ‘Submit Assignment’ button, all forms are validated correctly;
3. If all forms are valid, a modal appears which asks if the client really wants to submit the assignment;
4. When clicked on ‘Submit Assignment, the assignment is correctly created in the database and the client is redirected to the ‘My Assignments’ page;
5. If the client does not want to submit the proposal, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

### Different mobile devices

##### The user wants to view the site on its preferred mobile device

1. Responsinator.com was used to see if all data is viewed correctly on mobile devices. It has been confirmed that it does so.

### Different desktop browsers

##### The user wants to view the site on a desktop computer

1. The website has been tested in FireFox and it functions correctly;
2. The website has been tested in Internet Explorer and it functions correctly;

## Deployment

### Run Project Locally

You can run the project locally in your IDE by following these instructions:
PIP, Python3 and Git need to be installed on your computer.

1.	On the GitHub repository of Custom Artist, click clone or download;
2.	Click ‘Download ZIP;
3.	Unpack the downloaded ZIP file;
4.	Open the index.html file with your preferred IDE;
5.	Install Flask by entering 'pip3 install flask' in the terminal of your IDE

### Heroku Deployment

Deployment of Custom Artist to Heroku has been done by the following steps:
1.	A new app was created on the Heroku Dashboard.
2.	From the Heroku dashboard of the application, GitHub was selected as the deployment method.
3.	The Config Vars of the application were set.
4.	A requirements.txt file was created using pip freeze > requirements.txt in the terminal of the IDE
5.	A Procfile was created using echo web: pythob app.py > Procfile in the terminal of the IDE
6.	The new requirements.txt file and Procfile were added and commited and pushed to GitHub
7.	A connection between the IDE and Heroku was established by logging in on Heroku in the terminal of the IDE.
8.	The project was pushed to Heroku

### Deployment version vs. development version

There are no major differences between the deployment version and the development version.
The only differences that might be noticed are changes in the database.
Users will be able to upload assignments and proposals. And as such, the assignments and proposals in the database may change over time.

## Credits

All content was on the website was conceived by myself.

### Media

- The logo, both with and without the mascot, and the mascot itself, were designed by [Jo Zhuang](https://99designs.nl/profiles/jozhuang)
- The background image with the woman on the graffiti wall comes from [Alphacoders.com](https://wall.alphacoders.com/by_sub_category.php?id=168539&name=Graffiti+Wallpapers&filter=4K+Ultra+HD).
- The background image with the grafiti bird is made by [Luis Seven Martins](https://frankiebeane.wordpress.com/2015/04/26/l7m-luis-seven-martins-sao-paulo-brasil-graffiti-artist/).
- The background image with the colorful painting of a park comes from [Alimentatiehaven.nl](https://alimentatiehaven.nl/art-201/).
- The background image with the of the sculpture comes from [Coderch & Malavia Sculptors](https://www.facebook.com/CoderchMalaviaSculptors/).
- The 2 background images with the fireworks come from [Ryan Mc Ginley](https://www.juxtapoz.com/news/news/ryan-mcginleys-fireworks/).
- The 3 background images with the model pictures come from [Ilva Stoelwinder](https://twitter.com/ilvaphotography).
- The phone icon in the 'How Does It Work' section comes from [IconBros](https://nl.pinterest.com/pin/814588651336180920/).
- The colourful cloud behind the logo on the homepage comes from [Freepik.com](https://nl.freepik.com/vrije-foto-vectoren/splash-achtergrond).
- The placeholder image of the person in the assignment divs is a free picture taken from [Thebuiscitstuidio](https://www.thebiscuitstudio.co.za/simple-testimonials/elizabeth-gray/placeholder-team-women/).

### Techniques

- The fading backgrounds were created using a tutorial of [rudolfson.junior](https://www.youtube.com/watch?v=XjPdQSqtJhs). Thank you very much!
- The javascript scroll-to system was based on code by [devers](https://coderwall.com/p/z7gfjq/scroll-to-page-sections-with-nav-links). Thank you very much!
- The Flask login system was based on a tutorial by [Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE). Thank you very much!
- The repository was set up by using the [Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template). Thank you very much!

### Acknowledgements

The idea of this website is my own. I made a thesis about it in my education Leisure Management, but never got the chance to make it myself. Now, I was able to make the first step :)

### Special Thanks

* Code Instute, and all their tutors;
* My mentor, Antonio Rodriguez;
* Other students from Code Institute;
* Ilva Stoelwinder;
* Berber Visser;

