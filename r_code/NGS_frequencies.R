library(utils)
library(dplyr)

#Routine to read in all Sanger tsv files for parentals
files_to_read <- list.files(path = "",pattern = "\\.tsv$",full.names = T)
names(files_to_read) <- gsub(".tsv","", files_to_read)

all_files <- lapply(files_to_read,function(x) {
  read.table(file = x,
             sep = '\t',
             stringsAsFactors = FALSE,
             header = TRUE)
})

all_data <- bind_rows(all_files, .id = "Sample")

#Write a routine that makes a new "Clone" column in the sangertsv dataframe
all_data$Clone = paste(all_data$CDR.H1, all_data$CDR.H2, all_data$CDR.H3, sep="_")
selected_data <- all_data %>% select(cloneID, VH, Clone)

#Routine to read in all NGS VH tables into a list of dataframes
path_variable = ""
listfiles <- list.files(path = path_variable, pattern = "VH.freq.total.table.txt")

list.df.freq <- list()

for (i in 1:length(listfiles)){
  df <- read.table(paste0(path_variable, listfiles[i]), skip = 1, header = F, sep = '\t', stringsAsFactors = F)
  names(df) <- c("VH_Clone","Freq")
  df[,"Clone"] <- gsub("IGH.*SH2_","",df$VH_Clone)
  df <- df %>% select(-"VH_Clone")
  list.df.freq[[i]] <- df
}

length(list.df.freq)
combined_list <- list()

#Write a routine that combines the sangertsv dataframe with EACH VH freq table dataframe
for (i in 1:length(list.df.freq)) {
  sanger_frequency_df <- merge(selected_data, list.df.freq[[i]], by="Clone")
}
