[33mcommit 2eb5255aca46037145cf4466da7871c9c72bd27c[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmain[m[33m)[m
Author: lilyyoung02 <101677793+lilyyoung02@users.noreply.github.com>
Date:   Sun Apr 27 23:35:25 2025 +0000

    removed commented out unused variables flagged by ruff.

[1mdiff --git a/CalculateHoldings.py b/CalculateHoldings.py[m
[1mindex 92bfed2..097ace3 100644[m
[1m--- a/CalculateHoldings.py[m
[1m+++ b/CalculateHoldings.py[m
[36m@@ -1,8 +1,5 @@[m
[31m-import matplotlib.pyplot as plt[m
 from MarketObject import MarketObject[m
[31m-from FactorFunction import Factors, Momentum6m, ROE, ROA[m
 from portfolio import Portfolio[m
[31m-import pandas as pd[m
 import numpy as np[m
 def calculate_holdings(factor, aum, market):[m
     # Factor values for all tickers in the market[m
[1mdiff --git a/FactorFunction.py b/FactorFunction.py[m
[1mindex 5cf6403..b5bcc97 100644[m
[1m--- a/FactorFunction.py[m
[1m+++ b/FactorFunction.py[m
[36m@@ -1,8 +1,6 @@[m
[31m-from MarketObject import MarketObject, load_data[m
[31m-import pandas as pd[m
[32m+[m[32mfrom MarketObject import load_data[m
 [m
 load_data[m
[31m-import numpy as np[m
 class Factors:[m
     def get(ticker, market):[m
         return "Factor not specified"[m
[1mdiff --git a/MarketObject.py b/MarketObject.py[m
[1mindex 03406e8..307e810 100644[m
[1m--- a/MarketObject.py[m
[1m+++ b/MarketObject.py[m
[36m@@ -2,7 +2,6 @@[m
 ##from google.colab import drive[m
 ##drive.mount('/content/drive')[m
 import pandas as pd[m
[31m-import numpy as np[m
 ### CREATING FUNCTION TO LOAD DATA ###[m
 def load_data():[m
     file_path = '/content/drive/My Drive/Cayuga Fund Factor Lake/FR2000 Annual Quant Data FOR RETURN SIMULATION.xlsx'[m
[1mdiff --git a/UnitTests/test_known_good.py b/UnitTests/test_known_good.py[m
[1mindex 1651be9..f12fe63 100644[m
[1m--- a/UnitTests/test_known_good.py[m
[1m+++ b/UnitTests/test_known_good.py[m
[36m@@ -1,5 +1,5 @@[m
[31m-from FactorFunction import Factors, Momentum6m[m
[31m-from MarketObject import MarketObject, load_data[m
[32m+[m[32mfrom FactorFunction import Momentum6m[m
[32m+[m[32mfrom MarketObject import load_data[m
 from CalculateHoldings import rebalance_portfolio[m
 import unittest[m
 import pandas as pd[m
[1mdiff --git a/UnitTests/test_multiple_factors.py b/UnitTests/test_multiple_factors.py[m
[1mindex bace029..f52bd00 100644[m
[1m--- a/UnitTests/test_multiple_factors.py[m
[1m+++ b/UnitTests/test_multiple_factors.py[m
[36m@@ -1,5 +1,5 @@[m
[31m-from FactorFunction import Factors, Momentum6m, ROE, ROA[m
[31m-from MarketObject import MarketObject, load_data[m
[32m+[m[32mfrom FactorFunction import Momentum6m, ROE, ROA[m
[32m+[m[32mfrom MarketObject import load_data[m
 from CalculateHoldings import rebalance_portfolio[m
 import unittest[m
 import pandas as pd[m
[1mdiff --git a/UserInput.py b/UserInput.py[m
[1mindex 87f0db9..1d7914e 100644[m
[1m--- a/UserInput.py[m
[1m+++ b/UserInput.py[m
[36m@@ -2,21 +2,21 @@[m [mimport FactorFunction[m
 [m
 def get_factors(available_factors):[m
     # Display the lists of available factors with index[m
[31m-    print(f"\nAvailable factors: ")[m
[32m+[m[32m    print("\nAvailable factors: ")[m
     for i in range(len(available_factors)):[m
         print(f"{i + 1}. {available_factors[i]}")[m
     [m
     # Get the number of factors user wants to use[m
     while(True):[m
         try:[m
[31m-            num = int(input(f"How many factors do you want to use?\n"))[m
[32m+[m[32m            num = int(input("How many factors do you want to use?\n"))[m
             if num > len(available_factors):[m
                 raise Exception[m
         except ValueError:[m
[31m-            print(f"Please input an integer.")[m
[32m+[m[32m            print("Please input an integer.")[m
             continue[m
         except Exception:[m
[31m-            print(f"Number is out of range.")[m
[32m+[m[32m            print("Number is out of range.")[m
             continue[m
         else:[m
             break[m
[36m@@ -30,10 +30,10 @@[m [mdef get_factors(available_factors):[m
                 if selected_factor > len(available_factors):[m
                     raise Exception[m
             except ValueError:[m
[31m-                print(f"Please input an integer.")[m
[32m+[m[32m                print("Please input an integer.")[m
                 continue[m
             except Exception:[m
[31m-                print(f"Index is out of range.")[m
[32m+[m[32m                print("Index is out of range.")[m
                 continue[m
             else:[m
                 break[m
[1mdiff --git a/main.py b/main.py[m
[1mindex b1f8d9c..35b5e27 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -1,10 +1,8 @@[m
[31m-from MarketObject import load_data, MarketObject[m
[31m-from portfolio import Portfolio[m
[32m+[m[32mfrom MarketObject import load_data[m
 from CalculateHoldings import rebalance_portfolio[m
 from UserInput import get_factors[m
 from VerbosityOptions import get_verbosity_level[m
 import pandas as pd[m
[31m-import numpy as np[m
 [m
 def main():[m
     ### Load market data ###[m
[36m@@ -21,6 +19,8 @@[m [mdef main():[m
     verbosity_level = get_verbosity_level() [m
     ### Rebalancing portfolio across years ###[m
     print("\nRebalancing portfolio...")[m
[31m-    final_portfolio = rebalance_portfolio(rdata, factors, start_year=2002, end_year=2023, initial_aum=1,verbosity=verbosity_level)[m
[32m+[m[32m    #final_portfolio = rebalance_portfolio(rdata, factors, start_year=2002, end_year=2023, initial_aum=1,verbosity=verbosity_level)[m
[32m+[m[32m    rebalance_portfolio(rdata, factors, start_year=2002, end_year=2023, initial_aum=1,verbosity=verbosity_level)[m
[32m+[m
 if __name__ == "__main__":[m
     main()[m
[1mdiff --git a/portfolio.py b/portfolio.py[m
[1mindex 10015b7..d675233 100644[m
[1m--- a/portfolio.py[m
[1m+++ b/portfolio.py[m
[36m@@ -1,5 +1,3 @@[m
[31m-from MarketObject import MarketObject[m
[31m-import pandas as pd[m
 [m
 class Portfolio:[m
     ### Initialize portfolio by providing a name and a list of investments ###[m
[1mdiff --git a/scripts/bandit_to_sarif.py b/scripts/bandit_to_sarif.py[m
[1mindex 50f4532..941754d 100644[m
[1m--- a/scripts/bandit_to_sarif.py[m
[1m+++ b/scripts/bandit_to_sarif.py[m
[36m@@ -26,7 +26,7 @@[m [mdef convert_bandit_to_sarif(bandit_json_path, sarif_output_path):[m
     }[m
 [m
     rules_seen = {}[m
[31m-    results = [][m
[32m+[m[32m    #results = [][m
 [m
     for result in bandit_data.get("results", []):[m
         test_id = result.get("test_id", "UNKNOWN")[m
[1mdiff --git a/scripts/convert_safety_to_sarif.py b/scripts/convert_safety_to_sarif.py[m
[1mindex a5ec496..4206a68 100644[m
[1m--- a/scripts/convert_safety_to_sarif.py[m
[1m+++ b/scripts/convert_safety_to_sarif.py[m
[36m@@ -56,7 +56,7 @@[m [mdef convert_safety_to_sarif(safety_json, sarif_file, requirements_file):[m
         sys.exit(1)[m
 [m
     # we're looking at the requirements file[m
[31m-    dependencies = load_requirements(requirements_file)[m
[32m+[m[32m    #dependencies = load_requirements(requirements_file)[m
 [m
     # just want to see the json data[m
     print("Safety JSON structure:", safety_data)[m
