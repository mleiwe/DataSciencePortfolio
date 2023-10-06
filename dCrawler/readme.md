## dCrawler
<img width="1255" alt="Screenshot 2023-09-20 at 10 27 12 AM" src="https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/154d7662-9406-4930-ad9a-df73f0365e53">

Data may sometimes be clustered where
1. We don't know the the final number of clusters (ruling out k-means)
2. The clusters may be neighbouring each other (ruling out DBSCAN)
3. The densities of each cluster are not even, or Gaussian (ruling out Mean-Shift Clustering)

Therefore, I developed an unsupervised clustering algorithm that relies on a single metric, Th(d). It follows three key phases: 
1. An initial crawl/allocation of points to clusters
2. An adjustment phase, where points are allocated to their nearest cluster centroid
3. Finally a merging of clusters whose centroids are within Th(d)

[dCrawler Demonstration](https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/de4ea1c5-5647-4c7a-a54f-5da4afb69c3d)

[Basic Description](https://github.com/mleiwe/dCrawler/blob/main/Schema_For_dCrawler.pdf)

[As featured in](https://www.biorxiv.org/content/10.1101/2022.10.20.512984v1)

[Full Repository](https://github.com/mleiwe/dCrawler)

[Examples](https://docs.google.com/presentation/d/1GiOclAU5ou5rQsCh44iIiMeyRRVG1xwc_2LyqghLLLw/edit?usp=sharing)
