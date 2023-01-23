# |||     ZAD 1    |||

#install.packages("magrittr")
library(magrittr)

#zad1_list_10_elements <- c(6,9,2,3,8,3,6,8,1,2)
#print(zad1_list_10_elements)

zad1_list <- 1:10
wynik_zad1_1 <- zad1_list %>% log2() %>% sin() %>% sum() %>% sqrt()
print(zad1_list)
print(wynik_zad1_1)

data(iris)
print(head(iris))

wynik_zad1_2 <- iris %>% aggregate(. ~ Species, .,mean)
print(wynik_zad1_2)

# |||    ZAD 2     |||

#install.packages("ggplot2")
library("ggplot2")

Zad2_p1 <- ggplot(iris, aes(x=Petal.Length, color = Species)) + 
geom_histogram(fill="white", position="dodge", bins = 20) +
geom_vline(data=wynik_zad1_2, aes(xintercept=Petal.Length, color=Species),linetype="dashed")


#install.packages("GGally")
library("GGally") 

zad2_p2 <- ggpairs(data=iris, aes(color = Species))

#|||    Zad 3     |||

library(cluster)

X <- iris[,c("Sepal.Length","Sepal.Width","Petal.Length","Petal.Width")]
Y <- iris[,c("Species")]

Tot_list = list()
for (i in 1:10) {
    loopedkmeans <- kmeans(X, i, iter.max = 10, nstart = 1)
    loopedtot <- loopedkmeans$tot.withinss
    Tot_list <- append(Tot_list,loopedtot)
}
elbow_plot_data <- data.frame(unlist(Tot_list))
Zad3_p1 <- ggplot(data=elbow_plot_data, aes(x=1:10, y = unlist.Tot_list.)) +
    geom_line() +
    geom_point()

kmeans3 <- kmeans(X, 3, iter.max = 10, nstart = 1)

iris_extended <- iris
iris_extended["Cluster"] <- kmeans3["cluster"]
Zad3_p2 <- ggplot(iris_extended, aes(x=Petal.Length, y=Petal.Width, color = Cluster)) + geom_point()
Zad3_p3 <- ggplot(iris_extended, aes(x=Petal.Length, y=Petal.Width, color = Species)) + geom_point()


