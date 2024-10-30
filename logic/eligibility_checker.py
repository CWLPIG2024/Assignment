def check_eligibility(age, citizenship, marital_status, has_nucleus, has_non_citizen_spouse, owns_property, years_as_pr=None):
    # Check Citizenship Eligibility
    if citizenship == "Foreigner":
        return "At least one buyer must be a Singapore Citizen (SC) or Singapore Permanent Resident (SPR) to buy a resale HDB flat."
    
    if citizenship == "Singapore Permanent Resident (SPR)" and (years_as_pr is None or years_as_pr < 3):
        return "If there are no Singapore Citizens in the household, all SPR owners must have permanent residency status for at least three years."

    # Check Age Eligibility
    if age < 21:
        return "All buyers must be at least 21 years old to purchase a resale HDB flat."
    
    if marital_status == "Single" and age < 35:
        return "Single buyers below the age of 35 are not eligible to purchase a resale HDB flat without a family nucleus."
        
    # Check Family Nucleus Condition
    if marital_status in ["Married", "Widowed", "Divorced"] and has_nucleus == "Single":
        return "Married, widowed, or divorced individuals must have a family nucleus to buy a resale HDB flat."

    if has_nucleus == "Couples and Families" and marital_status == "Single":
        return "Singles cannot apply under the Couples and Families scheme."

    # Check Property Ownership Condition
    if owns_property == "Yes":
        return "All currently owned private or HDB properties must be disposed of within six months of purchasing the resale HDB flat."

    # Additional Checks
    if has_non_citizen_spouse == "Yes" and citizenship != "Singapore Citizen":
        return "If you have a non-citizen spouse, at least one buyer must be a Singapore Citizen."

    return "You are seem to be eligible to purchase a resale HDB flat!"