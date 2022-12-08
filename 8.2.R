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

scores <- matrix(0, nrow = size, ncol = size)
for(i in 1:size){
  print(i)
  if(i == 1 || i == size) next
  for(j in 1:size){
    if(j == 1 || j == size) next
    
    cur_height <- heights[i,j]
    
    #Look Right
    score_r = 1
    counter <- j
    while(counter+1 < size && cur_height > heights[i, counter+1]){
      score_r <- score_r + 1
      counter <- counter + 1
    }
    
    #Look Left
    score_l = 1
    counter <- j
    while(counter-1 > 1 && cur_height > heights[i, counter-1]){
      score_l <- score_l + 1
      counter <- counter - 1
    }
    
    #Look down
    score_d = 1
    counter <- i
    while(counter+1 < size && cur_height > heights[counter+1, j]){
      score_d <- score_d + 1
      counter <- counter +1
    }
    
    #Look up
    score_u = 1
    counter <- i
    while(counter-1 > 1 && cur_height > heights[counter-1, j]){
      score_u <- score_u + 1
      counter <- counter - 1
    }
    
    scores[i,j] <- score_r * score_l * score_d * score_u
  }
  
}

max(scores)