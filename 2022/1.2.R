library(dplyr)

df <- read.delim("~/Downloads/input-1.txt", blank.lines.skip = F, header = F)
names(df) <- "col1"

df %>% 
  mutate(isna = is.na(col1),
         elfnum = cumsum(isna),
         elfnum = elfnum+1) %>%
  filter(!is.na(col1)) %>%
  group_by(elfnum) %>%
  summarise(calories = sum(col1)) %>%
  mutate(ranks = rank(calories)) %>%
  filter(ranks > nrow(.)-3) %>%
  .$calories %>%
  sum()
