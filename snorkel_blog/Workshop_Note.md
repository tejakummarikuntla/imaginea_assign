# Snorkel Workshop Notes:

## Introduction to snorkel

Dark Data Extraction
-   The porblem of Training Data.

Most of the preprocessing phase of pipelines has the complexity of 
taking the unstructured data or the Dark Data, like text, Tables, Image, etc, and turning into the structured data which usually takes months or years and to build ML models further.
Before building an ML model over the extracted data, we need to Hand label it, those are called Gold Labels. If we look from Today's Machine Learning pipeline at a high level this explicitly says that people spent most of the time on creating the Training Dataset and little hustle over Feature Engineering as Deep Learning makes it easy, the crucial part of creating a Training data set is labeling that data points correctly, because the performance of the end model totally depends on how well it trained with correct labels. Now, the question is can we hasten up the process of labeling using any Framework ?, This is where Snorkel began to accelerate Data Building and Managing, not only labeling, snorkel has many other features that make the bottlenecks unclogged.
Snorkel: A framework for Rapidly Generating Training Data with Weak Supervision.
> Image: Training Data set creation
## Weak Supervision
By eliminating the Hand labeling process, Now we can programmatically generate labels with external Domain knowledge or any patterns. This results in low-quality lables[Weak labels] more efficiently, which means Weak labels are intended to decrease the cost and increase efficiency. 
Using noisy, imprecise sources for building a large amount of training data in supervised learning is called Weak Supervision. One of the famous methodologies of weak labeling is Distant supervision.
To reiterate Snorkel is an open-source system for quickly assembling training data through weak supervision.

## What Snorkel can do?
Snorkel currently has three features for creating and handling training data sets.
- **Data Labeling:** Assigning a value to each data point based on Heruristc, Distant Supervision Techniques, etc.,
- **Data Transformation:** Converting existing data from one format to another or modifying the data which doesn't affect actual labels. e.g: rotating an image in different angles, etc.,
- **Data Slicing:** Segmenting a data set into required subsets for different purposes like improving model perfomance.

![Abstractions](/Images/fig_abstractions.png)


## How Snorkel does it?


![work_flow](/Images/Snorkel_HighLevel_WorkFlow.png)



![work_flow](/Images/snorkel_Labeling_overview.png)