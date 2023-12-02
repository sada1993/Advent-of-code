library(dplyr)
library(stringr)

is_buffer_unique <- function(buffer){
  length(unique(buffer)) == length(buffer)
}

file_con <- file("~/Downloads/input-6.txt")
file_content <- readLines(con = file_con)
close(file_con)

stream <- str_split(file_content, "")[[1]]

# Populate buffer
for(i in seq_along(stream)){
  print(i)
  buffer <- stream[i:(i + 13)]
  if(is_buffer_unique(buffer)) break()
}

print(i + 13)
