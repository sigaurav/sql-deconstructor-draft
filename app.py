"""
To-DO Things
Write logic for no aliases in below methods
 -def identifier(self, token):
 -def extract_select_columns_and_aliases(self, identifiers_):
 -def extract_from_table_and_aliases(self, identifiers_):

"""
import re
import sqlparse
from sqlparse.tokens import Keyword, DML, Punctuation
from sqlparse.sql import IdentifierList,Token, Parenthesis, Identifier


class SQLDeconstructor:

    select_dict = {}
    from_dict = {}

    def process_query(self, full_query):
        """

        :param query:
        :return:
        """

        full_query = re.sub(r"(?:'[^']*'\s*)|(\s+)", lambda match: " " if match.group(1) else match.group(0), query)
        sql_tokens = sqlparse.parse(full_query)[0].tokens
        identifiers_ = list(sqlparse.sql.IdentifierList(sql_tokens).get_identifiers())

        self.extract_select_columns_and_aliases(identifiers_)
        self.extract_from_table_and_aliases(identifiers_)

        lookup_dict = self.lookup_table_aliases(self.select_dict.copy(), self.select_dict.copy())


    def lookup_table_aliases(self, select_dict, from_dict):
        """

        :param select_dict:
        :param from_dict:
        :return:
        """





    def extract_select_columns_and_aliases(self, identifiers_):
        """

        :param sql_query:
        :return:
        """


        print(identifiers_)
        for index, item in enumerate(identifiers_):
            if isinstance(item, Token) and item.value.upper() == "SELECT":
                for col in identifiers_[index + 1].get_identifiers():
                    if col.has_alias():
                        self.select_dict[col.get_alias()] = col.value.replace(col.get_alias(), '').strip()


    def extract_from_table_and_aliases(self, identifiers_):
        """

        :param sql_query:
        :return:
        """
        for index, item in enumerate(identifiers_):
            print(type(identifiers_[index]))

            # Capture tables in FROM
            if isinstance(item, Token) and item.value.upper() == "FROM":
                for table in identifiers_[index + 1].get_identifiers():
                    if table.has_alias():
                        self.from_dict[table.get_alias()] = table.value.replace(table.get_alias(), '').strip()

            # Capture tables in parentheses and JOINS
            if isinstance(item, Parenthesis):
                self.parenthesis(item)


    def identifier(self, token):
        if token.has_alias():
            self.from_dict[token.get_alias()] = token.value.replace(token.get_alias(), '').strip()

    def parenthesis(self, token):
        for subtoken in token.tokens:
            if isinstance(subtoken, Identifier):
                self.identifier(subtoken)
            elif isinstance(subtoken, Parenthesis):
                self.parenthesis(subtoken)


query = "SELECT SUM(T609604.TOTAL_BALANCE_BEQ) C1, SUM(T609604.TOTAL_YTD_PERIOD_BAL_BEQ) C2, SUM(T609604.TOTAL_QTD_PERIOD_BAL_BEQ) C3, SUM(T609604.TOTAL_AVG_PERIOD_BAL_BEQ) C4, SUM(T609604.TOTAL_ACTIVITY_BEQ) C5, SUM(T609604.YTD_BALANCE_BEQ) C6, SUM(T609604.YTD_PERIOD_BALANCE_BEQ) C7, SUM(T609604.QTD_PERIOD_BALANCE_BEQ) C8, SUM(T609604.AVG_PERIOD_BALANCE_BEQ) C9, SUM(T609604.PERIOD_ACTIVITY_BEQ) C10, SUM(T609604.YTD_BALANCE) C11, SUM(T609604.YTD_PERIOD_BALANCE) C12, SUM(T609604.QTD_PERIOD_BALANCE) C13, SUM(T609604.AVG_PERIOD_BALANCE) C14, SUM(T609604.PERIOD_ACTIVITY) C15, T471748.ACCOUNT_NAME C16, T471748.ACCOUNT_NUMBER C17, T471748.SECONDARY_ACCT_USAGE_CODE C18, T470966.SECONDARY_ACCT_USAGE_NAME C19, T428190.AU_NUMBER C20, T469643.ACTUAL_DATE C21, T428176.COMPANY_NUMBER C22, T470283.CURRENCY_CODE C23, T609604.BALANCE_TYPE C24, T609530.DESTINATION C25, T609604.GLM_INSTRUMENT_NBR C26, T609609.CYCLE_TYPE C27, T609604.OUTPUT_RUN_ID C28, T609604.RECON_DATE C29, CASE WHEN 'AD' = 'AD' THEN T609604.SRC_INSTRUMENT_ID WHEN NOT T427926.SOURCE NAME = 'AD' THEN T609604.SRC_INSTRUMENT_ID ELSE '--RESTRICTED--' END C30, T470284.LEDGER_SHORT_NAME C31, T427926.SOURCE_NAME C32, T471557.SL_SUBACCOUNT_NBR C33, T431211.PERIOD_NAME C34, CASE WHEN T427926.SRC_SYSTEM_ID IN ('C6','C62', 'C63') THEN 'C6' ELSE T427926.V_DATA_ORIGIN END C35, T469643.CALENDAR_DAY_ID C36 FROM RDR.FND_SYS_PERIODS T431211, RDR.FND_GLM_AU T428190, RDR.FND_GLM_COMPANY T428176, (( RDR.RPT_DIM_CALENDAR T469643 INNER JOIN ( RDR.FND_SL_CURRENCIES T470283 INNER JOIN ( RDR.FND_SL_LEDGERS T470284 INNER JOIN ((GLR.GLR_INSTRUMENT_BALANCES T609604 INNER JOIN (RDR.FND_SRC_SYSTEMS T427926 INNER JOIN GLR.GLR_INSTRUMENT_BALANCE_STATUS T609609 ON T427926.SRC_SYSTEM_ID = T609609.SRC_SYSTEM_ID) ON T609604.AS_OF_DATE = T609609.AS_OF_DATE AND T609604.LOAD_ID = T609609.LOAD_ID AND T609604.RECON_DATE = T609609.RECON_DATE AND T609604.SRC_SYSTEM_ID = T609609.SRC_SYSTEM_ID) LEFT OUTER JOIN ( RDR.FND_GLM_ACCT_SECONDARY_USAGE T470966 INNER JOIN RDR.FND_GLM_ACCOUNTS T471748 ON T470966.EXPIRED_FLAG = 'N' AND T470966.SECONDARY_ACCT_USAGE_CODE = T471748.SECONDARY_ACCT_USAGE_CODE) ON T471748.GLM_ACCOUNT_SID = T609604.GLM_ACCOUNT_SID) ON T470284.LEDGER_SID = T609604.LEDGER_SID) ON T470283.CURRENCY_SID = T609604.CURRENCY_SID) ON T469643.ACTUAL_DATE=T609609.AS_OF_DATE) LEFT OUTER JOIN RDR.FND_SL_SUBACCOUNTS T471557 ON T471557.SL_SUBACCOUNT_SID = T609604.GLM_SUBACCOUNT_SID) LEFT OUTER JOIN EAGLE_OLTP.BATCH T609530 ON T609530.BATCH ID =T609604.ADJ_SET_SID WHERE ( T428176.GLM_COMPANY_SID = T609604.GLM_COMPANY_SID AND T428190.GLM_AU_SID = T609604.GLM_AU_SID AND T427926.SOURCE NAME = 'AFS      COMMERCIAL LOAN' AND T431211.PERIOD_NAME = T609604.PERIOD_NAME AND T431211.PERIOD_NAME = 'OCT-22' AND T469643.ACTUAL_DATE = TO_DATE ('2022-10-31', 'YYYY-MM-DD') AND T470284.LEDGER SHORT NAME = 'AMER_USD_SL' AND T609609.CYCLE_TYPE = 'FINAL') GROUP BY T427926.SOURCE_NAME, T428176.COMPANY_NUMBER, T428190.AU_NUMBER, T431211.PERIOD_NAME, ACTUAL_DATE, T469643.CALENDAR_DAY_ID, T470283.CURRENCY_CODE, T470284.LEDGER_SHORT_NAME, T470966.SECONDARY_ACCT_USAGE_NAME, T471557.SL_SUBACCOUNT_NBR, T471748.SECONDARY_ACCT_USAGE_CODE, T471748.ACCOUNT_NAME, T471748.ACCOUNT_NUMBER, T609530.DESTINATION, T609604.BALANCE_TYPE, T609604.GLM_INSTRUMENT_NBR, T609604.OUTPUT_RUN_ID, T609604.RECON_DATE, T609609.CYCLE_TYPE, CASE WHEN T427926.SRC_SYSTEM_ID IN ('C6','C62') THEN 'C6' ELSE T427926.V_DATA_ORIGIN END, CASE WHEN 'AD' = 'AD' THEN T609604.SRC_INSTRUMENT_ID WHEN NOT T427926.SOURCE NAME = 'AD' THEN T609604.SRC_INSTRUMENT_ID ELSE '--RESTRICTED--' END"
sd = SQLDeconstructor()
sd.process_query(query)
print(sd.from_dict)
print(sd.select_dict)
