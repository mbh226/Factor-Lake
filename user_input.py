import factor_function

def get_factors(available_factors):
    # Display the lists of available factors with index
    print("\nAvailable factors: ")
    for i in range(len(available_factors)):
        print(f"{i + 1}. {available_factors[i]}")
    
    # Get the number of factors user wants to use
    while(True):
        try:
            num = int(input("How many factors do you want to use?\n"))
            if num > len(available_factors):
                raise Exception
        except ValueError:
            print("Please input an integer.")
            continue
        except Exception:
            print("Number is out of range.")
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
                print("Please input an integer.")
                continue
            except Exception:
                print("Index is out of range.")
                continue
            else:
                break
        
        match available_factors[selected_factor - 1]:
            case "ROE using 9/30 Data":
                factors.append(factor_function.ROE())
            case "ROA using 9/30 Data":
                factors.append(factor_function.ROA())
            case "6-Mo Momentum %":
                factors.append(factor_function.Momentum6m())
            case "12-Mo Momentum %":
                factors.append(factor_function.Momentum12m())
            case "1-Mo Momentum %":
                factors.append(factor_function.Momentum1m())
            case "Price to Book Using 9/30 Data":
                factors.append(factor_function.P2B())
            case "Next FY Earns/P":
                factors.append(factor_function.NextFYrEarns())
            case "1-Yr Price Vol %":
                factors.append(factor_function.OneYrPriceVol())
            case "Accruals/Assets":
                factors.append(factor_function.AccrualsAssets())
            case "ROA %":
                factors.append(factor_function.ROAPercentage())
            case "1-Yr Asset Growth %":
                factors.append(factor_function.OneYrAssetGrowth())
            case "1-Yr CapEX Growth %":
                factors.append(factor_function.OneYrCapEXGrowth())
            case "Book/Price":
                factors.append(factor_function.BookPrice())
            case "Next-Year\'s Return %":
                factors.append(factor_function.NextYrReturn())
            case "Next-Year\'s Active Return %":
                factors.append(factor_function.NextYrActiveReturn())    
            case _:
                print(f"factor {available_factors[selected_factor - 1]} is not available.")
    
    return factors
