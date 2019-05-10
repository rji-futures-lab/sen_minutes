setwd("~/Desktop/senate_minutes/data")

witness_for <- read.csv('witness_for.csv', stringsAsFactors=F)
witness_against <- read.csv('witness_against.csv', stringsAsFactors=F)

committees_1 <- distinct(witness_for, committee)
committees_2 <- distinct(witness_against, committee)

