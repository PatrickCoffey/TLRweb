# TLRweb

## Background
This is a basic dashboard written in Python Django. It must have atleast the 
same functionality as the current traffic light reports with no increase in 
difficulty to use.

The coice of using a Django app is very easy as python is a very simple language
and there is a huge amount of information on the internet regarding how to use.

The best thing about having this written in python is that as a language python
strives to be easy to understand, well documented, mostly backwards compatible;
while the community encourage things to be written modularly and the easiest way
to understand. Its not like `C` in the sense that performance only takes precedence
if the resulting code will still be easily maintainable and understood.

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
Currently development is done using a small Database program called SQLite3, it
works quite well for low volume and provides a very small footprint. The back 
end database is intended to be upgraded to something along the lines of MySQL 
or another DBMS of similar qualities.

The intended web server is apache due to the fact that it is a very common web
server, this should make it a sustainable choice!