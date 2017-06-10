# simple-shop

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ea2408a8483748fa966f4a3913cc13ae)](https://www.codacy.com/app/sascha.o.peter/simple-shop?utm_source=github.com&utm_medium=referral&utm_content=Sascha-Peter/simple-shop&utm_campaign=badger)
[![Circle CI](https://circleci.com/gh/Sascha-Peter/simple-shop.svg?style=svg)](https://circleci.com/gh/Sascha-Peter/simple-shop) [![Updates](https://pyup.io/repos/github/Sascha-Peter/simple-shop/shield.svg)](https://pyup.io/repos/github/Sascha-Peter/simple-shop/) [![Python 3](https://pyup.io/repos/github/Sascha-Peter/simple-shop/python-3-shield.svg)](https://pyup.io/repos/github/Sascha-Peter/simple-shop/)

This project is a sample coding exercise implementing a simple shop front with products,
categories and shopping cart integration.

Finished all-in-one solutions like Django-Oscar or Cartridge for Mezzanine
have been avoided on purpose although they would have covered everything and
beyond.

Author: [Sascha Peter](https://github.com/Sascha-Peter)
Since: 2015-06-13

## Requirements
To run this project, the following requirements need to be met:

* Python 3.3+
* Virtualenv
* PIP (Package Manager for installing additional requirements)

## Additional requirements
All additional packages can be found in `pip-requirements.txt`.

### Installation of additional requirements
All additional packages can simply be installed by running:

```bash
pip install -r pip-requirements.txt
```

## Features

### Done

* Creation and editing of products
* Creation of product categories
* Display of products within categories and product details
* Shopping cart implementation to add, remove and display products
* Implementation of vouchers
* Disallow ordering more items than in stock
* User Documentation for mac users

### Outstanding

* More unit tests

## User Documentation
This project contains a small user documentation how to setup and install this project (currently only covers MAC).
The user documentation can be found under docs/Simple-Shop_Documentation/tmpt/en-GB/ in a variety of formats.

The formats include:

* epub (untested)
* html
* html-desktop
* html-single
* pdf
* txt
* xml

Please note that due to licencing of the documentation, it is not suitable for printing.

## Copyright
This codebase, unless otherwise stated, is Copyright by Sascha Peter &copy; 2015 <sascha.o.peter@gmail.com>.

This project incorporates third party libraries such as [Django-Cart](https://github.com/bmentges/django-cart) - and is licensed under [GPLv3](http://www.gnu.org/licenses/gpl-3.0.en.html). The source code in this project has been modified to work with Python 3.3 / Django 1.8 and to support the features listed above . Author, license and source code files can be found in the djangocart folder - the original project can be found [here](https://github.com/bmentges/django-cart).

The user documentation of this project has been written and generated with [Publican](https://fedorahosted.org/publican/) - and may only be distributed subject to the terms and conditions set forth in the GNU Free Documentation License (GFDL), V1.2 or later (the latest version is presently available [here](http://www.gnu.org/licenses/fdl.txt)).
