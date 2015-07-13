# simple-shop

This project is aimed to be a small coding excercise implementing
a simple shop front with products, categories 
and a simple cart integration whilst showing the coding ability.

Finished all-in-one solutions like Django-Oscar or Cartridge for Mezzanine
have been avoided on purpose although they would have covered everything and
beyond.

Author: Sascha Peter <sascha.o.peter@gmail.com>
Since: 2015-06-13

## Requirements
To run this project, the following requirements need to be met:
* Python 3.3+
* Virtualenv
* PIP (Package Manager for installing additional requirements)

## Additional requirements
All additional packages can be found in pip-requirements.txt.

### Installation of additional requirements
All additional packages can simply be installed by running:
`pip install -r pip-requirements.txt`

## Features

### Done
* Creation and editing of products
* Creation of product categories
* Display of products within categories and product details
* Shopping cart implementation to add, remove and display products
* Implementation of vouchers

### Outstanding
* Disallow ordering more items than in stock
* Unit tests

## Copyright
This codebase, unless otherwise stated, is Copyright by Sascha Peter (c) 2015 sascha.o.peter@gmail.com.

This project incorporates third party libraries such as Django-Cart - https://github.com/bmentges/django-cart - and is licensed under GPLv3 - http://www.gnu.org/licenses/gpl-3.0.en.html. The source code in this project has been modified to work with Python 3.3 / Django 1.8 and to support the features listed above . Author, license and source code files can be found in the djangocart folder - the original project can be found at https://github.com/bmentges/django-cart
