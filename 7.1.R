library(dplyr)
library(data.tree)
library(glue)
library(stringr)

file_con <- file("~/Downloads/input-7.txt")
file_content <- readLines(con = file_con)
close(file_con)

# Populate a tree data structure
# Use absolute paths from the base to navigate the tree
base <- Node$new("base")
current_directory <- "base"
for(line in file_content){
  if(grepl("^\\$ ls", line)) next()
  if(grepl("^\\$ cd", line)){
    # Change Directory
    if(grepl("^\\$ cd \\.\\.", line)){
      # Move up a directory
      current_directory <- str_match(current_directory, "(.*)_")[[2]]
    }else{
      # Move into a directory
      dir_name <- str_match(line, "^\\$ cd (.*)$")[[2]]
      if(dir_name == "/") next()
      current_directory <- file.path(current_directory, dir_name, fsep = "_")
    }
  }
  
  if(grepl("^\\d+", line)){
    # File name
    file_size <- as.numeric(str_match(line, "^\\d+"))
    file_name <- str_match(line, "^\\d+ (.*)$")[[2]]
    file_path <- file.path(current_directory, file_name, fsep = "_")
    
    eval(parse(text = glue("{file_path} <- {current_directory}$AddChild('{file_path}')")))
    eval(parse(text = glue("{file_path}$size <- {file_size}")))
  }
  
  if(grepl("^dir", line)){
    # Directory name
    dir_name <- file.path(current_directory, str_match(line, "^dir (.*)$")[[2]], fsep = "_")
    
    eval(parse(text = glue("{dir_name} <- {current_directory}$AddChild('{dir_name}')")))
  }
  
}

# Traverse the tree and compute the answer
folders <- names(base$Get('name', pruneFun = isNotLeaf))
sizes <- c()
for(folder in folders){
  eval(parse(text = glue("sizes${folder} <- Aggregate({folder}, 'size', sum)")))
}

cat("Answer: ", sum(unlist(sizes[sizes<100000])), "\n")

# Visualize the tree print(base, "size")