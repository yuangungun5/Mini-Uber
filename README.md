# ERSS-hw1-qx37-yz553

This is a Django web-app for ride share service. Users can request a ride, or search and join an open ride, and also can register as a driver to search and accept a request.

## Functions Introduction

1. Create a user account<br/>
The website has a header with "Login" and "Register" on the right side when user doest not login. If user clicks on "Register", then the website page will forward to a registration form which has fields "username", "email", "password" and "password confirmation". If the input information is not valid, the corresponding warning messages will alert. If the user already has an account, there is a "sign in" URL at the bottom to log in.

2. Login with a valid user account<br/>
If user clicks on "Login", the page will forward to a login form which has fields "username" and "password". If the user is new to the website, there is a "sign up" URL at the bottom to register. If both username and password are valid, the website will forward to the homepage.

3. Handle login failure with an an invalid user account<br/>
If username or password is not correct, the warning messages will be issued. 

4. Logout from a user session<br/>
After user logs in, there is a "Logout" headline on the right side. When clicking on "Logout", the website will forward to the logout page with message "You have been logged out".

5. User can register as a driver by entering their personal & vehicle info<br/>
After user logins in, there is a "Account" headline on the right side. When clicking on "Account", the user profile will be displayed. If the user does not register as a driver, there is a "Driver Registration" choice at the bottom. When user clicks on "Driver Registration", or user can click on the "Driver" on the right side of header, then the website will forward to the driver enrollment form which has fields "name", "is driver", "licence", "car id", "level", "max passenger" and optional "special". User must confirm "is driver" option to register as a driver.

6. User can view and edit their driver status as well as personal & vehicle info<br/>
By clicking on the "Account" headline, user can modify their personal information as well as driver information.

7. User can submit a ride request by specifying the required and any combination of the optional info<br/>
User can request a ride by clicking "Owner" on the top and then filling the request form with fields "start", "destination", "date arrival"， "passenger num" and optional "capacity level", "is shared", and "note". 

8. User can make a selection to view any non-complete ride they belong to<br/>
By clicking "MyRide" on the left side of the header, user can go to the list of history orders with order status. Each order has a URL connected to the detail page. If the order is still open, then user can edit or cancel the order; if the order is confirmed by a driver, then the driver information will be listed on the detail page, and user cannot edit the order anymore. 

9. User can make a selection to edit any open ride they belong to

10. A ride owner can edit the requested attributes of a ride until that ride is confirmed

11. User can view all ride details for any open ride they belong to

12. User can view all ride details + driver and vehicle details for any confirmed ride they belong to

13. User can search for sharable, open ride requests (by destination, arrival window, and number of passengers)<br/>
By clicking "Sharer" on the top-right of the website page, user can fill in the requirements of "destination", "passenger num", "arrival after" and "arrival before" then start searching.

14. User can join a ride returned in a search<br/>
The search results will be listed according to the arrival time. By clicking the title of the order, user can check details of the order and choose "join the ride". After user confirms sharing, the owner who intiated the request will receive an email notification.

15. A registered driver can search for open ride requests (filtered by the driver's vehicle capacity and type / special info, if applicable)<br/>
By clicking "Driver" and choose suitable arrival window, driver can obtain the results filtered by the arrival window and the vehicle information that driver registered.

16. A registered driver can mark a selected ride (returned from a search) as confirmed (thus claiming and starting the ride)<br/>
Clicking the title of the order, driver can check the details of the order and confirm the order. After that, the passengers (owner and sharer) will receive the email notification.

17. An email should be sent to the owner and sharer of a ride once it is confirmed by a driver<br/>

18. A driver should be able to see a list of their confirmed rides<br/>
Cliking "MyDrive" on the top-left, driver can go to the list of history orders with order status. Each order has a URL connected to the detail page. The details include "arrival time", "shared or not", "sharer", "how many passengers" and special note.

19. A driver can select a confirmed ride and view all of the ride details
20. A driver can edit a confirmed ride for the purpose of marking it complete after the ride is over<br/>
On the detail page of the order, if the order status is still open, then driver can complete the order and change the order status.<br/>

## Possible Problems

The email host used in this web-app is 163-mail. Email sending works for gamil but the sent email may be handled as trash mail. If the receiver is an outlook user, then the email connection may be refused.<br/>