## nubank_self_control
This application is designed to provide insightful analysis of your Nubank Monthly Account Activity.

Scripts Overview
This repository comprises three essential Python scripts tailored for efficient data manipulation and analysis.

## 1. main.py
Run these file with the possible options and functions to get the result in the console output.
```python
import search_data as sd

dat = sd.search_period(x, '2022-02-01', '2022-02-28')  # Period to analyze

```
Features:
Data Filtering: Utilize filters to target activity-specific descriptions, ensuring precise analysis.

## 2. nu_get_data.py
This script is dedicated to seamlessly loading and merging data from multiple CSV files within a specified directory.

## 3. math_tools.py
This script offers fundamental mathematical functions crucial for financial analysis:

Functions:
input: Calculates the total sum of received money, including transfers and pix.
output: Computes the total sum of bills and other paid outputs.
outcome: Evaluates the net financial result by subtracting output from input.
These functions provide essential insights into your financial activities, facilitating better control and management of your finances.

###4. search_data.py
This script provides a comprehensive set of functions to search and filter your Nubank account data:

functions:
search_description(data, term): This function searches for transactions with descriptions containing a specified term. It returns a dataframe containing the matching transactions.

search_identificator(data, term): This function searches for transactions with identifiers containing a specified term. It returns a dataframe containing the matching transactions.

search_date(data, date): This function searches for transactions that occurred on a specific date. It returns a dataframe containing the transactions from the specified date.

search_period(data, start_time, end_time): This function filters transactions within a specified period, defined by start and end dates. It returns a dataframe containing transactions that fall within the specified period.

search_send_pix(data): This function identifies transactions sent via Pix (instant payment system). It returns a dataframe containing transactions with descriptions indicating they were sent via Pix.

search_receive_pix(data): This function identifies transactions received via Pix (instant payment system). It returns a dataframe containing transactions with descriptions indicating they were received via Pix.

search_tag(data, tag:str): This function searches for transactions with descriptions containing a specific tag or keyword. It returns a dataframe containing transactions with descriptions matching the provided tag.

These functions enable you to efficiently search and filter your Nubank account data based on various criteria, providing you with enhanced control and understanding of your financial transactions.


Licença: Este projeto está licenciado sob a Licença GNU General Public License. Consulte o arquivo LICENSE para obter mais detalhes.

Contato Se você tiver dúvidas ou sugestões, sinta-se à vontade para entrar em contato através do email: mateusmengatto@gmail.com
