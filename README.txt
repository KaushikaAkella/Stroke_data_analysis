ASSOCIATION RULE BASED HYPERGRAPH FOR STROKE DATA ANALYSIS USING MINIMAL DOMINATING SET

1. Open the "Step 1 - Data Preprocessing" folder and run the "preprocess.py" file. 
   The original file with all the posts is in the "strokedata - orig.xlsx" file
   The pre-processed data is stored in "data - preprocessed.csv"
2. Open the "Step 2 - Association Rule" folder and run the "apriori.py" file.
   Using the "data - preprocessed.csv" file, the association rules are saved as a json file in "apriori-rules.txt"
3. Open the "Step 3 - Hypergraph - Linegraph" folder and run the "hypergraph.py" file. 
   The association rule file "apriori-rules.txt" is used for the plot of the hypergraph which will be displayed.
4. Open the "Step 4 - Minimal Dominating Set" folder and run the "mindom.py" file. 
   Using the hypergraph constructed, the minimal dominating set is displayed in the python command prompt. 
