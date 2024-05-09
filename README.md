<h1>Multinomial Choice Probability Calculation using Logistic Function</br></h1>

**Introduction**</br>
In this project, we explore the calculation of probabilities for each alternative in a
multinomial choice setting using the logistic function. The goal is to understand how
different independent variables influence the probabilities of choosing each alternative.

**Assumptions**</br>
We assume a multinomial logit model where the probability of each alternative is
calculated using a logistic function.</br>
The dataset contains independent variables such as 'X1', 'X2', 'Sero', and 'S1'.</br>
We have parameters ('β') for each variable to compute the deterministic utility for each
alternative.</br>
The alternatives ('AV1', 'AV2', 'AV3') have corresponding utility functions.</br>

**Methodology**</br>
*Data Description:*</br>
The dataset consists of the following variables:</br>
'X1': Independent variable 1</br>
'X2': Independent variable 2</br>
'Sero': Independent variable 3</br>
'S1': Independent variable 4</br>
'AV1', 'AV2', 'AV3': Alternatives</br>
*Utility Functions:*</br>
Utility functions are defined for each alternative based on the provided parameters and
data:</br>
V1 = β01 + β1*X1 + βS1,13*S1</br>
V2 = β02 + β2*X2 + βS1,23*S1</br>
V3 = β03 + β1*Sero + β2*Sero</br>
*Probability Calculation:*</br>
Probabilities for each alternative are calculated using the logistic function:</br>
P1 = exp(V1) / (exp(V1) + exp(V2) + exp(V3))</br>
P2 = exp(V2) / (exp(V1) + exp(V2) + exp(V3))</br>
P3 = exp(V3) / (exp(V1) + exp(V2) + exp(V3))</br>

**Results**</br>
The probabilities of choosing each alternative ('AV1', 'AV2', 'AV3') were calculated based
on the given dataset and parameters. Here are the summarized findings:</br>
AV1: The probability of choosing AV1 ranged from approximately 0.24 to 0.58 across
the dataset.</br>
Higher values of 'X1' and 'S1' tended to increase the probability of choosing AV1.</br>
AV2: The probability of choosing AV2 ranged from approximately 0.25 to 0.49 across
the dataset.</br>
Higher values of 'X2' and 'S1' tended to increase the probability of choosing AV2.</br>
AV3: The probability of choosing AV3 ranged from approximately 0.17 to 0.35 across
the dataset.</br>
Higher values of 'Sero' and 'S1' tended to increase the probability of choosing AV3.</br>

**Conclusion**</br>
The multinomial choice probabilities were successfully calculated using the logistic
function and the provided utility functions.</br>
Different combinations of independent variables influenced the probabilities of choosing
each alternative.</br>
This analysis provides insights into how various factors impact decision-making in a
multinomial choice scenario.</br>
