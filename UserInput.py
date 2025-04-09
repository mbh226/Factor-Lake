from FactorFunction import Momentum6m, ROE, ROA

def get_factors(available_factors):
    # Display the lists of available factors with index
    print(f"Available factors: ")
    for i in range(len(available_factors)):
        print(f"{i + 1}. {available_factors[i]}")
    
    # Get the number of factors user wants to use
    while(True):
        try:
            num = int(input(f"How many factors do you want to use?\n"))
            if num > len(available_factors):
                raise Exception
        except ValueError:
            print(f"Please input an integer.")
            continue
        except Exception:
            print(f"Number is out of range.")
            continue
        else:
            break
    
    # Get the selected factors
    factors = []
    for i in range(num):
        while(True):
            try:
                selected_factor = int(input(f"Please input the index of factor {i + 1}: \n"))
                if selected_factor > len(available_factors):
                    raise Exception
            except ValueError:
                print(f"Please input an integer.")
                continue
            except Exception:
                print(f"Index is out of range.")
                continue
            else:
                break
        
        match available_factors[selected_factor - 1]:
            case "ROE using 9/30 Data":
                factors.append(ROE())
            case "ROA using 9/30 Data":
                factors.append(ROA())
            case "6-Mo Momentum %":
                factors.append(Momentum6m())
            case _:
                print(f"factor {available_factors[selected_factor - 1]} is not available.")
    
    return factors