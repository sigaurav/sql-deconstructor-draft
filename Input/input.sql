SELECT investments.month_nm AS month_nm,
       acquisitions.companies_acquired,
       investments.companies_rec_investment
  FROM (
        SELECT acq.acquired_month_nm AS month_nm,
               COUNT(DISTINCT acq.company_permalink) AS companies_acquired
          FROM tutorial.crunchbase_acquisitions acq
         GROUP BY 1
       ) acquisitions

  FULL JOIN (
        SELECT invst.funded_month_nm AS month_nm,
               COUNT(DISTINCT invst.company_permalink) AS companies_rec_investment
          FROM tutorial.crunchbase_investments invst
         GROUP BY 1
       ) investments

    ON acquisitions.month_nm = investments.month_nm