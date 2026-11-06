**Optical simulation of the free Dirac Equation** 

Thais L. Silva,<sup>1, ∗</sup> E. R. F. Taillebois,<sup>2</sup> R. M. Gomes,<sup>2</sup> S. P. Walborn,<sup>1</sup> and Ardiley T. Avelar<sup>2</sup> 

> _1Instituto de Física, Universidade Federal do Rio de Janeiro, 21941-972, Rio de Janeiro, Rio de Janeiro, Brazil_ 

> _2Instituto de Física, Universidade Federal de Goiás, 74.690-900, Goiânia, Goiás, Brazil_ 

We present a classical optics simulation of the one-dimensional Dirac equation for a free particle. Positive and negative energy components are represented by orthogonal polarizations of a free propagating beam, while the spatial profile represents the spatial wave function of the particle. Using a completely tunable time parameter, we observed the oscillation of the average value of the Dirac position operator–known as _Zitterbewegung_ (ZB). We are also able to measure the so called mean-position operator which is a single-particle observable and presents no oscillations. Our work opens the way for optical simulation of interesting phenomenon of relativistic systems, as well as condensed-matter physics, without any requirement for specially engineered medium. 

PACS numbers: 

# **I. INTRODUCTION** 

Although the Dirac equation [1] represents a historical landmark in the quantum description of relativistic systems – satisfactorily explaining the origin of spin and predicting the existence of antimatter [2] – it still provokes a lot of discussion about its interpretation, even when applied to describe the simplest physical system, that is, a free particle. In this case, the Dirac equation predicts intriguing phenomena, for instance the ZB [3] and Klein’s paradox [4], which impede the single-particle (SP) interpretation of the Dirac equation. As fundamental effects in the understanding of relativistic influence over quantum theory, they have contributed to the transition to the many-body quantum field approach [5]. 

The important technical difficulties involved in the direct observation of several relativistic quantum predictions have led to an increased interest in their simulations in trapped ions [6, 7], photonic crystals [8], confined light [9], graphene [10], optical superlattices [11], BoseEinstein condensates [12, 13] and ultracold atoms [14]. Among the unexpected effects of Dirac equation, the ZB – the flickering motion of a free relativistic quantum particle described by a Dirac wavefunction with positive and negative energy components – is one of most investigated due to its interesting counterintuitive nature. 

Despite the previous studies [6, 11, 12], an important feature was not explored: the Dirac position operator related to the flickering motion is not a SP observable, i.e. it cannot be written as the direct sum of its positive and negative energy projections. From a SP perspective, Dirac’s equation must be interpreted as the simultaneous solving of two independent problems, for instance, the single free evolution of both electron and positron. Therefore, there is no meaning in assigning a physical interpretation to an operator that is not SP. This fact can be well understood by making explicit the connection between the theory of irreducible unitary representations of the Poincaré group and the explicitly covariant reducible 

representation associated to Dirac’s equation [15]. In the SP approach, physical results must be obtained by projecting SP observables over the subspace corresponding to the problem of interest. 

For Dirac’s theory, a SP position observable exists and is obtained using the so-called Foldy–Wouthuysen transformation (FWT) [16] – a momentum dependent unitary transformation that diagonalizes Dirac’s Hamiltonian and is at the kernel of important algorithms used to obtain quantum relativistic corrections [17, 18]. This observable is often called mean-position operator and does not exhibit the oscillatory behavior characteristic of the ZB, a result that generates doubts concerning its actual existence. 

Here, the simulation of the Dirac one-dimensional free evolution and the ZB is performed using the transverse degrees of freedom of a paraxial light beam, where different components of the spinor are represented by different polarization components of the beam. This physical setup is well suited for the purpose of quantum simulation, as it allows for implementation of the dynamical phases with easy tuning of the important physical parameters [19]. Besides being a proof-of-concept for the optical simulation of Dirac particles, the present approach differs from others in the theoretical procedure adopted to perform the simulation. Previous works perform a direct simulation of the 1+1D Dirac Hamiltonian, while the present approach performs the evolution in the diagonalized Foldy–Wouthuysen representation (FWR) and permits one to switch back and forth between this and Dirac’s representation, allowing us to investigate the behavior of both the Dirac position and the mean-position operators. 

2 

# **II. DIRAC EQUATION AND POSITION OPERATOR** 

Consider the 1D Dirac equation 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0002-03.png)


<!-- Start of picture text -->
i ℏ ∂t ∂ ψD = Hˆ DψD = ( cpσ ˆ 1 +  mc 2 σ 3) ψD, (1)<br><!-- End of picture text -->

where _c_ is the speed of light, _p_ ˆ is the momentum operator, _m_ is the mass of the particle, and _σi_ are the usual Pauli matrices. The information of this system is encoded in the spinor _ψD_ that has only two components which are related to positive and negative energy states in the particle’s rest frame, i.e. spin degrees of freedom are eliminated by the dimensional constrain [20]. In Dirac’s coordinate representation, the momentum operator _p_ ˆ assumes the usual form − _i_ ℏ _∂x_<sup>_∂_,where</sup><sup>_x_isthe</sup> so-called Dirac coordinate associated to the multiplication operator _x_ ˆ _DψD_ ( _x_ ) = _xψD_ ( _x_ ). Since the Hamiltonian operator is not diagonal in this representation, the positive and negative energy eigenstates are nontrivial and assume, respectively, the forms _ψp_<sup>+(</sup><sup>_x, t_)=</sup> _u_ ( _p_ ) _e_<sup>−</sup><sup>_iε_(</sup><sup>_p_)</sup><sup>_t/_ℏ</sup> _e_<sup>_ipx/_ℏ</sup> and _ψp_<sup>−(</sup><sup>_x, t_)=</sup><sup>_v_(</sup><sup>_p_)</sup><sup>_eiε_(</sup><sup>_p_)</sup><sup>_t/_ℏ</sup><sup>_e_−</sup><sup>_ipx/_ℏ,</sup> with _ε_ ( _p_ ) ≡ �( _mc_<sup>2</sup> )<sup>2</sup> + ( _pc_ )<sup>2</sup> , _u_ ( _p_ ) = [2 _mc_<sup>2</sup> ( _ε_ ( _p_ ) + _mc_<sup>2</sup> )]<sup>−1</sup><sup>_/_2 �</sup> _ε_ ( _p_ ) + _mc_<sup>2</sup> _cp_<sup>�</sup><sup>_T_</sup> and _v_ ( _p_ ) = [2 _mc_<sup>2</sup> ( _ε_ ( _p_ ) + _mc_<sup>2</sup> )]<sup>−1</sup><sup>_/_2 �</sup> _cp ε_ ( _p_ ) + _mc_<sup>2�</sup><sup>_T_</sup> . 

The non-diagonal form of H<sup>ˆ</sup> _D_ in Dirac’s representation is evinced by the commutator [ H<sup>ˆ</sup> _D,_ ˆ _xD_ ] = − _ic_ ℏ _σ_ 1 and leads to the Heisenberg picture evolution given by [21] 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0002-06.png)


<!-- Start of picture text -->
x ˆ D ( t ) =ˆ xD (0) +  c 2 p ˆH ˆ D −1 t<br>(2)<br>− c ℏHˆ D −1 e 2 i H ˆ Dt/ ℏ − 1 cp ˆH ˆ D −1 − σ 1 .<br>2 i � �� �<br><!-- End of picture text -->

The first two terms on the right represent the expected linear time evolution of a free particle, the last term being associated to the ZB. This flickering motion is accompanied by other particularities of the _x_ ˆ _D_ operator. Indeed, the evolution given in (2) is derived from the equation of motion _x_ ˆ<sup>˙</sup> _D_ = ℏ _i_<sup>[ ˆH</sup><sup>_D,_ˆ</sup><sup>_xD_]=</sup><sup>_cσ_1</sup><sup>_,_whichimpliesthat,</sup> although ⟨ _x_ ˆ<sup>˙</sup> _D_ ⟩ = ⟨ _c_<sup>2</sup> _p_ ˆH<sup>ˆ</sup> _D_<sup>−1⟩,theeigenvaluesassociated</sup> to the velocity _x_ ˆ<sup>˙</sup> _D_ are restricted to ± _c_ , a remarkable result which contributes to raise doubts as to the correct interpretation of _x_ ˆ _D_ as definition of position. These peculiarities of the operator _x_ ˆ _D_ arise from the fact that this is not a SP observable, i.e. _x_ ˆ _D_ ̸ = _P_<sup>ˆ</sup> + _x_ ˆ _DP_<sup>ˆ</sup> +<sup>†+</sup><sup>_P_ˆ−</sup><sup>_x_ˆ</sup><sup>_D_ˆ</sup><sup>_P_</sup> −<sup>†,</sup> where _P_<sup>ˆ</sup> _ǫ_ = 2 _mc_ 1<sup>2</sup> � _mc_<sup>2</sup> _ǫcp_ + _ǫε_ ( _p_ ) _mc_ −<sup>2</sup> − _ǫcpǫε_ ( _p_ ) � is the projection operator over the subspace of states with energy sign _ǫ_ . To obtain a SP position, the FWT must be applied to diagonalize the Dirac Hamiltonian. For the 1D Dirac free particle, this canonical transformation is given by the momentum dependent unitary operator _U_<sup>ˆ</sup> (ˆ _p_ ) = _e_<sup>_iS_ˆ(ˆ</sup><sup>_p_)</sup> with _S_ ˆ(ˆ _p_ ) ≡ _σ_ 22<sup>tg−1 �</sup> _mcp_ ˆ �. In the resulting FWR, the original Dirac Hamiltonian is given by H<sup>ˆ</sup> _D_<sup>′=</sup><sup>_σ_3</sup><sup>_ε_(ˆ</sup><sup>_p_),and</sup> 

the former _x_ ˆ _D_ operator by _x_ ˆ<sup>′</sup> _D_<sup>=</sup><sup>_x_ˆ</sup><sup>_F W_+</sup> 2<sup>ℏ</sup> _ε_<sup>_mc_</sup> ( _p_ )<sup>32</sup><sup>_σ_2,where</sup> _x_ ˆ _F W_ is the new multiplication operator in the FWR. The operator _x_ ˆ _F W_ is the so called mean-position operator and, unlike the operator _x_ ˆ _D_ , it is a SP observable since _x_ ˆ _F W_ = _P_<sup>ˆ</sup> +<sup>′</sup><sup>_x_ˆ</sup><sup>_F WP_ˆ</sup> +<sup>′+</sup><sup>_P_ˆ</sup> +<sup>′</sup><sup>_x_ˆ</sup><sup>_F WP_ˆ</sup> +<sup>′,where</sup><sup>_P_ˆ</sup> _ǫ_<sup>′=</sup> � _δǫ_ 0+ _δǫ_ 0− � are the energy projectors in the new representation. Aside from being SP, the operator _x_ ˆ _F W_ also satisfies the equation _x_ ˆ<sup>˙</sup> _F W_ = _c_<sup>2</sup> _p_ ˆH<sup>ˆ</sup> _D_<sup>′,resultingintheHeisenberg</sup> picture evolution [21] 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0002-09.png)


<!-- Start of picture text -->
x ˆ F W  ( t ) = x ˆ F W  (0) +  c 2 p ˆH ˆ D ′−1 t (3)<br><!-- End of picture text -->

that is linear in time, as expected for a free particle. Thus, as stated before, the ZB does not occur for this operator. Here, as a proof-of-concept for the simulation of relativistic systems using free propagating light beams, the simulation of both the Dirac and FWRs will be performed in a single setup. This difference with other simulation procedures open the possibility for future investigations on more complex FWTs associated to relativistic scenarios involving interactions. 

# **III. SIMULATION PROTOCOL AND EXPERIMENT** 

One way to simulate the dynamics associated to Eq. (1) is to directly implement the evolution opera−<sup>_i_</sup> H<sup>ˆ</sup> _D t_ tor exp ℏ , which is usually a tough task due to � � the non-diagonal character of H<sup>ˆ</sup> _D_ . This difficulty can be overcome by using the FWT, since this transformation allows the time evolution operator to be written as −<sup>_i_</sup> H<sup>ˆ</sup> _D t_ −<sup>_i_</sup> H<sup>ˆ′</sup> _D_<sup>_t_</sup> exp � ℏ � = _U_<sup>ˆ−1</sup> (ˆ _p_ ) exp � ℏ � _U_ ˆ (ˆ _p_ ) _._ This operator can be implemented in an optical beam by considering the vertical coordinate on the transverse plane as the particle’s position and the horizontal (vertical) polarization as the superior (inferior) component of the spinor. The horizontal spatial degrees of freedom on the transverse plane play no relevant role in the experiment. Although a spinor is a mathematical object which transforms very specifically under a reference frame change, it is not a concern for this simulation since the reference frame is assumed to be fixed. 

The optical transformations required for the simulation are polarization transformations (acting as nondiagonal operators) and phase shifts (used to introduce momentum dependent phases). The former are obtained with the suitable application of wave plates and the last are realized by spatial light modulators (SLMs), which are able to imprint programmable position dependent phases exp[ _i_ f( _x, y_ )] in the horizontal polarization. To transform these position-dependent phases into momentumdependent ones, optical Fourier transforms are used. The action of a quarter wave plate (QWP) set to 45<sup>◦</sup> is given 

3 

Table I: Summary of the optical analogy 

|**Optical System**|**Simulated System**|
|---|---|
|Vertical transverse position|_x_|
|Transverse profile of<br>horizontal polarization|_ψD_1(_x_)|
|Transverse profile of<br>vertical polarization|_ψD_2(_x_)<br>|
|QWP@45<sup>◦</sup>|ˆ_Q_= _e_<sup>_i π_</sup><br>4_/_<br>√<br>2(1−_iσ_1)|
|HWP@45<sup>◦</sup>|ˆ_H_ =_σ_1|
|SLM printing phase _f_(_x, y_)|ˆ_P_[_f_(_x, y_)] =<br>exp[_i_f(_x, y_)]_σ_+_σ_−+_σ_−_σ_+|
|Normalized horizontal<br>polarization intensity at _x_||_ψD_1(_x_)|<sup>2</sup>|



_i_<sup>_π_</sup> by the operator _Q_<sup>ˆ</sup> =<sup>_e_</sup> 4 _/_ √2 (1 − _iσ_ 1), while _H_<sup>ˆ</sup> = _σ_ 1 describes a half wave plate at 45<sup>◦</sup> . The action of a SLM is equivalent to applying _P_<sup>ˆ</sup> [ _f_ ( _x, y_ )] = exp[ _i_ f( _x, y_ )] _σ_ + _σ_ − + _σ_ − _σ_ + over the transverse profile spinor. Using this operator representation for the optical devices, it follows that 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0003-04.png)


<!-- Start of picture text -->
U ˆ ( p ) = Q ˆ P  ˆ [− θ ( p )] H ˆ P ˆ [ θ ( p )] Q, ˆ (4)<br><!-- End of picture text -->

with 2 _θ_ ( _p_ ) = tan<sup>−1</sup> _mcp_<sup>.WeexpresstheinverseFWT</sup> in an analogous fashion. As the Hamiltonian is diagonal in the FWR, the transformed time evolution operator is achieved via the application of the dynamical phase exp [± _itε_ ( _p_ ) _/_ ℏ] in each spinor component using waveplates and the SLM, which concludes the simulation. A summary of the analogy between the optical simulator and the simulated system is given in Table I. 

The experimental scheme is shown in Fig.1. A He-Ne laser with wavelength 632.8 nm and two Holoeye reflective SLMs, each of which divided into halves to operate twice, are used. The Fourier transforms are made by plano-convex cylindrical lenses with 150 mm focal distance such that the position space (mirrors and camera) is in one focal plane and the momentum space is in the opposite focal plane where the SLM is located. The momentum _p_ and the position on the SLM, _X_ , are connected by _X_ = _λfh_<sup>_p_,where</sup><sup>_f_isthefocaldis-</sup> tance and _λ_ is the laser wavelength [22]. In terms of _X_ , the applied phases become 2 _θ_ ( _X_ ) = tan<sup>−1</sup> _mch λfX_ 

2 and _tε_ ( _p_ ) _/_ ℏ = 2 _πt λfX_ + _mch_ 2, so the parameters <(-）(一) 

we need to set are the speed of light _c_ and the Compton wavelength _λC_ = _h/mc_ , which are easily tunable since they enter as programmable parameters in the imprinted phases. Since the time coordinate also comes up as a programmable parameter, we could in principle take measurements for as many time values as we wish inside a time interval. This also implies that the unit of measurement for time is an arbitrary _τ_ . In this realization we chose ∆ _t/τ_ = 1. 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0003-09.png)


<!-- Start of picture text -->
He-Ne Laser<br>Initialstatepreparation FWT<br>Timeevolution<br>inFWR<br>InverseFwT<br>CCD<br>PBSMirorNDFQWPHWPSLMLens<br><!-- End of picture text -->

Figure 1: A He-Ne laser, prepared with an initial gaussian profile and anti-diagonal polarization state, is sent through an optical system designed to implement the Dirac Hamiltionian. The grey shaded regions of the SLMs implement the FWTs, while the striped regions implement the free-evolution. Lenses are used to map the field profile among the different planes of the SLMs, and wave plates to control the polarization state. A CCD camera is used to register the intensity profile of the output field. Additional details are provided in the text. 

The laser produces a Gaussian spatial profile separable in the _x_ and _y_ coordinates, so the initial spinor is 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0003-12.png)


<!-- Start of picture text -->
a<br>ψD ( x, t  = 0) = e − iπx 2 / ( λR ) e − x 2 / (4∆2) , (5)<br>(√2 π 2∆) 1 / 2 b<br><!-- End of picture text -->

where _a_ and _b_ are the proportions of horizontal and vertical polarizations (| _a_ |<sup>2</sup> + | _b_ |<sup>2</sup> = 1), ∆is the beam width in the vertical direction, and _R_ is the vertical radius of curvature of the beam in the initial position plane. The propagation and Gouy terms of the Gaussian beam only introduce global phases which do not affect the dynamical evolution [22]. We start with _a_ = − _b_ = 1, but changing _a_ and _b_ would enable us to prepare different positive and negative energy superpositions. Two cylindrical lenses are placed before the first position space in order to manipulate the initial momentum distribution which depends on _R_ and therefore on ∆. Using a beam profiler, we determined the initial state parameters to be ∆= 48 _,_ 6 _µm_ and _λR/π_ = (2 _._ 2∆)<sup>2</sup> . 

The average position of the simulated particle is calculated as ⟨ _x_ ˆ _D_ ⟩( _t_ ) = _i_ =1 _,_ 2 _dx x_ | _ψDi_ ( _x, t_ )|<sup>2</sup> _,_ where | _ψDi_ ( _x, t_ )|<sup>2</sup> is proportional to the light intensity of polarization component _i_ at position _x_ on the transverse plane measured by a CCD camera placed at the output position space. Each instant of time corresponds to one programmable-phases configuration and one intensityprofile measurement. It is worth noting that the evolved state is accessible for any time value. 

# **IV. RESULTS** 

A summary of our experimental procedure for the particular case _λC_ = 5∆is depicted in Fig.2. In Fig.2-(a) we present the mean position ⟨ _x_ ˆ _D_ ⟩( _t_ ) as a function of _t_ , the ZB being evidenced by the oscillatory behavior. The solid red line is the theoretical prediction, while points 

4 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0004-01.png)


<!-- Start of picture text -->
(a) 0.4<br>0<br>-0.4<br>-0.8<br>-1.2<br>-1.6<br>-2<br>0 10 20 30 40 50 60 70 80 90<br>(b) t (units of τ)<br>60 0 250<br>40 0 125<br>20 0 0<br>(c) 200 400y (px)600 800 200 400y (px)600 800 200 400y (px)600 800 200 400 600 800y (px)<br>250<br>200<br>150<br>100<br>50<br>0<br>-20-10 0 10 20 -20-10 0 10 20 -20-10 0 10 20 -20-10 0 10 20<br>x(units of ∆) x(units of ∆) x(units of ∆) x(units of ∆)<br><x(t)> ∆ (units of)<br>x (px)<br>Intensity<br><!-- End of picture text -->

Figure 2: (a) Mean position ⟨ _x_ ˆ _D_ ( _t_ )⟩ as a function of the time parameter _t_ for Compton length _λC/_ ∆= 5. Points are experimental data, the dashed line is the numerical solution and filled band is the experimental error of one _σ_ . (b) The camera image and (c) the one dimensional state got from marginalizing the intensity measured by the camera over _y_ for four values of the parameter _t_ , namely _t/τ_ = 0 _,_ 30 _,_ 60 and 95, are shown. In (c) red solid lines are experimental data and black dashed curves are numerical solutions. Intensity is in grayscale. 

are experimental results obtained from the images shown in Fig.2-(b). The shaded region represents uncertainty of one _σ_ . Fig.2-(b) shows samples of the data collected by the CCD camera for some instants of time, the _x_ distribution being obtained by considering only a fixed _y_ coordinate at the center of the beam. The _x_ distributions used to calculate ⟨ _x_ ˆ _D_ ⟩( _t_ ) are shown in Fig.2-(c). This procedure assumes that _x_ and _y_ intensity distributions remain separable troughout all the apparatus. This is true in the ideal case, however the cylindrical lenses can introduce some non-separability as one can see in the slightly tilted eliptical intensity pattern shown in Fig. 2-(b). The non-separability causes the initial state to be not entirely pure. Since our experimental results agree well with theory, we conclude that these effects are negligible for the present experiment. 

For a fixed initial state and speed of light _c_ = 0 _._ 1<sup>∆</sup> _/τ_ , we measured the average position in Dirac’s representation for different values of the Compton wavelength, as shown in Fig.3. We fitted the average position with the function _vt_ + _A_ sin( _ωt_ + _δ_ ) for each _λC_ to estimate the mean velocity, amplitude and frequency of the oscillation. These quantities are shown in Fig.4. Our experimental results are in agreement with the expected linear dependence of amplitude and inverse dependence of frequency on _λC_ for small _λC_ [23], as can be seen in Fig.4-(b). This is consistent with the fact that the ZB visibility in Fig.3 increases for smaller values of _λC_ . 

The different inclinations exhibited in Fig.3 are due to the fact that each mass, i.e. Compton wavelength, is as- 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0004-06.png)


<!-- Start of picture text -->
0<br>-1<br>-2<br>-3<br>-4 λC=1∆<br>λC=3∆<br>-5<br>-6 λC=5∆<br>-7 λC=7∆<br>-8 λC=10∆<br>-9 λC=100∆<br>0 10 20 30 40 50 60 70 80 90<br>t (units of τ)<br><x(t)> ∆ (units of)<br><!-- End of picture text -->

Figure 3: Average position ⟨ _x_ ˆ _D_ ( _t_ )⟩ as a function of the time parameter _t_ for Compton lengths _λc/_ ∆= 1 _,_ 3 _,_ 5 _,_ 7 _,_ 10 _,_ 100. Dashed lines are numerical predictions of the theory using Eq. (1), while points are experimental results. The filled bands are experimental errors of one _σ_ . 

sociated to a different velocity distribution, even the momentum distribution being the same for all values of _λC_ . Although the initial state (5) has zero average momentum, this is not true for the mean velocity in Fig.4-(a). As is expected, the mean velocity falls quadratically with _λC_ for large masses (small _λC_ ), while it is close to the speed of light for very small masses ( _λC_ = 100∆). 

The agreement between the experimental ZB data and the theoretical predictions confirm that our optical setup is well suited for the study of 1+1D relativistic dynamical systems, the theoretical extension to larger dimensions being discussed in the Appendix. Beside serving as a proof-of-concept, the proposed setup permits to investigate the system in the FWR, an interesting possibility since it allows to describe the dynamics of the system according to the single-particle perspective, i.e. assigning physical sense only to the projections of single-particle operators over the subspaces of definite sign of energy. 

From the SP perspective, operators that are not blockdiagonal in the FWR, as is the case for _x_ ˆ _D_ , have no physical meaning, since they mix components of positive and negative energy that are associated to two distinct problems. On the other hand, operators that are block-diagonal in the FWR, as ˆ _xF W_ or the Dirac Hamiltonian, may have a physical sense assigned to their positive and negative projections. In this sense, the correct description of the dynamics of a single electron (positron), for example, should be given by _x_ ˆ _F W,_ + = _P_ +<sup>′</sup><sup>_x_ˆ</sup><sup>_F W P_</sup> +<sup>′</sup> (ˆ _xF W,_ − = _P_ −<sup>′</sup><sup>_x_ˆ</sup><sup>_F WP_</sup> −<sup>′).Inoursetup,theaverage⟨</sup><sup>_x_ˆ</sup><sup>_F W_⟩</sup> measured using both positive and negative components of the spinor can be obtained by measuring the transverse profile of the beam before the inverse FWT. However, since the positive and negative components of the spinor are encoded in the horizontal and vertical polarizations of the beam in the FWR, the single-particle position dynamics described by _x_ ˆ _F W,_ + (particle) and _x_ ˆ _F W,_ − (anti-particle) is also accessible by simply selecting one of the polarizations prior to the CCD measurement in the FWR. 

5 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0005-01.png)


<!-- Start of picture text -->
0 1.5<br>-2 (a) 0.4 (b) 1.2<br>0.3<br>-4 0.9<br>-6 0.2 0.6<br>-8 0.1 0.3<br>-10 0 0<br>1 10 100 0 2 4 6 8 10<br>λc(units of ∆) λc(units of ∆)<br>Velocity<br>Amplitude Frequency<br><!-- End of picture text -->

Figure 4: (a) Mean velocity (in units of 10<sup>−2</sup> ∆ _/τ_ ), (b) amplitude (red circles, in units of ∆) and frequency (black squares, in units of _τ_<sup>−1</sup> ) of ZB obtained by fitting a sinusoidal function to the average position ⟨ _x_ ˆ _D_ ( _t_ )⟩ for each Compton wavelength. For small values of Compton wavelength (large masses) the mean velocity falls quadratically with _λC_ (dashed blue line) and for a large value of Compton wavelength (vanishing mass) it appoximates the speed of light set on the experiment. The amplitude dependence with _λC_ is in well agreement with linear behavior (dashed blue line) while frequency is proportional to 1 _/λc_ (solid purple line). 

Experimental results for the mean-position operator are shown in Fig. 5 for _λC_ = 5∆. The experimental data concerning the ZB effect for the _x_ ˆ _D_ operator is also plotted for comparison (blue points). Measurements of ⟨ _x_ ˆ _F W,_ +( _t_ )⟩ and ⟨ _x_ ˆ _F W,_ −( _t_ )⟩ are shown as black dots. As is expected from the independence of the two problems in the SP description, we have two independent mean trajectories corresponding to the free evolution of the particle and the corresponding anti-particle. The ZB is not present for these mean trajectories and a linear behavior in time is observed, as it was expected. As mentioned earlier, we were also able to measure the mean value of the FW mean-position operator _x_ ˆ _F W_ . The results are plotted as the red circles and represent an average of the positive and negative projections cases. The small deviation from a perfect linear behavior can be explained assuming that the SLMs do not modulate all the incident light but a fraction of it, as is shown in the inset picture which shows the same mean values as the experimental plot but obtained from a numerical simulation of the experiment for modulation efficiency of 95% in each SLM. 

# **V. DISCUSSION AND CONCLUSIONS** 

Our experiment demonstrates how relativistic dynamics can be studied using classical optics, and opens the way to more sophisticated investigations. For this purpose it would also be desirable to produce more general initial states. This can be accomplished using intensity and phase masks in the initial state preparation. The state produced in this experiment had zero avarage momentum, but simply shifting the momentum in all SLMs phases by the same ∆ _p_ can be interpreted as if the state has non-vanishing average momentum. 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0005-06.png)


<!-- Start of picture text -->
0.5 0<br>-1<br>0<br>-2<br>-0.5 0 20 40 60 80<br>-1<br>-1.5<br>-2<br>0 10 20 30 40 50 60 70 80 90<br>t (units of τ)<br><x(t)> ∆ (units of)<br><!-- End of picture text -->

Figure 5: Experimental mean positions ⟨ _x_ ˆ _D_ ( _t_ )⟩ (blue dots) and ⟨ _x_ ˆ _F W_ ( _t_ )⟩ (red circles) for _λC/_ ∆= 5. Measurements of _x_ ˆ _F W_ ( _t_ ) projected over positive energy components (horizontal polarization in FWR) as well as negative energy components (vertical polarization in FWR) are shown as black dots. The shaded regions are the mean value uncertainties. The ⟨ _x_ ˆ _F W_ ( _t_ )⟩ data presents no ZB and fits a linear dependence with _R_<sup>2</sup> = 99 _._ 6%. The inset picture shows the result of a numeric simulation of the experimental setup assuming ideal devices except that the SLMs have efficiency of 95%. The inset axes are the same as the main picture. 

In principle the method implemented in this simulation using the FWT could be applied for other simulation schemes of the Dirac equation, however this transformation requires applying a phase shift that is proportional to the inverse tangent of momentum. In our approach the application of this phase is fairly easy, thanks to the spatial light modulator (SLM). However, in other systems, this is quite challenging. Typically in continuous variable quantum simulators one can implement Gaussian Hamiltonians, but non-Gaussian operations (third order and above) are quite difficult [24]. Thus, we believe that our approach is quite interesting in this regard, as it allows one to employ the FWT and investigate relevant aspects of it. 

Albeit here we present the theory and results for the 1+1D case, the extension for 2+1D and for some initial states in 3+1D is straightforward as shown in the Appendix. The first is a direct extension considering the second transverse coordinate of the beam as the second spatial degree of freedom of the simulated particle. A 2+1D simulation also allows for investigation of electronic behavior in bidimensional condensed matter systems such as graphene [10], but still do not present any spin effect. For a general 3+1D simulation it would be necessary a third beam coordinate what is not available in this scheme. In spite of this limitation, in the Appendix we show a class of initial states which dependence on the third coordinate does not alter the time evolution. In this case, the two extra spinor components are provided by the polarization components of a second beam. 

It is well known that there is no exact FWT for the non-free Dirac equation, i.e., if we add a potential to the free Dirac equation (1) the Dirac Hamiltonian becomes 

6 

no longer diagonalizable with one single unitary transformation [20]. This seems to be a very limiting factor of our simulation technique and indeed it is if we try to implement the actual FWT for a potential problem. Instead of doing so, we can try to find other kinds of unitary transformations which reproduce the time evolution and are experimentaly feasible with the available optical elements. Up to now we know that at least for a particular class of potentials it is possible to break the time evolution operator into a position dependent phase which carries all the information about the potential followed by the free evolution presented in this work. This particular case is discussed on Appendix B. 

In conclusion, we have presented an all-optical simulation of the dynamics of a one-dimensional relativistic free point particle, where the beam’s spatial profile plays the role of the particle’s wavefunction, and its orthogonal polarization components are associated to spinor components. Our experiment is based on the diagonalization of the Dirac Hamiltonian using the FWT, which allowed for the decomposition of the unitary evolution into operations that are realizable with off-the-shelf optical components. Adjusting the tunable time parameter we observed the oscillatory ZB phenomenon for Dirac’s position operator. Using our experimental FWT, we were also able to address this phenomenon from a single-particle perspective, where the position description is given by the positive and negative energy projections of the single-particle mean-position operator. This approach allowed us to observe the absence of ZB oscillations for the particle and anti-particle single-particle dynamical evolutions. 

We thank the Brazilian agencies CAPES (PROCAD2013 project), CNPq (#459339/2014-1), FAPEG (PRONEX # 201710267000503) and the Instituto Nacional de Ciência e Tecnologia-Informação Quântica (INCT-IQ) for partial support. 

# **Appendix A: Simulation for more spatial degrees of freedom** 

The goal of this Appendix is to show the simulation protocols for particles in two and three spatial dimensions. 

# **1. Simulation of 2+1 dimensional Dirac Equation** 

Consider the Dirac Hamiltonian for a free particle existing in a 2D space 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0006-08.png)


<!-- Start of picture text -->
H =  c ( σ 1 px  +  σ 2p y ) +  mc 2 σ 3 . (A1)<br><!-- End of picture text -->

_σ_ 1 _px_ − _σ_ 2 _py_ The unitary transformation _e_<sup>_iS_2</sup> = _e_<sup>−</sup><sup>_i_</sup> | **p** | _θ_ ( **p** ) is the FWT which diagonalizes the Hamiltonian in this case, with _θ_ ( **p** ) =<sup>1</sup> 2<sup>tg−1</sup> _mc_<sup>|</sup><sup>**p**|.Forthesamereasonsasinthe</sup> 

1D situation, there is no spin if the space is restricted to two dimensions and the particle state is a spinor with two components. Once we manage to construct FWT from optical device operators, the simulation protocol is made possible identifying again the transverse profile of a laser beam in the two orthogonal polarizations with the spinor components and identifying the two transverse coordinates with particle position. To show that in fact there is such a decomposition let us define a new momentum dependent phase 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0006-11.png)


<!-- Start of picture text -->
tg −1 ( py/px ) , py >  0 or py = 0 , px >  0<br>θ ′ ( p ) =<br>� π  + tg −1 ( py/px ) , py <  0 or py = 0 , px <  0 ,<br>(A2)<br><!-- End of picture text -->

motivated by the polar expression _px_ − _ipy_ = | **p** | _e_<sup>−</sup><sup>_iθ_′</sup> . In terms of the two phase functions the FWT reads 

cos _θ_ ( **p** ) _e_<sup>−</sup><sup>_iθ_′</sup> sin _θ_ ( **p** ) _e_<sup>_iS_2</sup> = _._ (A3) � − _e_<sup>_iθ_′</sup> sin _θ_ ( **p** ) cos _θ_ ( **p** ) � Using the definitions given in the main text it is easy to see that the operator sequence _P_ ˆ �− _θ_ ′( **p** )� _Q_ ˆ _P_ ˆ [− _θ_ ( **p** )] _H_ ˆ _P_ ˆ [ _θ_ ( **p** )] _Q_ ˆ _P_ ˆ � _θ_ ′ ( **p** )� is equal to the FW unitary. The transformed diagonalized time evolution is then given by the product _H_ ˆ _P_ ˆ [ _iε_ ( **p** ) _t/_ ℏ] _H_ ˆ _P_ ˆ [− _iε_ ( **p** ) _t/_ ℏ]. Just to conclude the protocol, the inverse FWT is given analogously by the same set of devices as the FWT with different imprinted phases and different angles for the wave plates. 

# **2. Simulation of 3+1 dimensional Dirac Equation for a particular class of initial states** 

Let us consider the 3+1 Dirac equation 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0006-16.png)


<!-- Start of picture text -->
i ℏ ∂ψ ( x , t ) = � c α  ·  p  +  mc 2 β � ψ ( x , t ) (A4)<br>∂t<br>=<br>with the standard choice of Dirac matrices β<br>0 σk<br>�120×2 −12×2� , αk = � σ 0 k 0 �. The four com-<br>ponents of the spinor  ψ ( x , t ) accounts for the two signs of<br>the energy and for the two spin projections along a fixed<br>direction. The FWT reads  e iS 3 = cos  θ ( p )+ β α | p ·p | sen  θ ( p )<br>with the same definition for θ ( p ) as before.<br><!-- End of picture text -->

A general simulation of the above equation, besides of requiring a four dimensional object to emulate the four spinor components, it would also require three spatial degrees of freedom, while the presented setup allows for just two. Instead of proposing a complete simulation, let us consider only the particular family of initial states given by 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0006-18.png)


<!-- Start of picture text -->
ψ ( x , t  = 0) =  √1 L  φ ˜1( x, y ... )  − L 2 < z < L 2 . (A5)<br>0  φ ˜4( x, y )  elsewhere<br><!-- End of picture text -->

7 

which depedence on _pz_ behaves like a _δ_ ( _pz_ ) for large values of _L_ . 

In momentum space this state becomes 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0007-03.png)


<!-- Start of picture text -->
 φ ˜1( px, py )  L sin p 2 z ℏ L Thus we can approximate the FW transformed state<br>ψ ˜( t  = 0 ,  p ) =  ...  � 2 π ℏ pz L , (A6) by<br>� 2ℏ �<br> φ ˜4( px, py ) <br><!-- End of picture text -->


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0007-04.png)


<!-- Start of picture text -->
ψ ˜ ′ ( p , t  = 0) ≈ �cos ( θ ( px, py,  0)) +  β  α | x ( p p x x , p  + y  α ,  0) yp | y sin  θ ( px, py,  0) � ψ ˜( p , t  = 0) , (A7)<br><!-- End of picture text -->

and all the momentum dependent phases only depend on two coordinates and can be aplied with SLMs. 

The transformed state is explicitly written as 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0007-07.png)


<!-- Start of picture text -->
cos  θ 0 0 px − ipy sin  θ<br> | p |  φ 1<br>ψ ′ ( p , t  = 0) =  00 − px | p +cos| ipy θ sin  θ px |+ p cos ip | y  θ sin  θ 00   φφ 23  � 2 Lπ ℏ � sin p 2 z ℏ p L 2 z ℏ L � (A8)<br>− px − ipy sin  θ 0 0 cos  θ  φ 4 <br> | p | <br><!-- End of picture text -->

we notice that the FWR only mixes the components two by two what makes possible to simulate it using two beams without any joint transformation between them. Then we can address the transverse profiles of horizontal and vertical polarizations of the first beam to _φ_ 1 and _φ_ 4 and the FWR as well as the subsequent diagonal time evolution do not mix this components with the two remaining. Moreover, each pair of mixed components transforms like the two spatial dimensions case (Eq. (A3)) with the suitable phase signs. 

The interesting thing about three spatial dimensions simulation is that it would enable us to investigate also spin effects like the spin analogous to _Zitterbewegung_ . 

For the above particular case, we define _φD_ such that 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0007-11.png)


<!-- Start of picture text -->
ψD =  e − i ℏ 1 c � V 1( x ′ )1 dx ′ φD. (B3)<br><!-- End of picture text -->

The substitution of this state on Eq.(B1) shows that the spinor _φD_ evolves according to the free Dirac equation (Eq.(1)). Thus, if we want to simulate the time evolution of the initial state _ψD_ ( _x, t_ = 0), we need to prepare the state _φD_ ( _x, t_ = 0) = exp � _i_ ℏ<sup>1</sup> _c_ � _V_ 1( _x_<sup>′</sup> )1 _dx_<sup>′�</sup> _ψD_ ( _x, t_ = 0) and the dynamics of the free evolution. From the experimental point of view, this corresponds to applying a local phase in position space to all the components of the spinor before performing the free evolution in the way as it is shown in the main text. 

# **Appendix B: Simulation of 1+1 dimensional Dirac Equation for a particular class of potentials** 

Employing the strategy of [25], we show in this Appendix that, if the initial state is conveniently prepared, our approach is able to simulate the Dirac equation for a particular class of potentials. To this end, consider the 1D Dirac equation 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0007-15.png)


<!-- Start of picture text -->
i ℏ ∂t ∂ ψD = ( cpσ ˆ 1 +  mc 2 σ 3 +  V  ( x )) ψD, (B1)<br><!-- End of picture text -->

where _V_ ( _x_ ) is a spinorial potential of the form 


![](images/Zheng_2021_Wuji_Automatic_Online_Combat_Game_Testing.pdf-0007-17.png)


<!-- Start of picture text -->
V  ( x ) =  V 1( x ) σ 1 . (B2)<br><!-- End of picture text -->

- ∗ Electronic address: thaisdelimasilva@gmail.com 

- [1] P.A.M. Dirac, Proc. Royal Soc. Lond. 117, 610 (1928). 

- [2] C.D. Anderson, Phys. Rev. 43, 491 (1933). 

- [3] E. Schrödinger, Sitzungsber. Preuss. Akad. Wiss. Phys.Math. Kl. 24, 418 (1930). 

- [4] Klein, O. Die Reflexion von Elektronen an einem Potentialsprung nach der relativistischen Dynamik von Dirac. Z. Phys. 53, 157 (1929). 

- [5] P. Krekora, Q. Su, and R. Grobe, Phys. Rev. Lett. 93, 043004 (2004) 

- [6] R. Gerritsma, G. Kirchmair, F. Zähringer, E. Solano, R. Blatt, and C. F. Roos, Nature 463, 68 (2010). 

- [7] R. Gerritsma, B. P. Lanyon, G. Kirchmair, F. Zähringer, C. Hempel, J. Casanova, J. J. García-Ripoll, E. Solano, 

8 

R. Blatt, and C. F. Roos, Phys. Rev. Lett. 106, 060503 (2011). 

- [8] X. Zhang, Phys. Rev. Lett. 100, 113903 (2008). 

- [9] J. Otterbach, R. G. Unanyan, and M. Fleischhauer, Phys. Rev. Lett. 102, 063602 (2009). 

- [10] M. I. Katsnelson, K. S. Novoselov, and A. K. Geim, Nature Physics 2, 620 (2006). 

- [11] F. Dreisow, M. Heinrich, R. Keil, A. Tünnermann, S. Nolte, S. Longhi, and A. Szameit, Phys. Rev. Lett. 105, 143902 (2010). 

- [12] L. J. LeBlanc et al, New J. Phys. 15, 073011 (2013). 

- [13] T. Salger, C. Grossert, S. Kling, and M. Weitz, Phys. Rev. Lett. 107, 240401 (2011). 

- [14] J. Y. Vaishnav, C. W. Clark, Phys. Rev. Lett. 100, 153002 (2008). 

- [15] P. Caban, J. Rembieliński e M. Wlodarczyk, Ann. Phys. 330, 263 (2013). 

- [16] L. L. Foldy, S. A. Wouthuysen, Phys. Rev. 78(1), 29 (1950). 

- [17] Y. N. Obukhov, Phys. Rev. Lett. 86, 192 (2001). 

- [18] J. Q. Quach, Phys. Rev. D 92, 084047 (2015). 

- [19] G. B. Lemos, R. M. Gomes, S. P. Walborn, P. H. Souto Ribeiro, and F. Toscano, Nat. Commun. 3, 1211 (2012). 

- [20] F. Schwabl, _Advanced Quantum Mechanics_ , SpringerVerlag (2008). 

- [21] B. Thaller, _The Dirac Equation_ , Springer-Verlag (1992). 

- [22] B.E.A. Saleh, and M.C. Teich, _Fundamentals of Photonics_ , Wiley (2007). 

- [23] From Eq.(2) we have that the amplitude of ocillations for a given momentum eigenstate is proportional to _ch/ǫ_ ( _p_ ), which for small _λC_ , i.e., large mass, can be approximated by _λC_ . On the other hand, the frequency is proportional to _ǫ_ ( _p_ ) _/h_ , that approaches _c/λC_ for large masses. 

- [24] D.S. Tasca, R.M. Gomes, F. Toscano, P.H. Souto Ribeiro, and S.P. Walborn, Phys. Rev. A 83, 052325 (2011). 

- [25] C. Sabín, J. Casanova, J. J. García-Ripoll, L. Lamata, E. Solano, and J. León Phys. Rev. A 85, 052301 (2012). 

