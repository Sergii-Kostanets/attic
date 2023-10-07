# **Attic Shop**

*Attic* is a e-commerce project dedicated to cameras, lenses and accessories for them. All visitors can buy products, create their own user profile to start adding products to their wishlist and leave reviews. All reviews need approval by *Attic* website owner so everyone can feel safe from abuse, inappropriate language, etc. The approvals are being made from website UI pages that only is accessed by website owner.

This website was created for Portfolio Project #5 - Diploma in Full Stack Software Development Diploma at the [Code Institute](https://www.codeinstitute.net).

[View live website here](https://atticstore-95ba3f90b672.herokuapp.com/)

![United responsive design](readme/images/responsive.png)

# Contents

* [**Strategy**](<#strategy>)

    * [Site User Goals](<#site-user-goals>)
    
    * [Site Owner Goals](<#site-owner-goals>)
    
    * [Target Audience](#target-audience)
    
    * [Business Model](#business-model)
    
    * [SEO](#seo)
    
    * [Marketing](#marketing)
    
    * [Project Management](<#project-management>)

# Strategy

## Site User Goals

- Selecting products
- Searching for products
- Buying products
- Register or Login
- Review product
- Add product to the wishlist

## Site Owner Goals

- Sell products
- Get people to subscribe
- Promote own business
- Add products
- Edit products
- Delete products

## Target Audience

- Professional photographers
- Amateur photographers
- Experimental photographers
- Fans of rare film cameras

## Business Model

*Attic* is designed as a minimalistic shop for cameras directly selling to the consumer (B2C). The user can order their products online and then the products will be shipped to them.

There is the subscribtion for the future for discounts and the newsletter with information about new cameras, lenses and accessories.

The most popular social platforms Facebook and Instagram are used to communicate with potential buyers.

## SEO

Keywords, title and description meta tags have been added for SEO.

Descriptive urls have been used for the main site navigation to be more SEO friendly.

File `robots.txt` created to improve SEO.

File `sitemap.xml` created with [Free Online Sitemap Generator](https://www.xml-sitemaps.com/).

## Marketing

### Facebook

There is a Facebook page for *Attic*. The shop can post new products and advertise discounts with the Facebook instruments.

[View live Attic Facebook page here](https://www.facebook.com/atticcamerashop/)

<details><summary><b>Facebook Page</b></summary>

![Facebook Page](readme/images/facebook.png)
</details><br/>

### Instagram

There is an Instagram page for *Attic*. The shop can post new products and advertise discounts with the Instagram instruments.

[View live Attic Instagram page here](https://www.instagram.com/cherdackshopblog/)

<details><summary><b>Instagram Page</b></summary>

![Instagram Page](readme/images/instagram.png)
</details><br/>

### Newsletter

Users can subscribe to a newsletter to stay up to date with what is happening and get dicounts. Service provided by [Mailchimp](https://mailchimp.com/).

<details><summary><b>Newsletter</b></summary>

![Newsletter](readme/images/newsletter.png)
</details><br/>

### Additional

There is the possibilities for more social media pages and running google ads to increase visibility.
Contests could be hosted to win prices and bring more people to join the newsletter.

## Project Management

### Github Board
I've been using the project board in GitHub to keep my project together. It helped me structure up my work. GitHub was used to plan and organize my user stories.

<details><summary><b>User Stories</b></summary>

![User Stories](readme/images/user_stories.png)
</details><br/>

[Back to top](<#contents>)

### Database Schema
I've used a modelling tool called [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) to create the database schema. It shows the relationships between the different models in the database connected to the application. Graph Models exports a *.png file which visualize models.

Models used (besides standard user model) in this project are:

* **Category** - Handles all the categories in the products application.
* **Product** - Handles all the products for categories in the products application.
* **Review** - Handles all the reviews for products in the products application.
* **SizeCategory** - Handles type of size for their categiry in the products application.
* **ProductSize** - Handles all the product sizes for their size category in the products application.
* **Wishlist** - Handles all the products in the wishlist of user in the wishlist application.
* **UserProfile** - Handles all the profiles for users in the profiles application.
* **Order** - Handles all the orders for user profile in the checkout application.
* **OrderLineItem** - Handles all the items for the order in the checkout application.

<details><summary><b>Database Schema Small</b></summary>

![Database Schema Small](readme/images/database_schema_small.png)
</details><br/>

<details><summary><b>Database Schema Full</b></summary>

![Database Schema Full](readme/images/database_schema_full.png)
</details><br/>


