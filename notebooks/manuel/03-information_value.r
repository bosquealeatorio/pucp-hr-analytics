## Cálculo de information value para las variables 

library(Information)
library(openxlsx)
library(readr)

rm(list = ls())

data <- read_csv('../../data/raw/preprocess_v1_train.csv' )
View(data)

iv <- Information::create_infotables(data=data, y="is_promoted", parallel=FALSE)
print(iv$Summary)
tables <- iv$Tables
tables$gender

wb <- createWorkbook()

addWorksheet(wb, 'iv')
writeData(wb, sheet = 'iv', iv$Summary, colNames = TRUE)

for (name in names(tables))
{
  table_variable = tables[name]
  addWorksheet(wb, name)
  writeData(wb, sheet = name, table_variable, colNames = TRUE)
}

saveWorkbook(wb, file = "'../../data/descriptives/information_value.xlsx'", overwrite = TRUE)