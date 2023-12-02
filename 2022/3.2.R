library(dplyr)
library(stringr)

df <- read.delim("~/Downloads/input-3.txt", blank.lines.skip = F, header = F, sep = " ", stringsAsFactors = F)
names(df) <- c("rucksack")


points <- tibble(
  letters = c(sapply(c(97:122), intToUtf8), sapply(c(65:90), intToUtf8)),
  points = c(1:26, 27:52)
)

x <- c(1:(nrow(df)/3))
x <- c(x,x,x)
x <- x[order(x)]

df %>%
  tibble() %>%
  mutate(rows = x,
         rucksack = str_split(rucksack, "")) %>%
  group_by(rows) %>%
  summarise(rucksack = list(rucksack)) %>%
  ungroup() %>%
  rowwise() %>%
  mutate(inter = intersect(intersect(rucksack[[1]], rucksack[[2]]), rucksack[[3]])) %>%
  left_join(points, by = c(inter = "letters")) %>%
  .$points %>%
  sum
