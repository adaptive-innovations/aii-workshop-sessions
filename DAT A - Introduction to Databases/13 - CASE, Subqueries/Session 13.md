# DAT A - Introduction to Databases
## Session 13


|Session Time|Facilitator|Starting URL              |
|------------|-----------|-------------------------------------------------------|
|1 Hour      |GR         |[CASE Statement](https://www.w3schools.com/sql/sql_ref_case.asp)  |



## Code Highlights
Check out the ```lumber``` table in the ```workshop``` database:
```sql
USE workshop;
SELECT * FROM lumber;
```

```CASE``` Statement
Basic Syntax: ```CASE WHEN (Condition A) THEN (Output A) WHEN (Condition B) THEN (Output B) END```
```sql
SELECT 
    unit
    ,length
    ,CASE
      WHEN unit = 'ft' THEN length * 12
      WHEN unit = 'yd' THEN length * 12 * 3
      ELSE length
    END AS inches
FROM lumber;
```
- Start with ```CASE```
- Ends with ```END```
- Each ```IF```, ```ELSE IF``` uses command ```WHEN```

Remember that the CASE statement is assessed in order of appearance for each WHEN in the statement.

CASE Examples to ORDER BY
```sql
SELECT 
    unit
    ,length
    ,description
    ,CASE
        WHEN unit = 'ft' THEN length * 12
        WHEN unit = 'yd' THEN length * 12 * 3
        ELSE length
    END AS inches
FROM lumber
ORDER BY CASE
        WHEN unit = 'ft' THEN length * 12
        WHEN unit = 'yd' THEN length * 12 * 3
        ELSE length
    END;
```

```sql
WITH QueryA AS
(
    SELECT 
        unit
        ,length
        ,description
        ,CASE
            WHEN unit = 'ft' THEN length * 12
            WHEN unit = 'yd' THEN length * 12 * 3
            ELSE length
        END AS inches
    FROM lumber
)
SELECT * FROM QueryA ORDER BY inches;
```


SUBQUERIES!
See the Source Tables:
```sql
SELECT * FROM survey_grade;
SELECT * FROM survey_results;
```

Use the subquery
```sql
SELECT user_id
      ,score
	  ,(SELECT TOP(1) description FROM survey_grade WHERE min_score <= score ORDER BY min_score DESC) AS RatingDescription
  FROM survey_results;
```

## Notes
- When using a subquery, ask yourself if you should be using as ```JOIN``` instead. Joins are faster, as a rule, than subqueries.
- When possible, use WITH to store the data as a temporary table in memory to optimize the subquery.



## Challenge