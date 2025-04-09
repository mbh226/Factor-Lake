from FactorFunction import Momentum6m, ROE, ROA

def get_factors(available_factors):
    # Display the lists of available factors with index
    print(f"Available factors: ")
    for i in range(len(available_factors)):
        print(f"{i + 1}. {available_factors[i]}")
    
    # Get the number of factors user wants to use
    while(True):
        num = input(f"How many factors do you want to use?")
        if type(num) != int:
            print(f"Please input an integer.")
        else:
            break
    
    # Get the selected factors
    factors = []
    for i in range(num):
        while(True):
            selected_factor = input(f"Please input the index of factor {i + 1}: ")
            if selected_factor != int:
                print(f"Please input an integer.")
            elif selected_factor > len(available_factors):
                print(f"Index is out of range.")
            else:
                break
        match available_factors[selected_factor]:
            case "ROE using 9/30 Data":
                factors.append(ROE())
            case "ROA using 9/30 Data":
                factors.append(ROA())
            case "6-Mo Momentum %":
                factors.append(Momentum6m())
            case _:
                print(f"factor {available_factors[selected_factor]} is not available.")
    
    return factors