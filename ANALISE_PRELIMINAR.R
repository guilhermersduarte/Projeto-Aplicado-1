df = read.csv("Walmart_sales.csv")
summary(df)
print(df[df$Store==1,]$Date)
print(df[df$Date=='23-04-2010',]$Unemployment)
print(df[df$Date=='17-08-2012',]$Unemployment)

