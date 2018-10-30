# insight_cc

## Problem

 contains Problem, Approach and Run instructions sections
In this data challenge, we perform simple data processing to h1b statistics. We generate two files given h1b statistics data. The output file "top_10_occupations.txt" gives top 10 occupations for certified visa applications. The output file "top_10_states.txt" gives top 10 states for certified visa applications.

For the data, we assume that there are fields "SOC_NAME", "SOC_CODE", "CERTIFIED_STATUS" or "WORK_STATE". It is fine even if they are not named exactly the same as long as they for the first two fields they contain the substring, and a field contain "status" and another field contains both "work" and "status". Please make sure that there exists only 1 column for each field or only 1 column satisfy each requirement. Otherwise, the default would be using the last column that fits the requirement for a given field.

## Approach

My approach for this problem is to first go through the file line by line and store the corresponding number of certified applications for each occupation and state into 2 different dictionary. Then, we sort the list of tuple where the first field is negative number of certified applications an second field being SOC_NAME/state. Therefore, when we are sorting in ascending order, we will have the number of certified applications sorted in descending order and SOC_NAME/state in ascending order alphabetically. (We are using built-in sorting function in python). Then, we take the first 10 item and write them to their corresponding fields.

## Run

With run.sh, it takes 3 arguments where the first one is the path for input file, second and third arguments being the PATH for the two output files.