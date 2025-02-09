SELECT A.APNT_NO, P.PT_NAME, A.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT A
JOIN PATIENT P ON A.PT_NO = P.PT_NO
JOIN DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE A.APNT_YMD BETWEEN TO_DATE('2022-04-13 00:00:00', 'YYYY-MM-DD HH24:MI:SS') 
                    AND TO_DATE('2022-04-13 23:59:59', 'YYYY-MM-DD HH24:MI:SS')
  AND A.MCDP_CD = 'CS'
  AND A.APNT_CNCL_YN = 'N'
ORDER BY A.APNT_YMD;