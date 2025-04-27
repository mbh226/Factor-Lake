import FactorFunction

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
                factors.append(FactorFunction.ROE())
            case "ROA using 9/30 Data":
                factors.append(FactorFunction.ROA())
            case "6-Mo Momentum %":
                factors.append(FactorFunction.Momentum6m())
            case "12-Mo Momentum %":
                factors.append(FactorFunction.Momentum12m())
            case "1-Mo Momentum %":
                factors.append(FactorFunction.Momentum1m())
            case "Price to Book Using 9/30 Data":
                factors.append(FactorFunction.P2B())
            case "Next FY Earns/P":
                factors.append(FactorFunction.NextFYrEarns())
            case "1-Yr Price Vol %":
                factors.append(FactorFunction.OneYrPriceVol())
            case "Accruals/Assets":
                factors.append(FactorFunction.AccrualsAssets())
            case "ROA %":
                factors.append(FactorFunction.ROAPercentage())
            case "1-Yr Asset Growth %":
                factors.append(FactorFunction.OneYrAssetGrowth())
            case "1-Yr CapEX Growth %":
                factors.append(FactorFunction.OneYrCapEXGrowth())
            case "Book/Price":
                factors.append(FactorFunction.BookPrice())
            case "Next-Year\'s Return %":
                factors.append(FactorFunction.NextYrReturn())
            case "Next-Year\'s Active Return %":
                factors.append(FactorFunction.NextYrActiveReturn())    
            case _:
                print(f"factor {available_factors[selected_factor - 1]} is not available.")
    
    return factors
