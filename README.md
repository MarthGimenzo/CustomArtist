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

 
### User Stories

1.	A user wants a clear explanation of the website’s purpose so that they can find out if it fits their needs;
1.	A user wants to register to the site so they can log in to their personal dashboard and manage their assignments and proposals;
3.	Artists want to get an overview of assignments so that they can find an assignment that fits them;
4.	Artists want to add a proposal for an artwork to an assignment so that they will have a chance in getting the job for the assignment;
5.	Clients want to post detailed assignments for a specific type of artwork – either for business or private – so they can find an artist that is suited to fulfil the assignment;
6.	Clients want to get an overview of proposals from artists for their assignments.
7.	Clients want to get in touch with the artist of a certain proposal.

### Mockups
 
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

* When an artist has logged in: An overview of all assignments available for the artist to make a proposal for;
* When an artist has logged in: A detailed description of an assignment with a button to make a proposal for the current assignment;
* When an artist has logged in: The ability to input a full description of a proposal for a specific assignment and upload it.
* When an artist has logged in: An overview of all the proposals the artist has done;
* When an artist has logged in: The ability to delete, or edit the currently viewed proposal;
* When an artist has logged in: The ability to logout.

* When a client has logged in: An overview of all assignments the client has posted;
* When a client has logged in: A detailed description of a specific assignment and the ability to delete it;
* When a client has logged in: The ability to see all proposals by artists that have been done for a specific assignment.
* When a client has logged in: The ability to create a new assignment and upload it. There are many different types of input types the user can make use of, to specify the assignment very clearly.
* When a client has logged in: The ability to logout.

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

IMAGE HERE

## Testing

### Navbar Functions

#### Index Page Navbar (base)

##### An artist wants to login

-	When clicked on the ‘Artists’ item a modal appears;
-	When the user enters false credentials, they are redirected to the index page and the modal reappears mentioning the credentials are invalid;
-	When the user enters correct credentials, they are redirected to the ‘available assignments’ page;
-	If the user does not want to log in, clicking the area around the modal, will close the modal.

##### An artist wants to register

-	When clicked on the ‘Artists’ item a modal appears;
-	When clicked on ‘Register as new Artist’, the user is logged in and they are redirected to the ‘register artist’ page.
-	If the user does not want to register, clicking the area around the modal, will close the modal.

##### A client wants to login

-	When clicked on the ‘Clients’ item a modal appears;
-	When the user enters false credentials, they are redirected to the index page and the modal reappears mentioning the credentials are invalid;
-	When the user enters correct credentials, the user is logged in and they are redirected to the ‘my assignments’ page.
-	If the user does not want to log in, clicking the area around the modal, will close the modal.

##### A client wants to register

-	When clicked on the ‘Client’ item a modal appears;
-	When clicked on ‘Register as new Client’, they are redirected to the ‘register client’ page.
-	If the user does not want to register, clicking the area around the modal, will close the modal.
A user wants to see how the website works
-	When clicked on the ‘How does it work’ item, the page scrolls to the ‘How Does It Work’ section on the index page.
A user wants to get back to the top of the index page
-	When clicked on the logo, the user is redirected to the index page.

#### Register Page Navbar (base)

#####  An artist wants to login

-	When clicked on the ‘Artists’ item a modal appears;
-	When the user enters false credentials, they are redirected to the index page and the modal reappears mentioning the credentials are invalid;
-	When the user enters correct credentials, they are redirected to the ‘available assignments’ page;
-	If the user does not want to log in, clicking the area around the modal, will close the modal.

#####  An artist wants to register

-	When clicked on the ‘Artists’ item a modal appears;
-	When clicked on ‘Register as new Artist’, the user is logged in and they are redirected to the ‘register artist’ page.
-	If the user does not want to register, clicking the area around the modal, will close the modal.

##### A client wants to login

-	When clicked on the ‘Clients’ item a modal appears;
-	When the user enters false credentials, they are redirected to the index page and the modal reappears mentioning the credentials are invalid;
-	When the user enters correct credentials, the user is logged in and they are redirected to the ‘my assignments’ page.
-	If the user does not want to log in, clicking the area around the modal, will close the modal.

##### A client wants to register

-	When clicked on the ‘Client’ item a modal appears;
-	When clicked on ‘Register as new Client’, they are redirected to the ‘register client’ page.
-	If the user does not want to register, clicking the area around the modal, will close the modal.
A user wants to get back to the index page
-	When clicked on the logo, the user is redirected to the index page.

#### Artist Index Navbar (base)

##### An artist wants to see all available assignments

-	When clicked on the ‘Assignments’ item, the artist is redirected to the ‘Available Assignments’ page.
-	When clicked on the logo,  the artist is redirected to the ‘Available Assignments’ page.

##### An artist wants to see all the proposals he has done

-	When clicked on the ‘My Proposals’ item, the artist is redirected to the ‘My Proposals’ page.

##### An artist wants to log out

-	When clicked on the ‘Log Out: <username>’ item, a modal appears asking if the user really wants to log out.
-	When clicked on ‘Log Out’, the session is ended and the user is redirected to the index page.
-	If the user does not want to log out, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

#### Client Index Navbar (base)

##### A client wants to see all their own posted assignments

-	When clicked on the ‘My Assignments’ item, the client is redirected to the ‘My Assignments’ page.
-	When clicked on the logo,  the client is redirected to the ‘My Assignments’ page.

##### A client wants to post a new assignment

-	When clicked on the ‘New Assignment’ item, the client is redirected to the ‘New Assignment’ page.

##### A client wants to log out

-	When clicked on the ‘Log Out: username’ item, a modal appears asking if the user really wants to log out.
-	When clicked on ‘Log Out’, the session is ended and the user is redirected to the index page.
-	If the user does not want to log out, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

### Main Pages

#### Index page

#####  A user wants to get back to the top of the index page

-	When clicked on the logo, the user is redirected to the index page.

### Artist Pages

#### Available Assignments

##### An artist wants to see all available assignments

-	The ‘Available Assignments’ page offers a list with all assignments that were posted by all clients correctly;
-	All data of the assignment is viewed correctly. If a client has left out some input data, that data does not appear.
-	If there are no available assignments, a message will be visible saying there are no assignments available.

#####  An artist wants to see the details of a specific assignment

-	When clicked on the ‘View Details’ button of an assignment, the artist is redirected to the ‘Assignment Details’ page of that specific assignment correctly.

#### Assignment Details

##### An artist wants to see all details of an assignment

-	All data of the specified assignment is viewed correctly. All data appears as it should. If a client has left out some input data, that data does not appear.

##### An artist wants to get back to see all available assignments

-	When clicked on the ‘Back to Assignments’ button, the artist is redirected to the ‘Available Assignments’ page.

##### An artist wants to add a proposal to an assignment

-	When clicked on the ‘Submit a Proposal’ button, the artist is redirected to the ‘Add a Proposal’ page.

#### Add a Proposal

##### An artist wants to submit a proposal

-	The artist should fill in all forms;
-	When clicked on the ‘Submit Proposal’ button, all forms are validated correctly;
-	If all forms are valid, a modal appears which asks if the artist really wants to submit the proposal;
-	When clicked on ‘Submit Proposal, proposal is correctly created in the database and the artist is redirected to the ‘Available Assignments’ page;
-	If the artist does not want to submit the proposal, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

##### An artist wants to get back to see all available assignments

-	When clicked on the ‘Back to Assignments’ button, the artist is redirected to the ‘Available Assignments’ page.

#### My Proposals

##### An artist wants to see all his proposals

-	The ‘My Proposals’ page offers a list with all proposals that were posted by the current artist correctly;
-	If the artist has done no proposals yet, a message will be visible saying the artist has done no proposals yet.

##### An artist wants to edit or delete a proposal

-	When clicked on the ‘Edit Proposal’ button, the artist is redirected to the ‘Edit Proposal’ page.

#### Edit Proposal

##### An artist wants to edit the proposal

-	All forms are filled in with the values of the proposal correctly;
-	An artist can edit these fields;
-	When clicked on the ‘Save Changes’ button, the proposal is correctly edited in the database and the artist is redirected to the ‘My Proposals’ page.

##### An artist wants to delete the proposal

-	When clicked on ‘Delete Proposal’, a modal appears which asks if the artist really wants to delete the proposal;
-	When clicked on ‘Delete Proposal, the proposal is correctly deleted from the database and the artist is redirected to the ‘My Proposals’ page;
-	If the artist does not want to delete the proposal, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

##### An artist wants to get back to see all available assignments

-	When clicked on the ‘Back to Assignments’ button, the artist is redirected to the ‘Available Assignments’ page.

### Client Pages

#### My Assignments

##### A client wants to see all his posted assignments

-	The ‘My Assignments’ page offers a list with all assignments that were posted by the current user correctly;
-	If the client has no running assignments, a message will be visible saying the client has no running assignments.

##### A client wants to see the details of a specific assignment

-	When clicked on the ‘View Details’ button of an assignment, the artist is redirected to the ‘My Assignment Details’ page of that specific assignment correctly.

##### My Assignment Details

##### A client wants to see all details of an assignment

-	All data of the specified assignment is viewed correctly. All data appears as it should. If the client has left out some input data, that data does not appear.

##### A client wants to get back to see all his posted assignments

-	When clicked on the ‘Back to Assignments’ button, the client is redirected to the ‘My Assignments’ page.

##### A client wants to delete the assignment

-	When clicked on ‘Delete Assignment’, a modal appears which asks if the client really wants to delete the assignment;
-	When clicked on ‘Delete Assignment’, the assignment and all corresponding proposals for that assignment are correctly deleted from the database and the client is redirected to the ‘My Assignments’ page;
-	If the client does not want to delete the assignment, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

##### A client wants to see if he has any proposals from artists for his assignment

-	At the bottom of the page the proposals of artists are displayed. If the assignment has no proposals yet, a message will be visible saying the client has received no proposals yet.

#### New Assignment

##### A client wants to submit a new assignment

-	The client should fill in the required forms;
-	When clicked on the ‘Submit Assignment’ button, all forms are validated correctly;
-	If all forms are valid, a modal appears which asks if the client really wants to submit the assignment;
-	When clicked on ‘Submit Assignment, the assignment is correctly created in the database and the client is redirected to the ‘My Assignments’ page;
-	If the client does not want to submit the proposal, both the ‘Close Button’ and clicking the area around the modal, will close the modal.

### Different mobile devices

##### The user wants to view the site on its preferred mobile device

-	Responsinator.com was used to see if all data is viewed correctly on mobile devices. It has been confirmed that it does so.

### Different desktop browsers

##### The user wants to view the site on a desktop computer

-	The website has been tested in FireFox and it functions correctly;
-	The website has been tested in Internet Explorer and it functions correctly;

## Deployment

### Run Project Locally

You can run the project locally in your IDE by following these instructions:
PIP, Python3 and Git need to be installed on your computer
1.	On the GitHub repository of Custom Artist, click clone or download;
2.	Click ‘Download ZIP;
3.	Unpack the downloaded ZIP file;
4.	Open the index.html file with your preferred browser;
5.	Install Flask by entering pip install flask in the terminal of your IDE

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

## Credits

All content was on the website was conceived by myself, except for the following content.

### Media

### Acknowledgements
