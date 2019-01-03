![simplinnovation](https://4.bp.blogspot.com/-f7YxPyqHAzY/WJ6VnkvE0SI/AAAAAAAADTQ/0tDQPTrVrtMAFT-q-1-3ktUQT5Il9FGdQCLcB/s350/simpLINnovation1a.png)

# Basic CRUD: Flask & MySQL

1. Activate __MySQL__ server:
    
    ```bash
    $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
    $ mysql.exe -u <username> -p<password>
    ```
    
    On my case:
    
    ```bash
    $ mysql.exe -u lintang -p12345
    ```

#

2. Create a database & table on MySQL. I'll use a database called __"lin_flask"__ & a table called __"users"__:
    
    ```bash
    mysql>  CREATE DATABASE lin_flask;
    mysql>  USE lin_flask;
    mysql>  CREATE TABLE users (
                id int auto_increment,
                name varchar(100) not null,
                age tinyint,
                primary key (id)
            );
    ``` 

#

3. Clone this repo. Edit __database.yaml__ file according to your database configuration, then install all the packages needed. In this project I'm using __flask__, __flask_cors__ & __flask_mysqldb__:
    ```bash
    $ git clone https://github.com/LintangWisesa/CRUD_Flask_MySQL.git
    $ cd CRUD_Flask_MySQL
    $ pip install flask flask_cors flask_mysqldb
    ```

#

4. Run the server file. Make sure your MySQL server is still running. Your application server will run locally at __*http://localhost:5000/*__ :
    ```bash
    $ python app.py
    ```

#

5. Give a request to the server. You can use __Postman__ app:
    
    __See the opening screen (*home.html*)__
    ```bash
    GET /
    ```

    __Post a data to database:__ 
    ```bash
    POST /data
    body request: {name:"x", age:"y"}
    ```
    __Get all data & specific data by id:__
    ```bash
    GET /data
    GET /data/{:id}
    ```
    __Update a data by id__:
    ```bash
    PUT /data/{:id}
    body request: {name:"x", age:"y"}
    ```
    __Delete a data by id:__
    ```bash
    DELETE /data/{:id}
    ```

#

6. Enjoy your code! 😎👌

#

#### Lintang Wisesa :love_letter: _lintangwisesa@ymail.com_

[Facebook](https://www.facebook.com/lintangbagus) | 
[Twitter](https://twitter.com/Lintang_Wisesa) |
[Google+](https://plus.google.com/u/0/+LintangWisesa1) |
[Youtube](https://www.youtube.com/user/lintangbagus) | 
:octocat: [GitHub](https://github.com/LintangWisesa) |
[Hackster](https://www.hackster.io/lintangwisesa)