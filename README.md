# Python-tkinter
Food Delivery System using python-Tkinter which features signup, log in, Restaurant selection, food item selection, checkout, confirmation via email, order status using google map
<br>

### Packages

| Required Packages  | Installation Process  |
| ------------------ | --------------------- |
| os  | pip install os  |
| PIL  | pip install PIL  |
| Sqlite3  | pip install sqlite3L  |
| smtplib  | pip install smtplib  |
| tkinter  | pip install tkinter  |
| time  | pip install time  |
| randon  | pip install random  |

***

### Setting Credentials and APIs

This project uses Google APIs for sending mails and viewing order status on google map.<br>
create API: "https://www.youtube.com/watch?v=I5ili_1G0Vk"<br>
<br>
After creting API key set below variables in Application.py file.<br>

<ul>
<li>sender : sender's email id</li>
<li>password : sender's email password</li>
<li>API_KEY : generated API Key</li>
</ul>



***

### Execution process

<ul>
<li>Open command prompt at the project folder location</li>
<li>Enter as below in command prompt:
</li>
<li>python main.py</li>
<li>A window will get popped up.</li>
<li>Then proceed as shown in window.</li>
</ul>

***

### Project features
<ol>
<li>Sign Up</li>
<ul>
<li>If a new user comes in, he/she needs to sign up.</li>
<li>Over there, details like name, email, password are asked.</li>
<li>A warning is displayed if any wrong info is passed or if any field is left empty.</li>
<li>If everything goes fine then, user is signed up and his information is added to database file. (This is an actual database file. It is not stored in any kind of array, rather in a table in database file.)
</li></ul>
<li>Sign In</li>
<ul>
<li>Enter email address and password and user gets logged in (After verifying in table in database).</li>
<li>A warning is displayed if any wrong info is passed or if any field is left empty.</li>
</ul>
<li>Address</li>
<ul>
<li>Delivery address information is asked over here.</li>
<li>Over here, it is mandatory to enter valid 6-digit zip code.</li>
<li>A warning is displayed if any wrong info is passed or if any field is left empty.</li>
</ul>
<li>Restaurant selection</li>
<ul>
<li>Select the desired restaurant from the application.</li>
<li>User can reselect the restaurant if he/she doesn’t like menu of a restaurant by pressing back button.</li>
</ul>
<li>Food selection</li>
<ul>
<li>Select food items you want to add to cart.</li>
<li>User can select another restaurant by pressing back button.</li>
<li>Select a particular item and then user will be asked to add toppings (if any) and quantity of respective food item.</li>
<li>After selecting toppings, it will be added to cart which will be shown on right hand side of window.</li>
</ul>
<li>Checkout</li>
<ul>
<li>Your profile and delivery address are shown here.</li>
<li>Along with that, food items in cart are also shown here.</li>
<li>Then, select your payment mode and proceed to confirmation window.</li>
<li>Note: It may take some time to pop new window as it sends email for confirmation.</li>
</ul>
<li>Confirmation</li>
<ul>
<li>An OTP will be sent to user’s email.</li>
<li>Enter that OTP to confirm order.</li>
</ul>
<li>Order status</li>
<ul>
<li>Order confirmation status will be displayed here and also an email will be sent saying the same.</li>
<li>After a period of 5 seconds this window will disappear and Login window will pop up.</li>
<li>Note: It may take some time to pop new window as it sends email for confirmation.</li>
</ul>
</ol>


