import pandas as pd

students = pd.DataFrame({
  "name": ["Daniel", "John", "Lucy"],
  "grade": [99, 80, 92],
  "nationality": ["israeli", "american", "british"]
})

# students.to_csv("students.csv")

def fromCSV_toExcel(file):
  ob = pd.read_csv(file)
  return ob.to_excel("new_excel.xlsx")

fromCSV_toExcel("students.csv")