def trains(st1,st2):
    
    if st1=='lko' and st2=='ndls':
        print('''**************************LUCKNOW NR TO NEW DELHI**********************************
                 02916	ASHRAM EXP SPL	LKO	15:20	NDLS	07:40  AC-3 Tier  ₹1,475.00
                 02958	RAJDHANI SPL	LKO	20:25	NDLS	10:10  AC chair   ₹290.00 ''')
    elif st1=='ndls' and st2=='bct':
        print('''******************************NEW DELHI TO MUMBAI CENTRAL***************************
                 02630	YPR S KRNTI SPL	NDLS	08:45	BCT	10:25	AC-1 Tier ₹4,185.00
                 02780	GOA EXPRESS SPL	NDLS	15:00	BCT	15:50	AC-3 Tier ₹1,770.00
                 02494	NDLS BCT AC SPL	NDLS	21:35	BCT	21:25   AC-2 Tier ₹2,545.00 ''')
    
    elif st1=='ndls' and st2=='lko':
        print('''******************************NEW DELHI TO LUCKNOW NR************************************
                 02004	NDLS LJNSPL     NDLS    06:10	LJN	12:45	AC-1 Tier ₹4,285.00
                 02570	DBG HUMSAFAR	NDLS	12:15	ASH	19:40	AC-3 Tier ₹1,870.00
                 02494	NDLS AC SPL	NDLS	21:35	PUNE	21:25   AC-2 Tier ₹2,045.00 ''')
    elif st1=='lko' and st2=='bct':
        print('''******************************LUCKNOW TO MUMBAI CENTRAL************************************
                 02954	AUG KR RAJ SPL	NZM	17:20	MMCT	10:05	AC-1 Tier ₹3,185.00
                 02926	PASCHIM EXP SPL	SZM	15:56	BDTS	14:45	AC-3 Tier ₹2,770.00
                 02494	NDLS AC SPL	NZM	21:35	KYN	17:47   AC-2 Tier ₹1,545.00 ''')
        
    elif st1=='bct' and st2=='ndls':
        print('''******************************MUMBAI CENTRAL TO NEW DELHI************************************
                 02954	AUG KR RAJ SPL	BCT	17:20	NDLS	10:05	AC-1 Tier ₹3,185.00
                 02926	PASCHIM EXP SPL	BCT	15:56	NDLS	14:45	AC-3 Tier ₹2,770.00
                 02494	NDLS AC SPL	BCT	21:35	NDLS	17:47   AC-2 Tier ₹1,545.00 ''')
        
    elif st1=='bct' and st2=='lko':
        print('''******************************NEW DELHI TO LUCKNOW NR************************************
                 02004	NDLS LJNSPL     BCT    06:10	LKO	12:45	AC-1 Tier ₹4,285.00
                 02570	DBG HUMSAFAR	BCT	12:15	LKO	19:40	AC-3 Tier ₹1,870.00
                 02494	NDLS AC SPL	BCT	21:35	LKO	21:25   AC-2 Tier ₹2,045.00 ''')
    else:
        print("WRONG VALUES")
    

        
