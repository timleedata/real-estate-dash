import pandas as pd
import re

'''
Cleaning steps:
1. Concat listing and sold df
2. Remove "checked" column
3. Fill nan/nulls w/ blanks
4. Remove html tags
5. Drop duplicates: keep based on sold or not
6. Street -> check for any extra characters (not alphanumeric or '#')
7. City -> Capitalize first letter only, remove non-alpha chars?
8. State -> state abbr.
9. Zip Code -> 5 digit
10. Price -> digits only
11. Bed/Sqft -> digits only
12. Bath -> float only
13. Home Type -> check uniques
14. Neighbord -> Remove "Transportation in "
15. Scores -> 2 digit only
16. Sold History -> formatting and also remove duplicates (maybe use dict {date:price} if date not in dict.keys)
'''

# load listings to dataframes
curr_listings_df = pd.read_csv("data/prepared/rs_df_listed.csv")
sold_listings_df = pd.read_csv("data/prepared/rs_df_sold.csv")
all_listings_df = pd.concat([curr_listings_df, sold_listings_df])

# general
all_listings_df.drop(labels=["checked"], axis=1, inplace=True)
all_listings_df.fillna(value="", inplace=True)
all_listings_df.replace(to_replace="<[^<]*>", value="", regex=True, inplace=True)
all_listings_df.sort_values(by="price", inplace=True)
all_listings_df.drop_duplicates(subset="url", keep="last", inplace=True)

# specific columns
all_listings_df["street"] = all_listings_df["street"].str.title()
all_listings_df["city"] = all_listings_df.apply(lambda row: row["city"].split(",")[0].capitalize(), axis=1)
all_listings_df["zip_code"] = all_listings_df.apply(lambda row: row["zip_code"].split("-")[0], axis=1)
all_listings_df["price"] = all_listings_df.apply(lambda row: row["price"].replace("$", "").replace("+", "").replace(",", "").strip(), axis=1)
all_listings_df["sqft"] = all_listings_df.apply(lambda row: row["sqft"].replace(",", ""), axis=1)
all_listings_df.loc[(all_listings_df["home_type"] == "Multi-Family (2-4 Unit)"), "home_type"] = "MultiFamily"
all_listings_df.loc[(all_listings_df["home_type"] == "Single Family Residential"), "home_type"] = "SingleFamily"
all_listings_df["neighborhood"] = all_listings_df.apply(lambda row: row["neighborhood"].replace(" Transportation in ", ""), axis=1)
all_listings_df["sold_history"] = all_listings_df.apply(lambda row: re.sub("\s\([^\)]*\)", "", string=row["sold_history"].replace("$", "").replace(",", "").replace(" :", ":")), axis=1)

# filter out specific records which need manual cleaning
manual_fix = []
manual_fix.extend(all_listings_df[all_listings_df["street"].str.contains(pat="[^\w#\-\s,\.]")]["url"].tolist())
manual_fix.extend(all_listings_df[(all_listings_df["price"] == "") | (all_listings_df["neighborhood"] == "")]["url"].tolist())
manual_fix.extend(all_listings_df[all_listings_df["sqft"] == "1"]["url"].tolist())
manual_fix.extend(all_listings_df[all_listings_df["home_type"].isin(["", "Other", "Vacant Land", "Parking"])]["url"].tolist())
manual_fix_df = all_listings_df[all_listings_df["url"].isin(manual_fix)].copy()
manual_fix_df["street"] = manual_fix_df["street"].str.title()

# operations on specific columns
filtered_df = all_listings_df[~all_listings_df["url"].isin(manual_fix)].copy()

'''
def main():
    print("Main")
    
if __name__ == "__main__":
    main()
'''