{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "BUAN_6340_Report_Final.ipynb",
      "version": "0.3.2",
      "provenance": [],
      "collapsed_sections": [
        "H3VzsTGaVuDb",
        "8LZIheSBVuDc",
        "ZObb7XQFVuDi",
        "Ziy1NXlhVuDm",
        "qKYY0xdfryQd",
        "IkRSqEDBsdMh",
        "j2D-dtwOtAoZ",
        "qlrgCpI-tVKY",
        "XrUEx7rkVuDr",
        "jcglW3ZnVuDu",
        "kXzvwwOQVuDy",
        "nlugmUVhVuD4",
        "g8K4zaGVVuD9",
        "_-fXPGKBVuD-",
        "aADPRIu2VuEE",
        "svRw0pJlVuEL",
        "rMut7RY1VuEP",
        "sHQnGJVqVuEX",
        "oOJ1oWEpVuEY",
        "d4AZ1R80VuEc",
        "Kqy8ZTtUVuEe",
        "VKKj6qTtVuEi",
        "rvG512g9VuEj",
        "DtJUOH2tVuEm",
        "kcvHcBPCVuEp"
      ]
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.6.4"
    },
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "T6KNW55XVt__",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from IPython.core.interactiveshell import InteractiveShell\n",
        "InteractiveShell.ast_node_interactivity = \"all\""
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tMiWeaXPVuAD",
        "colab_type": "text"
      },
      "source": [
        "# Default of Credit Card Clients Data Set \n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ISjxMcPKVuAG",
        "colab_type": "text"
      },
      "source": [
        "# 1. Introduction"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kjNMTFRMVuAJ",
        "colab_type": "text"
      },
      "source": [
        "## 1.1 Project Motivation/Background"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PQGwoX31Wzt_",
        "colab_type": "text"
      },
      "source": [
        "Credit cards have been viewed as a competitive banking product which helps to improve a bank’s financial position. Credit card had a $28.84 trillion global market in 2014 (lsmail, 2014). For the convenience of citizens abroad traveling, credit cards were first issued in Taiwan in 1973. In year 2000, electronic payment on the internet have been established, which lead to a rapid expansion of credit card market (Lee, 2011).   \n",
        "Credit card payment becomes one of the most common and popular payment method for online purchasing. Financial corporations process payments between store and card banks, enabling millions of users around the world to make purchases with branded credit cards. In year 2005, there are forty-nine credit card banks located in Taiwan, and the number of credit cards issued had reached 45 million (Lee, 2011).   \n",
        "The size of credit card market has given consumers more opportunities for making purchasing. Credit card holders from different age groups, different education level, and different gender have different usage behaviors. It is meaningful for banks and financial institutions to investigating the credit card default issue and predicting the default of all clients in various condition.   \n",
        "In this paper, we explored the factors influencing the defaults of credit card clients, tried to determine how much each factor contribute to the default of credit card, and proposed a model for predicting default of credit card clients. "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "savnt9lIVuAM",
        "colab_type": "text"
      },
      "source": [
        "## 1.2 Data Set Information:  \n",
        "\n",
        "This research aimed at the case of customers default payments in Taiwan and compares the predictive accuracy of probability of default among six data mining methods. From the perspective of risk management, the result of predictive accuracy of the estimated probability of default will be more valuable than the binary result of classification - credible or not credible clients. Because the real probability of default is unknown, this study presented the novel â€œSorting Smoothing Method to estimate the real probability of default.   \n",
        "\n",
        "With the real probability of default as the response variable (Y), and the predictive probability of default as the independent variable (X), the simple linear regression result (Y = A + BX) shows that the forecasting model produced by artificial neural network has the highest coefficient of determination; its regression intercept (A) is close to zero, and regression coefficient (B) to one. Therefore, among the six data mining techniques, artificial neural network is the only one that can accurately estimate the real probability of default."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XToVs2uIVuAM",
        "colab_type": "text"
      },
      "source": [
        "### Attribute Information:\n",
        "\n",
        "This research employed a binary variable, default payment (Yes = 1, No = 0), as the response variable. This study reviewed the literature and used the following 23 variables as explanatory variables:  \n",
        "X1: Amount of the given credit (NT dollar): it includes both the individual consumer credit and his/her family (supplementary) credit.  \n",
        "X2: Gender (1 = male; 2 = female).  \n",
        "X3: Education (1 = graduate school; 2 = university; 3 = high school; 4 = others).  \n",
        "X4: Marital status (1 = married; 2 = single; 3 = others).  \n",
        "X5: Age (year).  \n",
        "X6 - X11: History of past payment. We tracked the past monthly payment records (from April to September, 2005) as follows:   \n",
        "X6 = the repayment status in September, 2005;    \n",
        "X7 = the repayment status in August, 2005; . . .;  \n",
        "X11 = the repayment status in April, 2005.   \n",
        "The measurement scale for the repayment status is: -1 = pay duly; 1 = payment delay for one month; 2 = payment delay for two months; . . .; 8 = payment delay for eight months; 9 = payment delay for nine months and above.  \n",
        "X12-X17: Amount of bill statement (NT dollar). X12 = amount of bill statement in September, 2005; X13 = amount of bill statement in August, 2005; . . .; X17 = amount of bill statement in April, 2005.  \n",
        "X18-X23: Amount of previous payment (NT dollar). X18 = amount paid in September, 2005; X19 = amount paid in August, 2005; . . .;X23 = amount paid in April, 2005. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iJ-F2CY5VuAN",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "np.random.seed(0)\n",
        "\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "%matplotlib inline "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rHWokOmGVuAP",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "data = pd.read_csv('credit_default.csv') # relative directory"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aidtXdJyVuAS",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# make a copy of the dataset for EDA\n",
        "data1 = data.copy()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "gGFDohCHVuAV",
        "colab_type": "code",
        "outputId": "bd347bb6-4b56-4e7d-957a-4544b5c258d4",
        "colab": {}
      },
      "source": [
        "data1.describe().T"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>count</th>\n",
              "      <th>mean</th>\n",
              "      <th>std</th>\n",
              "      <th>min</th>\n",
              "      <th>25%</th>\n",
              "      <th>50%</th>\n",
              "      <th>75%</th>\n",
              "      <th>max</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>ID</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>15000.500000</td>\n",
              "      <td>8660.398374</td>\n",
              "      <td>1.0</td>\n",
              "      <td>7500.75</td>\n",
              "      <td>15000.5</td>\n",
              "      <td>22500.25</td>\n",
              "      <td>30000.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>LIMIT_BAL</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>167484.322667</td>\n",
              "      <td>129747.661567</td>\n",
              "      <td>10000.0</td>\n",
              "      <td>50000.00</td>\n",
              "      <td>140000.0</td>\n",
              "      <td>240000.00</td>\n",
              "      <td>1000000.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>SEX</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>1.603733</td>\n",
              "      <td>0.489129</td>\n",
              "      <td>1.0</td>\n",
              "      <td>1.00</td>\n",
              "      <td>2.0</td>\n",
              "      <td>2.00</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>EDUCATION</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>1.853133</td>\n",
              "      <td>0.790349</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.00</td>\n",
              "      <td>2.0</td>\n",
              "      <td>2.00</td>\n",
              "      <td>6.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>MARRIAGE</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>1.551867</td>\n",
              "      <td>0.521970</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1.00</td>\n",
              "      <td>2.0</td>\n",
              "      <td>2.00</td>\n",
              "      <td>3.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>AGE</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>35.485500</td>\n",
              "      <td>9.217904</td>\n",
              "      <td>21.0</td>\n",
              "      <td>28.00</td>\n",
              "      <td>34.0</td>\n",
              "      <td>41.00</td>\n",
              "      <td>79.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_0</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>-0.016700</td>\n",
              "      <td>1.123802</td>\n",
              "      <td>-2.0</td>\n",
              "      <td>-1.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>8.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_2</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>-0.133767</td>\n",
              "      <td>1.197186</td>\n",
              "      <td>-2.0</td>\n",
              "      <td>-1.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>8.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_3</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>-0.166200</td>\n",
              "      <td>1.196868</td>\n",
              "      <td>-2.0</td>\n",
              "      <td>-1.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>8.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_4</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>-0.220667</td>\n",
              "      <td>1.169139</td>\n",
              "      <td>-2.0</td>\n",
              "      <td>-1.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>8.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_5</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>-0.266200</td>\n",
              "      <td>1.133187</td>\n",
              "      <td>-2.0</td>\n",
              "      <td>-1.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>8.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_6</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>-0.291100</td>\n",
              "      <td>1.149988</td>\n",
              "      <td>-2.0</td>\n",
              "      <td>-1.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>8.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT1</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>51223.330900</td>\n",
              "      <td>73635.860576</td>\n",
              "      <td>-165580.0</td>\n",
              "      <td>3558.75</td>\n",
              "      <td>22381.5</td>\n",
              "      <td>67091.00</td>\n",
              "      <td>964511.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT2</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>49179.075167</td>\n",
              "      <td>71173.768783</td>\n",
              "      <td>-69777.0</td>\n",
              "      <td>2984.75</td>\n",
              "      <td>21200.0</td>\n",
              "      <td>64006.25</td>\n",
              "      <td>983931.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT3</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>47013.154800</td>\n",
              "      <td>69349.387427</td>\n",
              "      <td>-157264.0</td>\n",
              "      <td>2666.25</td>\n",
              "      <td>20088.5</td>\n",
              "      <td>60164.75</td>\n",
              "      <td>1664089.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT4</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>43262.948967</td>\n",
              "      <td>64332.856134</td>\n",
              "      <td>-170000.0</td>\n",
              "      <td>2326.75</td>\n",
              "      <td>19052.0</td>\n",
              "      <td>54506.00</td>\n",
              "      <td>891586.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT5</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>40311.400967</td>\n",
              "      <td>60797.155770</td>\n",
              "      <td>-81334.0</td>\n",
              "      <td>1763.00</td>\n",
              "      <td>18104.5</td>\n",
              "      <td>50190.50</td>\n",
              "      <td>927171.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT6</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>38871.760400</td>\n",
              "      <td>59554.107537</td>\n",
              "      <td>-339603.0</td>\n",
              "      <td>1256.00</td>\n",
              "      <td>17071.0</td>\n",
              "      <td>49198.25</td>\n",
              "      <td>961664.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT1</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>5663.580500</td>\n",
              "      <td>16563.280354</td>\n",
              "      <td>0.0</td>\n",
              "      <td>1000.00</td>\n",
              "      <td>2100.0</td>\n",
              "      <td>5006.00</td>\n",
              "      <td>873552.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT2</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>5921.163500</td>\n",
              "      <td>23040.870402</td>\n",
              "      <td>0.0</td>\n",
              "      <td>833.00</td>\n",
              "      <td>2009.0</td>\n",
              "      <td>5000.00</td>\n",
              "      <td>1684259.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT3</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>5225.681500</td>\n",
              "      <td>17606.961470</td>\n",
              "      <td>0.0</td>\n",
              "      <td>390.00</td>\n",
              "      <td>1800.0</td>\n",
              "      <td>4505.00</td>\n",
              "      <td>896040.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT4</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>4826.076867</td>\n",
              "      <td>15666.159744</td>\n",
              "      <td>0.0</td>\n",
              "      <td>296.00</td>\n",
              "      <td>1500.0</td>\n",
              "      <td>4013.25</td>\n",
              "      <td>621000.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT5</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>4799.387633</td>\n",
              "      <td>15278.305679</td>\n",
              "      <td>0.0</td>\n",
              "      <td>252.50</td>\n",
              "      <td>1500.0</td>\n",
              "      <td>4031.50</td>\n",
              "      <td>426529.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT6</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>5215.502567</td>\n",
              "      <td>17777.465775</td>\n",
              "      <td>0.0</td>\n",
              "      <td>117.75</td>\n",
              "      <td>1500.0</td>\n",
              "      <td>4000.00</td>\n",
              "      <td>528666.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>default payment next month</th>\n",
              "      <td>30000.0</td>\n",
              "      <td>0.221200</td>\n",
              "      <td>0.415062</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>0.0</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                              count           mean            std       min  \\\n",
              "ID                          30000.0   15000.500000    8660.398374       1.0   \n",
              "LIMIT_BAL                   30000.0  167484.322667  129747.661567   10000.0   \n",
              "SEX                         30000.0       1.603733       0.489129       1.0   \n",
              "EDUCATION                   30000.0       1.853133       0.790349       0.0   \n",
              "MARRIAGE                    30000.0       1.551867       0.521970       0.0   \n",
              "AGE                         30000.0      35.485500       9.217904      21.0   \n",
              "PAY_0                       30000.0      -0.016700       1.123802      -2.0   \n",
              "PAY_2                       30000.0      -0.133767       1.197186      -2.0   \n",
              "PAY_3                       30000.0      -0.166200       1.196868      -2.0   \n",
              "PAY_4                       30000.0      -0.220667       1.169139      -2.0   \n",
              "PAY_5                       30000.0      -0.266200       1.133187      -2.0   \n",
              "PAY_6                       30000.0      -0.291100       1.149988      -2.0   \n",
              "BILL_AMT1                   30000.0   51223.330900   73635.860576 -165580.0   \n",
              "BILL_AMT2                   30000.0   49179.075167   71173.768783  -69777.0   \n",
              "BILL_AMT3                   30000.0   47013.154800   69349.387427 -157264.0   \n",
              "BILL_AMT4                   30000.0   43262.948967   64332.856134 -170000.0   \n",
              "BILL_AMT5                   30000.0   40311.400967   60797.155770  -81334.0   \n",
              "BILL_AMT6                   30000.0   38871.760400   59554.107537 -339603.0   \n",
              "PAY_AMT1                    30000.0    5663.580500   16563.280354       0.0   \n",
              "PAY_AMT2                    30000.0    5921.163500   23040.870402       0.0   \n",
              "PAY_AMT3                    30000.0    5225.681500   17606.961470       0.0   \n",
              "PAY_AMT4                    30000.0    4826.076867   15666.159744       0.0   \n",
              "PAY_AMT5                    30000.0    4799.387633   15278.305679       0.0   \n",
              "PAY_AMT6                    30000.0    5215.502567   17777.465775       0.0   \n",
              "default payment next month  30000.0       0.221200       0.415062       0.0   \n",
              "\n",
              "                                 25%       50%        75%        max  \n",
              "ID                           7500.75   15000.5   22500.25    30000.0  \n",
              "LIMIT_BAL                   50000.00  140000.0  240000.00  1000000.0  \n",
              "SEX                             1.00       2.0       2.00        2.0  \n",
              "EDUCATION                       1.00       2.0       2.00        6.0  \n",
              "MARRIAGE                        1.00       2.0       2.00        3.0  \n",
              "AGE                            28.00      34.0      41.00       79.0  \n",
              "PAY_0                          -1.00       0.0       0.00        8.0  \n",
              "PAY_2                          -1.00       0.0       0.00        8.0  \n",
              "PAY_3                          -1.00       0.0       0.00        8.0  \n",
              "PAY_4                          -1.00       0.0       0.00        8.0  \n",
              "PAY_5                          -1.00       0.0       0.00        8.0  \n",
              "PAY_6                          -1.00       0.0       0.00        8.0  \n",
              "BILL_AMT1                    3558.75   22381.5   67091.00   964511.0  \n",
              "BILL_AMT2                    2984.75   21200.0   64006.25   983931.0  \n",
              "BILL_AMT3                    2666.25   20088.5   60164.75  1664089.0  \n",
              "BILL_AMT4                    2326.75   19052.0   54506.00   891586.0  \n",
              "BILL_AMT5                    1763.00   18104.5   50190.50   927171.0  \n",
              "BILL_AMT6                    1256.00   17071.0   49198.25   961664.0  \n",
              "PAY_AMT1                     1000.00    2100.0    5006.00   873552.0  \n",
              "PAY_AMT2                      833.00    2009.0    5000.00  1684259.0  \n",
              "PAY_AMT3                      390.00    1800.0    4505.00   896040.0  \n",
              "PAY_AMT4                      296.00    1500.0    4013.25   621000.0  \n",
              "PAY_AMT5                      252.50    1500.0    4031.50   426529.0  \n",
              "PAY_AMT6                      117.75    1500.0    4000.00   528666.0  \n",
              "default payment next month      0.00       0.0       0.00        1.0  "
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 107
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "fSddq_ksVuAa",
        "colab_type": "code",
        "outputId": "3c770c48-a59e-44ee-d834-6a57b136bbdd",
        "colab": {}
      },
      "source": [
        "print('shape of the dataset: {}'.format(data1.shape))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "shape of the dataset: (30000, 25)\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ulPnrER_VuAf",
        "colab_type": "text"
      },
      "source": [
        "# 2. Exploratory Data Analysis"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hymn0XVjVuAi",
        "colab_type": "text"
      },
      "source": [
        "## 2.1 Data Information"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "SMDZnXJpVuAk",
        "colab_type": "code",
        "outputId": "802693e9-e9df-46aa-eb43-4e66f18011b2",
        "colab": {}
      },
      "source": [
        "data1.info()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 30000 entries, 0 to 29999\n",
            "Data columns (total 25 columns):\n",
            "ID                            30000 non-null int64\n",
            "LIMIT_BAL                     30000 non-null int64\n",
            "SEX                           30000 non-null int64\n",
            "EDUCATION                     30000 non-null int64\n",
            "MARRIAGE                      30000 non-null int64\n",
            "AGE                           30000 non-null int64\n",
            "PAY_0                         30000 non-null int64\n",
            "PAY_2                         30000 non-null int64\n",
            "PAY_3                         30000 non-null int64\n",
            "PAY_4                         30000 non-null int64\n",
            "PAY_5                         30000 non-null int64\n",
            "PAY_6                         30000 non-null int64\n",
            "BILL_AMT1                     30000 non-null int64\n",
            "BILL_AMT2                     30000 non-null int64\n",
            "BILL_AMT3                     30000 non-null int64\n",
            "BILL_AMT4                     30000 non-null int64\n",
            "BILL_AMT5                     30000 non-null int64\n",
            "BILL_AMT6                     30000 non-null int64\n",
            "PAY_AMT1                      30000 non-null int64\n",
            "PAY_AMT2                      30000 non-null int64\n",
            "PAY_AMT3                      30000 non-null int64\n",
            "PAY_AMT4                      30000 non-null int64\n",
            "PAY_AMT5                      30000 non-null int64\n",
            "PAY_AMT6                      30000 non-null int64\n",
            "default payment next month    30000 non-null int64\n",
            "dtypes: int64(25)\n",
            "memory usage: 5.7 MB\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2Bt9qmSsVuAn",
        "colab_type": "code",
        "outputId": "21d3a71b-df7d-464a-e2f0-2a57927a7540",
        "colab": {}
      },
      "source": [
        "data1['SEX'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2    18112\n",
              "1    11888\n",
              "Name: SEX, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 110
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7XdLyGckVuAp",
        "colab_type": "code",
        "outputId": "606d032b-4e80-4dc2-8cfd-43594fbe52e4",
        "colab": {}
      },
      "source": [
        "data1['EDUCATION'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2    14030\n",
              "1    10585\n",
              "3     4917\n",
              "5      280\n",
              "4      123\n",
              "6       51\n",
              "0       14\n",
              "Name: EDUCATION, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 111
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mr9pTBOrVuAu",
        "colab_type": "code",
        "outputId": "11237b1d-abec-41da-9e35-22ec0a453a62",
        "colab": {}
      },
      "source": [
        "data1['MARRIAGE'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2    15964\n",
              "1    13659\n",
              "3      323\n",
              "0       54\n",
              "Name: MARRIAGE, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 112
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kicox251VuAx",
        "colab_type": "code",
        "outputId": "1025117d-094f-41c3-ae5a-5a7bef7a7478",
        "colab": {}
      },
      "source": [
        "data1['default payment next month'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    23364\n",
              "1     6636\n",
              "Name: default payment next month, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 113
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PDljCn62VuA0",
        "colab_type": "code",
        "outputId": "6240e405-1426-4530-a6dc-db723474243f",
        "colab": {}
      },
      "source": [
        "data1['PAY_0'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              " 0    14737\n",
              "-1     5686\n",
              " 1     3688\n",
              "-2     2759\n",
              " 2     2667\n",
              " 3      322\n",
              " 4       76\n",
              " 5       26\n",
              " 8       19\n",
              " 6       11\n",
              " 7        9\n",
              "Name: PAY_0, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 114
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CkbnfU2KVuA3",
        "colab_type": "code",
        "outputId": "ca6a7309-5087-43b3-e3a5-0de41eacbad6",
        "colab": {}
      },
      "source": [
        "data['PAY_2'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              " 0    15730\n",
              "-1     6050\n",
              " 2     3927\n",
              "-2     3782\n",
              " 3      326\n",
              " 4       99\n",
              " 1       28\n",
              " 5       25\n",
              " 7       20\n",
              " 6       12\n",
              " 8        1\n",
              "Name: PAY_2, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hrp0MJoUVuA6",
        "colab_type": "code",
        "outputId": "570c7206-c413-43be-d4fa-53374dd6f4b7",
        "colab": {}
      },
      "source": [
        "data1['PAY_3'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              " 0    15764\n",
              "-1     5938\n",
              "-2     4085\n",
              " 2     3819\n",
              " 3      240\n",
              " 4       76\n",
              " 7       27\n",
              " 6       23\n",
              " 5       21\n",
              " 1        4\n",
              " 8        3\n",
              "Name: PAY_3, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 115
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JlrVJR6fVuBD",
        "colab_type": "code",
        "outputId": "032292c3-a64a-49f7-80ab-a32b74719f4c",
        "colab": {}
      },
      "source": [
        "data1['PAY_4'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              " 0    16455\n",
              "-1     5687\n",
              "-2     4348\n",
              " 2     3159\n",
              " 3      180\n",
              " 4       69\n",
              " 7       58\n",
              " 5       35\n",
              " 6        5\n",
              " 8        2\n",
              " 1        2\n",
              "Name: PAY_4, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 116
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sztLxd9sVuBJ",
        "colab_type": "code",
        "outputId": "db574109-e74e-4522-d09e-82160347f540",
        "colab": {}
      },
      "source": [
        "data1['PAY_5'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              " 0    16947\n",
              "-1     5539\n",
              "-2     4546\n",
              " 2     2626\n",
              " 3      178\n",
              " 4       84\n",
              " 7       58\n",
              " 5       17\n",
              " 6        4\n",
              " 8        1\n",
              "Name: PAY_5, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 117
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "blgvwsC7VuBO",
        "colab_type": "text"
      },
      "source": [
        " In EDUCATION variable, we discover unexpected values 5,6, and 0, when the data description only provides value 1,2,3 and 4. In MARRIAGE variable, an unexpected variable 0 takes place. Also in PAY_n variables, we have unexpected values -2, and 0.  \n",
        " For EDUCATION, we decide to combine 5,6,0 values into 4, which stands for 'others'. The same way we deal with MARRIAGE, which is to combine 0 into 3.   \n",
        " However for PAY_n, we need to take a closer look at what value -2 and 0 stand for."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "LB3yFIlxVuBU",
        "colab_type": "text"
      },
      "source": [
        "## 2.2 Graph"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "27D7CGVAVuBV",
        "colab_type": "code",
        "outputId": "66d08e13-1442-4bbb-f4ec-c640a7a6409a",
        "colab": {}
      },
      "source": [
        "corrdata=data1[['LIMIT_BAL','SEX','EDUCATION','MARRIAGE','AGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6','default payment next month']]\n",
        "corr = corrdata.corr()\n",
        "plt.figure(figsize=(15,8))\n",
        "sns.heatmap(corr, annot=True, annot_kws={\"size\": 15})"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Figure size 1080x576 with 0 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 118
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x1a26573160>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 118
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1080x576 with 2 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "McZIDVHMwkKd",
        "colab_type": "text"
      },
      "source": [
        "After plotting the correlation chart for all variables, we found that LIMIT_BAL, SEX, EDU, AGE and MARRIAGE are not highly correlated to each. PAY_0, PAY_2, PAY_3, PAY-4, PAY_5, PAY_6 are correlated much higher degree than other variables. In this way, we can have a brief thought is that those people who can pay the bill on time will highly possbile to pay next bill one time. The probability of their late payment is mianly based on their previous behaviors instead of their characterics.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tt4ecoF6VuCR",
        "colab_type": "code",
        "outputId": "08bd7524-7bec-4ade-88b3-a399dbf67b08",
        "colab": {}
      },
      "source": [
        "sns.pairplot(data1, hue = 'default payment next month', vars = ['AGE', 'MARRIAGE', 'SEX', 'EDUCATION', 'LIMIT_BAL'] )"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.PairGrid at 0x1a2d011dd8>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 129
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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tZ4PUP3bMdOFXq8Xjz76KL7whS/gxInMP6233norXnjhBTz66KMYGhrCLbfcUlGb6XQasrx+ud10UroWslzecUql0mWX3U61Fme54zWr1uJvVJlwS/PNuLvrNkTjEnRqDYLBzGd4ayVOi2iBpcmCD3bdjqAUyXzOOFBbMa5Ua32cVc5YrbdjXW212nfVVC99vB3n1kaNHrfaDuCu7psRTUiZeyRENn5sqn2sTUotbrUdwJ2dBxGXE5l7JEjJDbe3WjWOoUYUcUuvFbf12SCnUpl7JCRTG45RFATs72jADXub1tx3qJ7Gq0W0wGax4v7r7sZiZAlKhRIqQYmgFIVJo0MwKkGrVEOSkrn8tpb271rthnNrIbt1v2nz7ZjJhG9/+9sIBAJ48skn8eSTTwIA/vAP/xDf+c538Pzzz0OhUOAb3/jG9gZJROuKRBJobjZjfj603aEUFQ4nYG1uqukYdwoe652PfVxcZgJBKOtmi+Wo9rHOTCAIZd9scTtkJxCq9bWNqVQaKqW4I95ISsVEROXU8lcGi8s34RQQTSS2OzQiqhM7ZjLhy1/+Mr785S+vWf7d7353G6KhQh5/4QsVlf/rezj5Q0REREREVIt2zGQC1T5+lSQREREREdHOUP93VCEiIiIiIiKiLcUrE6hm8WMRREREREREtYmTCVSzKv1YxOPg5AMREREREdFWENLpdP3fjpaIiIiIiIiItgzvmUBEREREREREFeFkAhERERERERFVhJMJRERERERERFQRTiYQERERERERUUU4mUBEREREREREFeFkAhERERERERFVhJMJRERERERERFQRTiYQERERERERUUU4mUBEREREREREFeFkAhERERERERFVhJMJRERERERERFQRTiYQERERERERUUU4mUBEREREREREFeFkAhERERERERFVhJMJRERERERERFQRTiYQERERERERUUU4mUBEREREREREFeFkAhERERERERFVhJMJRERERERERFQRTiYQERERERERUUU4mUBEREREREREFVFudwC1zOsNllwvCAIsFgP8/jDS6fQWRVU5xlld5cbZ0mLawqjWH69ZtX6caz0+oPZjrDS+Wh2rQO0f62rbbfsL7JzxWg99V+sx1np8wM4Yr/VwnKttN+4zUPvjleofr0y4BgpF5o9UUeNHkXFWV73EWUytx1/r8QG1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F1/EP/3TP+Hv/u7vtjEqIiIiIiIiot2j7iYTACAQCOCpp57Cj370IywuLuKRRx7Z7pCIiIiIiIiIdo26mkwYGxvDP4+gkAUAACAASURBVPzDP+D555/Hvn37EAqF8NJLL8FoNG53aERERERERES7Rt1MJjz88MPw+/346Ec/iqeffhr79u3DPffcw4kEIiIiIiIioi1WN5MJkiTBbDYDuPp9rIIgbGdIRFQl0TMVfr3rPZsTBxERERERladuJhOeeeYZXLhwAT/5yU/wqU99Cnv27EEoFMLS0hIaGhq2OzwiIiIiIiKiXUOx3QFU4sCBA/jKV76CV155BY888gj27t2L48eP40/+5E+2OzQiIiIiIiKiXaOuJhOydDodPvGJT+DHP/4xfvKTn0Cj0Wx3SERERERERES7Rt18zGF8fLzgcoVCgU996lNbHA0RERERERHR7lU3kwmPPfZY0XWCIODkyZNbGA0RERERERHR7lU3kwkvvPDCdodARERERERERKizeyaEw2EkEom8ZZIk4Vvf+tY2RURERERERES0+9TNZMK//Mu/4LbbbsOxY8cwMjICAHjuuedw33334fnnn9/m6IiIiIiIiIh2j7r5mMP3vvc9/OQnP8GVK1fwve99D2azGc899xwef/xx/OZv/uZ2h0dERERERES0a9TNZIJarcbAwAAGBgbwla98BQMDA3j++edhtVq3OzQiIiIiIiKiXaVuJhNEUcz9bjAY8Fd/9VfQ6XTbGBERERERERHR7lQ390wQBCH3u8lk4kQCERERERER0TapmysT3G43vvGNb6z5PesLX/jCdoRFREREREREtOvUzWTCI488UvB3IiIiIiIiItpadTOZ8Hu/93tF1zmdzq0LhIiIiIiIiGiXq5t7Jly5cgVPPPEEvvrVryISiQAAQqEQvv71r+OBBx7Y5uiIiIiIiIiIdo+6mUz44he/iObmZni9Xnz3u9/F66+/jvvvvx9nzpzB3//93293eERERERERES7Rt18zMHn8+GP//iPIUkSHnzwQTzzzDN4/PHH8elPfzrvmx6IiIiIiIiIaHPVzWRC9qsgNRoNIpEIvvOd72BwcHCboyIiIiIiIiLafermYw4rrz5obm7mRAIRERERERHRNqmbKxMkScLExATS6TQSiUTu96ze3t5tjI6IiIiIiIho96ibyYRYLIbP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ZRkSJMhKAqIICBAgJ4BEPAEg+XOU1HKCICzaNXK0WhFmiwEBfxixWGLB+VlMoEKVVDEhJRaL4YUXXsAzzzyDwcFBXHvttbj99tuLvp58iwlqT/oYZ3HlG6caEwhAndtZjV/c1RhTvlZSMUGN43Uxrbb+AitnvJbCvlN7jGqPD1gZ47UUtnOxrcY+A+ofr1T6SuaaCTNptVq84x3vwPbtyd9BPfnkk8scEREREREREdHqUTK3hgQAv9+P3/72t3j22WfR3d2Na6+9Fg888AC2bt263KERERERERERrRolU0z44he/iDfffBNXXXUVPvOZz2D79u0QklcCJCIiIiIiIqIlVDLFhN/97ncwm83Yv38/nnvuufTrqYvivfLKK8sYHREREREREdHqUTLFhH379i13CERERERERESEEiomrFmzZrlDICIiIiIiIiKU6N0ciIiIiIiIiGj5sJhARERERERERAVhMYGIiIiIiIiICsJiAhEREREREREVhMUEIiIiIiIiIioIiwlEREREREREVBAWE4iIiIiIiIioICwmEBEREREREVFBWEwgIiIiIiIiooKwmEBEREREREREBWExgYiIiIiIiIgKwmICERERERERERWExQQiIiIiIiIiKgiLCURERERERERUEBYTiIiIiIiIiKggLCYQERERERERUUFYTCAiIiIiIiKigrCYQEREREREREQFYTGBiIiIiIiIiArCYgIRERERERERFYTFBCIiIiIiIiIqCIsJRERERERERFQQFhOIiIiIiIiIqCAsJhARERERERFRQVhMWASiKAACoNNJgABoNMnNrNNJgKTAYNACkpKeLorCvGWMRh0gIDlvqo0Z0/V6zay/ZnNyfpNJN69NrVZCMBKDXp9cr16vAUQlOT0Vr6ik15X6Ozf+VHuiKKTjSa0/0zwzn6fmT71ORJQPs1mLsWkvzGbtcodCi8Rs1mLMO819nMGsz/oiMBi0mPD6k5/zRVBWpgN08eRfKjkarQRBFNJ5n8Xydi6p00nQGURo9VroTRIkjQi9XgONXoBGJ0Gv10AQBYiSAJ1OgqBJ5pGCJpnfmkw6CJIAg1EHjVaEpBEhzMgfZ+aDoihAo50xfY65uSURqUdxPp0IABCTE+gZ8eFU/xREjYABlw/DYwFc1FaJhpYoRkL9MGh1GJgegcs/ijpLLdort0ATssHr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+jPNk25bUdLxp14vZHuqDYsJxafGL+5qjClfak8e8h2rAFBWpoMvEoFVr4fXm/k2YSuJGt+fiy25j8Ow6g157WO1jtfF2Hd6vQZROQ6dpEEksvDdGxZiNusQiceh12gQCJz/+ym574Kw6k1FeX+WwvhfCcfXVB+8vhCicRl6jQaRaAxmkw6BcDKXjMdlCBKQUERIYgKxmAKNKCIBGQpESBAQjcsQgWSOl4hDq9EhKkehETTQaCSE4zHoJC3keBwJJE+1lwRhXj4oigIkSUBcUSBBQDyemBXv3NzyXJTC2FoMah+vVPpW/AUYl0PqQBeNygCAeCIx47mAcDwGQEBUTk6fWc9JLRMKJT+Uk/MifWBNTU8lFam/qaQgGI/OazMWk2G1GjER8EORBUTicQACFLz9OypASN8WKrXOufGn+qUob/8GK7X+TPPMfJ6Kn7UrIipEIBCDrapsRV5skZKS+7ic+ziD9Gd9/PwLCQAQDsfSXyyKIVlA0MAbWfmFvpUoHpOhyEo67/P7Z+eSSTJi6X8l0v+Kp/8FyHIyv5VT+S3kdA4ZxuyxEcfsPBFI5orpfBHz88S5uSURqceKv2YCERERERERERUXiwlEREREREREVBD+zIGIqAT8v/13FTT/L27510WKhIiIiIiIxQQiopIQ+v11hS1wy+LEQUREREQEsJhAtCp98I7/LGh+Nd2pgIiIiIiIlh9vDUlEREREREREBeEFGImIiIiIiIioICwmEBEREREREVFBWEwgIiIiIiIiooKwmEBEREREREREBWExgYiIiIiIiIgKwmICERERERERERWExQQiIiIiIiIiKgiLCURERERERERUEBYTiIiIiIiIiKggLCYQERERERERUUFYTCAiIiIiIiKigrCYQEREREREREQFYTGBiIiIiIiIiArCYgIRERERERERFYTFBCIiIiIiIiIqCIsJRERERERERFQQFhOIiIiIiIiIqCAsJhARERERERFRQVhMICIiIiIiIqKCsJhARERERERERAVhMYGIiIiIiIiICqJZ7gDUzOPx5ZwuCAKqq80YHw9AUZQliqpwjLO48o3TbrcuYVQLj9cUtW9ntccHqD/GQuNT61gF1L+ti2219RdYOeO1FPad2mNUe3zAyhivpbCdi2019hlQ/3il0sczE86DKCbfpKLKtyLjLK5SiTMbtcev9vgA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4lJbnPmO1xS1xT+X2uMD1B+jWuMrdKwC6u3LYllt/QXU2+eVdmwF1B+j2uMD1BtjIeNVrX1YTKuxz8Dq7TctvpK/AONcfX19uOOOOwAA999/P37wgx/gk5/8JP76r/8a3/zmN5c5OiIiIiIiIqLSt2LOTEhdL6GxsREPPfQQAKClpQWPPfbYcoZFREREREREtOKsuDMTiIiIiIiIiGhxsZhARERERERERAVhMYGIiIiIiIiICsJiAhEREREREREVhMUEIiIiIiIiIioIiwlEREREREREVBAWE4iIiIiIiIioICwmEBEREREREVFBWEwgIiIiIiIiooKwmEBEREREREREBWExgYiIiIiIiIgKwmICERERERERERWExQQiIiIiIiIiKgiLCURERERERERUEM1yB0BERJTLR3/+hYLm//6uby1SJERERESUwjMTiIiIiIiIiKggLCYQERERERERUUFYTCAiIiIiIiKigqyIYkJvby+uueaaea+Hw2Hce++9uPXWW/GRj3wEL7744jJER0RERERERLSylPwFGPfs2YMnn3wSk5OT86b9+Mc/Rl1dHb7xjW9gYGAAzz//PK688sq82xYEAWKOcosoCrP+qhXjLC61xrnQeE1Ra/wpao8PUH+Mao8v37EKnFsfJEmd/c6H2vfdYlJrn1fKsRVQf4xqjw9Qf4z5jFe192ExrMY+A6u337R0Sr6YYLPZsHfvXuzYsWPetBdffBHve9/78NnPfhaSJOGrX/1qQW1XV5shCAu/+SoqzAW1u1wYZ3GpLc58x2uK2uKfS+3xAeqPUa3xFTpWC1VVZVm0tpeKWvfdYlJrn1fasRVQf4xqjw9Qb4yFjFe19mExrcY+A6u337T4Sr6Y8N73vjfrtImJCQwNDeGRRx7BgQMHcM899+CnP/1p3m2PjwcWPDOhosKMqakAEgmlkLCXFOMsrnzjXOovNAuN1xS1b2e1xweoP8ZC41PrWAXO7X9TJib8BS+jFmofW4up1MdrKew7tceo9viAlXF8LYXtXGyrsc+A+scrlb6SLybkUlFRgfe85z0AgJ07d+LOO+8saHlFUSDLC8+XSCiQZfUfmBhncaktznzHa4ra4p9L7fEB6o9RrfEVOlYLpcY+F0qt+24xqbXPK+3YCqg/RrXHB6g3xkLGq1r7sJhWY5+B1dtvWnwr4gKM2Vx66aU4cOAAAKCzsxNr165d5oiIiIiIiIiISp8qiglPP/10xtej0SgeeOCBgtrq6+vDHXfcAQD43Oc+h6GhIdxyyy3YvXs3du/efd6xEhEREREREa12qviZw09+8hO88cYbuPfee6HVagEAPT09+Ku/+ivY7fa82jh48CAAoLGxEQ899BAAwGq14p//+Z8XJ2giIiIiIiKiVUoVZybs3bsX0WgUt956K4aHh/GLX/wCt9xyCz74wQ/ixz/+8XKHR0REREREREQzqOLMBJ1Oh927d+OJJ57Addddh/Lycjz66KPYunXrcodGRERERERERHOo4swEADhy5AgeffRRXHPNNTCbzXjmmWcQi8WWOywiIiIiIiIimkMVxYQf//jH+OxnP4s///M/x0MPPYQnn3wSo6OjuOWWW9Df37/c4RERERERERHRDKooJjz77LP4+c9/jhtvvBEAYDab8S//8i/40Ic+hJtvvnmZoyMiIiIiIiKimVRRTHjiiSfQ1NQ07/VPfepTePjhh5c+ICIiIiIiIlrQ4OAgbrvttqzT4/E4brvtNnz84x9HNBrNu93bbrsNg4ODGBoawoEDB4oR6qKYmprCf/3XfxW93b179xa9zZm6urpw6NAhAMCuXbvOqQ1VFBN+8YtfpP996tSpWdOefvrppQ6HiIiIiIiIimB0dBSxWAx79+6FTqcrePnXXnsNhw8fXoTIiuPEiRN44YUXit7uI488UvQ2Z/rtb3+L3t7e82pDFXdzePLJJ/HJT34SAHDXXXfhqaeeSk9LVUuIiIiIiIho+fn9ftxxxx0IBAJwOBzp11955RV897vfhSiK2LBhAx544AF8/etfR3d3N3bv3o2bbroJ//iP/4hEIoFgMIgHH3wQY2NjeOqpp/Dggw8CSP4v+f79+9NtPvzww4hGo+jo6MBVV12Vfv29730vWltbMTAwgO3bt+Ouu+5CV1fXvPZ/9atfYe3atbj55psxODiIv/3bv8X111+P559/HsFgEBMTE7j11lvx29/+FkNDQ/jud7+LlpYWfOtb38Ibb7yBRCKBL3zhC3jXu96F2267Da2trejq6kIikcAPfvADPPzww+jq6sJ//Md/4CMf+Ug6vhtvvBEXXXQRurq6UF5eju9973sIBAK47777MD09DVEU8fd///eQJAmf+cxn8MQTT+CVV17Bb37zG2zevBkejwe7d+/Gfffdl27zK1/5CnQ6Hfr7+6HX63HxxRfjpZdeQjwex6OPPopwOIw777wTwWAQAHDfffehvb0d733ve9HR0YGenh60tbXhS1/6Ep566inodDq0tbUBAO6991709vbCYrHge9/7Xl6FH1WcmaAoSsZ/Z3pOREREREREy+fnP/85LrzwQvz0pz/F+973PgDJ721f+9rX8P3vfx979uyBJEn4zW9+g3vvvRdtbW2477770N3djfvvvx+PPfYY3v/+9+N///d/F1zX7bffjg9/+MOzCgkA4HK58JWvfAVPPvkk3nrrLRw5ciRj+zfddFP6bPdf/epX+PCHPwwAiEajeOSRR3DDDTfg5ZdfxsMPP4ybbroJ+/btw4EDB+DxePCzn/0Mjz76KB566KH0TzQuu+wyPP7442hqasJLL72E22+/HVdeeeWsQgIAeL1efPSjH8XPfvYzhMNhvPXWW/jRj36EnTt34vHHH8fdd9+N3bt3o76+Hl/84hfxla98Bf/2b/+Gr3/967j99ttht9tnFRJSmpub8e///u+QJAkWiwWPPfYYrFYrjh8/jn/913/FNddcgz179uBrX/sa7r//fgDA0NAQ7r77bvzyl7/E66+/DgD48Ic/jNtvvz1dTLj11luxd+9eyLKM48eP5zUOVHFmwkyCIOR8TkRERERERMunt7cX1157LQBg27ZteOyxxzAxMQGPx4MvfelLAIBgMAiHw4EtW7akl3M6nfjud78LvV6PsbExXHjhhbPaLeQ/khsaGlBbWwsA2Lp1K/r6+jK239TUBEVRMDAwgOeeew579+7Fs88+i/b2dgBAWVkZ1q1bBwCwWq1wuVw4efIkDh8+nL4WRDweh9vtBgBs3Lgx3ZdIJJIzxtbW1lnznjp1Cq+//nq6uBEOhwEA119/Pf7pn/4JN910E8rKynK2mfryPzNui8WCSCSCnp6e9A0M1q9fj4mJCQCA3W5HdXU1AKCmpiZj3Js3b07Pm4prIaooJrBgQEREREREVBqam5vx5ptv4sorr8TRo0cBAJWVlairq8MPf/hDmM1m/Pd///esn0AAwO7du/G9730Pa9aswQMPPABFUaDX69Nf1FNtzSSKIhKJxLzXh4aGMDExgcrKShw+fBgf+MAHcM8998xrHwA+8pGP4Dvf+Q62bt0KvV4PIPd30HXr1uHKK6/EV7/6VcTjcXz/+99HTU1NxuWyxZdp3nXr1uEd73gHrr32WrhcrvSFG3/4wx/iAx/4APbt24f3v//9aG5uzlpYWSjuQ4cOoaWlBd3d3bBarVmXEQRhVtzn8p1cFcWEwcHBdAVr5r8VRcHQ0NByhkZERMss9PvrClvg3C5ITERERHm69dZb8Td/8zf4xCc+gcbGRgDJL9V33XUX/uzP/gyyLKOyshLf+ta34PV608tdf/31+NM//VNUVlbCZrNBURRs3rwZer0eH/vYx7Bx40ZUVFTMWteGDRvwwx/+EJs2bcJ73vOe9Os6nQ73338/XC4Xrr76arS2tmZsHwCuu+46fP3rX8dPfvKTvPq3a9cuvPbaa/jEJz4Bv9+PG2+8MV2EmGvt2rV466238MQTT+BjH/tYznY///nP47777sPjjz+OQCCAO++8E4cPH8bzzz+PvXv3YteuXbj77ruxZ88e1NfX4/7778c//MM/5BVzqv177rkHv/rVrxCLxXIuu2nTJnz729/G+vXr825/LkFRwUUJZl5wMWVychLl5eUQRTH9u5al5vH4ck6XJAFVVRZMTPghy8u+GbNinMWVb5x2u3UJo1p4vKaofTurPT5A/TEWGp9axyqQ7Mundu8rqP1Hv1K61QS1j618/emD+xeeaYZnHvpQyY/XUth3ao9R7fEBK+P4WgrbudhWY58B9Y/X8zX3Qo25+Hw+fP7zn8eePXsWOarVRRUXYNy1axdefPFFrFmzBjfeeCP279+P73znO/jBD36Ajo6O5Q6PiIiIiIiIStDBgwfx8Y9/HJ/73OeWO5QVRxU/c/jmN7+JNWvWoK2tDb/73e/Q2dmJF154Ab29vXjwwQfx8MMPL3eIREREREREpBL5npVw8cUX45lnnlnkaFYnVRQTjh49mt7BL774Iq699lpUVVWhqqqK10wgIiIiIiIiUhlV/MxBFN8O4w9/+AO2b9+efp66nycRERERERER/X/27jy4jfS+G/y30Qdu8ACIgyIFUtTooA7OaKSxNCMPxyM7k6xjr51687per5NstuKkKlvriu14s5mUk8q6tpJKyqlUatepVKVyVc1sKlnndRx782btGVtjeUZjjWeGOihqREqgeODmgftqYP+AABEkABIUjwb5/VShQPTz9INfdz/d+OFho1sbNDGYYLFYcO/ePdy8eRMzMzPVwYTr169X74fZ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\n",
            "text/plain": [
              "<Figure size 1029.19x900 with 30 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UlfF8HzpVuBa",
        "colab_type": "code",
        "outputId": "67645024-7f03-47f4-c859-b2bd861ddf00",
        "colab": {}
      },
      "source": [
        "sns.jointplot(x='EDUCATION',y='LIMIT_BAL', data = data1)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.JointGrid at 0x1a2653c588>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 119
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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KTC3GdOjcxRMkaGyfh0N5H6+21JX50JdXf1IyKOPzoXFcgEzZtyNhIROePjhBXjxxefwzjtvoarKhrvvvg+hoREYPnwkHnjgnl/v18XDarXA6XTB5ULjOejXrz8eemg2DAYDwsPDMXLkaIwePRZr1jyDBx98ANXVVZgxIx2dO3eDywXU1dX/bF2d69f3ff3zOJ2tn1dvznefPv0xZsxYzJ59P+rqnEhPvx8GQzQKCk7jrbf+ihUrnsWLL74Ap7MOa9bUX1Hp9aFYsmQ53nzzNfTr1x+PPz4fADBw4CA8+OAjrd7Ta+s8Ns3Tm7wvPaevv74BQ4b8BkOHjkBxcTHuuWcmgoKCcPvtU9GpU1fceusdePHF1XjoodmwWq0YNWo0oqKMzf6+rl2TMGDAlZg9+14EBQWjZ89euO22qXj55XW4cOECMjM3ITNzEwBg0aKluPPOGVi3bg0uXnwDTqcTy5ZlwOXS+Py93p7POqXRuDq4o+LQoUPx/fffw263Y+nSpSgsLITT6URGRgauuOIKnDlzBk8++SRqa2thMBiwbt06REdHY+/evXj55Zfhcrnwm9/8BkuXLoVGo8Hrr7+Ozz77DHV1dbjnnnswZcoUr59b1OU0VtTpNDCZDL9+U5b3h3BrszcbxETqFTF7U0nnu6mmee/c+TGOH/83/vCHhf5OyyO5nO8PP9yMa6+9Dt26/We48+9/39nmeZRL3t5qT95sItu6Di96ShboRQ/4dZ3etwXIL2qyTq9zFNJGKmOdntLOdwMWvfYpLi5Cp06dmx1j0WuORa91XJyucqnJJqQmm1BuqYHdCei5I4vkJk++xd8pKM6lBQ/geSQxLHoEAIg3hinymzARkTcCaL4OERGReyx6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6RESkGix6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oaGh6NSpE3r27IlTp075O62AwKLnQ8OGDcPu3bvhcrlQUlKCkpIS9OrVy99pBaSysjKkp6djzpw5irrBv337drz00ksAgNDQUAQHB0Oj0fg5K882b96MzZs343/+538wZswYzJ8/H0OHDvV3Wh5t3boVTz/9NADAarUiNzcXffv29XNWng0fPhxff/01nE4nLBYLTp06haSkJH+nFRA4vOlDEyZMwP79+3HXXXfB4XDgqaeeUtRNfyXZsGEDLly4gHfffRfvvvsuACAjI0P2XzImTpyIJ598EjNmzIDT6cQdd9yBlJQUf6cVsO68804sXboU06dPBwA88cQTiI+P93NWnl133XU4dOgQpk2bBpfLhQULFsBoNPo7rYDAfnpERKQaHN4kIiLVYNEjIiLVYNEjIiLVYNEjIiLVYNEjIiLV4JIFUqWzZ8/ipptuarFmq3///ujevTsyMzORkJAAl8sFu92Oa6+9FosWLUJoaCj279+P559/Hn/729+a/ez48ePx2muvoV+/fgCA999/H//7v/8Lh8MBp9OJm2++GQ899BC02v9811y9ejW2bNmCPXv2ICoqCgDwl7/8pXE/zry8PHTr1g16vR5xcXF46623cPfdd+P+++/HuHHjAAD//Oc/8dprr8FisUCn0+HKK6/EY489hoSEhMa8xo4di6eeeqrx733//ffx448/Ys2aNT4+s0TyxqJHqhUZGYkdO3a0OP7qq69iypQpjXt71tbWYtGiRXj66afx3HPPCT33q6++ioMHD+LNN99ETEwMrFYrHn74YVy8eLFx95ja2lpkZWVhzJgx2LZtG+677z4AwEMPPYSHHnoIQH3BeuWVVxoL6aU++eQT/PnPf8b69evRv39/1NXV4cMPP8T06dOxffv2xkK6detWjB8/HqNHj/buJBEFGA5vEnkQEhKCpUuX4uOPPxbaS9Vms+Gtt97CM888g5iYGAD1W9Q9++yzGDZsWGPcF198gaSkJEyfPh2ZmZm4nCWzL730EpYvX964CbRWq8WMGTMwYMAAvP/++41xjz76KJYuXYqKigqv/w6iQMIrPVIti8WC2267rdmx9PT0VmMTEhIQGRkptP/hyZMnER4eju7duzc73r1792bHtmzZgrS0NFxzzTWoqanBV199heuvv144//Lycpw5cwZDhgxp8diIESPwzTffNP557NixOHv2LFauXIn169cL/x1EgYZFj1TL3fBmW/R6Pex2e6uPuVwuaLVaaLVa1NXVuf27T58+jYMHD+Kll16CVqtFWloaNm3a5FXRa9iz0+FwtHistra2xbHFixdjypQp+Pjjj4X/DqJAw+FNov/f3v2Cqg7FcQD/gnDHWFCDSRgDzSJiVUSwGUWTwSIGBUWtYpl/msEmWESwiAajLDgw2UWjFi3CgoJM8AZBnrz7eF5eenffTzyMc85O+cL5jf3ecDwecT6fIcsyHA7Hb9ec9/sdp9MJdrsdXq8X1+sV+/3+5ZnNZoNqtQrgUWOz2WxIJBKIRqOYzWbQdR273e7tPTmdTiiK8mW3g9VqBb/f/zImSRLa7TZUVcXhcHh7HaKfhKFH9BeXywWtVgvJZBKiKMLj8eB2u730lRuPx1AUBS6XC4IgIJPJoFarPWtohmFAVVW43W7cbjdMJhN0Oh1omgZN06DrOoLBIIbD4bf2VqlU0Gg0sN1uATzCdzAYYL1eP3+y/KtAIIBUKoV+v/8PJ0L0/+L1JlnWVzW9j48PhMNhTKdTLJfLZ1f2UCiEUqkE4PGxSLfbRbPZRKvVgmmakGUZ3W73OU+hUECv10M6nX7OEY/HkcvlMJ/PIUkSIpHIy9rZbBblchnFYhGiKL71DrFYDIIgoF6vwzAMmKYJn8+H0Wj0x16O+Xwei8XiGydF9HOwywIREVkGrzeJiMgyGHpERGQZDD0iIrIMhh4REVkGQ4+IiCyDoUdERJbB0CMiIstg6BERkWV8AoRqE05lTIytAAAAAElFTkSuQmCC\n",
            "text/plain": [
              "<Figure size 432x432 with 3 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IRVGkEbLVuBk",
        "colab_type": "code",
        "outputId": "b8efd693-6df7-4d17-aa12-f59b469c11c8",
        "colab": {}
      },
      "source": [
        "sns.jointplot('EDUCATION', 'PAY_TOTAL', data1, kind = 'regid')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.JointGrid at 0x1a2ce2db38>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 124
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x432 with 3 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eTa3XY3SywM4",
        "colab_type": "text"
      },
      "source": [
        "In two chart above, we can find that the higher education level, the higher LIMIT_BAL and PAY_TOTAL, meaning that clients with higher education level will have lower probability to have late payments\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8I8Cb4DvVuBf",
        "colab_type": "code",
        "outputId": "1dd135fa-5ff6-4a86-9601-072e202bc361",
        "colab": {}
      },
      "source": [
        "data1['PAY_TOTAL'] = (data1.PAY_0 + data1.PAY_2 + data1.PAY_3 + data1.PAY_4 + data1.PAY_5 + data1.PAY_6)\n",
        "data1['RISK_CAT'] = pd.cut(data1.PAY_TOTAL, [-20,-10,0,10], labels=[\"low\",\"medium\",\"high\"])\n",
        "data1['AGE_GROUP'] = pd.cut(data1.AGE, [21,40,60,81], labels=[\"young\",\"middle\",\"senior\"])\n",
        "sns.lmplot(x='AGE', y='PAY_TOTAL', data=data1, hue ='SEX')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<seaborn.axisgrid.FacetGrid at 0x1a2cee02b0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 123
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 403.315x360 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "OapzTkCZzGQA",
        "colab_type": "text"
      },
      "source": [
        "In this plot chart, we tries to present the corrleation of AGE and PAY-TOTAL by comparing different sex. Based on the trend line we have, as AGE going up, Men have higher value  for the PAY_TOTAL than Weman. For both gender, as age increases, the value of PAY_TOTAL descrases a little bit might be caused by more stable per"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s4EJV_11VuCB",
        "colab_type": "code",
        "outputId": "4dc4cf96-c6b4-4766-981e-47cc3bb6d59c",
        "colab": {}
      },
      "source": [
        "plt.figure(figsize=(15,8))\n",
        "sns.boxplot(x= 'EDUCATION', y = 'PAY_TOTAL',data=data1, hue = 'RISK_CAT')\n",
        "plt.legend(bbox_to_anchor=(1, 1), loc=2)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Figure size 1080x576 with 0 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 125
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x1a2c56cc88>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 125
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.legend.Legend at 0x1a2d7a7f98>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 125
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA8sAAAHhCAYAAABZWSzWAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvIxREBQAAIABJREFUeJzt3Xt8XHWZP/BnkkmvCaW5VUERFWgLri91UfAlCEUExSKCQlsqRUBRd4Et1gqWixdoKBa2eFkvKxdXoQW6BcriDREE8cJSXPWltIgIP5DF0iRAk0LSTDK/P1hie0ib20zOZPJ+/3UyZ86Zp3lyTucz3+85k8nn8/kAAAAAelWkXQAAAACUGmEZAAAAEoRlAAAASBCWAQAAIEFYBgAAgARhGQAAABKyaRcwXJs2taVdAgAAQGoaGmrSLqEsGVkGAACABGEZAAAAEoRlAAAASBCWAQAAIEFYBgAAgARhGQAAABKEZQAAAEgY9d+zDAAAwM51dHREV1dXQfdZVVUVEyZMKOg+S4mwDAAAUMY6OjrilFNOjfb2toLut7q6Jq655uqyDczCMgAAQBnr6uqK9va2mPz690WmclxB9pnv3hrtj3w/urq6dhqWb7rppli/fn2cd955BXndkSQsAwAAjAGZynGRqRyfdhmjhht8AQAAUFTXXXddfPCDH4x58+bF4sWLo6OjI84444y4//77IyJiwYIF8Y1vfCMiIr7yla/ELbfckma5ESEsAwAAUESPPPJI3HDDDbFq1apYtWpVNDQ0xDXXXBNHHnlk3HXXXdHe3h5btmyJX/ziFxERcc8998Thhx+ectXCMgAAAEW0cePGeNOb3hTjxr14vfQBBxwQDz/8cMyaNSt+9atfxb333hvvfe9744UXXog//vGP0dDQENXV1SlX7ZplAACAMSHfvTWVfTU0NMTvfve72Lp1a4wbNy5+/etfx5577hnV1dXxile8IlauXBnnn39+bN68OS666KKYN29eweocjlTC8mOPPRYf+9jH4ic/+Uls3bo1PvvZz8aTTz4ZmUwmPve5z8WMGTPSKAsAAKDsVFVVRXV1TbQ/8v2C7re6uiaqqqr6fd7ee+8de+65Z8yfPz8ymUzstttusXTp0oiIOPLII2PFihWxzz77xDvf+c645ppr4l3veldB6xyqTD6fz4/kC1533XWxZs2aePzxx2PdunXx3e9+N5588sn47Gc/Gxs2bIjPfe5zccMNNwx4f5s2Ffa7wgAAAEaThoaafp/T0dERXV1dBX3dqqqqsv2O5YgURpbr6+tj5cqVcdBBB0VExP333x/z58+PiIgZM2bEpk2bor29vSTmqEO5yOVy0drastP1ERHZ7I5PCbW1dTtdT3r0t3zpLQCFMmHChLIOtsUw4v97Hnnkkdv93NbWFjU1f/8kZPLkyYMKy5lMJircpgx2KJfLxZIli6K5edOw9lNf3xCXXvqv3nSXGP0tX3oLAOlK/X/O6urqaG9v7/15y5Yt24Xn/tTVTY5MJlOM0qAsdHV1RUXF8I+RiopMTJ06eUDXpTBy9Ld86S0ApGvEr1l+yf777x/r1q2L73znO/HUU0/1XrN8wQUXxOrVqwe8n+bmdiPL0I9cLhctLX1P5WxpaY5LL704IiLOOef8qKur7/N5dXWmcpYq/S1fegvAQNTWuoS1GFL/33PevHmxZMmSmDt3bnR3d8cXvvCFQW2fz+eju7tIxUGZyGQqo76+sc91PT1//7xs6tS6HT4vIqK7O5XP1uiH/pYvvQWA9KQWltetWxcREePHj4/LL788rTIAAADKnrthD17qI8sAAAAUT0dHR5xy6inR3tbe/5MHobqmOq65+pqiB+avfvWrUVNTEx/5yEfi4x//eHzrW98q6uu9RFgGAAAoY11dXdHe1h67HvHqyIwrzA2f8lt74tnbn4iurq4RHV0eqaAcISwDAACMCZlxFVExrrIg++oZ4PNuuummuOOOOyKXy8XGjRvjxBNPjF/96lfxpz/9KY4++ug4/PDD46KLLop8Ph/jxo2LL3zhC/GqV70qbrjhhli5cmXU1dVFd3d3zJo1KyL+fqPok046KZYsWRIzZ86MO+64I+64445YtmxZzJo1Kw488MB49NFHY5999ona2tp44IEHoqurK6666qqYPHnygP+NwjIAAABF89xzz8W1114b//3f/x2LFy+OO+64I1544YV43/veF3fddVecf/758cY3vjHuu+++uPjii2Pp0qXxrW99K2677baYOHFi/NM//dOAX+upp56Kj3/847HnnnvGYYcdFhdccEEsXLgwPvnJT8ZvfvObOPjggwe8L2EZAACAopk5c2ZkMpnYZZdd4jWveU2MGzcuxo0bFx0dHfHw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6adj48aN8brXvW5A2+bz+ege3rFSMjKZyqivb+xzXU9Pvnd56tS6HT4vIqK7O7/DdRTHtv2pmJSNyuo+RvZ3GZk69L+wtu1ttm5C370tku72ru3q0NvC09/yNaDzcoRz8yjl2C1v+kup6DcsNzc3F72Id73rXXHffffFnDlzIpfLxYUXXhiVlZVFf10AAADoS79heevWrfHII49EPt/3pyp77bXXsIvIZDJx3nnnDXs/AAAAUAj9huXHH388Tj/99D7DciaTiZ/+9KdFKQwAAADS0m9Y3muvveKWW24ZiVoAAACgJJTJfaQBAACgcPoNy+95z3tGog4AAAAoGf1Ow/7EJz4R3d3d8eMf/zh++9vfRkTEm970pjjiiCMimx3U1zQDAADAqNDvyHJ7e3vMmTMnrrzyyqisrIyenp648sorY86cOdHePjq+pBsAAAAGo9+h4S9/+ctx0EEHxcKFC7d7/Etf+lKsWLEiLrjggqIVBwAAAGnoNyz/+te/jptvvvlljy9atCje9773FaUoAAAASFO/07Dz+Xyf1yZXVlZGVVVVUYoCAACANPUblisrK+Nvf/vbyx5/6qmnYvz48UUpCgAAANLUb1g+6aST4uyzz44nnnii97E///nPceaZZ8ZHPvKRYtYGAAAAqej3muUPfehD0draGu9///tj0qRJkcvloqenJ84444yYPXv2SNQIAAAAI6rfsJzP5+P000+Pk08+OR5++OHIZDKx1157mYINAABA2ep3GvZxxx0XERHjx4+PN7zhDbHffvsJygAAAJS1Ad0NGwAAAMaSfqdht7e3x913373D9YccckhBCwIAAIC09RuWW1pa4qqrrupzhDmTyQjLAAAAlJ1+w/JrXvOa+O53vzsStQAAAEBJ6PeaZQAAABhr+g3LCxYs6Hcnt99+e0GKAQAAgFIw4K+O2plvfOMbBSkGAAAASkFBpmH7eikAAADKSUHCciaTKcRuAAAAoCS4wRcAAAAkCMsAAACQ4JplAAAASOg3LH/729/udyfnn39+QYoBAACAUtBvWP7Zz34WJ598cmzcuHGHz9l///0LWhQAAACkqd+wfO2118YhhxwSxx9/fPz4xz8eiZoAAAAgVdn+npDJZOLUU0+NWbNmxYUXXhjf//7341WvelXv+s985jNFLRBGm+7nc2X9egAAMBb0G5Zf8thjj8X/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BfHYY4/F1q1b40Mf+lDMmzcv7bIokJ6enrjoooviwQcfjHw+H5/61KfiwAMPTLssCmjLli0xb968OOuss+Lwww9PuxwK6Nhjj43q6uqIiKiqqoqrr7465YoopGuuuSZ++MMfRi6Xi/e85z1x+umnp10So5SwPArceeed8dRTT8Xq1atj48aNcfLJJ8dtt90W2az2lYvrrrsu1qxZE88880zapVBAa9eujWw2G6tWrYrOzs446qij4t3vfnfU19enXRoF8LOf/SyeeeaZuOGGG+KJJ56Ij33sY/GjH/0o7bIokHw+H+eff35UVlamXQoF1tHRER0dHXHzzTenXQpFsG7durjnnnti5cqVERHxla98JXK5nPfNDIlp2KPA/fffH4ceemhEREybNi0aGhrikUceSbcoCqq+vr73pE75eM973hPnnHNORERkMpno7u6OqqqqlKuiUA477LC47LLLIiLiySefjJqampQropD+9V//NWbNmhXTp09PuxQKbP369dHd3R2nnXZazJ8/P+6+++60S6KA7rnnnnjDG94QCxcujJNPPjkOOOAAQZkh85czCrS1tW33Jmzy5MnR1taWYkUU2pFHHpl2CRTB5MmTIyKis7MzFi1aFB/4wAdiypQpKVdFIWWz2bjooovipptuikWLFqVdDgWydu3a6Onpife///3xy1/+Mu1yKLCJEyfGKaecEnPmzInm5uaYP39+zJgxI6ZNm5Z2aRRAa2tr/PnPf47vfOc78eyzz8aJJ54Ya9eu9YEmQ2JkeRSorq6O9vb23p+3bNniDTeMEhs3bowFCxbEG9/4xli4cGHa5VAEF1xwQfz85z+PG2+8MdavX592ORTAjTfeGL/97W/jpJNOip///OdxxRVXxLp169IuiwJ57WtfG8cee2xUVFREY2Nj7LvvvmbslZFdd901DjrooJgwYUK84hWviNe+9rXx6KOPpl0Wo5SwPAq89a1vjbvuuivy+Xxs3LgxNm7cGK973evSLgvox6ZNm2LBggVx+umnu7lIGbrllltixYoVERExYcKEqKqqikwmk3JVFMJ1110X1113XXzve9+Lgw8+OBYuXBj7779/2mVRIKtXr44vfvGLERHR3t4eGzZsiL333jvlqiiUt73tbXHvvfdGd3d3tLW1xaOPPhp77LFH2mUxSpmGPQq8613vivvuuy/mzJkTuVwuLrzwQjccgVHg61//emzevDm+853vxHe+852IiPjCF77gw64yceSRR8Z5550X8+bNi+7u7jjuuONixowZaZcF9OOEE06IJUuWxNy5cyMiYvHixdHQ0JByVRTKO9/5zvjNb34Txx9/fOTz+Tj77LNj1113TbssRqlMPp/Pp10EAAAAlBLTsAEAACBBWAYAAIAEYRkAAAAShGUAAABIEJYBAAAgwVdHATBq/fWvf40jjjjiZd+ROn369Hj1q18dK1eujMbGxsjn89HZ2RnveMc74jOf+UxMmDAh7rvvvrj00kvjpptu2m7bww47LL75zW/GPvvsExERq1ativ/8z/+MXC4X3d3d8d73vjc++clPRkXF3z9vvuSSS+LGG2+Mu+++O3bZZZeIiPjGN74RP/rRjyIi4pFHHolXvepVMX78+Kivr4+rrroqTjrppDj11FNj1qxZERHx05/+NL75zW9GW1tbVFZWxj/8wz/Epz71qWhsbOyt69BDD40LL7yw93VXrVoVv/vd72LZsmUF/s0CAMIyAKNaTU1NrF279mWPf/WrX40PfOADcc4550RExNatW+Mzn/lMfPGLX4ympqYB7furX/1qPPDAA3HllVfG1KlTo729Pf75n/85urq6YuHChb37ve222+Lggw+ONWvWxCmnnBIREZ/85Cfjk5/8ZES8GHS/8pWv9AbwpO9///vxta99La644oqYPn169PT0xA033BBz586NW265pTeAr169Og477LA46KCDBvdLAgAGzTRsAMaEcePGxZIlS+LWW2+Ntra2fp+/ZcuWuOqqq+Kiiy6KqVOnRkREdXV1XHzxxfHWt76193k/+clPYo899oi5c+fGypUrI5/PD7q2FStWxAUXXBDTp0+PiIiKioqYN29e7LfffrFq1are55155pmxZMmSePbZZwf9GgDA4BhZBmBUa2tri2OOOWa7xxYsWNDncxsbG6OmpiYeffTRfvf7l7/8JSZNmhSvfvWrt3v81a9+9XaP3XjjjTF79uw48MADo6OjI+6555445JBDBlx/a2trPPHEE/HmN7/5ZesOOOCA+MUvftH786GHHhp//etf4/Of/3xcccUVA34NAGDwhGUARrWdTcPekfHjx0dnZ2ef6/L5fFRUVERFRUX09PTs9LUff/zxeOCBB2LFihVRUVERs2fPjmuvvXZQYTmTyURERC6Xe9m6rVu3vuyxc845Jz7wgQ/ErbfeOuDXAAAGzzRsAMaMjRs3xpYtW2KPPfaIXXfd9WXTsfP5fLS2tsaUKVNir732is7OznjiiSe2e85DDz0UixcvjogXryGurKyMD33oQ3HYYYfFbbfdFj//+c/j8ccfH3BNU6dOjT333DPWrVv3snXr1q2LN73pTds9Nnny5Lj00ktj6dKl8be//W3ArwMADI6wDMCY8Pzzz8eyZcvihBNOiIkTJ8brX//6yOVy8ctf/rL3OWvWrIk999wzGhoaYvz48XHKKafEhRde2HuN8HPPPRdLly6N3XffPXK5XNx8881xxRVXxJ133hl33nln/PznP4/9998/rrvuukHV9ulPfzqampriT3/6U0S8GNq/973vxfr162Pu3Lkve/5b3vKWmDNnTlx99dXD+I0AADtjGjYAo1pf1yyPGzcu3vnOd8Ytt9wSv/zlLyOTyUR3d3ccfPDBcfbZZ0fEizfR+trXvhaXXHJJLFu2LLq6umKPPfaIr33ta737OfPMM+Pb3/52nHTSSb37mD17dnziE5+IO+64IyZPnhyHHnrodq99+umnx6JFi2LhwoUxceLEAf0b3v3ud8f48ePj85//fDz33HPR1dUVb3zjG+P666+PKVOm9LnNGWecEffcc88gflMAwGBk8kO5bScAAACUMdOwAQAAIEFYBgAAgARhGQAAABKEZQAAAEgQlgEAACBBWAYAAIAEYRkAAAAShGUAAABI+P+428XPpRb9GQAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 1080x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xEbf4Ob0ePyH",
        "colab_type": "text"
      },
      "source": [
        "We have divided pay_total into three different groups, low, medium and high. Here low risk includes those whose pay_total is under -10, and medium refers to those between -10 and 0, and the rest belong to the high risk, which means those customers haven’t paid the credit card bill for quite a long time. As mentioned before, the smaller number means a higher education level. From this box plot, it is obvious that most high risk is concentrated among high education levels, from high school to graduate. And medium risk is distributed more uniformly among all education levels."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GHH_UBshVuCD",
        "colab_type": "code",
        "outputId": "21c70e7c-86dd-4ebd-bf7f-92253eee3ba1",
        "colab": {}
      },
      "source": [
        "plt.figure(figsize=(15,8))\n",
        "sns.set_style('whitegrid')\n",
        "sns.violinplot('AGE_GROUP', 'PAY_TOTAL', data = data1, hue = 'RISK_CAT')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Figure size 1080x576 with 0 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 126
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x1a2d041438>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 126
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA3wAAAHhCAYAAAA1c7yWAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvIxREBQAAIABJREFUeJzs3Xl8XHW9//H3mS172iZNm+4t3WmLrUURpEAFRQRRKthyoZXtolfBq1fx/tygvQh6FR7cqwiirMoit4+CIiggUBGxIJAWsKULZWshpG2atkmaSWY5vz9mzsnMZLYkMzmTmdfz8eDBzDlnpp/20Xx73ue7GaZpmgIAAAAAFB2X0wUAAAAAAPKDwAcAAAAARYrABwAAAABFisAHAAAAAEWKwAcAAAAARYrABwAAAABFyuN0AYP10ksvOV0CAAAAADhq8eLFSY8P+8Anpf7NAQAAAECxS9cJxpBOAAAAAChSBD4AAAAAKFIEPgAAAAAoUgQ+AAAAAChSBD4AAAAAKFIEPgAAAAAoUgQ+AAAAAChSBD4AAAAAKFIEvhjPP/+8PvrRj2rlypVauXKlPvOZz2jNmjXavXu3Vq5cKUlqbW3VV77yFV100UX6/Oc/r5/85CcyTTPuGkl68skn9elPf1otLS0pf72tW7fq4osv1sqVK3X22WfrnnvuiTt/ww036PTTT5dpmpKkjRs32rUtWLDAfv3222/n4U8DAAAAwHDncbqAQrNkyRL96Ec/kiSZpqnzzjtPnZ2d9vnbbrtNp5xyis466yxJ0le/+lWtX79es2bNsq958skndeONN+r2229XQ0ND0l/n4MGD+ta3vqWbb75ZEyZMUHd3t1atWqUjjjhCxx57rEKhkP7yl7/oAx/4gDZs2KDjjjtOixYt0m9+8xtJ0sc+9jH7NQAAAAAkQ+BLo7OzU+3t7Tp48KB9rLGxUY888ojGjx+vRYsW6frrr5fH49G7774rKRL2fvrTn+qOO+5QXV1dyu9+8skndcIJJ2jChAmSpLKyMt16662qrKyUJP3tb3/T/PnzdeaZZ+ruu+/Wcccdl8ffKQAAAIBiROBL8Mwzz2jlypXau3evKisr9aUvfUnjx4+3z59//vkqKyvTTTfdpC1btuiEE07QmjVrJEmvv/66fvnLX+rw4cMKBAJpf529e/dq4sSJccdqamrs1+vWrdOqVau0ePFiff/731dLS4vGjh2bw98pAAAAgGLHHL4ES5Ys0W9+8xvdeeed8vv9mjJlStz55557Tuecc47uuusu/fWvf1Vtba1+9atfSZKqqqp022236bLLLtM3v/lNhUKhlL9OY2Ojmpub44699tpr2rZtm/bv368NGzbo5ptv1iWXXCJJWrt2bY5/pwAAAACKHYEvhcbGRl111VX6+te/ru7ubvv4XXfdpT/84Q+SpIqKCk2ZMkUeT6SjdNy4caqurtZnPvMZ1dfX66abbkr5/UuXLtVTTz2l9957T5J0+PBhXXnllWptbdVDDz2klStX6rbbbtNtt92mu+66Sw888EDaAAkAAAAAiQh8aRxzzDH68Ic/rJtvvtk+tmbNGv3pT3/SsmXLtGLFCr366qu66KKL+nx2zZo1euCBB/T8888n/e7a2lpdffXV+ta3vqWVK1fq/PPP19lnn63jjjtO69at05lnnmlfO27cOE2bNk3r16/P/W8SAAAAQNEyTGvN/2HqpZde0uLFi50uAwAAAAAckS4TsWhLnt1///16+OGH+xz/7//+77jFYAAAAAD0XygUktvtdrqMgkXgy7Ply5dr+fLlTpcBAAAAFJ3bb79djz76qK688krNnz/f6XIKEnP4AAAAAAxLDz74oLq6unTrrbc6XUrBIvABAAAAGNb27NnjdAkFqySGdPr9/owbofeX1+tVeXl5Tr8TAAAAAHKp6AOf3+/XhRdepI6O9px+b3V1je6443ZCHwAAAICCVfSBLxAIqKOjXVXTT5fh9uXkO81Qjzp2PqJAIJA28D3wwAN67bXX9N3vfjcnvy4AAAAA9EfRBz6L4fbJcJc5XQYAAAAADBkWbRkC99xzjz73uc/p3HPP1RVXXCG/36/LLrtML7zwgiRp1apVuvnmmyVJP/3pT/W73/3OyXIBAAAAFAkCX57t3LlT999/v+677z7dd999amho0B133KFTTz1V69evV0dHhzo7O/Xss89Kkv7617/qlFNOcbhqAAAAAMWAwJdnLS0tWrhwoXy+yPzBY445Rjt27NDSpUu1YcMG/e1vf9Npp52mrq4ubd68WQ0NDaqurna4agAAAADFgMCXZw0NDXr55ZfV09MjSXruuec0depUVVdXq7GxUffee69OOOEEffSjH9XVV1+tT37ykw5XDAAA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vDzcbt8QTMMWiSViBHQ35LJ9Y3TT3Qz4evPOPvtsLrvsMm2fINJDCnwiIiIiMiBqamp45513+PTTT3u03UsHwzBYsGAB11xzDampqSexQpHwozl8IiIiIjIgkpKSWLJkCRdffDFffPEFTqfzuO+x2+2cffbZTJgwYQAqFBlaFPhEREREpN+NGTOGMWPGBLsMkSHPEuwCRERERERE5ORQ4BMREREREQlTCnwiIiIiIiJhSoFPREREREQkTCnwiYiIiIiIhCkFPhERERERkTClwCciIiIiIhKmFPhERERERETClAKfiIiIiIhImFLgExERERERCVMKfCIiIiIiImFKgU9ERERERCRMKfCJiIiIiIiEKQU+ERERERGRMKXAJyIiIiIiEqYU+ERERERERMKUAp+IiIiIiEiYsgW7gP6wdevWYJcgIiIiIiIy6BimaZrBLkJERERERET6n4Z0ioiIiIiIhCkFPhERERERkTClwCciIiIiIhKmFPhERERERETClAKfiIiIiIhImFLgExERERERCVMKfCIiIiIiImFKgU9ERKQHXn31VfLz87scX7BgAfX19V2Oz5o1C4CHHnqIdevWnfT6RCR8rV69mk8++STYZUiIsgW7ABERkVBw6623BrsEERmifvaznwW7BAlhCnwSch566CHmzp3LpZdeSmNjI4sWLeK6665j9erVOBwOsrKy+Ld/+ze2b9/O66+/zksvvQTA5ZdfzosvvsgHH3xASUkJtbW1lJSUcOutt3LFFVdQUFDA448/TnR0NJmZmZSWlvLGG28E+dOKyEBZvXo169atw+12U1lZybXXXsvGjRvZvXs3l112Gfv27eO8885jzpw5PPjgg1RVVZGRkUFLSwsABw4c4L777sPlcjFmzJgu53e73fzmN7+hsLAQj8fD9ddfz2WXXTbQH1NEguDHH3/k4YcfxuFw4HQ6eeKJJ9i2bRsffPABVquVadOm8dBDD7F69Wq++OILnE4npaWlXHrppdx2220sX76cuLg4br75Zp599lk2bNiA1Wpl6tSpPPzww3z44Ye89957AFx33XVccsklQf7EMpgo8EnIWbx4McuWLePSSy9lzZo1XHzxxbzzzju89957OBwOli5dymuvvcaMGTO6Pc+rr77Krl27uPvuu7niiit49NFHefLJJ8nJyeG///u/KS0tHaBPJCKDRV1dHStXruTrr7/m/vvvZ926dbS0tHDJJZcwd+5cAN5++21SU1N5/vnnqaio4B/+4R8AWLFiBfPmzePmm2+moKCgy/Crd999F4vFwltvvUVbWxuLFi0iNzeXlJSUAf+cIjKwNmzYwGmnncYDDzzA3//+dxobG1m1ahXvvPMODoeDhx9+mE8//RSAgwcP8sYbb9DY2MjZZ5/Nbbfd5j9PXl4eBQUFrFq1CsMw+Jd/+Rc++ugjAOx2O6+//npQPp8MbprDJyFn+vTp1NXVUVZWxurVq8nKymL69Ok4HA4AcnNz+eGHH7q8zzRN/+NTTz0VgPT0dJxOJwDFxcXk5OQAcMYZZ5zsjyEig9DkyZMxDINhw4YxatQoHA4Hw4cPp7W11f+avXv3Mn36dADS0tLIzs7ucvy0004jKioq4Ny7d+9my5Yt3HDDDfziF7/A7XZTXFw8QJ9MRILpqquuIiEhgV/96le8/PLLbN26lZqaGm655RZuuOEGdu3a5W8PJk2ahGEYxMXFYbMF9s388MMPzJ49G4vFgmEYnHHGGf5rngkTJgz455LQoMAnIemqq65i2bJlpKenc+qpp7J9+3Z/cNu0aROjR48mKiqKyspKwHe3bP/+/d2ec8yYMXz//fcAbNu27eR+ABEZlAzDOO5rxo8f71+8paamhrKysi7Hd+/e7R/q2WHcuHGcd955vPHGG7z++utcdNFFjB07tp8/gYgMRp9++ik5OTm89tpr3HLLLXz55ZeMGjWK119/nTfeeIMbb7yR2bNnA923QxMmTCA/Px+v14tpmnz99deMHj36uO+ToU1DOiUkXXbZZfz+979n+fLlTJw40T+PzzAMMjIyeOqpp4iMjCQtLY0rr7ySkSNH+hvEY/nNb37Dk08+SUREBMOHD+9yV01EBHzDyv/1X/+VRYsWkZaWRkJCAgB33HEHDzzwAOvXr2fUqFFER0cHvO/qq6/miSee4Prrr6ehoYH58+f73ysi4W3q1Kk89NBDvPrqq3g8HpYsWUJRURHXXnstHo+H9PR0fve731FUVNTteebNm8e2bdtYvHgxHo+HnJwcLr/8ctasWTNAn0RCkWF2HucmEiLq6+u5+eabef/99/vtjtabb77J+eefT0pKCqtWrWL79u089dRT/XJuEREREZFgUBeGhJx169bx3HPPcd999/Xr8IXk5GSWLFlCREQENptNYU9EREREQp56+ERERERERMKUFm0REREREREJUwp8IiIiIiIiYUqBT0REREREJEwp8ImIiIiIiIQprdIpIiIh6+DBg8ybN4+f//zn3HPPPf7j1dXVPPvss+Tn5/v31Fy8eDE33ngjAMuXL+ett94iJSUl4Hy33347F154Ybe/s7fn9nq9tLa2cuutt3LVVVcB0NbWxvLly/nss89wOBxYrVYWLlzITTfdhGEYbN68maeffprVq1cH/O4FCxbw8ssvM3HiRE455RQmTpyIxeK7d2sYBnfccQcXXHDBCf1ZiohIeFLgExGRkPXhhx9y7rnn8t5773HnnXficDhoaGjwB7Df/va3WCwWDh06xG233UZUVJQ/dC1cuJAHH3ywV7/vRM9dUFDA1VdfzUUXXURsbCxLliwhPT2dDz74gOjoaA4dOsT9999PaWkpv/71r3tcz9tvv01MTAwAO3fuZPHixcycOZPExMRefS4REQlfGtIpIiIh691332XRokWMGjWKtWvXAvDOO+8wefJkbrrpJn/v14gRI3jiiScYMWJEn37fiZ67pKSEqKgoHA4H+fn5FBUV8eSTTxIdHe0/x9KlS1m1ahUVFRUnVNukSZOIjo6mrKzshN4vIiLhST18IiISkvLz82loaCA3N5d9+/axcuVKFi5cyNatW5kzZ06X10+ePJnJkyf7n3/44Yf89a9/DXjNn/70p26DW2/P3djYSFNTE7m5ubz22ms4HA62b9/O1KlT/YGxQ0JCAuPHj+e7775j2LBhPf5z6LB+/XpM02T8+PG9fq+IiIQvBT4REQlJq1at4uKLL8ZqtXLRRRfx1FNP8e2332KaZsDrVqxYwSeffILX68XhcPD+++8DJzaks7fnbmpq4s4772T48OFMmTIF8M21c7vdRz2/y+UC6BIGO//+zj9bvHgxFosFt9tNcnIyy5cv9/caioiIgAKfiIiEoPr6ev785z8TFxfHunXrALDZbKxcuZJp06aRn5/P9ddfD/gWYrn99tspKiril7/8ZZ9+b2/PHRMTw9KlS7nooovIzc3lkksuYfr06fzpT3/C6XTicDj8r62urqakpIScnBwaGhpoaGgIOJdpmhw8eJDhw4f7j3WewyciInI0msMnIiIhZ82aNYwbN46vvvqK9evXs379el5++WU+/vhjrr76ar7//ntWrlzp70lzOp18/vnnx+w566lrr7221+dOTk7mzjvvZOnSpbS0tDBjxgymTJnCY489RktLC+BbbfTBBx/kyiuvJC0tjXHjxuF2uwOGnL7//vuMHj2a5OTkPn0GEREZWtTDJyIiIWfVqlXccsstAcfOPPNMJk+ezKpVq1i1ahXLli3jiiuuwGKx4HQ6mT17Nn/84x/9rz/aHL4LL7yQ22+//Zi/d/jw4T0695Guu+463n77bV599VXuvvtunnvuOV555RWuvPJKLBYLhmFwxRVXcPPNNwO+IZ0vvPAC//7v/85//Md/4HK5GDlyJC+88MIJ/GmJiMhQZphHTkgQERERERGRsKAePhERkU5uuOEG6uvruxw/5ZRTWLp0aRAqEhEROXHq4RMREREREQlTWrRFREREREQkTCnwiYiIiIiIhCkFPhERERERkTClwCciIiIiIhKmFPhERERERETC1P8Dytgx1fM78bsAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 1080x576 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "egpU06EUefRZ",
        "colab_type": "text"
      },
      "source": [
        "Since age has a wide range, we grouped them into young, middle and senior. Where young represents those who are above 21 but under 40, middle is among 40 to 60 and senior is over 60 to 81. From this plot, we can see no matter risk it is, senior group always has the largest size, which means people over 60 would have a higher risk of credit card default compared with younger people."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Pl-_pDD4VuCI",
        "colab_type": "code",
        "outputId": "b743e7ee-dc04-4fbc-aba8-644cdd5560f8",
        "colab": {}
      },
      "source": [
        "plt.figure(figsize = (15,10))\n",
        "sns.countplot(x='RISK_CAT', data=data1)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Figure size 1080x720 with 0 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 127
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x1a264c34e0>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 127
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAA4cAAAJOCAYAAAAEfXJeAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvIxREBQAAIABJREFUeJzs3X2c1XWd///nwMyIcBjQZCjiayZpY4iKSOQtLuTCMNTCwkS5Ek1DKNJVIVERUMRrqt0oc0uW1EzExc0W1wtYF8WMIC9uuGwuyVauoaXiHNZBR87vj37NRrY0pDMjM/f7X5z3fD5zXu+53Ti3z2POmXPKSqVSKQAAALRp7Vp6AAAAAFqeOAQAAEAcAgAAIA4BAACIOAQAACDiEAAAgCTlLT1Ac1q3bl1LjwAAANCi+vXr92fX21QcJv/3DwIAAKC129UTZl5WCgAAgDgEAABAHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQJLylh4AgN1z+s1fbukRoE1aPPlrLT0CQJPyzCEAAADiEAAAAHEIAABAxCEAAAARhwAAAKQJ3620vr4+l156aTZv3pzXX389Y8aMyahRo3LBBRdk27Zt2WuvvTJ//vz06NEjTz/9dObOnZv27dtn//33z7x581JZWZnly5dnyZIlqaioyMiRI3PGGWekVCplwYIF+dnPfpaysrKcd955Ofroo5tqGwAAAG1Ck8Xh3XffnfLy8nz/+9/P9u3bM2rUqDz55JMZNGhQJk6cmAcffDDXXnttFi5cmEsuuSRXXnllampqsmDBgixbtiwjR47MokWLsnz58lRUVGT8+PEZMmRINm/enOeffz5Lly7Nli1bMmnSpNxzzz0pL/epHAAAAH+tJntZ6XHHHZeZM2cmScrKyvLmm29m7dq1GTp0aJJkyJAheeyxx1IsFvPKK6+kpqYmSTJs2LCsWbMmjz/+ePr27ZuOHTumoqIiAwcOzJo1a7J27docc8wxSZLu3bunW7du2bRpU1NtAwAAoE1osqfbOnXqlCTZvn17zj///IwePTo/+tGP0rlz59/fcXl56uvrUywWG45NkkKhkNra2tTW1jYcu6v1Tp06pba2ttFz1dXVvd2tAQBtkGsIoLVr0tdibtmyJdOnT8/w4cNz9tln56GHHkqxWEzXrl1TX1+fysrKFAqFbNu2reGcYrGYqqqqFAqFFIvFndb33XffbN26daf1bdu2pUuXLo2eacOGDe/M5gCANsU1BNDaNVkcvvjii5k4cWJmzJiR4cOHJ0mOOuqorFy5MhMnTsxDDz2Ufv36pVAopKqqKhs3bkxNTU1WrlyZAQMG5IgjjsjVV1+dYrGYvfbaK6tXr878+fPTvXv33H333TnppJPywgsvZMuWLTnwwAMbPVfv3r2bassAzePJlh4A2ibXEEBrsKtfdDVZHC5atCivvvpqFi9enMWLFydJLrjggnzzm9/MihUr0q5du1xzzTVJkiuuuCJz5sxJqVRKz549c/7556eysjJTp07NxIkTUyqVMmrUqBx00EH50Ic+lMceeyynnHJK6uvrM3v27LRv377Rc3Xo0KEptgsAtHKuIYDWrqxUKpVaeojmsm7duvTr16+lxwB4W06/+cstPQK0SYsnf62lRwB423bVRE32bqUAAADsOcQhAAAA4hAAAABxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQJLypvzmmzdvzllnnZX7778/X//617N27dokyWuvvZb/+I//yOrVq/Ob3/wmZ555Zg488MAkybBhwzJ58uQ8/PDDWbhwYSoqKtK3b9/MmDEjZWVluemmm7JixYq0b98+kyZNygknnNCUWwAAAGgTmiwOb7311ixbtiwvv/xykmT69OkNX7vwwgtzyimnpGvXrrn//vszbty4TJ06teHr9fX1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EYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAABBxCAAAQMQhAAAAEYcAAABEHAIAAJCkvKUHAACg5f3zxMktPQK0SaOW3NzSIzTwzCEAAADiEAAAAHEIAABAxCEAAAARhwAAAEQcAgAAEHEIAABAxCEAAAARhwAAAEQcAgAAEHEIAABAxCEAAAARhwAAACQpb+47POmkk1IoFJIkFRUVWbhwYS644IJs27Yte+21V+bPn58ePXrk6aefzty5c9O+ffvsv//+mTdvXiorK7N8+fIsWbIkFRUVGTlyZM4444zm3gIAAECr06xxWFdXl7q6uvzjP/5jw9qCBQsyaNCgTJw4MQ8++GCuvfbaLFy4MJdcckmuvPLK1NTUZMGCBVm2bFlGjhyZRYsWZfny5amoqMj48eMzZMiQ9OrVqzm3AQAA0Oo068tK//3f/z1vvvlmzjzzzIwbNy4PPfRQ1q5dm6FDhyZJhgwZksceeyzFYjGvvPJKampqkiTDhg3LmjVr8vjjj6dv377p2LFjKioqMnDgwKxZs6Y5twAAANAqNeszh3vvvXcmT56cU045Jb/97W8zbty47NixI507d/79MOXlqa+vT7FYTKdOnRrOKxQKqa2tTW1tbcOxf7y+O+rq6t6ZzQAAbYprCKApvJseW5o1Dj/4wQ/mgAMOSLt27VJdXZ2PfOQj+eUvf5lisZiuXbumvr4+lZWVKRQK2bZtW8N5xWIxVVVVKRQKKRaLO63vu+++uzXDhg0b3rH9AABth2sIoCm8mx5bmjUOly5dmqeffjpXXnllisViNm7cmAEDBmTlypWZOHFiHnroofTr1y+FQiFVVVXZuHFjampqsnLlygwYMCBHHHFErr766hSLxey1115ZvXp15s+fv1sz9O7du4l2B9BMnmzpAaBtau3XEFtaegBoo5r7sWVXMdqscfi5z30us2bNytixY5MkF154Yfr165eLLrooK1asSLt27XLNNdckSa644orMmTMnpVIpPXv2zPnnn5/KyspMnTo1EydOTKlUyqhRo3LQQQft1gwdOnR4x/cFALR+riGApvBuemxp1jisrKzMdddd95b1b33rW29ZO/TQQ3P77be/ZX306NEZPXp0k8wHAADQVjXru5UCAADw7iQOAQAAEIcAAACIQwAAACIO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ffTR/PznP8+JJ56YESNG5PLLL0+pVEplZWXmzp2bnj175gc/+EFuu+22vOc978mbb76ZoUOHJkmOOuqo/PSnP82ECRMya9asHHLIIXnggQfywAMP5KqrrsrQoUPzsY99LM8++2wOPvjg7Lvvvlm3bl3eeOONfOc730mnTp1a+CcCNJcNGzbkzDPPzO9+97uMGDEipVIpnTt3zumnn5758+dn3bp12WefffLaa6/ly1/+8p8954tf/GIL74I9gTikTdu0aVMee+yx3HnnnamsrMw111yTm2++OSNHjsyqVatyyCGHZNu2bXnkkUdyzjnn5N/+7d8aXhIGtD1bt27NLbfckp/85Ce58MIL88ADD+S1117L8ccfn1WrVuWSSy7JYYcdlsceeyxXXHFF5s+fnxtvvDH33HNP9t5770ydOrXR9/X888/nC1/4Qg444IAMGzYsl156ac4999ycc845Wb9+fQYNGtSEOwXeTcrKyvLtb387r732WoYMGZLTTz89SbJq1ar86le/yrJly1JXV5cTTzzx/zxHHNIY4pA2bcuWLenXr18qKyuTJAMGDMjdd9+dCRMm5Lvf/W4OO+ywfPKTn8yKFSuyYcOGdOvWLYVCoYWnBlrKIYcckrKyslRVVeUDH/hAKisrU1lZmbq6ujzzzDO59tprkySlUinbt2/PL3/5y3zwgx9Mx44dk/z+2cJdKZVKDf/u1KlTDjjggCRJ586dc9BBByVJunTpku3btzfB7oB3q0MOOSTt27dPoVBIWVlZw/ozzzyTI488MmVlZdl7771z6KGH/sVzYFe8IQ1tWrdu3fLEE0/k9ddfT5L8+Mc/zgEHHJBCoZD3vve9ue222zJ48OB8/OMfz+WXX57jjjuuhScGWtKuLrAOPPDAXH755fne976Xyy+/PMcff3w+8IEP5Be/+EWKxWKS5IknnnjLeR06dMiWLVuSJE8++WSj7gtoW/6vx4MPf/jDWb9+fcMvpJ5++um/eA7simcOadMOOuigHHDAARk3blzKysrSo0ePhnf3GjlyZBYuXJiDDz44gwcPzs0335zhw4e38MTAu9X8+fMze/bsvPnmm9m+fXtmzpyZfffdN+eee27Gjx+frl27pkOHDm85b+LEibnyyivzD//wD9l///1bYHJgTzVkyJCsWbMmp5xySvbZZ59UVlamvNzlPX+9stIfv4YFAADYIzz77LN54oknMnr06Gzfvj0nnHBClixZkve9730tPRp7KHEIAAB7oNdeey0XXHBBXnnllWzfvj2jRo3KGWec0dJjsQcThwAAAHhDGgAAAMQhAAAAEYcAAABEHAIAABCfcwhAG/frX/86n/jEJ3LQQQc1rNXW1uaII47I/Pnz8/d///f5n//5n8ycOTOlUinf/OY3c++99zYce8opp2TcuHFJkgkTJuSMM87I0KFDk/z+Q+2nTJmSiy++OMcff/wu5/jxj3+cRYsWZevWramvr0+fPn3yla98JV27dm045sEHH8zUqVPzne98JwMHDkySrF69Otddd12S5Pnnn0+HDh2yzz77JEm+9a1veUt7ABpNHALQ5nXu3Dl33313w+3XX389p556apYvX77TcStWrMijjz6aO++8M5WVlXnllVcyduzY9OzZM0OGDNnp2PXr1+dLX/pSFixY8Jav/alHH300F198cb71rW/l4IMPzo4dO3LDDTdk6tSpue222xqOW7p0aUaNGpVbbrmlIQ4HDRqUQYMGJUm+8pWv5NBDD8348ePf1s8DgLZJHALAn3jllVdSLBbTpUuX/Pa3v21Yf/HFF7Njx468/vrrqaysTNeuXbNw4cIUCoWdzl+7dm3+5m/+Jl/96lfTv3//v3h/3/jGNzJt2rQcfPDBSZJ27dpl+vTp+Zd/+Ze88cYbqaioyJYtW/LYY4/l3nvvzXHHHZdf//rX6dmz5zu7cQDaNH9zCECbV1tbm09/+tM5/vjjc/TRR2fatGmZOHFiRo0atdNxJ510Utq1a5ejjz46EyZMyFe/+tWUl5fn//2//9dwzKOPPpqzzz47/fv3b1QYJsmGDRtyxBFH7LRWWVmZE088MRUVFUmSO++8M4MGDUr37t1zzDHH7PSMIgC8E8QhAG3eH15W+qMf/SjTp0/PSy+9lBEjRrzluKqqqnzve9/L3XffneOOOy7PPPNMPvOZz+T+++9vOOaf//mfc9NNN+WnP/1p/umf/qlR919WVpYdO3b8n1/fsWNHli1blk996lNJkk996lNZtmxZtm/fvps7BYD/mzgEgD9y6qmnpk+fPpk1a9Zbvvad73wnTz75ZA488MCMGzcu3/jGN3L++edn6dKlDcdceumlOeqoo3LNNddk7ty52bRp01+8z8MPPzxPPvnkTmv19fWZMmVKXnjhhTzyyCP5zW9+k/nz52fYsGGZN29eamtr88Mf/vDtbxgA/n/iEAD+xFe+8pWsW7cuDz744E7rxWIxN9xwQ1599dUkv39G79lnn80hhxzScExlZWWS5GMf+1jGjx+fc889N3V1dbu8v7PPPjvf+MY38swzzyT5fRhef/31efXVV1NdXZ2lS5dm0qRJWbVqVVauXJlVq1ZlypQpXloKwDtKHALAn3jve9+bz3/+87n66qvzxhtvNKxPmzYthx9+eD772c/mk5/8ZI4//vh07Ngx06ZN+7Pf50tf+lL23nvvzJ07d5f3d/TRR2fWrFmZNWtWPv3pT+fEE0/M1q1bs2jRovzud7/Lv/7rv77lHUgnTJiQZ599NuvXr3/7Gwbg/2vvjm0AhkEgAH5mpPcGLO1FyABJm7i5a2m+fSEESa6ZmdMhAAAAOMsrCwD42N473f06q6qstX5OBABPNocAAAC4OQQAAEA5BAAAIMohAAAAUQ4BAACIcggAAECSGywsP6F+LCBUAAAAAElFTkSuQmCC\n",
            "text/plain": [
              "<Figure size 1080x720 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "CXbhdlIneoGK",
        "colab_type": "text"
      },
      "source": [
        "This chart shows the distribution of risk among the entire dataset. Low risk has the least customers while middle risk has the most. And here middle risk is over 8 times the size of low risk and about 4 times of high risk. It is not so bad because although low risk is the least, middle risk still covers the most."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8vLWCU4JVuCO",
        "colab_type": "code",
        "outputId": "1e309e0a-a230-4ff1-aa0e-82b0ececd99e",
        "colab": {}
      },
      "source": [
        "sns.set(rc={'figure.figsize':(15,7)})\n",
        "sns.set_context(\"talk\", font_scale=0.8)\n",
        "\n",
        "pay1 = sns.countplot( y=\"PAY_0\", hue='default payment next month', data=data1)\n",
        "pay1.set_yticklabels(['No Consumption','Paid in Full','Use Revolving Credit','Delay 1 mth','Delay 2 mths'\n",
        "                     ,'Delay 3 mths','Delay 4 mths','Delay 5 mths','Delay 6 mths','Delay 7 mths','Delay 8 mths'])\n",
        "pay1.set_title('Credit Behaviour (most recent month)')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[Text(0,0,'No Consumption'),\n",
              " Text(0,0,'Paid in Full'),\n",
              " Text(0,0,'Use Revolving Credit'),\n",
              " Text(0,0,'Delay 1 mth'),\n",
              " Text(0,0,'Delay 2 mths'),\n",
              " Text(0,0,'Delay 3 mths'),\n",
              " Text(0,0,'Delay 4 mths'),\n",
              " Text(0,0,'Delay 5 mths'),\n",
              " Text(0,0,'Delay 6 mths'),\n",
              " Text(0,0,'Delay 7 mths'),\n",
              " Text(0,0,'Delay 8 mths')]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 128
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5,1,'Credit Behaviour (most recent month)')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 128
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 1080x504 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IKta5felex2_",
        "colab_type": "text"
      },
      "source": [
        "This graph shows the relationship between default and credit behaviors. For those who have no consumption, paid in full every month and delay 1 month, the number of no default is more than that of default. For those who use revolving credit, which means people who only pay the minimum every month, the non-default far exceeds the default. However, for those who delay the payment for more than one month, it turns out that the likelihood of default would then surpass the non-default, which also means the longer the payment delay, the higher risk for that person on default."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PhhiwO-hVuCV",
        "colab_type": "text"
      },
      "source": [
        "# 3. Data Cleaning and Pre-processing"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "j401lqaUnxl0",
        "colab_type": "text"
      },
      "source": [
        "In this section we will deal with these aspects:\n",
        "- Missing values  \n",
        "- Categorical Variables:\n",
        "  - Ordinal variables: EDUCATION, PAY_n\n",
        "  - Norminal variables : MARRIAGE, SEX\n",
        "- Train-test split\n",
        "- Resampling\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e0OPNTdyVuCY",
        "colab_type": "text"
      },
      "source": [
        "## 3.1 Checking Missing Values"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "d_WFHwa8VuCZ",
        "colab_type": "code",
        "outputId": "ea02cc78-7c0e-416d-fe54-b0db5d02d978",
        "colab": {}
      },
      "source": [
        "# use a copy of the original dataset for cleaning and modeling\n",
        "credit.isnull().sum()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "ID                            0\n",
              "LIMIT_BAL                     0\n",
              "SEX                           0\n",
              "EDUCATION                     0\n",
              "MARRIAGE                      0\n",
              "AGE                           0\n",
              "PAY_0                         0\n",
              "PAY_2                         0\n",
              "PAY_3                         0\n",
              "PAY_4                         0\n",
              "PAY_5                         0\n",
              "PAY_6                         0\n",
              "BILL_AMT1                     0\n",
              "BILL_AMT2                     0\n",
              "BILL_AMT3                     0\n",
              "BILL_AMT4                     0\n",
              "BILL_AMT5                     0\n",
              "BILL_AMT6                     0\n",
              "PAY_AMT1                      0\n",
              "PAY_AMT2                      0\n",
              "PAY_AMT3                      0\n",
              "PAY_AMT4                      0\n",
              "PAY_AMT5                      0\n",
              "PAY_AMT6                      0\n",
              "default payment next month    0\n",
              "dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_fgWJvbCVuCc",
        "colab_type": "text"
      },
      "source": [
        "## 3.2 Categorical Varaibles: "
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "k3IU15fvVuCc",
        "colab_type": "text"
      },
      "source": [
        "### 3.2.1 Ordinal variables: EDUCATION, PAY_n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NBGSASHEq84O",
        "colab_type": "text"
      },
      "source": [
        "We consider EDUCATION and PAY_n as ordinal variables, which means the value has a clear ordering.   \n",
        "In EDUCATION variable, we discover some unexpected values 5,6, and 0, when the data description only provides value 1,2,3 and 4. We decide to combine 5,6,0 all into 4, which stands for 'other'.  \n",
        "Also in PAY_n variables, we have unexpected values -2, and 0."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uSp0sklrVuCd",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "data['EDUCATION']= data['EDUCATION'].apply(lambda x:4 if x in [5,6,0] else x)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "s1OO9-ChVuCj",
        "colab_type": "code",
        "outputId": "dba3cba9-7b54-4228-b0e3-8f0055c81d09",
        "colab": {}
      },
      "source": [
        "data['EDUCATION'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2    14030\n",
              "1    10585\n",
              "3     4917\n",
              "4      468\n",
              "Name: EDUCATION, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "Jt4mWch0VuCp",
        "colab_type": "code",
        "outputId": "bc73cf3b-f009-486b-d60e-82670367c666",
        "colab": {}
      },
      "source": [
        "#PAY_n\n",
        "data[['PAY_0','BILL_AMT1','PAY_AMT1']][(data['PAY_0']==0) | (data['PAY_0'] ==-1)|(data['PAY_0'] ==-2)]"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PAY_0</th>\n",
              "      <th>BILL_AMT1</th>\n",
              "      <th>PAY_AMT1</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>-1</td>\n",
              "      <td>2682</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0</td>\n",
              "      <td>29239</td>\n",
              "      <td>1518</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0</td>\n",
              "      <td>46990</td>\n",
              "      <td>2000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>-1</td>\n",
              "      <td>8617</td>\n",
              "      <td>2000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>0</td>\n",
              "      <td>64400</td>\n",
              "      <td>2500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>0</td>\n",
              "      <td>367965</td>\n",
              "      <td>55000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>0</td>\n",
              "      <td>11876</td>\n",
              "      <td>380</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>0</td>\n",
              "      <td>11285</td>\n",
              "      <td>3329</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>-2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>0</td>\n",
              "      <td>11073</td>\n",
              "      <td>2306</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>-1</td>\n",
              "      <td>12261</td>\n",
              "      <td>21818</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>-1</td>\n",
              "      <td>12137</td>\n",
              "      <td>1000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>0</td>\n",
              "      <td>70887</td>\n",
              "      <td>3000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>0</td>\n",
              "      <td>15376</td>\n",
              "      <td>3200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>0</td>\n",
              "      <td>253286</td>\n",
              "      <td>10358</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>0</td>\n",
              "      <td>38358</td>\n",
              "      <td>3000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>-1</td>\n",
              "      <td>316</td>\n",
              "      <td>316</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23</th>\n",
              "      <td>-2</td>\n",
              "      <td>5512</td>\n",
              "      <td>19428</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>0</td>\n",
              "      <td>4744</td>\n",
              "      <td>5757</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>0</td>\n",
              "      <td>47620</td>\n",
              "      <td>1973</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>27</th>\n",
              "      <td>0</td>\n",
              "      <td>22541</td>\n",
              "      <td>1300</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>28</th>\n",
              "      <td>-1</td>\n",
              "      <td>650</td>\n",
              "      <td>3415</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29</th>\n",
              "      <td>0</td>\n",
              "      <td>15329</td>\n",
              "      <td>1500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>30</th>\n",
              "      <td>-1</td>\n",
              "      <td>16646</td>\n",
              "      <td>17270</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>32</th>\n",
              "      <td>0</td>\n",
              "      <td>93036</td>\n",
              "      <td>3023</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>33</th>\n",
              "      <td>-2</td>\n",
              "      <td>10929</td>\n",
              "      <td>4152</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>34</th>\n",
              "      <td>-2</td>\n",
              "      <td>13709</td>\n",
              "      <td>5006</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>35</th>\n",
              "      <td>-1</td>\n",
              "      <td>30265</td>\n",
              "      <td>131</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>36</th>\n",
              "      <td>0</td>\n",
              "      <td>186503</td>\n",
              "      <td>8026</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>37</th>\n",
              "      <td>0</td>\n",
              "      <td>15054</td>\n",
              "      <td>1500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29960</th>\n",
              "      <td>0</td>\n",
              "      <td>9406</td>\n",
              "      <td>3009</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29961</th>\n",
              "      <td>-2</td>\n",
              "      <td>0</td>\n",
              "      <td>263</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29963</th>\n",
              "      <td>0</td>\n",
              "      <td>348392</td>\n",
              "      <td>323014</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29964</th>\n",
              "      <td>-1</td>\n",
              "      <td>735</td>\n",
              "      <td>51</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29965</th>\n",
              "      <td>0</td>\n",
              "      <td>134236</td>\n",
              "      <td>6300</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29967</th>\n",
              "      <td>0</td>\n",
              "      <td>50564</td>\n",
              "      <td>2686</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29968</th>\n",
              "      <td>0</td>\n",
              "      <td>13730</td>\n",
              "      <td>2000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29969</th>\n",
              "      <td>0</td>\n",
              "      <td>110006</td>\n",
              "      <td>5000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29970</th>\n",
              "      <td>-1</td>\n",
              "      <td>33654</td>\n",
              "      <td>52951</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29971</th>\n",
              "      <td>0</td>\n",
              "      <td>65554</td>\n",
              "      <td>2395</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29972</th>\n",
              "      <td>0</td>\n",
              "      <td>21628</td>\n",
              "      <td>2000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29975</th>\n",
              "      <td>0</td>\n",
              "      <td>45075</td>\n",
              "      <td>8840</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29977</th>\n",
              "      <td>0</td>\n",
              "      <td>131939</td>\n",
              "      <td>7000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29978</th>\n",
              "      <td>0</td>\n",
              "      <td>238973</td>\n",
              "      <td>10029</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29979</th>\n",
              "      <td>-2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29980</th>\n",
              "      <td>0</td>\n",
              "      <td>43998</td>\n",
              "      <td>10000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29982</th>\n",
              "      <td>0</td>\n",
              "      <td>7752</td>\n",
              "      <td>1500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29983</th>\n",
              "      <td>-2</td>\n",
              "      <td>1822</td>\n",
              "      <td>2890</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29984</th>\n",
              "      <td>-1</td>\n",
              "      <td>315</td>\n",
              "      <td>923</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29985</th>\n",
              "      <td>-2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29986</th>\n",
              "      <td>-1</td>\n",
              "      <td>2220</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29987</th>\n",
              "      <td>0</td>\n",
              "      <td>23292</td>\n",
              "      <td>3000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29988</th>\n",
              "      <td>0</td>\n",
              "      <td>279640</td>\n",
              "      <td>65000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29989</th>\n",
              "      <td>-1</td>\n",
              "      <td>3425</td>\n",
              "      <td>9054</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29990</th>\n",
              "      <td>0</td>\n",
              "      <td>138325</td>\n",
              "      <td>6000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29992</th>\n",
              "      <td>0</td>\n",
              "      <td>8802</td>\n",
              "      <td>2000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29993</th>\n",
              "      <td>0</td>\n",
              "      <td>3042</td>\n",
              "      <td>2000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29995</th>\n",
              "      <td>0</td>\n",
              "      <td>188948</td>\n",
              "      <td>8500</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29996</th>\n",
              "      <td>-1</td>\n",
              "      <td>1683</td>\n",
              "      <td>1837</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29999</th>\n",
              "      <td>0</td>\n",
              "      <td>47929</td>\n",
              "      <td>2078</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>23182 rows × 3 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "       PAY_0  BILL_AMT1  PAY_AMT1\n",
              "1         -1       2682         0\n",
              "2          0      29239      1518\n",
              "3          0      46990      2000\n",
              "4         -1       8617      2000\n",
              "5          0      64400      2500\n",
              "6          0     367965     55000\n",
              "7          0      11876       380\n",
              "8          0      11285      3329\n",
              "9         -2          0         0\n",
              "10         0      11073      2306\n",
              "11        -1      12261     21818\n",
              "12        -1      12137      1000\n",
              "14         0      70887      3000\n",
              "16         0      15376      3200\n",
              "17         0     253286     10358\n",
              "20         0      38358      3000\n",
              "21        -1        316       316\n",
              "23        -2       5512     19428\n",
              "24         0       4744      5757\n",
              "25         0      47620      1973\n",
              "27         0      22541      1300\n",
              "28        -1        650      3415\n",
              "29         0      15329      1500\n",
              "30        -1      16646     17270\n",
              "32         0      93036      3023\n",
              "33        -2      10929      4152\n",
              "34        -2      13709      5006\n",
              "35        -1      30265       131\n",
              "36         0     186503      8026\n",
              "37         0      15054      1500\n",
              "...      ...        ...       ...\n",
              "29960      0       9406      3009\n",
              "29961     -2          0       263\n",
              "29963      0     348392    323014\n",
              "29964     -1        735        51\n",
              "29965      0     134236      6300\n",
              "29967      0      50564      2686\n",
              "29968      0      13730      2000\n",
              "29969      0     110006      5000\n",
              "29970     -1      33654     52951\n",
              "29971      0      65554      2395\n",
              "29972      0      21628      2000\n",
              "29975      0      45075      8840\n",
              "29977      0     131939      7000\n",
              "29978      0     238973     10029\n",
              "29979     -2          0         0\n",
              "29980      0      43998     10000\n",
              "29982      0       7752      1500\n",
              "29983     -2       1822      2890\n",
              "29984     -1        315       923\n",
              "29985     -2          0         0\n",
              "29986     -1       2220         0\n",
              "29987      0      23292      3000\n",
              "29988      0     279640     65000\n",
              "29989     -1       3425      9054\n",
              "29990      0     138325      6000\n",
              "29992      0       8802      2000\n",
              "29993      0       3042      2000\n",
              "29995      0     188948      8500\n",
              "29996     -1       1683      1837\n",
              "29999      0      47929      2078\n",
              "\n",
              "[23182 rows x 3 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tAoPYFKaVuC2",
        "colab_type": "text"
      },
      "source": [
        "## 3.2.2 Norminal Variables: MARRIAGE and SEX"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dCGrXtyrB4g2",
        "colab_type": "text"
      },
      "source": [
        "We identify MARRIAGE and SEX as norminal variables, which means there is no intrinsic ordering to the categories.  \n",
        "SEX has onley 2 categories: 1 for male and 2 for female. We can keep its original format.  \n",
        "MARRIAGE should have 3 values according to data description. However, an unexpected variable 0 takes place. We decided to merge value 0 into value 3, which stands for 'other'.\n",
        "We then apply one-hot encoding to create dummy variables for MARRIAGE."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CIqrif7MDPVV",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "data['MARRIAGE'] = data['MARRIAGE'].apply(lambda x:3 if x==0 else x )"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8UcqCKtSVuCh",
        "colab_type": "code",
        "outputId": "c8e5e4ca-0b98-4a2b-c7bc-5b3fa264fac0",
        "colab": {}
      },
      "source": [
        "data['MARRIAGE'].value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2    15964\n",
              "1    13659\n",
              "3      377\n",
              "Name: MARRIAGE, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NgZPcJMqVuC3",
        "colab_type": "code",
        "outputId": "f7880d3f-588c-47d7-d845-118d70d7fafa",
        "colab": {}
      },
      "source": [
        "marriage=pd.get_dummies(data['MARRIAGE'],columns='MARRIAGE',prefix='MARRIAGE')\n",
        "marriage.head()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>MARRIAGE_1</th>\n",
              "      <th>MARRIAGE_2</th>\n",
              "      <th>MARRIAGE_3</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   MARRIAGE_1  MARRIAGE_2  MARRIAGE_3\n",
              "0           1           0           0\n",
              "1           0           1           0\n",
              "2           0           1           0\n",
              "3           1           0           0\n",
              "4           1           0           0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2d3g4IKyVuC6",
        "colab_type": "code",
        "outputId": "0feef45b-1797-4306-9c60-4249fc115d9e",
        "colab": {}
      },
      "source": [
        "datanew1 = pd.concat([data.iloc[:,0:3],marriage],axis = 1)\n",
        "datanew = pd.concat([datanew1,data.iloc[:,4:24]],axis = 1)\n",
        "datanew.shape"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(30000, 26)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "scrolled": true,
        "id": "j8B6EiHkVuC8",
        "colab_type": "code",
        "outputId": "21c76a07-6811-46e8-a014-e8de95aa597a",
        "colab": {}
      },
      "source": [
        "datanew.head().T"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "      <th>1</th>\n",
              "      <th>2</th>\n",
              "      <th>3</th>\n",
              "      <th>4</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>LIMIT_BAL</th>\n",
              "      <td>20000</td>\n",
              "      <td>120000</td>\n",
              "      <td>90000</td>\n",
              "      <td>50000</td>\n",
              "      <td>50000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>SEX</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>EDUCATION</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>MARRIAGE_1</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>MARRIAGE_2</th>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>MARRIAGE_3</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>AGE</th>\n",
              "      <td>24</td>\n",
              "      <td>26</td>\n",
              "      <td>34</td>\n",
              "      <td>37</td>\n",
              "      <td>57</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_0</th>\n",
              "      <td>2</td>\n",
              "      <td>-1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>-1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_2</th>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_3</th>\n",
              "      <td>-1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>-1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_4</th>\n",
              "      <td>-1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_5</th>\n",
              "      <td>-2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_6</th>\n",
              "      <td>-2</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT1</th>\n",
              "      <td>3913</td>\n",
              "      <td>2682</td>\n",
              "      <td>29239</td>\n",
              "      <td>46990</td>\n",
              "      <td>8617</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT2</th>\n",
              "      <td>3102</td>\n",
              "      <td>1725</td>\n",
              "      <td>14027</td>\n",
              "      <td>48233</td>\n",
              "      <td>5670</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT3</th>\n",
              "      <td>689</td>\n",
              "      <td>2682</td>\n",
              "      <td>13559</td>\n",
              "      <td>49291</td>\n",
              "      <td>35835</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT4</th>\n",
              "      <td>0</td>\n",
              "      <td>3272</td>\n",
              "      <td>14331</td>\n",
              "      <td>28314</td>\n",
              "      <td>20940</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT5</th>\n",
              "      <td>0</td>\n",
              "      <td>3455</td>\n",
              "      <td>14948</td>\n",
              "      <td>28959</td>\n",
              "      <td>19146</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>BILL_AMT6</th>\n",
              "      <td>0</td>\n",
              "      <td>3261</td>\n",
              "      <td>15549</td>\n",
              "      <td>29547</td>\n",
              "      <td>19131</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT1</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1518</td>\n",
              "      <td>2000</td>\n",
              "      <td>2000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT2</th>\n",
              "      <td>689</td>\n",
              "      <td>1000</td>\n",
              "      <td>1500</td>\n",
              "      <td>2019</td>\n",
              "      <td>36681</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT3</th>\n",
              "      <td>0</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>1200</td>\n",
              "      <td>10000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT4</th>\n",
              "      <td>0</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>1100</td>\n",
              "      <td>9000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT5</th>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1000</td>\n",
              "      <td>1069</td>\n",
              "      <td>689</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>PAY_AMT6</th>\n",
              "      <td>0</td>\n",
              "      <td>2000</td>\n",
              "      <td>5000</td>\n",
              "      <td>1000</td>\n",
              "      <td>679</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Default</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                0       1      2      3      4\n",
              "LIMIT_BAL   20000  120000  90000  50000  50000\n",
              "SEX             2       2      2      2      1\n",
              "EDUCATION       2       2      2      2      2\n",
              "MARRIAGE_1      1       0      0      1      1\n",
              "MARRIAGE_2      0       1      1      0      0\n",
              "MARRIAGE_3      0       0      0      0      0\n",
              "AGE            24      26     34     37     57\n",
              "PAY_0           2      -1      0      0     -1\n",
              "PAY_2           2       2      0      0      0\n",
              "PAY_3          -1       0      0      0     -1\n",
              "PAY_4          -1       0      0      0      0\n",
              "PAY_5          -2       0      0      0      0\n",
              "PAY_6          -2       2      0      0      0\n",
              "BILL_AMT1    3913    2682  29239  46990   8617\n",
              "BILL_AMT2    3102    1725  14027  48233   5670\n",
              "BILL_AMT3     689    2682  13559  49291  35835\n",
              "BILL_AMT4       0    3272  14331  28314  20940\n",
              "BILL_AMT5       0    3455  14948  28959  19146\n",
              "BILL_AMT6       0    3261  15549  29547  19131\n",
              "PAY_AMT1        0       0   1518   2000   2000\n",
              "PAY_AMT2      689    1000   1500   2019  36681\n",
              "PAY_AMT3        0    1000   1000   1200  10000\n",
              "PAY_AMT4        0    1000   1000   1100   9000\n",
              "PAY_AMT5        0       0   1000   1069    689\n",
              "PAY_AMT6        0    2000   5000   1000    679\n",
              "Default         1       1      0      0      0"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 37
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZXmW43NoVuCs",
        "colab_type": "text"
      },
      "source": [
        "## 3.3 Rename Target Column and Drop id"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lLud8pG8VuCv",
        "colab_type": "code",
        "outputId": "96e0f122-3e25-4245-fe65-ee143bb046bc",
        "colab": {}
      },
      "source": [
        "data.rename(columns ={'default payment next month': 'Default'}, inplace = True)\n",
        "data.head(5)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>ID</th>\n",
              "      <th>LIMIT_BAL</th>\n",
              "      <th>SEX</th>\n",
              "      <th>EDUCATION</th>\n",
              "      <th>MARRIAGE</th>\n",
              "      <th>AGE</th>\n",
              "      <th>PAY_0</th>\n",
              "      <th>PAY_2</th>\n",
              "      <th>PAY_3</th>\n",
              "      <th>PAY_4</th>\n",
              "      <th>...</th>\n",
              "      <th>PAY_AMT1</th>\n",
              "      <th>PAY_AMT2</th>\n",
              "      <th>PAY_AMT3</th>\n",
              "      <th>PAY_AMT4</th>\n",
              "      <th>PAY_AMT5</th>\n",
              "      <th>PAY_AMT6</th>\n",
              "      <th>Default</th>\n",
              "      <th>PAY_TOTAL</th>\n",
              "      <th>RISK_CAT</th>\n",
              "      <th>AGE_GROUP</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>20000</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>-1</td>\n",
              "      <td>-1</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>689</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>-2</td>\n",
              "      <td>medium</td>\n",
              "      <td>young</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>120000</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>26</td>\n",
              "      <td>-1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>0</td>\n",
              "      <td>2000</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>high</td>\n",
              "      <td>young</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>90000</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>34</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>1518</td>\n",
              "      <td>1500</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>5000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>medium</td>\n",
              "      <td>young</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>50000</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>37</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>2000</td>\n",
              "      <td>2019</td>\n",
              "      <td>1200</td>\n",
              "      <td>1100</td>\n",
              "      <td>1069</td>\n",
              "      <td>1000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>medium</td>\n",
              "      <td>young</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>50000</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>57</td>\n",
              "      <td>-1</td>\n",
              "      <td>0</td>\n",
              "      <td>-1</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>2000</td>\n",
              "      <td>36681</td>\n",
              "      <td>10000</td>\n",
              "      <td>9000</td>\n",
              "      <td>689</td>\n",
              "      <td>679</td>\n",
              "      <td>0</td>\n",
              "      <td>-2</td>\n",
              "      <td>medium</td>\n",
              "      <td>middle</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 28 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "   ID  LIMIT_BAL  SEX  EDUCATION  MARRIAGE  AGE  PAY_0  PAY_2  PAY_3  PAY_4  \\\n",
              "0   1      20000    2          2         1   24      2      2     -1     -1   \n",
              "1   2     120000    2          2         2   26     -1      2      0      0   \n",
              "2   3      90000    2          2         2   34      0      0      0      0   \n",
              "3   4      50000    2          2         1   37      0      0      0      0   \n",
              "4   5      50000    1          2         1   57     -1      0     -1      0   \n",
              "\n",
              "   ...  PAY_AMT1  PAY_AMT2  PAY_AMT3  PAY_AMT4  PAY_AMT5  PAY_AMT6  Default  \\\n",
              "0  ...         0       689         0         0         0         0        1   \n",
              "1  ...         0      1000      1000      1000         0      2000        1   \n",
              "2  ...      1518      1500      1000      1000      1000      5000        0   \n",
              "3  ...      2000      2019      1200      1100      1069      1000        0   \n",
              "4  ...      2000     36681     10000      9000       689       679        0   \n",
              "\n",
              "   PAY_TOTAL  RISK_CAT  AGE_GROUP  \n",
              "0         -2    medium      young  \n",
              "1          3      high      young  \n",
              "2          0    medium      young  \n",
              "3          0    medium      young  \n",
              "4         -2    medium     middle  \n",
              "\n",
              "[5 rows x 28 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2c2ZUwBQVuCy",
        "colab_type": "code",
        "outputId": "ebcb34df-d944-4e92-f41c-9b5d36dc0b23",
        "colab": {}
      },
      "source": [
        "data.drop(columns = 'ID', axis = 1, inplace = True)\n",
        "data.head()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>LIMIT_BAL</th>\n",
              "      <th>SEX</th>\n",
              "      <th>EDUCATION</th>\n",
              "      <th>MARRIAGE</th>\n",
              "      <th>AGE</th>\n",
              "      <th>PAY_0</th>\n",
              "      <th>PAY_2</th>\n",
              "      <th>PAY_3</th>\n",
              "      <th>PAY_4</th>\n",
              "      <th>PAY_5</th>\n",
              "      <th>...</th>\n",
              "      <th>PAY_AMT1</th>\n",
              "      <th>PAY_AMT2</th>\n",
              "      <th>PAY_AMT3</th>\n",
              "      <th>PAY_AMT4</th>\n",
              "      <th>PAY_AMT5</th>\n",
              "      <th>PAY_AMT6</th>\n",
              "      <th>Default</th>\n",
              "      <th>PAY_TOTAL</th>\n",
              "      <th>RISK_CAT</th>\n",
              "      <th>AGE_GROUP</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>20000</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>-1</td>\n",
              "      <td>-1</td>\n",
              "      <td>-2</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>689</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>-2</td>\n",
              "      <td>medium</td>\n",
              "      <td>young</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>120000</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>26</td>\n",
              "      <td>-1</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>0</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>0</td>\n",
              "      <td>2000</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>high</td>\n",
              "      <td>young</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>90000</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>34</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>1518</td>\n",
              "      <td>1500</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>1000</td>\n",
              "      <td>5000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>medium</td>\n",
              "      <td>young</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>50000</td>\n",
              "      <td>2</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>37</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>2000</td>\n",
              "      <td>2019</td>\n",
              "      <td>1200</td>\n",
              "      <td>1100</td>\n",
              "      <td>1069</td>\n",
              "      <td>1000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>medium</td>\n",
              "      <td>young</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>50000</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>57</td>\n",
              "      <td>-1</td>\n",
              "      <td>0</td>\n",
              "      <td>-1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>...</td>\n",
              "      <td>2000</td>\n",
              "      <td>36681</td>\n",
              "      <td>10000</td>\n",
              "      <td>9000</td>\n",
              "      <td>689</td>\n",
              "      <td>679</td>\n",
              "      <td>0</td>\n",
              "      <td>-2</td>\n",
              "      <td>medium</td>\n",
              "      <td>middle</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 27 columns</p>\n",
              "</div>"
            ],
            "text/plain": [
              "   LIMIT_BAL  SEX  EDUCATION  MARRIAGE  AGE  PAY_0  PAY_2  PAY_3  PAY_4  \\\n",
              "0      20000    2          2         1   24      2      2     -1     -1   \n",
              "1     120000    2          2         2   26     -1      2      0      0   \n",
              "2      90000    2          2         2   34      0      0      0      0   \n",
              "3      50000    2          2         1   37      0      0      0      0   \n",
              "4      50000    1          2         1   57     -1      0     -1      0   \n",
              "\n",
              "   PAY_5  ...  PAY_AMT1  PAY_AMT2  PAY_AMT3  PAY_AMT4  PAY_AMT5  PAY_AMT6  \\\n",
              "0     -2  ...         0       689         0         0         0         0   \n",
              "1      0  ...         0      1000      1000      1000         0      2000   \n",
              "2      0  ...      1518      1500      1000      1000      1000      5000   \n",
              "3      0  ...      2000      2019      1200      1100      1069      1000   \n",
              "4      0  ...      2000     36681     10000      9000       689       679   \n",
              "\n",
              "   Default  PAY_TOTAL  RISK_CAT  AGE_GROUP  \n",
              "0        1         -2    medium      young  \n",
              "1        1          3      high      young  \n",
              "2        0          0    medium      young  \n",
              "3        0          0    medium      young  \n",
              "4        0         -2    medium     middle  \n",
              "\n",
              "[5 rows x 27 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ps1WsSFQVuC_",
        "colab_type": "text"
      },
      "source": [
        "## 3.4 Train Test Split"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KO6ArfV-Ducm",
        "colab_type": "text"
      },
      "source": [
        "We then split the orignial dataset into train and test data for model training."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YCt5RVBwVuDB",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "X = datanew\n",
        "y = datanew.iloc[:,25]\n",
        "from sklearn.model_selection import train_test_split  \n",
        "X_train_org, X_test_org, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  "
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2ZoheZ4qVuDD",
        "colab_type": "code",
        "outputId": "87c4386e-c5bd-4dbc-d762-d2c3180a049e",
        "colab": {}
      },
      "source": [
        "X_train = X_train_org.copy()\n",
        "X_test = X_test_org.copy()\n",
        "\n",
        "X_train.drop(columns = 'Default', axis = 1, inplace = True)\n",
        "X_test.drop(columns = 'Default', axis = 1, inplace = True)\n",
        "\n",
        "X_train.columns\n",
        "X_test.columns"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE_1', 'MARRIAGE_2',\n",
              "       'MARRIAGE_3', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5',\n",
              "       'PAY_6', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4',\n",
              "       'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3',\n",
              "       'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "cDYtiykwVuDF",
        "colab_type": "text"
      },
      "source": [
        "## 3.5 Resampling"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "4Fu0irotVuDH",
        "colab_type": "text"
      },
      "source": [
        "In EDA, we discovers that this is a very imbalanced dataset, that default = 1 values only counts for 22% of the whole dataset. Thus, it doesn't have enough data for models to identify features for default = 1 values.  \n",
        "we need to apply resampling methods to increase the percent of default =1 values in order to ahcieve better model training results. "
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TXShxDxSVuDH",
        "colab_type": "code",
        "outputId": "12b8a695-7764-4b17-de80-b279d7857e57",
        "colab": {}
      },
      "source": [
        "train_majority = X_train_org[X_train_org['Default'] ==0]\n",
        "train_minority = X_train_org[X_train_org['Default'] ==1]\n",
        "\n",
        "train_majority.shape\n",
        "train_minority.shape"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(5339, 26)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0WPRkAUPVuDJ",
        "colab_type": "text"
      },
      "source": [
        "### 3.5.1 Up-Sampling"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NbwuACrSFEHW",
        "colab_type": "text"
      },
      "source": [
        "By using Up-sampling method, we randomly increase the amount of minority labels(default = 1) to match the amount of majority labels(default = 0).  \n",
        "After up-sampling, the amount of both categories would equal to 18661."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "oGPNOw9RVuDM",
        "colab_type": "code",
        "outputId": "04878e25-47d5-491b-fc44-5dd161d72faa",
        "colab": {}
      },
      "source": [
        "# upsampling - increase the amount of minority labels to match majority\n",
        "from sklearn.utils import resample\n",
        "train_min_upsampled = resample(train_minority, replace =True, n_samples = 18661, random_state = 42)\n",
        "train_upsampled = pd.concat([train_min_upsampled, train_majority]).sample(frac =1,random_state = 3)\n",
        "\n",
        "train_upsampled.Default.value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    18661\n",
              "0    18661\n",
              "Name: Default, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 44
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xx5fkr-GVuDP",
        "colab_type": "code",
        "outputId": "835f77a9-7e58-493a-c601-224644f00aa8",
        "colab": {}
      },
      "source": [
        "# upsampled dataset\n",
        "train_upsampled.shape\n",
        "train_upsampled.columns\n",
        "\n",
        "X_train_up =train_upsampled.iloc[:,0:25]\n",
        "y_train_up = train_upsampled.iloc[:,25]\n",
        "\n",
        "X_train_up.shape\n",
        "y_train_up.shape"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(37322, 26)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 50
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE_1', 'MARRIAGE_2',\n",
              "       'MARRIAGE_3', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5',\n",
              "       'PAY_6', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4',\n",
              "       'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3',\n",
              "       'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6', 'Default'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 50
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(37322, 25)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 50
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(37322,)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sZ6EkPbPVuDR",
        "colab_type": "text"
      },
      "source": [
        "### 3.5.2 Down-Sampling"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1tiEp3mvFojy",
        "colab_type": "text"
      },
      "source": [
        "By using Down-sampling method, we randomly decrease the amount of majority labels(default = 0) to match the amount of minority labels(default = 1).  \n",
        "After down-sampling, the amount of both categories would equal to 5339."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZVoz-YFVVuDT",
        "colab_type": "code",
        "outputId": "3ef4a8e8-efa2-4fbb-a5d7-bf9e59c99cca",
        "colab": {}
      },
      "source": [
        "# downsampling - decrease the amount of majority labels to match minority\n",
        "train_maj_downsampled = resample(train_majority, replace =True, n_samples = 5339, random_state = 27)\n",
        "train_downsampled = pd.concat([train_maj_downsampled, train_minority]).sample(frac =1,random_state = 6)\n",
        "\n",
        "train_downsampled.Default.value_counts()"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1    5339\n",
              "0    5339\n",
              "Name: Default, dtype: int64"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 49
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rVHzYDVdVuDW",
        "colab_type": "code",
        "outputId": "04f57496-35d8-476e-de66-dc4f6a6c3e14",
        "colab": {}
      },
      "source": [
        "# downsampled dataset\n",
        "train_downsampled.shape\n",
        "train_downsampled.columns\n",
        "\n",
        "X_train_down =train_downsampled.iloc[:,0:25]\n",
        "y_train_down = train_downsampled.iloc[:,25]\n",
        "\n",
        "X_train_down.shape\n",
        "y_train_down.shape"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(10678, 26)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE_1', 'MARRIAGE_2',\n",
              "       'MARRIAGE_3', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5',\n",
              "       'PAY_6', 'BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4',\n",
              "       'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3',\n",
              "       'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6', 'Default'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(10678, 25)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(10678,)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "47gqIEcOVuDX",
        "colab_type": "text"
      },
      "source": [
        "Now we have 3 set of training dataset :   \n",
        "- original train dataset - X_train,   \n",
        "- upsampled train dataset - X_train_up,   \n",
        "- downsampled train dataset - X_train_down  \n",
        "We will use all the 3 data training dataset to train models and evaluate the results."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MEhOf15FVuDY",
        "colab_type": "text"
      },
      "source": [
        "# 4. Predictive Analysis"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EmkjZp4pjOUD",
        "colab_type": "text"
      },
      "source": [
        "Models used for making prediction:\n",
        "\n",
        "\n",
        "\n",
        "*   Logistic Regression\n",
        "*   Support Vector Machine\n",
        "*   Decision Tree\n",
        "*   Random Forest\n",
        "*   KNN\n",
        "*   Gradient Boosting Tree"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wSVkRT0PVuDY",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.metrics import accuracy_score\n",
        "from sklearn.metrics import roc_curve\n",
        "from sklearn.metrics import confusion_matrix\n",
        "from sklearn.metrics import roc_auc_score\n",
        "from sklearn.metrics import recall_score\n",
        "from sklearn.metrics import precision_score\n",
        "from sklearn.metrics import f1_score\n",
        "\n",
        "from sklearn.model_selection import GridSearchCV"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "H3VzsTGaVuDb",
        "colab_type": "text"
      },
      "source": [
        "## 4.1 Logistic Regression"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "r7zDrhWHVuDb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.model_selection import GridSearchCV\n",
        "\n",
        "logis= LogisticRegression()\n",
        "grid_param={'penalty':['l1','l2'],\n",
        "             'C':[0.01, 0.1, 1, 10, 100]}\n",
        "logis_grid = GridSearchCV(logis, grid_param, cv = 5, n_jobs = -1)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8LZIheSBVuDc",
        "colab_type": "text"
      },
      "source": [
        "### original dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pKV8RY5OVuDd",
        "colab_type": "code",
        "outputId": "70a7ad76-3f4e-4edb-ce39-f29a47d106d1",
        "colab": {}
      },
      "source": [
        "# original training dataset\n",
        "logis_grid.fit(X_train, y_train)\n",
        "print('Best Parameters- original', logis_grid.best_params_)\n",
        "pred_train = logis_grid.predict(X_train)\n",
        "pred_test = logis_grid.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=5, error_score='raise-deprecating',\n",
              "       estimator=LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
              "          intercept_scaling=1, max_iter=100, multi_class='warn',\n",
              "          n_jobs=None, penalty='l2', random_state=None, solver='warn',\n",
              "          tol=0.0001, verbose=0, warm_start=False),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'penalty': ['l1', 'l2'], 'C': [0.01, 0.1, 1, 10, 100]},\n",
              "       pre_dispatch='2*n_jobs', refit=True, return_train_score='warn',\n",
              "       scoring=None, verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 53
        },
        {
          "output_type": "stream",
          "text": [
            "Best Parameters- original {'C': 1, 'penalty': 'l1'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WKUzmFVwVuDg",
        "colab_type": "code",
        "outputId": "35c3fae7-43ea-4fe3-ddae-ccaca0afce0c",
        "colab": {}
      },
      "source": [
        "# results - original training dataset\n",
        "logis_org_train_accuracy = accuracy_score(y_train, pred_train)\n",
        "logis_org_test_accuracy = accuracy_score(y_test, pred_test)\n",
        "logis_org_train_recall = recall_score(y_train, pred_train)\n",
        "logis_org_test_recall = recall_score(y_test, pred_test)\n",
        "logis_org_train_precision = precision_score(y_train,pred_train)\n",
        "logis_org_test_precision = precision_score(y_test,pred_test)\n",
        "logis_org_train_confusion_matrix = confusion_matrix(y_train, pred_train)\n",
        "logis_org_test_confusion_matrix = confusion_matrix(y_test, pred_test)\n",
        "\n",
        "print('best score - original', logis_grid.best_score_)\n",
        "print('train accuracy: ', logis_org_train_accuracy)\n",
        "print('test accuracy: ', logis_org_test_accuracy)\n",
        "print('train recall', logis_org_train_recall)\n",
        "print('test recall: ', logis_org_test_recall)\n",
        "print('train precision: ', logis_org_train_precision)\n",
        "print('test precision: ', logis_org_test_precision)\n",
        "print('train confusion matrix: ', logis_org_train_confusion_matrix)\n",
        "print('test confusion matrix: ', logis_org_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "best score - original 0.8076666666666666\n",
            "train accuracy:  0.8080416666666667\n",
            "test accuracy:  0.8185\n",
            "train recall 0.23450084285446712\n",
            "test recall:  0.23670007710100233\n",
            "train precision:  0.7065462753950339\n",
            "test precision:  0.7561576354679803\n",
            "train confusion matrix:  [[18141   520]\n",
            " [ 4087  1252]]\n",
            "test confusion matrix:  [[4604   99]\n",
            " [ 990  307]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZObb7XQFVuDi",
        "colab_type": "text"
      },
      "source": [
        "### up-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1ylarkJhVuDi",
        "colab_type": "code",
        "outputId": "89871bec-081d-4fa9-ef01-4990e4bd5e18",
        "colab": {}
      },
      "source": [
        "# upsampled dataset\n",
        "logis_grid.fit(X_train_up, y_train_up)\n",
        "print('Best Parameters- upsampled', logis_grid.best_params_)\n",
        "pred_train_up = logis_grid.predict(X_train_up)\n",
        "pred_test_up = logis_grid.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=5, error_score='raise-deprecating',\n",
              "       estimator=LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
              "          intercept_scaling=1, max_iter=100, multi_class='warn',\n",
              "          n_jobs=None, penalty='l2', random_state=None, solver='warn',\n",
              "          tol=0.0001, verbose=0, warm_start=False),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'penalty': ['l1', 'l2'], 'C': [0.01, 0.1, 1, 10, 100]},\n",
              "       pre_dispatch='2*n_jobs', refit=True, return_train_score='warn',\n",
              "       scoring=None, verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 55
        },
        {
          "output_type": "stream",
          "text": [
            "Best Parameters- upsampled {'C': 0.01, 'penalty': 'l1'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sJ12KKZ6VuDk",
        "colab_type": "code",
        "outputId": "fbf0e51a-2d54-4d0d-8e13-585483182948",
        "colab": {}
      },
      "source": [
        "#results - upsampled training dataset\n",
        "logis_up_train_accuracy = accuracy_score(y_train_up, pred_train_up)\n",
        "logis_up_test_accuracy = accuracy_score(y_test, pred_test_up)\n",
        "logis_up_train_recall = recall_score(y_train_up, pred_train_up)\n",
        "logis_up_test_recall = recall_score(y_test, pred_test_up)\n",
        "logis_up_train_precision = precision_score(y_train_up,pred_train_up)\n",
        "logis_up_test_precision = precision_score(y_test,pred_test_up)\n",
        "logis_up_train_confusion_matrix = confusion_matrix(y_train_up, pred_train_up)\n",
        "logis_up_test_confusion_matrix = confusion_matrix(y_test, pred_test_up)\n",
        "\n",
        "print('best score - original', logis_grid.best_score_)\n",
        "print('train accuracy: ', logis_up_train_accuracy)\n",
        "print('test accuracy: ', logis_up_test_accuracy)\n",
        "print('train recall', logis_up_train_recall)\n",
        "print('test recall: ', logis_up_test_recall)\n",
        "print('train precision: ', logis_up_train_precision)\n",
        "print('test precision: ', logis_up_test_precision)\n",
        "print('train confusion matrix: ', logis_up_train_confusion_matrix)\n",
        "print('test confusion matrix: ', logis_up_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "best score - original 0.6692299448046728\n",
            "train accuracy:  0.670382080274369\n",
            "test accuracy:  0.6866666666666666\n",
            "train recall 0.6396763303145597\n",
            "test recall:  0.6399383191981496\n",
            "train precision:  0.681530117042535\n",
            "test precision:  0.3700401248328132\n",
            "train confusion matrix:  [[13083  5578]\n",
            " [ 6724 11937]]\n",
            "test confusion matrix:  [[3290 1413]\n",
            " [ 467  830]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Ziy1NXlhVuDm",
        "colab_type": "text"
      },
      "source": [
        "### down-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "__rqB_xWVuDm",
        "colab_type": "code",
        "outputId": "a936524d-ff07-4b83-c601-9839b2c3be36",
        "colab": {}
      },
      "source": [
        "# downsampled dataset\n",
        "logis_grid.fit(X_train_down, y_train_down)\n",
        "print('Best Parameters- upsampled', logis_grid.best_params_)\n",
        "pred_train_down = logis_grid.predict(X_train_down)\n",
        "pred_test_down = logis_grid.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=5, error_score='raise-deprecating',\n",
              "       estimator=LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
              "          intercept_scaling=1, max_iter=100, multi_class='warn',\n",
              "          n_jobs=None, penalty='l2', random_state=None, solver='warn',\n",
              "          tol=0.0001, verbose=0, warm_start=False),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'penalty': ['l1', 'l2'], 'C': [0.01, 0.1, 1, 10, 100]},\n",
              "       pre_dispatch='2*n_jobs', refit=True, return_train_score='warn',\n",
              "       scoring=None, verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 57
        },
        {
          "output_type": "stream",
          "text": [
            "Best Parameters- upsampled {'C': 0.1, 'penalty': 'l1'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zhs0YTZZVuDp",
        "colab_type": "code",
        "outputId": "084e5260-08e0-4f25-faec-86d73c974c28",
        "colab": {}
      },
      "source": [
        "# results - downsampled training dataset\n",
        "logis_down_train_accuracy = accuracy_score(y_train_down, pred_train_down)\n",
        "logis_down_test_accuracy = accuracy_score(y_test, pred_test_down)\n",
        "logis_down_train_recall = recall_score(y_train_down, pred_train_down)\n",
        "logis_down_test_recall = recall_score(y_test, pred_test_down)\n",
        "logis_down_train_precision = precision_score(y_train_down,pred_train_down)\n",
        "logis_down_test_precision = precision_score(y_test,pred_test_down)\n",
        "logis_down_train_confusion_matrix = confusion_matrix(y_train_down, pred_train_down)\n",
        "logis_down_test_confusion_matrix = confusion_matrix(y_test, pred_test_down)\n",
        "\n",
        "print('best score - original', logis_grid.best_score_)\n",
        "print('train accuracy: ', logis_down_train_accuracy)\n",
        "print('test accuracy: ', logis_down_test_accuracy)\n",
        "print('train recall', logis_down_train_recall)\n",
        "print('test recall: ', logis_down_test_recall)\n",
        "print('train precision: ', logis_down_train_precision)\n",
        "print('test precision: ', logis_down_test_precision)\n",
        "print('train confusion matrix: ', logis_down_train_confusion_matrix)\n",
        "print('test confusion matrix: ', logis_down_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "best score - original 0.6744708746956359\n",
            "train accuracy:  0.6758756321408503\n",
            "test accuracy:  0.6873333333333334\n",
            "train recall 0.6409439970031842\n",
            "test recall:  0.6353122590593677\n",
            "train precision:  0.6890857833266211\n",
            "test precision:  0.3700044903457566\n",
            "train confusion matrix:  [[3795 1544]\n",
            " [1917 3422]]\n",
            "test confusion matrix:  [[3300 1403]\n",
            " [ 473  824]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qKYY0xdfryQd",
        "colab_type": "text"
      },
      "source": [
        "## 4.2 SVM"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kLxeNLJSr2wd",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.svm import SVC\n"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IkRSqEDBsdMh",
        "colab_type": "text"
      },
      "source": [
        "### original dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4Z4AXmZnsgcx",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# original dataset\n",
        "svc = SVC()\n",
        "svc.fit(X_train, y_train)\n",
        "\n",
        "print(\"Accuracy on training set: {:.2f}\".format(svc.score(X_train, y_train)))\n",
        "print(\"Accuracy on test set: {:.2f}\".format(svc.score(X_test, y_test)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2axlWufesjoe",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "print('Model Performance Of SVM')\n",
        "\n",
        "predictions = svc.predict(X_test)\n",
        "\n",
        "print(\"-------------\")\n",
        "TP = np.sum(np.logical_and(predictions == 1, y_test == 1))\n",
        "TN = np.sum(np.logical_and(predictions == 0, y_test == 0))\n",
        "FP = np.sum(np.logical_and(predictions == 1, y_test == 0))\n",
        "FN = np.sum(np.logical_and(predictions == 0, y_test == 1))\n",
        "pred = len(predictions)\n",
        "\n",
        "print('True Positives: {}'.format(TP))\n",
        "print('False Positive: {}'.format(FP))\n",
        "print('True Negative: {}'.format(TN))\n",
        "print('False Negative: {}'.format(FN))\n",
        "\n",
        "\n",
        "print(\"Accuracy: {}\".format(round(accuracy_score(y_true = y_test, y_pred = predictions),3)))\n",
        "print('Precision: {}'.format(round(TP/(TP+FP),2)))\n",
        "print('Recall: {}'.format(round(TP/(TP+FN),2)))\n",
        "print('Problematic ratio: {}'.format(round(FN/(FN+TP),2)))\n",
        "print('AUC Score: {}'.format(roc_auc_score(y_test, predictions)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "j2D-dtwOtAoZ",
        "colab_type": "text"
      },
      "source": [
        "### up-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "evTpKLUetFr4",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# up-sampled dataset\n",
        "svc = SVC()\n",
        "svc.fit(X_train_up, y_train_up)\n",
        "\n",
        "print(\"Accuracy on training set: {:.2f}\".format(svc.score(X_train_up, y_train_up)))\n",
        "print(\"Accuracy on test set: {:.2f}\".format(svc.score(X_test, y_test)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bexhT7qEtKqB",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "print('Model Performance Of SVM')\n",
        "\n",
        "predictions = svc.predict(X_test)\n",
        "\n",
        "print(\"-------------\")\n",
        "TP = np.sum(np.logical_and(predictions == 1, y_test == 1))\n",
        "TN = np.sum(np.logical_and(predictions == 0, y_test == 0))\n",
        "FP = np.sum(np.logical_and(predictions == 1, y_test == 0))\n",
        "FN = np.sum(np.logical_and(predictions == 0, y_test == 1))\n",
        "pred = len(predictions)\n",
        "\n",
        "print('True Positives: {}'.format(TP))\n",
        "print('False Positive: {}'.format(FP))\n",
        "print('True Negative: {}'.format(TN))\n",
        "print('False Negative: {}'.format(FN))\n",
        "\n",
        "\n",
        "print(\"Accuracy: {}\".format(round(accuracy_score(y_true = y_test, y_pred = predictions),3)))\n",
        "print('Precision: {}'.format(round(TP/(TP+FP),2)))\n",
        "print('Recall: {}'.format(round(TP/(TP+FN),2)))\n",
        "print('Problematic ratio: {}'.format(round(FN/(FN+TP),2)))\n",
        "print('AUC Score: {}'.format(roc_auc_score(y_test, predictions)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qlrgCpI-tVKY",
        "colab_type": "text"
      },
      "source": [
        "### down-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "c5cfXhzutYt-",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "# down-sampled dataset\n",
        "svc = SVC()\n",
        "svc.fit(X_train_down, y_train_down)\n",
        "\n",
        "print(\"Accuracy on training set: {:.2f}\".format(svc.score(X_train_down, y_train_down)))\n",
        "print(\"Accuracy on test set: {:.2f}\".format(svc.score(X_test, y_test)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RAazMb0OtxBv",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "print('Model Performance Of SVM')\n",
        "\n",
        "predictions = svc.predict(X_test)\n",
        "\n",
        "print(\"-------------\")\n",
        "TP = np.sum(np.logical_and(predictions == 1, y_test == 1))\n",
        "TN = np.sum(np.logical_and(predictions == 0, y_test == 0))\n",
        "FP = np.sum(np.logical_and(predictions == 1, y_test == 0))\n",
        "FN = np.sum(np.logical_and(predictions == 0, y_test == 1))\n",
        "pred = len(predictions)\n",
        "\n",
        "print('True Positives: {}'.format(TP))\n",
        "print('False Positive: {}'.format(FP))\n",
        "print('True Negative: {}'.format(TN))\n",
        "print('False Negative: {}'.format(FN))\n",
        "\n",
        "\n",
        "print(\"Accuracy: {}\".format(round(accuracy_score(y_true = y_test, y_pred = predictions),3)))\n",
        "print('Precision: {}'.format(round(TP/(TP+FP),2)))\n",
        "print('Recall: {}'.format(round(TP/(TP+FN),2)))\n",
        "print('Problematic ratio: {}'.format(round(FN/(FN+TP),2)))\n",
        "print('AUC Score: {}'.format(roc_auc_score(y_test, predictions)))"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "XrUEx7rkVuDr",
        "colab_type": "text"
      },
      "source": [
        "## 4.3 Decision Tree"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ByDb9CelVuDr",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.tree import DecisionTreeClassifier\n",
        "dt = DecisionTreeClassifier()\n",
        "grid_param = {'max_depth':[1, 2, 3, 4, 5, 6, 7, 11, 19]}\n",
        "dt_grid = GridSearchCV(dt, grid_param, cv = 5, n_jobs = -1)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "jcglW3ZnVuDu",
        "colab_type": "text"
      },
      "source": [
        "### original dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UZdLDtNOVuDu",
        "colab_type": "code",
        "outputId": "d3167c27-8a97-4a85-e7b4-c58ce5e93174",
        "colab": {}
      },
      "source": [
        "# original training dataset\n",
        "dt_grid.fit(X_train, y_train)\n",
        "print('Best Parameters- original', dt_grid.best_params_)\n",
        "pred_train = dt_grid.predict(X_train)\n",
        "pred_test = dt_grid.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=5, error_score='raise-deprecating',\n",
              "       estimator=DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,\n",
              "            max_features=None, max_leaf_nodes=None,\n",
              "            min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "            min_samples_leaf=1, min_samples_split=2,\n",
              "            min_weight_fraction_leaf=0.0, presort=False, random_state=None,\n",
              "            splitter='best'),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'max_depth': [1, 2, 3, 4, 5, 6, 7, 11, 19]},\n",
              "       pre_dispatch='2*n_jobs', refit=True, return_train_score='warn',\n",
              "       scoring=None, verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 60
        },
        {
          "output_type": "stream",
          "text": [
            "Best Parameters- original {'max_depth': 3}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tRaP1YPmVuDw",
        "colab_type": "code",
        "outputId": "558f42fa-de89-4b70-d01c-e52df24b2553",
        "colab": {}
      },
      "source": [
        "# results - original training dataset\n",
        "dt_org_train_accuracy = accuracy_score(y_train, pred_train)\n",
        "dt_org_test_accuracy = accuracy_score(y_test, pred_test)\n",
        "dt_org_train_recall = recall_score(y_train, pred_train)\n",
        "dt_org_test_recall = recall_score(y_test, pred_test)\n",
        "dt_org_train_precision = precision_score(y_train,pred_train)\n",
        "dt_org_test_precision = precision_score(y_test,pred_test)\n",
        "dt_org_train_confusion_matrix = confusion_matrix(y_train, pred_train)\n",
        "dt_org_test_confusion_matrix = confusion_matrix(y_test, pred_test)\n",
        "\n",
        "print('best score - original', dt_grid.best_score_)\n",
        "print('train accuracy: ', dt_org_train_accuracy)\n",
        "print('test accuracy: ', dt_org_test_accuracy)\n",
        "print('train recall', dt_org_train_recall)\n",
        "print('test recall: ', dt_org_test_recall)\n",
        "print('train precision: ', dt_org_train_precision)\n",
        "print('test precision: ', dt_org_test_precision)\n",
        "print('train confusion matrix: ', dt_org_train_confusion_matrix)\n",
        "print('test confusion matrix: ', dt_org_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "best score - original 0.8194166666666667\n",
            "train accuracy:  0.82025\n",
            "test accuracy:  0.8263333333333334\n",
            "train recall 0.364862333770369\n",
            "test recall:  0.361603700848111\n",
            "train precision:  0.6785092302333682\n",
            "test precision:  0.6866764275256223\n",
            "train confusion matrix:  [[17738   923]\n",
            " [ 3391  1948]]\n",
            "test confusion matrix:  [[4489  214]\n",
            " [ 828  469]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kXzvwwOQVuDy",
        "colab_type": "text"
      },
      "source": [
        "###  up-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "EQrmY9ARVuDy",
        "colab_type": "code",
        "outputId": "b69ceb24-d40f-40b6-b1b5-b895f38516a2",
        "colab": {}
      },
      "source": [
        "# upsampled dataset\n",
        "dt_grid.fit(X_train_up, y_train_up)\n",
        "print('Best Parameters- upsampled', dt_grid.best_params_)\n",
        "pred_train_up = dt_grid.predict(X_train_up)\n",
        "pred_test_up = dt_grid.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=5, error_score='raise-deprecating',\n",
              "       estimator=DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,\n",
              "            max_features=None, max_leaf_nodes=None,\n",
              "            min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "            min_samples_leaf=1, min_samples_split=2,\n",
              "            min_weight_fraction_leaf=0.0, presort=False, random_state=None,\n",
              "            splitter='best'),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'max_depth': [1, 2, 3, 4, 5, 6, 7, 11, 19]},\n",
              "       pre_dispatch='2*n_jobs', refit=True, return_train_score='warn',\n",
              "       scoring=None, verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 62
        },
        {
          "output_type": "stream",
          "text": [
            "Best Parameters- upsampled {'max_depth': 19}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Gv8SvT7VVuD2",
        "colab_type": "code",
        "outputId": "215c08a7-2d2d-4818-972b-ff267cf8e7c0",
        "colab": {}
      },
      "source": [
        "# results - upsampled training dataset\n",
        "dt_up_train_accuracy = accuracy_score(y_train_up, pred_train_up)\n",
        "dt_up_test_accuracy = accuracy_score(y_test, pred_test_up)\n",
        "dt_up_train_recall = recall_score(y_train_up, pred_train_up)\n",
        "dt_up_test_recall = recall_score(y_test, pred_test_up)\n",
        "dt_up_train_precision = precision_score(y_train_up,pred_train_up)\n",
        "dt_up_test_precision = precision_score(y_test,pred_test_up)\n",
        "dt_up_train_confusion_matrix = confusion_matrix(y_train_up, pred_train_up)\n",
        "dt_up_test_confusion_matrix = confusion_matrix(y_test, pred_test_up)\n",
        "\n",
        "print('best score - original', dt_grid.best_score_)\n",
        "print('train accuracy: ', dt_up_train_accuracy)\n",
        "print('test accuracy: ', dt_up_test_accuracy)\n",
        "print('train recall', dt_up_train_recall)\n",
        "print('test recall: ', dt_up_test_recall)\n",
        "print('train precision: ', dt_up_train_precision)\n",
        "print('test precision: ', dt_up_test_precision)\n",
        "print('train confusion matrix: ', dt_up_train_confusion_matrix)\n",
        "print('test confusion matrix: ', dt_up_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "best score - original 0.8486683457478164\n",
            "train accuracy:  0.9494935962702964\n",
            "test accuracy:  0.7283333333333334\n",
            "train recall 0.9668828037082686\n",
            "test recall:  0.48727833461835\n",
            "train precision:  0.9343863283272915\n",
            "test precision:  0.39574201628052597\n",
            "train confusion matrix:  [[17394  1267]\n",
            " [  618 18043]]\n",
            "test confusion matrix:  [[3738  965]\n",
            " [ 665  632]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "nlugmUVhVuD4",
        "colab_type": "text"
      },
      "source": [
        "### down-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "g02N0KoaVuD4",
        "colab_type": "code",
        "outputId": "09013ed8-b6ca-442a-fa77-22f5ba4c3582",
        "colab": {}
      },
      "source": [
        "# downsampled dataset\n",
        "dt_grid.fit(X_train_down, y_train_down)\n",
        "print('Best Parameters- upsampled', dt_grid.best_params_)\n",
        "pred_train_down = dt_grid.predict(X_train_down)\n",
        "pred_test_down = dt_grid.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=5, error_score='raise-deprecating',\n",
              "       estimator=DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,\n",
              "            max_features=None, max_leaf_nodes=None,\n",
              "            min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "            min_samples_leaf=1, min_samples_split=2,\n",
              "            min_weight_fraction_leaf=0.0, presort=False, random_state=None,\n",
              "            splitter='best'),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'max_depth': [1, 2, 3, 4, 5, 6, 7, 11, 19]},\n",
              "       pre_dispatch='2*n_jobs', refit=True, return_train_score='warn',\n",
              "       scoring=None, verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 64
        },
        {
          "output_type": "stream",
          "text": [
            "Best Parameters- upsampled {'max_depth': 4}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MEMFfNZdVuD6",
        "colab_type": "code",
        "outputId": "fc6f097f-027e-488c-d056-b1ba50379638",
        "colab": {}
      },
      "source": [
        "# results - downsampled training dataset\n",
        "dt_down_train_accuracy = accuracy_score(y_train_down, pred_train_down)\n",
        "dt_down_test_accuracy = accuracy_score(y_test, pred_test_down)\n",
        "dt_down_train_recall = recall_score(y_train_down, pred_train_down)\n",
        "dt_down_test_recall = recall_score(y_test, pred_test_down)\n",
        "dt_down_train_precision = precision_score(y_train_down,pred_train_down)\n",
        "dt_down_test_precision = precision_score(y_test,pred_test_down)\n",
        "dt_down_train_confusion_matrix = confusion_matrix(y_train_down, pred_train_down)\n",
        "dt_down_test_confusion_matrix = confusion_matrix(y_test, pred_test_down)\n",
        "\n",
        "print('best score - original', dt_grid.best_score_)\n",
        "print('train accuracy: ', dt_down_train_accuracy)\n",
        "print('test accuracy: ', dt_down_test_accuracy)\n",
        "print('train recall', dt_down_train_recall)\n",
        "print('test recall: ', dt_down_test_recall)\n",
        "print('train precision: ', dt_down_train_precision)\n",
        "print('test precision: ', dt_down_test_precision)\n",
        "print('train confusion matrix: ', dt_down_train_confusion_matrix)\n",
        "print('test confusion matrix: ', dt_down_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "best score - original 0.6990073047387151\n",
            "train accuracy:  0.7055628394830492\n",
            "test accuracy:  0.7726666666666666\n",
            "train recall 0.5909346319535493\n",
            "test recall:  0.5859676175790285\n",
            "train precision:  0.7667071688942891\n",
            "test precision:  0.4788909892879647\n",
            "train confusion matrix:  [[4379  960]\n",
            " [2184 3155]]\n",
            "test confusion matrix:  [[3876  827]\n",
            " [ 537  760]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "g8K4zaGVVuD9",
        "colab_type": "text"
      },
      "source": [
        "## 4.4 Random Forest"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ojTD-p6GVuD9",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.ensemble import RandomForestClassifier\n",
        "\n",
        "param_grid = {'n_estimators':[100, 150, 200],\n",
        "             'max_depth': [5, 15, 20, 30],\n",
        "             'max_leaf_nodes': [8, 10, 14, 18, 20]}\n",
        "\n",
        "rnd_clf = RandomForestClassifier()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "_-fXPGKBVuD-",
        "colab_type": "text"
      },
      "source": [
        "### original dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JfeAPvauVuD_",
        "colab_type": "code",
        "outputId": "2cafa565-0a0e-4b48-8435-818cc7900a52",
        "colab": {}
      },
      "source": [
        "# original training dataset\n",
        "rnd_grid = GridSearchCV(rnd_clf, param_grid, cv=5, n_jobs=-1, scoring ='roc_auc', return_train_score = True)\n",
        "rnd_grid.fit(X_train, y_train)\n",
        "\n",
        "print('Best Parameters- original', rnd_grid.best_params_)\n",
        "pred_train = rnd_grid.predict(X_train)\n",
        "pred_test = rnd_grid.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=5, error_score='raise-deprecating',\n",
              "       estimator=RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',\n",
              "            max_depth=None, max_features='auto', max_leaf_nodes=None,\n",
              "            min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "            min_samples_leaf=1, min_samples_split=2,\n",
              "            min_weight_fraction_leaf=0.0, n_estimators='warn', n_jobs=None,\n",
              "            oob_score=False, random_state=None, verbose=0,\n",
              "            warm_start=False),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'n_estimators': [100, 150, 200], 'max_depth': [5, 15, 20, 30], 'max_leaf_nodes': [8, 10, 14, 18, 20]},\n",
              "       pre_dispatch='2*n_jobs', refit=True, return_train_score=True,\n",
              "       scoring='roc_auc', verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 67
        },
        {
          "output_type": "stream",
          "text": [
            "Best Parameters- original {'max_depth': 30, 'max_leaf_nodes': 20, 'n_estimators': 100}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hbDHU_BjVuEB",
        "colab_type": "code",
        "outputId": "253cc619-72ac-4d77-9dc4-0e0cfdf39e55",
        "colab": {}
      },
      "source": [
        "# results - original training dataset\n",
        "rnd_org_train_accuracy = accuracy_score(y_train, pred_train)\n",
        "rnd_org_test_accuracy = accuracy_score(y_test, pred_test)\n",
        "rnd_org_train_recall = recall_score(y_train, pred_train)\n",
        "rnd_org_test_recall = recall_score(y_test, pred_test)\n",
        "rnd_org_train_precision = precision_score(y_train,pred_train)\n",
        "rnd_org_test_precision = precision_score(y_test,pred_test)\n",
        "rnd_org_train_confusion_matrix = confusion_matrix(y_train, pred_train)\n",
        "rnd_org_test_confusion_matrix = confusion_matrix(y_test, pred_test)\n",
        "\n",
        "print('best score - original', rnd_grid.best_score_)\n",
        "print('train accuracy: ', rnd_org_train_accuracy)\n",
        "print('test accuracy: ', rnd_org_test_accuracy)\n",
        "print('train recall',  rnd_org_train_recall)\n",
        "print('test recall: ', rnd_org_test_recall)\n",
        "print('train precision: ', rnd_org_train_precision)\n",
        "print('test precision: ', rnd_org_test_precision)\n",
        "print('train confusion matrix: ',  rnd_org_train_confusion_matrix)\n",
        "print('test confusion matrix: ', rnd_org_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "best score - original 0.7741674041633684\n",
            "train accuracy:  0.8210416666666667\n",
            "test accuracy:  0.8293333333333334\n",
            "train recall 0.35830679902603485\n",
            "test recall:  0.361603700848111\n",
            "train precision:  0.6876347951114307\n",
            "test precision:  0.7052631578947368\n",
            "train confusion matrix:  [[17792   869]\n",
            " [ 3426  1913]]\n",
            "test confusion matrix:  [[4507  196]\n",
            " [ 828  469]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aADPRIu2VuEE",
        "colab_type": "text"
      },
      "source": [
        "### up-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uQV8C8YeVuEF",
        "colab_type": "code",
        "outputId": "ef0ff0fc-6899-49c2-f71f-b02ec0c361be",
        "colab": {}
      },
      "source": [
        "# upsampled dataset\n",
        "rnd_grid_up = GridSearchCV(rnd_clf, param_grid, cv=5, n_jobs=-1, scoring ='roc_auc', return_train_score = True)\n",
        "rnd_grid_up.fit(X_train_up, y_train_up)\n",
        "print('Best Parameters- upsampled', rnd_grid_up.best_params_)\n",
        "pred_train_up = rnd_grid_up.predict(X_train_up)\n",
        "pred_test_up = rnd_grid_up.predict(X_test)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=5, error_score='raise-deprecating',\n",
              "       estimator=RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',\n",
              "            max_depth=None, max_features='auto', max_leaf_nodes=None,\n",
              "            min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "            min_samples_leaf=1, min_samples_split=2,\n",
              "            min_weight_fraction_leaf=0.0, n_estimators='warn', n_jobs=None,\n",
              "            oob_score=False, random_state=None, verbose=0,\n",
              "            warm_start=False),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'n_estimators': [100, 150, 200], 'max_depth': [5, 15, 20, 30], 'max_leaf_nodes': [8, 10, 14, 18, 20]},\n",
              "       pre_dispatch='2*n_jobs', refit=True, return_train_score=True,\n",
              "       scoring='roc_auc', verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 70
        },
        {
          "output_type": "stream",
          "text": [
            "Best Parameters- upsampled {'max_depth': 20, 'max_leaf_nodes': 20, 'n_estimators': 200}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "f5kJPPGVVuEJ",
        "colab_type": "code",
        "outputId": "76232557-582a-41ba-a58f-3590b239a2cf",
        "colab": {}
      },
      "source": [
        "# results - upsampled training dataset\n",
        "rnd_up_train_accuracy = accuracy_score(y_train_up, pred_train_up)\n",
        "rnd_up_test_accuracy = accuracy_score(y_test, pred_test_up)\n",
        "rnd_up_train_recall = recall_score(y_train_up, pred_train_up)\n",
        "rnd_up_test_recall = recall_score(y_test, pred_test_up)\n",
        "rnd_up_train_precision = precision_score(y_train_up,pred_train_up)\n",
        "rnd_up_test_precision = precision_score(y_test,pred_test_up)\n",
        "rnd_up_train_confusion_matrix = confusion_matrix(y_train_up, pred_train_up)\n",
        "rnd_up_test_confusion_matrix = confusion_matrix(y_test, pred_test_up)\n",
        "\n",
        "print('best score - original', rnd_grid.best_score_)\n",
        "print('train accuracy: ', rnd_up_train_accuracy)\n",
        "print('test accuracy: ', rnd_up_test_accuracy)\n",
        "print('train recall',  rnd_up_train_recall)\n",
        "print('test recall: ', rnd_up_test_recall)\n",
        "print('train precision: ', rnd_up_train_precision)\n",
        "print('test precision: ', rnd_up_test_precision)\n",
        "print('train confusion matrix: ',  rnd_up_train_confusion_matrix)\n",
        "print('test confusion matrix: ', rnd_up_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "best score - original 0.7741674041633684\n",
            "train accuracy:  0.721076040941\n",
            "test accuracy:  0.7615\n",
            "train recall 0.6443384598896094\n",
            "test recall:  0.6245181187355435\n",
            "train precision:  0.761157181743369\n",
            "test precision:  0.4618015963511973\n",
            "train confusion matrix:  [[14888  3773]\n",
            " [ 6637 12024]]\n",
            "test confusion matrix:  [[3759  944]\n",
            " [ 487  810]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "svRw0pJlVuEL",
        "colab_type": "text"
      },
      "source": [
        "### down-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DqyeKVx5VuEM",
        "colab_type": "code",
        "outputId": "0d136ac7-845b-4d0b-ed1e-185895bd3e81",
        "colab": {}
      },
      "source": [
        "# downsampled dataset\n",
        "rnd_grid_down = GridSearchCV(rnd_clf, param_grid, cv=5, n_jobs=-1, scoring ='roc_auc', return_train_score = True)\n",
        "rnd_grid_down.fit(X_train_down, y_train_down)\n",
        "pred_train_down = rnd_grid_down.predict(X_train_down)\n",
        "pred_test_down = rnd_grid_down.predict(X_test)\n",
        "\n",
        "print('Best Parameters- upsampled', rnd_grid_down.best_params_)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=5, error_score='raise-deprecating',\n",
              "       estimator=RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',\n",
              "            max_depth=None, max_features='auto', max_leaf_nodes=None,\n",
              "            min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "            min_samples_leaf=1, min_samples_split=2,\n",
              "            min_weight_fraction_leaf=0.0, n_estimators='warn', n_jobs=None,\n",
              "            oob_score=False, random_state=None, verbose=0,\n",
              "            warm_start=False),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'n_estimators': [100, 150, 200], 'max_depth': [5, 15, 20, 30], 'max_leaf_nodes': [8, 10, 14, 18, 20]},\n",
              "       pre_dispatch='2*n_jobs', refit=True, return_train_score=True,\n",
              "       scoring='roc_auc', verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 72
        },
        {
          "output_type": "stream",
          "text": [
            "Best Parameters- upsampled {'max_depth': 20, 'max_leaf_nodes': 20, 'n_estimators': 150}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VZOOF8QVVuEN",
        "colab_type": "code",
        "outputId": "26f47e51-a8f6-4556-f244-02712f022c99",
        "colab": {}
      },
      "source": [
        "# results - downsampled training dataset\n",
        "rnd_down_train_accuracy = accuracy_score(y_train_down, pred_train_down)\n",
        "rnd_down_test_accuracy = accuracy_score(y_test, pred_test_down)\n",
        "rnd_down_train_recall = recall_score(y_train_down, pred_train_down)\n",
        "rnd_down_test_recall = recall_score(y_test, pred_test_down)\n",
        "rnd_down_train_precision = precision_score(y_train_down,pred_train_down)\n",
        "rnd_down_test_precision = precision_score(y_test,pred_test_down)\n",
        "rnd_down_train_confusion_matrix = confusion_matrix(y_train_down, pred_train_down)\n",
        "rnd_down_test_confusion_matrix = confusion_matrix(y_test, pred_test_down)\n",
        "\n",
        "print('best score - original', rnd_grid.best_score_)\n",
        "print('train accuracy: ', rnd_down_train_accuracy)\n",
        "print('test accuracy: ', rnd_down_test_accuracy)\n",
        "print('train recall',  rnd_down_train_recall)\n",
        "print('test recall: ', rnd_down_test_recall)\n",
        "print('train precision: ', rnd_down_train_precision)\n",
        "print('test precision: ', rnd_down_test_precision)\n",
        "print('train confusion matrix: ',  rnd_down_train_confusion_matrix)\n",
        "print('test confusion matrix: ', rnd_down_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "best score - original 0.7741674041633684\n",
            "train accuracy:  0.7247611912343136\n",
            "test accuracy:  0.7638333333333334\n",
            "train recall 0.6300805394268589\n",
            "test recall:  0.6114109483423285\n",
            "train precision:  0.777264325323475\n",
            "test precision:  0.46483001172332944\n",
            "train confusion matrix:  [[4375  964]\n",
            " [1975 3364]]\n",
            "test confusion matrix:  [[3790  913]\n",
            " [ 504  793]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rMut7RY1VuEP",
        "colab_type": "text"
      },
      "source": [
        "### Feature Importance"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "99ZrW82sVuEP",
        "colab_type": "code",
        "outputId": "47f6ce3e-abd1-480e-9f30-806274b11020",
        "colab": {}
      },
      "source": [
        "# original\n",
        "rnd_org = RandomForestClassifier(max_leaf_nodes =20, max_depth=20, n_estimators=200,random_state = 20).fit(X_train, y_train)\n",
        "feat_importances = pd.Series(rnd_org.feature_importances_, index=X_train.columns)\n",
        "feat_importances.nlargest(20).plot(kind='barh')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x1a26606518>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 74
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZUAAAD0CAYAAABThLtwAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvIxREBQAAIABJREFUeJzt3X1cVHXe//HXgIguxKIrFrlZ3oSYxmbuY9Usb1DD2zAM0R2mvdRMS+VSsiCNRCVv4iE+Sl1YK9QdwJuxQC6JMMn00pSrJsxH3pTRpS3az5tMCeLOOL8/vDjrBMIMDoc59Hn+tZyZOfM+57GPvs453+/7GBRFURBCCCGcwK2lAwghhGg9ZFARQgjhNDKoCCGEcBoZVIQQQjiNDCpCCCGcRgYVIYQQTtOmpQO0JKvV2tIRhBBCl/r371/v9t/0oAK3PjGu7uTJk/Tu3bulYzhMcmtPr9klt/bszd7QP8jl8pcQQginafSXSkFBAfPnz6dnz54oikJVVRXx8fHk5+fTqVMnpk6dyuDBgzl06JDN59atW6e+bq/4+HiOHj1KVlaWus1kMnH58mVyc3PVbXv27GHevHnk5+ezdu1aLl68yLlz5/Dw8KBz584EBAQQFxfHP/7xDz766COqq6uZOnUq4eHhdb7zvtgcAM6sGmd3TiGEEPWz6/LXwIEDWbt2LQAHDx7kjTfeoG/fvk4NUl5ejtVqJSAggIKCAgYMGGDz+s0/y3JycujSpQsAa9asAeoOYgUFBRQWFrJ161bKy8tJTU11al4hhBB1OXxPpaSkhI4dOzo9SG5uLoMGDWLIkCGkp6fbDCrjxo1j9+7d9O7dm5KSEiorK+nUqVOD+zt48CABAQHMmTOH0tJSXnrppQbff/LkSacch1YqKip0lxkkd0vQa3bJrT1nZLdrUDly5Agmk4mqqipOnTrFhg0bKCwsvK0v/jWLxcKyZcvo0aMH8fHxXLhwgTvvvBOA4OBgYmJiWLhwIXl5eYwePZqMjIwG9/fjjz9y/vx5UlJSKC4u5rnnnuODDz7AYDDU+3693VjT681Aya09vWaX3NrT7Eb9wIEDMZvNbN++nczMTKKjo6moqLA/aSOKioo4ffo0q1atYubMmRgMBrZu3aq+7unpSe/evSksLGTv3r2MGjWq0X36+vry6KOP0rZtW7p3746npydXrlxxWmYhhBB1OXz5q7HLTk1hsVhYsGABRqMRgPPnzxMREcHzzz+vvmf8+PFs3rwZHx8fvLy8Gt1n//79+ec//8m0adO4ePEi5eXl+Pr61nmf3KAXQgjncejyl5ubG2VlZcTGxnLu3Dn19atXrxIWFqb+PX36dAA2btyIxWIBwMvLC7PZXGffVVVV7N69m+zsbHXb3XffTWBgIHl5eeq2Rx55hNjYWFauXGnXgQ0fPpxPP/2Up556CkVRePXVV3F3d7frs0IIIZrG8Ft+SJfVapXFjxqT3NrTa3bJrT1H7qm4xIr6uXPncu3aNZtt3t7eJCcnaxlDCCFEM9F0UFm/fr2WXyeEEEJjuun+euutt9iyZQv5+fl4enoCNxZBpqenA+Du7k5gYCAvvvgibdu2JTg4GH9/f9zc/j3BLSYmps6iTVlRL4QQzqObQSU7O5uxY8eSk5NDWFgY+/fvZ8eOHaSkpODj44OiKKxcuZKsrCwmT54MQGpqqjoACSGEaH66KJQsKCiga9euTJkyRf1lYjabeemll/Dx8QHAYDDw8ssvqwOKEEII7enil4rFYiE8PJzu3bvTtm1bvvjiC4qLi7n33nsBKCwsJCkpierqavz9/dWesunTp6uXv9zc3NiyZcstv0NvtQp6rYKQ3NrTa3bJrT3Nalpa0rVr1zhw4ABXrlzBbDZTWlpKWloa/v7+FBcXExgYSL9+/TCbzRQVFREfH69+1pHLX3qbAqjXaYuSW3t6zS65tfebeJ5KdnY2kyZNIjU1lXfeeYcdO3Zw6NAhnnjiCV5//XV++ukn9b3/8z//04JJhRBCuPwvFYvFwuuvv67+3b59ex5//HEuXLhgU+VSVlZGz549Wb58ufremy9/ATz99NN1esNk1pcQQjiPyw8qN9e31Lr5EldISEi9n/voo4+aK5IQQohbcPnLX0IIIfRDBhUhhBBOI4OKEEIIp3H5eyrNrbamBeSmvRBC3K5Gf6kUFBQwaNAgTCYTkZGRTJ48mRMnTrBu3Tr16YyDBw+u87mbX7dXfHw8EydOtNlmMpkYM2aMzbY9e/bQq1cviouLeeGFFzCZTAQHBxMSEoLJZLKZAfbDDz8wdOhQioqKHMoihBDCcXb9Uhk4cKC6Sv3gwYO88cYbdYoZb1d5eTlWq5WAgAAKCgoYMGCAzes3L8rJycmhS5cuAKxZswa4MYh16tSJqVOnqp+prq7m1VdfpV27dk7NKoQQon4OX/4qKSmhY8eOTg+Sm5vLoEGDGDJkCOnp6TaDyrhx49i9eze9e/empKSEyspKux5rvHr1aqZMmcLGjRvtyqCnagW9VkFIbu3pNbvk1p5mNS21jxOuqqri1KlTbNiwgcLCwtv64l+zWCwsW7aMHj16EB8fz4ULF7jzzjsBCA4OJiYmhoULF5KXl8fo0aPJyMhocH/vvfceHTt25LHHHrN7UNFTtYJeqyAkt/b0ml1ya0+zmpaBAwdiNpvZvn07mZmZREdHU1FRYX/SRhQVFXH69GlWrVrFzJkzMRgMNvdjPD096d27N4WFhezdu7fOqvj6vPvuu3zyySeYTCZOnjxJTEwMly5dclpmIYQQdTl8+cuey06OslgsLFiwAKPRCMD58+dtKlgAxo8fz+bNm/Hx8cHLy6vRfdZW5MONm/3x8fH4+fnVeZ/M+BJCCOdx6PKXm5sbZWVlxMbGcu7cOfX1q1evEhYWpv49ffp0ADZu3IjFYgHAy8sLs9lcZ99VVVXs3r3bpo7l7rvvJjAwkLy8PHXbI488QmxsLCtXrnTwEIUQQmjFoCiK0tIhWorVaqV///4tHaNJ9HrdVnJrT6/ZJbf2HLmncqv/dmq6+HHu3Llcu3bNZpu3tzfJyclaxhBCCNFMNB1U1q9fr+XXCSGE0JjUtNxU0wJy414IIW5Ho4NKQUEB8+fPp2fPniiKQlVVFfHx8eTn56sr2AcPHsyhQ4dsPlffCvfGxMfHc/ToUbKystRtJpOJy5cvk5ubq27bs2cP8+bNIz8/n7Vr13Lx4kXOnTuHh4cHnTt3JiAggEWLFvHKK6/wv//7vxgMBpYuXUpAQIDdWYQQQjiu1da07N27F4Bt27ZRUFDA2rVr5d6NEEI0s1Zb0zJy5EiGDRsG3Fj34uPjY1cOvdQr6LUKQnJrT6/ZJbf2pKalEW3atCEmJoYPP/yQN998064cepkKqNdpi5Jbe3rNLrm1JzUtdli9ejV5eXnExcXx888/Oy2zEEKIulptTUtWVhYXLlxg1qxZtG/fHoPBgJtb3TFUZnsJIYTztNqalscff5yXX34Zo9HI9evXWbRokTxXRQghmpnUtEhNi6Ykt/b0ml1ya09qWoQQQrgUqWkRQgjhNK12RX1cXBxPPvkk3t7eAPzxj3+s936M1LQIIYTztNoV9ZWVlSiKUu/kACGEEM3DrnUqN2vuFfVPPvmkzVMb4d8r6mu/354V9adOnaK8vJzp06fz9NNPc/ToUadnFkIIYavVrqhv164dM2bMIDw8nDNnzjBz5kw++OAD2rRp+JD1Uq+g1yoIya09vWaX3NrTrKbl5stf3377LVOmTCE8PPy2vvhmN6+oB9QV9fPnzwfqrqhPSkpqdFDp1q0b9957LwaDgW7duuHr68ulS5fw9/dv8HN6mQqo12mLklt7es0uubXnjJqWVruifufOnXz99dfqr57S0lL8/Pycnl0IIcS/tdoV9U899RQvv/wyU6dOxWAwsGLFinovfclsLyGEcB5ZUS8r6jUlubWn1+ySW3uyol4IIYRLkRX1QgghnMbhdSpCCCHErThU0wI3VqpPmDABk8kEQGhoKA8//DBLliwBIC0tjX379vHOO++o+5g3bx6DBg3ir3/96y2/p7KykuDgYKZNm8YzzzwDQHFxMSNGjOCFF17g2WefVd87e/ZsysrKeOWVV0hISADg6NGjBAUF4ebmxowZM+jcuTOzZs3ivvvuA2Dq1KmMHTu2zvf+uqalltzAF0IIxzm8TqWqqorRo0cTGhrK6dOnCQgI4MiRI5SWluLt7Y3RaCQ/Px+LxUJ4eDg5OTlUV1c3OKAA5OXlMXbsWDIzM5k+fbr6QK2uXbuSl5enDio//vgjZ8+epVOnTvTq1UudURYcHExqaiqenp7AjWnK06ZNU2eiCSGEaH4OX/4qLS3Fzc0Nd3d3LBYLISEhjBo1Si2BrJ2+m5yczDfffENKSgorVqxodL8Wi4VJkyYRGBjI/v371e0dOnTgD3/4A0VFRcCNOpfRo0c3ur8vv/ySjz/+GKPRyKJFiygtLXX0UIUQQjjIoXUqBoMBDw8P4uLiUBQFq9VKQkICPXv2ZM6cOURGRgLg7+9PVFQUERERJCUlNdoVdubMGcrLywkMDGTSpEmkpqYyfPhw9fVx48aRk5NDVFQU+fn5REdH89lnnzW4z6CgIMLDw+nbty/Jycls2LCBmJgYew4XcP26Fr1WQUhu7ek1u+TWXovUtNTKyMigpqaGWbNmAXDp0iUOHz7MoEGDAJg4cSKJiYkMHTq00f1bLBbKy8uZMWMGAJ9//jlnz57F3d0dgJEjR2I0GgkLC8PPz8+uxwKPGjUKHx8f9X8vX77cnkNVufo8c73OhZfc2tNrdsmtvRapaam1c+dOUlJSuP/++wHIzs4mPT1dHVTsVV1dzfvvv09mZia+vr4AJCcnk5GRoU4G8PLyolu3biQmJtrdOTZjxgzi4uIICgri8OHD9OnTp973yQ15IYRwniZNKT5+/DiKoqgDCkBISAhWq5Xvv//eoX3t27ePPn36qAMKQFhYGLt27aKiokLdNmHCBKxWq92DVnx8PCtWrMBkMvH555/b9IgJIYRoHlLTIjUtmpLc2tNrdsmtPV3VtBw7dozExMQ628eMGdPodGMhhBD6oNmgEhQUJI/2FUKIVk5qWoQQQjhNq61pGTZsGAD/9V//RVpaGtu3b6/3e29V0wIyM0wIIRxl1y+VgQMHYjabMZvNpKWlsWnTJkpKSrBarTY1LQBGo5Gamhr14VxNqWmpqalRt9fWtNSqrWkB1JoWs9mMn58fqampmM1mdUA5ceIEO3fu5Dc8F0EIITTVamtafvzxR5KSkli0aJGjhyiEEKKJWmVNyy+//MLixYt5+eWX1YLJpnDlqgW9VkFIbu3pNbvk1p7UtNzC8ePHOXv2LPHx8VRWVvLNN9/w2muvsXjxYnsOV+XKc831OhdecmtPr9klt/akpuUWgoKCyMm5cQO+uLiY6OjoWw4ocjNeCCGcp9XWtAghhNCe1LRITYumJLf29JpdcmtPalqEEEK4FKlpEUII4TRS0yKEEMJpWm1Ny4MPPsgrr7xCSUkJv/zyC6+//jpdu3at871S0yKEEM7TamtaEhMTmTBhAunp6cyfP59vv/3WsTMjhBDCYQ7fU6mvpsXf35+srCwiIyPVmhaj0Ui/fv1ISUlhy5Ytje7XYrGwePFirly5wv79+9UV9R06dMDX15eioiJ69Oih1rQ0tKIebiyg7NWrF//xH/9Bly5dHF74CLKivjlIbu3pNbvk1p5mK+r1VtMCcO7cOXx8fNi8eTPr16/nrbfe4j//8z/tOVyVK08L1Ou0RcmtPb1ml9za02xFvd5qWgB8fX0JDg4GIDg4uE5+IYQQztcqa1oA+vfvz/79+5k4cSKffvqpOtHg1+RmvBBCOE+rrWmJiYlh165dTJkyhf/+7/9m9uzZDuUSQgjhOKlpkZoWTUlu7ek1u+TWntS0CCGEcClS0yKEEMJppKZFCCGE0zhU06IoClVVVcTHx5Ofn0+nTp2YOnUqgwcP5tChQzafW7dunfq6veLj4zl69Kj6vHsAk8nE5cuXyc3NVbft2bOHefPmkZ+fz9q1a7l48SLnzp3Dw8ODzp07ExAQQGxsLIsWLeLcuXNUVVXx3HPPMWLEiDrfKTUtQgjhPA6vUzl48CBvvPEGffv2dWqQ8vJytfaloKCAAQMG2Lx+8w2knJwcunTpAsCaNWuAuoPYu+++i6+vL4mJiVy9epWJEyfWO6gIIYRwHofvqZSUlDS6Qr4pcnNzGTRoEEOGDCE9Pd1mUBk3bhy7d++md+/elJSUUFlZSadOnRrc3+jRowkJCQFAURR1IaUjXLlqQa9VEJJbe3rNLrm1p3lNS1VVFadOnWLDhg0UFhbe1hf/msViYdmyZfTo0YP4+HguXLjAnXfeCdxYER8TE8PChQvJy8tj9OjRZGRkNLg/Ly8v4EZXWVRUFPPnz3c4kytPC9TrtEXJrT29Zpfc2nNGTYtDLcXbt28nMzOT6Ohom4WJt6uoqIjTp0+zatUqZs6cicFgYOvWrerrnp6e9O7dm8LCQvbu3cuoUaPs2u/333/P008/TWhoKBMmTHBaXiGEEPVz+PJXY5edmsJisbBgwQKMRiMA58+fJyIigueff159z/jx49m8eTM+Pj7qr5CGXL58menTp/Pqq682uApfbsYLIYTzOHT5y83NjbKyMmJjYzl37pz6+tWrVwkLC1P/nj59OgAbN25Un6vi5eVV7zqVqqoqdu/eTXZ2trrt7rvvJjAw0OY5Ko888gixsbGsXLnSrgNLSUmhpKSEv//97/z9738H4K233rKrjFIIIUTTSE2L1LRoSnJrT6/ZJbf2dFXTAjB37lyuXbtms83b25vk5GQtYwghhGgmmg4q69ev1/LrhBBCaEzTQcUVNbSi/tfkpr4QQjSs0SnFBQUFDBo0CJPJhMlkYvLkyTY33ENDQ1m6dKn6d1pamvoEx1rz5s1rdF1JZWUlgwcP5u2331a3FRcX06tXLzZu3Gjz3tmzZ2Mymfjqq6/UXA8++CBGoxGTycTHH3/MN998w9SpU5kyZQqxsbFcv369sUMVQghxmxxap2I2m0lLS2PTpk2UlJSotSpHjhyhtLQUAKPRSE1NjTrrKycnh+rq6kbr7fPy8hg7diyZmZnU1NSo27t27WozC+zHH3/k7NmzAPTq1UvN5efnR2pqKmazmWHDhpGUlER0dDTbtm0DbjwMTAghRPNy+PJXaWkpbm5uuLu7Y7FYCAkJwd/fn6ysLCIjIzEYDKxYsQKj0Ui/fv1ISUlhy5Ytje7XYrGwePFirly5wv79+xk+fDgAHTp0wNfXl6KiInr06EFubi6jR4/ms88+a3B/69atw93dnaqqKi5duoS3t7ejh1qHK1Uv6LUKQnJrT6/ZJbf2NK9pMRgMeHh4EBcXh6IoWK1WEhIS6NmzJ3PmzCEyMhIAf39/oqKiiIiIICkpqdGusDNnzlBeXk5gYCCTJk0iNTVVHVTgRvdXTk4OUVFR5OfnEx0d3eig4u7uzrlz55g2bRre3t4EBgbac6gNcqVpgnqdtii5tafX7JJbe86oaXG4pbhWRkYGNTU1zJo1C4BLly5x+PBhdfX6xIkTSUxMZOjQoY3u32KxUF5ert6L+fzzzzl79qxaAjly5EiMRiNhYWH4+fnZvYCxS5cu7NmzB4vFwqpVq1i9erVdnxNCCNE0TZ79tXPnTlJSUrj//vsByM7OJj09vcFKlPpUV1fz/vvvk5mZia+vLwDJyclkZGRgMpmAG6vxu3XrRmJiIuHh4Xbtd/bs2cTGxnLffffh5eWFm1v9t49kRpcQQjhPk578ePz4cRRFUQcUgJCQEKxWK99//71D+9q3bx99+vRRBxSAsLAwdu3aZVNaOWHCBKxWq92D1rPPPktsbCwmk4msrCwWLFjgUC4hhBCOk5oWqWnRlOTWnl6zS27t6aqm5dixYyQmJtbZPmbMmEanGwshhNAHzQaVoKCgeluKhRBCtB5S0+JATQvIjX0hhGiIQzUtkZGRTJ48mRMnTrBu3Tr16YyDBw+u87mbX7dXfHw8EydOtNlmMpkYM2aMzbY9e/bQq1cviouLeeGFFzCZTAQHBxMSEoLJZGL58uXqe7/44gt1FpkQQojm5fA6lYMHD/LGG2/Qt29fpwYpLy9Xa18KCgoYMGCAzes330DKycmhS5cuAKxZswa4MYh16tSJqVOnqp956623yM7Opn379k7NKoQQon4OX/4qKSlpdIV8U+Tm5jJo0CCGDBlCenq6zaAybtw4du/eTe/evSkpKaGystKuxxp37dqVdevW8dJLLzktp6vUL+i1CkJya0+v2SW39jSvaamqquLUqVNs2LCBwsLC2/riX7NYLCxbtowePXoQHx/PhQsXuPPOOwEIDg4mJiaGhQsXkpeXx+jRoxttPYYba2eKi4udmtNVpgrqddqi5NaeXrNLbu05o6bFoZbi7du3k5mZSXR0tM3CxNtVVFTE6dOnWbVqFTNnzsRgMNjcj/H09KR3794UFhayd+9eRo0a5bTvFkII4TwOX/6y57KToywWCwsWLMBoNAJw/vx5IiIieP7559X3jB8/ns2bN+Pj44OXl5fTvltmcwkhhPM4dPnLzc2NsrIyYmNjOXfunPr61atXCQsLU/+ePn06ABs3blSfq+Ll5VXvOpWqqip2795Ndna2uu3uu+8mMDDQ5jkqjzzyCLGxsaxcudLBQxRCCKEVqWmRmhZNSW7t6TW75NaermpaAObOncu1a9dstnl7e5OcnKxlDCGEEM1E00Fl/fr1Wn6dEEIIjUlNi4M1LTeTm/xCCGHLoZoWk8nE5MmTbW64h4aGsnTpUvXvtLQ09QmOtebNm9foupLKykoGDx7M22+/rW4rLi6mV69ebNy40ea9s2fPxmQy8dVXX6m5HnzwQYxGIyaTiY8//piTJ0/y17/+FZPJxIwZM7h8+XJjhyqEEOI2ObROxWw2k5aWxqZNmygpKVFrVY4cOUJpaSkARqORmpoaddZXTk4O1dXVjdbb5+XlMXbsWDIzM6mpqVG3d+3a1WYW2I8//sjZs2cB6NWrl5rLz8+P1NRUzGYzw4YN47XXXiMuLg6z2cyoUaN46623HDszQgghHObw5a/S0lLc3Nxwd3fHYrEQEhKCv78/WVlZREZGYjAYWLFiBUajkX79+pGSksKWLVsa3a/FYmHx4sVcuXKF/fv3M3z4cAA6dOiAr68vRUVF9OjRg9zcXEaPHs1nn33W4P6SkpLo3LkzAL/88guenp6OHmqjWrKKQa9VEJJbe3rNLrm1p3lNi8FgwMPDg7i4OBRFwWq1kpCQQM+ePZkzZw6RkZEA+Pv7ExUVRUREBElJSY12hZ05c4by8nICAwOZNGkSqamp6qACN7q/cnJyiIqKIj8/n+jo6EYHldoB5fPPPyctLY309HR7DtUhLTltUK/TFiW39vSaXXJrzxk1LQ63FNfKyMigpqaGWbNmAXDp0iUOHz6sPkN+4sSJJCYmMnTo0Eb3b7FYKC8vV+/FfP7555w9exZ3d3cARo4cidFoJCwsDD8/P9q1a2dPbN5//32Sk5PZuHFjs5RgCiGEsNXk2V87d+4kJSWF+++/H4Ds7GzS09PVQcVe1dXVvP/++2RmZuLr6wtAcnIyGRkZ6nNQvLy86NatG4mJiYSHh9u13127drF9+3bMZrO63/rIDC4hhHAeu27U/9rx48dRFEUdUOBGI7DVauX77793aF/79u2jT58+Nv/hDwsLY9euXTallRMmTMBqtdo1aP3yyy+89tprlJWVMW/ePEwmE2+++aZDuYQQQjhOalqkpkVTklt7es0uubWnq5qWY8eOkZiYWGf7mDFjGp1uLIQQQh80G1SCgoLqbSkWQgjRejg0qBQUFLBt2zabmWCxsbGMHTuW7t27M2LECF544QWeffZZ9fXZs2dTVlaG2WxW3/v111+zf/9+SkpKuHjxIj179gRg8+bN6oyvm7333nu8+eab3HPPPfzyyy+4ubmxevVq9Tn1lZWVBAcHM23aNJ555hngxmr86OhoduzY0eAx3U5Ny63IzX8hxG9Vk27U30pDq99v9swzz2A2m1m0aJHNav36BpRa48ePx2w2k5GRwYQJE3jnnXfU1261Gl8IIYS2nDqodOjQgT/84Q8UFRUBqKvfne3atWs2604sFguTJk0iMDCQ/fv3O/37hBBC2Mfp91SasvrdHrt37+aLL76grKyM7777jrS0NKDx1fgtQYuKBr1WQUhu7ek1u+TWnmY1LY5o6ur3xowfP56FCxcCcPjwYebNm8eHH37Y6Gr8lqDFdEK9TluU3NrTa3bJrT3Naloc0ZTV747y9/enurrartX4jZGb6kII4TwODyqHDh0iLCxM/btbt2513jNhwgReffVVkpKSOHPmzG0FrFV7+cvd3Z2ysjKWLl16y9X4oaGhhIeHc/r0aZussbGx/OUvf3FKHiGEEHXJinpZUa8pya09vWaX3NrT1Yp6e8ydO5dr167ZbPP29iY5ObmFEgkhhHCESw0q69evb+kIQgghboNT16kIIYT4bWv0l0pBQQHz589Xq1QqKyuZMGGCOrsqNDSUhx9+mCVLlgCQlpbGvn37bFa8z5s3j0GDBjVYHHmrqpWGql9eeeUVEhISADh69ChBQUG4ubkxY8YMhg0bBsCKFSvo1q0bU6dOrfd7m6OmpTEy40wI0VrZ9Uvl5iqVtLQ0Nm3aRElJCVarlYCAAI4cOUJpaSkARqORmpoaLBYLADk5OVRXVzfaRHyrqpWGql969eql5vLz8yM1NRWz2cywYcO4cuUKzzzzDB999JFjZ0QIIUSTOXz5q7S0FDc3N9zd3bFYLISEhDBq1CiysrIAMBgMrFixguTkZL755htSUlJYsWJFo/u9VdVKU6tfah/QFRoa6ughCiGEaCK7btQfOXIEk8mEwWDAw8ODuLg4FEXBarWSkJBAz549mTNnDpGRkcCNxYlRUVFERESQlJTU6PPhG6taaUr1yz333MM999zDgQMH7DlETTmjwkGvVRCSW3t6zS65tadZTcvAgQNt6u4BMjIyqKmpYdasWQBcunSJw4cPq48kz31MAAAN+klEQVT7nThxIomJiQwdOrTR/TdWtdJc1S8txRlz2PU6F15ya0+v2SW39lq0pmXnzp2kpKSoz6nPzs4mPT3drmfI38yeqpXmrH6Rm+ZCCOE8TZpSfPz4cRRFUQcUgJCQEKxWK99//71D+7pV1cquXbuoqKhQt02YMAGr1erwoCWEEEI7UtMiNS2aktza02t2ya09XdW0HDt2jMTExDrbx4wZ0+h0YyGEEPqg2aASFBSE2WzW6uuEEEK0AKlpEUII4TQtUiipRfXL2bNnWbJkCdXV1bRt25akpCQ6dOhQ530tUdPiDLl/697SEYQQoo4Waym+ee1LVVUVo0ePJjQ0lNOnT9tUv3h7e2M0GsnPz8disRAeHm5X9UtcXBzR0dE89NBD5OXlcebMmXoHFSGEEM7jEpe/nF39UlFRwZUrV9i3bx8mk0ktmxRCCNG8WmRK8c2Xv2qrX55++mn69+/Pk08+SW5uLsXFxcyZM4ecnH9fnsrKymL58uUkJSU1uFL/woULDBkyhC1btjBgwAAWL17Mww8/zFNPPWXzPqvVyiTL/2u242xOmRF367JZoKKiQnJrTK/ZJbf27M3+888/t/yU4l9rzuqX3//+93h5eTFw4EAAhg8fzqFDh+oMKnrWrl07Xc6F1+scfr3mBv1ml9zaa9GalubgrOqXdu3acd999/HZZ5/x5z//mU8//dRm9f/N9FrTotfCOiFE6+YS91TAudUvcOPhXGvWrGHy5MlcvnzZ6Z1hQggh6mqRXyoDBgxgwIABNtv69OlDZmamzTZPT08OHz5ss+3QoUN2fUdgYCBbt269vaBCCCEc4lKXvxwl1S9CCOFadD2oSPWLEEK4Fpe5pyKEEEL/WuyXihZVLR9++CGrV6/G399fff9f/vIXm/fotablhm8d/oReZ7sJIfShRS9/NXdVy5dffsmLL75ISEiIVockhBC/aS5zT6W+qhZ/f3+ysrKIjIxUq1qMRiP9+vUjJSWFLVu2NLjP48ePc/LkSbZs2UJQUBALFy6kTRuXOeQW0dLrWyoqKlo8Q1PoNTfoN7vk1p4zsrfof2GPHDmCyWRSq1ri4uJQFAWr1UpCQgI9e/Zkzpw5REZGAuDv709UVBQREREkJSXRsWPHBvc/ePBgRo4cyR//+EeWLFnCtm3b1H39VrX0Sl+9rjbWa27Qb3bJrT3dr6hvzqoWgEmTJuHj4wPAiBEjyMvLc/IRCCGEuJnLXQtyVlWLoig88cQTbNu2jbvuuovDhw/Tp0+fOu/T641rPf9rSAjRernUlGJnVrUYDAYSEhKYO3cukZGRlJeXM3nyZGdHFkIIcZMW+6WiRVXLo48+yqOPPnp7QYUQQtjN5S5/OUqqWoQQwnXoflCRqhYhhHAdLnVPRQghhL61yC8VLSpaaqWkpPDVV1/Vmbpc67dW0+IMep0xJ4Rofi32S2XgwIGYzWbMZjNpaWls2rSJkpISrFarTUULgNFopKamBovFAmBXRQvA/v37+fjjj5v7UIQQQvwfl7in0hwVLWfPnmX79u1ERUWpg5FwjtupcdBrhYVec4N+s0tu7em6pqU5K1rKyspYtmwZq1evpqioSKtD+s24nUWXel20qdfcoN/sklt7uq5pac6KlkOHDnHp0iUWLFhASUkJFy9eZOPGjTz77LPNczBCCCEAF7n8VctZFS2PP/44jz/+OHBjUsC2bdtuOaDo9aaznv81JIRovVxmSrEzK1qEEEK0jBb5paJFRUtD3yWEEKJ5uNTlL0dJRYsQQrgWXQ8qUtEihBCuRdeDijPIivqW4Jzcep1kIURr1iI36gsKChg0aBAmkwmTycTkyZNtfnGEhoaydOlS9e+0tDRmzJhhs4958+aRkZFxy+/47LPPCA8PZ/LkyfVeIhNCCOF8rbamZcWKFSQlJbFjxw6OHTvGiRMnNDkuIYT4LXOJy1/NUdOyY8cO2rRpQ1lZGaWlpfzud7/T6GiEVrSswvitV2+0BMmtPalpaUCbNm04evQo0dHR9OjRg7vuukuLwxIa0nLxp54Xm+o1u+TWntS0NOKhhx7io48+Yu3atWzcuJGoqCjnHoQQQggbLnH5q5azaloURcFoNJKcnMzvf/97vLy8qKqqqve9ep1BpNd/Dek1txDCPq2ypsVgMDB9+nRmzpxJZGQkJ0+eZNq0ac6OLIQQ4ldabU3LyJEjGTly5O0FFUII4RCXuvzlKKlpEUII16LrQUVqWoQQwrXoelBxBqlpaQmS2156nUgifrtabU3L4cOHiYiIwGg0EhUVRXl5ufMPRAghhI1WW9MSHx/Phg0bSE9P595771U/K4QQovm4xOWv5qhpMZvNdOrUCYDr16/j6empxaEI4VTOqPvQa22I5Nae1LQ0oHPnzgDs2bOHgoIC5s+f3+zHJISzOWOhqF4XnEpu7UlNSyM2b97MBx98wNtvvy2/VIQQQgMucfmrlrNqWgCSk5M5fvw4mzdvpl27drd8n15n1+j1X0OSW4jWrVXWtFy+fJkNGzZw8eJFZs6ciclkanCmmBBCCOdolTUtnTp14ssvv7z9oEIIIRziUpe/HCU1LUII4Vp0PahITYsQQrgWXQ8qziA1LS1BcmtPr9kld3NozglKLXajXouqlqNHjxIeHs6UKVNYv3698w9CCCGEjRad/dXcVS1LlixhzZo1bN26lS+++IITJ05oclxCCPFb5TKXv5xd1VJaWkpVVRVdu3YF4NFHH+WTTz7hgQce0OqQhBDCJd2qikXXNS3QvFUtpaWleHt7q397eXnxr3/9q9mPSQghXN2tFvLquqYFmreqxdvbm7KyMvXvsrIyfHx8nHwEQgghbuYyl79qOauqxdvbGw8PD7777jvuueceDh48yNy5c+u8T2patCW5tafX7JJbn1ympgWcW9UCsHTpUhYuXMhTTz3FAw88wJ/+9CdnxhVCCPErBkVRlJYO0VIaui4ohBDi1vr371/vdt0PKlLVIoQQrkP3g4oQQgjX4VL3VIQQQuiby83+cpaamhri4+P56quvaNu2LQkJCdx7773q6zt27GDbtm20adOG5557juHDh3PlyhUWLlxIRUUFnTt3ZuXKlbRv397lc1+9epWQkBACAgIAGDlyJH/72980zW1PdoArV64wdepUsrOz8fT0pKKighdffJEffvgBLy8vVq9e3eijol0ht6IoDBkyhPvuuw+Ahx56iBdeeMGlcm/evJmcnBvddkOHDmXu3Lkucb6bml0P5zw9PZ333nsPg8HA9OnTGTt2rEuc86bkbvL5VlqpvLw8JSYmRlEURSksLFRmz56tvnbx4kVl/PjxSmVlpVJSUqL+7+XLlyvvvvuuoiiK8o9//EPZtGmTLnIfOnRIWbZsmeZZf62h7IqiKAcOHFBCQ0OVfv36KRUVFYqiKEpqaqry5ptvKoqiKLt371aWL1+ubWilabnPnDmjzJo1S/OsN2so93fffac8+eSTyvXr15WamholIiJCOXnypEuc76Zmd/Vz/sMPPyjjxo1TqqqqlJ9++kkZMmSIUlNT4xLnvCm5m3q+W+3lL6vVymOPPQbcGGFvfmjXsWPH6NevH23btuWOO+6ga9eunDp1yuYzQ4YM4ZNPPtFF7i+//JLjx48TGRlJVFQUFy9e1Dx3Y9kB3Nzc2LRpE76+vvV+ZsiQIXUeyqaFpuQ+fvw4Fy5cwGQyMXPmTL79VvtW2oZy33XXXbz99tu4u7tjMBi4fv06np6eLnG+m5rd1c95x44dycrKwsPDg8uXL+Pp6YnBYHCJc96U3E093612UPl1TYu7uzvXr19XX7vjjjvU17y8vCgtLbXZ7uXlxU8//aRtaJqWu3v37kRFRZGWlsbIkSNJSEjQPHdtvltlBxg8eDAdOnSo8xlXPudQf24/Pz+effZZzGYzs2bN4sUXX9Qsb62Gcnt4eNCxY0cURWH16tU88MADdOvWzSXOd1Ozu/o5B2jTpg1paWlERETwxBNPqJ9p6XPelNxNPd+t9p7Kr2taampqaNOmTb2vlZWVcccdd6jb27Vr12K1Lk3JHRQUpN77GTVqFG+++aa2of9PQ9nt+YwrnvNb6du3L+7u7gD8+c9/5uLFiyiKgsFgaNasN2ssd2VlJYsWLcLLy4slS5bU+UxLVhc1JbsezjlAZGQkkydPZubMmRw5csQlznlTcv/pT39q0vlutb9UHn74YQ4cOADceK5K7U1suPHESKvVSmVlJT/99BNFRUUEBATw8MMPs3//fgAOHDhwy8U9rpb7lVdeIS8vD4DDhw/Tp08fzXM3lr2hz7jyOb+V9evXqy3Zp06dwt/fX9P/uEHDuRVF4fnnn6dXr14sW7ZM/Y+DK5zv2hyOZnf1c/7tt9+qEwo8PDxo27Ytbm5uLnHOm5K7qee71a5TqZ3t8PXXX6MoCitWrODAgQN07dqVESNGsGPHDrZv346iKMyaNYuQkBAuX75MTEwMZWVldOjQgTVr1vC73/3O5XP/61//YtGiRQC0b9+ehIQEOnfurGlue7LXCg4OJjc3F09PT8rLy4mJieHSpUt4eHiwZs0a/Pz8XD73tWvXePHFF/n5559xd3fn1VdfpUePHi6Tu6amhujoaB566CH1/dHR0QQGBrb4+W5q9u7du7v0OR8xYgTr16/nwIEDGAwGHnvsMebOnauL/4/Xl7up/x9vtYOKEEII7bXay19CCCG0J4OKEEIIp5FBRQghhNPIoCKEEMJpZFARQgjhNDKoCCGEcBoZVIQQQjiNDCpCCCGc5v8Dm9gw110xmhkAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e0wkpe9wVuER",
        "colab_type": "code",
        "outputId": "a96c6773-1aea-4ffa-a6a4-702a9acad94b",
        "colab": {}
      },
      "source": [
        "# upsampled \n",
        "rnd_up = RandomForestClassifier(max_leaf_nodes =20, max_depth=15, n_estimators=200,random_state = 20).fit(X_train, y_train)\n",
        "feat_importances = pd.Series(rnd_up.feature_importances_, index=X_train.columns)\n",
        "feat_importances.nlargest(20).plot(kind='barh')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x1a24a1c908>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 75
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "PjrORW2xVuES",
        "colab_type": "code",
        "outputId": "15f18932-5f92-437a-c6d7-1f2d9dad7412",
        "colab": {}
      },
      "source": [
        "# downsampled\n",
        "rnd_down = RandomForestClassifier(max_leaf_nodes =20, max_depth=15, n_estimators=200,random_state = 20).fit(X_train, y_train)\n",
        "feat_importances = pd.Series(rnd_down.feature_importances_, index=X_train.columns)\n",
        "feat_importances.nlargest(20).plot(kind='barh')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.axes._subplots.AxesSubplot at 0x1a24a86f28>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 76
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZUAAAD0CAYAAABThLtwAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvIxREBQAAIABJREFUeJzt3X1cVHXe//HXgIguxKIrFrlZ3oSYxmbuY9Usb1DD2zAM0R2mvdRMS+VSsiCNRCVv4iE+Sl1YK9QdwJuxQC6JMMn00pSrJsxH3pTRpS3az5tMCeLOOL8/vDjrBMIMDoc59Hn+tZyZOfM+57GPvs453+/7GBRFURBCCCGcwK2lAwghhGg9ZFARQgjhNDKoCCGEcBoZVIQQQjiNDCpCCCGcRgYVIYQQTtOmpQO0JKvV2tIRhBBCl/r371/v9t/0oAK3PjGu7uTJk/Tu3bulYzhMcmtPr9klt/bszd7QP8jl8pcQQginafSXSkFBAfPnz6dnz54oikJVVRXx8fHk5+fTqVMnpk6dyuDBgzl06JDN59atW6e+bq/4+HiOHj1KVlaWus1kMnH58mVyc3PVbXv27GHevHnk5+ezdu1aLl68yLlz5/Dw8KBz584EBAQQFxfHP/7xDz766COqq6uZOnUq4eHhdb7zvtgcAM6sGmd3TiGEEPWz6/LXwIEDWbt2LQAHDx7kjTfeoG/fvk4NUl5ejtVqJSAggIKCAgYMGGDz+s0/y3JycujSpQsAa9asAeoOYgUFBRQWFrJ161bKy8tJTU11al4hhBB1OXxPpaSkhI4dOzo9SG5uLoMGDWLIkCGkp6fbDCrjxo1j9+7d9O7dm5KSEiorK+nUqVOD+zt48CABAQHMmTOH0tJSXnrppQbff/LkSacch1YqKip0lxkkd0vQa3bJrT1nZLdrUDly5Agmk4mqqipOnTrFhg0bKCwsvK0v/jWLxcKyZcvo0aMH8fHxXLhwgTvvvBOA4OBgYmJiWLhwIXl5eYwePZqMjIwG9/fjjz9y/vx5UlJSKC4u5rnnnuODDz7AYDDU+3693VjT681Aya09vWaX3NrT7Eb9wIEDMZvNbN++nczMTKKjo6moqLA/aSOKioo4ffo0q1atYubMmRgMBrZu3aq+7unpSe/evSksLGTv3r2MGjWq0X36+vry6KOP0rZtW7p3746npydXrlxxWmYhhBB1OXz5q7HLTk1hsVhYsGABRqMRgPPnzxMREcHzzz+vvmf8+PFs3rwZHx8fvLy8Gt1n//79+ec//8m0adO4ePEi5eXl+Pr61nmf3KAXQgjncejyl5ubG2VlZcTGxnLu3Dn19atXrxIWFqb+PX36dAA2btyIxWIBwMvLC7PZXGffVVVV7N69m+zsbHXb3XffTWBgIHl5eeq2Rx55hNjYWFauXGnXgQ0fPpxPP/2Up556CkVRePXVV3F3d7frs0IIIZrG8Ft+SJfVapXFjxqT3NrTa3bJrT1H7qm4xIr6uXPncu3aNZtt3t7eJCcnaxlDCCFEM9F0UFm/fr2WXyeEEEJjuun+euutt9iyZQv5+fl4enoCNxZBpqenA+Du7k5gYCAvvvgibdu2JTg4GH9/f9zc/j3BLSYmps6iTVlRL4QQzqObQSU7O5uxY8eSk5NDWFgY+/fvZ8eOHaSkpODj44OiKKxcuZKsrCwmT54MQGpqqjoACSGEaH66KJQsKCiga9euTJkyRf1lYjabeemll/Dx8QHAYDDw8ssvqwOKEEII7enil4rFYiE8PJzu3bvTtm1bvvjiC4qLi7n33nsBKCwsJCkpierqavz9/dWesunTp6uXv9zc3NiyZcstv0NvtQp6rYKQ3NrTa3bJrT3Nalpa0rVr1zhw4ABXrlzBbDZTWlpKWloa/v7+FBcXExgYSL9+/TCbzRQVFREfH69+1pHLX3qbAqjXaYuSW3t6zS65tfebeJ5KdnY2kyZNIjU1lXfeeYcdO3Zw6NAhnnjiCV5//XV++ukn9b3/8z//04JJhRBCuPwvFYvFwuuvv67+3b59ex5//HEuXLhgU+VSVlZGz549Wb58ufremy9/ATz99NN1esNk1pcQQjiPyw8qN9e31Lr5EldISEi9n/voo4+aK5IQQohbcPnLX0IIIfRDBhUhhBBOI4OKEEIIp3H5eyrNrbamBeSmvRBC3K5Gf6kUFBQwaNAgTCYTkZGRTJ48mRMnTrBu3Tr16YyDBw+u87mbX7dXfHw8EydOtNlmMpkYM2aMzbY9e/bQq1cviouLeeGFFzCZTAQHBxMSEoLJZLKZAfbDDz8wdOhQioqKHMoihBDCcXb9Uhk4cKC6Sv3gwYO88cYbdYoZb1d5eTlWq5WAgAAKCgoYMGCAzes3L8rJycmhS5cuAKxZswa4MYh16tSJqVOnqp+prq7m1VdfpV27dk7NKoQQon4OX/4qKSmhY8eOTg+Sm5vLoEGDGDJkCOnp6TaDyrhx49i9eze9e/empKSEyspKux5rvHr1aqZMmcLGjRvtyqCnagW9VkFIbu3pNbvk1p5mNS21jxOuqqri1KlTbNiwgcLCwtv64l+zWCwsW7aMHj16EB8fz4ULF7jzzjsBCA4OJiYmhoULF5KXl8fo0aPJyMhocH/vvfceHTt25LHHHrN7UNFTtYJeqyAkt/b0ml1ya0+zmpaBAwdiNpvZvn07mZmZREdHU1FRYX/SRhQVFXH69GlWrVrFzJkzMRgMNvdjPD096d27N4WFhezdu7fOqvj6vPvuu3zyySeYTCZOnjxJTEwMly5dclpmIYQQdTl8+cuey06OslgsLFiwAKPRCMD58+dtKlgAxo8fz+bNm/Hx8cHLy6vRfdZW5MONm/3x8fH4+fnVeZ/M+BJCCOdx6PKXm5sbZWVlxMbGcu7cOfX1q1evEhYWpv49ffp0ADZu3IjFYgHAy8sLs9lcZ99VVVXs3r3bpo7l7rvvJjAwkLy8PHXbI488QmxsLCtXrnTwEIUQQmjFoCiK0tIhWorVaqV///4tHaNJ9HrdVnJrT6/ZJbf2HLmncqv/dmq6+HHu3Llcu3bNZpu3tzfJyclaxhBCCNFMNB1U1q9fr+XXCSGE0JjUtNxU0wJy414IIW5Ho4NKQUEB8+fPp2fPniiKQlVVFfHx8eTn56sr2AcPHsyhQ4dsPlffCvfGxMfHc/ToUbKystRtJpOJy5cvk5ubq27bs2cP8+bNIz8/n7Vr13Lx4kXOnTuHh4cHnTt3JiAggEWLFvHKK6/wv//7vxgMBpYuXUpAQIDdWYQQQjiu1da07N27F4Bt27ZRUFDA2rVr5d6NEEI0s1Zb0zJy5EiGDRsG3Fj34uPjY1cOvdQr6LUKQnJrT6/ZJbf2pKalEW3atCEmJoYPP/yQN998064cepkKqNdpi5Jbe3rNLrm1JzUtdli9ejV5eXnExcXx888/Oy2zEEKIulptTUtWVhYXLlxg1qxZtG/fHoPBgJtb3TFUZnsJIYTztNqalscff5yXX34Zo9HI9evXWbRokTxXRQghmpnUtEhNi6Ykt/b0ml1ya09qWoQQQrgUqWkRQgjhNK12RX1cXBxPPvkk3t7eAPzxj3+s936M1LQIIYTztNoV9ZWVlSiKUu/kACGEEM3DrnUqN2vuFfVPPvmkzVMb4d8r6mu/354V9adOnaK8vJzp06fz9NNPc/ToUadnFkIIYavVrqhv164dM2bMIDw8nDNnzjBz5kw++OAD2rRp+JD1Uq+g1yoIya09vWaX3NrTrKbl5stf3377LVOmTCE8PPy2vvhmN6+oB9QV9fPnzwfqrqhPSkpqdFDp1q0b9957LwaDgW7duuHr68ulS5fw9/dv8HN6mQqo12mLklt7es0uubXnjJqWVruifufOnXz99dfqr57S0lL8/Pycnl0IIcS/tdoV9U899RQvv/wyU6dOxWAwsGLFinovfclsLyGEcB5ZUS8r6jUlubWn1+ySW3uyol4IIYRLkRX1QgghnMbhdSpCCCHErThU0wI3VqpPmDABk8kEQGhoKA8//DBLliwBIC0tjX379vHOO++o+5g3bx6DBg3ir3/96y2/p7KykuDgYKZNm8YzzzwDQHFxMSNGjOCFF17g2WefVd87e/ZsysrKeOWVV0hISADg6NGjBAUF4ebmxowZM+jcuTOzZs3ivvvuA2Dq1KmMHTu2zvf+uqalltzAF0IIxzm8TqWqqorRo0cTGhrK6dOnCQgI4MiRI5SWluLt7Y3RaCQ/Px+LxUJ4eDg5OTlUV1c3OKAA5OXlMXbsWDIzM5k+fbr6QK2uXbuSl5enDio//vgjZ8+epVOnTvTq1UudURYcHExqaiqenp7AjWnK06ZNU2eiCSGEaH4OX/4qLS3Fzc0Nd3d3LBYLISEhjBo1Si2BrJ2+m5yczDfffENKSgorVqxodL8Wi4VJkyYRGBjI/v371e0dOnTgD3/4A0VFRcCNOpfRo0c3ur8vv/ySjz/+GKPRyKJFiygtLXX0UIUQQjjIoXUqBoMBDw8P4uLiUBQFq9VKQkICPXv2ZM6cOURGRgLg7+9PVFQUERERJCUlNdoVdubMGcrLywkMDGTSpEmkpqYyfPhw9fVx48aRk5NDVFQU+fn5REdH89lnnzW4z6CgIMLDw+nbty/Jycls2LCBmJgYew4XcP26Fr1WQUhu7ek1u+TWXovUtNTKyMigpqaGWbNmAXDp0iUOHz7MoEGDAJg4cSKJiYkMHTq00f1bLBbKy8uZMWMGAJ9//jlnz57F3d0dgJEjR2I0GgkLC8PPz8+uxwKPGjUKHx8f9X8vX77cnkNVufo8c73OhZfc2tNrdsmtvRapaam1c+dOUlJSuP/++wHIzs4mPT1dHVTsVV1dzfvvv09mZia+vr4AJCcnk5GRoU4G8PLyolu3biQmJtrdOTZjxgzi4uIICgri8OHD9OnTp973yQ15IYRwniZNKT5+/DiKoqgDCkBISAhWq5Xvv//eoX3t27ePPn36qAMKQFhYGLt27aKiokLdNmHCBKxWq92DVnx8PCtWrMBkMvH555/b9IgJIYRoHlLTIjUtmpLc2tNrdsmtPV3VtBw7dozExMQ628eMGdPodGMhhBD6oNmgEhQUJI/2FUKIVk5qWoQQQjhNq61pGTZsGAD/9V//RVpaGtu3b6/3e29V0wIyM0wIIRxl1y+VgQMHYjabMZvNpKWlsWnTJkpKSrBarTY1LQBGo5Gamhr14VxNqWmpqalRt9fWtNSqrWkB1JoWs9mMn58fqampmM1mdUA5ceIEO3fu5Dc8F0EIITTVamtafvzxR5KSkli0aJGjhyiEEKKJWmVNyy+//MLixYt5+eWX1YLJpnDlqgW9VkFIbu3pNbvk1p7UtNzC8ePHOXv2LPHx8VRWVvLNN9/w2muvsXjxYnsOV+XKc831OhdecmtPr9klt/akpuUWgoKCyMm5cQO+uLiY6OjoWw4ocjNeCCGcp9XWtAghhNCe1LRITYumJLf29JpdcmtPalqEEEK4FKlpEUII4TRS0yKEEMJpWm1Ny4MPPsgrr7xCSUkJv/zyC6+//jpdu3at871S0yKEEM7TamtaEhMTmTBhAunp6cyfP59vv/3WsTMjhBDCYQ7fU6mvpsXf35+srCwiIyPVmhaj0Ui/fv1ISUlhy5Ytje7XYrGwePFirly5wv79+9UV9R06dMDX15eioiJ69Oih1rQ0tKIebiyg7NWrF//xH/9Bly5dHF74CLKivjlIbu3pNbvk1p5mK+r1VtMCcO7cOXx8fNi8eTPr16/nrbfe4j//8z/tOVyVK08L1Ou0RcmtPb1ml9za02xFvd5qWgB8fX0JDg4GIDg4uE5+IYQQztcqa1oA+vfvz/79+5k4cSKffvqpOtHg1+RmvBBCOE+rrWmJiYlh165dTJkyhf/+7/9m9uzZDuUSQgjhOKlpkZoWTUlu7ek1u+TWntS0CCGEcClS0yKEEMJppKZFCCGE0zhU06IoClVVVcTHx5Ofn0+nTp2YOnUqgwcP5tChQzafW7dunfq6veLj4zl69Kj6vHsAk8nE5cuXyc3NVbft2bOHefPmkZ+fz9q1a7l48SLnzp3Dw8ODzp07ExAQQGxsLIsWLeLcuXNUVVXx3HPPMWLEiDrfKTUtQgjhPA6vUzl48CBvvPEGffv2dWqQ8vJytfaloKCAAQMG2Lx+8w2knJwcunTpAsCaNWuAuoPYu+++i6+vL4mJiVy9epWJEyfWO6gIIYRwHofvqZSUlDS6Qr4pcnNzGTRoEEOGDCE9Pd1mUBk3bhy7d++md+/elJSUUFlZSadOnRrc3+jRowkJCQFAURR1IaUjXLlqQa9VEJJbe3rNLrm1p3lNS1VVFadOnWLDhg0UFhbe1hf/msViYdmyZfTo0YP4+HguXLjAnXfeCdxYER8TE8PChQvJy8tj9OjRZGRkNLg/Ly8v4EZXWVRUFPPnz3c4kytPC9TrtEXJrT29Zpfc2nNGTYtDLcXbt28nMzOT6Ohom4WJt6uoqIjTp0+zatUqZs6cicFgYOvWrerrnp6e9O7dm8LCQvbu3cuoUaPs2u/333/P008/TWhoKBMmTHBaXiGEEPVz+PJXY5edmsJisbBgwQKMRiMA58+fJyIigueff159z/jx49m8eTM+Pj7qr5CGXL58menTp/Pqq682uApfbsYLIYTzOHT5y83NjbKyMmJjYzl37pz6+tWrVwkLC1P/nj59OgAbN25Un6vi5eVV7zqVqqoqdu/eTXZ2trrt7rvvJjAw0OY5Ko888gixsbGsXLnSrgNLSUmhpKSEv//97/z9738H4K233rKrjFIIIUTTSE2L1LRoSnJrT6/ZJbf2dFXTAjB37lyuXbtms83b25vk5GQtYwghhGgmmg4q69ev1/LrhBBCaEzTQcUVNbSi/tfkpr4QQjSs0SnFBQUFDBo0CJPJhMlkYvLkyTY33ENDQ1m6dKn6d1pamvoEx1rz5s1rdF1JZWUlgwcP5u2331a3FRcX06tXLzZu3Gjz3tmzZ2Mymfjqq6/UXA8++CBGoxGTycTHH3/MN998w9SpU5kyZQqxsbFcv369sUMVQghxmxxap2I2m0lLS2PTpk2UlJSotSpHjhyhtLQUAKPRSE1NjTrrKycnh+rq6kbr7fPy8hg7diyZmZnU1NSo27t27WozC+zHH3/k7NmzAPTq1UvN5efnR2pqKmazmWHDhpGUlER0dDTbtm0DbjwMTAghRPNy+PJXaWkpbm5uuLu7Y7FYCAkJwd/fn6ysLCIjIzEYDKxYsQKj0Ui/fv1ISUlhy5Ytje7XYrGwePFirly5wv79+xk+fDgAHTp0wNfXl6KiInr06EFubi6jR4/ms88+a3B/69atw93dnaqqKi5duoS3t7ejh1qHK1Uv6LUKQnJrT6/ZJbf2NK9pMRgMeHh4EBcXh6IoWK1WEhIS6NmzJ3PmzCEyMhIAf39/oqKiiIiIICkpqdGusDNnzlBeXk5gYCCTJk0iNTVVHVTgRvdXTk4OUVFR5OfnEx0d3eig4u7uzrlz55g2bRre3t4EBgbac6gNcqVpgnqdtii5tafX7JJbe86oaXG4pbhWRkYGNTU1zJo1C4BLly5x+PBhdfX6xIkTSUxMZOjQoY3u32KxUF5ert6L+fzzzzl79qxaAjly5EiMRiNhYWH4+fnZvYCxS5cu7NmzB4vFwqpVq1i9erVdnxNCCNE0TZ79tXPnTlJSUrj//vsByM7OJj09vcFKlPpUV1fz/vvvk5mZia+vLwDJyclkZGRgMpmAG6vxu3XrRmJiIuHh4Xbtd/bs2cTGxnLffffh5eWFm1v9t49kRpcQQjhPk578ePz4cRRFUQcUgJCQEKxWK99//71D+9q3bx99+vRRBxSAsLAwdu3aZVNaOWHCBKxWq92D1rPPPktsbCwmk4msrCwWLFjgUC4hhBCOk5oWqWnRlOTWnl6zS27t6aqm5dixYyQmJtbZPmbMmEanGwshhNAHzQaVoKCgeluKhRBCtB5S0+JATQvIjX0hhGiIQzUtkZGRTJ48mRMnTrBu3Tr16YyDBw+u87mbX7dXfHw8EydOtNlmMpkYM2aMzbY9e/bQq1cviouLeeGFFzCZTAQHBxMSEoLJZGL58uXqe7/44gt1FpkQQojm5fA6lYMHD/LGG2/Qt29fpwYpLy9Xa18KCgoYMGCAzes330DKycmhS5cuAKxZswa4MYh16tSJqVOnqp956623yM7Opn379k7NKoQQon4OX/4qKSlpdIV8U+Tm5jJo0CCGDBlCenq6zaAybtw4du/eTe/evSkpKaGystKuxxp37dqVdevW8dJLLzktp6vUL+i1CkJya0+v2SW39jSvaamqquLUqVNs2LCBwsLC2/riX7NYLCxbtowePXoQHx/PhQsXuPPOOwEIDg4mJiaGhQsXkpeXx+jRoxttPYYba2eKi4udmtNVpgrqddqi5NaeXrNLbu05o6bFoZbi7du3k5mZSXR0tM3CxNtVVFTE6dOnWbVqFTNnzsRgMNjcj/H09KR3794UFhayd+9eRo0a5bTvFkII4TwOX/6y57KToywWCwsWLMBoNAJw/vx5IiIieP7559X3jB8/ns2bN+Pj44OXl5fTvltmcwkhhPM4dPnLzc2NsrIyYmNjOXfunPr61atXCQsLU/+ePn06ABs3blSfq+Ll5VXvOpWqqip2795Ndna2uu3uu+8mMDDQ5jkqjzzyCLGxsaxcudLBQxRCCKEVqWmRmhZNSW7t6TW75NaermpaAObOncu1a9dstnl7e5OcnKxlDCGEEM1E00Fl/fr1Wn6dEEIIjUlNi4M1LTeTm/xCCGHLoZoWk8nE5MmTbW64h4aGsnTpUvXvtLQ09QmOtebNm9foupLKykoGDx7M22+/rW4rLi6mV69ebNy40ea9s2fPxmQy8dVXX6m5HnzwQYxGIyaTiY8//piTJ0/y17/+FZPJxIwZM7h8+XJjhyqEEOI2ObROxWw2k5aWxqZNmygpKVFrVY4cOUJpaSkARqORmpoaddZXTk4O1dXVjdbb5+XlMXbsWDIzM6mpqVG3d+3a1WYW2I8//sjZs2cB6NWrl5rLz8+P1NRUzGYzw4YN47XXXiMuLg6z2cyoUaN46623HDszQgghHObw5a/S0lLc3Nxwd3fHYrEQEhKCv78/WVlZREZGYjAYWLFiBUajkX79+pGSksKWLVsa3a/FYmHx4sVcuXKF/fv3M3z4cAA6dOiAr68vRUVF9OjRg9zcXEaPHs1nn33W4P6SkpLo3LkzAL/88guenp6OHmqjWrKKQa9VEJJbe3rNLrm1p3lNi8FgwMPDg7i4OBRFwWq1kpCQQM+ePZkzZw6RkZEA+Pv7ExUVRUREBElJSY12hZ05c4by8nICAwOZNGkSqamp6qACN7q/cnJyiIqKIj8/n+jo6EYHldoB5fPPPyctLY309HR7DtUhLTltUK/TFiW39vSaXXJrzxk1LQ63FNfKyMigpqaGWbNmAXDp0iUOHz6sPkN+4sSJJCYmMnTo0Eb3b7FYKC8vV+/FfP7555w9exZ3d3cARo4cidFoJCwsDD8/P9q1a2dPbN5//32Sk5PZuHFjs5RgCiGEsNXk2V87d+4kJSWF+++/H4Ds7GzS09PVQcVe1dXVvP/++2RmZuLr6wtAcnIyGRkZ6nNQvLy86NatG4mJiYSHh9u13127drF9+3bMZrO63/rIDC4hhHAeu27U/9rx48dRFEUdUOBGI7DVauX77793aF/79u2jT58+Nv/hDwsLY9euXTallRMmTMBqtdo1aP3yyy+89tprlJWVMW/ePEwmE2+++aZDuYQQQjhOalqkpkVTklt7es0uubWnq5qWY8eOkZiYWGf7mDFjGp1uLIQQQh80G1SCgoLqbSkWQgjRejg0qBQUFLBt2zabmWCxsbGMHTuW7t27M2LECF544QWeffZZ9fXZs2dTVlaG2WxW3/v111+zf/9+SkpKuHjxIj179gRg8+bN6oyvm7333nu8+eab3HPPPfzyyy+4ubmxevVq9Tn1lZWVBAcHM23aNJ555hngxmr86OhoduzY0eAx3U5Ny63IzX8hxG9Vk27U30pDq99v9swzz2A2m1m0aJHNav36BpRa48ePx2w2k5GRwYQJE3jnnXfU1261Gl8IIYS2nDqodOjQgT/84Q8UFRUBqKvfne3atWs2604sFguTJk0iMDCQ/fv3O/37hBBC2Mfp91SasvrdHrt37+aLL76grKyM7777jrS0NKDx1fgtQYuKBr1WQUhu7ek1u+TWnmY1LY5o6ur3xowfP56FCxcCcPjwYebNm8eHH37Y6Gr8lqDFdEK9TluU3NrTa3bJrT3Naloc0ZTV747y9/enurrartX4jZGb6kII4TwODyqHDh0iLCxM/btbt2513jNhwgReffVVkpKSOHPmzG0FrFV7+cvd3Z2ysjKWLl16y9X4oaGhhIeHc/r0aZussbGx/OUvf3FKHiGEEHXJinpZUa8pya09vWaX3NrT1Yp6e8ydO5dr167ZbPP29iY5ObmFEgkhhHCESw0q69evb+kIQgghboNT16kIIYT4bWv0l0pBQQHz589Xq1QqKyuZMGGCOrsqNDSUhx9+mCVLlgCQlpbGvn37bFa8z5s3j0GDBjVYHHmrqpWGql9eeeUVEhISADh69ChBQUG4ubkxY8YMhg0bBsCKFSvo1q0bU6dOrfd7m6OmpTEy40wI0VrZ9Uvl5iqVtLQ0Nm3aRElJCVarlYCAAI4cOUJpaSkARqORmpoaLBYLADk5OVRXVzfaRHyrqpWGql969eql5vLz8yM1NRWz2cywYcO4cuUKzzzzDB999JFjZ0QIIUSTOXz5q7S0FDc3N9zd3bFYLISEhDBq1CiysrIAMBgMrFixguTkZL755htSUlJYsWJFo/u9VdVKU6tfah/QFRoa6ughCiGEaCK7btQfOXIEk8mEwWDAw8ODuLg4FEXBarWSkJBAz549mTNnDpGRkcCNxYlRUVFERESQlJTU6PPhG6taaUr1yz333MM999zDgQMH7DlETTmjwkGvVRCSW3t6zS65tadZTcvAgQNt6u4BMjIyqKmpYdasWQBcunSJw4cPq48kz31MAAAN+klEQVT7nThxIomJiQwdOrTR/TdWtdJc1S8txRlz2PU6F15ya0+v2SW39lq0pmXnzp2kpKSoz6nPzs4mPT3drmfI38yeqpXmrH6Rm+ZCCOE8TZpSfPz4cRRFUQcUgJCQEKxWK99//71D+7pV1cquXbuoqKhQt02YMAGr1erwoCWEEEI7UtMiNS2aktza02t2ya09XdW0HDt2jMTExDrbx4wZ0+h0YyGEEPqg2aASFBSE2WzW6uuEEEK0AKlpEUII4TQtUiipRfXL2bNnWbJkCdXV1bRt25akpCQ6dOhQ530tUdPiDLl/697SEYQQoo4Waym+ee1LVVUVo0ePJjQ0lNOnT9tUv3h7e2M0GsnPz8disRAeHm5X9UtcXBzR0dE89NBD5OXlcebMmXoHFSGEEM7jEpe/nF39UlFRwZUrV9i3bx8mk0ktmxRCCNG8WmRK8c2Xv2qrX55++mn69+/Pk08+SW5uLsXFxcyZM4ecnH9fnsrKymL58uUkJSU1uFL/woULDBkyhC1btjBgwAAWL17Mww8/zFNPPWXzPqvVyiTL/2u242xOmRF367JZoKKiQnJrTK/ZJbf27M3+888/t/yU4l9rzuqX3//+93h5eTFw4EAAhg8fzqFDh+oMKnrWrl07Xc6F1+scfr3mBv1ml9zaa9GalubgrOqXdu3acd999/HZZ5/x5z//mU8//dRm9f/N9FrTotfCOiFE6+YS91TAudUvcOPhXGvWrGHy5MlcvnzZ6Z1hQggh6mqRXyoDBgxgwIABNtv69OlDZmamzTZPT08OHz5ss+3QoUN2fUdgYCBbt269vaBCCCEc4lKXvxwl1S9CCOFadD2oSPWLEEK4Fpe5pyKEEEL/WuyXihZVLR9++CGrV6/G399fff9f/vIXm/fotablhm8d/oReZ7sJIfShRS9/NXdVy5dffsmLL75ISEiIVockhBC/aS5zT6W+qhZ/f3+ysrKIjIxUq1qMRiP9+vUjJSWFLVu2NLjP48ePc/LkSbZs2UJQUBALFy6kTRuXOeQW0dLrWyoqKlo8Q1PoNTfoN7vk1p4zsrfof2GPHDmCyWRSq1ri4uJQFAWr1UpCQgI9e/Zkzpw5REZGAuDv709UVBQREREkJSXRsWPHBvc/ePBgRo4cyR//+EeWLFnCtm3b1H39VrX0Sl+9rjbWa27Qb3bJrT3dr6hvzqoWgEmTJuHj4wPAiBEjyMvLc/IRCCGEuJnLXQtyVlWLoig88cQTbNu2jbvuuovDhw/Tp0+fOu/T641rPf9rSAjRernUlGJnVrUYDAYSEhKYO3cukZGRlJeXM3nyZGdHFkIIcZMW+6WiRVXLo48+yqOPPnp7QYUQQtjN5S5/OUqqWoQQwnXoflCRqhYhhHAdLnVPRQghhL61yC8VLSpaaqWkpPDVV1/Vmbpc67dW0+IMep0xJ4Rofi32S2XgwIGYzWbMZjNpaWls2rSJkpISrFarTUULgNFopKamBovFAmBXRQvA/v37+fjjj5v7UIQQQvwfl7in0hwVLWfPnmX79u1ERUWpg5FwjtupcdBrhYVec4N+s0tu7em6pqU5K1rKyspYtmwZq1evpqioSKtD+s24nUWXel20qdfcoN/sklt7uq5pac6KlkOHDnHp0iUWLFhASUkJFy9eZOPGjTz77LPNczBCCCEAF7n8VctZFS2PP/44jz/+OHBjUsC2bdtuOaDo9aaznv81JIRovVxmSrEzK1qEEEK0jBb5paJFRUtD3yWEEKJ5uNTlL0dJRYsQQrgWXQ8qUtEihBCuRdeDijPIivqW4Jzcep1kIURr1iI36gsKChg0aBAmkwmTycTkyZNtfnGEhoaydOlS9e+0tDRmzJhhs4958+aRkZFxy+/47LPPCA8PZ/LkyfVeIhNCCOF8rbamZcWKFSQlJbFjxw6OHTvGiRMnNDkuIYT4LXOJy1/NUdOyY8cO2rRpQ1lZGaWlpfzud7/T6GiEVrSswvitV2+0BMmtPalpaUCbNm04evQo0dHR9OjRg7vuukuLwxIa0nLxp54Xm+o1u+TWntS0NOKhhx7io48+Yu3atWzcuJGoqCjnHoQQQggbLnH5q5azaloURcFoNJKcnMzvf/97vLy8qKqqqve9ep1BpNd/Dek1txDCPq2ypsVgMDB9+nRmzpxJZGQkJ0+eZNq0ac6OLIQQ4ldabU3LyJEjGTly5O0FFUII4RCXuvzlKKlpEUII16LrQUVqWoQQwrXoelBxBqlpaQmS2156nUgifrtabU3L4cOHiYiIwGg0EhUVRXl5ufMPRAghhI1WW9MSHx/Phg0bSE9P595771U/K4QQovm4xOWv5qhpMZvNdOrUCYDr16/j6empxaEI4VTOqPvQa22I5Nae1LQ0oHPnzgDs2bOHgoIC5s+f3+zHJISzOWOhqF4XnEpu7UlNSyM2b97MBx98wNtvvy2/VIQQQgMucfmrlrNqWgCSk5M5fvw4mzdvpl27drd8n15n1+j1X0OSW4jWrVXWtFy+fJkNGzZw8eJFZs6ciclkanCmmBBCCOdolTUtnTp14ssvv7z9oEIIIRziUpe/HCU1LUII4Vp0PahITYsQQrgWXQ8qziA1LS1BcmtPr9kld3NozglKLXajXouqlqNHjxIeHs6UKVNYv3698w9CCCGEjRad/dXcVS1LlixhzZo1bN26lS+++IITJ05oclxCCPFb5TKXv5xd1VJaWkpVVRVdu3YF4NFHH+WTTz7hgQce0OqQhBDCJd2qikXXNS3QvFUtpaWleHt7q397eXnxr3/9q9mPSQghXN2tFvLquqYFmreqxdvbm7KyMvXvsrIyfHx8nHwEQgghbuYyl79qOauqxdvbGw8PD7777jvuueceDh48yNy5c+u8T2patCW5tafX7JJbn1ympgWcW9UCsHTpUhYuXMhTTz3FAw88wJ/+9CdnxhVCCPErBkVRlJYO0VIaui4ohBDi1vr371/vdt0PKlLVIoQQrkP3g4oQQgjX4VL3VIQQQuiby83+cpaamhri4+P56quvaNu2LQkJCdx7773q6zt27GDbtm20adOG5557juHDh3PlyhUWLlxIRUUFnTt3ZuXKlbRv397lc1+9epWQkBACAgIAGDlyJH/72980zW1PdoArV64wdepUsrOz8fT0pKKighdffJEffvgBLy8vVq9e3eijol0ht6IoDBkyhPvuuw+Ahx56iBdeeMGlcm/evJmcnBvddkOHDmXu3Lkucb6bml0P5zw9PZ333nsPg8HA9OnTGTt2rEuc86bkbvL5VlqpvLw8JSYmRlEURSksLFRmz56tvnbx4kVl/PjxSmVlpVJSUqL+7+XLlyvvvvuuoiiK8o9//EPZtGmTLnIfOnRIWbZsmeZZf62h7IqiKAcOHFBCQ0OVfv36KRUVFYqiKEpqaqry5ptvKoqiKLt371aWL1+ubWilabnPnDmjzJo1S/OsN2so93fffac8+eSTyvXr15WamholIiJCOXnypEuc76Zmd/Vz/sMPPyjjxo1TqqqqlJ9++kkZMmSIUlNT4xLnvCm5m3q+W+3lL6vVymOPPQbcGGFvfmjXsWPH6NevH23btuWOO+6ga9eunDp1yuYzQ4YM4ZNPPtFF7i+//JLjx48TGRlJVFQUFy9e1Dx3Y9kB3Nzc2LRpE76+vvV+ZsiQIXUeyqaFpuQ+fvw4Fy5cwGQyMXPmTL79VvtW2oZy33XXXbz99tu4u7tjMBi4fv06np6eLnG+m5rd1c95x44dycrKwsPDg8uXL+Pp6YnBYHCJc96U3E093612UPl1TYu7uzvXr19XX7vjjjvU17y8vCgtLbXZ7uXlxU8//aRtaJqWu3v37kRFRZGWlsbIkSNJSEjQPHdtvltlBxg8eDAdOnSo8xlXPudQf24/Pz+effZZzGYzs2bN4sUXX9Qsb62Gcnt4eNCxY0cURWH16tU88MADdOvWzSXOd1Ozu/o5B2jTpg1paWlERETwxBNPqJ9p6XPelNxNPd+t9p7Kr2taampqaNOmTb2vlZWVcccdd6jb27Vr12K1Lk3JHRQUpN77GTVqFG+++aa2of9PQ9nt+YwrnvNb6du3L+7u7gD8+c9/5uLFiyiKgsFgaNasN2ssd2VlJYsWLcLLy4slS5bU+UxLVhc1JbsezjlAZGQkkydPZubMmRw5csQlznlTcv/pT39q0vlutb9UHn74YQ4cOADceK5K7U1suPHESKvVSmVlJT/99BNFRUUEBATw8MMPs3//fgAOHDhwy8U9rpb7lVdeIS8vD4DDhw/Tp08fzXM3lr2hz7jyOb+V9evXqy3Zp06dwt/fX9P/uEHDuRVF4fnnn6dXr14sW7ZM/Y+DK5zv2hyOZnf1c/7tt9+qEwo8PDxo27Ytbm5uLnHOm5K7qee71a5TqZ3t8PXXX6MoCitWrODAgQN07dqVESNGsGPHDrZv346iKMyaNYuQkBAuX75MTEwMZWVldOjQgTVr1vC73/3O5XP/61//YtGiRQC0b9+ehIQEOnfurGlue7LXCg4OJjc3F09PT8rLy4mJieHSpUt4eHiwZs0a/Pz8XD73tWvXePHFF/n5559xd3fn1VdfpUePHi6Tu6amhujoaB566CH1/dHR0QQGBrb4+W5q9u7du7v0OR8xYgTr16/nwIEDGAwGHnvsMebOnauL/4/Xl7up/x9vtYOKEEII7bXay19CCCG0J4OKEEIIp5FBRQghhNPIoCKEEMJpZFARQgjhNDKoCCGEcBoZVIQQQjiNDCpCCCGc5v8Dm9gw110xmhkAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "sHQnGJVqVuEX",
        "colab_type": "text"
      },
      "source": [
        "## 4.4 KNN"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aOACMSpAVuEX",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "\n",
        "\n",
        "knn = KNeighborsClassifier()\n",
        "param_knn = {'n_neighbors':range(1,10)}"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "oOJ1oWEpVuEY",
        "colab_type": "text"
      },
      "source": [
        "### original dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2rjENTLcVuEY",
        "colab_type": "code",
        "outputId": "234976e9-1bc4-4e6f-c109-1e9065cad6f5",
        "colab": {}
      },
      "source": [
        "grid_knn_org = GridSearchCV(knn,param_knn, n_jobs= -1)\n",
        "grid_knn_org.fit(X_train, y_train)\n",
        "knn_pred_train = grid_knn_org.predict(X_train)\n",
        "knn_pred_test = grid_knn_org.predict(X_test)\n",
        "\n",
        "print('Best Parameter:',grid_knn_org.best_params_)\n",
        "print('Train set score: {:f}'.format(grid_knn_org.score(X_train, y_train)))\n",
        "print('Test set score: {:f} '.format(grid_knn_org.score(X_test, y_test)))\n",
        "print('Cross-Validation best score:{:f} '.format(grid_knn_org.best_score_))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv='warn', error_score='raise-deprecating',\n",
              "       estimator=KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',\n",
              "           metric_params=None, n_jobs=None, n_neighbors=5, p=2,\n",
              "           weights='uniform'),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'n_neighbors': range(1, 10)}, pre_dispatch='2*n_jobs',\n",
              "       refit=True, return_train_score='warn', scoring=None, verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 81
        },
        {
          "output_type": "stream",
          "text": [
            "Best Parameter: {'n_neighbors': 8}\n",
            "Train set score: 0.798500\n",
            "Test set score: 0.778667 \n",
            "Cross-Validation best score:0.770250 \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ujVkD-AmVuEa",
        "colab_type": "code",
        "outputId": "20ece0c0-1ef0-4d42-a88f-d77ae82f3960",
        "colab": {}
      },
      "source": [
        "knn_org_train_accuracy = accuracy_score(y_train, knn_pred_train)\n",
        "knn_org_test_accuracy = accuracy_score(y_test, knn_pred_test)\n",
        "knn_org_train_recall = recall_score(y_train, knn_pred_train)\n",
        "knn_org_test_recall = recall_score(y_test, knn_pred_test)\n",
        "knn_org_train_precision = precision_score(y_train,knn_pred_train)\n",
        "knn_org_test_precision = precision_score(y_test,knn_pred_test)\n",
        "knn_org_train_confusion_matrix = confusion_matrix(y_train, knn_pred_train)\n",
        "knn_org_test_confusion_matrix = confusion_matrix(y_test, knn_pred_test)\n",
        "\n",
        "print('best score - original', grid_knn_org.best_score_)\n",
        "print('train accuracy: ', knn_org_train_accuracy)\n",
        "print('test accuracy: ', knn_org_test_accuracy)\n",
        "print('train recall',  knn_org_train_recall)\n",
        "print('test recall: ', knn_org_test_recall)\n",
        "print('train precision: ', knn_org_train_precision)\n",
        "print('test precision: ', knn_org_test_precision)\n",
        "print('train confusion matrix: ',  knn_org_train_confusion_matrix)\n",
        "print('test confusion matrix: ', knn_org_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "best score - original 0.77025\n",
            "train accuracy:  0.7985\n",
            "test accuracy:  0.7786666666666666\n",
            "train recall 0.16051695073983893\n",
            "test recall:  0.1040863531225906\n",
            "train precision:  0.7076796036333609\n",
            "test precision:  0.4485049833887043\n",
            "train confusion matrix:  [[18307   354]\n",
            " [ 4482   857]]\n",
            "test confusion matrix:  [[4537  166]\n",
            " [1162  135]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d4AZ1R80VuEc",
        "colab_type": "text"
      },
      "source": [
        "### up-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "d0j9Yx-VVuEc",
        "colab_type": "code",
        "outputId": "9e33a30f-189a-497e-a454-358704fe0ce0",
        "colab": {}
      },
      "source": [
        "# upsampled dataset\n",
        "knn_up = KNeighborsClassifier()\n",
        "param_knn = {'n_neighbors':range(2,10)}\n",
        "grid_knn_up = GridSearchCV(knn_up,param_knn, n_jobs= -1)\n",
        "grid_knn_up.fit(X_train_up, y_train_up)\n",
        "knn_up_pred_train = grid_knn_up.predict(X_train_up)\n",
        "knn_up_pred_test = grid_knn_up.predict(X_test)\n",
        "\n",
        "print('Upsample Best Parameter:',grid_knn_up.best_params_)\n",
        "print('Upsample Train set score: {:f}'.format(grid_knn_up.score(X_train_up, y_train_up)))\n",
        "print('Upsample Test set score: {:f} '.format(grid_knn_up.score(X_test, y_test)))\n",
        "print('Upsample Cross-Validation best score:{:f} '.format(grid_knn_up.best_score_))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv='warn', error_score='raise-deprecating',\n",
              "       estimator=KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',\n",
              "           metric_params=None, n_jobs=None, n_neighbors=5, p=2,\n",
              "           weights='uniform'),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'n_neighbors': range(2, 10)}, pre_dispatch='2*n_jobs',\n",
              "       refit=True, return_train_score='warn', scoring=None, verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 83
        },
        {
          "output_type": "stream",
          "text": [
            "Upsample Best Parameter: {'n_neighbors': 2}\n",
            "Upsample Train set score: 0.988184\n",
            "Upsample Test set score: 0.709000 \n",
            "Upsample Cross-Validation best score:0.793098 \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cP8CcCIAVuEd",
        "colab_type": "code",
        "outputId": "fb23b3d6-fb8c-4530-d7d0-6e3cfb579de9",
        "colab": {}
      },
      "source": [
        "# results - upsampled training dataset\n",
        "knn_up_train_accuracy = accuracy_score(y_train_up, knn_up_pred_train)\n",
        "knn_up_test_accuracy = accuracy_score(y_test, knn_up_pred_test)\n",
        "knn_up_train_recall = recall_score(y_train_up, knn_up_pred_train)\n",
        "knn_up_test_recall = recall_score(y_test, knn_up_pred_test)\n",
        "knn_up_train_precision = precision_score(y_train_up,knn_up_pred_train)\n",
        "knn_up_test_precision = precision_score(y_test,knn_up_pred_test)\n",
        "knn_up_train_confusion_matrix = confusion_matrix(y_train_up, knn_up_pred_train)\n",
        "knn_up_test_confusion_matrix = confusion_matrix(y_test, knn_up_pred_test)\n",
        "\n",
        "print('Upsample best score:', grid_knn_up.best_score_)\n",
        "print('Upsample train accuracy: ', knn_up_train_accuracy)\n",
        "print('Upsample test accuracy: ', knn_up_test_accuracy)\n",
        "print('Upsample train recall',  knn_up_train_recall)\n",
        "print('Upsample test recall: ', knn_up_test_recall)\n",
        "print('Upsample train precision: ', knn_up_train_precision)\n",
        "print('Upsample test precision: ', knn_up_test_precision)\n",
        "print('Upsample train confusion matrix: ',  knn_up_train_confusion_matrix)\n",
        "print('Upsample test confusion matrix: ', knn_up_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Upsample best score: 0.793097904721076\n",
            "Upsample train accuracy:  0.9881839129735812\n",
            "Upsample test accuracy:  0.709\n",
            "Upsample train recall 0.9766893521247522\n",
            "Upsample test recall:  0.26985350809560527\n",
            "Upsample train precision:  0.999670908293111\n",
            "Upsample test precision:  0.30461270670147955\n",
            "Upsample train confusion matrix:  [[18655     6]\n",
            " [  435 18226]]\n",
            "Upsample test confusion matrix:  [[3904  799]\n",
            " [ 947  350]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Kqy8ZTtUVuEe",
        "colab_type": "text"
      },
      "source": [
        "### down-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e-CCSs4CVuEf",
        "colab_type": "code",
        "outputId": "bfd16dde-38f5-4e3c-c82f-18a6b7a03fab",
        "colab": {}
      },
      "source": [
        "# downsampled dataset\n",
        "knn_down = KNeighborsClassifier()\n",
        "param_knn = {'n_neighbors':range(2,10)}\n",
        "grid_knn_down = GridSearchCV(knn_down,param_knn, n_jobs= -1)\n",
        "grid_knn_down.fit(X_train_down, y_train_down)\n",
        "knn_down_pred_train = grid_knn_down.predict(X_train_down)\n",
        "knn_down_pred_test = grid_knn_down.predict(X_test)\n",
        "\n",
        "print('Downsample Best Parameter:',grid_knn_down.best_params_)\n",
        "print('Downsample Train set score: {:f}'.format(grid_knn_down.score(X_train_down, y_train_down)))\n",
        "print('Downsample Test set score: {:f} '.format(grid_knn_down.score(X_test, y_test)))\n",
        "print('Downsample Cross-Validation best score:{:f} '.format(grid_knn_down.best_score_))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv='warn', error_score='raise-deprecating',\n",
              "       estimator=KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',\n",
              "           metric_params=None, n_jobs=None, n_neighbors=5, p=2,\n",
              "           weights='uniform'),\n",
              "       fit_params=None, iid='warn', n_jobs=-1,\n",
              "       param_grid={'n_neighbors': range(2, 10)}, pre_dispatch='2*n_jobs',\n",
              "       refit=True, return_train_score='warn', scoring=None, verbose=0)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 85
        },
        {
          "output_type": "stream",
          "text": [
            "Downsample Best Parameter: {'n_neighbors': 7}\n",
            "Downsample Train set score: 0.716239\n",
            "Downsample Test set score: 0.571333 \n",
            "Downsample Cross-Validation best score:0.599550 \n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wa1-mW8SVuEg",
        "colab_type": "code",
        "outputId": "1f15ba8b-bdf2-428c-f36b-1111372ed3e0",
        "colab": {}
      },
      "source": [
        "# results - downsampled training dataset\n",
        "knn_down_train_accuracy = accuracy_score(y_train_down, knn_down_pred_train)\n",
        "knn_down_test_accuracy = accuracy_score(y_test, knn_down_pred_test)\n",
        "knn_down_train_recall = recall_score(y_train_down, knn_down_pred_train)\n",
        "knn_down_test_recall = recall_score(y_test, knn_down_pred_test)\n",
        "knn_down_train_precision = precision_score(y_train_down,knn_down_pred_train)\n",
        "knn_down_test_precision = precision_score(y_test,knn_down_pred_test)\n",
        "knn_down_train_confusion_matrix = confusion_matrix(y_train_down, knn_down_pred_train)\n",
        "knn_down_test_confusion_matrix = confusion_matrix(y_test, knn_down_pred_test)\n",
        "\n",
        "print('Downsample best score: ', grid_knn_down.best_score_)\n",
        "print('Downsample train accuracy: ', knn_down_train_accuracy)\n",
        "print('Downsample test accuracy: ', knn_down_test_accuracy)\n",
        "print('Downsample train recall',  knn_down_train_recall)\n",
        "print('Downsample test recall: ', knn_down_test_recall)\n",
        "print('Downsample train precision: ', knn_down_train_precision)\n",
        "print('Downsample test precision: ', knn_down_test_precision)\n",
        "print('Downsample train confusion matrix: ',  knn_down_train_confusion_matrix)\n",
        "print('Downsample test confusion matrix: ', knn_down_test_confusion_matrix)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Downsample best score:  0.5995504776175313\n",
            "Downsample train accuracy:  0.7162389960666792\n",
            "Downsample test accuracy:  0.5713333333333334\n",
            "Downsample train recall 0.7184866079790223\n",
            "Downsample test recall:  0.6175790285273709\n",
            "Downsample train precision:  0.7152713033749767\n",
            "Downsample test precision:  0.278415015641293\n",
            "Downsample train confusion matrix:  [[3812 1527]\n",
            " [1503 3836]]\n",
            "Downsample test confusion matrix:  [[2627 2076]\n",
            " [ 496  801]]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "VKKj6qTtVuEi",
        "colab_type": "text"
      },
      "source": [
        "## 4.5 Gradient Boosting Tree"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GVz5soyHVuEi",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "import xgboost as xgb"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "rvG512g9VuEj",
        "colab_type": "text"
      },
      "source": [
        "### original dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VCw3wK6TVuEj",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "xgb_train = xgb.DMatrix(X_train, label=y_train)\n",
        "xgb_test = xgb.DMatrix(X_test, label=y_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tq5nuJUSVuEk",
        "colab_type": "code",
        "outputId": "11ee275b-31fe-42ed-c9f2-521e443e379a",
        "colab": {}
      },
      "source": [
        "param = {\"objective\": \"binary:hinge\",\n",
        "         \"alpha\": 0,\n",
        "         \"lambda\": 0.9,\n",
        "         \"n_estimator\": 100,\n",
        "         \"booster\": \"gbtree\",\n",
        "         \"eval_metric\": \"auc\",\n",
        "         \"learning_rate\": 0.05,\n",
        "         \"max_depth\": 15,\n",
        "         \"nthread\": 6,\n",
        "         \"max_depth\": 15, \n",
        "         \"eta\": 0.08, \n",
        "         \"subsample\": 0.85,\n",
        "         \"colsample_bytree\": 0.9} \n",
        "\n",
        "watchlist = [(xgb_train, 'xgb_train'), (xgb_test, 'xgb_test')]\n",
        "\n",
        "xgbm = xgb.train(params = param, \n",
        "                 num_boost_round=200,\n",
        "                 dtrain = xgb_train,\n",
        "                 early_stopping_rounds = 40,\n",
        "                 verbose_eval = 10,\n",
        "                 evals = watchlist)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0]\txgb_train-auc:0.5\txgb_test-auc:0.5\n",
            "Multiple eval metrics have been passed: 'xgb_test-auc' will be used for early stopping.\n",
            "\n",
            "Will train until xgb_test-auc hasn't improved in 40 rounds.\n",
            "[10]\txgb_train-auc:0.541894\txgb_test-auc:0.529301\n",
            "[20]\txgb_train-auc:0.900331\txgb_test-auc:0.701672\n",
            "[30]\txgb_train-auc:0.891298\txgb_test-auc:0.688329\n",
            "[40]\txgb_train-auc:0.887279\txgb_test-auc:0.675801\n",
            "[50]\txgb_train-auc:0.89634\txgb_test-auc:0.666521\n",
            "Stopping. Best iteration:\n",
            "[19]\txgb_train-auc:0.902385\txgb_test-auc:0.706074\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3c2yOfiNVuEl",
        "colab_type": "code",
        "outputId": "3d73be0b-6b2a-42e6-8422-2e3e64a6936a",
        "colab": {}
      },
      "source": [
        "y_pred = xgbm.predict(xgb_test)\n",
        "print(\"Recall score for Gradient Boosting with original data: {:5f}\".format(recall_score(y_test, y_pred)))\n",
        "print(\"Accuracy for Gradient Boosting with original data: {:5f}\".format(accuracy_score(y_test, y_pred)))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Recall score for Gradient Boosting with original data: 0.384734\n",
            "Accuracy for Gradient Boosting with original data: 0.816500\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "DtJUOH2tVuEm",
        "colab_type": "text"
      },
      "source": [
        "### up-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jEJe-SFtVuEm",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "xgb_train = xgb.DMatrix(X_train_up, label=y_train_up)\n",
        "xgb_test = xgb.DMatrix(X_test, label=y_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AMDSwsuDVuEn",
        "colab_type": "code",
        "outputId": "72353df2-3a07-4748-db84-c6a94e30ad91",
        "colab": {}
      },
      "source": [
        "param = {\"objective\": \"binary:hinge\",\n",
        "         \"alpha\": 0,\n",
        "         \"lambda\": 0.9,\n",
        "         \"n_estimator\": 100,\n",
        "         \"booster\": \"gbtree\",\n",
        "         \"eval_metric\": \"auc\",\n",
        "         \"learning_rate\": 0.05,\n",
        "         \"max_depth\": 15,\n",
        "         \"nthread\": 6,\n",
        "         \"max_depth\": 15, \n",
        "         \"eta\": 0.08, \n",
        "         \"subsample\": 0.85,\n",
        "         \"colsample_bytree\": 0.9} \n",
        "\n",
        "watchlist = [(xgb_train, 'xgb_train'), (xgb_test, 'xgb_test')]\n",
        "\n",
        "xgbm = xgb.train(params = param, \n",
        "                 num_boost_round=300,\n",
        "                 dtrain = xgb_train,\n",
        "                 early_stopping_rounds = 50,\n",
        "                 verbose_eval = 10,\n",
        "                 evals = watchlist)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0]\txgb_train-auc:0.5\txgb_test-auc:0.5\n",
            "Multiple eval metrics have been passed: 'xgb_test-auc' will be used for early stopping.\n",
            "\n",
            "Will train until xgb_test-auc hasn't improved in 100 rounds.\n",
            "[10]\txgb_train-auc:0.546059\txgb_test-auc:0.519227\n",
            "[20]\txgb_train-auc:0.896469\txgb_test-auc:0.682373\n",
            "[30]\txgb_train-auc:0.949226\txgb_test-auc:0.698686\n",
            "[40]\txgb_train-auc:0.964096\txgb_test-auc:0.68993\n",
            "[50]\txgb_train-auc:0.972536\txgb_test-auc:0.683212\n",
            "[60]\txgb_train-auc:0.979422\txgb_test-auc:0.674304\n",
            "[70]\txgb_train-auc:0.982986\txgb_test-auc:0.671498\n",
            "[80]\txgb_train-auc:0.985638\txgb_test-auc:0.66832\n",
            "[90]\txgb_train-auc:0.988425\txgb_test-auc:0.665554\n",
            "[100]\txgb_train-auc:0.989926\txgb_test-auc:0.658974\n",
            "[110]\txgb_train-auc:0.99097\txgb_test-auc:0.658428\n",
            "[120]\txgb_train-auc:0.992042\txgb_test-auc:0.658468\n",
            "[130]\txgb_train-auc:0.992846\txgb_test-auc:0.65658\n",
            "Stopping. Best iteration:\n",
            "[30]\txgb_train-auc:0.949226\txgb_test-auc:0.698686\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "n2j4CUBcVuEo",
        "colab_type": "code",
        "outputId": "5a372438-e3b2-4207-98b0-b1f699062568",
        "colab": {}
      },
      "source": [
        "y_pred = xgbm.predict(xgb_test)\n",
        "print(\"Recall score for Gradient Boosting with original data: {:5f}\".format(recall_score(y_test, y_pred)))\n",
        "print(\"Accuracy for Gradient Boosting with original data: {:5f}\".format(accuracy_score(y_test, y_pred)))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Recall score for Gradient Boosting with original data: 0.396299\n",
            "Accuracy for Gradient Boosting with original data: 0.804333\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kcvHcBPCVuEp",
        "colab_type": "text"
      },
      "source": [
        "### down-sampled dataset"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2Zc5jHzKVuEp",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "xgb_train = xgb.DMatrix(X_train_down, label=y_train_down)\n",
        "xgb_test = xgb.DMatrix(X_test, label=y_test)"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "e36TmeYcVuEq",
        "colab_type": "code",
        "outputId": "d25a24f7-180c-45c5-bb8b-f7062d8a95d2",
        "colab": {}
      },
      "source": [
        "param = {\"objective\": \"binary:hinge\",\n",
        "         \"alpha\": 0,\n",
        "         \"lambda\": 0.9,\n",
        "         \"n_estimator\": 100,\n",
        "         \"booster\": \"gbtree\",\n",
        "         \"eval_metric\": \"auc\",\n",
        "         \"learning_rate\": 0.05,\n",
        "         \"max_depth\": 15,\n",
        "         \"nthread\": 6,\n",
        "         \"max_depth\": 15, \n",
        "         \"eta\": 0.08, \n",
        "         \"subsample\": 0.85,\n",
        "         \"colsample_bytree\": 0.9} \n",
        "\n",
        "watchlist = [(xgb_train, 'xgb_train'), (xgb_test, 'xgb_test')]\n",
        "\n",
        "xgbm = xgb.train(params = param, \n",
        "                 num_boost_round=300,\n",
        "                 dtrain = xgb_train,\n",
        "                 early_stopping_rounds = 50,\n",
        "                 verbose_eval = 10,\n",
        "                 evals = watchlist)"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[0]\txgb_train-auc:0.5\txgb_test-auc:0.5\n",
            "Multiple eval metrics have been passed: 'xgb_test-auc' will be used for early stopping.\n",
            "\n",
            "Will train until xgb_test-auc hasn't improved in 50 rounds.\n",
            "[10]\txgb_train-auc:0.508429\txgb_test-auc:0.500638\n",
            "[20]\txgb_train-auc:0.913467\txgb_test-auc:0.616921\n",
            "[30]\txgb_train-auc:0.966005\txgb_test-auc:0.665401\n",
            "[40]\txgb_train-auc:0.97743\txgb_test-auc:0.686281\n",
            "[50]\txgb_train-auc:0.983424\txgb_test-auc:0.691168\n",
            "[60]\txgb_train-auc:0.986795\txgb_test-auc:0.688348\n",
            "[70]\txgb_train-auc:0.989043\txgb_test-auc:0.693478\n",
            "[80]\txgb_train-auc:0.990448\txgb_test-auc:0.690195\n",
            "[90]\txgb_train-auc:0.991478\txgb_test-auc:0.68868\n",
            "Stopping. Best iteration:\n",
            "[46]\txgb_train-auc:0.981645\txgb_test-auc:0.694425\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UW55M1qOVuEr",
        "colab_type": "code",
        "outputId": "d52ffddb-67d5-4fa2-df17-813e015f62ed",
        "colab": {}
      },
      "source": [
        "y_pred = xgbm.predict(xgb_test)\n",
        "print(\"Recall score for Gradient Boosting with down-sampled data: {:5f}\".format(recall_score(y_test, y_pred)))\n",
        "print(\"Accuracy for Gradient Boosting with down-sampled data: {:5f}\".format(accuracy_score(y_test, y_pred)))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Recall score for Gradient Boosting with down-sampled data: 0.703161\n",
            "Accuracy for Gradient Boosting with down-sampled data: 0.679833\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TZwSqVtVVuEs",
        "colab_type": "text"
      },
      "source": [
        "# 5. Model Performance"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EqqJ2tbLAoji",
        "colab_type": "text"
      },
      "source": [
        "By conducting various machine learning models on the dataset, we trained several classifiers can be used for predictive analysis. Our next step is to compare the performance of different models and pick top ones to be used under business environment. We compare the prediction accuracy of each model on testing dataset. As we can see, by using original training set,  the accuracy of LR, DT, RF and KNN are around 80%\n",
        "By using UpSampled dataset, the accuracy of all models are around 70%. And by using downsampled dataset, the accuracy of SVM is much higher than using other two dataset. \n",
        "\n",
        "However, detecting potential late payments for the credit account is a special task that we should focus more on how successfully the model can predict to recognize clients with late payment potential. That is why we should pay more attention on Recall rate, instead of accuracy. Obviously, by using downsampled dataset as training set, all models have higher recall rate than using other two datasets. Among all these models, LR, SVM, RF are three classifiers with best performance, which the average recall rate is around 65%. -Meaning that 65% of potential late payment can be detected successfully.\n",
        "\n",
        "Therefore, we pick these three models to be used for further learning process to improve the performance. On the other hand, we can use model resembling methods such as voting and stacking to enhance the overall performance of the prediction."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "74Tq1bQAVuEu",
        "colab_type": "text"
      },
      "source": [
        "# 6. Conclusion"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "K9MXGTo5CQN0",
        "colab_type": "text"
      },
      "source": [
        "Based on a better prediction model, we have several suggestions for both banks and individual clients.   \n",
        "- For banks: Keep tracking clients using revolving credits and Push notification of payment remind to those clients who are predicted to be with late payment.   \n",
        "- For customers: Check your credit card accounts frequently and Check your credit report at least once per year to monitor credit history.\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3WMIeoNkcpGP",
        "colab_type": "text"
      },
      "source": [
        "\n",
        "#**7. Reference**\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vt7v87pjdKo6",
        "colab_type": "text"
      },
      "source": [
        "Ismail, S., Amin, H., Shayeri, S. F., & Hashim, N. (2014). Determinants of Attitude towards Credit Card Usage. Jurnal Pengurusan, 41, 145–154. Retrieved from http://search.ebscohost.com.libproxy.utdallas.edu/login.aspx?direct=true&db=bth&AN=99747154&site=ehost-live\n",
        "\n",
        "Lee, Y.-H., & Huang, Y.-L. (2011). Do you have credit cards? The expansion of the credit card market in Taiwan. Applied Economics Letters, 18(17), 1639–1644. https://doi-org.libproxy.utdallas.edu/10.1080/13504851.2011.556586\n"
      ]
    }
  ]
}
