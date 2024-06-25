#if has high income and good credit . Then eligible for loan

#AND condition
    #both
#OR condition
    #at least one
#NOT

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")




has_high_income = False
has_good_credit = False


#if has high income OR good credit . Then eligible for loan
if has_high_income or has_good_credit:
    print("Eligible for loan with guildline 2")


#if has high income AND doesn't have criminal record . Then eligible for loan.

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan with guildline 3")