library(dplyr)
library(stringr)

df <- read.delim("~/Downloads/input-3.txt", blank.lines.skip = F, header = F, sep = " ", stringsAsFactors = F)
names(df) <- c("rucksack")


points <- tibble(
  letters = c(sapply(c(97:122), intToUtf8), sapply(c(65:90), intToUtf8)),
  points = c(1:26, 27:52)
)


df %>%
  tibble() %>%
  mutate(rucksack_split = str_split(rucksack, ""),
         len = sapply(rucksack_split, length),
         midpoint = len/2) %>%
  rowwise() %>%
  mutate(first = list(rucksack_split[1:midpoint]),
         second = list(rucksack_split[(midpoint+1): len]),
         common_elements = intersect(first, second)) %>%
  ungroup() %>%
  left_join(points, by = c(common_elements = "letters")) %>%
  .$points %>%
  sum
