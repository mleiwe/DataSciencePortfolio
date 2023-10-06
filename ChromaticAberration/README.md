# ML solution for solving chromatic aberration in microscopy sample
Improvements in imaging technology and optical clearing have now allowed many researchers to image their samples in 3D. However, this has introduced a new problem: chromatic aberration (different wavelengths of light are shifted to different positions in the image). We investigated this phenomenon using fluorescent beads and found that even with optical lenses that claim to correct for chromatic aberration there were significant deviations along the Z-axis.

We found that across microscopes and lenses, this aberration was linear but unique to each combination. Therefore we wrote code to allow the user to train a linear regressor on ground truth images, and then implement the correction on their images.
![CA_Fig5](https://github.com/mleiwe/DataSciencePortfolio/assets/29621219/c22f85cd-5c6b-489d-858c-e4ddcac89b55)

[Summary write up](https://github.com/mleiwe/DataSciencePortfolio/blob/main/ChromaticAberration/DataScienceFriendlyWriteUp.pages "Portfolio write up")

[Full paper](https://www.frontiersin.org/articles/10.3389/fnana.2021.760063/full "Leiwe et al 2021")

[Repository](https://github.com/mleiwe/ChromaticAberrationCorrection "Functioning Repository")

## Cited by...
[MacCormac et al. 2023](https://www.frontiersin.org/articles/10.3389/fnins.2023.1239764/full): Lightfield hyperspectral imaging in neuro-oncology surgery: an IDEAL 0 and 1 study
[Loi et al. 2023](https://rupress.org/jcb/article/222/4/e202202078/213839/Semi-automated-3D-fluorescence-speckle-analyzer-3D): Semi-automated 3D fluorescence speckle analyzer (3D-Speckler) for microscope calibration and nanoscale measurement
[Goleń et al. 2022](https://www.sciencedirect.com/science/article/abs/pii/S1434461022000311): A Model of F-actin Organization in Granuloreticulopodia in Foraminifera: Morphogenetic and Evolutionary Implications from Novel Fluorescent and Polarised Light Observations
