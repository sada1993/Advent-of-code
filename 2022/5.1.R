library(dplyr)
library(dequer)
library(stringr)
library(glue)

n_containers <- 9

file_con <- file("~/Downloads/input-5.txt")
file_content <- readLines(con = file_con)
close(file_con)

containers_file <- file_content[1:8]
instructions <- file_content[11:length(file_content)]

#Populate stacks
tbl <- matrix("", nrow = 8, ncol = 9)
for(i in seq_along(containers_file)){
  tbl[i,] <- str_match_all(containers_file[i], "\\[?([A-Z]| {4})\\]?")[[1]][,2]
}

tbl[tbl == "    "] <- NA_character_

#Convert to stacks datastructure
containers <- list()
for(i in 1:n_containers){
  stk <- tbl[,i]
  stk <- stk[!is.na(stk)]
  containers[[i]] <- as.stack(as.list(stk))
}

#Parse instructions
inst <- matrix(0, nrow = length(instructions), ncol = 3)
for(i in 1:nrow(inst)){
  inst[i,] <- as.numeric(str_match(instructions[i], "move (\\d+) from (\\d+) to (\\d+)")[c(2:4)])
}

# Implement instructions
for(i in 1:nrow(inst)){
  instruction <- inst[i,]
  n_containers_to_move <- instruction[1]
  from <- instruction[2]
  to <- instruction[3]
  
  for(j in 1:n_containers_to_move){
    container <- pop(containers[[from]])
    push( containers[[to]], container)
  }
}

# Answer
for(i in 1:n_containers){
  print(pop(containers[[i]]))
}

