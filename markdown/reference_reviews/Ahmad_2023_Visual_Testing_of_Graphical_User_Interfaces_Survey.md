---
title: "Visual Testing of Graphical User Interfaces Survey"
author: "Ahmad"
year: "2023"
source_file: "Ahmad_2023_Visual_Testing_of_Graphical_User_Interfaces_Survey.pdf"
source_sha256: "e2aea84f27fa46855e9df2979a57df1b85b6374130c7d9ca30b1f59ddf057d53"
converted_at: "2026-11-06T15:44:05.394614+00:00"
markitdown_version: "0.1.9"
char_count: 75210
---
Draft version November 29, 2023
TypesetusingLATEXtwocolumnstyleinAASTeX631
Constraining Neutrino Cosmologies with Nonlinear Reconstruction
Shi-Hui Zang (臧诗慧) 1 and Hong-Ming Zhu (朱弘明) 1,2
1National Astronomy Observatories, Chinese Academy of Sciences, 20A Datun Road, Beijing 100101, China
2Canadian Institute for Theoretical Astrophysics, 60 St. George Street, Toronto, Ontario M5S 3H8, Canada
ABSTRACT
Nonlinear gravitational evolution induces strong nonlinearities in the observed cosmological density
fields, leading to positive off-diagonal correlations in the power spectrum covariance. This has caused
theinformationsaturationinthepowerspectrum, e.g., theneutrinomassconstraintsfromthenonlin-
earpowerspectraarelowerthantheirlinearcounterpartsbyafactorof∼2atz =0. Inthispaper,we
explore how nonlinear reconstruction methods improve the cosmological information from nonlinear
cosmic fields. By applying nonlinear reconstruction to cold dark matter fields from the Quijote simu-
lations, we find that nonlinear reconstruction can improve the constraints on cosmological parameters
significantly, nearly reaching the linear theory limit. For neutrino mass, the result is only 12% lower
than the linear power spectrum, i.e., the theoretical best result. This makes nonlinear reconstruction
an efficient and useful method to extract neutrino information from current and upcoming galaxy
surveys.
Keywords: Cosmology (343) — Large-scale structure of the universe (902)
1. INTRODUCTION stages of the Universe (Ferraro et al. 2022). However,
at low redshifts and on small scales, nonlinear evolu-
The large-scale structure of the Universe as traced
tion leads to the coupling of modes on different scales
by galaxy clustering provides one of the best windows
andtypicallycausessignificantcorrelationsinthesmall-
onfundamentalphysicsincludingneutrinomasses,dark
scale power spectrum (Meiksin & White 1999; Rimes &
energy, inflation and gravity. The ongoing and future
Hamilton 2005, 2006). These positive off-diagonal cor-
galaxyredshiftsurveyshavethepotentialofgreatlyim-
relations in the power spectrum covariance lead to the
proving our constraints on cosmology and fundamental
informationsaturationinthepowerspectrum(Rimes&
physics (e.g., DESI DESI Collaboration et al. 2016; Eu-
Hamilton 2005, 2006; Villaescusa-Navarro et al. 2020;
clid Amendola et al. 2018; Euclid Collaboration et al.
Bayer et al. 2021), i.e., the cosmological information
2020; SPHEREx Dor´e et al. 2014; Subaru Prime Focus
does not increase when increasing the wavenumber in
Spectrograph Takada et al. 2014; Vera Rubin Obser-
the nonlinear regime. For example, the constraints on
vatory/LSST LSST Science Collaboration et al. 2009;
neutrino mass from the nonlinear power spectra are
Roman Space Telescope/WFIRST Akeson et al. 2019;
lower than their linear counterparts by a factor of 2 at
MegaMapperSchlegeletal.2022). Tofullyexploitthese
redshift z =0 (Bayer et al. 2022).
powerful surveys, it is necessary to understand how to
Theconstraintsoncosmologicalparametersincluding
optimally extract information from the observed galaxy
neutrinomassscaleapproximatelylinearlywiththepri-
density fields.
mordialphysicsFigureofMerit(FoM),whichcountsthe
Cosmological constraints derived from galaxy power
total number of linear modes accessible to a galaxy red-
spectrum are connected to extracting information from
shiftsurvey(seeSaileretal.2021;Ferraroetal.2022,for
linear (or mildly nonlinear) modes, for which the cou-
morediscussions). Nonlinearstructureformationerases
pling with other modes can be assumed be to subdom-
thecorrelationwiththeinitialconditionsandleadstoa
inant and have evolved independently from the early
loss of information, which degrades the FoM of low red-
shift surveys significantly. Therefore, recovering more
hmzhu@nao.cas.cn linear modes from the observed nonlinear fields can im-
3202
voN
82
]OC.hp-ortsa[
1v93461.1132:viXra

2
provetheFoMandcosmologicalconstraintsgreatlyand 2. METHOD
thus maximize the scientific return of future surveys.
Neutrinos with finite mass suppress the small-scale
Reconstruction has been an efficient technique to re-
powerspectrumbelowtheneutrinofree-streamingscale
store the baryonic acoustic oscillation (BAO) feature in
(Bondetal.1980;Lesgourgues&Pastor2006). Thesup-
the linear power spectrum (Eisenstein et al. 2007) and
pression is proportional to the sum of neutrino masses,
has been widely used to analyse the galaxy survey data
thus allowing us to measure or constrain the total neu-
(e.g.,SDSSPadmanabhanetal.2012,BOSSAlametal.
trino mass M . Detecting the minimum neutrino mass
ν
2017;eBOSSAlametal.2021). Instandardreconstruc-
fromtheeffectsofneutrinosonthetotalmatterδ and
m
tion, the linear displacement field estimated from the
cold dark matter (CDM)+baryon perturbations δ is
cb
observednonlineardensityundertheZel’dovichapprox-
one of the key science goals of the near-term and future
imation is used to move galaxies, which reverses the
galaxy surveys.
large-scale bulk flows and partially restores the linear
Forgalaxyclusteringinthepresenceofmassiveneutri-
BAO signal (Eisenstein et al. 2007). Recently nonlinear
nos,thenow-standardapproximationthatgalaxiestrace
reconstruction algorithms have been developed to fur-
the CDM+baryon density field δ has been shown to
cb
ther improve upon the standard reconstruction by solv-
be an excellent approximation well into the quasi-linear
ingthefullnonlineardisplacementfield(Zhuetal.2017;
regime(Castorinaetal.2015). Thegalaxyoverdensityis
Schmittfulletal.2017;Shietal.2018). Thereconstruc-
givenbyδ =F[δ ]andatlinearorderδ =bδ ,where
g cb g cb
tionmethodsworksextraordinarilywellforreducingthe
b is the linear galaxy bias. Recently, Bayer et al. (2022)
uncertainty on the BAO scale. Slightly more generally,
demonstrated that all the information of neutrinos in
thereconstructioncanrestoreinformationaboutthelin-
the CDM field is in the linear power spectrum set by
ear modes that were corrupted by nonlinear structure theinitialconditionsfork ≲1hMpc−1 usingthephase-
formationandahigherprimordialFoMcanbeobtained.
matched N-body simulations. Thus, galaxy clustering,
Ithasbeenshownthatnonlinearreconstructionreduces
which is based on the δ field will have negligible con-
cb
the off-diagonal components of power spectrum covari-
straining power on neutrino masses beyond that which
ance prominently and increase the information content
exists in the linear density field over the same range of
ofpowerspectrumamplitudesubstantially(seee.g.,Pan
scales(Bayeretal.2022). Theyhavefoundsimilarcon-
etal.2017). Recently, Wangetal.(2022)haveexplored
clusions for other parameters such as the total matter
the improvement of cosmological constraints using the
density Ω and primordial power spectrum amplitude
m
standard reconstruction algorithm, while Fl¨oss & Meer-
A . Whilethelate-timelinearpowerspectrumisnotan
s
burg (2023) have studied improving constraints using
observable, it provides a bound on the error of neutrino
neural network based reconstruction, in particular pri-
masses available from galaxy clustering. However, the
mordial non-Gaussianity.
nonlinear power spectrum does not reach this bound,
Inthispaper,weexplorehownonlinearreconstruction
because of the positive off-diagonal components in its
improves the constraints on cosmological parameters,
covariancewhichdegradestheconstraintssubstantially.
with a focus on neutrino mass. This improves upon the
Theresultingconstrainingpowerofthenonlinearpower
previous study (Pan et al. 2017), which only considered
spectrum for δ is a factor of 2 lower than the linear
cb
one parameter, the power spectrum amplitude. We use
one (Bayer et al. 2022).
theQuijotesimulations(Villaescusa-Navarroetal.2020)
Therefore, there is still room for improving neutrino
tocomputethepre-andpost-reconstructionpowerspec-
mass constraints from galaxy clustering and potentially
trum covariance and perform a detailed Fisher analysis.
afactorof2betterconstraintscanbeachieved. Thegoal
We find that nonlinear reconstruction can efficiently re-
of this paper is to investigate whether nonlinear recon-
ducethemode-couplingeffectsinthenonlinearfieldand
structioncanrecovertheinformationfromthenonlinear
improve the cosmological constraints significantly, al-
δ field to the linear theory limit.
cb
mostreachingthelineartheorylimit,whichisanimpor-
In this section, we review the reconstruction algo-
tant step towards optimal extraction of neutrino mass
rithms including standard and nonlinear reconstruction
information on small scales and has profound implica-
and describe the Fisher analysis of cosmological infor-
tions for future galaxy redshift surveys.
mation.
Thispaperisorganizedasfollows. InSection2,wede-
scribe the reconstruction algorithms and Fisher matrix.
2.1. Reconstruction
In Section 3, we present the numerical implementation
Reconstructionisanefficientwaytoreducenonlinear-
oftheFisheranalysis. InSection4,weshowthenumer-
itiesinducedbythelarge-scalebulkflows. Thestandard
ical results. We discuss and conclude in Section 5.
reconstructionhasbeenfirstproposedtoreconstructthe

3
linear BAO signal (Eisenstein et al. 2007). The algo- 4. Move the object by the displacement s and
rithm devised by Eisenstein et al. (2007) consists of the update the object’s position.
following steps:
• Compute the total displacement of each object
• SmooththenonlineardensityfieldwithaGaussian
χ(qˆ ) = qˆ −x , where x is the start-
end end start start
kernel W (k) of scale R, to filter out small-scale
R ingpositionbeforethefirstiterationstepandqˆ
end
modes.
is the end position of each object after iteration
• Compute the shift s from the smoothed density (x start is the Eulerian position of each object and
qˆ is the estimated Lagrangian position).
field using the Zel’dovich approximation, end
ik • Paint the estimated displacement χ(qˆ ) defined
s(k)=− W (k)δ(k). (1) end
k2 R on the estimated Lagrangian position qˆ
end
to a
regular grid and truncate the small-scale modes
• Movethegalaxiesbystocomputethe“displaced”
beyond k .
Ny
density field, δ (x).
d
• The reconstructed density field from nonlinear re-
• Shift an spatially uniform distribution of particles
construction is
by s to form the shifted density field, δ (x).
s
• The reconstructed density field is defined as δ nr (q)=∇ q ·χ(q). (4)
δ (x)≡δ (x)−δ (x).
r d s
An improved estimation of the small-scale displace-
The Zel’dovich approximation only captures the lin-
mentallowsustorecovermoresmall-scalelinearmodes.
ear displacement on large scales, limiting the efficacy
The cross-correlation coefficient of the reconstructed
of standard reconstruction to relatively large scales,
field with the linear initial conditions is higher than 0.5
k ∼0.2hMpc−1. Recentnewreconstructionalgorithms
for k ≲ 1 hMpc−1 (Zhu et al. 2017; Schmittfull et al.
havebeenpresentedtosolvethenonlineardisplacement
2017; Shi et al. 2018). Note that such an improvement
field (Zhu et al. 2017; Schmittfull et al. 2017; Shi et al.
can also be achieved by combining the standard recon-
2018), which improve upon the linear standard recon-
structionandconvolutionalneuralnetworks(seeShallue
struction with a substantially improved small-scale per-
& Eisenstein 2022; Fl¨oss & Meerburg 2023).
formance. While these methods are different in the de-
tailed numerical implementations, the underlying phys-
2.2. Fisher analysis
ical principles are the same, i.e., solving the full dis-
placement from the mass conservation relation. In the Toquantifythecosmologicalinformationinthepower
following analysis, we use the algorithm of Schmittfull spectrum of pre- and post-reconstruction fields, we use
et al. (2017), solving the displacement field iteratively theFisherinformationmatrix(Fisher1925). TheFisher
using the fast Fourier transform, which is efficient and matrix is defined as
easy to apply. The reconstruction algorithm devised by
Schmittfull et al. (2017) consists of the following steps: F αβ = (cid:88) ∂ ∂ θ P iC i − j 1 ∂ ∂ P θ j, (5)
α β
i,j
• Iteratively displace objects as follows:
where P = P(k ) is the power spectrum of the ith bin
i i
1. From the catalog, compute the density field
andC isthepowerspectrumcovariancematrix,andθ
ij a
on the grid.
representsthecosmologicalparameters(Tegmark1997).
2. Smooth the density field with the Gaussian We have neglected the dependence of covariance on the
window W R (k), with smoothing scale cosmological parameters to avoid underestimating the
errors (Carron 2013).
R=max(ϵn−1R ,R ), (2)
R init min The inverse of the Fisher matrix gives the covariance
matrixoftheparametersandtheexpectederrorsonthe
in the nth iteration step and truncate small-
parameters are equal to the square root of the diagonal
scale modes by setting δ(k) = 0 if k > k ,
Ny
elements of F−1,
where k is the Nyquist frequency.
Ny
3. Compute the negative Zel’dovich displace- σ(θ )= (cid:112) (F−1) , (6)
α αα
ment
ik
s(k)=− W (k)δ(k). (3) which represents the minimum error achievable.
k2 R

4
3. SIMULATIONS ing the linear power spectrum at z = 0 from the linear
Boltzmann code CAMB (Lewis et al. 2000).
To compute the covariance matrix of the power spec-
Since the covariance matrix is estimated from simu-
trum and the response of power spectrum with re-
lations, it is itself a random variable with errors. The
spect to the cosmological parameters, we use the Qui-
matrix inversions lead to biased constraints on the pa-
jote simulations (Villaescusa-Navarro et al. 2020), run
rameters. To account for this, we apply a correction to
with the TreePM code Gadget-III, an improved ver-
thecovariancematrix(Percivaletal.2022;Paillasetal.
sion of Gadget-II (Springel 2005). Each simulation
evolves5123CDMparticles(plus5123neutrinoparticles 2022)
n −1
for nonzero neutrino mass) in a cosmological volume of C = sim Cˆ, (9)
n −n +n −1
1(h−1Gpc)3. TheQuijotesimulationshavebeenwidely sim bins θ
wheren isthenumberofsimulationstocalculatethe
used to quantify the information content of nonlinear sim
covariance matrix, n is the number of parameters in
statistics (e.g., Villaescusa-Navarro et al. 2020; Hahn θ
Fisher analysis, n is the number of power spectrum
et al. 2020; Massara et al. 2021; Bayer et al. 2021; Pail- bins
bins. In our case, we have 5,000, n = 6, and n
las et al. 2022). More details of the Quijote simulations θ bins
dependsonthemaximumwavenumberk includedin
can be found in Villaescusa-Navarro et al. (2020). max
theanalysis. Wehavecheckedthatthiscorrectionfactor
We consider six cosmological parameters, Ω , Ω , h,
m b
is less than 1% for k <0.5 hMpc−1.
n , σ , and M . We use 5,000 simulations of the fidu- max
s 8 ν
cial cosmology to compute the covariance matrix. We
3.2. Derivatives
use 1,000 simulations to compute the derivatives with
respect to each parameter. The detailed information of FortheparametersΩ m ,Ω b ,h,n s andσ 8 ,weuseacen-
simulations we used in the analysis is shown in Table 1. tral difference scheme to compute the derivatives,
Wehaveperformedadetailedconvergencetestandver-
∂P(k) P(k)| −P(k)|
ified that our results are converged, i.e., the constraints ≃ θi+δθi θi−δθi, (10)
∂θ 2δθ
i i
do not change much if the power spectrum covariance
and derivatives are evaluated with less simulations (See whereP(k)isthemeasuredpowerspectrumfromsimu-
Appendix A for more details). lations and only the considered parameter is varied and
WeusethesnapshotofCDMparticlesfromthesimu- other parameters are fixed. We have used 500 pairs of
lationoutputatredshiftz =0. Hereweassumebaryons simulations to calculate each derivative using Eq. (10).
trace CDM. We compute the nonlinear δ field on a For neutrino mass M , the second term in the nu-
cb ν
5123 grid using the cloud-in-cell interpolation scheme. merator of Eq. (10) corresponds to a cosmology with
Forstandardreconstruction,weuseaGaussiansmooth- negative neutrino mass, since the fiducial value of the
ing of scale R = 10 h−1Mpc, W (k) = e−(kR)2/2 fol- neutrino mass is at the boundary of the allowed region,
R
lowing Eisenstein et al. (2007). For nonlinear recon- i.e., M = 0. Therefore, we use a first-order forward
ν
struction, we use R = 10 h−1Mpc, ϵ = 0.5, and difference scheme to compute the derivative,
init R
R = 1 h−1Mpc. We use eight iteration steps in the
min ∂P(k) 1 (cid:104) (cid:105)
reconstruction (Schmittfull et al. 2017). ≃ P(k)| −P(k)| , (11)
∂M δM Mν+δMν Mν
ν ν
3.1. Covariance matrix
where the fiducial neutrino mass M =0. We use 1,000
ν
We estimate the covariance matrix using 5,000 simu- simulations to compute the derivative with respect to
lations of the fiducial cosmology as the neutrino mass.
Cˆ ij =⟨(P i −⟨P i ⟩)(P j −⟨P j ⟩)⟩, (7) 4. RESULTS
where⟨·⟩denotestheensembleaverageoversimulations. In this section, we present the reconstruction results,
The covariance matrix for fields δ , δ and δ are esti- including the cross-correlation coefficient, power spec-
cb r nr
mated numerically using the Quijote simulations. trum covariance matrix, and cosmological parameter
Forthelineardensityfield(aGaussianrandomfield), constraints.
the power spectrum covariance matrix is diagonal,
4.1. Cross-correlation coefficient
2[P(k )]2
C = i δ , (8) To quantify the reconstruction performance, we use
ij N ij
ki the cross-correlation coefficient,
where N is the number of Fourier modes in the cor-
ki P (k)
responding k bin. This can be directly computed us- r (k)= δAδB , (12)
i δAδB (cid:112)
P (k)P (k)
δAδA δBδB

5
|     |     | Name     | Ω      | Ω     | h      | n      | σ     | M   | [eV] | ICs  | Realizations |       |     |     |     |
| --- | --- | -------- | ------ | ----- | ------ | ------ | ----- | --- | ---- | ---- | ------------ | ----- | --- | --- | --- |
|     |     |          | m      |       | b      | s      | 8     | ν   |      |      |              |       |     |     |     |
|     |     | Fiducial | 0.3175 | 0.049 | 0.6711 | 0.9624 | 0.834 | 0.0 |      | 2LPT |              | 5,000 |     |     |     |
Fiducial ZA 0.3175 0.049 0.6711 0.9624 0.834 0.0 Zel’dovich 500
|     |     | Ω+  | 0.3275 | 0.049 | 0.6711 | 0.9624 | 0.834 | 0.0 |     | 2LPT |     | 500 |     |     |     |
| --- | --- | --- | ------ | ----- | ------ | ------ | ----- | --- | --- | ---- | --- | --- | --- | --- | --- |
m
|     |     | Ω−  | 0.3075 | 0.049 | 0.6711 | 0.9624 | 0.834 | 0.0 |     | 2LPT |     | 500 |     |     |     |
| --- | --- | --- | ------ | ----- | ------ | ------ | ----- | --- | --- | ---- | --- | --- | --- | --- | --- |
m
|     |     | Ω++ | 0.3175 | 0.051 | 0.6711 | 0.9624 | 0.834 | 0.0 |     | 2LPT |     | 500 |     |     |     |
| --- | --- | --- | ------ | ----- | ------ | ------ | ----- | --- | --- | ---- | --- | --- | --- | --- | --- |
b
Ω−−
|     |     |     | 0.3175 | 0.047 | 0.6711 | 0.9624 | 0.834 | 0.0 |     | 2LPT |     | 500 |     |     |     |
| --- | --- | --- | ------ | ----- | ------ | ------ | ----- | --- | --- | ---- | --- | --- | --- | --- | --- |
b
|     |     | h+  | 0.3175 | 0.049 | 0.6911 | 0.9624 | 0.834 | 0.0 |     | 2LPT |     | 500 |     |     |     |
| --- | --- | --- | ------ | ----- | ------ | ------ | ----- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     | h−  | 0.3175 | 0.049 | 0.6511 | 0.9624 | 0.834 | 0.0 |     | 2LPT |     | 500 |     |     |     |
|     |     | n+  | 0.3175 | 0.049 | 0.6711 | 0.9824 | 0.834 | 0.0 |     | 2LPT |     | 500 |     |     |     |
s
|     |     | n−  | 0.3175 | 0.049 | 0.6711 | 0.9424 | 0.834 | 0.0 |     | 2LPT |     | 500 |     |     |     |
| --- | --- | --- | ------ | ----- | ------ | ------ | ----- | --- | --- | ---- | --- | --- | --- | --- | --- |
s
σ+
|     |     | 8   | 0.3175 | 0.049 | 0.6711 | 0.9624 | 0.849 | 0.0 |     | 2LPT |     | 500 |     |     |     |
| --- | --- | --- | ------ | ----- | ------ | ------ | ----- | --- | --- | ---- | --- | --- | --- | --- | --- |
|     |     | σ−  | 0.3175 | 0.049 | 0.6711 | 0.9624 | 0.819 | 0.0 |     | 2LPT |     | 500 |     |     |     |
8
M+
|     |     |     | 0.3175 | 0.049 | 0.6711 | 0.9624 | 0.834 | 0.1 |     | Zel’dovich |     | 500 |     |     |     |
| --- | --- | --- | ------ | ----- | ------ | ------ | ----- | --- | --- | ---------- | --- | --- | --- | --- | --- |
ν
Table 1. The details of the Quijote simulations used in this work. The fiducial cosmology contains 5,000 simulations, which
areusedtoestimatethepowerspectrumcovariancematrix. Othersimulationswithdifferentcosmologicalparametersareused
to compute the partial derivatives of the power spectrum to cosmological parameters, where only the considered parameter
is varied and other parameters are fixed. The initial conditions are generated at z = 127 using the second-order Lagrangian
perturbation theory, except for the neutrino simulations where the Zel’dovich approximation is used.
whereP (k)andP (k)arethepowerspectrumof pecially at small scales. While being competitive with
| δAδA |     | δBδB |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
≲0.2hMpc−1,
fields δ (k) and δ (k), and P (k) is the cross-power nonlinearreconstructionatlargescalesk
| A   |     | B   | δAδB |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
spectrum between the two fields. thestandardreconstructionhasalowercorrelationwith
|     |     |     |     |     |     |     |     |     |     |     |     |     | ≳   | hMpc−1, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- |
In Figure 1, we plot the cross-correlation coefficient the linear field δ at smaller scales k 0.2
L
|     |     |     |     |     |     |     | which        | needs | to be    | improved |               | by solving | the    | small-scale |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | -------- | -------- | ------------- | ---------- | ------ | ----------- | --- |
|     |     |     |     |     |     |     | displacement |       | or using | the      | convolutional |            | neural | network     |     |
1.0
|     |     |     |     |     |     |     | (e.g. | Zhu et  | al. 2017; | Schmittfull |        | et            | al. 2017; | Shi | et al. |
| --- | --- | --- | --- | --- | --- | --- | ----- | ------- | --------- | ----------- | ------ | ------------- | --------- | --- | ------ |
|     |     |     |     |     |     |     | 2018; | Shallue | &         | Eisenstein  | 2022). | Nevertheless, |           |     | we ex- |
0.8
pectthatbothreconstructionmethodscanrecovermore
|     |     |     |     |     |     |     | small-scale |      | linear | modes,    | i.e., | a much  | higher | primordial   |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------ | --------- | ----- | ------- | ------ | ------------ | --- |
| 0.6 |     |     |     |     |     |     | physics     | FoM, | and    | therefore |       | improve | the    | cosmological |     |
)k(r
constraints.
|     |     |     |     |     |     |     | Note | that | reconstruction |     | algorithms |     | based | on  | solving |
| --- | --- | --- | --- | --- | --- | --- | ---- | ---- | -------------- | --- | ---------- | --- | ----- | --- | ------- |
0.4
|     | cb  |     |     |     |     |     | the   | full nonlinear |             | displacement |             | have | a similar |     | perfor- |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------------- | ----------- | ------------ | ----------- | ---- | --------- | --- | ------- |
|     |     |     |     |     |     |     | mance | with           | correlation |              | coefficient |      | r(k) ≳    | 0.5 | at k ≲  |
| 0.2 | r   |     |     |     |     |     |       |                |             |              |             |      |           |     |         |
hMpc−1
|     |     |     |     |     |     |     | 1   |     | (Zhu | et al. 2017; |     | Schmittfull | et  | al. 2017; | Shi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | --- | ----------- | --- | --------- | --- |
nr
|     |     |     |     |     |     |     | et al. | 2018). | To reduce |     | the computational |     |     | cost, we | have |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --------- | --- | ----------------- | --- | --- | -------- | ---- |
0.0
10−2 10−1 100 used the iterative algorithm of Schmittfull et al. (2017).
|                                   |                       |     | k [hMpc     | 1]                     |          |        |        |      |            |               |     |       |          |     |         |
| --------------------------------- | --------------------- | --- | ----------- | ---------------------- | -------- | ------ | ------ | ---- | ---------- | ------------- | --- | ----- | -------- | --- | ------- |
|                                   |                       |     |             |                        |          |        |        | 4.2. | Full shape | reconstructed |     | power | spectrum |     |         |
| Figure 1.                         | The cross-correlation |     | coefficient |                        | with the | linear |        |      |            |               |     |       |          |     |         |
|                                   |                       |     |             |                        |          |        | Figure | 2    | shows      | the measured  |     | power | spectra  |     | divided |
| initialconditionsforthenonlinearδ |                       |     |             | field,thereconstructed |          |        |        |      |            |               |     |       |          |     |         |
cb
fields using standard reconstruction δ and nonlinear recon- by the linear initial power spectrum linearly scaled to
r
|               |                                            |     |     |     |     |     | the | redshift | z = | 0 of | the | simulation. |     | The | original |
| ------------- | ------------------------------------------ | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | --- | ----------- | --- | --- | -------- |
| structionδ nr | . Whilebothreconstructionalgorithmsimprove |     |     |     |     |     |     |          |     |      |     |             |     |     |          |
thecorrelationwiththelinearinitialconditionssubstantially, nonlinear power and linear power agree within 5% at
the nonlinear method has a better performance on smaller k < 0.15 hMpc−1, and the reconstructed power spec-
| scales, k≳0.2 | hMpc−1. |     |     |     |     |     |      |        |         |            |     |                |     |        |          |
| ------------- | ------- | --- | --- | --- | --- | --- | ---- | ------ | ------- | ---------- | --- | -------------- | --- | ------ | -------- |
|               |         |     |     |     |     |     | trum | agrees | with    | the linear |     | power spectrum |     | within | 5%       |
|               |         |     |     |     |     |     | at k | < 0.16 | hMpc−1. | Nonlinear  |     | reconstruction |     |        | slightly |
with the linear initial conditions δ for the nonlinear extends the k range where the linear theory is valid. As
L
δ field, the reconstructed fields using standard recon- we have noticed in Fig. 1, the cross-correlation coeffi-
cb
struction δ and nonlinear reconstruction δ . We note cientr becomessmallerthanunityonsmallerscales,we
| r   |     |     |     |     | nr  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thatthebothreconstructionalgorithmsimprovethecor- would have to add corrections to the linear power spec-
relation with the linear density field substantially, es- trumtomodelthepowerspectrumafterreconstruction.

6
1.4
1.2
1.0
0.8
0.6
0.4
0.2
0.0
10−2 10−1 100
k [hMpc 1]
P/P
L
of variations due to the cosmic variance. The max-
imum wavenumber included in the fitting is k =
max
0.8 hMpc−1. We use equal weights for all k bins to
avoid over-fitting small scales. The best-fit parameters
are Σ = 1.67 h−1Mpc and P = 38 [(h−1Mpc)3]. The
N
best-fit theoretical model agrees with the reconstructed
powerspectrumwithin1%atk ≲0.24hMpc−1 and3%
L at k ≲0.5 hMpc−1, which makes it possible to perform
cosmologicalparameterinferenceatthepercentlevelus- cb
ing the reconstructed power spectrum. However, when
nr
applying to galaxy surveys, more complexities have to
Model
be considered such as galaxy biasing and redshift space
distortions, which will be explored in the future.
Onsmallerscales,k ≳0.5hMpc−1,themodelpredicts
a higher noise level than the data. This is partly due
Figure 2. Power spectra from the simulations at z = 0, to that the simple white noise term misses the scale-
divided by the linear initial power spectrum linearly scaled dependence of the residual nonlinearities. Additional
toz=0. Thereconstructedpowerspectrumagreeswiththe
improvements on small scales may be possible by using
linearpowerspectrumwithin5%atk<0.16hMpc−1,while
the effective field theory of large-scale structure. On
the original nonlinear power and linear power agree within
5%atk<0.15hMpc−1. Comparedtothenonlineardensity small scales we would have to add more counterterms
withoutreconstruction,nonlinearreconstructionslightlyim- to this simple model to match the reconstructed power
provestheagreementwiththelinearlinearpowerspectrum. spectrum (e.g., Schmittfull et al. 2017). We leave this
However, the best-fit theoretical model agrees with the re- for future work.
constructedpowerspectrumwithin1%atk≲0.24hMpc−1
In the following analysis, we use the reconstructed
and 3% at k≲0.5 hMpc−1.
powerspectruminthesimulationtocomputetheFisher
information.
The fact that nonlinear reconstruction misses small-
scalebroadbandpowerrelativetothelinearpowerisnot
4.3. Covariance matrix
necessarilyaproblem. Allthatisneededtoestimatecos-
mological parameters is a theoretical model describing We apply two reconstruction algorithms to the 5,000
the reconstructed power spectrum as a function of cos- simulations of fiducial cosmology and compute the co-
mological parameters. Following the literature on mod- variance matrix of the power spectrum.
eling the reconstructed power spectrum (see e.g. Noh In Figure 3, we plot the correlation matrix, i.e., the
(cid:112)
et al. 2009; Padmanabhan et al. 2009; White 2015), we normalized covariance matrix, defined as C ij / C ii C jj ,
useasimpletheoreticalmodeltofitthepowerspectrum whereC ij isthecovariancematrix. Forthenonlinearδ cb
after reconstruction, field, the correlation matrix is almost diagonal on large
scales, k ≲ 0.1 hMpc−1, and exhibits significant off-
P theory (k)=C2(k)P δL (k)+P N , (13) diagonalcorrelationsonsmallerscales,k ≳0.1hMpc−1,
which leads to the information saturation of the non-
where the propagator C(k) = e−k2Σ2/2 describes the
linear power spectrum (e.g., Rimes & Hamilton 2005,
damping of the linear power spectrum, P is the linear
δL 2006;Villaescusa-Navarroetal.2020;Bayeretal.2021).
initial power spectrum linearly scaled to redshift z =0,
Thestandardreconstructionreducestheoff-diagonalel-
and the noise power spectrum P quantifies the nonlin-
N ements and the covariance matrix is nearly diagonal at
earitiesafterreconstruction. Wethenfitthetwoparam- k ≲0.2hMpc−1,inagreementwiththecross-correlation
eters Σ and P by minimizing the sum of squares
N coefficientobservedinFigure1. However,thecovariance
S =
(cid:88)(cid:16)
Pˆ δnr (k i )−P theory (k i )
(cid:17)2
, (14)
m
th
a
e
tr
n
i
o
x
n
o
li
f
n
n
ea
o
r
nl
r
i
e
n
g
e
i
a
m
r
e
r
,
ec
k
on
≲
st
0
r
.
u
8
ct
h
i
M
on
p
i
c
s
−
d
1
i
,
a
w
go
h
n
e
a
re
l w
th
e
e
ll
c
in
ou
to
-
i pling with other modes are subdominant. This nearly
where the hat denotes the reconstructed power spec- diagonal covariance matrix for the δ field indicates
nr
trum estimated from simulations and k denotes the more linear information available than the power spec-
i
power spectrum in the ith bin. Here, we directly use tra of the δ and δ fields.
cb r
the measured linear initial power spectrum Pˆ when With enough simulations, we have not observed large
δL
computing the theoretical model, to reduce the impact negative off-diagonal elements before and after recon-

7
1.0
0.8
0.6
0.4
0.2
0.0 0.2 0.4 0.6 0.8 1.0
k
1
[hMpc 1]
]1
cpMh[
2 k
cb
1.0
0.8
0.6
0.4
0.2
0.0 0.2 0.4 0.6 0.8 1.0
k
1
[hMpc 1]
]1
cpMh[
2 k
r
1.0
0.8
0.6
0.4
0.2
0.0 0.2 0.4 0.6 0.8 1.0
k
1
[hMpc 1]
]1
cpMh[
2 k
nr
1.0
0.8
0.6
0.4
0.2
0.0
−0.2
))jk(P,)ik(P(rroC
Figure 3. Correlation matrix for the power spectrum of the nonlinear δ field, and the reconstruction fields δ and δ
cb r nr
usingstandardandnonlinearreconstructionmethods,respectively. Thecovariancematrixisestimatedusing5,000simulations.
Reconstructionreducestheoff-diagonalcorrelationsubstantially. Thedensitymodesarenearlyindependentatk≲0.8hMpc−1
for the nonlinear reconstruction method.
struction. There only exists a few negative off-diagonal nonlinearities, which is not captured by the Zel’dovich
elementswithverysmallabsolutevalues∼10−2,mainly approximation.
due to the random statistical fluctuations. Therefore, We notice that the constraints on neutrino mass M
ν
our results should be more robust than the previous with reconstruction are almost the same as the linear
work which uses less realizations to estimate the co- field at k ≲0.25 hMpc−1 and the constraint still nearly
variance matrix (Pan et al. 2017). We have confirmed reaches the linear theory limit at k ≳ 0.25 hMpc−1 for
thatourresultshaveconverged,i.e.,theparametercon- the nonlinear reconstruction method. This result is re-
straintsdonotchangemuchiflesssimulationsareused. markable,sincetheδ fieldandderivedquantities,e.g.,
cb
See Appendix A for more details of the convergence the halo field, contain little information about neutrino
tests. mass beyond that which exists in the linear power spec-
trum for k ≲ 1 hMpc−1, demonstrated by using phase-
matched simulations (Bayer et al. 2022). Therefore, the
4.4. Cosmological constraints linear power spectrum provides a bound on the error
that can be obtained using δ and it is exciting to see
In Figure 4, we show the marginalized 1σ constraints cb
that nonlinear reconstruction can recover nearly all the
oncosmologicalparameters,Ω ,Ω ,h,n ,σ ,andM ,
m b s 8 ν
informationregardingneutrinomassfromthenonlinear
as a function of k . On large scales where the cosmic
max
δ field.
densityfieldevolvedlinearlyfromtheinitialconditions, cb
TheM −σ degeneracyhaslimitedtheneutrinomass
all fields, δ , δ , δ , and δ , have a similar constraint ν 8
L cb r nr
on the parameters at k ≲0.1 hMpc−1. The constraints constraint on small scales (Villaescusa-Navarro et al.
2020;Bayeretal.2021),whichcouldnotbereducedus-
from the nonlinear δ start to saturate at k =
cb max
0.2 hMpc−1, especially for σ and M , for which the ingpowerspectrumalone(SeeFigure8ofAppendixB).
8 ν
Combining other nonlinear statistics such as halo mass
dominant information comes from the power spectrum
function and void size function can tighten the con-
amplitude. Forstandardreconstruction,theconstraints
straint on neutrino mass by breaking the degeneracy
are much better than the nonlinear δ field. The infor-
cb
mationfromδ continuetoincreasefork ≳0.2hMpc−1 between different parameters (e.g. Bayer et al. 2021),
r
andsaturatesatk ∼0.3hMpc−1. Thisisduetothe which will be subject of further inquiry.
max
In Table 2, we list the marginalized 1σ errors for
limitedvalidityoftheZel’dovichapproximationadopted
k =0.5hMpc−1. Wefindthatnonlinearreconstruc-
inthestandardreconstruction. However, the constrain- max
tion can achieve a significant level of improvement on
ing power of the δ field is even better than δ and the
nr r
all6parametersandtheimprovementstobeafactorof
constraintsobtainedusingnonlinearreconstructioncon-
tinuetoimproveuntilk =0.5hMpc−1,nearlyreach- 2.72,2.65,2.64,2.65,2.49,2.54forΩ m ,Ω b ,h,n s ,σ 8 and
max
M , respectively. Thus, the constraining power of the
ing the linear theory constraints. The improvement at ν
k ≳ 0.3 hMpc−1 upon the standard reconstruction is reconstructed power spectrum P δnr , i.e., the signal to
noiseratioofneutrinomassmeasurement∝1/σ(M ),is
mainly because a better estimation of small-scale dis- ν
placement using nonlinear methods removes more shift

8
100
10−1
10−2
0.1 0.2 0.3 0.4 0.5
)m
(
100
10−1
10−2
0.1 0.2 0.3 0.4 0.5
)b
(
101
100
10−1
0.1 0.2 0.3 0.4 0.5
)h(
101
10−1
0.1 0.2 0.3 0.4 0.5
k [hMpc 1]
)sn(
100
10−1
0.1 0.2 0.3 0.4 0.5
k [hMpc 1]
)8
(
102
101
100
0.1 0.2 0.3 0.4 0.5
k [hMpc 1]
]Ve[)vM(
L r
cb nr
Figure 4. The marginalized 1σ error for each cosmological parameters as a function of k . The parameter constraints from
max
the nonlinear δ start to saturate at k =0.2 hMpc−1. The information from standard reconstruction continues to increase
cb max
until k ∼0.3 hMpc−1, limited by the linear assumption when estimating the displacement field. The constraining power of
max
the δ field is much better than δ and δ and continues to improve until k ∼0.5 hMpc−1.
nr cb r max
Marginalized Fisher Constraints
Probes Ω Ω h n σ M [eV]
m b s 8 ν
δ 0.063 0.018 0.19 0.13 0.010 1.7
cb
δ 0.035 0.0097 0.11 0.072 0.059 0.99
r
δ 0.023 0.0066 0.073 0.049 0.040 0.67
nr
δ 0.017 0.0055 0.054 0.027 0.034 0.59
L
Improvement 2.72 2.65 2.64 2.65 2.49 2.54
Table 2. Marginalized1σ errorsofcosmologicalparametersfork =0.5hMpc−1.Welisttheconstraintsobtainedfromthe
max
power spectrum of δ , δ , δ , and δ , and the multiplicative improvement in the constraints with nonlinear reconstruction,
cb r nr L
compared to those from the power spectrum of δ field alone. The signal to noise ratio of neutrino mass measurement,
cb
∝1/σ(M ), is only 12% lower than the linear power spectrum, i.e., the theoretical upper limit achievable with the δ field.
ν cb
only 12% lower than the theoretical upper limit achiev- Improvement
able with the δ field. Probes Ω Ω h n σ M
cb m b s 8 ν
We notice that the exact values of σ(M ) are slightly δ 2.72 2.65 2.64 2.65 2.49 2.54
ν nr
different between our results and Bayer et al. (2022). Model 1.63 1.78 1.49 1.00 1.95 2.00
Wehaveconfirmed thatthis isdue tothe different fidu-
Table 3. Multiplicative improvement using the recon-
cial cosmology adopted to compute the derivatives to
structed power spectrum and the theoretical model for
neutrinos. OurfiducialcosmologyisforaUniversewith k =0.5 hMpc−1.
max
massless neutrinos, while Bayer et al. (2022) have used
afiducialneutrinomassM =0.05eV whencomputing
ν
In the above analysis, we have used the reconstructed
thelineartheoryconstraints. Nevertheless,wefindthat
power spectrum from simulations for computing the co-
the relative improvements are not sensitive to these nu-
variance matrix and derivatives to cosmological param-
merical details and thus this does not impact our major
eters. This requires an accurate modeling of the re-
conclusions presented above, i.e., nonlinear reconstruc-
constructed power spectrum, which might be achieved
tion can recover almost all the neutrino information,
withtheemulatorconstructedfromsimulations(seee.g.,
nearly reaching the theoretical upper limit.
Wang et al. 2023, for a recent exploration).
When using the perturbation theory approach, usu-
4.5. Test with the theoretical model ally we need to use more parameters to describe the

9
nonlinear effects in the reconstructed power spectrum, simulated galaxy samples, which are more representa-
such as the simple model we introduced earlier. The tive of real data.
constraints on cosmological parameters will degrade af- In redshift space, more information regarding neutri-
termarginalizingoverthesenuisanceparametersdueto nos is available, since the redshift space distortions is
possible degeneracy between parameters. We can em- induced by the peculiar velocity, which is sourced by
ploy the simplified model in Eq. (13) to calculate the the total matter field and thus is sensitive to the neu-
Fisher information. In this approach, we utilize the re- trino overdensity δ (Bayer et al. 2022). Therefore, it is
ν
constructed power spectrum covariance matrix in the possible to obtain better constraints in redshift space,
simulations, while using Eq. (13) for derivative compu- which we plan to explore in future.
tations. In this way, we include the damping scale Σ To obtain an unbiased inference of cosmological pa-
and noise power spectrum P in the Fisher analysis. rameters,itisnecessarytohaveanaccuratepowerspec-
N
In Table 3, welist the multiplicative improvementus- trum model for reconstruction. The modeling of stan-
ing the reconstructed power spectrum from simulations dard reconstruction has been explored using both the
and the theoretical model for k = 0.5 hMpc−1. We Lagrangian perturbation theory (Noh et al. 2009; Pad-
max
see that the improvement of the constraint on neutrino manabhanetal.2009;White2015;Seoetal.2016;Chen
mass is ∼ 20% lower than using the power spectrum et al. 2019) and standard perturbation theory (Hikage
fromsimulation. However, nonlinearreconstructioncan et al. 2017, 2020). Recently, Ota et al. (2021, 2022)
still achieve a substantial improvement, by a factor of have explored the modeling of nonlinear displacement
2, compared to the original nonlinear power spectrum. using Lagrangian perturbation theory. The simulation-
The constraints on other parameters are not as good based method such as power spectrum emulator might
as the neutrino mass, which is due to the degeneracy be needed on nonlinear scales, where the perturbation
between the cosmological and nuisance parameters, es- theory methods are no longer available.
peciallythespectrumindexn ,sinceboththespectrum We have exclusively considered the nonlinear recon-
s
indexandthedampingscalechangethepowerspectrum struction methods based on solving the full nonlinear
shape. displacement field (Zhu et al. 2017; Schmittfull et al.
2017; Shi et al. 2018). The applications to halo fields
and redshift-space distortions have been studied exten-
5. DISCUSSION AND CONCLUSION
sively (see e.g., Yu et al. 2017; Zhu et al. 2018; Wang
In this paper, we apply nonlinear reconstruction to
& Pen 2019; Birkin et al. 2019; Wang et al. 2020; Liu
the CDM density fields from simulations and find the
et al. 2021; Seo et al. 2022). There are many other re-
parameterconstraintsare muchtighterthanthose from
constructionmethodsbasedondifferentprinciples, e.g.,
the power spectrum of δ directly, with the improve-
cb iterativemethods(Hada&Eisenstein2018,2019),opti-
menttobeafactorof∼2foreachparameter. Asalient
mizationtechniques(Seljaketal.2017;Fengetal.2018;
conclusion is that the constraint on neutrino mass can
Modi et al. 2018), forwarding modeling (Jasche & Wan-
nearly reach that of the linear power spectrum, with a
delt2013;Wangetal.2014),effectivefieldtheorybased
signal-to-noise ratio only 12% lower than the theoreti-
likelihood (Schmidt et al. 2019; Elsner et al. 2020), fast
cal best result, making reconstruction an efficient way
action minimization (Nusser & Branchini 2000; Sarpa
to extract cosmological information from the nonlinear
et al. 2019), machine learning (Mao et al. 2021; Shallue
galaxy survey data.
& Eisenstein 2022; Fl¨oss & Meerburg 2023), etc, which
WehaveassumedbaryonstraceCDMwhenusingthe
could also provide an improvement in the cosmological
CDM field as an approximation of the CDM+baryon
parameter constraints.
distribution. Thisisavalidapproximationonlargeand
While for the current galaxy samples such as BOSS
intermediate scales, k ≲ 0.5 hMpc−1, where the bary-
(Alam et al. 2017) and eBOSS (Alam et al. 2021), the
oniceffectsaresubdominant(seee.g.Chisarietal.2019;
nonlinear reconstruction methods have a similar effi-
Villaescusa-Navarro et al. 2021). The analysis with δ
cb ciency as standard reconstruction because of the higher
corresponds to an unbiased tracer with negligible shot
shotnoise. Theneartermandupcomingsurveyssuchas
noise, δ = bδ with b = 1. Therefore, our constraints
g cb DESI (DESI Collaboration et al. 2016), Euclid (Amen-
on M should be interpreted as maximum information
ν dola et al. 2018; Euclid Collaboration et al. 2020),
content in principle. Higher order biasing contributes
MegaMapper (Schlegel et al. 2022), etc, will generally
tens of percent of the total galaxy power spectrum at
have a much higher galaxy number density and there-
k ∼ 0.5 hMpc−1 (see e.g., Schmittfull et al. 2019) and
fore nonlinear reconstruction can achieve a better per-
theimportanceofshotnoisedependsonthespecificsur-
formance with the lower shot noise. We expect that
veys. In future work, we plan to extend the analysis to

10
reconstruction will be a promising method to extract
cosmological information from future galaxy surveys. We acknowledge Adrian Bayer and Gong-Bo Zhao for
enlightening discussions about the Fisher matrix cal-
culation. Hong-Ming Zhu receives support from the
National Natural Science Foundation of China (NSFC)
[Grant No. 11890691] and the Natural Sciences and En-
gineering Research Council of Canada (NSERC) [fund-
ing reference number CITA 490888-16]. Computations
were performed on the Niagara supercomputer at the
SciNetHPCConsortiumandtheSOSCIPConsortium’s
CPUcomputingplatform(Ponceetal.2019;Lokenetal.
2010). SciNet is funded by: the Canada Foundation
forInnovation; theGovernmentofOntario; OntarioRe-
search Fund - Research Excellence; and the University
ofToronto. SOSCIPisfundedbytheFederalEconomic
DevelopmentAgencyofSouthernOntario,theProvince
of Ontario, IBM Canada Ltd., Ontario Centres of Ex-
cellence,Mitacsand15Ontarioacademicmemberinsti-
tutions.
APPENDIX
A. CONVERGENCE TEST
In this appendix, we present the convergence tests of our results. In Figure 5, we show the marginalized 1σ errors
1.20
1.15
1.10
1.05
1.00
0.95
0.90
0.85
0.80 0 2000 4000
N
cov
)0005=voc
N(
/)voc
N(
k max=0.05hMpc 1 k max=0.06hMpc 1 k max=0.1hMpc 1 k max=0.5hMpc 1 k max=1hMpc 1
1.20 1.20 1.20 1.20
m ns
1.15 1.15 1.15 1.15
b 8
1.10 1.10 1.10 1.10 h Mv
1.05 1.05 1.05 1.05
1.00 1.00 1.00 1.00
0.95 0.95 0.95 0.95
0.90 0.90 0.90 0.90
0.85 0.85 0.85 0.85
0.80 0 2000 4000 0.80 0 2000 4000 0.80 0 2000 4000 0.80 0 2000 4000
N N N N
cov cov cov cov
Figure5. Marginalized1σerrorasafunctionofthenumberofsimulationsusedtocalculatethecovariancematrixfornonlinear
reconstruction. From left to right, we show the results for different k . For N =5000, a tight convergence is achieved.
max cov
on cosmological parameters as a function of the number of simulations used to estimate the covariance matrix for
nonlinear reconstruction. The results are presented as the ratio of the errors computed using N simulations and
cov
5000 simulations. The derivatives are computed using 500 pairs of simulations. From left to right, we show the
convergence of marginalized constraints for different k . We see that the results converge well for all scales from
max
0.05 hMpc−1 to 1 hMpc−1, with a small error at percent level.
In Fig. 6, we show the derivatives of power spectrum with respect to cosmological parameters. The derivatives for
the power spectrum show good convergence for 500 pairs of simulations.
Figure7showsthemarginalized1σerrorswithnonlinearreconstructiononthecosmologicalparametersasafunction
ofthesimulationpairstocomputethederivatives. Theresultsarepresentedastheratiobetweentheerrorscalculated

11
|     | 2.5 |     |     |     |     |     |     |     |     |     | 1   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10
| m   | 0.0 |     |     |     | b   |     |     |     |     | h   | 0   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
 /)k(Pnl
|  /)k(Pnl |     |     |     |     |  /)k(Pnl | 5   |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−2.5
−1
|     | −5.0 |     |     |     |     | 0   |     |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
−2
−7.5
|     | 10−2 |     | 10−1 | 100 |     | 10−2 | 10−1 |     | 100 |     | 10−2 |     | 10−1 | 100 |
| --- | ---- | --- | ---- | --- | --- | ---- | ---- | --- | --- | --- | ---- | --- | ---- | --- |
2
|     |     |     |     |     |     |     |     |     |     |     | 0.4 |     | L   | r   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     | 8 3 |     |     |     |     |     |     | n   | nr  |
|     | n s |     |     |     |     |     |     |     |     | M   |     |     |     |     |
0.3
|     |  /)k(Pnl 0 |     |     |     |  /)k(Pnl |     |     |     |     |  /)k(Pnl |     |     |     |     |
| --- | ---------- | --- | --- | --- | -------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
0.2
2
−2
0.1
|     | 10−2 |     | 10−1       | 100 |     | 10−2 | 10−1    |     | 100 |     | 10−2 |         | 10−1 | 100 |
| --- | ---- | --- | ---------- | --- | --- | ---- | ------- | --- | --- | --- | ---- | ------- | ---- | --- |
|     |      |     | k [hMpc 1] |     |     |      | k [hMpc | 1]  |     |     |      | k [hMpc | 1]   |     |
Figure 6. The derivatives of the power spectrum to cosmological parameters. The derivatives are well converged using 500
pairs of simulations.
k max=0.05hMpc 1 k max=0.06hMpc 1 k max=0.1hMpc 1 k max=0.5hMpc 1 k max=1hMpc 1
1.20
|     |     |     | 1.20 |     |     | 1.20 |     |     | 1.20 |     |     | 1.20 |     |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- |
ns
|           | 1.15 |     |      |     |     |      |     |     |      |     |     |      | m   |     |
| --------- | ---- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- |
|           |      |     | 1.15 |     |     | 1.15 |     |     | 1.15 |     |     | 1.15 |     |     |
|           |      |     |      |     |     |      |     |     |      |     |     |      | b   | 8   |
| )005=ired | 1.10 |     |      |     |     |      |     |     |      |     |     |      | h   | Mv  |
|           |      |     | 1.10 |     |     | 1.10 |     |     | 1.10 |     |     | 1.10 |     |     |
1.05
|     |     |     | 1.05 |     |     | 1.05 |     |     | 1.05 |     |     | 1.05 |     |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- |
N( 1.00
|     |     |     | 1.00 |     |     | 1.00 |     |     | 1.00 |     |     | 1.00 |     |     |
| --- | --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- |
/)ired
|     | 0.95 |     | 0.95 |     |     | 0.95 |     |     | 0.95 |     |     | 0.95 |     |     |
| --- | ---- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- | ---- | --- | --- |
N(
|     | 0.90 |      | 0.90  |     |      | 0.90  |      |     | 0.90 |     |      | 0.90 |      |     |
| --- | ---- | ---- | ----- | --- | ---- | ----- | ---- | --- | ---- | --- | ---- | ---- | ---- | --- |
|     | 0.85 |      | 0.85  |     |      | 0.85  |      |     | 0.85 |     |      | 0.85 |      |     |
|     | 0.80 |      | 0.80  |     |      | 0.80  |      |     | 0.80 |     |      | 0.80 |      |     |
|     | 0    | 200  | 400 0 |     | 200  | 400 0 | 200  | 400 | 0    | 200 | 400  | 0    | 200  | 400 |
|     |      | N    |       |     | N    |       | N    |     |      |     | N    |      | N    |     |
|     |      | deri |       |     | deri |       | deri |     |      |     | deri |      | deri |     |
Figure 7. Marginalized 1σ error as a function of the number of simulation pairs used to calculate the partial derivatives for
nonlinear reconstruction. From left to right, we show the results for different k . For N = 500, a good convergence is
|          |     |        |             |     |             |     |     |     |     | max | deri |     |     |     |
| -------- | --- | ------ | ----------- | --- | ----------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
| achieved | for | k from | 0.06 hMpc−1 | to  | 0.5 hMpc−1. |     |     |     |     |     |      |     |     |     |
max
with N pairs and 500 pairs of simulations. The covariance matrix is computed using 5000 simulations. For the
Deri
derivatives, a good convergence is achieved for k from 0.06 hMpc−1 to 0.5 hMpc−1. For k = 0.05 hMpc−1,
|     |     |     |     |     |     | max |     |     |     |     |     | max |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the fractional error is about 20% when using 500 simulation pairs. There are not enough modes on these large scales
to get converged results with the simulations available. A higher accuracy power spectrum estimation is required
hMpc−1,
to obtain reliable results at k max = 0.05 but it is fine since the dominant constraining power comes from
small-scale modes. For k = 0.06 hMpc−1, the results become much more stable. The fractional error is under
max
2% when using 500 simulation pairs to obtain partial derivatives. Therefore, we present the Fisher constraints from
| k   | =0.06 | hMpc−1 | to k | =0.5 hMpc−1 |     | as our default | results. |           |     |     |     |     |     |     |
| --- | ----- | ------ | ---- | ----------- | --- | -------------- | -------- | --------- | --- | --- | --- | --- | --- | --- |
| max |       |        | max  |             |     |                |          |           |     |     |     |     |     |     |
|     |       |        |      |             | B.  | CONFIDENCE     |          | INTERVALS |     |     |     |     |     |     |
In Figure 8, We show the two-dimensional 68% and 95% confidence intervals from the Fisher analysis for
hMpc−1.
k = 0.5 The constraints are generally much tighter after reconstruction. However, it does not break
max

12
2
0
2
0.3 0.4
m
]Ve[v
M
0.9
0.8
0.7
8
1.0
0.8
n s
0.8
0.6
0.4
h
0.06
0.04
b
L
cb
nr
Model
0.03 0.07 0.5 0.9 0.8 1.0 0.7 0.80.9 2 0 2
b h n s 8 M v[eV]
Figure 8. 68% (darker shades) and 95% (lighter shades) confidence contours for the cosmological parameters for P (black),
δL
P (red), P (blue) and power spectrum with our theoretical model (orange) with k =0.5 hMpc−1. The constraints are
δcb δnr max
much tighter after reconstruction.
the strong degeneracy between σ and M using the reconstructed power spectrum alone. By introducing other
8 ν
nonlinear statistics, a much tighter constraint can be achieved (Bayer et al. 2021).
REFERENCES
Akeson, R., Armus, L., Bachelet, E., et al. 2019, arXiv Alam, S., Aubert, M., Avila, S., et al. 2021, PhRvD, 103,
e-prints, arXiv:1902.05569. 083533, doi: 10.1103/PhysRevD.103.083533
https://arxiv.org/abs/1902.05569 Amendola, L., Appleby, S., Avgoustidis, A., et al. 2018,
Alam, S., Ata, M., Bailey, S., et al. 2017, MNRAS, 470, Living Reviews in Relativity, 21, 2,
2617, doi: 10.1093/mnras/stx721 doi: 10.1007/s41114-017-0010-3

13
Bayer, A. E., Banerjee, A., & Seljak, U. 2022, PhRvD, 105, Hikage, C., Koyama, K., & Takahashi, R. 2020, PhRvD,
123510, doi: 10.1103/PhysRevD.105.123510 101, 043510, doi: 10.1103/PhysRevD.101.043510
Bayer, A. E., Villaescusa-Navarro, F., Massara, E., et al. Jasche, J., & Wandelt, B. D. 2013, MNRAS, 432, 894,
| 2021, | ApJ, 919, | 24, | doi: 10.3847/1538-4357/ac0e91 |     |     |     |     |     |     |     |     |     |     |     |
| ----- | --------- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
doi: 10.1093/mnras/stt449
| Birkin, J., | Li,  | B., Cautun,           | M., | & Shi, | Y. 2019, | MNRAS, |              |     |           |     |       |           |      |     |
| ----------- | ---- | --------------------- | --- | ------ | -------- | ------ | ------------ | --- | --------- | --- | ----- | --------- | ---- | --- |
|             |      |                       |     |        |          |        | Lesgourgues, | J., | & Pastor, | S.  | 2006, | PhR, 429, | 307, |     |
| 483, 5267,  | doi: | 10.1093/mnras/sty3365 |     |        |          |        |              |     |           |     |       |           |      |     |
doi: 10.1016/j.physrep.2006.04.001
| Bond, J. | R., Efstathiou,                  |      | G., &     | Silk, | J. 1980, | PhRvL, 45, |            |                |       |            |       |          |      |      |
| -------- | -------------------------------- | ---- | --------- | ----- | -------- | ---------- | ---------- | -------------- | ----- | ---------- | ----- | -------- | ---- | ---- |
|          |                                  |      |           |       |          |            | Lewis, A., | Challinor,     | A.,   | & Lasenby, |       | A. 2000, | ApJ, | 538, |
| 1980,    | doi: 10.1103/PhysRevLett.45.1980 |      |           |       |          |            |            |                |       |            |       |          |      |      |
|          |                                  |      |           |       |          |            | 473, doi:  | 10.1086/309179 |       |            |       |          |      |      |
| Carron,  | J. 2013,                         | A&A, | 551, A88, |       |          |            |            |                |       |            |       |          |      |      |
|          |                                  |      |           |       |          |            | Liu, Y.,   | Yu, Y.,        | & Li, | B. 2021,   | ApJS, | 254,     | 4,   |      |
doi: 10.1051/0004-6361/201220538
doi: 10.3847/1538-4365/abe868
| Castorina, | E.,   | Carbone, | C., Bel, | J., | Sefusatti, | E., & Dolag, |            |         |     |        |        |           |         |     |
| ---------- | ----- | -------- | -------- | --- | ---------- | ------------ | ---------- | ------- | --- | ------ | ------ | --------- | ------- | --- |
|            |       |          |          |     |            |              | Loken, C., | Gruner, | D., | Groer, | L., et | al. 2010, | Journal | of  |
| K. 2015,   | JCAP, | 2015,    | 043,     |     |            |              |            |         |     |        |        |           |         |     |
doi: 10.1088/1475-7516/2015/07/043 Physics: Conference Series, 256, 012026,
Chen, S.-F., Vlah, Z., & White, M. 2019, JCAP, 2019, 017, doi: 10.1088/1742-6596/256/1/012026
|     |     |     |     |     |     |     | LSST Science | Collaboration, |     |     | Abell, | P. A., | Allison, | J., et al. |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | --- | ------ | ------ | -------- | ---------- |
doi: 10.1088/1475-7516/2019/09/017
|          |        |       |                 |     |        |               | 2009, | arXiv e-prints, |     | arXiv:0912.0201. |     |     |     |     |
| -------- | ------ | ----- | --------------- | --- | ------ | ------------- | ----- | --------------- | --- | ---------------- | --- | --- | --- | --- |
| Chisari, | N. E., | Mead, | A. J., Joudaki, |     | S., et | al. 2019, The |       |                 |     |                  |     |     |     |     |
Open Journal of Astrophysics, 2, 4, https://arxiv.org/abs/0912.0201
doi: 10.21105/astro.1905.06082 Mao, T.-X., Wang, J., Li, B., et al. 2021, MNRAS, 501,
| DESI Collaboration, |       | Aghamousa, |                   | A., | Aguilar, | J., et al. |          |                             |     |     |     |     |            |       |
| ------------------- | ----- | ---------- | ----------------- | --- | -------- | ---------- | -------- | --------------------------- | --- | --- | --- | --- | ---------- | ----- |
|                     |       |            |                   |     |          |            | 1499,    | doi: 10.1093/mnras/staa3741 |     |     |     |     |            |       |
| 2016,               | arXiv | e-prints,  | arXiv:1611.00036. |     |          |            |          |                             |     |     |     |     |            |       |
|                     |       |            |                   |     |          |            | Massara, | E., Villaescusa-Navarro,    |     |     | F., | Ho, | S., Dalal, | N., & |
https://arxiv.org/abs/1611.00036 Spergel, D. N. 2021, PhRvL, 126, 011301, doi: 10.1103/
| Dor´e, O., | Bock, | J., Ashby, | M., | et al. | 2014, | arXiv e-prints, |     |     |     |     |     |     |     |     |
| ---------- | ----- | ---------- | --- | ------ | ----- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
PhysRevLett.126.01130110.48550/arXiv.2001.11024
| arXiv:1412.4872. |     | https://arxiv.org/abs/1412.4872 |        |            |            |       |          |       |        |          |        |     |            |     |
| ---------------- | --- | ------------------------------- | ------ | ---------- | ---------- | ----- | -------- | ----- | ------ | -------- | ------ | --- | ---------- | --- |
|                  |     |                                 |        |            |            |       | Meiksin, | A., & | White, | M. 1999, | MNRAS, |     | 308, 1179, |     |
| Eisenstein,      | D.  | J., Seo,                        | H.-J., | Sirko, E., | & Spergel, | D. N. |          |       |        |          |        |     |            |     |
doi: 10.1046/j.1365-8711.1999.02825.x
| 2007,       | ApJ, 664, | 675, | doi: 10.1086/518712 |             |     |               |           |       |       |         |          |       |       |      |
| ----------- | --------- | ---- | ------------------- | ----------- | --- | ------------- | --------- | ----- | ----- | ------- | -------- | ----- | ----- | ---- |
|             |           |      |                     |             |     |               | Modi, C., | Feng, | Y., & | Seljak, | U. 2018, | JCAP, | 2018, | 028, |
| Elsner, F., | Schmidt,  | F.,  | Jasche,             | J., Lavaux, |     | G., & Nguyen, |           |       |       |         |          |       |       |      |
doi: 10.1088/1475-7516/2018/10/028
| N.-M. | 2020, | JCAP, | 2020, 029, |     |     |     |     |     |     |     |     |     |     |     |
| ----- | ----- | ----- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
doi: 10.1088/1475-7516/2020/01/029 Noh,Y.,White,M.,&Padmanabhan,N.2009,PhRvD,80,
|                       |      |            |            |     |         |            | 123501, | doi:             | 10.1103/PhysRevD.80.123501 |          |        |     |           |     |
| --------------------- | ---- | ---------- | ---------- | --- | ------- | ---------- | ------- | ---------------- | -------------------------- | -------- | ------ | --- | --------- | --- |
| Euclid Collaboration, |      |            | Blanchard, | A., | Camera, | S., et al. |         |                  |                            |          |        |     |           |     |
|                       |      |            |            |     |         |            | Nusser, | A., & Branchini, |                            | E. 2000, | MNRAS, |     | 313, 587, |     |
| 2020,                 | A&A, | 642, A191, |            |     |         |            |         |                  |                            |          |        |     |           |     |
doi: 10.1051/0004-6361/202038071 doi: 10.1046/j.1365-8711.2000.03261.x
Feng, Y., Seljak, U., & Zaldarriaga, M. 2018, JCAP, 2018, Ota, A., Seo, H.-J., Saito, S., & Beutler, F. 2021, PhRvD,
043, doi: 10.1088/1475-7516/2018/07/043 104, 123508, doi: 10.1103/PhysRevD.104.123508
| Ferraro,  | S., Sailer,       | N., | Slosar, | A., & | White, | M. 2022, arXiv |                                  |       |           |                   |     |     |     |     |
| --------- | ----------------- | --- | ------- | ----- | ------ | -------------- | -------------------------------- | ----- | --------- | ----------------- | --- | --- | --- | --- |
|           |                   |     |         |       |        |                | —. 2022,                         | arXiv | e-prints, | arXiv:2211.07960. |     |     |     |     |
| e-prints, | arXiv:2203.07506. |     |         |       |        |                | https://arxiv.org/abs/2211.07960 |       |           |                   |     |     |     |     |
https://arxiv.org/abs/2203.07506 Padmanabhan,N.,White,M.,&Cohn,J.D.2009,PhRvD,
| Fisher, R.    | A. 1925, | Proceedings |          | of the | Cambridge |     |              |      |                            |                 |     |     |            |       |
| ------------- | -------- | ----------- | -------- | ------ | --------- | --- | ------------ | ---- | -------------------------- | --------------- | --- | --- | ---------- | ----- |
|               |          |             |          |        |           |     | 79, 063523,  | doi: | 10.1103/PhysRevD.79.063523 |                 |     |     |            |       |
| Philosophical |          | Society,    | 22, 700, |        |           |     |              |      |                            |                 |     |     |            |       |
|               |          |             |          |        |           |     | Padmanabhan, |      | N., Xu,                    | X., Eisenstein, |     | D.  | J., et al. | 2012, |
doi: 10.1017/S0305004100009580
|             |             |     |       |             |           |     | MNRAS, | 427, | 2132, |     |     |     |     |     |
| ----------- | ----------- | --- | ----- | ----------- | --------- | --- | ------ | ---- | ----- | --- | --- | --- | --- | --- |
| Flo¨ss, T., | & Meerburg, |     | P. D. | 2023, arXiv | e-prints, |     |        |      |       |     |     |     |     |     |
doi: 10.1111/j.1365-2966.2012.21888.x
| arXiv:2305.07018, |               | doi: | 10.48550/arXiv.2305.07018 |       |        |            |          |                    |                   |     |          |     |        |       |
| ----------------- | ------------- | ---- | ------------------------- | ----- | ------ | ---------- | -------- | ------------------ | ----------------- | --- | -------- | --- | ------ | ----- |
|                   |               |      |                           |       |        |            | Paillas, | E., Cuesta-Lazaro, |                   | C., | Zarrouk, | P., | et al. | 2022, |
| Hada, R.,         | & Eisenstein, |      | D. J.                     | 2018, | MNRAS, | 478, 1866, |          |                    |                   |     |          |     |        |       |
|                   |               |      |                           |       |        |            | arXiv    | e-prints,          | arXiv:2209.04310. |     |          |     |        |       |
doi: 10.1093/mnras/sty1203
https://arxiv.org/abs/2209.04310
| —. 2019,  | MNRAS,               | 482, | 5685, | doi: 10.1093/mnras/sty3137 |     |       |          |             |        |     |       |       |       |     |
| --------- | -------------------- | ---- | ----- | -------------------------- | --- | ----- | -------- | ----------- | ------ | --- | ----- | ----- | ----- | --- |
|           |                      |      |       |                            |     |       | Pan, Q., | Pen, U.-L., | Inman, | D., | & Yu, | H.-R. | 2017, |     |
| Hahn, C., | Villaescusa-Navarro, |      |       | F., Castorina,             |     | E., & |          |             |        |     |       |       |       |     |
Scoccimarro, R. 2020, JCAP, 2020, 040, MNRAS, 469, 1968, doi: 10.1093/mnras/stx774
doi: 10.1088/1475-7516/2020/03/040 Percival, W. J., Friedrich, O., Sellentin, E., & Heavens, A.
Hikage, C., Koyama, K., & Heavens, A. 2017, PhRvD, 96, 2022, MNRAS, 510, 3207,
043513, doi: 10.1103/PhysRevD.96.043513 doi: 10.1093/mnras/stab354010.48550/arXiv.2108.10402

14
Ponce, M., van Zon, R., Northrup, S., et al. 2019, in Shi, Y., Cautun, M., & Li, B. 2018, PhRvD, 97, 023505,
Proceedings of the Practice and Experience in Advanced doi: 10.1103/PhysRevD.97.023505
Research Computing on Rise of the Machines (Learning), Springel, V. 2005, MNRAS, 364, 1105, doi: 10.1111/j.
PEARC ’19 (New York, NY, USA: Association for 1365-2966.2005.09655.x10.48550/arXiv.astro-ph/0505010
Computing Machinery), doi: 10.1145/3332186.3332195 Takada, M., Ellis, R. S., Chiba, M., et al. 2014, PASJ, 66,
| Rimes, | C. D., & | Hamilton, |     | A. J. S. | 2005, MNRAS, | 360, |          |                     |     |     |     |     |
| ------ | -------- | --------- | --- | -------- | ------------ | ---- | -------- | ------------------- | --- | --- | --- | --- |
|        |          |           |     |          |              |      | R1, doi: | 10.1093/pasj/pst019 |     |     |     |     |
L82, doi: 10.1111/j.1745-3933.2005.00051.x Tegmark, M. 1997, PhRvL, 79, 3806,
| —. 2006, | MNRAS, | 371, | 1205, |     |     |     | doi: 10.1103/PhysRevLett.79.3806 |     |     |     |     |     |
| -------- | ------ | ---- | ----- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
doi: 10.1111/j.1365-2966.2006.10710.x Villaescusa-Navarro, F., Hahn, C., Massara, E., et al. 2020,
Sailer, N., Castorina, E., Ferraro, S., & White, M. 2021, ApJS, 250, 2, doi: 10.3847/1538-4365/ab9d82
| JCAP, | 2021, | 049, doi: | 10.1088/1475-7516/2021/12/049 |     |     |     |                      |     |     |                   |     |            |
| ----- | ----- | --------- | ----------------------------- | --- | --- | --- | -------------------- | --- | --- | ----------------- | --- | ---------- |
|       |       |           |                               |     |     |     | Villaescusa-Navarro, |     | F., | Angl´es-Alca´zar, | D., | Genel, S., |
Sarpa, E., Schimd, C., Branchini, E., & Matarrese, S. 2019, et al. 2021, ApJ, 915, 71, doi: 10.3847/1538-4357/abf7ba
MNRAS, 484, 3818, doi: 10.1093/mnras/stz278 Wang, H., Mo, H. J., Yang, X., Jing, Y. P., & Lin, W. P.
| Schlegel, | D. J., | Kollmeier, | J.  | A., Aldering, |     | G., et al. 2022, |       |           |          |                            |     |     |
| --------- | ------ | ---------- | --- | ------------- | --- | ---------------- | ----- | --------- | -------- | -------------------------- | --- | --- |
|           |        |            |     |               |     |                  | 2014, | ApJ, 794, | 94, doi: | 10.1088/0004-637X/794/1/94 |     |     |
arXiv e-prints, arXiv:2209.04322. Wang, X., & Pen, U.-L. 2019, ApJ, 870, 116,
https://arxiv.org/abs/2209.04322
doi: 10.3847/1538-4357/aaf231
Schmidt, F., Elsner, F., Jasche, J., Nguyen, N. M., & Wang, Y., Li, B., & Cautun, M. 2020, MNRAS, 497, 3451,
Lavaux, G. 2019, JCAP, 2019, 042, doi: 10.1093/mnras/staa2136
doi: 10.1088/1475-7516/2019/01/042
|              |     |          |                                 |                |     |          | Wang, Y., | Zhao,             | G.-B., | Koyama, K., | et al. 2022, | arXiv |
| ------------ | --- | -------- | ------------------------------- | -------------- | --- | -------- | --------- | ----------------- | ------ | ----------- | ------------ | ----- |
| Schmittfull, | M., | Baldauf, | T.,                             | & Zaldarriaga, |     | M. 2017, |           |                   |        |             |              |       |
|              |     |          |                                 |                |     |          | e-prints, | arXiv:2202.05248. |        |             |              |       |
| PhRvD,       | 96, | 023505,  | doi: 10.1103/PhysRevD.96.023505 |                |     |          |           |                   |        |             |              |       |
https://arxiv.org/abs/2202.05248
| Schmittfull, | M.,    | Simonovi´c, |         | M., Assassi, | V., | & Zaldarriaga, |                   |       |           |                           |       |           |
| ------------ | ------ | ----------- | ------- | ------------ | --- | -------------- | ----------------- | ----- | --------- | ------------------------- | ----- | --------- |
|              |        |             |         |              |     |                | Wang, Y.,         | Zhao, | R., Zhai, | Z., et al. 2023,          | arXiv | e-prints, |
| M. 2019,     | PhRvD, | 100,        | 043514, |              |     |                |                   |       |           |                           |       |           |
|              |        |             |         |              |     |                | arXiv:2311.05848, |       | doi:      | 10.48550/arXiv.2311.05848 |       |           |
doi: 10.1103/PhysRevD.100.043514
|     |     |     |     |     |     |     | White, M. | 2015, | MNRAS, | 450, 3822, |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------ | ---------- | --- | --- |
Seljak,U.,Aslanyan,G.,Feng,Y.,&Modi,C.2017,JCAP,
doi: 10.1093/mnras/stv842
| 2017,       | 009, doi: | 10.1088/1475-7516/2017/12/009 |       |          |        |          |              |        |     |                  |      |           |
| ----------- | --------- | ----------------------------- | ----- | -------- | ------ | -------- | ------------ | ------ | --- | ---------------- | ---- | --------- |
|             |           |                               |       |          |        |          | Yu, Y., Zhu, | H.-M., | &   | Pen, U.-L. 2017, | ApJ, | 847, 110, |
| Seo, H.-J., | Beutler,  | F.,                           | Ross, | A. J., & | Saito, | S. 2016, |              |        |     |                  |      |           |
doi: 10.3847/1538-4357/aa89e7
| MNRAS, | 460, | 2453, | doi: 10.1093/mnras/stw1138 |     |     |     |     |     |     |     |     |     |
| ------ | ---- | ----- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Zhu,H.-M.,Yu,Y.,&Pen,U.-L.2018,PhRvD,97,043502,
| Seo, H.-J., | Ota, | A., Schmittfull, |     | M., | Saito, | S., & Beutler, F. |     |     |     |     |     |     |
| ----------- | ---- | ---------------- | --- | --- | ------ | ----------------- | --- | --- | --- | --- | --- | --- |
doi: 10.1103/PhysRevD.97.043502
| 2022, | MNRAS, | 511, | 1557, | doi: 10.1093/mnras/stac082 |     |     |     |     |     |     |     |     |
| ----- | ------ | ---- | ----- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Zhu,H.-M.,Yu,Y.,Pen,U.-L.,Chen,X.,&Yu,H.-R.2017,
| Shallue,          | C. J., | & Eisenstein, |                                  | D. J. 2022, | arXiv | e-prints, |        |             |     |                                 |     |     |
| ----------------- | ------ | ------------- | -------------------------------- | ----------- | ----- | --------- | ------ | ----------- | --- | ------------------------------- | --- | --- |
|                   |        |               |                                  |             |       |           | PhRvD, | 96, 123502, |     | doi: 10.1103/PhysRevD.96.123502 |     |     |
| arXiv:2207.12511. |        |               | https://arxiv.org/abs/2207.12511 |             |       |           |        |             |     |                                 |     |     |