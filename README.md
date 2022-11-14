<a name="readme-top"></a>

## Test-it backend

A backend for test-it web application

## Requirements

1. [python 3](https://www.python.org/downloads/) installed

After installing python make sure to add python to your PATH variable.
- on [windows](https://datatofish.com/add-python-to-windows-path/)
- on [mac](https://opensource.com/article/19/5/python-3-default-mac)

<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Getting started

### Installation

To install the python packages needed, navigate to the project root folder and use the following command:
```
pip install -r requirements.txt
```

<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Usage

To start the backend server use the following command:
```
python main.py
```

<p align="right">[<a href="#readme-top">back to top</a>]</p>

## API

### Hero

To get the hero data, create following API request
```
GET /hero
```

To edit the hero data, create following API request
```
PUT /hero
```

### About us

To get the about us data, create following API request
```
GET /about-us
```

To edit the about us data, create following API request
```
PUT /about-us
```

### Services

To get the services data, create following API request
```
GET /services
```

To edit the services data, create following API request
```
PUT /services
```

### Contact

To get the contact data, create following API request
```
GET /contact
```

To edit the contact data, create following API request
```
PUT /contact
```

### Likes

To get the likes data, create following API request
```
GET /likes
```

To edit the likes data, create following API request
```
PUT /likes
```

<p align="right">[<a href="#readme-top">back to top</a>]</p>

## Roadmap
- [x] Add installation file
- [x] Add hero service
  - [x] Add Get route
  - [x] Add Put route
  - [x] Add data to return
- [x] Add about us service
  - [x] Add Get route
  - [x] Add Put route
  - [x] Add data to return
- [x] Add services service
  - [x] Add Get route
  - [x] Add Put route
  - [x] Add data to return
- [x] Add contact service
  - [x] Add Get route
  - [x] Add Put route
  - [x] Add data to return
  - [ ] Refector data to return
- [x] Add likes service
  - [x] Add Get route
  - [x] Add Put route
  - [x] Add data to return
  - [ ] Refector data to return

<p align="right">[<a href="#readme-top">back to top</a>]</p>
