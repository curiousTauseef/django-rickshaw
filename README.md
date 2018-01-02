## Django Rickshaw

Rickshaw is a handy shopping cart experience for the Django framework **(2.0 only)**.

## Features

- Session based persistent shopping basket, stores record in DB
- Convert to wishlist for later use
- Celery tasks for reminding customers cargo is left in their rickshaw (only if registered user) (also management command)
- Custom management command for DB housekeeping
- Wrapper class to make things dry :cocktail:
- Signals setup and ready to go
- Custom configuration via settings.py

## Installation
***Coming Soon :sweat_smile:***

## Overview

***Say a user visits your website and your selling t-shirts, he finds a top he likes and clicks add to basket.***

The user has already had a rickshaw assigned and is now able to add cargo to their rickshaw. The user can then leave and come back and his items will still be there, at least until his session expires. If that user then wants to save this for a wishlist, we can store the users rickshaw and cargo in the database.

***Lets say this user forgot that he had an item left in the basket***

Either through CRON or Celery the user is notified so long as they have made an account, they will recieve and email saying you've left some items in your basket, similar to Amazon and other big brands.

***That user then buys the item***

Using the wrapper class, you can configure the rickshaw depending on the outcome from your payment provider.

## Instructions
***Coming Soon :sweat_smile:***

 