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
* Creating and editing of Products
* Creation of product categories
* Display of products within categories and product details
* Shopping cart implementation to add, remove and display products

### Outstanding
* Implementation of vouchers
* Unit tests

## Copyright
This codebase, unless otherwise stated, is (c) 2015 by Sascha Peter <sascha.o.peter@gmail.com>.

This project incorporates 3rd party libraries such as Django-Cart - https://github.com/bmentges/django-cart - licensed under GPLv3.
The source of the library as found in this project has been modified to work with python 3.3 / django 1.8 and may contains further modifications to make it work for specific use-cases I intend it to work for.
Author and license files, amongst the source code can be found in the djangocart folder - the original project can be found at https://github.com/bmentges/django-cart
