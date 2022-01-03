###################################################
#   Code Wars: Growth of a Population
###################################################

def nb_year(p0, percent, aug, p):
    yearCount = 0;
    pop = p0;
    while (pop < p) :
        pop += int(pop * (percent / 100)) + aug;
        yearCount += 1;
    return yearCount;

print ("nb_year(1000, 2, 50, 1200)", nb_year(1000, 2, 50, 1200));
print ("nb_year(1500, 5, 100, 5000)", nb_year(1500, 5, 100, 5000));
print ("nb_year(1500000, 2.5, 10000, 2000000)", nb_year(1500000, 2.5, 10000, 2000000));
print ("nb_year(1500000, 0.25, 1000, 2000000)", nb_year(1500000, 0.25, 1000, 2000000));