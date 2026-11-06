1 

# A Configuration Based Pumped Storage Hydro Model in MISO Day-Ahead Market 

Bing Huang, _Member, IEEE,_ Yonghong Chen, _Senior Member, IEEE_ and Ross Baldick, _Fellow, IEEE_ 

**_Abstract_ —Pumped storage hydro units (PSHU) can provide flexibility to power systems. This becomes particularly valuable in recent years with the increasing shares of intermittent renewable resources. However, due to emphasis on thermal generation in the current market practices, the flexibility from PSHUs have not been fully explored and utilized. This paper proposes a configuration based pumped storage hydro (PSH) model for the day-ahead market, in order to enhance the use of PSH resources in the system. A strategic design of incorporating and fully optimizing PSHUs in the day-ahead market is presented. We show the compactness of the proposed model. Numerical studies are presented in an illustrative test system and the Midcontinent Independent System Operator (MISO) system.** 

**_Index Terms_ —Pumped storage hydro, configuration based model, mixed-integer programming, security constrained unit commitment.** 

||NOMENCLATURE<br>|
|---|---|
|Sets and|ndices:|
|_t ∈T_|set of time intervals;|
|_g ∈Gpsh_|set of PSHUs;|
|_g ∈Gpsh,_|_r_set of PSHUs that share the same reservoir _r_;|
|_g ∈G_|set of the rest of the generating units in a system;|
|_m ∈Mg_|set of configurations, _Mg_ = [_alloff, gen, pump_];|
|_n ∈M_<sup>_F,_</sup><br>_g_|<sup>_m_</sup><br>set of configurations that configuration _m_ can<br>feasibly transit to;|
|_r ∈R_|set of reservoirs.|
|Data [uni|ts]:|
|_Dt_|system net load at period _t_ [$/MW];|
|_Q_<br>_gen_<br>_~~g~~_|minimum generation power of PSHU _g_ [MW];|
|_Q_<br>_~~g~~en_<br>_g_|maximum generation power of PSHU _g_ [MW];|
|_Q_<br>_pump_<br>_~~g~~_|minimum pumping power of PSHU _g_ [MW];|
|_Q_<br>_~~p~~ump_<br>_g_|maximum pumping power of PSHU _g_ [MW];|
|_η_<sup>_gen_</sup><br>_g_|generating efficiency of the PSHU _g_ [NA];|
|_η_<sup>_pump_</sup><br>_g_|pumping efficiency of the PSHU _g_ [NA];|
|_Er,_0|initial energy level of the reservoir _r_ [MWh];|
|_Er,|T |_|final energy level of the reservoir _r_ [MWh];|
|_Er_|maximum energy level of the reservoir_r_[MWh];|
|_E_<br>_~~r~~_|minimum energy level of the reservoir_r_[MWh];|



B. Huang and Y. Chen are with Midcontinent Independent System Operator, Inc. (MISO), Carmel, IN, 46032 USA. 

R. Baldick is an emeritus professor at the Department of Electrical and Computer Engineering, University of Texas, Austin, TX, 78712 USA. This work has been submitted to the IEEE for possible publication. Copyright may be transferred without notice, after which this version may no longer be accessible. 

|_C_<sup>_pump_</sup><br>_g,t_|the bid price of pump load at unit _g_ during time<br>interval _t_ [$/MW].|
|---|---|
|Variables|[units]:|
|_er,t_|energy stored in the reservoir_r_at time_t_[MWh];|
|_u_<sup>_m_</sup><br>_g,t_|binary variable, commitment variable of unit _g_<br>configuration _m_ during time interval _t_ [NA];|
|_ur_<sup>_m_</sup><br>_r,t_|continuous variable, if_ur_<sup>_m_</sup><br>_r,t_ <sup>= 1, it represents the</sup><br>status of reservoir_r_ in mode_m ∈{gen, pump}_,<br>at time interval _t_ [NA];|
|_v_<sup>_m,n_</sup><br>_g,t_|binary variable, transition variable between con-<br>figuration _m_ and configuration _n_ of PSHU _g_<br>during time interval _t_ [NA];|
|_q_<sup>_gen_</sup><br>_g,t_|continuous variable, amount of generation at a<br>PSHU _g_ during time interval _t_ [MW];|
|_q_<sup>_pump_</sup><br>_g,t_|continuous variable, amount of pumping load at<br>a PSHU _g_ during time interval _t_ [MW];|
|_qg,t_|continuous variable, amount of generation at unit<br>_g_ during time interval _t_ [MW].|
|Auxiliary|Variables [units]:|
|_f _<sup>_gen_</sup><br>_g,t_|continuous variable, energy opportunity cost of<br>_gen_configuration offered at PSHU_g_during time<br>interval _t_ [$ /hr];|
|_C_(_qg,t_)|cost function of generating unit _g_ [$ /hr].|



## I. INTRODUCTION 

## _A. Background and Motivation_ 

**P** UMPEDditional flexibilitystorage hydroto powerunits systems.(PSHU) couldThis flexibilityprovide ad-is 

ditional flexibilitystorage to powerunits systems.(PSHU) This flexibilityprovide is critical to enhance the reliability of modern power systems that are experiencing more uncertainties nowadays. There are a total of 40 pumped storage hydro (PSH) plants with over 22 GW capacity in the United States [1], which roughly equals 2% of U.S. generating capacity [1]. In the 2016 Hydropower Vision Report (DOE Report) [2], the investigation explores a range of growth scenarios, finding that the pumped storage capacity can increase in both the near term (2030), by 16.2 GW, and in the longer term (2050), by an additional 19.3 GW, for a total of 35.5 GW deployed by 2050 [2] (pp 17-19). However, the footprint and required topography for reservoirs pose significant regulatory challenges such as licensing and satisfying environmental requirements. 

One of the major benefits a PSHU brings to the system is it stockpiles excess electricity that enables base-load generators to stay on line when the net load is low. The number of expensive shut down and start up operations can be reduced 

2 

at those generators. The energy stored in a PSH reservoir is used to generate electricity later when it is needed. Therefore, the system overall operation cost is reduced. 

This load/generation-shifting effects are particularly useful in the current system with greater uncertainties on both generation and (net) load sides. In addition, a PSHU is able to provide a variety of services ranging from weekly and daily smoothing of load to providing hourly and subhourly reserves to responding to frequency control within a minute [3]. Such flexibility provided by PSHUs would significantly facilitate the integration of renewable resource with lower costs. 

However, these important and valuable services that are available from PSHUs have not been utilized largely due to the fact that PSHUs have not been fully optimized in the market. For example, the owners of PSHUs on the footprint of Midcontinent Independent System Operator (MISO) make their decisions of pumping and generating based on their forecast of market prices. 

This practice of PSH technology has two drawbacks: First, as a market participant with limited information about the market, the forecast of market prices can deviate significantly from the realization. Therefore, the decisions made based on the forecast would impair profits for the PSHU in short term and this would discourage the development and investment in the PSHU in long term; Secondly, the decisions made by PSHU are sub-optimal to the system welfare. That is, the benefits and the flexibility provided by PSHU are not fully exploited by the system under the current practice. 

To overcome the drawbacks of the current practice, introducing the PSHUs into MISO’s day-ahead unit commitment model is a first step. Therefore, a suitable model for PSHU in a unit commitment (UC) problem is studied in this paper. 

## _B. Literature Review_ 

One of the important benefits a PSHU can provide to a system is smoothing power injections from renewable resources; therefore, PSHU models have been widely discussed and deeply developed for operation with renewable resources. PSH models have also been studied in unit commitment problems and stand alone systems. 

In [4] and [5], a profit maximization problem is formulated for a single wind farm together with a PSH plant. A hybrid wind plus general storage plant model is presented in [6]. The impact of energy storage sizing on wind-hydro system operation and economics has been studied in [6], [7] and [8]. In these works, a PSH plant is modeled as two individual units: a pump and a generator. The state of charge of the storage is modeled with energy balance constraints across each pair of successive time intervals with efficiency lost. 

In [8], additional constraints are introduced to meet spinning reserve requirements or frequency regulation unit commitment requirements. The bidding and scheduling of a PSHU is studied as part of a generating company with hydro, thermal and PSHUs in [9]. In [10], stochastic joint optimization is used to maximize the profit of wind generation and PSHUs in an electricity market. 

In [4]-[10], the market prices are taken as an input for the profit maximization problem at a renewable-pumped storage 

hydro hybrid plant level. The feasibility of standalone solarpumped storage hydro and solar-wind-pumped storage hydro is studied in an island mode by [11] and [12]. 

Although these works provide a variety of models for a PSHU, incorporating a PSHU in an electricity market clearing process is not their major concern. The following paragraphs discuss formulations that are more suitable for incorporation in a market clearing process. 

A robust unit commitment problem with wind power and a PSHU is studied in [13]. A binary variable is introduced to indicate whether the unit absorbs (pumping) or generates electricity. In this model, a PSHU has to be either pumping or generating at a given time. However, for some PSH plants, due to their physical or operational limits, there are minimum outputs for each mode. That is, because of the minimum limits, the PSHUs are either generating or pumping at least at their minimum limits. However, at certain times in the day it may be the best to neither pump or generate. In other word, constantly charging or discharging the PSHU is not always the best strategy in the system operation. 

The introduction of an idle mode would allow a PSHU to turn off. The scheduling of PSHUs are modeled in a day-ahead market in [14] and [15]. Three modes, pumping, generating and idle are modeled for each of the pump storage units. However, the transitions between each pair of modes are not specifically modeled in these works. Therefore, some operation features, for example those related to transition time between modes of a PSHU, are either simplified or ignored. 

Some of the operation features of a combined cycle gas turbine unit in a day-ahead market are similar to those of a PSHU. In particular, we found the configuration based model used for combined cycle gas turbines (CCGTs) in unit commitment problem described in [16], [17] and [18] fits well with the operation of a PSHU. Similar to CCGTs, a PSHU can also be modeled with different operational configurations such as pumping and generating. An “alloff” configuration can be introduced to allow the unit to stay idle. 

## _C. Contributions_ 

This paper focuses on developing a new model for a PSHU in day-ahead market. The contributions are summarized below: 

- A configuration based PSHU model is developed in a unit commitment problem such that the flexibility of existing pumped storage hydro plants can be leveraged at the system level. 

- An “Alloff” configuration is introduced to allow the unit to stay idle at anytime within the operating window. Conveniently, offline supplemental reserve can be cleared for the “Alloff” configuration of a PSHU. What is more, transitions between each pair of modes are modeled specifically. The state of charge constraints are modeled for each reservoir included sharing of reservoirs by multiple units. 

- The compactness of the model is compared with configuration based combined cycle gas turbine models. 

- The proposed model is demonstrated in a test system and implemented in a MISO system with a benefit analysis and a computational study. 

3 

Notice that it is necessary to specifically model the transitions between different modes. The inter-temporal constraints related to the transitions such as min up/down time and transition time in a PSHU varies and can be accurately modeled. For example, the transition time needed from a generation mode to a pump mode may different from the transition time from an alloff mode to a pump mode. What is more, it is recognized that there is a fixed generation output pattern during a transition from one configuration to another in a combined cycle unit [19]. A similar pattern exists in the operation of some PSHUs. Having the transitions between different modes explicitly modeled enables the representation of these operational features and would make the model flexible and easy to extend into a market with various length of time intervals. 

The rest of the paper is organized as follows. Section II presents the proposed Mixed Integer Programming (MIP) formulation for PSHUs. The configuration based formulation is introduced in details and the compactness of the model is discussed. Section III gives numerical study results on a small test system and the large MISO system. A detailed benefit analysis is presented with MISO case studies. Section IV concludes this paper. 

## II. CONFIGURATION-BASED MODELING OF A PUMPED STORAGE HYDRO UNIT 

Section III. The third term in (1) represents the piece-wise linear production costs of the rest of generators in the system. 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0003-05.png)


<!-- Start of picture text -->
min q,u MM ( fg,t gen − C g,t pump qg,t pump ) + MM C ( qg,t ) .<br>g∈Gpsh t∈T g∈G t∈T<br>(1)<br><!-- End of picture text -->

_2) System Energy Balance Constraints:_ The generation has to be balanced with net load in the system at all times. In (2), during each interval _t_ , the total generation in the system including the generation from PSHUs on the left should be balanced with the sum of the net load and the pumping load from the PSHUs on the right. 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0003-07.png)


<!-- Start of picture text -->
MM qg,t  + qg,t gen =  Dt + qg,t pump , ∀t ∈T . (2)<br>g∈G g∈Gpsh g∈Gpsh<br><!-- End of picture text -->

_3) State and Transition Logic Constraints:_ Constraints (3) guarantee that the unit commitment variables of each mode in a PSHU described in Fig. 1 are mutually exclusive, as modeled for CCGTs in [20]: 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0003-09.png)


<!-- Start of picture text -->
M u m g,t = 1 , ∀g ∈Gpsh, ∀t ∈T . (3)<br>m∈Mg<br><!-- End of picture text -->

The transition between two modes _m, n_ in a PSHU _g_ at time _t_ is defined as a binary variable _vg,t_<sup>_m,n_.Noticethatthe</sup> start up and shut down of a mode are modeled as the transition between the mode and the _alloff_ mode. These constraints are modeled for CCGTs in [21]. 

## _A. Mathematical Formulation_ 

The configuration based modeling of PSHU represents all feasible operation modes of a PSHU. A pumped storage hydro plant can contain multiple units and each of them will be modeled individually. There are only three operation modes in a PSHU namely generating, pumping and offline. Transitions are allowed between each pair of these modes shown in Fig. 1. The “Mode 0” represents the state when the unit is offline. 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0003-13.png)


<!-- Start of picture text -->
Mode 0<br>Alloff<br>Mode 1 Mode 2<br>Generating Pumping<br><!-- End of picture text -->

Figure 1. Mode transition diagram of a PSHU in two consecutive periods. 

_1) Objective Function:_ The objective of the unit commitment problem is to minimize the system operating costs. Under MISO current practice, the costs related to a PSHU is the offered production costs of the generating mode minus the bid prices of the pumping mode which is reflected as negative costs in (1). These terms in box (1) will be removed from the objective ultimately because the operating cost of PSH is close to zero, but are presented here for the discussion in 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0003-16.png)


<!-- Start of picture text -->
u m g,t − u g,t m − 1 = M vg,t n,m − M vg,t m,n,<br>n∈M F,m g n∈M F,m g (4)<br>∀g ∈Gpsh, ∀m ∈M, ∀t ∈T .<br><!-- End of picture text -->

In addition to the mutual exclusivity constraints on the commitment variable of each configuration, there should be at most one feasible transition at any time [16]: 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0003-18.png)


<!-- Start of picture text -->
MM vg,t m,n ≤ 1 , ∀g ∈Gpsh, ∀t ∈T .<br>(5)<br>m∈Mg n∈M F,m g<br><!-- End of picture text -->

_4) Box constraints:_ The amount of pumping load during interval _t_ from the PSHU is constrained by the capacity of the reservoir and the capacity of the pump unit in (6). The pump = output of a PSHU will be forced to zero by (6) when _u_<sup>_pump_</sup> _g,t_ 0 indicating the unit is not in a pumping mode. Symmetrically, the amount of generation during interval _t_ from the PSHU is constrained by the capacity of the reservoir and the capacity of the generation unit shown in (7). The generation output of a PSHU will be forced to zero by (7) when _u_<sup>_gen_</sup> _g,t_<sup>= 0indicating</sup> the unit is not in a generating mode. 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0003-20.png)


<!-- Start of picture text -->
u pump g,t Qpump g ≤ qg,t pump ≤ u pump g,t min { Eηrg pump  − E r , Q p gump},<br>∀r ∈R, ∀g ∈Gpsh,r, ∀t ∈T .<br>(6)<br><!-- End of picture text -->


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0003-21.png)


<!-- Start of picture text -->
u gen g,t Q gen g ≤ qg,t gen ≤ ugen g,t min { ( Er − E r ) η g gen , Q g gen}, (7)<br>∀r ∈R, ∀g ∈Gpsh,r, ∀t ∈T .<br><!-- End of picture text -->

4 

_5) Storage Energy Balance and State of Charge (SOC) Constraints:_ The energy stored in the PSH system is linked at each consecutive time interval as shown in (8). Notice that there can be more than one PSHU sharing a reservoir in the model. Parameters _ηg_<sup>_gen_</sup> and _ηg_<sup>_pump_</sup> are the efficiencies of generating and pumping indicating energy loss in both modes. The energy stored in the reservoir at the beginning and end of the day is given by (9) and (10), respectively. The upper and lower bounds of the SOC are provided by (11). The state of charge constraints modeled in this paper are based on previous work [4]-[10]. 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0004-02.png)


<!-- Start of picture text -->
er,t +1 =  er,t  + � ηg pump qg,t pump − � qg, gen t ,<br>g∈Gpsh,r g∈Gpsh,r ηg gen (8)<br>∀r ∈R, ∀t ∈ [0 , |T | − 1] .<br><!-- End of picture text -->


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0004-03.png)


<!-- Start of picture text -->
er, 0 =  Er, 0 , ∀r ∈R. (9)<br><!-- End of picture text -->


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0004-04.png)


<!-- Start of picture text -->
er,|T | =  Er,|T |, ∀r ∈R. (10)<br><!-- End of picture text -->


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0004-05.png)


<!-- Start of picture text -->
Er ≤ er,t ≤ Er, ∀r ∈R, ∀t ∈T . (11)<br><!-- End of picture text -->

The start up and shut down time, transition time, minimum up/down time and security constraints are not listed here. They can be easily handled in the configuration based model. The details can be found in [16]. 

_6) Practical Operational Limits:_ To demonstrate the adaptability of the proposed configuration based PSH model to industry practice, two additional constraints are presented to reflect some of the physical limits the PSHUs have in their daily operations. 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0004-08.png)


<!-- Start of picture text -->
� � vg,t n,pump ≤ N,<br>g∈Gpsh,r n∈M F,pump g (12)<br>∀r ∈R, ∀t ∈T .<br><!-- End of picture text -->

At some PSH plant, due to the physical limits in the start up procedure of pump units, only a limited number of pump units can be brought online in a given time period. In constraints (12), _M_<sup>_F,pump_</sup> _g_ is the set of modes for which unit _g_ can feasibly transit to a _pump_ mode, bearing in mind that _vg,t_<sup>_n,pump_</sup> is the transition variable of unit _g_ from mode _n_ to the _pump_ mode. Therefore, without introducing new variables, constraints (12) precisely capture the operational feature that no more than _N_ units sharing reservoir _r_ can transit from any mode to a pumping mode in time interval _t_ . 

For the PSH plant with large reservoirs, there are typically multiple PSH units installed in the plant and they are jointly operated with the reservoirs. It is not economical and physically not feasible for the plant to have one unit pumping and another generating at the same time. To incorporate this feature for a PSH plant with multiple units, constraints (13) and (14) are introduced. 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0004-11.png)


<!-- Start of picture text -->
urr,t pump +  urr,t gen ≤ 1 , ∀r ∈R, ∀t ∈T . (13)<br><!-- End of picture text -->


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0004-12.png)


<!-- Start of picture text -->
u m g,t ≤ ur r,t m , ∀r ∈R, ∀g ∈Gpsh,r,<br>(14)<br>∀m ∈{gen, pump}, ∀t ∈T .<br><!-- End of picture text -->

A pair of variables _urr,t_<sup>_pump_</sup> _, urr,t_<sup>_gen_</sup> are introduced for a reservoir or a PSH plant _r_ to represent the status of the plant as pumping or generating at time interval _t_ . Therefore, constraints (13) are the mutual exclusivity constraints at the plant level with (14) constraining _u_<sup>_m_</sup> _g,t_<sup>whichisthecommitmentvariable</sup> of PSHU _g_ in mode _m_ at time interval _t_ . Constraint (14) indicates if any unit _g_ of the plant _r_ is in _pump_ mode then the plant status will be in _pump_ mode indicated by _urr,t_<sup>_pump_</sup> = 1. The same for the _gen_ mode. Notice that since _u_<sup>_m_</sup> _g,t_<sup>isbinary,</sup> _urr,t_<sup>_m_canbecontinuousandboundedby(13)and(14).</sup> Combining (13) and (14), if any unit in a reservoir is generating at a time interval, all the other units sharing the same reservoir would not pump at the same time interval and vice versa. 

## _B. Compactness of the Proposed Formulation_ 

This section analyzes the scale of the proposed model in comparison with the configuration based combined cycle gas turbine model in [16] and [21]. The proposed model is formulated via constraints (3)-(14). Compared to the combined cycle model in [16] and [21], storage related constraints (8)-(14) represent the major differences. The impacts of the storage related constraints to computational complexity of the problem is analyzed with following parameters: 

- Number of Variables: There is only one continuous variable at each time interval for a reservoir. Two additional continuous variables are needed for each reservoir to enforce the mutual exclusivity constraints at the reservoir level if there are multiple PSHUs operating in the same reservoir. 

- Number of Constraints: The increases in the number of constraints on storage energy balance (8), state of charge (11), the pump start up constraints (12) and plant level mutual exclusivity constraints (13)-(14) are proportional to the number of reservoirs and the number of time intervals. 

- Number of Non-zeros: There are only a few non-zeros added by each constraint of (9)-(14). However, the intertemporal storage energy balance constraint (8) would introduce more non-zeros depending on the number of PSHUs sharing the reservoir. 

The impacts of the storage related constraints on problem computational complexity are moderate except for the storage energy balance constraints (8). Particularly, because it is common that multiple units share a reservoir in a PSHU, the increase of non-zeros per constraint can be significant. 

## III. NUMERICAL RESULTS 

In this section, first, the current PSHU model at MISO is introduced and compared with the proposed model in a case study with two PSHUs. Then, the proposed model is applied to a MISO system. Benefit analyses and computational studies are presented. 

5 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0005-01.png)


<!-- Start of picture text -->
PSH Current 1400<br>PSH Proposed<br>1200<br>LMP<br>1000<br>30<br>800<br>600 MW<br>$/MWh 20<br>15<br>400<br>200<br>Dispatched<br>-200<br>Pump Bid 10 15 20<br>Window Hours<br><!-- End of picture text -->

Figure 2. Small Case Study: PSHU Dispatch Results. 

## _A. Two Units Case Study_ 

A day ahead unit commitment (UC) and economic dispatch (ED) problem formulated in (1) - (11) is solved with a 24 hours net-load scenario. The results from current MISO model and proposed model will be compared. For the sake of a simple and clear illustration, the practical operational limits in (12)(14) are not included, minimum up/down time, reserve requirements, ramp constraints, and transmission security constraints are ignored in this small case study. 

Table I shows the units considered in this case study. The two pumped-storage hydro units that share a reservoir have the same parameters for both Pump and Gen modes as listed once in the table. Three thermal generators with different capacities and different costs are included to represent the generations besides pumped-storage hydro units in the system. For a simple presentation, the marginal generation costs and bid prices are constants over feasible generation and consumption levels and independent of time for all units. Notice that pumping in both units are “block loaded” meaning that the pumping load is either at a predetermined level or zero. This is a typical operating feature of the pumped-storage hydro units in the MISO system. The energy efficiency of the pumping and generating processes are identical in both units. 

Table I UNIT PARAMETERS 

|Unit|Cost/Price|_q_<br>_m_|_q_<sup>_~~m~~_</sup>|_η_<sup>_m_</sup><br>_g_|
|---|---|---|---|---|
||$/MWh|MW|MW||
|PSHU Pump|24|200|200|0_._9|
|PSHU Gen|26|100|200|0_._9|
|Thermal Gen 1|30|0|600|NA|
|Thermal Gen 2|20|0|400|NA|
|Thermal Gen 3|15|0|500|NA|



The energy price at each node in the transmission network or locational marginal price (LMP) is the dual value at the energy balance constraint in (2) after the problem been solved. Notice that since there is no transmission network constraint in this case study, there is a single marginal price for the whole system at every time interval. 

_1) Current PSHU Model at MISO:_ In the current MISO day ahead market, PSHUs offer opportunity costs and bid prices for their generation and pump mode, respectively. State of charge limits for their reservoirs are not enforced explicitly by the system operator. Instead, a maximum daily electricity generation limit is submitted and applied to PSHUs for their generation modes. The PSHU owner determines the pump/generate window. For example, the owner may bid one of their units as pumping load only between 0 _−_ 4 AM and that generation can occur during the rest of the day. 

The PSHU result using the current MISO model is compared with the results from the proposed model in Fig. 2. The PSHU outputs from the current model are represented by shaded blue bars and the PSHU outputs from the proposed model are represented by red solid bars. Notice that net-load _Dt_ and PSH output are aligned with the axis on the right in units of MW while LMP aligns with the axis on the left in units of $/MWh. The negative bars indicate the pumping load of the PSHU and the positive bars indicate the generation of the PSHU. Net-load in this paper is defined as the system fixed demand minus the renewable generations not including pumped-storage hydro units. 

Although state of charge are not represented in the market clearing process in the current model, it is incorporated in the owner’s bid and offer. For instance, the owner bid only one of their units for pumping for five hours starting at _t_ = 0 and ending at _t_ = 4 indicated as the “Pump Bid Window” in Fig. 2, such that if all their bids are cleared the reservoir would be charged to full at _t_ = 4. 

The bid prices for pump loads submitted by the pumpedstorage unit owners represent their willingness to purchase and consume the electricity in the pumping modes. The bid prices are calculated based on the owner’s forecast of the system LMP and this forecast is unlikely to be accurate. In the example of current model shown in Fig. 2, the bid prices for pump mode lead the system to clear the PSHUs to pump and fill the reservoir in the first five hours while losing the opportunity to pump in hour 5 and hour 6 with low generation costs and LMP. This myopic situation would impair the profits of the pumped-storage hydro unit owners and, in the meantime, the solution of the UC and ED problem deviates from a maximum social welfare. The myopic situation result from owner’s bid and offer and the negative impacts on the system production cost in the current model will be further discussed in the MISO case study in section III-B with realistic scenarios. 

_2) Proposed PSHU Model:_ In the proposed model, PSHUs do not submit offer/bid nor determine the scheduling window. Instead, they are fully optimized in the day-ahead market. State of charge of the reservoir is managed at the system level. In this study, the minimum and maximum energy capacity of the reservoir along with the state of charge of the reservoir at the beginning and the end time interval are listed in Table II. The state of charge at the end of the day is required to return to the same level as the start, such that energy used for generation from the pumped-storage hydro units has to be stored earlier or recharged later within the studied time range. Noticed that the SOC limits listed in Table II are explicitly modeled in the 

6 

proposed model while those limits are implicitly incorporated in the owner’s bid and offer in the current model as described in the previous section III-A1. 

||R|Table II<br>ESERVOIR|||
|---|---|---|---|---|
||_Er_|_Er_|_Er,_1|_Er,T_+1|
||MWh|MWh|MWh|MWh|
|Reservoir|1000|3500|2600|2600|



Thereafter, the bid price for pump loads is removed from the system objective. In addition, assume the generation costs for a PSHU is zero and ignore operation and maintenance costs and capital costs, the objective only contains the generation costs of the rest of the generators in the system besides the PSHUs as shown in (1’). 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0006-04.png)


<!-- Start of picture text -->
q,u,v,e min � � C ( qgt ) (1’)<br>g∈G t∈T<br><!-- End of picture text -->

The PSHU solutions from the proposed model are indicated as red bars in Fig. 2. Compare to the results from the current model, it can be observed that the same total amount of pumping energy is dispatched by the proposed model in the “Dispatched Pump Window” but the timing is shifted to when the system net-load is the lowest and accordingly with the lowest LMP. This improvement is beneficial in two perspectives. First, from the system operator point of view, overall system generation costs are reduced. The results in Fig. 2 demonstrate the load shifting effects of pump storage hydro units have been improved in the proposed model. PSHUs contribute more to reduce the system generation costs and to maximize the social welfare. Second, for PSHU owners, they are charged less for their pumping load with the proposed model. Given the same generation income in this case, the PSHU owner’s profits are improved. A detailed cost benefit analysis of the proposed model in a realistic MISO system is provided in Section III-B. 

## _B. MISO Case Study_ 

In this study we use a MISO case that includes 1,085 generators. Reserve requirements and transmission security constraints are included for all studies. Constraints on individual generators such as, minimum up/down time, maximum start up time, ramp constraints are included for all units including PSHUs with proposed model. We perform all tests on a 2 _._ 2-GHz quad-core Intel Xeon CPU E5-2699 with 32 GB Ram; all optimization problems are solved with Gurobi 8.0. 

The proposed generic model in (1)-(11) has been implemented for a pumped storage hydro plant with multiple pumping and generating units in the MISO prototype day ahead security constrained unit commitment tool [22]. The capacities of the unit for both pumping and generating are in GWs. An empirically hard to solve 36-hour load scenario from MISO historical data library is selected for the computational study. There are three peaks in the scenario. The highest and lowest hourly demand are 91 _._ 6 GW and 70 GW respectively. 

_1) Computational Study:_ Table III shows the computational results of different models: 

- Hippo: A High-Performance Power-Grid Optimization (Hippo) tool [22]. MISO current pumped storage hydro model introduced in Section III-A1 is applied; 

- Hippo + PSH: MISO current model is replaced by proposed pumped storage hydro model in Hippo; 

- Hippo + CC: Hippo with configuration based combined cycle model [23]. 

The test case and load scenario with Hippo has been benchmarked with MISO production day-ahead market engine. Therefore Hippo is used as a benchmark for this study. As introduced in Section III-A1, the PSHU currently offer costs and bid prices for their generation and pump mode respectively. State of charge of their reservoirs are not enforced by the system operator, instead, maximum daily generation is applied. Also, The pump/generate window for the unit are fixed. In Hippo + PSH, the particular PSHU is represented by the proposed model. In addition, a component-configuration based combined cycle model [16] that had been tested with Hippo is used for a comparison. 

|C|Table III<br>OMPUTATIONALRESULTS||
|---|---|---|
|Model|Hippo<br>Hippo + PSHU|Hippo + CC|
|Mip gap at 1200s|0.11 %<br>0.16 %|0.28 %|



Table III shows the computational performance of all three MIPs at the cutoff time. The day ahead market cutoff solving time in MISO is 1200 seconds. Solutions with MIP gap limit lower than 1% will be accepted according to the MISO operating guide. Since the MIP gap of three models are below 1%, the results are considered acceptable in MISO operation. Because of the limited number of PSHUs and the proposed tight formulation, there is only a moderate increase in the computational difficulty compared to the benchmark Hippo model. 

_2) Benefit Analysis:_ In this section, the proposed model is benchmarked with the current model in examples based on real data in an actual day in MISO system. 

To make a fair comparison between the proposed model and the current model, given a start state of a reservoir and round-trip efficiency of the PSHU, the realized state of the reservoir at the last hour of the day from the results of the current model is applied to the proposed model. That is, the total energy charged to or discharged from the reservoir in each day in the simulation are the same for both models. To lay out a more realistic benefit analysis, the minimum SOC and maximum SOC of a reservoir in the proposed model is calculated from the results of current model. To be precise, the minimum SOC is calculated as the start state of the reservoir minus the effect of the generation cleared by the current model considering the efficiency. Similarly, the maximum SOC is the start state of the reservoir plus pumping cleared by the current model considering the efficiency. The PSHU parameters in the proposed model are summarized below. 

- The SOC of a reservoir at the beginning of the day hour 

   - 0 is given. 

7 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0007-01.png)


<!-- Start of picture text -->
SOC<br>MAX<br>364 S/MWh<br>3.1 S/MWh/<br>SOC<br>START<br>MWh 21.6 S/MWh<br>PSH Current<br>PSH Proposed<br>SOC Current<br>SOC LMPSOC Proposed<br>END<br>10 15 20<br>Hours<br><!-- End of picture text -->

Figure 3. MISO Case Study Results: PSHU 1. 

- The SOC of a reservoir at the end of the day hour 24 is calculated from the results of the current model and is fixed in the proposed model. 

- The SOC min and max are calculated from the results of the current model and are fixed in the proposed model. 

- All the other unit parameters (such as min up/ down time, ramp rate etc.) in the proposed model are copied from the production offer in the current model. 

As shown in Fig. 3, the dispatch results of a PSHU in MW (aligned with the axis on the right side of the figure) from proposed model (solid red bars) are compared with current model (shaded blue bars). Notice that the positive side of the axis indicates generation and the negative side indicates pumping. The blue and red solid lines indicate the SOC of the current model and proposed model respectively with axis on the left using unit MWh. The dashed green line gives the trend of the Locational Marginal Price (LMP) at the PSHU connection node in the proposed model. 

Due to the tight SOC limits at PSHU 1, the dispatch results of the unit in current model and proposed model are very close as shown in Fig. 3. In fact, the total amount of pumping and generation are the same in both models. However, the pump load and generation are allocated at slightly different periods in the day. The differences are highlighted in the black boxes with time indexes in Fig. 3. Comparing the proposed model to the current model, it can be observed that the same amount of pump load is shifted from _t_ = 0 to _t_ = 3 when LMP is lower. On the generation side, it can also be observed that some generation is shifted from _t_ = 15 to _t_ = 16 when LMP is higher. Although the differences between the current model and the proposed model are small for PSHU 1, this indeed demonstrate the centralized optimal effects of the proposed model against the current model in a very precise and concrete way. As the results show, the proposed model would find the optimal solution that allocates the pump load to the intervals when the system is least stressed as indicated by the lower LMPs and allocates the generation to the intervals when the system is most stressed as indicated by the higher LMPs. 

The same study has been applied to a different PSHU 2, as the results are shown in Fig. 4. The PSHU parameters of the 


![](images/Biemer_2021_Grammar_Based_Procedural_Glitch_Synthesis.pdf-0007-09.png)


<!-- Start of picture text -->
0OS<br>MAX<br>SOC<br>START<br>MWh<br>SOC<br>END<br>PSH Current<br>PSH Proposed<br>SOC Current<br>SOC Proposed<br>LMP<br>10 15 20<br>Hours<br><!-- End of picture text -->

Figure 4. MISO Case Study Results: PSHU 2. 

unit in the proposed model are estimated in the same way from current model. The notations in Fig. 4 are exactly the same with Fig. 3. The key observation from Fig. 4 is, due to the fact that PSHU 2 has a larger reservoir and larger generate/pump capacities than PSHU 1, the proposed model would shift more pump loads and generations to optimal positions highlighted in the black dashed ellipses. Compared to results in Fig. 3, the benefits of the proposed model are more significant for the PSHU with a larger reservoir and larger generation and pump capacities. 

To briefly sum the qualitative benefits, especially shown in Fig. 4, the PSHU becomes more active and flexible with the proposed model compared to the current model. From the results of both units in Fig. 3 and Fig. 4, the pumping and generation from proposed model follows the system conditions closer than the current model, that is, with the proposed model, the PSHU pumps more when the LMP is low and generate more when the LMP is high. In the current model, a PSHU is dispatched based on the bid and offer from the unit owner. In particular, pumping is restricted to specific hours based on the owner forecast of minimum prices, but the minimum prices often occur at different times to that forecast. Inherently because a unit owner has limited system information, the PSHU owner can not perform better than the system operator on forecasting the system conditions in the Day-ahead Market. This gap between the current model and the proposed model would be enlarged if the system become more dynamic and even harder for the unit owner to predict. For example, the flexibility of the unit and the system optimality from proposed model will be more significant when more renewable especially solar generations are included in the system. 

||Tab<br>BENEFIT|le IV<br>ANALYSIS|||
|---|---|---|---|---|
||System|PSHU 1|PSHU 2|PSHU 3|
||Objective [$]|Profit [$]|Profit [$]|Profit [$]|
|Improvement %|0_._4%|1%|10_._8%|6%|



The benefits of the proposed model demonstrated in Fig. 

8 

3 and Fig. 4 are quantified and summarized in Table IV. The unit commitment solutions of the rest generation units in the system other than the three PSHU from the current model are fixed to the proposed model, such that the results shown in Table IV mainly reflects the impacts of the proposed model on the PSHUs. The reduction in system objective from the proposed model is shown as the percentage of the system objective of the current model. At the same time, the profit increment for the PSHU owners from the proposed model are shown as percentages of their profits result from current model. PSHU 2 and 3 have larger reservoirs and larger generate/pump capacities, therefore the proposed model gained more significant improvement compare to PSHU 1. A more realistic calibration of benefits can be done by considering both day ahead and real time market. However, the results in this study demonstrate that the proposed model would improve both social welfare and PSHU owner’s profits assuming perfect forecast in day ahead market. We will leave the multi-stage market study to the future work. 

In addition, the scenario used in this study is from historical data library and has less renewable interconnections. According to current MISO generation interconnection queue [24], significant amount of renewable units are likely to be interconnected in the near future. In a system with more variations and intermittencies, the value of the flexibility from a PSHU is expected to be further escalated with the proposed model. 

## IV. CONCLUSION AND FUTURE WORK 

The current model for PSHU in MISO day-ahead market is rigid and leads to less economic dispatch solutions. In this study, we propose a new formulation of PSHU that enhances the flexible dispatch of the unit in day-ahead market. A MISO case study shows the proposed model improves system welfare and increases PSHU owners’ profits. 

Although this paper focuses on the modeling of a PSHU in a day ahead market, the proposed configuration based model can be applied to other storage resources with multiple operating modes and states of charge. Also, by specifically modeling the transitions, the proposed model can be easily extended to include detailed operational features during transitions in a PSHU in a market with smaller time intervals. The numerical results show the applicability and scalability are promising for large systems. 

## ACKNOWLEDGMENT 

This material is based upon work supported, in part, by the U.S. Department of Energy’s Office of Energy Efficiency and Renewable Energy (EERE) under the Water Power Technologies Office Award Number DE-EE0008781. 

## REFERENCES 

- [1] “Pumped storage provides grid reliability even with net generation loss,” July 2013, https://www.eia.gov/todayinenergy/detail.php?id= 11991[Online; posted 08-July-2013]. 

- [2] DOE, “Hydropower vision report,” July 2016, https://www.energy. gov/eere/water/downloads/hydropower-vision-report-full-report[Online; posted 2016]. 

- [3] J. P. Barton, D. G. Infield _et al._ , “Energy storage and its use with intermittent renewable energy,” _IEEE transactions on energy conversion_ , vol. 19, no. 2, pp. 441–448, 2004. 

- [4] E. D. Castronuovo and J. P. Lopes, “On the optimization of the daily operation of a wind-hydro power plant,” _IEEE Transactions on Power Systems_ , vol. 19, no. 3, pp. 1599–1606, 2004. 

- [5] ´A. J. Duque, E. D. Castronuovo, I. S´anchez, and J. Usaola, “Optimal operation of a pumped-storage hydro plant that compensates the imbalances of a wind power producer,” _Electric Power Systems Research_ , vol. 81, no. 9, pp. 1767–1777, 2011. 

- [6] M. Korpaas, A. T. Holen, and R. Hildrum, “Operation and sizing of energy storage for wind power plants in a market system,” _International Journal of Electrical Power & Energy Systems_ , vol. 25, no. 8, pp. 599– 606, 2003. 

- [7] E. D. Castronuovo and J. A. P. Lopes, “Optimal operation and hydro storage sizing of a wind–hydro power plant,” _International Journal of Electrical Power & Energy Systems_ , vol. 26, no. 10, pp. 771–778, 2004. 

- [8] P. D. Brown, J. P. Lopes, and M. A. Matos, “Optimization of pumped storage capacity in an isolated power system with large renewable penetration,” _IEEE Transactions on Power systems_ , vol. 23, no. 2, pp. 523–531, 2008. 

- [9] E. Ni, P. B. Luh, and S. Rourke, “Optimal integrated generation bidding and scheduling with risk management under a deregulated power market,” _IEEE Transactions on Power Systems_ , vol. 19, no. 1, pp. 600– 609, 2004. 

- [10] J. Garcia-Gonzalez, R. M. R. de la Muela, L. M. Santos, and A. M. Gonzalez, “Stochastic joint optimization of wind generation and pumpedstorage units in an electricity market,” _IEEE Transactions on Power Systems_ , vol. 23, no. 2, pp. 460–468, 2008. 

- [11] T. Ma, H. Yang, L. Lu, and J. Peng, “Pumped storage-based standalone photovoltaic power generation system: Modeling and techno-economic optimization,” _Applied energy_ , vol. 137, pp. 649–659, 2015. 

- [12] T. Ma, H. Yang, L. Lu, and J. Peng, “Technical feasibility study on a standalone hybrid solar-wind system with pumped hydro storage for a remote island in Hong Kong,” _Renewable Energy_ , vol. 69, pp. 7–15, 2014. 

- [13] R. Jiang, J. Wang, and Y. Guan, “Robust unit commitment with wind power and pumped storage hydro,” _IEEE Transactions on Power Systems_ , vol. 27, no. 2, p. 800, 2012. 

- [14] M. E. Khodayar, M. Shahidehpour, and L. Wu, “Enhancing the dispatchability of variable wind generation by coordination with pumped-storage hydro units in stochastic power systems,” _IEEE Transactions on Power Systems_ , vol. 28, no. 3, pp. 2808–2818, 2013. 

- [15] N. Li and K. W. Hedman, “Enhanced pumped hydro storage utilization using policy functions,” _IEEE Transactions on Power Systems_ , vol. 32, no. 2, pp. 1089–1102, 2016. 

- [16] Y. Chen and F. Wang, “MIP formulation improvement for large scale security constrained unit commitment with configuration based combined cycle modeling,” _Electric Power Systems Research_ , vol. 148, pp. 147–154, 2017. 

- [17] B. Blevins, “Combined-cycle unit modeling in the nodal design,” _ERCOT, Taylor, Texas_ , 2007. 

- [18] H. Hui, C. N. Yu, F. Gao, and R. Surendran, “Combined cycle resource scheduling in ercot nodal market,” in _Power and Energy Society General Meeting_ . IEEE, 2011, pp. 1–8. 

- [19] B. Hua, B. Huang, R. Baldick, and Y. Chen, “Tight formulation of transition ramping of combined cycle units,” _IEEE Transactions on Power Systems_ , vol. 35, no. 3, pp. 2167–2175, 2020. 

- [20] C. Liu, M. Shahidehpour, Z. Li, and M. Fotuhi-Firuzabad, “Component and mode models for the short-term scheduling of combined-cycle units,” _IEEE Transactions on Power systems_ , vol. 24, no. 2, pp. 976–990, 2009. 

- [21] G. Morales-Espa˜na, C. M. Correa-Posada, and A. Ramos, “Tight and compact MIP formulation of configuration-based combined-cycle units,” _IEEE Transactions on Power Systems_ , vol. 31, no. 2, pp. 1350–1359, 2016. 

- [22] F. Pan, Y. Chen, D. Sun, and E. Rothberg, “High-performance powergrid optimization (HIPPO) for flexible and reliable resource commitment against uncertainties,” 2016, https://arpa-e.energy.gov/sites/default/files/ 13 <u>PNNL GD OP-15 HIPPO2 public.pdf[Online;</u> posted 2016]. 

- [23] C. Dai, Y. Chen, F. Wang, J. Wan, and L. Wu, “A configurationcomponent based hybrid model for combined-cycle units in MISO dayahead market,” _IEEE Transactions on Power Systems_ , 2018. 

- [24] MISO, “MISO GIQ web overview,” 2019, https://www.misoenergy.org/ planning/generator-interconnection/GI <u>Queue/[Online;</u> posted 2019]. 

