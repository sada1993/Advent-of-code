library(dplyr)
library(stringr)

file_con <- file("~/Downloads/input-8.txt")
file_content <- readLines(con = file_con)
close(file_con)

file_content <- str_split(file_content, "")
size <- length(file_content)

#Assume a square is provided, length = width

visible <- matrix(FALSE, nrow = size, ncol = size)
heights <- matrix(0, nrow = size, ncol = size)

for(i in 1:size){
  heights[i,] <- file_content[[i]]
}

visible[1,] <- rep(TRUE, size)
visible[size,] <- rep(TRUE, size)
visible[,1] <- rep(TRUE, size)
visible[,size] <- rep(TRUE, size)
# Left
for(i in 1:size){
  slice <- heights[i,]
  prev_tree <- 0
  for(j in 1:size){
    cur_tree <- slice[j]
    if(prev_tree < cur_tree){
      visible[i,j] <- TRUE
      prev_tree <- slice[j]
    }
  }
}

#Right
for(i in 1:size){
  slice <- heights[i,]
  prev_tree <- 0
  for(j in 1:size){
    cur_tree <- slice[size - j + 1]
    if(prev_tree < cur_tree){
      visible[i,size - j + 1] <- TRUE
      prev_tree <- slice[size - j + 1]
    }
  }
}

#Top
for(i in 1:size){
  slice <- heights[,i]
  prev_tree <- 0
  for(j in 1:size){
    cur_tree <- slice[j]
    if(prev_tree < cur_tree){
      visible[j,i] <- TRUE
      prev_tree <- slice[j]
    }
  }
}

#Bottom
for(i in 1:size){
  slice <- heights[,i]
  prev_tree <- 0
  for(j in 1:size){
    cur_tree <- slice[size - j + 1]
    if(prev_tree < cur_tree){
      visible[size - j + 1,i] <- TRUE
      prev_tree <- slice[size - j + 1]
    }
  }
}

sum(visible)
