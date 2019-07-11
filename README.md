# P_4_4_Biodegradability
Classifying biodegradability of compounds using QSAR Data

## Motivation
The Goal of this project is to use QSAR-Data (Quantitative Structure Ability Relationship) from cemical Compounds and classify biodegradable and non biodegradable substances. Since compounds can last hundreds of years before being decomposed, degradability experiments will take time accordingly. This is where the approach of QSAR begins to shine. Just by looking at relatively quick to obtain molecular properties, the molecules behaviour (in this case biodegradability) can be estimated. Thus helping to ensure correct disposal of chemicals and saving the environment, while also reducing expensive longterm experiments.

## Dataset
The dataset was provided by UCI. And can be found here:
https://archive.ics.uci.edu/ml/datasets/QSAR+biodegradation

## Explopratory Data Analysis (EDA)
For EDA the data was split into the two target classes "degradable" and non "degradable" in order to find features with significant differences between the two groups:

|Features provinding good seperation |
:---:
|Normalized spectral positive sum from Burden
![Burden](/Pictures/distritbution_plot_SpPosA_B(p).png "SpPosA_B(p)")|
|Percentage of C-Atoms
![C-Atoms](/Pictures/distribution_plot_C.png "Percentage of C-Atoms")|

## Feature Engineering
The findings from the EDA where then combined with my chemical backround knowledge to create new features that help dividing the target classes.
One of the features being the molecules functionality based on the number of heavy metal atoms (nHM).
It is most likely that in degradable organic compounds there is only one heavy metal atom present (nHM =1) as a single central atom in a chemical complex bound. These complexes are found in every species. A good example of this beeing the dye hemoglobine found in our blood as shown in the figure below (in the middle part).
If nHM exeeds one a compound will be either anorganic or of high toxicity and therefore lead to low biodegradability. (nHM >1)
![Molecule Functionality](/Pictures/Feature-Functionality.png "Molecule Functionality")|

## Model Selection
Starting with a logistic regression model as a baseline the following models where trained and testes after a train_test_split:
1. Logistic regression without penalty terms (base model)
2. Logistic regression with lasso penalty
3. KNN
4. Random forrest
5. Ensemble (cointaining models 2-5)
<<<<<<< HEAD
<br>Each of these models where trainied on a set of only linear features and a set of linear features and polynomial features. Ultimately leading to the following metrics:
![Model Selection](/Pictures/ModelSelection.png "Model Selection")

## Final Model
From the overview above the logistic regression model is chosen, since it provides the overall best performance. After Hyperparameter tuning and crossvalidation the following results are achieved on the test set:

![Final Scores](https://github.com/Pietrassyk/P_4_4_Biodegradability/blob/master/Pictures/Confucionmatrix_final%20Model.png "Final Scores")

The overall model performance provides a good classification of the target `degradability`. The most import metric being the precision score. The obtained precision score states that using this model 85% of all compounds to be classified as `degradable` are truly degradable.

Furthermore Sensitivity (81%) and Specificity are (92%) are higher than in the original model provided in the data source (both values being at around 80%).

The nature of the logistic regression model lets us further investigate the relationship between the used features and the classification:

![Feature Importance](https://github.com/Pietrassyk/P_4_4_Biodegradability/blob/master/Pictures/Feature_Importance.png "Feature Importance")

## Application
The OECD provides sufficient Data on Chemical Compounds, ready to be scraped for future Analysis. So this can be done to further improve model performance.

On an Industry Scale this model could be used to:
→ Create new biodegradable compounds based on the above Feature importance
→ Run Lab tests on waste to determine whether it is compostable or not
→ certify biodegradable products based on compound data
=======
Each of these models where trainied on a set of only linear features and a set of linear features and added polynomial features. Ultimately leading to the following performances:
![Model Selection](/Pictures/ModelSelection.png "Model Selection")

## Final Model
>>>>>>> f5e2aa7c3e5f1c5b55034ce179b9d454e1348adb


## Summary

+ Biodegradability of compounds can be classified  with a Logistic Regression Model at a precision of 86 % given basic QSAR-Data
+ Model performs better than the datasets author’s model.
+ Using this model multiple profitable and sustainable applications are possible.

The Slieshow Version of this Project can be found here:
https://docs.google.com/presentation/d/1vfoftgk9bQPBq6ZBiI38KFoI2lb7zBuYRb1dBCDa0EE/edit?usp=sharing
