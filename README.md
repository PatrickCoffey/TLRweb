# TLRweb

## Background
This is a basic dashboard written in Python Django. It must have atleast the same functionality as the current Traffic Light Reports with no increase in difficulty to use. Traffic Light Reports are a specific type of Chonic Disease dashboard, they were designed by Dr. Gary Sinclair for the NT DOH.

The choice of using a Django app is very easy as python is a very simple language and there is a huge amount of information on the internet regarding how to use.

The best thing about having this written in python is that as a language python strives to be easy to understand, well documented, mostly backwards compatible; while the community encourage things to be written modularly and the easiest way to understand. Its not like `C` in the sense that performance only takes precedence if the resulting code will still be easily maintainable and understood.

Taken from `the ZEN of Python`, by Tim Peters:

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
    
## Technical details
Currently development is done using a small Database program called SQLite3, it works quite well for low volume and provides a very small footprint. The back end database is intended to be upgraded to something along the lines of MySQL or another DBMS of similar qualities.

The intended web server is apache due to the fact that it is a very common web server, this should allow almost anyone to step in and take over administration.

Due to security implications we will not be opening the firewall to allow external users to request pages from the webserver. This will be done by limiting the IP range of hosts that are allowed to connect.

A CSV will be produced from the Business Intelligence server which will be read into the Staging Database by the app. Data will be queried and cleaned before being inserted into the Production database for access by users.

Users will access the database via a set of pages configured for certain roles, there will be roles for all levels of access. No one will have Write access to the server, and most users will only have access to their own Community. HSDA groups will be set up in addition, this will be used for Area service managers and CQI's alike. There will also be Territory and Region wide reports for the use of GM's etc.

Excel files will be downloadable from the server, this is to ensure that people will still have a familiar way to filter the spreadsheets!

It is intended that the staging database will be controlled using SQLAlchemy and that it will be very similar to the Django data base which will aid in supporting this application due to the fact Django actually uses SQLAlchemy to liaise with its own database!



## Administration
User access and User roles will be assigned to users only once they have been approved for access to said functions.


## Example

    +------------------------------------------------------------------------------------------+
    | DOH   Traffic Light Report                                               FEEDBACK  HELP  |
    |--------------------+---------------------------------------------------------------------|
    | Username's Reports |  +---------------+                                                  |
    |--------------------+  |DIABETES STATUS|                                                  |
    |                    |  +---------------+                                                  |
    |   HSDAname Report  |                                                                     |
    | * Community1       |  +                                   +                              |
    |   Community2       |  |                                   |  XX                          |
    |   etc...           |  |                                   |   XX                         |
    |--------------------+  |       XX                          |    XXX                       |
    |--------------------+  |      XXXXX                        |      XXX        XXXX         |
    |                    |  |     XX   XXXXXXX                  |        XX     XXX  XX        |
    | Community1 Report  |  |    XX     XX   XXX                |         XX   XX     XXX      |
    |--------------------+  |   XX             XXXX             |           XXX         XXXX   |
    |                    |  |  XX                 XXXXXX        |                          XX  |
    |   Summary          |  |XXX                       XXX      |                              |
    | * Diabetes Status  |  +------------------------------+    +----------------------------+ |
    |   Renal Status     |  +----------------------+                              +----------+ |
    |   Medications      |  | Diabetes Result Table|                              |  EXPORT  | |
    |                    |  +----------------------+                              +----------+ |
    |                    |  +----------------------------+-------------+--------+              |
    |                    |  | HRN   | DOB       | Gender | Result Date |  HbA1c |              |
    |--------------------+  +---------------------------------------------------+              |
    |                    |  | 12345 | 1/1/2015  | Male   | 1/1/2015    | 7      |              |
    |                    |  | 22345 | 1/1/2015  | Female | 1/1/2015    | 12     |              |
    |                    |  | 32345 | 1/1/2015  | Male   | 1/1/2015    | 14     |              |
    |                    |  | 42345 | 1/1/2015  | Male   | 1/1/2015    | 9      |              |
    |                    |  |       |           |        |             |        |              |
    +------------------------------------------------------------------------------------------+
