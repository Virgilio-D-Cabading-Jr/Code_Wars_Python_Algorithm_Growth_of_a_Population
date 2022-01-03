# Growth of a Population Read Me

This is a program for Code Wars

Language: Python

Platform: Visual Studio Code
------------------

# Instructions:

1. In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

More generally given parameters:

1. p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)

2. the function nb_year should return n number of entire years needed to get a population greater or equal to p.

3. aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

Note:

1. Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.

--------------------

## Sample output

1. nb_year(1500, 5, 100, 5000) -> 15
2. nb_year(1500000, 2.5, 10000, 2000000) -> 10