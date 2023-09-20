# DataSciencePortfolio
Check here for a showcase of the data science and data analysis projects that I've done

## Project List
### dCrawler
Data may sometimes be clustered where
1. We don't know the the final number of clusters (ruling out k-means)
2. The clusters may be neighbouring each other (ruling out DBSCAN)
3. The densities of each cluster are not even, or Gaussian (ruling out Mean-Shift Clustering)

Therefore, I developed an unsupervised clustering algorithm that relies on a single metric, Th(d). It follows three key phases: 
1. An initial crawl/allocation of points to clusters
2. An adjustment phase, where points are allocated to their nearest cluster centroid
3. Finally a merging of clusters whose centroids are within Th(d)

https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/de4ea1c5-5647-4c7a-a54f-5da4afb69c3d

[Basic Description](https://github.com/mleiwe/dCrawler/blob/main/Schema_For_dCrawler.pdf)

[As featured in](https://www.biorxiv.org/content/10.1101/2022.10.20.512984v1)

[Full Repository](https://github.com/mleiwe/dCrawler)

[Examples] ---> Coming soon

### ML solution for solving chromatic aberration in microscopy sample
Improvements in imaging technology and optical clearing have now allowed many researchers to image their samples in 3D. However, this has introduced a new problem: chromatic aberration (different wavelengths of light are shifted to different positions in the image). We investigated this phenomenon using fluorescent beads and found that even with optical lenses that claim to correct for chromatic aberration there were significant deviations along the Z-axis.

We found that across microscopes and lenses, this aberration was linear but unique to each combination. Therefore we wrote code to allow the user to train a linear regressor on ground truth images, and then implement the correction on their images.
![CA_Fig5](https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/c22f85cd-5c6b-489d-858c-e4ddcac89b55)

[Summary write up](https://google.com "Portfolio write up")

[Full paper](https://www.frontiersin.org/articles/10.3389/fnana.2021.760063/full "Leiwe et al 2021")

[Repository](https://github.com/mleiwe/ChromaticAberrationCorrection "Functioning Repository")

