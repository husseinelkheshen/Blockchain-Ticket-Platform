# Admit_01 Blockchain-Enabled eTicketing Platform

## Milestone 3b

### How to Compile
Since our code is written in Python, there is no need to compile.

### How to Run Our Code
Before doing anything else, you must execute 'make install' from the main directory in order to install the correct versions of pytest and pyqrcode.

To run frontend code, visit http://128.135.203.173:8000. You can click on the login link in the navbar to visit the login form.

To login as a customer (someone who can buy tickets), use the following credentials:
* username: joe
* password: chicagomaroon

To login as a venue (someone who can list tickets), use the following credentials:
* username: staff
* password: chicagomaroon

You can logout by visiting the logout link in the navbar as well.

The completed wireframes in HTML/CSS can be viewed from 'design/html_wireframes' in any browser. Bootstrap has already been downloaded into thhe project, and Popper.js is being grabbed from a CDN.

### How to Run the Unit Test Cases
You can use the Makefile to do so by executing 'make unit_tests' from the main directory. Please note that some of these tests may take upwards of two minutes to execute due to the rigor of the mining, and it occurring on the local machine.

To run the jasmine test cases for form validation, you just need to open 'tests.html' in the 'tests/frontend' folder  any browser that formats CSS remotely corretly. Jasmine provides a css formatted standalone testing framework for testing javascript used in HTML. If you want to know the details of installation they are on
https://github.com/jasmine/jasmine#installation, using the installation instructions for the standalone distribution. Very few changes were made to the validation tests, everywhere a change was made was marked with a "NOTE:" comment and some exclamation points. Explanation for changes are written in comments around changes. Likely more will get written as validation becomes more rigorous. The tests were all passing at the time of writing this. The jasmine tests themselves are written in the file 'validation_tests.js', and test the code written in 'validation.js'. Both of these files can alo be cound in the 'tests/frontend' folder.

### Suggestions for Acceptance Tests
To walk through our backend acceptance test, run this from terminal in the main directory:
make acceptance_test

This will walk you through all of the use cases, and finally save a .png file of the QR code of the ticket you will end up with. You will want to use reasonable ticket prices (less than $999,950) in order to get through the entire simulation without running out of money. The program will handle inadequate funds appropriately, but you will not get to the end of the use cases.

You can test our application's authentication system by attempting to login on the preliminary site with correct and incorrect credentials (the credentials were enumerated in the **How to Run Our Code** section).

Although the frontend and server end of buy and list ticket is implemented, acceptance testing is
not stable as the frontend currently cannot display available tickets as that was not planned for iteration 1. Thus, the request server (where Django is run), cannot get a ticket from the blockchain server that it can purchase or list.

### What is Implemented?

#### Front end
The request, database, and blockchain servers have been created and can successfully communicate with one another. The blockchain server receives requests from the request server to modify the blockchain, and the request server in turn receives requests from a user's browser and returns responses generated by a web application (Django) that displays info retrieved from the blockchain and database servers.

Additionally, a primitive version of a web application has been implemented, and can be accessed via a browser. Users can, if already registered in the system (at this point, registration can only be done through Django's admin interface, which is accessible at 128.135.203.173:8000/admin), login to the site. The authentication system is fully capable and implemented. The site recognizes that a user is signed in through a sessions framework.

The html/css wireframes have been fully marked up for all pages that serve the stated goals of compeleting Upgrade Ticket, Generate Ticket Code, Buy, Ticket, with the exception of the Create and List ticket. Since have still yet to implement mass generation of ticket blocks and have yet to determine how we will streamline the process venues creating tickets from the website, we thought it best not to waste the time marking up a wireframe that probably wouldn't get used. Time was spent instead marking up the Account page for users since many of the design goals for the week focused on how to create tickets for users. The Logo has also been finalized, and a favicon for the website.

The idea behind the CSS wireframes is that a home page will be required, which is what is found in 'index.html'. This homepage is incomplete as the explore feature will likely be implemented on it as well. An event page would be needed to buy tickets from, found in 'event_page.html', an actual ticket purchase confirmation page on 'purchase.html'. Wireframes for a login/resistration page in the form of 'login_register.html' and an account page on 'my_account.html' were provided as well.

#### Back end
On the back end, we have fully implemented the blockchain framework and currently have our transactions posting to two nodes (one held by the Event class, another held by the Venue class), though we are currently only using single-node validation. We will develop a three-point consensus mechanism in the second sprint, as planned.

In terms of use cases, we have fully and successfully implemented **Create Ticket**, **List Ticket**,  **Buy Ticket**, **Upgrade Ticket**, and **Generate Ticket Code**.

### Who Did What?

#### Front end
Pablo worked on creating virtual machines for the request, database, and blockchain servers. He also integrated the code written by the back end team so that the blockchain could communicate with the server instance on the blockchain server machine.

Euirim worked on setting up the virtual machines with frameworks that would help us expediate development. He also setup the Django-based web application and coded the client-facing html that displayed a very primitive interface. Euirim also integrated the database server with the Django hosting request server.

Samantha wrote all of the HTML/CSS, Provided all the UI design, logo desin, and wrote the Jasmine font end validation tests.

#### Back end
Ross and Ethan paired to develop and test the *Trackers*, *User*, *Venue*, *Event*, *Seat*, and *Ticket* classes.

Hayden and Hussein paired to develop and test the *Block*, *Chain*, and *Transaction* classes.

We met together as a larger team on a few occassions to integrate our components and complete the implementations of the use cases.

### Changes from Implementation Plan
There were several several, code correctness, test rigor, formatting and changes to the unit tests, none of which changed the scope or diminished the coverage of the tests.

The only major change is that we incorporated the *Host* class into the *Venue* class, since we could no longer see a logical purpose for a standalone *Host* class. *Venue* objects now have access to the union of all use cases from the previous definition of *Host* and those from the previous definition of *Venue*.

A minor change, as already discussed, resulted from ambiguity about how list ticket will be implemented on a venue wide scale, which meant holding off on UI design of it for the time being.


## Milestone 4a

### What Will Be Implemented?

#### Front end
In this iteration we will implement the web portal, which enables venues to create and manage events, create and manage tickets, schedule ticket releases, and validate tickets. We will also wireframe other aspects of the site (described below), and create a visualization for venues hosting events so that they may visualize the status of their ticket sales.

The API and request servers will also have implemented endpoints for genertaing ticket codes, validating tickets, searching for events. We will also implement endpoints that allow venues to mange their events. These include creating multiple tickets at a time, editing tickets, editing events, and scheduling releases of tickets.

We will implement full authentication for users and venues on the web server as well that is consistent with the Blockchain.

#### Back end
In this iteration we will implement more aspects of security for our blockchain framework, new ways to find events for users, as well as a few final use cases for events and venues which will complete each respective class and allow for more comprehensive control of tickets and events.

Our added security aspects will include a triple check (consensus checking algorithm) between each of the two blockchains held by *Venue* and each *Event* respectively, and the individual history held by each *Ticket*, in order to validate new transactions which occur, a robust generation of QR codes for each ticket (**Generate Ticket Code**), as well as a validation method for tickets when a given QR code is scanned (**Validate Ticket**).

Each *User* will be able to discover new events in two ways. Users will be able to search (**Search**) by artist, location, time, and tags. Users will also be able to explore (**Explore**) existing events through a recommendation algorithm based on prior interactions with events. Explore will select from active events based on a simple perceptron neural net which updates user preferences for features of the events for which they see, list, buy, and upgrade tickets. Users will then be able to ‘like’ or ‘dislike’ each suggested event, allowing them to further build their preferences and discover new events.

In order to complete the *Event* and *Venue* classes, we will be finalizing comprehensive creation and management of tickets and events. To make the creation of tickets easier, each venue will be able to create multiple tickets at a time (**Create Tickets**). Venues will be able to change attributes of tickets they have created (**Manage Ticket**), events they are hosting (**Manage Event**), as well as schedule a release time for tickets they have created (**Schedule Release**). We will also be implementing an easier and more controlled way for venues to create events (**Create Event**) to avoid any potential issues.

(**New tests for iteration 2 can be found in Blockchain-Ticket-Platform/tests/back_end and include:**)


Test_Explore.py

Test_ManageEvent.py

Test_ManageTicket.py

Test_ReadWriteValidation.py

Test_ScheduleRelease.py

Test_Search.py

Test_Trackers.py

Test_ValidateTicketCode.py



### Workload Division

#### Front end

Samantha will frame the event portal which enables venues to create and manage events, create and manage tickets, schedule release, and validate tickets. She will also modify existing wireframes for the search funciton, and wireframe event listings for the explore and search functions. She will also code a visualization in d3.js that allows the host of an event to visualize the state of the ticket blockchain.  

Euirim will design and implement the request forms for the web server and the requests between the API server and the web server. Pablo will integrate the aforementioned API endpoints with the Blockchain backend.

#### Back end

Hayden and Hussein will pair up to write **Validate Ticket**, **Manage Tickets**, **Manage Event** and **Schedule Release**

Ethan and Gina will pair up to write **Explore** and **Create Event**

Ross will write **Search**, **Create Tickets**, and implement the consensus mechanism described earlier

We have met, and will continue to meet as a larger group in order to discuss approaches, integrate our components, and finalize our implementations of the various use cases.

### Discussion

We have not altered anything significantly from our original plan. We will be, however, adding numerous additional components in order to truly sure up the security of our blockchain infrastructure, and in order to ensure scalability as if our platform were to be implemented in real life (e.g. more robust creation of QR codes, proper privacy constraints).

It will be difficult to properly unit test **Explore**, as proper functioning will be adaptively based on user preferences established over a history of their use of the platform. However, we will do everything possible to test proper form of inputs and outputs, as well as basic cases of learning.

A few more form validation tests have been coded and added to the already existing front end validation tests. Where the tests have been added has been marked on the page.

## Milestone 4b

### How to Compile
Since our code is written in Python, there is no need to compile.

### How to Run Our Code
Before doing anything else, you must execute 'make install' from the main directory in order to install the correct versions of our packages.

If you encounter an error which says CERTIFICATE_VERIFY_FAILED, please read the note below. This, of course, won't be an issue in the final deployment of the software since it will be a web app running on a remote server.

Skeleton code for events to view the visualization fo their ticketing blockchain can be found at 'design/html_wireframes/ticket_visualization_demo.html', and the javascript utilized to write the visualization function is in the js folder under 'ticket_visualization_demo.js'. The html can be pulled up in any browser, with chrome likely being the best to view the visualization in.

To view the basic UI/database website integration code, where you can perform the following functions
Navigate to http://ec2-18-219-133-194.us-east-2.compute.amazonaws.com:8000/

Testing Basic standard User UI integration
- Click register
- Enter Information and Register the user as a Customer
- Name should appear in upper right hand corner
- Click Logout once on the welcome page
- Login using the same credentials
- Name should disapper from upper right hand corner
- Name should appear in upper right hand corner
- Logout

Testing Basic event UI integration
- Click register
- Enter Information and Register the user as a Venue using a different using a different email
- The name you entered when registering should appear in the upper right, click on it
- See skeleton for an event profile page
- Logout
- Name should disappear from upper right hand corner
- Login using the same venue credentials
- Name should appear in upper right hand corner again
- Logout
- Name should disappear from upper right hand corner again


To view non integrated django templating engine, navigate to http://ec2-18-219-133-194.us-east-2.compute.amazonaws.com:8001/
The extensions are as follows to view the following pages:
- To view the home page, either no extension or 'home/'
- To veiw the event home page, 'event/'
- To view the normal login page 'login_register/'
- Event login page 'event/login_register/'
- To view an event's page on the main site 'detail_event/'
- Mock search results page 'search/'
- Mock explore results page 'explore/'
- Mock purchase page 'purchase/'

All of these templates are being served with dummy formatted data, so all that remains is to integrate the code that gets the data with the actual templates themselves


#### SSL CERTIFICATE VERIFICATION

Note: For Mac users who have not already enabled Python to install certificates, please run the following command from the Terminal including the quotation marks:

"/Applications/Python 3.x/Install Certificates.command"
(Replace x with your installed version of Python, for example 3.5 or 3.6)

If the terminal command does not work, please search "Install Certificates.command" on Finder, using the This Mac setting (search whole computer).
Once the file is found, please double click on it. It should execute in Shell and permit Python on your machine to install certificates.
Our Explore functions depends on a package which requires SSL certification to be downloaded.

### How to Run the Unit Test Cases
You can use the Makefile to run our test cases by executing 'make unit_tests' from the main directory. To store the outputs of the unit tests as .log files in './tests/back_end/pytest_logs', you can run 'make unit_tests_log' instead.

If you wish to only run the unit_tests that are new since the last iteration, you can instead run 'make iter2_unittests' or 'make iter2_unittests_log' (if you'd like to store the pytest logs, as described above).

### Suggestions for Acceptance Tests
To test API: Our API acceptance tests use the REST client Insomnia (https://insomnia.rest/download). To see our tests, import `tests/front_end/insomnia_api_tests.json` into Insomnia. Once that is done, the tests should appear in logical order, from top to bottom. Our API acceptance tests test the integration of the front end requests that the server makes to API library calls written by the back end team. Some implementation familiarity is necessary to edit the tests, but they are intuitive to read and therefore it is easy to validate its output. Failures in the API due to improper parameters should return helpful failure messages. Successful API calls return easily readable JSON messages.

### What is Implemented?

#### Front end
On the front end, we have achieved integration with the request API server to the Python backend. We are able to make requests from our server to the python server as well as manipulate and interact with our database. In addition to fully integrating our API server, we've also complete the django templating engine for the website UI and, as well as having achieved basic integation of the API server and the website UI views.

Skeleton code for a blockchain visualization was also implemented. This visualization was proposed as an important measure for events and venues to be able to visualize the state of their ticketing block-chain as a way that distinguishes our ticketing blockchain from normal ticketing software. However, since this was not included in the original design plan, we eventually thought it best not to spend more time than necessary and just leave it as conceptual skeleton code that demonstrates the uniqueness of the ticketing blockchain, albeit not fully implemented.

#### Back end
On the back end, we have developed a three-point consensus mechanism, as planned, to serve as the fault-tolerance basis of our blockchain. We have also implemented a quick hash-based validation algorithm to ensure consistency across nodes prior to any reads and writes.

In terms of use cases, we have fully and successfully implemented **Explore**, **Search**,  **Validate Ticket**, **Create Event**, **Schedule Release**, **Manage Event**, and **Manage Tickets**, as well as a 'plural' form of Create Ticket called **Create Tickets**, which is more practical for real-world situations. To assist with Manage Tickets, we also wrote a helper function **Venue Tickets** which traverses the blockchain to produce a list of ID numbers for tickets belonging to the Venue for a given event. This was also fully implemented and unit tested in Test_VenueTickets.py. We made minor security improvements to **Generate Ticket Code** and other peripheral helper functions as well to better integrate the fault-tolerant properties of the blockchain.

### Who Did What?

#### Front end

Pablo created the remaining Flask endpoints for the Blockchain API besides **Validate Ticket**. Pablo also created acceptance tests for these API endpoints. Finally, Pablo began to implement the API/Django integration.

Euirim implemented the Request server and the the beginning fully integrated UI to server templates

Samantha wrote the django UI templating engine for the html wireframes developed during the last sprint, as well as writing wireframes for the event portal of the website and the code for a blockchain data visualization.

#### Back end
Gina and Ethan paired to develop and test **Explore**.

Ross implemented and tested **Search**, **Create Event**, and **Create Tickets**, as well as adding the consensus mechanism to the already-implemented Ticket.mostRecentTransaction() function.

Hayden and Hussein paired to develop and test **Manage Event**, **Manage Tickets** (and its helper **Venue Tickets**), **Schedule Release** (and its helper **Check Release**) and **Validate Ticket Code**, as well as improving the security of our already implemented blockchain infrastructure by adding a read-write validator (**rwValidation**) function that quickly validates the blockchain prior to any read or write access to it.

### Changes from Implementation Plan
For the back end, there were several minor test rigor and formatting changes to the unit tests since they were delivered with 4a, none of which changed the scope or diminished the coverage of the tests.

For the front end, while we were able to achieve integration with the request server with the back end library calls, we weren't able to achieve full ui to back-end integration of the software. Because we don't learn a particularly great deal about how to integrate codebases, system architectures, and front end in general in the CS department and because we obviously had envisioned a finished product, we vastly underestimated the amount of code that is required to achieve fully integrated software from the back ends of library/api to the more minute detailed coding of ui that has to be able to interact with users and deal appropriately with user behavior. There was also the unanticipated time cost of having to create manage the system architecture with the servers not always being fully reliable and functional. That being said, while we deviated from the design goal of having a fully integrated website, we did manage to integrate the front end and the back ends, as well as building a templating engine for the UI that functions with dummy data that models the actual data context of the server.
