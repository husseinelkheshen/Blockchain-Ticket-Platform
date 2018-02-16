# Admit_01 Blockchain-Enabled eTicketing Platform

## Milestone 3b

### How to Compile
Since our code is written in Python, there is no need to compile.

### How to Run Our Code
Before doing anything else, you must execute 'make install' from the main directory in order to install the correct versions of pytest and pyqrcode.

@Euirim please explain how to run some simple UI implementation of the use cases

### How to Run the Unit Test Cases
You can use the Makefile to do so by executing 'make unit_tests' from the main directory.

### Suggestions for Acceptance Tests
use: make acceptance_test
This will walk you through all of the use cases, and finally save a .png file of the QR code of the ticket you will end up with.

### What is Implemented?

#### Front end
@front-end-dev-team fill this in

#### Back end
On the back end, we have fully implemented the blockchain framework and currently have our transactions posting to two nodes (one held by the Event class, another held by the Venue class), though we are currently only using single-node validation. We will develop a three-point consensus mechanism in the second sprint, as planned.

In terms of use cases, we have fully and successfully implemented **Create Ticket**, **List Ticket**,  **Buy Ticket**, **Upgrade Ticket**, and **Generate Ticket Code**.

### Who Did What?

#### Front end
@front-end-dev-team fill this in

#### Back end
Ross and Ethan paired to develop and test the *Trackers*, *User*, *Venue*, *Event*, *Seat*, and *Ticket* classes.

Hayden and Hussein paired to develop and test the *Block*, *Chain*, and *Transaction* classes.

We met together as a larger team on a few occassions to integrate our components and complete the implementations of the use cases.

### Changes from Implementation Plan
There were several minor formatting and code correctness changes to the unit tests, none of which changed the scope or diminished the coverage of the tests.

The only major change is that we incorporated the *Host* class into the *Venue* class, since we could no longer see a logical purpose for a standalone *Host* class. *Venue* objects now have access to the union of all use cases from the previous definition of *Host* and those from the previous definition of *Venue*.