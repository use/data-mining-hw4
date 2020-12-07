signals <- read.table("synthetic_control_data.txt")
fit <- kmeans(signals, 6)
signals <- cbind(signals, cluster=fit$cluster)

par(mfrow=c(2,3))
for (i in c(1:6)) {
  ts.plot(
    t(signals[signals["cluster"] == i,][1:60]),
    gpars = list(ylim = c(0,70)),
    col = rgb(red = 0, green = 0, blue = 1, alpha = 0.1)
  )
  write.table(
    file = paste("cluster", i, ".csv", sep=""),
    x = signals[signals["cluster"] == i,][1:60],
    row.names = FALSE,
    col.names = FALSE)
  lines(fit$centers[i,], col='red')
}
