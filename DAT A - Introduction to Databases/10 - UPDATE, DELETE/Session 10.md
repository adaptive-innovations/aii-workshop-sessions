# DAT A - Introduction to Databases
## Session 09


|Session Time|Facilitator|Starting URL              |
|------------|-----------|-------------------------------------------------------|
|1 Hour      |GR         |[Data Types](https://www.w3schools.com/sql/sql_datatypes.asp#midcontentadcontainer)     |



## Code Highlights
SELECT Current State of the insertTest Table
```sql
USE labs;
SELECT * FROM insertTest;
```
<br>

Update a record 

_(It is wise to test affected rows by crafting the SELECT statement first)_
```sql
UPDATE insertTest
SET stringColumn = 'Hey, this is new!'
WHERE entryID = 1;

SELECT * FROM insertTest WHERE entryID = 1;
```
<br>

Update using an operator
```sql
UPDATE insertTest
SET intColumn = intColumn + 2
WHERE entryID = 1;

SELECT * FROM insertTest WHERE entryID = 1;
```
<br>

Update multiple columns of a record
```sql
UPDATE insertTest
SET stringColumn = 'Hey, this is new!'
    ,intColumn = intColumn + 2
WHERE entryID = 1;

SELECT * FROM insertTest WHERE entryID = 1;
```
<br>

Update multiple columns of multiple records
```sql
UPDATE insertTest
SET stringColumn = 'Hey, these are new!'
    ,intColumn = intColumn + 2
WHERE entryID < 10;

SELECT * FROM insertTest WHERE entryID < 10;
```
<br>

## Notes




## Challenge