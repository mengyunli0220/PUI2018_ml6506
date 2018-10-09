# Assignment 1: Review your classmate's Citibike project proposal

This is a review of Mengyun Li's hypothesis by Keundeok Park.

#### a. verify that their Null and alternative hypotheses are formulated correctly

* There is no alternative hypothesis but it can be infered by the null hypothesis.
    * It could be *People born after 1980 are more to use CITIbike than people born before 1980 or same as people born before 1980.*
* Little mistake 1908 -> 1980.
* Signficance level is set.

#### b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

* Extracted data support hypothesis with additional information which was not refered in hypothesis.
    * In this case, we do not really need date data since the hypothesis is about the year that person is born. It looks that hypothesis changed
    * Grouping by birth year has been done.

#### c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

* I think t-test which compare two groups is proper statistical test for this case.
* So that we can find out difference between birth before 1980 group and birth after 1980 group.