# wiseR
 Structure learning offers an explainable, expressive and versatile approach to causal and mechanistic modeling of complex biological data. We present wiseR, an open source application for learning, evaluating and deploying robust causal graphical models using graph neural networks and Bayesian networks.

An example use of this package is to learn the best policy that will minimize bad patient-outcomes from a complex multivariate dataset where variables may be expected to have interaction among diseases and physiology. The nature and strength of these interactions is learned in the structure-learning step and these are quantified using inference-learning. The user can then set utility of a particular outcome, e.g. setting high preference for zero episodes of sepsis in the ICU and infer the best possible combination of actions that will minimize the probability of sepsis in the given setting. 

The CRAN release of the package can be installed by running install.packages("wiseR") and the development version can be installed by running devtools::install_github("tavlab-iiitd/wiseR")

Authors: Shubham Maheshwari (shubham14101@iiitd.ac.in), Dr. Tavpritesh Sethi (tavpriteshsethi@iiitd.ac.in)