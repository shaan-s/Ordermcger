# Introduction
Ordmcger is a Pygame-based application for managing the stock, inventory, and prices of items. It was created in Fall 2019. It is limited in its scope and was mostly a proof-of-concept for making non-game applications in Pygame (inspiring me to explore future projects like [Trascii](https://github.com/shaan-s/Trascii)).
![image](https://github.com/user-attachments/assets/ac68e18f-bf3c-4189-92c1-4c3520945a13)

# Usage
Ordmcger consists of a menu and 3 screens. All interactions are keyboard controlled (arrow keys and enter). The user can add new items, increase/decrease their stock, and modify their names and prices.

![image](https://github.com/user-attachments/assets/889dbc82-939f-4dbd-b586-f377ae7754f8)
The menu screen


![image](https://github.com/user-attachments/assets/dedb8f3e-8d8d-415c-9a31-8124b7907de9)
"Check info" which allows the user to view the database.


![image](https://github.com/user-attachments/assets/b7e29231-f9e2-433c-8704-66e5139c6111)
"Place order" where the user can select an item and decrease the stock by one (would theoretically be used at point-of-sale). Low stock items are displayed in warning colours.


![image](https://github.com/user-attachments/assets/95165d02-8862-4c6a-a04a-efe0a627c5d1)
"Edit data", where the user can edit the names, prices, and stock in a table-like array. The margins are calculated from the prices. 

# Installation
Make sure the latest version of Python is installed. The package `pygame` must be installed first. The font `bahnschrift` should also be installed on the system.

`pip install pygame`

`git clone https://github.com/shaan-s/Ordermcger`

Then run `ordmcger.py`.
