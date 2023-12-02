library(dplyr)

df <- read.delim("~/Downloads/input-2.txt", blank.lines.skip = F, header = F, sep = " ")
names(df) <- c("opponent", "me")


tibble(expand.grid(opponent = c("A", "B", "C"), me = c("X", "Y", "Z"))) %>%
  mutate(play_score = case_when(me == "X" ~ 1, me == "Y" ~ 2, me == "Z" ~ 3),
         win_score = c(3, 0, 6,
                       6, 3, 0,
                       0, 6, 3),
         total_score = play_score + win_score) %>%
  right_join(df) %>%
  .$total_score %>%
  sum()
