Instructions 

Python2.7 is needed to run this project

1. Execute genTrainingPosData.py

For UFDD DataSet: It selects a random file from DataSet->training->ufdd->classe21 
and moves it the file to DataSet->training->Query Image
Then it creates the postiveTrainSet folder. This folder the single positive query Image
it'stransformations(scale+crop,aspectRatio,translations)

Re-execution of the same file moves back the file from  DataSet->training->Query Image
 to DataSet->training->ufdd->classe21 and then create new postiveTrainSet folder
on disk, deleting existing one. It works similarly for Sketchy Database.

To change the Class i.e sourceDir change the following variable in the file:
sourceDir = "DataSet/training/classe21/"

2. Run trainClassifier.py

a)Extracts features(hog vector) of all the files inside postiveTrainSet, saves them 
inside DataSet->training/postiveFeatures/ and generate training data and their 
corresponding labels
b)Creates DataSet->training->negativeTrainSet and copies random 100 images from 
	DataSet->training->negativeImages
c)Extract features(hog vector) for DataSet->training->negativeTrainSet and 
generate training  data and label
d) Train the classifier and save the classifier in DataSet->training->Model


3. Run testClassifier.py

a)Generates labels for testing data based on dataSet and saves the file at 
   "DataSet/test/testLabels/genLabel.txt"
b)Saves predicted images along with their true labels in 
"DataSet/test/predictedFiles/predictedLabels.txt" and predicted images 
in "DataSet/test/predictedFiles/"
c)Prints accuracy_score as Reported scores

4.Run hardnegative.py
a)It removes some random amount of files from DataSet->training->negativeTrainSet.
b)Removes easy examples from DataSet->training->negativeTrainSet
c)Moves falsePositives from "DataSet/test/predictedFiles/" to 
"DataSet->training->negativeTrainSet"
d)Loads the classfier from "DataSet/training/Model"
c)Retrains the model using DataSet->training->negativeTrainSet and 
DataSet->training->postiveFeatures
d)Saves the classifier back to "DataSet/training/Model"

5.Do few iterations (max=10) depending upon when classifier does not return many 
false positive by  alerting the execution of testClassifier.py and
 hardnegative.py

6. Run genTestData.py (Execute this file for ufdd and sketchy)

a)For UFDD dataSet: For Given ClassName,it copies all postive instances of query Image 
from DataSet->training->ufdd->classe21.
It copies all negative instances from "DataSet/test/UFDD/painting",
"DataSet/test/UFDD/photo","DataSet/test/UFDD/sketch"

To add distractors to the testing set: set addRandomNegatives flag to true 
Then it copies some random negative images from Pascal VOC,INRIAHolidays,and random 
Flickr image. To add the how many random images need to be extracted modify
extractImage.py for method == "random": change randomFilesNum.

7)Run compareImage.py
a)Compares the Query Image with the images reported as positive instances in
"DataSet/test/predictedFiles/" and gives similarity score using 
Structural Similarity Measure
b)Generates "DataSet/test/predictedFiles/genScores.txt" which contains the image and their
similarity score with Query Image
Following variable contains the 
queryImage =  "DataSet/training/classe22/movedFiles/I_C021_00014.jpg"


8) Run displayTopResults.py
a)Sorts the "DataSet/test/predictedFiles/genScores.txt" based on score in descending order
and generates a file "DataSet/test/predictedFiles/genScoreSorted.txt"

Using "DataSet/test/predictedFiles/genScoreSorted.txt" Top matches can be seen in 
"DataSet/test/predictedFiles/

Note:
We can also filter the true positive Images by executing filterPostivePred.py
it moves all the files whose true and predicted label was positive to the folder:
DataSet->training->postivePredictions.
or based on score and filter top 10 images and move to 
DataSet->training->postivePredictions.

##########################################

For testing and negative dataset
Download PASCAL VOC, INRIA Holiday, random flickr images.

Copy Random flick images to both test and training by dividing them into half inside
DataSet/training,DataSet/test

From downloaded 2007 PASCAL VOC create a folder VOCdevkitTest and copy folders ImageSets
and JPEGImages.

Copy VOCdevkitTest, INRIA Holiday inside DataSet/test