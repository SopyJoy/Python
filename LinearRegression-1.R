year <- c(2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023)
yearNum <- c(413,335,403,277,272,413,417,462,328,891,826,631,806,844)
datadf <- data.frame(yearNum,year)

lmYearNum = lm(year~yearNum, data = datadf)
summary(yearNum)

par(mar = c(1, 1, 1, 1))

plot(yearNum, year, main = "Linear Model for Polio",
     xlab = "Polio Number", ylab = "Year",
     pch = 20, cex = 1, frame = TRUE, col = "blue")
abline(lmYearNum)

scatter.smooth(year~yearNum, data = datadf)

#dataImport <- read.csv("T35.csv")