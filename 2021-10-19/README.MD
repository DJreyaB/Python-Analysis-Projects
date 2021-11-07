# Pumpkin Analysis
A quantitative analyis of giant fruit and vegetable data gathered from Great Pumpkin competitions.

## TABLE OF CONTENTS

* [Background](#background)
    * [Data Dictionary](#data-dictionary)
* [Objective](#objective)
* [Tools and Packages](#tools)
* [Project Structure](#project-structure)
* [Data Collection](#data-collection)
* [Data Pre-Processing](#data-preprocessing)
* [Data Modeling](#data-modeling)
* [Data Visualization](#data-visualization)
* [Results](#results)
* [Conclusion](#conclusion)
* [References](#references)
* [Challenges and Future Work](#challenges-and-futurework)

# BACKGROUND

The data this week comes from [BigPumpkins.com](http://www.bigpumpkins.com/ViewArticle.asp?id=132).

> The Great Pumpkin Commonwealth's (GPC) mission cultivates the hobby of growing giant pumpkins throughout the world by establishing standards and regulations that ensure quality of fruit, fairness of competition, recognition of achievement, fellowship and education for all participating growers and weigh-off sites.
### DATA-DICTIONARY

# `data/unclean_pumpkins.csv`

|variable          |class     |description |
|:-----------------|:---------|:-----------|
|id                |character |Year-type|
|place             |character |Place/ranking |
|weight_lbs        |character |Weight in pounds |
|grower_name       |character |Name of grower |
|city              |character |City|
|state_prov        |character |State/Province|
|country           |character |Country|
|gpc_site          |character |GPC site (great pumpkin commonwealth) |
|seed_mother       |character |Seed mother|
|pollinator_father |character |Father |
|ott               |character |Over the top inches, can be used to estimate weight |
|est_weight        |character |Estimated weight in lbs |
|pct_chart         |character |Percent on chart |
|variety           |character |Variety of pumpkin |

Types: F = "Field Pumpkin", P = "Giant Pumpkin", S = "Giant Squash", W = "Giant Watermelon", L = "Long Gourd" (length in inches, not weight in pounds), T = Tomato

[Great Pumpkin Commonwealth rule book](https://gpc1.org/wp-content/uploads/2021/03/GPC-Rules-and-Handbook-2021.pdf)


## DATA-PREPROCESSING

<b> Data Cleaning </b> 
<li> Split ID column into 2 columns (Year, Type) using a dictionary to map the types </li>
