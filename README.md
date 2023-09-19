# DataSciencePortfolio
Check here for a showcase of the data science and data analysis projects that I've done

## Project List
### ML solution for solving chromatic aberration in microscopy sample
Improvements in imaging technology and optical clearing have now allowed many researchers to image their samples in 3D. However, this has introduced a new problem: chromatic aberration (different wavelengths of light are shifted to different positions in the image). We investigated this phenomenon using fluorescent beads and found that even with optical lenses that claim to correct for chromatic aberration there were significant deviations along the Z-axis

We found that across microscopes and lenses, this aberration was linear but unique to each combination. Therefore we wrote code to allow the user to train a linear regressor on ground truth images, and then implement the correction on their images.
![image](https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/3e733129-7ea1-440c-89ed-159d07a8ce16)

Full paper found here https://www.frontiersin.org/articles/10.3389/fnana.2021.760063/full
