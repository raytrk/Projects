# Data Cleaning Using Excel Power Query

## Disclaimer:

> Item codes and Item Descriptions have been obfuscated in the excel file for confidentiality purposes

---

### Summary:

> This Excel Project serves to extract data from 2 Excel Files, merge them and then extract the significant data.

> What's different from the common Power Query methodology is:
>
> 1. Users do not have to save their files with a specific name.
>    * The Power Query engine will use the latest file within the specified subfolder.

---

### Background

**Generating a list of top 60 items kept in the Pharmacy**

1.  This project was created to obtain the top 60 items kept in the Pharmacy

2.  These top 60 items were made up of the top 30 items by Unit Cost(UC) and top 30 items by Total Value(TV) where TV = UC \* Qty kept in the Pharmacy

3.  There maybe items in both lists, in which case, the next item chosen will be the next in sequence between the 2 lists. I.e.: 
    * 31st item from the top 30 by UC list then
    * 31st item from the top 30 by TV list then
    * 32nd item from the top 30 by UC list .... so on and so forth

5.  These data is not easily extracted from our inventory management system
    * The Stock Balance report details the quantity of each item held
    * The PostStockTake Analysis report details the Unit Cost of each item
6.  Hence a simple file that can generate these top 60 items each month is required.

---

### How to use the excel file

1. Generate the StockBalance Report > Save in SB subfolder

2. Generate the PostStockTakeAnalysisReport > Save in PostStockTakeAnalysisReport subfolder

3. Click Refresh All under the data tab

---

## Key Power Query code [M language]

### General steps:

1. Extract data from the Source excel files
2. Merge the data
3. Create separate queries for the descending list of items by UC and TV, inserting an Index Column (smaller indices = higher ranks)
4. Merge the UC and TV queries
5. Insert a column with the minimum index between the UC and TV queries for each item
6. Sort the list with this new ranking in ascending order
7. Obtain the top 60 items

> Full details of step 1 is expanded below as this is different from the usual Power Query methodology where it empowers non-technical users to change their filepaths and rename subdirectories as required.

---

### Set-up:

1. Copy and paste the following excel formula into a CELL to extract the filepath:

```
=LET(a,CELL("filename",A1), LEFT(a,FIND("[",a)-1))
```

2. Create named ranges for
   i. The cell with the filepath
   ii. Any other cells with the names of the subfolders
   ![alt text](image.png)

3. Create Queries to these named ranges with the following M language code, changing SB to the particular named range required.

```
= Excel.CurrentWorkbook(){[Name="SB"]}[Content]{0}[Column1]
```

---

### Extract the latest file from a subfolder

1. Create queries to your source files with the following M language code.
2. This code extracts data from the latest file saved within the specified subfolder
3. Q_CWD refers to the query for the filepath
4. Q_SB refers to the query for subfolder 1

```
let
    Source = Folder.Files(Q_CWD&"\"&Q_SB),
    #"Sorted Rows" = Table.Sort(Source,{{"Date modified", Order.Descending}}),
    #"Remove Hidden" = Table.SelectRows(#"Sorted Rows", each [Attributes]?[Hidden]? <> true),
    #"Kept First Rows" = Table.FirstN(#"Remove Hidden",1),
    MyWorkbook.xlsx = #"Kept First Rows"[Content]{0},
    #"Imported Excel Workbook1" = Excel.Workbook(MyWorkbook.xlsx),
    LEVEL11_Sheet = #"Imported Excel Workbook1"{[Item="LEVEL11",Kind="Sheet"]}[Data]
in
    LEVEL11_Sheet

```