# Just starting! Still WIP (Work in progress)

## Flask_SQList
Very specific &amp; hand tailored Flask web app for custom needs such as viewing/editing records in a database before
executing a chain of other events that are based on values from the db.

![SQList](http://i.imgur.com/45Y7ReP.png)

## Prerequisites:
Currently known (In addition to all of the imported libraries of course):


- for the MS SQL Server (Only!):

  - On Ubuntu x64, had to install FreeTDS:
    * sudo apt-get install freetds-dev freetds-bin unixodbc-dev tdsodbc

  - On Ubuntu x64 '/etc/odbcinst.ini' file look like this:
      ```
      [FreeTDS]
      Description=FreeTDS Driver
      Driver=/usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
      Setup=/usr/lib/x86_64-linux-gnu/odbc/libtdsS.so
      ```
  Depending on the driver and RDBMS you choose, you may need to install other/additional components.

## Todo
- Deploy behind uWSGI + nginx (+Extra Auth Layer) (Currently single threaded, Flask's default)
- Add specific DB models (and the corresponding views/templates)
       - Each DB has 2 relevant "hard coded" tables that the user needs to be able to:
         * View
         * Edit (Insert, Delete, Update) rows as needed
- Integrate a __call__ method to the relevant python file after the modifications above were completed (DB changes)
- CSS/HTML changes
- Update this list more often.

## Notes
