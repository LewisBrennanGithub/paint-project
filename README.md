# paint-project

The idea is to have a display of various paint colours! The basic concept is that each page will have two colours, a MAIN(side-bar-menu/main-body-text) colour and an OFFSET(side-bar-text/main-body-background)colour!

The user can select existing colours, but can add new colours in using rgb/hexidecimal, or maybe just add some presets. The MAIN colour will determine the offset colour.

MVP:

- Set up a website that has two sections, a nav-bar (likely on the side, perhaps adapted to the top for mobile(extension?)), and a body. 
- The website will allow users to select various paints, represented by an icon on the screen.
- The website will also allow users to add, remove or update existing paints.

EXTENSION:

- The website will use the paint selected to change the backdrop of the body.
- Deleting the paint will drain the page of colour.
	
ADVANCED EXTENSION:

- The main page colour will be used to offset the navbar colour. 
- The nav-bar text will reflect the body colour, and the body text will reflect the nav-bar colour.
- Users can vote for their favourite colour, and this will be represented as the default page colour.
- Possibly allow multiple colours on page at a time, with the navbar reflected. Only one colour for each text, the left-most/first colour to be selected.

RUN THE PROGRAMME

- Open a terminal session
- Clone the repository
- Requires: flask / psychopg2 (pip3 psychopg2) / postgres 
- dbcreate paints
- To set up seed data cd into the db folder and use the following command: "psql -d paints -f paints.sql"
- Navigate back to main and type flask run
- In the browser use the url: "localhost:4999" 
