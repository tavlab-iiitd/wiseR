dependency<-function()
{
  if (!requireNamespace("BiocManager"))
    install.packages("BiocManager")
  if(require('graph')==F)
  {
    BiocManager::install('graph')
  }
  if(require('igraph')==F)
  {
    install.packages('igraph',type = "binary")
  }
  if(require('bnlearn')==F)
  {
    install.packages('bnlearn',type = "binary")
  }
  if(require('HydeNet')==F)
  {
    install.packages('HydeNet',type = "binary")
  }
  if(require('rhandsontable')==F)
  {
    install.packages('rhandsontable',type = "binary")
  }
  if(require('visNetwork')==F)
  {
    install.packages('visNetwork',type = "binary")
  }
  if(require('missRanger')==F)
  {
    install.packages('missRanger',type = "binary")
  }
  if(require('arules')==F)
  {
    install.packages('arules',type = "binary")
  }
  if(require('psych')==F)
  {
    install.packages('psych',type = "binary")
  }
  if(require('DescTools')==F)
  {
    install.packages('DescTools',type = "binary")
  }
  if(require('DT')==F)
  {
    install.packages('DT',type = "binary")
  }
  if(require('linkcomm')==F)
  {
    install.packages('linkcomm',type = "binary")
  }
  if(require('reticulate')==F)
  {
    install.packages('reticulate',type = "binary")
  }
  if(require('RBGL')==F)
  {
    BiocManager::install('RBGL')
  }
  if(require('Rgraphviz')==F)
  {
    BiocManager::install('Rgraphviz')
  }
  if(require('gRbase')==F)
  {
    install.packages('gRbase')
  }
  if(require('gRain')==F)
  {
    install.packages('gRain')
  }
  if(!"RCy3" %in% installed.packages()){
    BiocManager::install("RCy3")
  }
  library(RCy3)
  if(require('reticulate')==F){
    install.packages("reticulate")
    conda_create("wiser")
    #conda_install("wiser", "pytorch")
    #conda_install("wiser", "matplotlib")
    #conda_install("wiser", "networkx")
    #conda_install("wiser", "pandas")
    #conda_install("wiser", "scipy")
    #conda_install("wiser", "scikit-learn")
  }
}
