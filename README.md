alengen
=======

Generate models from db tables for SQLAlchemy. Ported to Python 3.

Installation:
------------
    pip install alengen

Usage:
-----
    alengen url [options]

Examples:
--------
    # Write generated code to file
    alengen mysql+pymysql://user:password@localhost:3306/db_name?charset=utf8 --outfile entities.py
    # Print generated code
    alengen mysql+oursql://user:password@localhost/db_name
    alengen postgresql:///local_db
    alengen sqlite:///database.db
