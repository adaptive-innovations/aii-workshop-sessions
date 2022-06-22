# DAT A - Introduction to Databases
## Session 05


|Session Time|Facilitator|Starting URL                                                          |
|------------|-----------|----------------------------------------------------------------------|
|1 Hour      |GR         |[Joins](https://www.w3schools.com/sql/sql_join.asp)     |

Using (INNER) JOIN, LEFT (OUTER) JOIN, RIGHT (OUTER) JOIN, and FULL (OUTER) JOIN
> Syntax in (parentheses) optional.

## Code Highlights

- LEFT JOIN
- OUTER JOIN
- RIGHT JOIN

> Mastery and understanding of ```JOIN``` and ```LEFT JOIN``` should mean you're ready for real world scenarios.

Here's our reference drawing we made in class to demonstrate JOIN results:
<a href="https://github.com/adaptive-innovations/aii-workshop-sessions/blob/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN,%20Aliases/JoinDemonstration.PNG?raw=true">
  <img src="https://github.com/adaptive-innovations/aii-workshop-sessions/blob/main/DAT%20A%20-%20Introduction%20to%20Databases/04%20-%20JOIN,%20Aliases/JoinDemonstration.PNG?raw=true" alt="JOIN Illustratione" width=100%/>
</a>

## Challenge
- INNER JOIN ```Orders``` with ```Order Details```.
- INNER JOIN ```Orders``` with ```Customers```.
- INNER JOIN ```Employees``` with ```Employee Territories```.
- INNER JOIN ```Territories``` with ```Region```s.
- INNER JOIN ```Employees``` with ```Employee Territories``` with ```Territories```  with ```Region```s, returning at least 1 column each which isn't the column used in the JOIN.

Without looking at today's notes, do the following:
- USE Workshop;
- INNER JOIN ```Children``` with ```Parents```
- LEFT JOIN ```Children``` with ```Parents```
- RIGHT JOIN ```Children``` with ```Parents```
- FULL OUTER JOIN ```Children``` with ```Parents```