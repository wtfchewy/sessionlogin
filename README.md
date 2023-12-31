# Login Session - WIP
A session/cookie based login system that allows you to attach no personal information to users and keep them private using only account numbers/keys.

## What is the point?
The point of a system like this is for your users to have complete anonymity. There are no passwords, usernames, or ip addresses that can trace back to a user. You can see a similar usage of this by [MullvadVPN](https://mullvad.net/en).


## Routes
- ``/:`` The home page of the application. If the user is signed in, their account number is displayed. Otherwise, a message indicating that the user is not signed in is displayed.
- ``/login:`` A login page that allows the user to sign in with their account number. If the account number is valid, the user is redirected to the home page. Otherwise, an error message is displayed.
- ``/signup:`` A page that creates a new account with a randomly generated account number. The user is then signed in and redirected to the home page.
- ``/logout:`` A route that clears the user's session and redirects them to the home page.
- ``/dashboard:`` TBD
- ``/test:`` A test page that displays a list of all accounts in the database.

## Preview
### Home
![Home](https://media.discordapp.net/attachments/1047336119580242001/1190890998763630652/sessionLogin.jpeg?ex=65a372ab&is=6590fdab&hm=50f2c6c806da80031ba03db76844dbda6c0c879fb9a02664857e3576982e3ca9&=&format=webp&width=771&height=536)
### Login
![Login](https://media.discordapp.net/attachments/1047336119580242001/1190890999283712050/sessionLogin_11.34pm_12-30.jpeg?ex=65a372ab&is=6590fdab&hm=d70bd5f84e57f87a96e0e548cf27e49b8f61ab79e82462c784cc21d5bd9bbded&=&format=webp&width=771&height=536)
### Logged in Home
![LoggedinHome](https://media.discordapp.net/attachments/1047336119580242001/1190890999023685677/sessionLogin_11.35pm_12-30.jpeg?ex=65a372ab&is=6590fdab&hm=da3fe762afa11ac61c5c5143fdf973132362ec9c1207c893d5a339cb7653df87&=&format=webp&width=771&height=536)
