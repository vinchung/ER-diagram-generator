## ER-diagram-generator
Developed a script that takes in a SQL schema and outputs a DOT file that is used to render an ER diagram.  
Motivation came from having to hand-draw ER diagrams for a college class - it would be easier to automate this.  
Used schema for Mondial database as an example:  
[http://www.dbis.informatik.uni-goettingen.de/Mondial/](http://www.dbis.informatik.uni-goettingen.de/Mondial/)

### Tools
Python for parsing schema.  
Graphviz for rendering output DOT file.

### Files
sql2dot.py:  Parse SQL schema file to create a DOT file.  
mondial.sql: Sample input with the appropriate format (PostgreSQL) that works with sql2dot.py

### How to Run
	python sql2dot.py mondial.sql  
Output: result.dot  
Open result.dot in Graphviz.