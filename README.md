# sparcs_descriptive_2022
Python Assignment: Descriptive Analytics on SPARCS 2022 Data

 **Summary Report**:
   - Write a brief summary of your findings in the notebook:
     - What is the average length of stay?

     - How does the total cost vary by age group or type of admission?

     - Any noticeable trends in admissions or charges?
  
Length of Stay Distribution: The dataset shows the count of hospital stays for various lengths. The most common stays are between 1 to 5 days. The mean length of stay is approximately 49,410.2, with a median of 49,343.0.

Age Group Distribution: The dataset is dominated by patients aged 70 or older (128,947 patients), followed by those aged 50 to 69 (90,430 patients). The smallest group is patients aged 18 to 29 (23,061 patients).

Gender Distribution: The dataset consists of 187,404 females, 153,873 males, and 2 unspecified genders.

**Total Charges and Costs:**

Charges: The mean total charges for patients is $14,434.87, with a median of $15,082.10. The maximum charge in the dataset is $17,690.10, and the minimum is $9,203.04.
Costs: The mean total costs are $2,778.13, with a median of $2,384.85. The maximum cost is $4,825.86, and the minimum is $1,743.66.

Type of Admission Distribution: The most common type of admission is "Emergency" with 233,718 admissions, followed by "Elective" with 55,232. There are also 29,553 "Newborn" admissions.

Warnings in the Code: The dataset includes warnings related to mixed data types in columns, which suggests that cleaning or specifying data types may be necessary for accurate processing.

Visualization Issues: The output mentions future warnings about how color palettes are handled in visualizations, indicating the need for slight adjustments to the plotting code in future versions.