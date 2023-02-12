import sqlparse

query = "SUM(GLR.GLR_INSTRUMENT_BALANCES.TOTAL_BALANCE_BEQ) C1"

parsed = sqlparse.parse(query)[0]
ident = sqlparse.sql.IdentifierList(parsed).get_identifiers()

print(type(parsed))
print(type(parsed.tokens))
print(type(ident))

print(parsed.within(sqlparse.sql.Function))



