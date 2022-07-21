# DAT A - Introduction to Databases
## Session 09


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Data Types](https://www.w3schools.com/sql/sql_datatypes.asp#midcontentadcontainer)     |


## SQL Server Data Types
### Recommended for most use cases
#### Strings
- nvarchar()
- varbinary
- image
#### Numeric
- bit
- int
- bigint
- decimal()
- money
#### Date and Time
- datetime
- date
- timestamp



## Code Highlights
Inserting Records into a Table
```sql
INSERT INTO insertTest
(
    stringColumn
    ,bitColumn
    ,intColumn
    ,decimalColumn
    ,datetimeColumn
    ,dateColumn
)
VALUES (
    'What!'
    ,1.000
    ,1776/15
    ,123.455
    ,'05/15/2022 12:30:15'
    ,DATEFROMPARTS(2000, 01, 01)
);
```

If you're inserting into every single column, and in the order the columns are defined in the database, you can omit the insert column list.
```sql
INSERT INTO insertTest
VALUES (
    'What!'
    ,1.000
    ,1776/15
    ,123.455
    ,'05/15/2022 12:30:15'
    ,DATEFROMPARTS(2000, 01, 01)
);
```





## Notes

- [varchar vs nvarchar](https://www.sqlshack.com/sql-varchar-data-type-deep-dive/#:~:text=The%20key%20difference%20between%20varchar,the%20space%20as%20SQL%20varchar)


<a href="https://raw.githubusercontent.com/adaptive-innovations/aii-workshop-sessions/main/DAT%20A%20-%20Introduction%20to%20Databases/09%20-%20CAST%2C%20CONVERT/UTF-8_takes_over.png?raw=true">
  <img src="https://raw.githubusercontent.com/adaptive-innovations/aii-workshop-sessions/main/DAT%20A%20-%20Introduction%20to%20Databases/09%20-%20CAST%2C%20CONVERT/UTF-8_takes_over.png?raw=true" alt="UTF-8 Takes Over" width=25%/>
</a>



## Challenge