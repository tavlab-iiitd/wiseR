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
    install.packages("igraph", type = "binary")
  }
  if(require('visNetwork')==F)
  {
    install.packages("visNetwork_2.0.9.tar.gz",repos=NULL, type="source")
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
  if(packageVersion("visNetwork")!='2.0.9'){
    detach("package:visNetwork", unload = TRUE)
    install.packages("visNetwork_2.0.9.tar.gz",repos=NULL, type="source")
  }
}
