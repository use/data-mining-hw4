par(mfrow=c(2,3)) # create grid of graphs on a single image
filenames <- list.files(pattern="cluster-.*.csv")
for (file in filenames) {
    data = read.csv(file)
    ts.plot(
      t(data), # transpose, or else the graphs will make no sense...
      gpars=list(ylim=c(0,70)), # set range for the graph
      col=rgb(red = 0, green = 0, blue = 1, alpha = 0.1)) # colors, with alpha
      # if centroids are stored as the first item,
      # the following can be used to highlight them on the graphs
      lines(t(data)[,1], col='red')
}
