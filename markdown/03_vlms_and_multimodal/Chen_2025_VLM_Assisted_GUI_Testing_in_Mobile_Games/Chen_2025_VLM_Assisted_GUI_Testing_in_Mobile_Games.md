# **Modified Coherence and the Transverse Extent of Jets** 

Amit Kumar,<sup>1, 2</sup> Abhijit Majumder,<sup>2</sup> Chathuranga Sirimanna,<sup>3, 2</sup> and Yasuki Tachibana<sup>4</sup> 

> 1 _Department of Physics, University of Regina, Regina, SK S4S 0A2, Canada_ 

> 2 _Department of Physics and Astronomy, Wayne State University, Detroit, MI 48201._ 

> 3 _Department of Physics, Duke University, Durham, NC 27708._ 

> 4 _Akita International University, Yuwa, Akita-city 010-1292, Japan._ 

(Dated: January 15, 2025) 

We present a study of the transverse size of parton showers and their diminishing interaction with the medium in the high virtuality stage of jet evolution. We consider the process of a hard quark produced in deep inelastic scattering off a large nucleus. Single gluon radiation from this quark, in the absence of scattering, is re-derived using wave-packets. This allows for a derivation of the quantum uncertainty size of the hard quark, at the point of splitting. This uncertainty size is then incorporated within a Monte-Carlo shower routine yielding transverse shower sizes noticeably larger than the classical antenna size of the shower. No clear relation is found between the full uncertainty size of the shower and the virtuality of the originating parton. The single gluon emission from the hard quark is then re-analysed for the case of single rescattering off the remainder of the nucleus. A relation is derived between the jet transport coefficient _q_ ˆ and the gluon Transverse Momentum Dependent Parton Distribution Function (gTMDPDF). Solving this relation, for a simple case, clearly demonstrates the weakening of _q_ ˆ with the virtuality of the hard splitting parton. 

## **I. INTRODUCTION** 

The modification of high transverse momentum (high _pT_ ) jets [1–3] and hadrons [4–8] produced in a heavy-ion collision has become a central observable in the study of the quark-gluon-plasma (QGP) created in these collisions [9, 10]. What started as the study of stimulated gluon radiation off hard partons [11–13] has now turned into a study of the modification of jets of arbitrary number of partons, using sophisticated event generators [14– 20]. The plurality of these generators has necessitated the use of event generator frameworks [21], aggregating multiple generators in modular fashion within an end-toend simulation [22]. 

Each of these event generators are based on different formalisms of energy loss [23–28], each of which apply at a specific epoch of the evolution of the jet in the medium [9, 22]. Jets start as single partons emanating from a hard collision. These partons are highly virtual, i.e., far off their mass shell. They undergo sequential decay into less virtual partons, each with opposing transverse momentum relative to the direction of the parent parton, producing a spray of partons very close to their mass shell. Throughout this process, the strong coupling grows with every split as the momentum scale depreciates. Portions of the jet, where the momentum scale begins to approach ΛQCD, will begin to interact strongly with the medium, if within it, or hadronize, eventually turning the entire partonic system into a jet of hadrons. 

Even within the purely perturbative sector of the jet, where the momentum scale is still considerably larger than ΛQCD, there are at least two different stages of jet modification [29], one where the effect of the medium is a perturbative correction to the vacuum shower [23, 24, 30], and one where the medium induced radiation rate far exceeds the rate for a vacuum like split with the same kinematics [26, 31–33]. In the first stage, the virtuality 

of the parent parton _µ_<sup>2</sup> , or the transverse momentum of the radiated parton _ℓ_<sup>2</sup> _⊥_<sup>=</sup><sup>_µ_2</sup><sup>_y_(1</sup><sup>_−y_)</sup><sup>_∼µ_2(where</sup><sup>_y_is</sup> the forward momentum fraction of one of the offspring), is much larger than the transverse momentum acquired by multiple scattering of the parent parton _µ_<sup>2</sup> med<sup>=</sup><sup>_qτ_ˆ,</sup> namely _µ_<sup>2</sup> _≫ µ_<sup>2</sup> med<sup>[34].Thetransportcoefficient</sup><sup>_q_ˆ[35–</sup> 37] is the mean squared transverse momentum acquired by the parton per unit length and _τ_ is the formation time (equal to the formation length for light-like particles) given by 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0001-14.png)


<!-- Start of picture text -->
τ = 2 Ey (1  − y ) = 2 E (1)<br>ℓ 2 ⊥ µ 2 .<br><!-- End of picture text -->

In the second stage, the multiple scattering and rare emissions on average maintain the virtuality at the medium scale, namely the acquired transverse momentum: _µ_<sup>2</sup> _≈ µ_<sup>2</sup> med<sup>=</sup><sup>_qτ_ˆ.(Inthispaper,wewillconsider</sup> _y_ values to be in the range from 0 _._ 1 ≲ _y_ ≲ 0 _._ 9, and thus transverse momenta are of the order of virtuality _µ ∼ ℓ⊥_ .) 

Using the equation above, and setting _µ_<sup>2</sup> = _µ_<sup>2</sup> med<sup>we</sup> obtain an expression for the medium generated scale, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0001-17.png)


<!-- Start of picture text -->
µ 2 med = � 2ˆ qE. (2)<br><!-- End of picture text -->

This is often referred to as the saturation scale of the medium. Recent simulations using such a two-stage framework have demonstrated the need for separate formalism for parton virtualities above and at this scale [38– 41] (or the need for new formalism that can appropriately address both regimes), with a gradual _weakening_ of the effective transport coefficient _q_ ˆ above this saturation scale. In Refs. [38–41] the _weakening_ factor was virtuality dependent, i.e., 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0001-19.png)


<!-- Start of picture text -->
q ˆ( T, E, µ 2 ) =  f ( µ 2 )ˆ q ( T, E ) . (3)<br><!-- End of picture text -->

2 

where _q_ ˆ( _T, E_ ) is the Hard-Thermal-Loop (HTL) effective theory expression from Ref. [42]. The factor _f_ ( _µ_<sup>2</sup> ) was approximated from an effective description of the medium using a QGP parton distribution function (QGP-PDF) in Ref. [43]. In a wide ranging Bayesian analysis carried out in Ref. [44], which compared a multistage simulation with all leading hadron and jet data, the _f_ ( _µ_<sup>2</sup> ) was parametrized. The Bayesian analysis determined _f_ ( _µ_<sup>2</sup> ) to be a factor that drops swifty with _µ_<sup>2</sup> . 

Complementary to these phenomenological observations of a gradual weakening of the transport coefficient, with the virtuality of a given parton, are the “coherence” based arguments of Refs. [45–48]. These argue that splits, before or even after formation, cannot be resolved until the distance between the daughters becomes larger than the “typical” resolution scale of medium gluons 1 _/µ_ med _≃_ (2ˆ _qE_ )<sup>_−_1</sup><sup>_/_4</sup> . Thus, the effective transport coefficient should be reduced, as the gluons from the medium can only perceive the overall color charge of the produced antenna. In other words, parton showers with transverse size below the inverse saturation scale are almost unaffected by the medium, and are, thus, vacuum-like. 

The description above, while simple to state, is difficult to visualize or understand. Let us assume that the medium is large and static [49] and has a resolution scale of 1 _/µ_ med = (2ˆ _qE_ )<sup>_−_1</sup><sup>_/_4</sup> . Let us further imagine that a jet with a virtuality _µ ≫ µ_ med starts to propagate and shower in this medium. By the time that two partons (or parton clusters) are separated to the scale 1 _/µ_ med, there may have been many emissions, and the color charges of the two partons may not be easily related. Even if the two partons (or parton clusters) can be resolved by the medium at a later time, the medium can no longer affect the original process of emission as that has happened in the past. Thus, in the coherence picture, the only emissions that can be affected by the medium are those where the partons are separated by 1 _/µ_ med within their formation time. 

The calculations of coherence typically involve, a quark-anti-quark antenna formed from a virtual photon. The calculation of stimulated emission is carried out using the BDMPS-Z formalism, which is typically only applicable for virtualities at or below _µ_ med. Also, the formation of the quark-anti-quark antenna, and subsequent gluon radiation, at scales above _µ_ med, is considered to be unaffected by scattering in the medium. The entire antenna structure is formed by successive angle ordered vacuum like emission, where successive spilts happen at monotonically smaller angles. Based on these antenna arguments, it has been stated that jets with larger virtuality, which lead to antenna with larger transverse momentum, will tend to be resolved more (or earlier) by the medium, because of the larger size that these will grow to; and as a result, will experience greater quenching [45, 46]. 

In this paper, we will demonstrate that the picture of jet modification as outlined by the antenna approach may not be entirely accurate. Partons are quantum mechanical objects and thus possess an uncertainty in their 

momentum, and a corresponding uncertainty in their location. In the two dimensions transverse to the direction of propagation of a parton, one may na¨ıvely estimate the uncertainty of the transverse location of the off-spring as (in natural units with ℏ = 1), 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0002-07.png)


<!-- Start of picture text -->
δz⊥ ∼ 1 , (4)<br>ℓ⊥<br><!-- End of picture text -->

where, _ℓ⊥_ is the transverse momentum of either offspring, with respect to the parent. Treating their location uncertainty as a size, we can ascribe a transverse size to a developing shower beyond the classical antenna size of the shower. Quantum uncertainty will make the overall transverse size of the shower larger than the case of the classical antenna. 

Partons with lower virtualities may, due to their quantum uncertainty size, compensate for the smaller antenna size of the ensuing shower. We demonstrate how one can extract the quantum uncertainty size in the case of a final state shower in deep-inelastic scattering (DIS). Due to these compensatory effects, the transverse size of the shower is not directly related to the virtuality of the originating parton. This will be demonstrated using a vacuum simulation, which, for the first time, will include the quantum uncertainty size. 

To study the interaction of these jets with an extended medium, we will consider the process of deep-inelastic scattering on a large nucleus (A-DIS), where the outgoing radiating quark will interact with the glue field of the remaining nucleons along its path. While the transverse size of jets will be found to have a weak dependence on the off-shellness of the originating partons, we will demonstrate that the coupling between the medium and a radiating parton does indeed weaken at larger parton virtualities, leading to a reduction in the rate of stimulated emission. The cause for this will be found to depend on several factors, one of which is the transverse size of the radiating parton. Other factors include the scale and momentum fraction dependence of the Transverse Momentum Dependent Parton distribution Function (TMDPDF) which controls the momentum of the gluon exchanged between the jet and the medium. Both the scale and momentum fraction of the exchanged gluon will be found to depend on the scale of the hard parton. 

Our calculations will be carried out for a hard quark radiating a hard gluon in the higher twist formalism [23, 24, 30, 31], which is applicable to partons with a virtuality much larger than the medium scale _µ_<sup>2</sup> med<sup>=</sup><sup>_qτ_ˆ.</sup> To be clear, the current paper is _not_ a re-derivation of coherence effects in the higher-twist formalism. It is a revaluation of the gradient expansion carried out in all higher-twist calculations. Unlike prior efforts, the momentum fraction and scale dependence of the soft matrix elements will be retained and evaluated in the final expressions, where the differing dependencies of the hard part and soft matrix elements on the separation scale _µ_<sup>2</sup> _∼ ℓ_<sup>2</sup> _⊥_<sup>,willleadtotheweakeningoftheinteractionof</sup> the jet with the medium. 

3 

The remainder of the paper is organized as follows: In Sec. II, we re-introduce the reader to the formalism of DIS on a large nucleus using wave-packets, and consider the case of a single gluon emission from the struck quark, in vacuum. Here we re-organize the derivation to extract the transverse size from quantum uncertainty arguments. In Sec. III, we modify the MATTER generator in vacuum to include transverse uncertainty size of partons, and use this to estimate the transverse size of entire jets. This section will demonstrate that the transverse size of jets is wider than the antenna size, and does not have a strong dependence on the originating parton’s virtuality. In Sec. IV, we re-analyze the single gluon emission kernel at next-to-leading twist and derive a new relation between _q_ ˆ and the gluon TMDPDF within a nucleon beyond the struck quark. In Sec. V, we use this new relation to derive the scale dependence of _q_ ˆ, and its weakening with the off-shellness of the radiating quark. In Sec. VI, we summarize and provide an outlook on extensions and some consequences of this effort. 

## **II. THE SIZE OF VACUUM LIKE EMISSIONS** 

Hard jets (with energies ≳ 100 GeV) start with an off-shellness that is orders of magnitude higher than typical scales in the medium and thus produce multiple vacuum like emissions prior to interacting strongly with the medium. To study this vacuum stage and the start of interactions with the medium, we consider the higher-twist approach which focuses on emissions that are vacuum like, and, in addition, includes the interference terms between vacuum and medium induced emissions [23, 24, 30, 31]. 

As is typically the case in higher twist calculations, we consider the process of a hard quark produced in the deep-inelastic scattering (DIS) off a large nucleus (ADIS). For cases which ignore the correlation between initial state and final state interaction, as we are about to do in this paper, A-DIS provides a well controlled environment to study the produced jet. For the case of the first vacuum like emissions, we will not consider interactions in this section and will focus on hard gluon emissions from the produced quark (see Fig. 1). 

Following Ref. [15], the differential cross section to produce a quark and gluon in the final state from the hard scattering of a lepton on a proton (or a nucleus), via one photon exchange, is written as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0003-06.png)


<!-- Start of picture text -->
l<br>q q<br>z’ lq z<br>p’ p<br>0 0<br>P P<br><!-- End of picture text -->

FIG. 1. Single gluon emission from the outgoing struck quark produced in the deep-inelastic scattering off a large nucleus. The diagram above ignores final state interaction of the developing radiation. 

In Eq. (5), the leptonic tensor L<sup>_µν_</sup> contains all portions of the Dirac trace of leptonic variables. This is connected by a single exchanged photon with the hadronic tensor W _µν_ , which contains all hadronic fields: 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0003-09.png)


<!-- Start of picture text -->
W µν = Disc. d 4 yd 4 y ′ e iq· ( y−y′ ) ⟨P |J µ ( y ) J ν ( y ′ ) |P ⟩ . (7)<br>2 πi Ω �� �<br><!-- End of picture text -->

In the equation above, _|P ⟩_ is the incoming hadronic state. Unlike typical expressions for W<sup>_µν_</sup> , we include space-time integrations over the locations of both currents _y_ , _y_<sup>_′_</sup> . The extra space-time integration necessitates division by the four volume Ω. Using the collinear approximation _q_<sup>_−_</sup> _, q_<sup>+</sup> _≫ k⊥_ , where _k⊥_ represents a typical transverse momentum in the problem, we can factorize the hard part from the initial and final state of the process. 

To understand the transverse size of the radiating antenna, we consider the process of a single emitted gluon in the final state. For this case, we obtain the hadronic tensor as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0003-12.png)


<!-- Start of picture text -->
W µν = 1 d 4 yd 4 y ′ Tr F ( y, y ′ )O( y, y ′ ) , (8)<br>Ω� � γ 2 − γµ γ 2 + γν �<br>where,<br>F ( y, y ′ ) =  ⟨P |ψ ¯ ( y ) γ 2 + ψ ( y′ ) |P ⟩ , (9)<br><!-- End of picture text -->

where, 

and, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0003-15.png)


<!-- Start of picture text -->
dσ = α EM 2 L µν d W µν , (5)<br>d 3 Ld 3 ld 3 lq 2 πsELQ 4 d 3 ld 3 lq<br><!-- End of picture text -->

where, _L_ , _l_ and _lq_ are the momenta of the recoiling lepton (with energy _EL_ ), radiated gluon and out-going quark. The incoming proton (or nucleon in a nucleus) has a momentum of _P_ , while the momentum of the photon is 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0003-17.png)


<!-- Start of picture text -->
q = � − 2 qQ − 2 , q−,  0 ,  0 � . (6)<br><!-- End of picture text -->


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0003-18.png)


<!-- Start of picture text -->
d 4 l d 4 p d 4 p ′<br>O( y, y ′ ) = (10)<br>� (2 π ) 4 d 4 zd 4 z′ (2 d 4 π l ) q 4 (2 π ) 4 (2 π ) 4<br>( /p  + /q )<br>× g 2 Tr q ) γβ<br>� γ 2 − ( p  +  q ) 2 − iϵ γα/lq 2 πδ ( l 2<br>( /p ′ + /q )<br>× e iq· ( y−y′ ) e −i ( p + q ) · ( y−z )<br>( p ′ +  q ) 2 +  iϵ �<br>× e −i ( l + lq ) · ( z−z′ ) e i ( p′ + q ) · ( y′−z′ ) Gαβ ( l )2 πδ ( l 2 ) .<br><!-- End of picture text -->

4 

## **A. Incoming wave-packets** 

We can now introduce uncertainty in the incoming momentum states, by replacing the proton states _|P ⟩_ with single quark states, with transverse momentum distributed according to a Gaussian distribution: 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0004-03.png)


<!-- Start of picture text -->
− p ′ ⊥ 2 P + )2<br>d 3 p ′ exp� 2∆ 2 ⊥ − (p ′ + 2∆ − 2 + �<br>|P ⟩−→ | p ′ ⟩. (11)<br>� (2 π ) 3 � 2p ′ +<br><!-- End of picture text -->

In the above equation, P<sup><u>+</u></sup> is the large mean forward momentum of the incoming state. We assume that P<sup><u>+</u></sup> is larger than all other scales in the problem. As a result, p<sup>_′−_</sup> _≃_ p<sup>_′_2</sup> _⊥_<sup>_/_(2 ¯p</sup><sup>_′_+),and∆2</sup> _⊥_<sup>,∆2</sup> +<sup>arewidthsthat,we</sup> assume, can be controlled by the experiment. 

The incoming function _F_ ( _y, y_<sup>_′_</sup> ) can be re-expressed in terms of mean and uncertainty in p _, y_ as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0004-06.png)


<!-- Start of picture text -->
d 3 p d 3 p ′<br>F ( y, y ′ ) = (12)<br>� (2 π ) 3 � 2p + (2 π ) 3 � 2p ′ +<br>− p ⊥ 2 − p ′ ⊥ 2<br>2∆ 2 ⊥<br>× u ¯(p) γ +<br>2 u (p ′ ) ei p ·ye−i p ′·y′e<br>− (p+ − P + ) 2 − (p ′ + − P + ) 2<br>2∆ 2 2∆ 2<br>× e + e +<br>= u ¯(p ¯ + δ 2 p ) γ 2 + u (p ¯  − δ 2 p )<br>� d 3(2p¯ πd 3) 6 δ p 2 � ( ¯p + ) 2 − ( δ p + ) 2 / 4<br>− p¯ ⊥ 2 − δ p ⊥ 2 − (p ¯+  − P + ) 2<br>× exp exp<br>� ∆ 2 ⊥ 4∆ 2 ⊥ � � ∆ 2 + �<br>−δ p +2<br>× exp e i  ¯ p ·δye−iδ p ·y ¯ .<br>4∆ 2<br>� + �<br><!-- End of picture text -->

We have decomposed p = p¯ + _δ_ p _/_ 2, p<sup>_′_</sup> = p¯ _− δ_ p _/_ 2, _y_ = _y_ ¯ + _δy/_ 2 and _y_<sup>_′_</sup> = _y_ ¯ _− δy/_ 2. The Gaussian widths applied on the transverse momenta are assumed different from those applied on the longitudinal momenta. See Ref. [15], where widths on the transverse momenta were ignored. In the limit of large P<sup><u>+</u></sup> _≫_ ∆+ _,_ ∆ _⊥_ , we obtain, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0004-08.png)


<!-- Start of picture text -->
u ¯ p¯ + δ p p¯  − δ p ≃ 2P + . (13)<br>� 2 � γ 2+ u � 2 �<br><!-- End of picture text -->

Shifting p¯<sup>+</sup> = p¯<sup>+</sup> + P<sup><u>+</u></sup> , and approximating that P<sup><u>+</u></sup> is larger than all other momenta in the problem, we obtain, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0004-10.png)


<!-- Start of picture text -->
⊥<br>⊥ + δ p 4 2<br>p − = (p ¯ ⊥ +  δ p ⊥/ 2)2 + p¯ ⊥ · δ p ⊥ ,<br>2( ¯p + +  δ p + / 2) ≃ p¯2 2P + 2P +<br>⊥<br>p ′− = (p ¯ ⊥ − δ p ⊥/ 2)2 ⊥ + δ p 4 2 − p¯ ⊥ · δ p ⊥ . (14)<br>2( ¯p + − δ p + / 2) ≃ p¯2 2P + 2P +<br><!-- End of picture text -->

As a result, we obtain the mean and difference in the small ( _−_ )-component as: 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0004-12.png)


<!-- Start of picture text -->
⊥ + δ p ⊥ 2 / 4 )<br>p¯ − = (p ¯2 and  δ p − = p¯ ⊥ · δ p ⊥ . (15)<br>2P + P +<br><!-- End of picture text -->

Both of these terms are suppressed by the hard scale P<sup><u>+</u></sup> . In the high energy limit, we would obtain exponentials of the form exp[ _i_ p ¯<sup>_−_</sup> _δy_<sup>+</sup> ] and exp[ _iδ_ p<sup>_−_</sup> _y_ ¯<sup>+</sup> ]. Thus, when completely included in the p¯ _⊥_ and _δ_ p _⊥_ integrations, these terms will restrict _y_ ¯<sup>+</sup> and _δy_<sup>+</sup> to values smaller than _∼_<sup>2</sup> P<sup><u>+</u></sup> _/_ p¯ _⊥_<sup>2.Wewillignoretheseterms,in</sup> this first attempt to determine the uncertainty size of the incoming hard parton. Thus, we will only have distributions in the _−_ and _⊥_ components. 

If we were to integrate out p¯ _, δ_ p, the incoming state factor [ _F_ (¯ _y, δy_ )] reduces to, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0004-15.png)


<!-- Start of picture text -->
F (¯ y, δy ) =  e i P + δy − Ne− [2(¯ y − )∆+] 2 e− [( δy − )∆+] 2<br>× e −δy ⊥ 2 ∆2 ⊥ e −y ¯ ⊥ 2 4∆2 ⊥ . (16)<br><!-- End of picture text -->

The factor of _N_ includes all normalizations. Thus, the incoming state is centered at _y_ ¯ = 0 with an uncertainty of 1 _/_ [4∆<sup>2</sup> _p_<sup>] (where</sup><sup>_p ∈_+</sup><sup>_, ⊥_).By setting ∆</sup><sup>_p≃λQ_(where</sup> _λ ≪_ 1, however _λQ ≫_ ΛQCD), we localize the ( _y_<sup>_−_</sup> _, y⊥_ ) extent of the incoming and outgoing hard quark to a size of ( _y_<sup>_−_</sup> )<sup>2</sup> _, y⊥_<sup>2</sup><sup>_≃_1</sup><sup>_/_(</sup><sup>_λQ_)2.</sup> 

## **B. Wave-packets at split** 

In this paper, we are not interested in the distribution at _y_ but rather the distribution at _z_ , the location of the split of the hard quark into a quark and a gluon. This part can be calculated under the constraint that _y_<sup>_′_</sup> = 0, i.e., the calculation of the transverse size of the radiating parton, at the location of the split, does not require the mean and uncertainty of the initial hard scattering location to be specified. However, in the interest of continuity with the preceding sub-section, we will retain these locations in what follows. Substituting Eqs. (10,12) in Eq. (8), and carrying out the _y, y_<sup>_′_</sup> integration sets _p_ = p and _p_<sup>_′_</sup> = p<sup>_′_</sup> . The remaining expression for the hadronic tensor reads, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0004-19.png)


<!-- Start of picture text -->
Tr γ −<br>� 2 γµ γ 2 + γν �<br>W µν = (17)<br>Ω<br>d 4 l d 3 p¯ d 3 δ p<br>×<br>� (2 π ) 4 d 4 zd 4 z′ (2 d 4 π l ) q 4 (2 π ) 6<br>( / p + /q )<br>× g 2 Tr q ) γβ<br>� γ 2 − (p +  q ) 2 − iϵ γα/lq 2 πδ ( l 2<br>× ( / p ′ + /q ) e i (p+ q ) ·z exp − p¯ ⊥ 2 − δ p ⊥ 2<br>(p ′ +  q ) 2 +  iϵ � � ∆ 2 ⊥ 4∆ 2 ⊥ �<br>− (p ¯+  − P + ) 2 −δ p +2<br>× exp exp<br>� ∆ 2 + � � 4∆ 2 + �<br>× e −i ( l + lq ) · ( z−z′ ) e −i (p ′ + q ) ·z′ Gαβ ( l )2 πδ ( l 2 ) .<br><!-- End of picture text -->

Invoking the two on-shell delta functions, we get, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0004-21.png)


<!-- Start of picture text -->
2<br>⊥ ⊥<br>l + = l 2 q = lq . (18)<br>2 l − , and l + 2 lq −<br><!-- End of picture text -->

5 

Once again, we invoke the shift to remove the large component of p¯<sup>+</sup> as p¯<sup>+</sup> _→_ p¯<sup>+</sup> + P<sup><u>+</u></sup> , and separate out each of the phase factors for sequential integration, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0005-02.png)


<!-- Start of picture text -->
Tr γ −<br>� 2 γµ γ 2 + γν �<br>W µν = (19)<br>Ω<br>dl − d 2 l⊥ q d 2 lq ⊥ d 3 p¯ d 3 δ p<br>× g 2<br>� (2 π ) 3 2 l − d 4 zd ¯ 4 δz dl (2 − π ) 3 2 lq − (2 π ) 6<br>γ − γ +<br>× Tr γ α /lqγ β<br>� 2 2( ¯p + + δ p 2 + + P + +  q + − iϵ )<br>γ +<br>× Gαβ ( l )<br>2( ¯p + − δ p 2 + + P + +  q + +  iϵ ) �<br>− p¯ ⊥ 2 − δ p ⊥ 2<br>× exp<br>� ∆ 2 ⊥ 4∆ 2 ⊥ �<br>− (p ¯+)2 − δ p+2<br>× exp<br>∆ 2 4∆ 2<br>� + + �<br>× e −i ( l + lq ) ·δz e i ( ¯ p ·δz + δ p ·z ¯) ei (P+ q ) ·δz.<br><!-- End of picture text -->

In the equation above, P<sup>_<u>−</u>_</sup> = P _⊥_ = 0. 

We can carry out the integration of _z_ ¯, as we are only interested in the size given by _δz_ . One should note that there are 4 _z_ ¯ integrations but only 3 independent components of _δ_ p. As a result, the � _dz_ ¯<sup>+</sup> will produce a factor or length _L_<sup>+</sup> . In Ref. [15], the focus was on the longitudinal location of the split. Hence, in that effort, all positions other than _z_ ¯<sup>_−_</sup> were integrated over. In this effort, we are focused on the transverse size at the formation time. As such, we will integrate over all components of _z_ ¯. The naive integrations over _δz_ would typically yield the energy momentum conservation conditions: 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0005-05.png)


<!-- Start of picture text -->
(2 π ) 4 δ 4 ( ¯p + P +  q − l − lq ) . (20)<br><!-- End of picture text -->

However, at this point, we will not integrate over the offset in transverse positions, as that will yield the transverse size. We can integrate over _δz_<sup>+</sup> and _δz_<sup>_−_</sup> , yielding, 

In the equation above, the factor exp� _−i⃗_ p¯ _⊥ · δ⃗z⊥_ � is ignored in comparison to exp _i_ ( _⃗l⊥_ + _⃗lq ⊥_ ) _· δ⃗z⊥_ . This is � � based on a choice that p¯ _⊥_ has a narrower distribution compared to _l⊥_ and _lq ⊥_ [controlled by our choice of ∆ _⊥_ in the incoming wave-function in Eq. (11)]. In the absence of this assumption, completing the _δ⃗z⊥_ integration will set _⃗_ p _⊥_ = _⃗l⊥_ + _⃗lq⊥_ . This will yield a Gaussian factor of exp _{−_ ( _⃗l⊥_ + _⃗lq ⊥_ )<sup>2</sup> _/_ ∆<sup>2</sup> _⊥_<sup>_}_.Thisimpliesthatthatingen-</sup> eral _⃗l⊥̸_ = _−⃗lq ⊥_ . Assuming that _l⊥, lq ⊥ ≫_ ∆ _⊥_ , we would obtain the simple relation _⃗l⊥ ≃−⃗lq ⊥_ = _⃗ℓ⊥_ . 

While the exact distribution of _δz⊥_ may be difficult to surmise from the above form, we can calculate the leading contributions to the width of this distribution, by calculating, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0005-09.png)


<!-- Start of picture text -->
� d 2 δz⊥δz⊥ 2 ∂d 22 W δz·g⊥⊥<br>⟨δz⊥ 2 ⟩ = . (23)<br>W  · g⊥<br><!-- End of picture text -->

Where, W _· g⊥_ = W _µνg⊥_<sup>_µν_.Carryingoutthep</sup><sup>_⊥_integra-</sup> tion, the above expression can be expressed as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0005-11.png)


<!-- Start of picture text -->
g⊥ µν Tr γ 2 − γµ γ 2 + γν L + ∆ 2 ⊥<br>� �<br>⟨δz⊥ 2 ⟩ = d 2 δz⊥dyd 2 l⊥d 2 lq ⊥<br>� 2Ω(2 π ) 7<br>g 2 Gαβ ( l ) Tr[ γ + γ α /lqγ β ]<br>× �( − 1) ∇⃗ l⊥·⃗ ∇lq ⊥ 2 q − y (1  − y ) 4 L 2 ⊥<br>− ( L⊥ − P∆ + 2 −q + ) 2<br>× e + e −i ( ⃗l⊥ + ⃗lq ⊥ ) ·δ⃗z⊥ W  · g⊥. (24)<br>� �<br><!-- End of picture text -->

In the equation above, _L⊥_ =<sup>_l_</sup> _⊥_<sup>2</sup> _/_<sup>[2</sup><sup>_q−y_]</sup> +<sup>_lq_</sup> 2 _⊥_<sup>_/_[2</sup><sup>_q−_(1</sup><sup>_−y_)].</sup> Thus, for either gradient _∇l⊥_ , or _∇lq ⊥_ , we obtain, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0005-13.png)


<!-- Start of picture text -->
∂L⊥<br>∇l⊥ f( L⊥ ) = ∂ f 2 ⃗l⊥, (25)<br>∂L⊥ ∂l⊥ 2<br><!-- End of picture text -->


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0005-14.png)


<!-- Start of picture text -->
(2 π ) 2 δ ( ¯p + + P + +  q + − l + − lq +) δ ( q− − l− − l q − ) . (21)<br><!-- End of picture text -->

Using the above equations, we can carry out the _lq_<sup>_−_</sup> and p¯<sup>+</sup> integrations. All these simplifications yield, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0005-16.png)


<!-- Start of picture text -->
Tr γ −<br>� 2 γµ γ 2 + γν �<br>W µν = L + (22)<br>Ω<br>dyd 2 l⊥ d 2 lq ⊥ d 2 p¯ ⊥<br>×<br>� (2 π ) 3 2 y d 2 δz⊥ (2 π ) 2 2 q − (1  − y ) (2 π ) 2<br>γ + q −<br>× g 2 Tr � γ 2 − l⊥ 2 / y  + lq 2 ⊥ / (1  − y ) γα/lqγβ<br>× l⊥ 2 / y  + γ + lq q 2 ⊥ −/ (1  − y ) � exp� − ∆ p¯ ⊥ 2 ⊥ 2 �<br>− ( l ⊥ 2 / 2 l− + lq 2 ⊥ / 2 l q − − P + − q + ) 2<br>× exp<br>� ∆ 2 + �<br>× Gαβ ( l ) e −i ( ⃗l⊥ + ⃗lq ⊥ ) ·δ⃗z⊥ .<br><!-- End of picture text -->

where, f = exp _{−_<sup>(</sup><sup>_L_</sup> _⊥_<sup>_−_</sup> P<sup><u>+</u></sup> _− q_<sup>+</sup> )<sup>2</sup> _/_ ∆<sup>2</sup> +<sup>_}/L_</sup> _⊥_<sup>2.</sup> The factor P<sup><u>+</u></sup> + _q_<sup>+</sup> is positive definite and is related to the mean virtuality of the hard quark after scattering as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0005-18.png)


<!-- Start of picture text -->
⟨µ 2 ⟩≃ 2(P + +  q + ) q − . (26)<br><!-- End of picture text -->

Using the above expression in combination with the mean formation time _τ_ =<sup>2</sup><sup>_q−_</sup> _/⟨µ_<sup>2</sup> _⟩_ , we can carry out the integrations over _δz⊥_ . The remaining term that depends on _l⊥_ and _lq ⊥_ is g = _Gαβ_ ( _l_ ) _Tr_ [ _γ_<sup>+</sup> _γ_<sup>_α_</sup> _/lqγ_<sup>_β_</sup> ]. 

Carrying out the successive differentials, using Eq. (25), and setting _⃗l⊥_ = _−⃗lq ⊥_ = _⃗ℓ⊥_ , will yield several terms. In this first attempt to derive the transverse width, we will only retain the most singular contribution in terms of _ℓ⊥_ , i.e., terms which contain the quadratically divergent<sup>_dℓ_2</sup> _⊥/_<sup>_ℓ_</sup> _⊥_<sup>4terms.Collecting these terms from</sup> 

6 

_∇l⊥·⃗ ∇lq ⊥_ (f _·_ g), we obtain, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0006-02.png)


<!-- Start of picture text -->
2 L + ∆ 2 ⊥ 8 g 2<br>⟨δz⊥ 2 ⟩ = dyd 2 ℓ⊥ (27)<br>� Ω(2 π ) 5<br>3(1  − y ) 3 + 3 2 (1  − y )  − 1<br>� �<br>×<br>ℓ 4 ⊥<br>− ( ℓ ⊥ 2 / [2 q−y (1  − y )]  − 1 /τ ) 2<br>×  exp W  · g⊥.<br>∆ 2<br>� + ��<br><!-- End of picture text -->

Substituting _ℓ_<sup>2</sup> _⊥_<sup>=</sup><sup>_µ_2</sup><sup>_y_(1</sup><sup>_−y_), where</sup><sup>_µ_2 is the virtuality</sup> of the parton before the split, we obtain, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0006-04.png)


<!-- Start of picture text -->
⊥ 8 αS − � µ 2 − ⟨µ 2 ⟩ �2<br>⟨δz⊥ 2 ⟩ = 2 L Ω(2 +∆ π 2 ) 3 � dydµ 2 exp (2 q − ∆+) 2<br>� �<br>3(1  − y ) 3 + 2 3 (1  − y )  − 1<br>� �<br>× W  · g⊥. (28)<br>µ 4 y (1  − y )<br>�<br><!-- End of picture text -->

Carrying out the _y_ integration, we would obtain, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0006-06.png)


<!-- Start of picture text -->
− ( µ 2 −⟨µ 2 ⟩ ) 2<br>2 L Ω + (∆2 π 2 ⊥ ) 3 αS � dµµ 2 2 µ 202 log � 1 ϵ � e (2 q − ∆+) 2<br>⟨δz⊥ 2 ⟩ = . (29)<br>W  · g⊥<br><!-- End of picture text -->

The integration over _y_ in Eq. (27) is carried out from _ϵ_ to 1 _− ϵ_ , yielding � _ϵ_ 1 _−ϵ_ 1 _/y ≃_ log(<sup>1</sup> _/ϵ_ ), where _ϵ_ is an infrared regulator (the exact form of this regulator has no significance for the calculation of _⟨δz⊥_<sup>2</sup><sup>_⟩_).Usingsim-</sup> ilar approximations and steps for the denominator, we obtain, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0006-08.png)


<!-- Start of picture text -->
− ( µ 2 −⟨µ 2 ⟩ ) 2<br>W  · g⊥ = 2 L +∆ ⊥ 2 αS e (2 q − ∆+) 2 . (30)<br>Ω(2 π ) 3 � dµµ 2 2 2 log � 1 ϵ �<br><!-- End of picture text -->

Inspection of Eqs. (29,30) yields the approximate relation between the size of a splitting parton and its virtuality: 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0006-10.png)


<!-- Start of picture text -->
δz⊥ 2 ≃ 10 . (31)<br>µ 2 ≃ 10 ⟨y ( ℓ 12 ⊥  − y ) ⟩<br><!-- End of picture text -->

In the equation above _y_ is the forward momentum fraction of the radiated gluon. The angle brackets _⟨y_ (1 _− y_ ) _⟩_ indicate the mean or typical value of the _y_ -dependent factor (since _y_ was integrated out to obtain the above equations). For a typical value of the momentum fraction of a gluon radiated from a quark ( _y ∼_<sup>1</sup> _/_ 10), one obtains the expected relation: 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0006-12.png)


<!-- Start of picture text -->
δz⊥ ≈ 1 , (32)<br>ℓ⊥<br><!-- End of picture text -->

in units where ℏ = 1 (in real units: _δz⊥ ≈_<sup>ℏ</sup> _/ℓ⊥_ ). 

The equation above is what one would have expected from a _na¨ıve_ application of the uncertainty principle. It is reassuring to recover this relation using a fully quantal 

treatment of a hard quark radiating a gluon. We hasten to point out that, in the derivation above, the parent parton (quark) has a vanishing average transverse momentum. The hard quark, produced in the deep-inelastic scattering of the virtual photon with the incoming quark (Fig. 1), proceeds along the outgoing “jet axis”. The radiating gluon and outgoing quark (which encounter the cut line in Fig. 1 and are thus considered on shell) possess opposing transverse momenta of _⃗ℓ⊥_ . However, the uncertainty size of the _parent quark_ is _∼_<sup>1</sup> _/ℓ⊥_ . The parent quark reaches this size at the point where it splits into the outgoing quark and gluon [with momentum fractions _y_ and (1 _− y_ )], i.e., at the formation time _τ_ =<sup>2</sup><sup>_q−y_(1</sup><sup>_−y_)</sup> _/ℓ⊥_<sup>2.</sup> 

All of the above considerations apply to the single split from a hard quark. Realistic jets contain many partons which arise from multiple splits, each of which will be affected by its uncertainty size. In the subsequent section, we will estimate the combined effect of these multiple splits, each with a minimum uncertainty size, on the entire transverse size of jets. 

## **III. CALCULATING JET TRANSVERSE SIZE WITH A MONTE-CARLO IMPLEMENTATION** 

In the preceding section, we derived the transverse uncertainty size of a radiating quark, at the point where the radiating gluon and outgoing quark have split off from the parent quark. This represents the size at one split. In a typical jet shower, there are several splits, with successive partons emitted at larger angles away from the jet direction. Thus, the outgoing shower spreads to a larger transverse size with increasing time. The most straightforward means to calculate this increasing transverse size is to use a Monte-Carlo parton shower event generator. 

All current Monte-Carlo simulators of parton showers in the vacuum [50–52], have no need to determine this size, and thus operate entirely in momentum space. All current Monte-Carlo simulators of partons showers in a medium [14–16, 18–20, 53] tend to use either the classical (antenna) size [46] of the shower, or do not ascribe any transverse size to the shower. In this section, we will outline the differences between the quantum transverse uncertainty size and the classical or antenna transverse size of the shower. 

A related question is when does the radiating or splitting parent quark reach this transverse size. As stated above, this size is reached at the point of the split. The longitudinal location of the split depends on the formation time which describes the mean longitudinal location of the split. Returning to Eq. (19), we note that we had integrated over _z_ ¯<sup>_−_</sup> yielding a _δ_ ( _δp_<sup>+</sup> ). This was done in the interest of keeping the expressions less cumbersome. Following Ref. [15], we can integrate over _δp_<sup>+</sup> instead to obtain a multiplicative Gaussian factor of � _dz_ ¯<sup>_−_</sup> exp� _−z_ ¯<sup>_−_</sup> ∆<sup>2</sup> +�. This factor will remain in all following equations including Eqs. (29) and (30). Incorporating this factor will modulate the entire form for W<sup>_µν_</sup> 

7 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0007-01.png)


<!-- Start of picture text -->
𝛿𝑧1,⊥<br><!-- End of picture text -->

FIG. 2. The antenna picture of a developing parton shower, in coordinate space. Most jet configurations are not planar (as seemingly indicated by the figure). 

in Eq. (22), leading to a Gaussian dependence of the actual mean split time _z_ ¯<sup>_−_</sup> , as demonstrated in Ref. [15]. As done in Ref. [15], one sets ∆+ so that the mean split time equals the formation time _τ_ = 2 _E/µ_<sup>2</sup> , where _µ_ is the off-shellness or virtuality of the splitting parton. 

The uncertainty size _δz⊥_ combined with the split location _z_ ¯<sup>_−_</sup> , allows for multiple interpretations of the transverse size of the radiating partons. The simplest would be the typical (or classical) antenna size: Assume partons are classical point like particles, that follow classical straight line trajectories. This case is illustrated in Fig. 2. The initial partons have the largest virtuality, even compared to their energy, and thus have the shortest formation times, and the shortest lengths in the figure. The first split typically has the largest _l⊥_ and thus is drawn with the largest angle. Subsequent partons tend to live longer (and thus have longer path-lengths), and smaller opening angles, with smaller values of transverse momentum _ℓ⊥_ . It should be stressed that what is drawn in Fig. 2 represents the typical event. Specific events may present with the later splits being wider than earlier spits, if angular ordering is not imposed. 

Consider the same splitting process, but now with the inclusion of quantum uncertainty. Each splitting parton will have a transverse size given by Eq. (31) or Eq. (32). This transverse size is indicated using the orange cones surrounding the partons in Fig. 3. The cones represent the mean uncertainty of the location of the split point. As a result, the outgoing partons are located on these cones. A “semi-classical” means to imagine the developing wave-packets is to consider that each wave packet contains, within it, the two wave-packets of the partons that are about to split. These splitting wave-packets separate from each other at the formation length, at which point they are on the cone boundary, with their _mean_ location given by their respective momenta. The momenta of the partons in Fig. 2 and Fig. 3 are the same. However, the larger size of the shower due to quantum uncertainty, compared to the classical antenna picture, is evident. 

We point out here that the picture generated in Fig. 3, is one means to give a classical interpretation to a quantum phenomena. One could take a somewhat different approach, e.g., not limiting the cones to the mean width, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0007-07.png)


<!-- Start of picture text -->
𝛿𝑧!,#<br>𝛿𝑧!,#<br><!-- End of picture text -->

FIG. 3. The picture of a developing shower, in coordinate space, using quantum uncertainty arguments. The partons within each wavepacket have the same momenta as in Fig. 2. 

but requiring both daughter partons to originate at the same point on the cones. While this may lead to a slightly different estimate of the transverse size of the shower, it _will_ lead to a shower that is wider than that given by a classical antenna simulation. 

To obtain a quantitative estimate of this effect we calculate the average size of showers using the MATTER vacuum generator [14, 15] within the JETSCAPE framework [21]. A single parton with fixed momentum along the _x_ -axis is initiated and then allowed to shower for a fixed amount of time. To determine the size of the shower at a given time, we use the following measure: 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0007-11.png)


<!-- Start of picture text -->
Nevents Ni<br>1 1<br>r⊥ = Nevents � Ni � � yj 2 +  z j 2 +  δrj ⊥ 2 . (33)<br>i =1 j =1<br><!-- End of picture text -->

In the equation above, _Ni_ represents the number of partons in event _i_ , and _yj, zj_ represent the _y, z_ components of parton _j_ at the time where the size is being determined. The _δrj ⊥_ is the uncertainty size of the splitting parton at the time when the size is being determined. In the case of antenna simulations, i.e. Fig. 2, _δrj ⊥_ = 0. However, this is non-zero for the case of simulations where the quantum size is retained in the simulation (Fig. 3). 

Throughout this section, we use the term, “transverse size of jet shower” (or “transverse size of parton shower”, or just simply “transverse size of shower”), instead of “transverse size of jet”. This is because no jet clustering algorithm [54] has been exercised on the final partons. We consider all the partons within some specified kinematic conditions, emanating from an initial hard quark. 

The originating parton, a quark with an _E_ = 100 GeV starts at _x_ = _y_ = _z_ = 0, and moves in the _x_ -direction. The virtuality is assigned by sampling the Sudakov form factor with a maximum allowed value of _Q_ ≲ _E/_ 2. This choice of maximum allowed virtuality has led to the agreement between JETSCAPE simulations and a wide range of experimental data [38–40, 44, 55]. As splits happen, the outgoing shower spreads in the _y_ and _z_ direction. With repeated splits, the virtuality of the partons continues to drop. A given parton stops splitting once its 

8 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0008-01.png)


<!-- Start of picture text -->
QuarkJet100 GeV,10Kevents<br>Transverse Size at t =5fm/c<br>6000<br>Classical<br>Semi-Quantum<br><1>P/4000<br>Events<br>NP 2000<br>0.5 1.522.5 3.5<br><r>[fm]<br><!-- End of picture text -->

FIG. 4. Comparison of the transverse size of a developing shower from a 100 GeV quark jet at 5fm/c. The black dashed line is the classical antenna size, while the red solid line in the quantum uncertainty size. The maximum allowed offshellness of the initial hard parton is _Q ≤_ 50 GeV. The plot clearly shows the larger quantum size compared to the classical antenna size. See text for further details. 

virtuality reaches _Q_ 0 ≲ 1 GeV. Partons that have a virtuality at or below _Q_ 0, or those that have a split time well in excess of the time of observation ( _t_ = 5 fm/c), are free-streamed to this point in time. 

We first present the results of two separate simulations, each with 10K events: The first, where only the antenna size of the shower is retained in the simulation (this is what one would obtain by running MATTER _out-of-thebox_ ). The transverse size is calculated using partons in the jet’s hemisphere: _px ≥_ 0. This is indicated by the black dashed line in Fig. 4. The transverse size has a rising contribution at _r⊥ →_ 0. This emanates from contributions where the partons do not split (or have one soft split), and thus have an _r⊥ ≃_ 0. The entire distribution also has a wide and local maxima at 1 _._ 5 ≲ _r⊥_ ≲ 2 fm. To our knowledge, this is the first paper that attempts to calculate the transverse size of a hard jet shower in coordinate space. The plot indicates that at 5 fm/c, where jets typically have their maximal interaction with the dense medium [38] in a heavy-ion collision, the overall size of the jet shower is considerable, _∼_ 2 fm. This is just the effective radius of the jet shower as defined by Eq. (33). All simulations in this section are carried out in the vacuum, and no hadronization is applied. The sizes presented in Figs. 4, 5 are partonic sizes. 

In the second set of simulations, we initialize the hard parton in the same way as above; however, at each split, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0008-06.png)


<!-- Start of picture text -->
QuarkJet100GeV,50Kevents<br>Transverse Size att=5fm/c<br>2GeV<Q<3GeV<br>4GeV<Q<5GeV<br>9GeV<Q<10GeV<br><>P/<br>10<br>10 0 0.5 1.522.5 3.5<br><r>[fm]<br><!-- End of picture text -->

FIG. 5. The quantum transverse size distributions of jets at _t_ = 5 fm/c, with initial off-shellness ( _Q_ ) limited to 3 narrow windows. The initial parton in each case is a quark with _E_ = 100 GeV. See text for description of plots. 

we shift the physical location of the daughter partons to the edge of the wave-packet, as indicated in Fig. 3. As would be expected, this leads to a larger transverse size of the jet shower at _t_ = 5 fm/c. This is indicated by the red solid line in Fig. 4. One notices the lack of the spike at _r⊥ →_ 0. This is because partons that do not split, now have an uncertainty size given by _δr⊥_ . 

The initial hard quark in either simulation, with or without uncertainty broadening, are restricted to a maximum virtuality of _Q_ ≲ _E/_ 2 ( _E_ = 100 GeV, the energy of the parton). In each event, the actual virtuality of the parton can vary, logarithmically, between _Q_ 0 _≃_ 1 GeV and _E/_ 2. One may infer that this wide range in virtuality yields the broad distribution of jet transverse sizes in Fig. 4. This is not entirely true. While partons with very large initial virtuality do eventually lead to jets with a wide transverse size, at intermediate virtualities, the relation is not very clear cut. To illustrate this, we plot the transverse size of jets at _t_ = 5 fm/c, which start within narrow ranges of virtuality. The three cases studied in Fig. 5, are 2 GeV _≤ Q ≤_ 3 GeV (green solid), 4 GeV _≤ Q ≤_ 5 GeV (red dashed), and 9 GeV _≤ Q ≤_ 10 GeV (blue dot-dashed). The number of events is increased to 50K for better statistics. 

While jet showers produced in the large virtuality bin (9 GeV _≤ Q ≤_ 10 GeV) do indeed produce larger transverse sizes, at lower virtualities, there seems to be no clear relation between virtuality and transverse size. This is due to the compensatory effect between the intrinsic uncertainty size of individual partons [ _δrj ⊥_ in Eq. (33)], and 

9 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0009-01.png)


<!-- Start of picture text -->
QuarkJet100GeV,50Kevents<br>Transverse Size at t=5fm/c<br>5×10<br>P>0GeV<br>P>2GeV<br>4×10°<br>PT>10 GeV<br>3x10°<br><1>P/”<br>2×10°<br>1x10*<br><r>[fm]<br><!-- End of picture text -->

FIG. 6. The transverse size of the jet shower with a minimum _pT_ cutoff on the included partons. Results for _pT >_ 0 GeV, 2 GeV, or 10 GeV are plotted and show a narrowing of the jet shower with increasing _pT_ of the constituents. 

the antenna size of the shower [ _yj, zj_ in Eq. (33)]. Lower virtualities lead to smaller antenna sizes, but larger intrinsic uncertainty sizes (and _vice-versa_ ). 

Two observations stand out in the current section: As stated above, the relation between virtuality and the transverse size of jet showers is not straightforward. Second, jet showers have a much larger transverse size than what one would na¨ıvely expect. They are not narrow phenomena localized along a line, but may interact with a large region of the medium (if they were produced in a heavy-ion collision, or other media). 

Also, the widest parts of the jet are composed of the softest partons, with the hard core propagating along a narrower cone. This is illustrated in Fig. 6. We again start with a quark, possessing an energy of _E_ = 100 GeV, with its virtuality distributed logarithmically from _Q_ 0 = 1 to _Q_ Max = 50 GeV. The solid red line illustrates the same transverse size distribution as the _semi-quantum_ line in Fig. 4. The green dot-dashed line results when we only retain partons with _px >_ 2 GeV, and the blue dashed line only contains partons with _px >_ 10 GeV. 

One notes a gradual narrowing of the shower at 5 fm/c, as the focus shifts to the harder core of the shower. However, at 5 fm/c, the shower does not possess a _perturbative_ size ( _r⊥_ ≲ 0 _._ 2 fm _≃_ 1 GeV<sup>_−_1</sup> ). Its mean size is closer to _r⊥ ∼_ 1 fm. Thus, even the hardest part of the shower is quite extended around a _t_ = 5 fm/c. The transverse size at earlier times is indeed smaller, as shown in Fig. 7. Here we plot the hard sector of the jet shower (with all constituent parton _pT >_ 10 GeV), at various time inter- 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0009-07.png)


<!-- Start of picture text -->
QuarkJet100GeV,50Kevents<br>Transverse Sizes for pt > 10 GeV<br>=1 fm/c<br>1×10<br>=2.5fm/c<br>5fm/c<br><1>p/<br>1×10<br>0.1<br>[uy]<′1><br><!-- End of picture text -->

FIG. 7. The dependence of the transverse size for the hard part (parton _pT >_ 10 GeV) of a jet-shower as a function of time for 3 different times: 1 fm/c (red solid), 2.5 fm/c (green dot-dashed) and 5 fm/c (blue dashed). The reader should note the log-log nature of the plot. The blue dashed 5 fm/c line is identical to the blue dashed line in Fig. 6. 

vals: The red solid line is after 1 fm/c, the green dotdashed line is after 2.5 fm/c, and the blue dashed line after 5 fm/c is the same as the blue dashed line in Fig. 6. Thus, at very early times (1 _−_ 2 fm/c), the jet transverse size is indeed at a perturbative scale (0 _._ 1 _−_ 0 _._ 2 fm). 

For the remainder of this section, we will imagine that after formation, the jet propagates through a static quark-gluon plasma (QGP) with a _T_ ≳ 0 _._ 3 GeV, and then return to the case of jets propagating through a large nucleus (in A-DIS). The two sets of numerical values that follow, illustrate the different abilities of coldconfined and hot-deconfined, strongly interacting media to affect the hard core of jets. 

Typical arguments based on _coherence_ or interference in jet quenching [45, 46, 48] indicate that the early hard portion of the jet is too small to be resolved by typical excitations in the medium. This depends on the scale of the medium. While this may be true at _t_ = 1 fm/c, it is hard to see this by 2.5 fm/c. One should recall that in most modern simulations of the bulk evolution, the QGP is not even fully formed at 1 fm/c [56, 57]. A typical thermal scale in a QGP at RHIC or LHC (at _T ≃_ 0 _._ 3 _−_ 0 _._ 4 GeV) is _λT ∼_<sup>ℏ</sup> _/T ∼_ 0 _._ 5 _−_ 0 _._ 67 fm. Looking at the plot in Fig. 7, it is somewhat hard to accept that there is no interaction with the medium by 2.5 fm/c. This argument for no interaction with the medium, at early times, becomes further tenuous as one uses the harder medium scale of _µ_<sup>2</sup> med<sup>=</sup><sup>_qt_ˆ.</sup> For the case of nucleus- 

10 

nucleus ( _A_ - _A_ ) collisions, we use the estimate of a static QGP, where at _t_ = 1 fm/c, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0010-02.png)


<!-- Start of picture text -->
1 1<br>λ AA µ ( t  = 1fm / c)  ≃ ≃ (34)<br>µ med √ qt ˆ ≃ 0 . 2 fm .<br><!-- End of picture text -->

The last equality is obtained by setting _q_ ˆ = 1 GeV<sup>2</sup> /fm (typical of fits for jet quenching in a QGP at RHIC and LHC [58]). These sizes can be easily achieved by jet showers at _t_ = 1 fm/c. Thus, one should assume that a QGP medium can easily resolve the hard core of jets already at 1 fm/c. 

Returning to the case of quark jets in a large nucleus (A-DIS), we can obtain the _q_ ˆ from fits of the same formalism to the attenuation of leading hadrons as a function of their momentum fraction _z_ = _p_<sup>_−_</sup> _h_<sup>_/q−_[25,59].Fora</sup> typical value of _q_ ˆ _≈_ 0 _._ 1 GeV<sup>2</sup> /fm, we obtain the resolution scale of the cold medium in a large nucleus at _t_ = 2 _._ 5 fm/c as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0010-05.png)


<!-- Start of picture text -->
1 1<br>λ eA µ ( t  = 2 . 5fm / c)  ≃ ≃ (35)<br>µ med √ qt ˆ ≃ 0 . 4 fm .<br><!-- End of picture text -->

Our simulation results in Fig. 7, show that the jet easily grows past a transverse radius of 0 _._ 4 fm after _t_ = 2 _._ 5 fm/c, even in the vacuum. The rather weak dependence on _q_ ˆ is due to the square root taken in the equations above. Thus, the hard core of jets is also not unresolved by the cold confined medium of a large nucleus after 2.5 fm/c. This does not mean that the interaction with the medium is strong, at this time. These observations simply argue for the need of a more developed formalism for jet medium interaction, during the early high-virtuality stage of the jet. The subsequent section will specifically address this. 

In the preceding section, we derived the transverse size of a splitting parton in vacuum, from quantum uncertainty arguments. In this section, we provided a semi-classical or semi-quantum visualization of this uncertainty size, e.g., in Fig. 3, and incorporating this in Monte-Carlo simulations, generated the transverse size of developing jet showers, still entirely in the vacuum. The generated transverse sizes strongly question the _coherence_ based arguments that the early, high virtuality jet shower is too small to be resolved by the medium. We repeat again, this does not mean that the interaction with the medium at this stage is strong. In the subsequent section, we calculate the waxing of this interaction with the medium at higher parton virtuality. 

## **IV. MEDIUM MODIFIED KERNEL FROM DIS** 

In the preceding sections, we first calculated the transverse uncertainty size of a splitting quark, produced in a hard interaction. Using this iteratively in a parton shower, we then demonstrated that jet showers are rather broad objects, with a non-trivial dependence of the transverse size on the initial virtuality _Q_ of the hard par- 

ton. We further demonstrated that, similar to a single split, showers get broader with time. However, even at times as early as 1 fm/c, the typical shower from a 100 GeV quark still seems to be broad enough to be resolved at the medium scale of _µ_<sup>2</sup> med<sup>_≈_</sup><sup>_~~√~~_</sup> 2ˆ _qE_ (assuming _q_ ˆ _∼_ 1 GeV<sup>2</sup> /fm). 

We reiterate: Simply because the jet shower is resolved does not mean that the interaction with the medium is strong. In the high virtuality stage of a jet, the effect of the medium on a split is quantified by the ratio, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0010-12.png)


<!-- Start of picture text -->
q ˆ τ<br>≪ 1 , (36)<br>µ 2 ≃ q ˆ µ 24 E<br><!-- End of picture text -->

where, _E_ and _µ_ are the energy and virtuality of a given parton in the shower that is about to split, and _q_ ˆ is the transport coefficient specific to that parton. Beyond this, there is still a further weakening of the effective transport coefficient at large virtualities, i.e., there is an energy and scale dependence in _q_ ˆ: 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0010-14.png)


<!-- Start of picture text -->
q ˆ → q ˆ( E, µ 2 ) . (37)<br><!-- End of picture text -->

In this section, we will evaluate this dependence. 

To evaluate the effective dependence of _q_ ˆ on the energy _E_ and virtuality _µ_<sup>2</sup> of the hard parton, we will return to the straightforward process of deep-inelastic scattering on a large nucleus, as in Sec. II. The hadronic tensor, in the case of single gluon emission and scattering in the final state is given as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0010-17.png)


<!-- Start of picture text -->
W µν = � q � dydπ 2 ℓ⊥ fq A ( x ) dℓ d K2 ⊥ � q − , y, ℓ 2 ⊥ � H 0 µν,  (38)<br><!-- End of picture text -->

where _H_ 0<sup>_µν_</sup> is the partonic hard part [23, 24, 30] and K ( _q_<sup>_−_</sup> _, y_ ) is known as the medium modified kernel, and _fq_<sup>_A_(</sup><sup>_x_)isthenuclearpartondistributionfunctionofa</sup> quark with momentum fraction _x_ . The nucleus moves in the (+)-light cone direction with momentum _PA_<sup>+=</sup> _AP_<sup>+</sup> . The virtual photon has momentum components _q ≡_ ( _q_<sup>+</sup> _, q_<sup>_−_</sup> _,_ 0 _,_ 0), with _q_<sup>+</sup> = _−xBP_<sup>+</sup> , where _xB_ = _Q_<sup>2</sup> _/_ (2 _P_<sup>+</sup> _q_<sup>_−_</sup> ) is the Bjorken- _x_ variable. In the equation above, _yq_<sup>_−_</sup> _, ℓ⊥_ are the large light-cone and transverse momentum components of the radiated gluon. Note that _x_ in _fq_<sup>_A_(</sup><sup>_x_)isafunctionof</sup><sup>_xB, y, ℓ_</sup> _⊥_<sup>2.</sup> 

The expressions above appear different from those in Sec. II. In Sec. II, we did not consider scattering in the final state. We were interested in elucidating the transverse size of the radiating hard quark. In the current section, we are interested in studying the momentum structure of the single gluon emission kernel at next-to-leading twist, that leads to medium modified emission (or stimulated emission). As a result, all of the position integrations that were analysed in Sec. II, have been integrated out. The factor _y_ is the light-cone momentum fraction of the radiated gluon and not a position, as in Sec. II. 

11 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0011-01.png)


<!-- Start of picture text -->
lq.<br>P ps<br><!-- End of picture text -->

FIG. 8. Single gluon emission from the outgoing struck quark produced in the deep-inelastic scattering off a large nucleus followed by a scattering on gluon. This is the only contributing Feynman diagram when _k⊥_ dependence in the phase is ignored in the _k⊥_ expansion. 

## **A. Medium Modified Kernel in the limit of soft gluon emission approximation** 

In Eq. (38) the gluon emission kernel from the hard outgoing quark is medium modified. The medium modification arises from the scattering of this hard quark and radiated gluon off the glue field of the remaining nucleons, through which the quark and gluon propagate prior to hadronization. The excess radiation due to the scattering is denoted as energy loss of the fragmenting quark. 

Parton energy loss in DIS is calculated within the soft and collinear gluon emission approximation using the higher-twist formalism in Refs. [23, 24]. This involves several diagrams. However, if the factors of _k⊥_ in the phases (where they are divided by _q_<sup>_−_</sup> ) are ignored in the later Taylor expansion in _k⊥_ , then only one diagram contributes: The double gluon scattering diagram in Fig. 8. Incorporating this, the medium-modified kernel before collinear expansion is given by 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0011-06.png)


<!-- Start of picture text -->
dξ − dδξ − d 2 k⊥d 2 ξ⊥<br>KGW q − , y = αs d 2 ℓ⊥<br>2 π P ( y ) (2 π ) 2<br>( ℓ ⃗ ⊥ −⃗k ⊥ )2 ξ−<br>× 2  − 2 cos 2 q − y (12 −y ) e−i 2 q − yℓ 2 ⊥ (1 −y ) δξ− (39)<br>⃗ℓ⊥ −⃗k⊥<br>−i k⊥ 2 − 2 ⃗k⊥ ·⃗ℓ⊥ δξ − + i⃗k⊥·⃗ξ⊥<br>×e 2 yq −<br>× ⟨A| A + ξ − +  δξ − ,⃗ξ⊥ A + ξ − ,  0 |A⟩ .<br><!-- End of picture text -->

In the equation above, _ξ_<sup>_−_</sup> _, δξ_<sup>_−_</sup> represent the mean and offset in the light-cone locations of the scattering in the amplitude and complex conjugate, as depicted in Fig. 8, and _ξ⊥_ is the offset in the perpendicular locations. The above expression is derived in the light-cone gauge _A_<sup>_−_</sup> = 0. In this gauge, _A_<sup>+</sup> _≫ A⊥_ [31]. 

The differential yield of induced gluons, when the medium interaction is within the single gluon scattering 

per emission limit can be given by, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0011-10.png)


<!-- Start of picture text -->
dNg = d KGW = αs dξ − dδξ − d 2 k⊥d 2 ξ⊥<br>dydℓ 2 ⊥ dℓ 2 ⊥ 2 π 2 P ( y ) (2 π ) 2<br>( ℓ ⃗ ⊥ −⃗k ⊥ )2 ξ−<br>2  − 2 cos<br>2 q − y (1 −y ) −i ( ⃗ℓ⊥ −⃗k⊥ ) 2 δξ −<br>× 2 e 2 yq − (40)<br>⃗ℓ⊥ −⃗k⊥<br>×e−i 2 q − ℓ (1 2 ⊥−y ) δξ− e i⃗k⊥·⃗ξ⊥ ⟨A| A + δξ − ,⃗ξ⊥ A + (0)  |A⟩ .<br><!-- End of picture text -->

One immediately notes that the _ξ_<sup>_−_</sup> and _δξ_<sup>_−_</sup> integrations are factorized in the expression above. For the specific case of a system with translation invariance, i.e., the _⟨A_<sup>+</sup> _A_<sup>+</sup> _⟩_ correlator does not depend on the mean location _ξ_<sup>_−_</sup> (only on the relative separation), we can drop the _ξ_<sup>_−_</sup> dependence in the correlator. The _ξ_<sup>_−_</sup> integration can now be completed, integrating from _ξ_<sup>_−_</sup> = 0 to _ξ_<sup>_−_</sup> = 2 _τf_<sup>_−_=4</sup><sup>_<u>q−y</u>_</sup> _l⊥_<sup>2(1</sup><sup>_−y_</sup><sup><u>)</u></sup> , 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0011-12.png)


<!-- Start of picture text -->
dydℓdNg 2 ⊥ = 2 α π s 2 P ( y ) (2 d 2 πk ) ⊥ 2 (41)<br>2<br>8 q − y (1 −y ) − 4 q−y (1 −y ) 2( ⃗ℓ⊥−⃗k⊥ )<br>ℓ 2 ⊥ ( ⃗ℓ⊥−⃗k⊥ ) 2 sin ℓ 2 ⊥<br>×<br>2<br>⃗ℓ⊥ −⃗k⊥<br>× dδξ − d 2 ξ⊥e−i ( ⃗ℓ⊥ 2 −yq⃗k − ⊥ ) 2 δξ − e−i 2 q − ℓ (1 2 ⊥−y ) δξ− e i⃗k⊥·⃗ξ⊥<br>× ⟨A| A + δξ − ,⃗ξ⊥ A + (0)  |A⟩ .<br><!-- End of picture text -->

The general form of the equation above may be expressed as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0011-14.png)


<!-- Start of picture text -->
dN = αSP ( y ) d 2 k⊥<br>dydℓ 2 ⊥ π<br>× h ( ⃗k⊥, q − , y,⃗ℓ⊥ )  × g ( ⃗k⊥, q − , y,⃗ℓ⊥ ) , (42)<br><!-- End of picture text -->

where, _h_ contains the hard dynamics involving _ℓ⊥_ , _k⊥_ and _q_<sup>_−_</sup> , given by the second line of Eq. (41), and _g_ represents the soft matrix element (third and fourth line of the equation). A plot of _h_ for _q_<sup>_−_</sup> = 100 GeV, _y_ = 0 _._ 1, and _ℓx_ = _ℓy_ = 4 GeV is shown in Fig. 9. The function peaks in a conical structure around the point _k⊥_ = _ℓ⊥_ (in fact, _h_ = 0 at _k⊥_ = _ℓ⊥_ ). The rim-like structure has a radius of _δk⊥ ≃|⃗ℓ⊥|_ . Thus, the preponderance of values of _k⊥_ that enhance _h_ is large and of the order of _|⃗ℓ⊥|_ . This is in contrast with the soft matrix element _g_ , which is enhanced by small values of _k⊥_ , typically in the range _∼_ 1 GeV. In this paper, we are interested solely in the large virtuality limit, where _ℓ⊥ ≫_ 1 GeV. 

## **B. The Soft Matrix Element** 

Taking the limit of a large _ℓ⊥_ , which is much larger than the eventual _k⊥_ , we may simplify the equation for 

12 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0012-01.png)


<!-- Start of picture text -->
0.04<br>00<br>0.02<br>0.01<br><!-- End of picture text -->

FIG. 9. (Color Online) A plot of the hard portion (2nd line) of the differential gluon spectrum<sup>_dNg_</sup> _/dydℓ⊥_<sup>2inEq.(41)asa</sup> function of _⃗k⊥_ = _kxx_ ˆ + _ky_ ˆ _y_ . For the plot, _q_<sup>_−_</sup> = 100 GeV and _y_ = 0 _._ 1. Also we have set _ℓx_ = _ℓy_ = 4 GeV ( _⃗ℓ⊥_ = _ℓxx_ ˆ + _ℓy_ ˆ _y_ ). The function yields a steep cone like structure centered at _k⊥_ = _⃗ℓ⊥_ , with a rim radius approximately equal to _|⃗ℓ⊥|_ . 

the soft part _g_ ( _⃗k⊥, q_<sup>_−_</sup> _,⃗ℓ⊥_ ) as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0012-04.png)


<!-- Start of picture text -->
dδξ − d 2 ξ⊥ −i l 2 ⊥<br>g ( k⊥, q − , ℓ⊥ )  ≃ e 2 q − y (1 −y ) δξ− e i⃗k⊥·⃗ξ⊥<br>(2 π ) 3<br>× ⟨A| A + ( δξ − ,⃗ξ⊥ ) A + (0 ,  0)  |A⟩ . (43)<br><!-- End of picture text -->

Dropping the _⃗k⊥_ in the exponential for _δξ_<sup>_−_</sup> , along with the assumption that the two-point function is symmetric in _ϕξ⊥_ , leads to _g_ ( _k⊥, q_<sup>_−_</sup> _, y, ℓ⊥_ ) becoming independent of the azimuthal angle for _k⊥_ . The factor _g_ ( _k⊥, q_<sup>_−_</sup> _, y, ℓ⊥_ ), can then be expressed as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0012-06.png)


<!-- Start of picture text -->
g ( k⊥,q − , y, ℓ⊥ ) = xLP  + dδξ − d 2 ξ⊥ e −ixLP  + δξ− e i⃗k⊥·⃗ξ⊥<br>4 k⊥ 2 (2 π ) 3 xLP +<br>δξ − −δξ −<br>× ⟨A| F + ⊥ 2 ,⃗ ξ 2 ⊥ F⊥ + , 2 , −⃗ ξ 2 ⊥ |A⟩<br>(()<br>dδξ − d 2 ξ⊥ e −ixLP  + δξ− e i⃗k⊥·⃗ξ⊥<br>= ρxL<br>8 k⊥ 2 (2 π ) 3 xLP +<br>δξ − −δξ −<br>× ⟨P | F + ⊥ 2 ,⃗ ξ 2 ⊥ F⊥ + , 2 , −⃗ ξ 2 ⊥ |P ⟩<br>(-）(—)<br>= ρxL G ( xL, k⊥ ) . (44)<br>8 k⊥ 2<br><!-- End of picture text -->

_ℓ_<sup>2</sup> _⊥//_<sup>2</sup><sup>_q−P−PP_+</sup><sup>_y_(1</sup><sup>_−y_)</sup> , where 

In the equation above, _xL_ = _ℓ_<sup>2</sup> _⊥//_<sup>2</sup><sup>_q−P−PP_+</sup><sup>_y_(1</sup><sup>_−y_)</sup> , where _P_<sup>+</sup> = _PA_<sup>+</sup><sup>_/A_istheaveragelightconemomentumofone</sup> nucleon in the nucleus. We have further decomposed the nuclear state ( _|A⟩_ ) into nucleon states ( _|P ⟩_ ) as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0012-09.png)


<!-- Start of picture text -->
ρ<br>⟨A| . . . |A⟩≃ 2 P + ⟨P | . . . |P ⟩ , (45)<br><!-- End of picture text -->

where _ρ_ is the density of nucleons within the nucleus. The factor _G_ ( _xL, k⊥_ ) represents the gluon TMDPDF, and we have assumed that the operator product is translation invariant within the nuclear state _|A⟩_ . TMDPDFs even at leading order have a scale (¯ _µ_ ) dependence [60]. In this case, the scale of the TMDPDF is obviously _µ_ ¯<sup>2</sup> _≈ ℓ_<sup>2</sup> _⊥_<sup>.</sup> Thus, we will evaluate the quantity _G_ ( _xL, k⊥, ℓ_<sup>2</sup> _⊥_<sup>).One</sup> notes that _µ_ ¯<sup>2</sup> _≃ µ_<sup>2</sup> , the virtuality of the hard parton. Thus, in the remainder of this effort, we will simply use _µ_<sup>2</sup> as the scale of the TMDPDF, and hence, the eventual scale of the transport coefficient _q_ ˆ. 

## **C. Relating** _q_ ˆ **to the TMDPDF** 

The entire expression to be evaluated is, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0012-13.png)


<!-- Start of picture text -->
dN = αSP ( y ) d 2 k⊥h ( ⃗k⊥, q − , y,⃗ℓ⊥ )<br>dydℓ 2 ⊥ π<br>× ρxL G ( xL,⃗k⊥, ℓ⊥ 2 ) , (46)<br>8 k⊥ 2<br><!-- End of picture text -->

The standard method for calculating the above expression is to Taylor expand _h_ ( _⃗k⊥, q_<sup>_−_</sup> _,⃗ℓ⊥_ ) in _⃗k⊥_ , and take the second derivative, reducing the gluon yield to, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0012-15.png)


<!-- Start of picture text -->
dN = αSP ( y ) d 2 k⊥ ∇ 2 k⊥ h ( ⃗k⊥, q−, y,⃗ℓ⊥ )<br>dydℓ 2 ⊥ π 2!<br>k⊥ =0<br>× ρx 8 L G ( xL,⃗k⊥, ℓ ⊥ 2 ) . (47)<br><!-- End of picture text -->

The above expression is often expressed in terms of the jet transport coefficient _q_ ˆ as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0012-17.png)


<!-- Start of picture text -->
dN = αSP ( y ) ∇ 2 k⊥ h ( ⃗k⊥, q−, y,⃗ℓ⊥ ) ⊥ ) . (48)<br>dydℓ 2 ⊥ 2 π⃗ k⊥ =0 q ˆ( xL, ℓ 2<br><!-- End of picture text -->

In the above equation, _q_ ˆ, given as _d_<sup>2</sup> _k⊥ρxLG_ ( _xL,⃗k⊥, ℓ_<sup>2</sup> _⊥_<sup>)</sup><sup>_/_8,</sup> has an obvious dependence on scale ( _ℓ_<sup>2</sup> _⊥_<sup>)andtheenergyofthehardparton</sup> ( _q_<sup>_−_</sup> ), the momentum fraction of the radiated gluon ( _y_ ), via the momentum fraction _xL_ = _ℓ_<sup>2</sup> _⊥_<sup>_/_[2</sup><sup>_q−y_(1</sup><sup>_−y_)].It</sup> also may depend on location; we are neglecting this dependence by assuming _ρ_ to be a constant. Using Eq. (32), the dependence on scale can be thought of as a dependence on the transverse size ( _z⊥_ ) of the radiating antenna. We continue to use terminology such as “antenna”, for tha lack of a better term, even though our calculations refer to configurations such as those in Fig. 3. 

The above discussion implies that the interaction of a radiating parton with a medium (qualified by _q_ ˆ) depends on, among other things, the size of the radiating antenna (Fig. 3). The above discussion is somewhat different than the usual arguments of jet coherence, as it considers the transverse size at the point of formation and not after formation. Although, its overall phenomenological effect [38, 44] may indeed be indistinguishable from phenomenology based on typical coherence arguments. 

13 

Thus, to obtain the full scale (size) dependence of _q_ ˆ, we simply compare Eq. (46) with Eq. (48), to obtain, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0013-02.png)


<!-- Start of picture text -->
q ˆ( xL, ℓ 2 ⊥ )= � d 2 k 4 ⊥k⊥ 2 ρxL h ( ⃗k⊥, q − , y,⃗ℓ⊥ ) G ( xL,⃗k⊥, ℓ 2 ⊥ ) . (49)<br>∇⃗ 2 k⊥ h ( ⃗k⊥, q−, y,⃗ℓ⊥ ) ��� k⊥ =0<br><!-- End of picture text -->

The equation above, as written, is more general than the higher-twist approach used to derive it. It directly relates the TMDPDF of a given medium with the transverse momentum coefficient _q_ ˆ, and is true for any choice of _h_ . Similar relations have been suggested before [24, 43]. However, in this effort, we provide a straightforward derivation of this relation. It demonstrates with some clarity that the scale dependence of _q_ ˆ is directly related to the transverse momentum _k⊥_ , and the scale and _x_ dependence of the TMDPDF within the medium. 

## **V. RESULTS ON SCALE DEPENDENCE OF** _q_ ˆ 

In the preceeding section, we derived a relation between the gluon TMDPDF within the nucleons of a large nucleus and the jet transport coefficient _q_ ˆ. Eq. (49) can be solved at varying levels of complexity. The _h_ -function depends on approximations used in the derivation of the high-virtuality energy-loss kernel. The TMDPDF can be evaluated at varying levels of sophistication. In this paper, we will present the simplest possible version of this equation. The goal is for these results to be easily reproduced. More realistic calculations, including the attempt to extend these results to jets in a QGP will be left for a future effort. Our goal here is to simply elucidate the mechanics of the effect, making a clear connection between the TMDPDF and the scale dependence of _q_ ˆ. 

As such, we will use the method of Ref. [24], to obtain _⃗ ∇_<sup>2</sup> _k⊥_<sup>_h_(</sup><sup>_⃗k⊥, q−, y,⃗ℓ⊥_)</sup> ��� _k⊥_ =0<sup>,whereoneignoresderiva-</sup> tives on the phase. Although this was criticized in Refs. [61, 62] for being incomplete, a more general analysis including the full set of terms at next-to-leading twist [30], showed that the method of Ref. [24] is actually close to the complete result at _τ_ = 2 _τf_ . Within this approximation, we obtain, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0013-07.png)


<!-- Start of picture text -->
∇ 2 k⊥ h ( ⃗k⊥, q−, y,⃗ℓ⊥ ) . (50)<br>��� k⊥ =0 = 16 q−y (1 −y ℓ )6 ⊥  π [2 − sin (2)]<br><!-- End of picture text -->

Note that the corresponding _h_ factor is given by the second line of Eq. (41). 

We follow Aybat and Rogers [60], and express the gluon TMDPDF, at lowest order as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0013-10.png)


<!-- Start of picture text -->
G ( x,⃗k⊥, µ 2 ) =  F ( x ) e − 4 w ( kx,µ⊥ 2 2 ) (51)<br>4 πw ( x, µ 2 ) ,<br><!-- End of picture text -->

where, _F_ ( _x_ ) is the regular collinear parton distribution function (PDF) at lowest order, and the transverse width 

_w_ is given in the Brock-Landry-Nadolsky-Yuan form [63]: 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0013-13.png)


<!-- Start of picture text -->
g 2 log � 2 Qµ 0 �<br>w ( x, µ 2 ) = +  g 1 . (52)<br>2 � 21 +  g 3 log(10 x ) �<br><!-- End of picture text -->

The constants in the above equation are _Q_ 0 = 1 _._ 6 GeV, _g_ 1 = 0 _._ 21 GeV<sup>2</sup> , _g_ 2 = 0 _._ 68 GeV<sup>2</sup> , _g_ 3 = 1 _._ 6. Following Ref. [60], we take _F_ ( _x_ ) from the Martin-Stirling-ThorneWatt (MSTW) leading order parametrization, given in Ref. [64] as, 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0013-15.png)


<!-- Start of picture text -->
F ( x ) =  Ax δ (1  − x ) η (1 +  ϵ � ( x ) +  gx ) , (53)<br><!-- End of picture text -->

with _A_ = 0 _._ 0012216, _δ_ = _−_ 1 _._ 83657, _η_ = 2 _._ 3882, _ϵ_ = _−_ 38 _._ 997 and _g_ = 1445 _._ 5. Including higher orders will require evolving the above TMDPDF using the CollinsSoper equation [65]. In the interest of simplicity and ease of reproducibility, we will refrain from this, and use the TMDPDF as written in Eq. (51). 

In a realistic calculation, Eq. (51) provides the initial condition at a low value of _µ_<sup>2</sup> , and has to be evolved using the Collins-Soper equation to a _µ_<sup>2</sup> that is relevant to the physical problem. Carrying out this evolution will involve a certain amount of numerical computation. It will lead to a quantitative, but _not a qualitative_ , shift in our results. In a future effort, we plan to carry out this calculation using the full form of the hard sector function _h_ ( _⃗k⊥, q_<sup>_−_</sup> _, y,⃗ℓ⊥_ ), and an evolved form of the TMDPDF. The results presented in this paper can be reproduced by anyone, either by hand, or using analytic manipulation software such as _Mathematica_ (without the explicit use of any advanced numerical techniques). 

To carry out the _d_<sup>2</sup> _k⊥_ integration in the numerator of Eq. (49), requires an infrared regulator; we have set the minimum value of _k⊥_ to be Λ _QCD_ = 0 _._ 2 GeV. Incorporating all these terms, we can obtain the effective _q_ ˆ as a function of the inverse antenna size, given by _Q_<sup>2</sup> _≃ ℓ_<sup>2</sup> _⊥_<sup>at</sup><sup>_xL_=</sup><sup>_ℓ_</sup> _⊥_<sup>2</sup> _/_<sup>[2</sup><sup>_q−P_+</sup><sup>_y_(1</sup><sup>_−y_)]</sup> . For this estimate, since all our expressions are boost invariant for boosts in the _z_ -direction, we boost to the target frame and pick _q_<sup>_−_</sup> = 200 _~~√~~_ 2 GeV, with _P_<sup>+</sup> =<sup>1</sup> _/_ _~~√~~_ 2 GeV. We pick the radiated gluon’s momentum fraction as _y_ =<sup>1</sup> _/_ 2. In order to highlight the effect of evolution, we follow Ref. [38], and write 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0013-19.png)


<!-- Start of picture text -->
q ˆ( µ 2 ) = q ˆ  · f ( µ 2 ) , (54)<br><!-- End of picture text -->

i.e., we place the entire scale dependence in _f_ ( _µ_<sup>2</sup> ). Given the form of the TMDPDF, values of _µ_ = _ℓ⊥ ≡_ ~~�~~ ( _⃗ℓ⊥_ )<sup>2</sup> ⪅ 3 GeV correspond to a significant narrowing of the width _w_ ( _xL, µ_<sup>2</sup> ), coupled with a sharp rise in _F_ ( _xL_ ) [note _xL_ =<sup>_ℓ_2</sup> _⊥/_<sup>2</sup><sup>_q−P_+</sup><sup>_y_(1</sup><sup>_−y_)</sup> ]. As a result, given the choice of parameters, values of _µ_ ⪅ 3 GeV require a more careful numerical treatment. On the opposite end, for a _q_<sup>_−_</sup> = 200 _~~√~~_ 2 and _y_ =<sup>1</sup> _/_ 2, the maximum allowed value of _ℓ⊥_ = 10 GeV. Beyond this, the collinear PDF vanishies, i.e. _F_ ( _xL_ ) _→_ 0. As a result, we present the evolution of _q_ ˆ with scale _µ_ (= _ℓ⊥_ ) from 3.1 GeV to 9 GeV. 

14 


![](images/Chen_2025_VLM_Assisted_GUI_Testing_in_Mobile_Games.pdf-0014-01.png)


<!-- Start of picture text -->
0.8<br>0.6<br>0.4<br>0.2<br>9 10<br>μ[GeV]<br><!-- End of picture text -->

FIG. 10. A plot of the scaling function for _q_ ˆ as described in Eq. (54). _f_ ( _µ_<sup>2</sup> ) is determined by solving Eq. (49) and shows a rapid drop as a function of _µ_ . 

In Fig. 10, we present the behavior of the scaling function _f_ ( _µ_<sup>2</sup> ) from _µ_ = 3 _._ 1 GeV to 9 GeV. The function _f_ is defined such that at _µ_ = 3 _._ 1 GeV, _f_ = 1 and _q_ ˆ is the normalization, i.e., the value of _q_ ˆ( _µ_<sup>2</sup> ) at _µ_ = 3 _._ 1 GeV. The scaling function shows a strong dependence on the scale _µ_<sup>2</sup> , almost vanishing by the point _µ →_ 9 GeV. This is entirely consistent with the experimentally extracted forms of _f_ ( _µ_<sup>2</sup> ) in Refs. [38, 44], even though, those extractions were conducted for jets in a quark-gluon plasma. This is also consistent, though not obviously so, with the scale dependence of _q_ ˆ extracted in comparison with experimental data at RHIC and LHC energies in Ref. [43]. 

In prior efforts dealing with jet coherence and the non-interaction of jets of small transverse size with the medium, the entire effect is ascribed to the small size of the radiating antenna [45–48]. However, in our calculation, which considers the effect of the medium within the formation time of a radiation, the weakening of the effective transport coefficient _q_ ˆ with the scale of the splitting antenna arises from three separate effects. The first is the shrinking size of the radiating antenna, given by _δz⊥ ∼_<sup>1</sup> _/ℓ⊥_ , which leads to the antenna being affected only by transverse momenta, from the medium, of the same size as those from the antenna, i.e. _h_ is large when _k⊥ ∼ ℓ⊥_ . This is illustrated in Fig. 9. As one increases _ℓ⊥_ , it becomes less likely for the soft factor _g_ to produce a gluon with a _k⊥ ∼ ℓ⊥_ . This leads to the drop in _f_ ( _µ_<sup>2</sup> ) as _µ_ is increased from 3 GeV. As the scale _µ_ (= _ℓ⊥_ ) continues to increase, the width _w_ of the TMDPDF increases, and this increases the probability for larger _k⊥_ . This leads to the mild bump like structure between 4 and 6 GeV. Another reason for this structure is that it corresponds to an _xL_ in the range from 0.16 to 0.36 which is the least steep 

portion of _F_ ( _xL_ ). Larger values of _l⊥_ require comparable values of _k⊥_ , for _h · g_ to stop depreciating. However, there is almost no support from the TMDPDF for values of _k⊥_ larger that 6 GeV. This combined with the sharper drop in _F_ ( _xL_ ) for _xL →_ 1, leads to the precipitous drop of _f_ ( _µ_<sup>2</sup> ) with increasing _µ_ . 

A qualitative summary of the above analysis is that increasing the transverse momentum _ℓ⊥_ of a split, leading to smaller sizes of the radiating system, requires harder emissions from the medium to affect the splitting process. This becomes less probable with increasing _l⊥_ , and as a result, a radiating dipole has a progressively weaker interaction with the medium. This leads to a continuously decreasing effective _q_ ˆ with increasing _l⊥_ . Unlike the coherence based arguments [45, 46, 48], there is no sudden lack of interaction with the medium as the scale of the antenna drop below the medium scale _λ_<sup>_AA_</sup> _µ_ [Eq. (34)]. Instead there is a steady decrease in the effective _q_ ˆ due to the decreasing size of the radiating antenna, coupled with the _x_ and _k⊥_ dependence of the gluon-TMDPDF. Hence, we refer to the gradual weakening of the interaction, as a function of the scale of the radiating antenna (and by extension the scale of the gluon TMDPDF), described in this paper, as “Modified Coherence”. 

## **VI. SUMMARY AND OUTLOOK** 

Partons within jets are quantum mechanical objects. As such, their position and momentum uncertainties are related by Heisenberg’s principle. For all jet observables in vacuum, this uncertainty _size_ is almost irrelevant. However, for jets propagating through and interacting with a dense medium, an estimate of the mean and uncertainty of the location of a parton are essential. 

In earlier efforts, the transverse size of partonic showers was considered to be small compared to the size of the medium. Jet energy-loss event generators focused only on the longitudinal location of the developing shower [14, 15, 18, 19]. The transverse extent of the shower was either ignored or calculated using the classical antenna picture, where each parton traverses straight line trajectories. 

There is now a growing consensus that the hard virtual core of jets has a diminished interaction with the medium. Phenomenological fits based on multi-stage simulations [38–41, 44], which are compared with a wide swath of data, clearly indicate the presence of this diminishing interaction with increasing virtuality of the jet parton. Partons with a large virtuality, tend to produce spilts with a large momentum _ℓ⊥_ transverse to the direction of the parent parton. By uncertainty arguments, these splits should have a small size. This leads to the coherence based arguments that smaller antenna are not resolved by the medium and thus, these portions of hard jets evolve in the medium as a vacuum like shower [45, 46, 48]. 

The above arguments have prompted the current study, which was composed of three parts. In Sec. II, 

15 

we demonstrated that the transverse uncertainty size of splitting partons was indeed given by the na¨ıve relation _δz⊥ ∼_ 1 _/ℓ⊥_ . In Sec. III, we incorporated this relation within a Monte-Carlo parton shower and demonstrated the lack of a clear relation between the virtuality of the originating parton and the transverse size of the entire shower, as well as its hard core. In spite of this, in the next section, we found that each splitting parton has a diminishing interaction with the medium as its virtuality is increased, and this is caused by 3 separate effects: the shrinking size of the radiating parton requiring a larger _k⊥_ from the medium to affect the split, the scale dependent transverse momentum width and the _x_ dependence of the gluon TMDPDF, which sources the medium gluon, that interacts with the hard splitting parton. 

In Sec. IV, we derived a new equation [Eq. (49)], that can be used in any jet quenching formalism to deduce the relation between a gluon TMDPDF and the jet transport coefficient _q_ ˆ. At a phenomenological level, our results are similar to those derived using the “coherence” approach [45–48]. However, the exact reason for the diminishing interaction with the medium with increasing virtuality of the radiating parton is somewhat different. As a result, we refer to this effect as “Modified Coherence”. Basic and extensive phenomenology based on modified coherence, has already been carried out in Refs. [38– 41, 44], and show considerable agreement with a broad range of experimental data. 

Our final numerical results in Sec. V, were calculated using a simple model of the gluon TMDPDF, with parameters that were dialed by fits to data. We did not include a Collins-Soper evolution of the TMDPDF and explored a rather limited range in scale. Thus, our results will have to be improved upon. Our goal in this paper was to present a calculation that could be repeated by anyone without the need for any advanced numerical tools. In a future more numerical effort, one will be able to include lower scales and a full Collins-Soper evolution. 

- [1] G. Aad _et al._ (ATLAS), Measurement of the jet radius and transverse momentum dependence of inclusive jet suppression in lead-lead collisions at<sup>_~~√~~_</sup> _<u>sNN</u>_ <u>=</u> 2.76 TeV with the ATLAS detector, Phys. Lett. B **719** , 220 (2013), arXiv:1208.1967 [hep-ex]. 

- [2] S. Chatrchyan _et al._ (CMS), Observation and studies of jet quenching in PbPb collisions at nucleon-nucleon center-of-mass energy = 2.76 TeV, Phys. Rev. C **84** , 024906 (2011), arXiv:1102.1957 [nucl-ex]. 

- [3] B. Abelev _et al._ (ALICE), Measurement of charged jet suppression in Pb-Pb collisions at<sup>_~~√~~_</sup> _<u>sNN</u>_ = 2.76 TeV, JHEP **03** , 013, arXiv:1311.0633 [nucl-ex]. 

- [4] G. Aad _et al._ (ATLAS), Measurement of charged-particle spectra in Pb+Pb collisions at<sup>_~~√~~_</sup> _<u>s</u>_ NN = 2 _._ 76 TeV with the ATLAS detector at the LHC, JHEP **09** , 050, arXiv:1504.04337 [hep-ex]. 

- [5] S. Chatrchyan _et al._ (CMS), Study of high-pT charged particle suppression in PbPb compared to _pp_ collisions 

Such an effort will also allow the use of the full kernel at next-to-leading twist [30]. 

Beyond all the enhancements mentioned above will be the effort to obtain the scaling function _f_ ( _µ_<sup>2</sup> ) [Eq. (54)] for a jet traversing a quark-gluon plasma (QGP). One cannot directly use Eq. (49), as no TMDPDF has even been defined, let alone measured, in a QGP. However, one could use Eq. (49) in reverse: Having measured the _q_ ˆ and its scale dependence, one could surmise the form of a TMDPDF in the QGP. 

A surprising and side consequence of this effort, particularly that in Sec. III, is the realization that jets are rather wide objects. Looking at Fig. 6, specifically at the case with _pT >_ 0, one notes that at _t_ = 5 fm/c, jets have radii of several fm. For hard jets produced in relativistic heavy-ion collisions, this means that at least the softer portions of jets effect a much larger part of the QGP medium than previously imagined. We remind the reader that the simulations in Sec. III are vacuum simulations. Once repeated in the medium, these jets will only become wider. The softer part of the jets tend to dissipate in the medium leading to a wake of the jet [66]. Repeating these simulations, including the quantum uncertainty sizes will lead to even wider wakes of the jets. 

## **ACKNOWLEDGMENTS** 

This work was supported in part by the U.S. Department of Energy (DOE) under grant number DESC0013460. and in part by the National Science Foundation (NSF) under grant number ACI-1550300 within the framework of the JETSCAPE collaboration. C.S. is supported in part by the grant DE-FG02-05ER41367 from the U.S. Department of Energy, Office of Science, Nuclear Physics. 

   - at<sup>_~~√~~_</sup> _<u>sNN</u>_ = 2 _._ 76 TeV, Eur. Phys. J. C **72** , 1945 (2012), arXiv:1202.2554 [nucl-ex]. 

- [6] K. Aamodt _et al._ (ALICE), Suppression of Charged Particle Production at Large Transverse Momentum in Central Pb-Pb Collisions at<sup>_~~√~~_</sup> _<u>sNN</u>_ = 2.76 TeV, Phys. Lett. B **696** , 30 (2011), arXiv:1012.1004 [nucl-ex]. 

- [7] J. Adams _et al._ (STAR), Transverse momentum and collision energy dependence of high p(T) hadron suppression in Au+Au collisions at ultrarelativistic energies, Phys. Rev. Lett. **91** , 172302 (2003), arXiv:nucl-ex/0305015. 

- [8] K. Adcox _et al._ (PHENIX), Suppression of hadrons with large transverse momentum in central Au+Au collisions at<sup>_~~√~~_</sup> _<u>sNN</u>_ = 130-GeV, Phys. Rev. Lett. **88** , 022301 (2002), arXiv:nucl-ex/0109003. 

- [9] A. Majumder and M. Van Leeuwen, The Theory and Phenomenology of Perturbative QCD Based Jet Quenching, Prog. Part. Nucl. Phys. **66** , 41 (2011), arXiv:1002.2206 [hep-ph]. 

16 

- [10] S. Cao and X.-N. Wang, Jet quenching and medium response in high-energy heavy-ion collisions: a review, Rept. Prog. Phys. **84** , 024301 (2021), arXiv:2002.04028 [hep-ph]. 

- [11] X.-N. Wang and M. Gyulassy, Gluon shadowing and jet quenching in a + a collisions at s**(1/2) = 200-gev, Phys. Rev. Lett. **68** , 1480 (1992). 

- [12] M. Gyulassy and X.-N. Wang, Multiple collisions and induced gluon bremsstrahlung in qcd, Nucl. Phys. **B420** , 583 (1994), nucl-th/9306003. 

- [13] R. Baier, Y. L. Dokshitzer, S. Peigne, and D. Schiff, Induced gluon radiation in a QCD medium, Phys. Lett. **B345** , 277 (1995), arXiv:hep-ph/9411409. 

- [14] S. Cao and A. Majumder, Nuclear modification of leading hadrons and jets within a virtuality ordered parton shower, Phys. Rev. **C101** , 024903 (2020), arXiv:1712.10055 [nucl-th]. 

- [15] A. Majumder, Incorporating Space-Time Within Medium-Modified Jet Event Generators, Phys. Rev. **C88** , 014909 (2013), arXiv:1301.5323 [nucl-th]. 

- [16] K. Zapp, G. Ingelman, J. Rathsman, J. Stachel, and U. A. Wiedemann, A Monte Carlo Model for ’Jet Quenching’, Eur. Phys. J. **C60** , 617 (2009), arXiv:0804.3568 [hep-ph]. 

- [17] K. C. Zapp, F. Krauss, and U. A. Wiedemann, A perturbative framework for jet quenching, JHEP **1303** , 080, arXiv:1212.1599 [hep-ph]. 

- [18] Y. He, T. Luo, X.-N. Wang, and Y. Zhu, Linear Boltzmann Transport for Jet Propagation in the QuarkGluon Plasma: Elastic Processes and Medium Recoil, Phys. Rev. **C91** , 054908 (2015), [Erratum: Phys. Rev.C97,no.1,019902(2018)], arXiv:1503.03313 [nucl-th]. 

- [19] B. Schenke, C. Gale, and S. Jeon, MARTINI: An Event generator for relativistic heavy-ion collisions, Phys.Rev. **C80** , 054913 (2009), arXiv:0909.2037 [hep-ph]. 

- [20] J. Casalderrey-Solana, D. C. Gulhan, J. G. Milhano, D. Pablos, and K. Rajagopal, A Hybrid Strong/Weak Coupling Approach to Jet Quenching, JHEP **10** , 019, [Erratum: JHEP 09, 175 (2015)], arXiv:1405.3864 [hepph]. 

- [21] J. H. Putschke _et al._ , The JETSCAPE framework, (2019), arXiv:1903.07706 [nucl-th]. 

- [22] S. Cao, A. Majumder, R. Modarresi-Yazdi, I. Soudi, and Y. Tachibana, Jet Quenching: From Theory to Simulation, Int. J. Mod. Phys. E **33** , 2430002 (2024), arXiv:2401.10026 [hep-ph]. 

- [23] X.-F. Guo and X.-N. Wang, Multiple scattering, parton energy loss and modified fragmentation functions in deeply inelastic e A scattering, Phys. Rev. Lett. **85** , 3591 (2000), arXiv:hep-ph/0005044. 

- [24] X.-N. Wang and X.-F. Guo, Multiple parton scattering in nuclei: Parton energy loss, Nucl. Phys. **A696** , 788 (2001), arXiv:hep-ph/0102230. 

- [25] A. Majumder, The in-medium scale evolution in jet modification, (2009), arXiv:0901.4516 [nucl-th]. 

- [26] P. Arnold, G. D. Moore, and L. G. Yaffe, Photon and gluon emission in relativistic plasmas, JHEP **06** , 030, hep-ph/0204343. 

- [27] H. Liu, K. Rajagopal, and U. A. Wiedemann, An AdS/CFT Calculation of Screening in a Hot Wind, Phys. Rev. Lett. **98** , 182301 (2007), arXiv:hep-ph/0607062. 

- [28] A. Majumder, A comparative study of jet-quenching schemes, J. Phys. **G34** , S377 (2007), arXiv:nuclth/0702066. 

- [29] S. Cao _et al._ (JETSCAPE), Multistage Monte-Carlo simulation of jet modification in a static medium, Phys. Rev. **C96** , 024909 (2017), arXiv:1705.00050 [nucl-th]. 

- [30] C. Sirimanna, S. Cao, and A. Majumder, Final-state gluon emission in deep-inelastic scattering at nextto-leading twist, Phys. Rev. C **105** , 024908 (2022), arXiv:2108.05329 [hep-ph]. 

- [31] A. Majumder, Hard collinear gluon radiation and multiple scattering in a medium, Phys. Rev. **D85** , 014023 (2012). 

- [32] R. Baier, Y. L. Dokshitzer, A. H. Mueller, S. Peigne, and D. Schiff, Radiative energy loss of high energy quarks and gluons in a finite-volume quark-gluon plasma, Nucl. Phys. **B483** , 291 (1997), hep-ph/9607355. 

- [33] B. G. Zakharov, Fully quantum treatment of the landaupomeranchik-migdal effect in qed and qcd, Journal of Experimental and Theoretical Physics Letters **63** , 952–957 (1996). 

- [34] A. Majumder and J. Putschke, Mass depletion: a new parameter for quantitative jet modification, Phys. Rev. C **93** , 054909 (2016), arXiv:1408.3403 [nucl-th]. 

- [35] R. Baier, Jet quenching, Nucl. Phys. **A715** , 209 (2003), arXiv:hep-ph/0209038. 

- [36] A. Majumder, Calculating the jet quenching parameter _q_ ˆ in lattice gauge theory, Phys. Rev. **C87** , 034905 (2013). 

- [37] A. Kumar, A. Majumder, and J. H. Weber, Jet transport coefficient _q_ ˆ in (2+1)-flavor lattice QCD, (2020), arXiv:2010.14463 [hep-lat]. 

- [38] A. Kumar _et al._ (JETSCAPE), Inclusive jet and hadron suppression in a multistage approach, Phys. Rev. C **107** , 034911 (2023), arXiv:2204.01163 [hep-ph]. 

- [39] W. Fan _et al._ (JETSCAPE), Multiscale evolution of charmed particles in a nuclear medium, Phys. Rev. C **107** , 054901 (2023), arXiv:2208.00983 [nucl-th]. 

- [40] Y. Tachibana _et al._ (JETSCAPE), Hard jet substructure in a multistage approach, Phys. Rev. C **110** , 044907 (2024), arXiv:2301.02485 [hep-ph]. 

- [41] C. Sirimanna _et al._ (JETSCAPE), Hard Photon Triggered Jets in _p_ - _p_ and _A_ - _A_ Collisions, (2024), arXiv:2412.19738 [hep-ph]. 

- [42] P. Arnold and W. Xiao, High-energy jet quenching in weakly-coupled quark-gluon plasmas, Phys. Rev. **D78** , 125008 (2008), arXiv:0810.1026 [hep-ph]. 

- [43] A. Kumar, A. Majumder, and C. Shen, Energy and scale dependence of _q_ ˆ and the JET puzzle, Phys. Rev. **C101** , 034908 (2020), arXiv:1909.03178 [nucl-th]. 

- [44] R. Ehlers _et al._ (JETSCAPE), Bayesian Inference analysis of jet quenching using inclusive jet and hadron suppression measurements, (2024), arXiv:2408.08247 [hepph]. 

- [45] J. Casalderrey-Solana, Y. Mehtar-Tani, C. A. Salgado, and K. Tywoniuk, New picture of jet quenching dictated by color coherence, Phys. Lett. B **725** , 357 (2013), arXiv:1210.7765 [hep-ph]. 

- [46] Y. Mehtar-Tani, C. A. Salgado, and K. Tywoniuk, Jets in QCD Media: From Color Coherence to Decoherence, Phys. Lett. B **707** , 156 (2012), arXiv:1102.4317 [hep-ph]. 

- [47] N. Armesto, H. Ma, Y. Mehtar-Tani, C. A. Salgado, and K. Tywoniuk, Coherence effects and broadening in medium-induced QCD radiation off a massive _qq_ ¯ antenna, JHEP **01** , 109, arXiv:1110.4343 [hep-ph]. 

- [48] J. Casalderrey-Solana and E. Iancu, Interference effects in medium-induced gluon radiation, JHEP **08** , 015, arXiv:1105.1760 [hep-ph]. 

17 

- [49] S. Cao _et al._ (JETSCAPE), Multistage Monte-Carlo simulation of jet modification in a static medium, Phys. Rev. C **96** , 024909 (2017), arXiv:1705.00050 [nucl-th]. 

- [50] T. Sjostrand, S. Mrenna, and P. Z. Skands, A Brief Introduction to PYTHIA 8.1, Comput. Phys. Commun. **178** , 852 (2008), arXiv:0710.3820 [hep-ph]. 

- [51] G. Marchesini, B. Webber, G. Abbiendi, I. Knowles, M. Seymour, _et al._ , HERWIG: A Monte Carlo event generator for simulating hadron emission reactions with interfering gluons. Version 5.1 - April 1991, Comput.Phys.Commun. **67** , 465 (1992). 

- [52] T. Gleisberg, S. Hoeche, F. Krauss, M. Schonherr, S. Schumann, _et al._ , Event generation with SHERPA 1.1, JHEP **0902** , 007, arXiv:0811.4622 [hep-ph]. 

- [53] S. Cao, T. Luo, G.-Y. Qin, and X.-N. Wang, Linearized Boltzmann transport model for jet propagation in the quark-gluon plasma: Heavy quark evolution, Phys. Rev. C **94** , 014909 (2016), arXiv:1605.06447 [nucl-th]. 

- [54] M. Cacciari, G. P. Salam, and G. Soyez, The anti- _kt_ jet clustering algorithm, JHEP **04** , 063, arXiv:0802.1189 [hep-ph]. 

- [55] A. Kumar _et al._ (JETSCAPE), JETSCAPE framework: _p_ + _p_ results, Phys. Rev. **C102** , 054906 (2020), arXiv:1910.05481 [nucl-th]. 

- [56] D. Everett _et al._ (JETSCAPE), Phenomenological constraints on the transport properties of QCD matter with data-driven model averaging, Phys. Rev. Lett. **126** , 242301 (2021), arXiv:2010.03928 [hep-ph]. 

- [57] D. Everett _et al._ (JETSCAPE), Multisystem Bayesian constraints on the transport coefficients of QCD matter, Phys. Rev. C **103** , 054904 (2021), arXiv:2011.01430 [hepph]. 

- [58] A. Majumder and C. Shen, Suppression of the High _pT_ Charged Hadron _RAA_ at the LHC, Phys.Rev.Lett. **109** , 202301 (2012), arXiv:1103.0809 [hep-ph]. 

- [59] A. Majumder, E. Wang, and X.-N. Wang, Modified dihadron fragmentation functions in hot and nuclear matter, Phys. Rev. Lett. **99** , 152301 (2007), arXiv:nuclth/0412061. 

- [60] S. M. Aybat and T. C. Rogers, TMD Parton Distribution and Fragmentation Functions with QCD Evolution, Phys. Rev. D **83** , 114042 (2011), arXiv:1101.5057 [hepph]. 

- [61] P. Aurenche, B. Zakharov, and H. Zaraket, Failure of the collinear expansion in calculation of the induced gluon emission, JETP Lett. **87** , 605 (2008), arXiv:0804.4282 [hep-ph]. 

- [62] P. Aurenche, B. G. Zakharov, and H. Zaraket, Comment on “Success of collinear expansion in the calculation of induced gluon emission”, (2008), arXiv:0806.0160 [hepph]. 

- [63] F. Landry, R. Brock, P. M. Nadolsky, and C. P. Yuan, Tevatron Run-1 _Z_ boson data and Collins-Soper-Sterman resummation formalism, Phys. Rev. D **67** , 073016 (2003), arXiv:hep-ph/0212159. 

- [64] A. D. Martin, W. J. Stirling, R. S. Thorne, and G. Watt, Parton distributions for the LHC, Eur. Phys. J. C **63** , 189 (2009), arXiv:0901.0002 [hep-ph]. 

- [65] J. C. Collins and D. E. Soper, Parton distribution and decay functions, Nucl. Phys. **B194** , 445 (1982). 

- [66] Y. Tachibana, C. Shen, and A. Majumder, Bulk medium evolution has considerable effects on jet observables, Phys. Rev. C **106** , L021902 (2022), arXiv:2001.08321 [nucl-th]. 

