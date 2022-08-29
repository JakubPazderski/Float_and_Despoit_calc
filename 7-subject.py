import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt


#flat price increase
freq=1
rate=0.05
years=5
pv=120000
nper=years*12
periods=np.arange(1,nper+1,dtype=int)
monthly_rate=0.05/12

increase_list=[]
for period in periods:
    price=round(pv*monthly_rate+pv,2)
    increase=[price]
    pv=price
    increase_list+=increase
np_increase_list=np.array(increase_list)

#deposit calculation
rate1=0.12
pv1=np_increase_list[59]
monthly_rate1=rate1/12
years1=5
nper1=years*12
periods1=np.arange(1,nper+1,dtype=int)


payment=-np.around(npf.pmt(monthly_rate1,nper1,0,pv1),2)
interest_equal=np.around(npf.ipmt(monthly_rate1,periods1,nper1,0,pv1),2)
deposit=-np.around(npf.ppmt(monthly_rate1,periods1,nper1,0,pv1),2)
deposit_status=np.cumsum(deposit)

#Orientacyjna cena mieszkania za 5 lat będzie wynosić  154003,15zł
#By za 5 lat kupić analizowane mieszkanie, trzeba co miesiąc wpłacać na lokatę 1885,68zł

plt.plot(np_increase_list,label='wartość mieszkania')
plt.plot(deposit_status,label='status lokaty')
plt.legend()
plt.xlabel('Liczba okresów')
plt.ylabel('ZŁ')






    


    






