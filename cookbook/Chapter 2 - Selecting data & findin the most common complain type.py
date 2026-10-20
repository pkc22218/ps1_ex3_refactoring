# %%
import matplotlib.pyplot as plt
import polars as pl

# %%
# We're going to use a new dataset here, to demonstrate how to deal with larger datasets. This is a subset of the of 311 service requests from [NYC Open Data](https://nycopendata.socrata.com/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9).
# Read all columns as strings to handle mixed values such as zip codes with dashes.
pl_complaints = pl.read_csv("../data/311-service-requests.csv", infer_schema_length=0)
pl_complaints.head()

# %%
# Selecting columns:
pl_complaints.get_column("Complaint Type")

# %%
# Get the first 5 rows of a dataframe
pl_complaints[:5]

# %%
# Combine these to get the first 5 rows of a column:
pl_complaints["Complaint Type"][:5]

# %%
# Selecting multiple columns
pl_complaints[["Complaint Type", "Borough"]]

# %%
# What's the most common complaint type?
complaint_counts = pl_complaints["Complaint Type"].value_counts()
complaint_counts[:10]

# %%
# Plot the top 10 most common complaints
top_complaints = complaint_counts.sort("count", descending=True)[:10]
plt.bar(
    top_complaints["Complaint Type"].to_list(),
    top_complaints["count"].to_list(),
)
plt.title("Top 10 Complaint Types")
plt.xlabel("Complaint Type")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# %%
