# DataSciencePortfolio
Welcome to my data science portfolio the intent is to provide a showcase of the data science and data analysis projects that I've done.
Click on the links below to check out some of the projects that I've done

To find out more about me check out the [pptx](https://github.com/mleiwe/DataSciencePortfolio/blob/Introduction/WhoAmI_PlusOneCaseStudy.pptx) or check out the [google slide deck](https://docs.google.com/presentation/d/1Z9ctxT7zOCgElMMbZL1SyI6LiEEJxAnz_YTPMoUKxII/edit?usp=sharing)

## Selected Projects
### [Sea Turtle Facial Recognition](https://github.com/mleiwe/DataSciencePortfolio/tree/main/SeaTurtles) 
Facial recognition challenge for [FruitPunch AI](www.fruitpunch.ai/): Many sea turtle species are critically endangered and monitoring sea turtle populations is vital. However, tracking a turtle over several captures is a difficult challenge as metal tags can get damaged, and also cause distress to the turtle. By using facial recognition we came up with a solution that is more accurate and faster than manual annotation, and also minimises harm to the turtle. 
![LightGlueDemoSift](https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/39106829-db2d-4239-b685-0f0b9032c0f4)

Images were first passed through a YOLOv8_SAM network to isolate the relevant turtle pixels. Following this a variety of different models were tested to see which was the most effective. The winning solution was SIFT keypoint extraction followed by LightGlue for keypoint matching. However, instead of the basic point matching as demonstrated in the image above I devised a novel metric which compares the distribution of all the keypoints to a null distribution (average distribution of non-matching sea turtles). This difference in distributions was quantified using the Wasserstein distance. This can be seen in the distributions below

<img width="836" alt="Screenshot 2024-02-17 at 9 25 12 PM" src="https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/1e652fc4-3734-4d1c-94d7-025cddaff24b">

### [dCrawler](https://github.com/mleiwe/DataSciencePortfolio/tree/main/dCrawler): 
A new clustering algorithm that utilises a single distance threshold. Ideal for when you don't know how many clusters there should be but all the points should be closely related.

[Video Demonstration](https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/de4ea1c5-5647-4c7a-a54f-5da4afb69c3d)

dCrawler is particularly useful for clustering colors when compared to DBSCAN
![DBSCAN_vs_dCrawler_image](https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/cddbb868-f297-4a94-af2d-465f3af6455d)

### [CancerDetection](https://github.com/mleiwe/DataSciencePortfolio/tree/main/CancerDetection): 
As part of the ML zoomcamp training this was an exercise to get familiar with deploying a solution using docker images. In this example, I used features extracted from histological samples containing malignant or benign tumors. The [original data](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) set is nicely curated but with approximately 30 variables is quite large. By utilizing principal component analysis (PCA) I engineered 10 features that explain 95% of the variance. Many models were assessed using a gridsearch method, with the scoring metric being the F1 score due to a class imbalance in the dataset. I found that the most effective model on the validation set was a logistic regression classifier on the 10 Principal components. This produced an F1 score >0.975 on the validation data (see figure below)
   ![281686787-bcad93e2-c776-4959-bfad-da2307cd76f8](https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/30f35410-ee99-4fd5-8104-4b75d8aad2c6)

### [Correcting Chromatic Aberration](https://github.com/mleiwe/DataSciencePortfolio/tree/main/ChromaticAberration): 
In biological imaging often the colours smeer (chromatic aberration) which hinders any further analysis. I noticed that we could model the aberration and so reverse its effects to produce an accurate image. This meant we could keep unaffected areas the same (e.g. E) while correcting the distorted areas (e.g. F)
![CA_Fig5](https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/c22f85cd-5c6b-489d-858c-e4ddcac89b55)
