###################################################
#   Code Wars: Growth of a Population
###################################################

def nb_year(p0, percent, aug, p):
    yearCount = 0;
    pop = p0;
    while (pop < p) :
        pop += int(pop * (percent / 100)) + aug;
        yearCount += 1;
        print ("Year:", yearCount, " | Population:", pop);
    return pop;
    
print ("", nb_year(1000, 2, 50, 1200));