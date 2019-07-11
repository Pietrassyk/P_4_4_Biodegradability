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
Each of these models where trainied on a set of only linear features and a set of linear features and added polynomial features. Ultimately leading to the following performances:
![Model Selection](/Pictures/ModelSelection.png "Model Selection")

## Final Model

## Outlook

## Summary
The Slieshow Version of this Project can be found here:
https://docs.google.com/presentation/d/1vfoftgk9bQPBq6ZBiI38KFoI2lb7zBuYRb1dBCDa0EE/edit?usp=sharing
