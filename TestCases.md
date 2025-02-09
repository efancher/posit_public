# Posit take home

Expected test time ~ 15 minutes

## Assumptions

* Greenfield test case - I don’t assume any existing data
   
* Per requirements use of R Studio projects is limited to creating content.
  
## Motivation

   I feel that in this type of application, what we’re interested in is 
   
* Content Creation on the cloud
* RBAC - Can we share/delegate access to others

## Exclusions

  Security, Localizability/localization, Input Partitioning, Performance and some others

   So in that spirit, given the time limits. I would focus on a positive functionality test that covers basic content creation, sharing and RBAC permissions. I focused on Viewer initially, since it seems most likely users will want to be sharing with many who only have read access.

## Browsers

* Since time is a constraint, I would recommend mixing the three main browsers for each step, maybe just in a random order: Chrome, Firefox, Safari

* If available, splitting the run on the 3 main OS's would be a good idea: Widnows, MacOS, Linux

In my approach, I try to make things systemic, so the test is automatable and can be separated if there are others that can assist.

## Test Cases

### Create Account ~ 1 minute
In a web browser, got to posit.cloud
* Signup using an existing email/password
* May need to verify email, so it should be a real account you have access to.

Variations (Other auth services, email/password), TBD

### Initial Setup/Content Creation ~ 2 minutes
* Create new workspace 
* Create new R studio project 
* Change the project name at top 
  *  Open options (verify name changed in options)
  *  Add a description
* Go to resources
  *  Verify can decrease/increase within limits, write down the new values
* Create shiny app per https://docs.posit.co/cloud/get_started/ (~ 1 minute)
  *  Variations (other content types, TBD)

* Go back to content page 
  *  Verify project name is updated name
  *  Verify description is the one set
  *  Verify app is published per the name you’ve given it
* Open the project again, go to resources
  *  Verify the resorces reflect the updated values



### Add new member ~ 1 minute
* Create an additional user per the signup above
  
(As a note, if you have a gmail account posit does not consider myname@gmail.com and myname+posit@gmail.com as the same account, but google does, making it easier to keep track)

  *  Create as Viewer
  *  Variations (Admin,Moderator, Contributor)
* Click on the ellipses button, then settings for the shiny app
* Click on Access, Change the access to space members

* Log out


### Verify correct access for a Viewer member ~2 minutes

* Sign in as new Member
* Verify you can see the shared workspace
* Open the workspace
* Verify the new project doesn’t show up
* Verify you don’t get the usage menu item for the workspace
* Click on the shiny app name
* Verify you can see the running version of the app (not the project version)
* Logout

### Repeat With Admin ~ 3 minutes

Using the Viewer Test as a template

* Go to main account and change secondary member to Admin
* Go back to secondary account.
* Changes from Viewer test -
*  Verify can
  *  Delete old project
  *  Create a new project
  *  Publish shiny app
  *  Access Members page (With more time, might be better to do this with an additional account to be able to make changes)
  *  See Usage


### Repeat With Moderator ~ 3 minutes

Using the Viewer Test as a template

* Go to main account and change secondary member to Moderator
* Go back to secondary account
* Verify can
  *  Delete old project
  *  Create a new project
  *  Publish shiny app
  *  NOT Access Members page
  *  See Usage


### Repeat With Contributor ~ 3 minutes

Using the Viewer Test as a template

* Go to main account and change secondary member to Contributor
* Go back to secondary account
* Verify can
  *  NOT view project
  *  Create a new project in the shared workspace
  *  View shiny app
  *  NOT Access Members page
  *  NOT See Usage

## Optional

* If time, go back and verify you can delete all content/additional members.
* And, verify you can move deleted content to archive and restore it.

           

