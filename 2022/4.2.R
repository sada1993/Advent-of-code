library(dplyr)
library(tidyr)
library(stringr)

df <- read.delim("~/Downloads/inputs-4.txt", blank.lines.skip = F, header = F, sep = " ")

df %>%
  tibble() %>%
  separate(col = V1, into = c("elf1", "elf2"), sep = ",") %>%
  rowwise() %>%
  mutate(elf1 = list(seq(as.numeric(str_match(elf1, "(\\d+)-")[2]), 
                         as.numeric(str_match(elf1, "-(\\d+)")[2])
  )),
  elf2 = list(seq(as.numeric(str_match(elf2, "(\\d+)-")[2]), 
                  as.numeric(str_match(elf2, "-(\\d+)")[2])
  ))
  ) %>%
  mutate(inter = list(intersect(elf1, elf2))) %>%
  mutate(overlaps = length(inter) != 0) %>%
  .$overlaps %>%
  sum
