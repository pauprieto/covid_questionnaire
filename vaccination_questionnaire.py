# COVID-19 Vaccine Rollout Checker
# Developed by Paula Prieto (AUG, 2021)

"""The 'COVID-19 Vaccine Rollout Checker' program checks for COVID-19 Vaccination
Rollout eligibility of Phase number"""
print("*****  Welcome to the COVID-19 Vaccine Rollout Checker  *****")
print("** Please answer the following questions to know your rollout Phase **")

def invalid_integer():
    """To validate input as positive number"""
    print()
    print("Oops! that is not a valid number. Try again using a positive number.")
    return age()

def invalid_age():
    """Will validate age input to not be over 150 years old"""
    print()
    print("Oops! that is not a valid age. Try again using a number up to 150.")
    return age()

def phase_1a():
    """Exit program for users eligible for Phase 1a"""
    print()
    print("You are eligible for vaccination in Phase 1a")
    exit("Thank you for using the COVID-19 Vaccine Rollout Checker")

def phase_1b():
    """Exit program for users eligible for Phase 1b"""
    print()
    print("You are eligible for vaccination in Phase 1b")
    exit("Thank you for using the COVID-19 Vaccine Rollout Checker")

def phase_2a():
    """Exit program for users eligible for Phase 2a"""
    print()
    print("You are eligible for vaccination in Phase 2a")
    exit("Thank you for using the COVID-19 Vaccine Rollout Checker")

def phase_2b():
    """Exit program for users eligible for Phase 2b"""
    print()
    print("You are eligible for vaccination in Phase 2b")
    exit("Thank you for using the COVID-19 Vaccine Rollout Checker")

def phase_3():
    """Exit program for users eligible for Phase 3"""
    print()
    print("You are eligible for vaccination in Phase 3 (Pfizer vaccine only)")
    exit("Thank you for using the COVID-19 Vaccine Rollout Checker")

def under_18(high_risk):
    """Exit program for uses under 18, where vaccine is recommended vs not recommended"""
    while True:
        print()
        vaccine_recommendation = input("Has it been recommended you obtain a vaccine? (Y/N): ")
        if high_risk == "Y" and vaccine_recommendation == "Y":  # Other critical/high risk workers UNDER 18 (recommended vaccination)
            phase_2a()
        elif vaccine_recommendation == "Y":  # UNDER 18 recommended vaccination, NOT an other critical/high risk workers
            phase_3()
        elif vaccine_recommendation == "N":  # UNDER 18 NOT recommended vaccination, disregards other critical/high risk workers
            print()
            print("Vaccination is not recommended for you")
            exit("Thank you for using the COVID-19 Vaccine Rollout Checker")
        else:
            print()
            print("Oops, invalid entry. Please try again entering Y or 'Yes' or N for 'No'")  # Validation invalid character input

disability_user = None

def disability(user_age):
    """To identify users with underlying medical conditions or disability"""
    while True:
        print()
        disability_user = input("Do you have an underlying medical condition, "
                                "including those with a disability? (Y/N): ")
        if disability_user == "Y":  # Medical condition/disability category. No need to ask if indigenous, or if other critical or high risk worker.
            phase_1b()
        elif disability_user == "N" and user_age > 54:  # NO medical condition/disability for 55 OR OVER category. Moves to indigenous question.
            indigenous(user_age)
        elif disability_user == "N" and user_age < 55:  # NO medical condition/disability for UNDER 55 category. Moves to other critical/high risk worker question.
            other_critical_worker(user_age)
        else:
            print()
            print("Oops, invalid entry. Please try again entering Y or 'Yes' or N for 'No'")  # Validation invalid character input

indigenous_user = None

def indigenous(user_age):
    """To identify Aboriginal or Torres Strait Islander users"""
    while True:
        print()
        indigenous_user = input("Are you Aboriginal or Torres Strait Islander? (Y/N): ")
        if indigenous_user == "Y" and user_age > 54:  # indigenous category over 55, including other critical and high risk workers
            phase_1b()
        elif indigenous_user == "Y" and user_age < 55:  # OVER 55, no medical condition/disability, not indigenous category
            phase_2a()
        elif indigenous_user == "N" and user_age > 49:  # 50-69, no medical issues/disability, not indigenous category
            phase_2a()
        elif indigenous_user == "N" and user_age < 50:  # Balance of adult population category/catch up unvaccinated under 50 category
            phase_2b()
        else:
            print()
            print("Oops, invalid entry. Please try again entering Y or 'Yes' or N for 'No'")  # Validation invalid character input

# Eligibility for priority workers
def priority():
    """Validation of priority worker category"""
    while True:
        print()
        priority_worker = input("Are you a quarantine and border worker, prioritised frontline healthcare worker, "
                                "or an aged care/disability care staff member or resident? (Y/N): ")
        if priority_worker == "Y":
            phase_1a()
        elif priority_worker == "N":
            break
        else:
            print()
            print("Oops, invalid entry. Please try again entering Y or 'Yes' or N for 'No'")  # Validation invalid character input

priority()

# Eligibility for other health care workers
def other_health_worker():
    """Validation of other health worker category"""
    while True:
        print()
        other_hc = input("Are you a health care worker, or a critical or high risk worker "
                         "(including defence force, police, fire, emergency services and meat processing? (Y/N): ")
        if other_hc == "Y":
            phase_1b()
        elif other_hc == "N":
            break
        else:
            print()
            print("Oops, invalid entry. Please try again entering Y or 'Yes' or N for 'No'")  # Validation invalid character input

other_health_worker()

# Eligibility for other critical or high risk worker
def other_critical_worker(user_age):
    """Validation of other critical and high risk worker category"""
    while True:
        print()
        high_risk = input("Are you an other critical and high risk worker? (Y/N): ")
        if user_age < 18 and high_risk == "Y":  # UNDER 18 move to ask if vaccine has been recommended
            under_18(high_risk)
        elif user_age < 18 and high_risk == "N":
            under_18(high_risk)
        elif user_age > 17 and high_risk == "Y":  # Other critical/high risk workers, includes adults 18 and OVER to UNDER 70 with no medical conditions/disability.
            phase_2a()
        elif user_age > 17 and high_risk == "N":
            indigenous(user_age)  # Adults UNDER 55 with no medical conditions/disability, and NOT other critical/high risk worker. Move to indigenous question.
        else:
            print()
            print("Oops, invalid entry. Please try again entering Y or 'Yes' or N for 'No'")  # Validation invalid character input

user_age = 0

def age():
    """Function to identify user age with input validation"""
    while True:
        try:
            print()
            user_age = int(input("What is your age in years?: "))
            if user_age < 0:
                invalid_integer()  # validation negative number input
            elif user_age > 150:
                invalid_age()
            elif user_age >= 70:
                phase_1b()
            elif user_age >= 18:
                disability(user_age)
            elif user_age < 18:
                other_critical_worker(user_age)  # For employed UNDER 18 who may be other critical/high risk workers
        except ValueError:
            print()
            print("Oops! that entry is not valid. Try again using a positive number.")  # Validation invalid character input

age()
