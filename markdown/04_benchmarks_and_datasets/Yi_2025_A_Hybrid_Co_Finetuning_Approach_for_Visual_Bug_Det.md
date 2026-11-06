---
title: "A Hybrid Co Finetuning Approach for Visual Bug Det"
author: "Yi"
year: "2025"
source_file: "04_benchmarks_and_datasets/Yi_2025_A_Hybrid_Co_Finetuning_Approach_for_Visual_Bug_Det.pdf"
source_sha256: "eddbbcf6b5aebdb54c403bbdff306f4e753f074a4ee0a2c54c1198556e545c7e"
converted_at: "2026-11-06T15:13:12.456548+00:00"
markitdown_version: "0.1.9"
char_count: 93603
---
A Hybrid Co-Finetuning Approach for Visual Bug Detection in Video Games
|     |     |     | FaliuYi*1 | SherifAbdelfattah*1 |     |     | WeiHuang1 | AdrianBrown1 |     |     |     |
| --- | --- | --- | --------- | ------------------- | --- | --- | --------- | ------------ | --- | --- | --- |
Abstract ensureproductquality. However,theescalatingdemandand
complexityofgamespresentanotablechallengetothisap-
|     | Manual | identification | of  | visual bugs | in  | video |     |     |     |     |     |
| --- | ------ | -------------- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- |
proach,asexpandingtheworkforceentailsincreasedcosts
gamesisaresource-intensiveandcostlyprocess,
andmanagementoverhead.Oneoftheimportantgamequal-
oftendemandingspecializeddomainknowledge.
5202 tcO 4  ]VC.sc[  1v19530.0152:viXra itycontrolactivitiesistestingforvisualbugs(Taesirietal.,
Whilesupervisedvisualbugdetectionmodelsof- 2024),whichmightgetintroducedduetoissuesinthecode,
ferapromisingsolution,theirrelianceonexten-
hardwareinfrastructure,ornetworking(e.g.,playerload).
sivelabeleddatasetspresentsasignificantchal-
Ingeneral,gamevisualbugscouldbecategorizedintotwo
|     | lenge due                                 | to the | infrequent | occurrence | of  | such |             |                    |                |       |        |
| --- | ----------------------------------------- | ------ | ---------- | ---------- | --- | ---- | ----------- | ------------------ | -------------- | ----- | ------ |
|     |                                           |        |            |            |     |      | categories: | 1) bugs detectable | using a single | frame | (e.g., |
|     | bugs. Toovercomethislimitation,weproposea |        |            |            |     |      |             |                    |                |       |        |
textureissues,object-to-objectclipping,orobjectfloating),
hybridCo-FineTuning(CFT)methodthateffec- and2)bugsthatneedmulti-frame(i.e.,temporalcontext)
tivelyintegratesbothlabeledandunlabeleddata.
|     |     |     |     |     |     |     | tobedetected(e.g.,glitchesandlightingissues). |     |     |     | Thelat- |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | ------- |
Ourapproachleverageslabeledsamplesfromthe
|     |     |     |     |     |     |     | ter category | is more challenging | for the | need to consider |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------------- | ------- | ---------------- | --- |
targetgameanddiverseco-domaingames,addi-
thetemporalcontextacrossmultipleframes,whichmakes
tionallyincorporatingunlabeleddatatoenhance
itmoredemandingandtime-consumingforqualityteams
featurerepresentationlearning.Thisstrategymax- performingmanualtesting.
|     | imizes the | utility | of all | available data, | substan- |     |     |     |     |     |     |
| --- | ---------- | ------- | ------ | --------------- | -------- | --- | --- | --- | --- | --- | --- |
tiallyreducingthedependencyonlabeledexam- UsingComputerVision(CV)models(Paduraruetal.,2021)
forautomaticvisualbugdetectionisapromisingsolution
|     | plesfromthespecifictargetgame. |     |     | Thedeveloped |     |     |     |     |     |     |     |
| --- | ------------------------------ | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
frameworkdemonstratesenhancedscalabilityand that can significantly reduce costs and manual labor. A
typicalworkflowforutilizingaCVmodelforvisualbugde-
adaptability,facilitatingefficientvisualbugdetec-
tionacrossvariousgametitles. Ourexperimen- tectionisdepictedinFigure1. Theworkflowstartswithcol-
tal results show the robustness of the proposed lectinglabeledsampleshighlightingthebugs. Visualbugs
areusuallypreferredtobeindicatedwithinaboundingbox,
methodforgamevisualbugdetection,exhibiting
superiorperformancecomparedtoconventional makingiteasiertolocateandfixthebugs. Consequently,an
baselinesacrossmultiplegamingenvironments. objectdetectionannotationmethod(Linetal.,2014)iswell-
|     |     |     |     |     |     |     | suited to | meet this requirement. | Afterwards, | supervised |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------------------- | ----------- | ---------- | --- |
Furthermore,CFTmaintainscompetitiveperfor-
manceevenwhentrainedwithonly50%ofthe modeltrainingisinitiatedonthecollecteddatasets. During
|     |     |     |     |     |     |     | deployment | time, the model | predicts visual | bugs | on new |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | --------------- | ---- | ------ |
labeleddatafromthetargetgame.
|     |     |     |     |     |     |     | deployment | samples, followed | by a triage | stage to | verify |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------------- | ----------- | -------- | ------ |
andisolatefalse-positivesamples.Finally,thedetectedbugs
areloggedinthedatabase.
1.INTRODUCTION
Supervisedmachinelearning-basedvisualbugdetectionis
Overthepastdecade,thevideogameindustryhasexperi-
anincreasinglypromisingapproachforautomatinggame
| enced | substantial | growth, | driven | by advancements |     | in 3D |     |     |     |     |     |
| ----- | ----------- | ------- | ------ | --------------- | --- | ----- | --- | --- | --- | --- | --- |
testingworkflows,offeringeffectiveandlabor-efficientso-
gameengines,increasedcomputingpower,expandedInter-
lutions(Davarmaneshetal.,2020;Taesirietal.,2020;Azizi
netbandwidth,andsustainedconsumerdemand(Skwarczek,
|     |     |     |     |     |     |     | &Zaman,2023;2024;Lingetal.,2020). |     |     | Despitetheeffec- |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | ---------------- | --- |
2021). Thisgrowthhascoincidedwithacorrespondingrise
tivenessofthesupervisedlearningmethodology,itsprimary
inthecomplexityandscaleofgamedevelopment,necessi-
|     |     |     |     |     |     |     | limitation | is the requirement | for a substantial | volume | of  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------------------ | ----------------- | ------ | --- |
tatingthedeploymentoflargequalityassuranceteamsto
|     |     |     |     |     |     |     | labeled | training data. This | is particularly | challenging | for |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------- | --------------- | ----------- | --- |
*Equal 1Xbox multi-frame bugs, which typically have a low prevalence
|     | contribution |     |     | Studios Quality | AI  | Lab, Xbox |     |     |     |     |     |
| --- | ------------ | --- | --- | --------------- | --- | --------- | --- | --- | --- | --- | --- |
Game Studios, Microsoft, USA. Correspondence to: Faliu rate in video games. Current strategies to mitigate this
Yi <faliuyi@microsoft.com>, Sherif Abdelfattah <sherif- issueincludeemployingweaklysupervisedlearningwith
gad@microsoft.com>. synthetic data augmentations, which are generated using
|     |     |     |     |     |     |     | task-specificdomainknowledge(Rahman,2023). |     |     | Another |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | ------- | --- |

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
|     |     | Bug Labeling |     |     |     |     | Testing Video  |     |     | Video Triage |     |     |
| --- | --- | ------------ | --- | --- | --- | --- | -------------- | --- | --- | ------------ | --- | --- |
Collection
Training
|     | Dataset    |     |          |                                                    |     |     |     | Model      |     |     |     |             |
| --- | ---------- | --- | -------- | -------------------------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | ----------- |
|     |            |     |          | Model Training                                     |     |     |     |            |     |     |     | Bug Logging |
|     | Collection |     |          |                                                    |     |     |     | Prediction |     |     |     |             |
|     |            |     | Figure1. | Atypicalworkflowforvisualbugdetectioninvideogames. |     |     |     |            |     |     |     |             |
approachinvolvesleveragingtheinductivebiasofpretrained • Weproposeaco-finetuningmethodleveraginglabeled
multimodal large language models to reduce reliance on datafromatargetgameandamixtureofothergames
human supervision (Taesiri et al., 2022). In contrast to tomaximizetheutilizationofdatalabelingefforts.
thispriorwork,ourmethodisindependentoftask-specific
domainknowledgeandiscomputationallyefficient,facil-
itatingrapiddeploymentandbroadaccessibilityforgame
• Weproposeanovelself-supervisedlearningmethod
developmentteams. thatharnessesunlabeledgamingdatatolearnaneffec-
Weproposeahybridmethodutilizingbothsupervisedand tivevisualrepresentationandenhancedataefficiency.
self-supervisedlearningobjectivestoleveragelabeleddata,
providingadirectsignalforbugdetection,andunlabeled
data, providing inductive bias on the visual semantics in • We provide a comprehensive evaluation of the pro-
the gaming domain. Moreover, our method could effec- posed method using multiple gaming environments
tively fuse data from other games during training, which resembling actual AAA games and comparing with
werefertoasco-finetuning,tofurtherenhancethetraining
well-establishedbaselinestrainedandfine-tunedusing
| dataefficiencycharacteristics. |                |      | Duringsupervisedtraining, |      |      |     | AzureAutoML. |     |     |     |     |     |
| ------------------------------ | -------------- | ---- | ------------------------- | ---- | ---- | --- | ------------ | --- | --- | --- | --- | --- |
| we fuse                        | the supervised | loss | from a target             | game | with | one |              |     |     |     |     |     |
from a mixture of other gaming titles using a linear gat- 2.RELATEDWORK
| ingscheme. | Whileforself-supervisedlearning,weadopt |     |                   |     |            |     |               |            |          |     |            |       |
| ---------- | --------------------------------------- | --- | ----------------- | --- | ---------- | --- | ------------- | ---------- | -------- | --- | ---------- | ----- |
| a novel    | method following                        |     | a Joint Embedding |     | Predictive |     |               |            |          |     |            |       |
|            |                                         |     |                   |     |            |     | The emergence | of machine | learning | has | introduced | auto- |
Architecture (JEPA) (Assran et al., 2023) that aims to re- matedandsemi-automatedapproachestoenhancetheeffi-
constructmaskedpatchesfromunlabeledtrainingsamples ciencyofbugdetection. Supervisedmethodsforvisualbug
on a target embedding space rather than the pixel space. detection (Davarmanesh et al., 2020; Taesiri et al., 2020;
Targetingreconstructionontheembeddingspacehelpsto Azizi&Zaman,2023;2024;Lingetal.,2020;Tammetal.,
focusthelearnedvisualrepresentationonhigh-levelcon-
2022)areoftenlimitedbytheirrelianceonlarge,labeled
ceptswhilebeingrobusttonoiseandirrelevantdynamics datasets,whicharedifficulttocollectfromspecificgame
comparedtoworkingonthepixelspace(Dawid&LeCun, titles. To address this, some researchers have proposed
2023). Moreover, we aim to distill the target embedding weaksupervisionmethodsthatincorporatesyntheticdata
fromlargepretrainedvisionencoders(Kirillovetal.,2023; derivedfromtask-specificdomainknowledgetoreducethe
Caronetal.,2021;Oquabetal.,2023),whichincorporates
|     |     |     |     |     |     |     | need for | manual labeling | (Rahman, | 2023). |     | Another ap- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------- | -------- | ------ | --- | ----------- |
useful inductive bias and facilitates using efficient vision proach,demonstratedin(Arnabetal.,2022),showsthatco-
encodersduringinference. finetuningwithmultiplecorrelatedsupervisedtasks,suchas
videoactionclassificationandobjectdetection,canimprove
| Tocontrasttheperformanceofourproposedmethod, |                   |     |                 |       |       | we       |                                   |                  |          |                     |                 |          |
| -------------------------------------------- | ----------------- | --- | --------------- | ----- | ----- | -------- | --------------------------------- | ---------------- | -------- | ------------------- | --------------- | -------- |
|                                              |                   |     |                 |       |       |          | performance                       | over traditional | transfer |                     | learning.       | Our work |
| evaluate                                     | its bug detection |     | performance     | using | three | dif-     |                                   |                  |          |                     |                 |          |
|                                              |                   |     |                 |       |       |          | builds upon                       | this paradigm    | by       | combining           | self-supervised |          |
| ferent gaming                                | environments,     |     | while comparing |       | it    | to well- |                                   |                  |          |                     |                 |          |
|                                              |                   |     |                 |       |       |          | learningwithsupervisedobjectives. |                  |          | Inaseparateeffort,a |                 |          |
establishedobjectdetectionbaselines(Renetal.,2015;Red-
zero-shotvideogamebugdetectionmethod(Taesirietal.,
monetal.,2016)fromtheAzuremachinelearningplatform
2022)utilizedinductivebiasfromalargemultimodallan-
(AzureAutoML).Wesummarizeourcontributionpointsas
|     |     |     |     |     |     |     | guage model | to mitigate | reliance | on  | supervised | training |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | -------- | --- | ---------- | -------- |
follows:
samples.

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
3.PROBLEMDEFINITION
Co-Supervised Learning
| Followinganobjectdetectionobjective, |     |     |     |     | ourprimaryaim |     | Labeled images  |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | ------------- | --- | --------------- | --- | --- | --- | --- |
from other titles
istoaccuratelylocalizeandclassifyvisualbugsasobjects
| withinanimage. |     | Consequently,theproblemisformulated |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Embedding
as the minimization of a multi-task loss function, which Labeled images  ViT Faster R-CNN Visual Bug
|          |       |               |             |     |     |          | from target title |     |     | Detection Model | Detections |
| -------- | ----- | ------------- | ----------- | --- | --- | -------- | ----------------- | --- | --- | --------------- | ---------- |
| balances | these | two essential | components. |     | We  | assume a |                   |     |     |                 |            |
Weight β
regionproposalapproach(Renetal.,2015)wheretheloss
Latent ReconstructionLoss
| functioncomprisesaweightedsumoftheclassificationloss, |                                    |                                      |         |       |     |           | Self-Supervised Learning |                |                   |     |     |
| ----------------------------------------------------- | ---------------------------------- | ------------------------------------ | ------- | ----- | --- | --------- | ------------------------ | -------------- | ----------------- | --- | --- |
| L                                                     | , andtheboundingboxregressionloss, |                                      |         |       | L   | , applied | Un l a b el e            | d   im a g es  |                   |     |     |
| cls                                                   |                                    |                                      |         |       | loc |           |                          |                | Targe t  F rozen  |     |     |
|                                                       |                                    |                                      |         |       |     |           | f r o m   a              | ll  t itl e s  | V i T             |     |     |
| to both                                               | a                                  | Region Proposal                      | Network | (RPN) | and | the final |                          |                |                   |     |     |
| detectionhead.                                        |                                    | Formally,foragivenregionproposal,the |         |       |     |           |                          |                |                   |     |     |
totallossisdefinedas:
Figure2.AblockdiagramfortheCo-finetuningmethoddesign.It
involvestwomainobjectives:aself-supervisedtargetdistillation
|      |     | 1        |        | 1   |              |      | objectiveandaco-supervisedobjectdetectionobjective. |     |     |     |     |
| ---- | --- | -------- | ------ | --- | ------------ | ---- | --------------------------------------------------- | --- | --- | --- | --- |
|      |     | (cid:88) | ,p∗)+λ |     | (cid:88) p∗L | ,t∗) |                                                     |     |     |     |     |
| L od | =   | L cls (p | i      |     | loc          | (t i |                                                     |     |     |     |     |
|      | N   |          | i      | N   | i            | i    |                                                     |     |     |     |     |
|      |     | cls      |        | loc |              |      |                                                     |     |     |     |     |
|      |     | i        |        |     | i            |      |                                                     |     |     |     |     |
(1)
|     |     |     |     |     |     |     | WeadoptaFasterR-CNN |     | (Renetal.,2015)objectdetection |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | ------------------------------ | --- | --- |
architecturewithaVisionTransformer(ViT)(Dosovitskiy
Here,ireferstotheindexofananchor(fortheRPN)ora
|     |     |     |     |     |     |     | etal.,2020)backbone. |     | TheFasterR-CNNdetectionhead |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --------------------------- | --- | --- |
regionofinterest(forthedetectionhead).p i isthepredicted includesaregionproposalnetwork, aclassificationhead,
| probabilityofanchoribeinganobject,whilep∗ |     |     |     |     | isitscorre- |     |                        |     |                           |     |     |
| ----------------------------------------- | --- | --- | --- | --- | ----------- | --- | ---------------------- | --- | ------------------------- | --- | --- |
|                                           |     |     |     |     | i           |     | andaboxregressionhead. |     | AsperEquation1,weutilizea |     |     |
spondingground-truthlabel(1forpositive,0fornegative).
|     |     |     |     |     |     |     | cross-entropylossfortheL |     | term,andasmoothL1loss |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --------------------- | --- | --- |
cls
| t representsthepredictedboundingboxregressionoffsets |     |     |     |     |     |     | fortheL | term. |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ----- | --- | --- | --- |
| i                                                    |     |     |     |     |     |     | loc     |       |     |     |     |
foranchori,andt∗denotestheground-truthboundingbox
i
Thisco-finetuningalgorithmincludesbothco-supervised
| regressionoffsetsforapositiveanchori.   |     |     |     |     | N cls isthemini- |     |                                               |     |     |     |        |
| --------------------------------------- | --- | --- | --- | --- | ---------------- | --- | --------------------------------------------- | --- | --- | --- | ------ |
|                                         |     |     |     |     |                  |     | learningandself-supervisedlearningcomponents. |     |     |     | Forthe |
| batchsizeutilizedforclassification,andN |     |     |     |     | isthenumber      |     |                                               |     |     |     |        |
loc
of anchor locations used for localization. Finally, λ is a co-supervisedlearningpart,therearetwotypesoflabeled
|     |     |     |     |     |     |     | images: onefromthetargetgametitleandtheotherfrom |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
balancingweightusedtonormalizethecontributionsofthe
|     |     |     |     |     |     |     | differentgametitles. |     | Labeledimagesfrommultipletitles |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------------------------------- | --- | --- |
classificationandlocalizationlosses.
canincreasethediversityofmulti-framebugsandenhance
|     |     |     |     |     |     |     | performance. | The | labeled images | from the target | down- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------------- | --------------- | ----- |
4.METHODOLOGY
streamtitleandothertitlesshouldhavedifferentimportance
|         |          |              |     |         |        |          | duringthetrainingphase. |     | Therefore,weassignaweightα |     |     |
| ------- | -------- | ------------ | --- | ------- | ------ | -------- | ----------------------- | --- | -------------------------- | --- | --- |
| In this | section, | we introduce | the | details | of our | proposed |                         |     |                            |     |     |
tothelabeledimagesfromothertitles,whichisreflectedin
| hybridco-finetuningmethod. |     |     | Figure2depictsthedesign |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
thelosscalculation.
| of our                | proposed | method,                            | highlighting |     | two main | learning |     |     |     |     |     |
| --------------------- | -------- | ---------------------------------- | ------------ | --- | -------- | -------- | --- | --- | --- | --- | --- |
| objectives,including: |          | 1)co-supervisedlearning,and2)self- |              |     |          |          |     |     |     |     |     |
supervisedlearning. Thisdesignaimstoharnesslearning 4.2.Self-supervisedLearningModule
signalsfrombothlabeledandunlabeleddatatoenhancethe
Toleverageadditionallearningsignalsfromunlabeleddata
| detectionperformance. |     |     | Weoutlineeachoftheselearning |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
thatcouldbecollectedatacheapercostincomparisonto
objectivesasfollows. labeled the one, we propose a Self-supervised Learning
(SSL)modulethatworksasanauxiliarylosssignalgener-
4.1.Co-supervisedLearningModule ator during training time. Our SSL design is inspired by
Theobjectiveofthislearningmoduleistoutilizelabeled theimageMaskedAutoencoders(MAE)(Heetal.,2022)
andImage-basedJoint-EmbeddingPredictiveArchitecture
| data | from | the downstream | gaming | title | (i.e., the | one un- |     |     |     |     |     |
| ---- | ---- | -------------- | ------ | ----- | ---------- | ------- | --- | --- | --- | --- | --- |
(I-JEPA)(Assranetal.,2023),intermsofusingreconstruc-
derinvestigation)andfromothergamingtitlesthatmight
still provide relevant learning signals about the notion of tionaftermaskingasatargetandperformingreconstruction
|                        |     |     |                           |     |     |     | onthelatentspace,respectively. |     |     | Yet,ourapproachdiffers |     |
| ---------------------- | --- | --- | ------------------------- | --- | --- | --- | ------------------------------ | --- | --- | ---------------------- | --- |
| bugsthatweaimtodetect. |     |     | Thus,wecombinelabeleddata |     |     |     |                                |     |     |                        |     |
inusingaseparatetargetencoderfromtheoneusedbythe
intotwogroups,includingthedownstreamandtheco-title.
architecture,whichalsoactsasadistillationtargetduring
Duringtraining,wesamplemini-batchesfromeachgroup
|     |          |            |           |     |          |          | reconstruction. | Figure | 3 illustrates | the workflow | of our |
| --- | -------- | ---------- | --------- | --- | -------- | -------- | --------------- | ------ | ------------- | ------------ | ------ |
| and | fuse the | supervised | loss (see | Eq. | 1) using | a weight |                 |        |               |              |        |
hyperparameterα: SSL module. We combine images from all titles, includ-
|     |     |     |     |     |     |     | ingthedownstreamone,toformanunlabeleddataset. |     |     |     | For |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- |
L =Ldownstream+αLco−title (2) a given unlabeled image sample, we divide it into equal-
|     |     | cosup | od  |     | od  |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
|              |     |          |     |     |           |     | we developed                                    | using | the      | Unreal | Engine    | and  | one released |
| ------------ | --- | -------- | --- | --- | --------- | --- | ----------------------------------------------- | ----- | -------- | ------ | --------- | ---- | ------------ |
|              |     | Patch    |     |     |           |     | Xbox game.                                      | We    | followed | an     | automated | data | collection   |
| Masked Frame |     | Encoding |     |     |           |     |                                                 |       |          |        |           |      |              |
|              |     |          |     |     | Predicted |     | fromexperimentalgamesusingtheUnrealCVplugin(Qiu |       |          |        |           |      |              |
Latent
Student Mask & Yuille, 2016) and manual collection from the released
|     | Encoder |     |     | Decoder |     |     | Xboxgame. | Weoutlinethegamesasfollows: |     |     |     |     |     |
| --- | ------- | --- | --- | ------- | --- | --- | --------- | --------------------------- | --- | --- | --- | --- | --- |
MSE
|     |     |     |     |     |     | Loss | • GiantMap: |     | Thisgamesimulatesalargecityparkarea |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ----------------------------------- | --- | --- | --- | --- |
Target
|     |     |     |         |        | Latent |     | featuringopen-worldcharacteristicswithtrails,play- |         |             |     |             |     |             |
| --- | --- | --- | ------- | ------ | ------ | --- | -------------------------------------------------- | ------- | ----------- | --- | ----------- | --- | ----------- |
|     |     |     | Target  | Filter |        |     |                                                    |         |             |     |             |     |             |
|     |     |     |         | \\     |        |     | grounds,                                           | service | facilities, |     | and natural |     | scenery. We |
|     |     |     | Encoder | Masked |        |     |                                                    |         |             |     |             |     |             |
|     |     |     |         | Stop   |        |     | scatter3Dassetsaroundtheparkandrandomlyinject      |         |             |     |             |     |             |
Gradient
|     | RGB Frame |     |     |     |     |     | visualbugsintoacertainportionofthem. |     |     |     |     |     | Representa- |
| --- | --------- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- | ----------- |
tiveframesfromGiantMaparepresentedinFigure4.
Figure3.Illustrationforourproposedself-supervisedobjective. • HighRise:ThisgameispartoftheShootergamedemo
Wefollowalatentmaskedautoencoderwithatargetdistillation from Unreal Engine. It simulates a futuristic indoor
| criterion, | where an | input frame | is  | patchified | and masked, | then |     |     |     |     |     |     |     |
| ---------- | -------- | ----------- | --- | ---------- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
environmentofatwo-storybuilding.HighRiseisafast-
wefeedtheoriginalversionintoatargetencoderandthemasked
pacedshooterthatshowcasesadvancedarchitectural
onetoourstudentencoder,finally,wecalculatethereconstruction
|     |     |     |     |     |     |     | designsanddynamiclightingeffects. |     |     |     |     | Representative |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | -------------- | --- |
erroronthelatentspace,mainlyconsideringmaskedpatches.
framesfromthisgameareillustratedinFigure5.
sizedpatches(similartotheViT(Dosovitskiyetal.,2020) • CombatGame: Thisisarealcombat-orientedAAA
|            |         |        |         |         |               |     | game | that highlights |     | tactical | engagements, |     | weapon- |
| ---------- | ------- | ------ | ------- | ------- | ------------- | --- | ---- | --------------- | --- | -------- | ------------ | --- | ------- |
| approach), | then we | create | another | replica | by performing |     |      |                 |     |          |              |     |         |
patch-wiserandommasking(withamaskingratioof0.75) based combat, and rugged terrain. We do not show
framesfromthisenvironmentforprivacyreasons.
| on it. We | feed the | original | image | to  | the target encoder, |     |     |     |     |     |     |     |     |
| --------- | -------- | -------- | ----- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
whichiskeptfrozenduringtraining,andthemaskedoneto
| thestudentencoderusedinsideourarchitecture. |     |     |     |     | Insteadof |     |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
calculatingthereconstructionlossonthepixelspaceasin
MAEs(Heetal.,2022),wetargettoreconstructthemasked
patchesonthelatentspaceofthetargetencoder,similartoI-
| JEPA(Assranetal.,2023). |     |     | Afterencodingallthepatchesin |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
theinputimageusingthestudentencoder,includingmasked
ones,wereconstructthemaskedpatchesusingamaskde-
coder. Finally,wematchthereconstructedlatentswiththe
targetonesfromthetargetencodertocalculateourSSLloss.
|     |     |     |     |     |     |     | Figure4. | RepresentativeframesfromtheGiantMapgame. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------------------------------------- | --- | --- | --- | --- | --- |
Wenotethatweonlyfocusourlatentreconstructionlosson
themaskedpatcheswithoutconsideringtheunmaskedones
byfilteringthemoutofthelosscomputation.
WeutilizeMeanSquaredError(MSE)tocalculatethelatent
constructionerror,andwecombinetheSSLlosstermwith
theco-supervisedoneusingahyperparameterβ.
|     | L   | =L  |       | +βMSE |     | (3) |     |     |     |     |     |     |     |
| --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | CFT |     | cosup |       | ssl |     |     |     |     |     |     |     |     |
5.EXPERIMENTALEVALUATION
|                  |           |           |          |            |                  |     | Figure5.   | RepresentativeframesfromtheHighRisegame. |             |     |        |            |          |
| ---------------- | --------- | --------- | -------- | ---------- | ---------------- | --- | ---------- | ---------------------------------------- | ----------- | --- | ------ | ---------- | -------- |
| In this section, | we        | introduce | details  | of         | our experimental |     |            |                                          |             |     |        |            |          |
| evaluation,      | including | the       | dataset, | baselines, | experiments,     |     |            |                                          |             |     |        |            |          |
|                  |           |           |          |            |                  |     | This study | addresses                                | multi-frame |     | visual | artifacts, | specifi- |
andresults.
callyLevelofDetail(LOD)popsandcullingpops.AnLOD
popoccurswhenanobject’svisualrepresentation,suchas
5.1.DataCollectionandSplittingStrategy
itstextureorgeometricdetail,undergoesanabruptchange
Wecollecteddatasetsfromthreedistinctvideogametitles, asaviewer’sdistancetoitvaries,resultinginadiscontin-
eachofferinguniquevisualstylesandgameplaydynamics. uousLODtransition. Conversely,acullingpopmanifests
The selected titles include two experimental games that as the sudden appearance or disappearance of an object

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
withintherenderedscene,typicallyinresponsetochanges arestackedtoformanewthree-channelimagesuitablefor
inviewerproximityororientation. Illustrativeexamplesof input into the Azure AutoML model.The process is fur-
bothcullingandLODpopsareprovidedinFigure6. ther described as follows: four RGB frames-rgb 0 , rgb 1 ,
|                                                    |     |     |     |                        |     |     | rgb ,andrgb | -areused,withthepopbugoccurringinrgb |              |     |                           |           | .   |
| -------------------------------------------------- | --- | --- | --- | ---------------------- | --- | --- | ----------- | ------------------------------------ | ------------ | --- | ------------------------- | --------- | --- |
| Thedatasetforeachgametitlewaspartitionedintotrain- |     |     |     |                        |     |     | 2           | 3                                    |              |     |                           |           | 2   |
|                                                    |     |     |     |                        |     |     | Each RGB    | image                                | is converted |     | to grayscale,             | resulting | in  |
| ing,validation,andtestingsets.                     |     |     |     | Thetrainingsetincludes |     |     |             |                                      |              |     |                           |           |     |
|                                                    |     |     |     |                        |     |     | gray ,gray  | ,gray                                | ,andgray     |     | . Then,theabsolutediffer- |           |     |
| approximately4,000pops(GiantMap:                   |     |     |     | 4503,CombatGame:       |     |     | 0           | 1                                    | 2            | 3   |                           |           |     |
encesbetweenconsecutivegrayscaleimagesarecomputed:
| 4661, Highrise: |     | 2866), while | both | validation |     | and testing |        |       |       |         |         |       |        |
| --------------- | --- | ------------ | ---- | ---------- | --- | ----------- | ------ | ----- | ----- | ------- | ------- | ----- | ------ |
|                 |     |              |      |            |     |             | diff = | |gray | −gray | |, diff | = |gray | −gray | |, and |
setseachcontainroughly500pops(Validation: GiantMap: 1 1 0 2 2 1
|                  |     |               |           |              |      |            | diff =          | |gray | −gray                               | | where | |·| denotes | the | absolute |
| ---------------- | --- | ------------- | --------- | ------------ | ---- | ---------- | --------------- | ----- | ----------------------------------- | ------- | ----------- | --- | -------- |
| 500,CombatGame:  |     | 543,Highrise: |           | 351;Testing: |      | GiantMap:  | 3               |       | 3                                   | 2       |             |     |          |
|                  |     |               |           |              |      |            | valueoperation. |       | Thesethreedifferentimagesarestacked |         |             |     |          |
| 503, CombatGame: |     | 507,          | Highrise: | 352).        | Full | details on |                 |       |                                     |         |             |     |          |
toformanewthree-channelimage,denotedasimg,which
| popandimagecountsforallfourtitlesareinTable1. |     |     |     |     |     | Note |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
issubsequentlyusedasinputforboththeAzureAutoML
thatimagecountsmaydifferfrompopcounts,asoneimage
|                         |     |     |                          |     |     |     | objectdetectionmodelandourproposedCFTmodel. |     |     |     |     |     | This |
| ----------------------- | --- | --- | ------------------------ | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | ---- |
| cancontainmultiplepops. |     |     | Eachpopwasannotatedbyone |     |     |     |                                             |     |     |     |     |     |      |
imagepreparationstepforthemodelinputisalsoillustrated
person,verifiedbyasecond,andadjudicatedbyathirdin
inFigure7.
| casesofdisagreement.                 |     | Additionally, |     | 2,000unlabeledim- |               |     |     |     |     |     |     |     |     |
| ------------------------------------ | --- | ------------- | --- | ----------------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ageswererandomlysampledpergametitle. |     |               |     |                   | Fortrainingon |     |     |     |     |     |     |     |     |
5.3.ResearchQuestions
eachtargetgame,theothertwogameswillserveasco-titles.
Ourexperimentalevaluationsetupaimstoassessthediffer-
5.2.ComparisonBaselines entaspectsoftheproposedhybridco-finetuningmethodby
answeringthefollowingresearchquestions.
WeusetheobjectdetectionmodelsprovidedbyAzureAu-
| toMLasourbaseline. |     | AzureAutoMLisacloud-basedser- |     |     |     |     |          |     |      |            |     |           |         |
| ------------------ | --- | ----------------------------- | --- | --- | --- | --- | -------- | --- | ---- | ---------- | --- | --------- | ------- |
|                    |     |                               |     |     |     |     | • [RQ1]: | How | does | the visual | bug | detection | perfor- |
vicewithinMicrosoftAzure’sAutomatedMachineLearn-
ing suite that enables users to automatically build, train, mance of the proposed method compare to well-
establishedobjectdetectionbaselinesusingtheevalua-
| anddeploymachinelearningmodels, |     |     |     | includingthosefor |     |     |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tiongamingenvironments?
| object detection.             |     | Azure | AutoML                | supports | two | types of |          |      |       |        |          |        |          |
| ----------------------------- | --- | ----- | --------------------- | -------- | --- | -------- | -------- | ---- | ----- | ------ | -------- | ------ | -------- |
| objectdetectionarchitectures: |     |       | atwo-stageFasterR-CNN |          |     |          |          |      |       |        |          |        |          |
|                               |     |       |                       |          |     |          | • [RQ2]: | What | would | be the | suitable | mixing | strategy |
detector(Renetal.,2015)andasingle-stageYOLOv5de-
whenlearningfrommixedgamingdata?
| tector (Redmon |     | et al., 2016; | Jocher | et  | al., 2020). | When |     |     |     |     |     |     |     |
| -------------- | --- | ------------- | ------ | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
running object detection tasks, Azure AutoML automati- • [RQ3]: Whatistheimpactofdifferentbuildingblocks
callyexploresmultiplevariantsofthesemodelsandselects intheproposedhybridco-finetuningmethod?
thebest-performingmodelbasedonavalidationdatasetand
|             |        |         |          |        |          |       | • [RQ4]: |     | Could the | proposed | hybrid | co-finetuning |     |
| ----------- | ------ | ------- | -------- | ------ | -------- | ----- | -------- | --- | --------- | -------- | ------ | ------------- | --- |
| a specified | target | metric. | We refer | to the | selected | Azure |          |     |           |          |        |               |     |
AutoML variant as “AutoML” in our result reporting for method generalize its performance to other types of
visualbugsingames?
brevity. Inourcase,thetargetmetricismeanaveragepre-
| cision (mAP) | (Ren     | et al.,      | 2015). | Thus, | our    | comparison |     |     |     |     |     |     |     |
| ------------ | -------- | ------------ | ------ | ----- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
| baseline     | is not a | single fixed | model, | but   | rather | the result |     |     |     |     |     |     |     |
5.4.Results&Discussion
ofanautomatedsearchacrossstate-of-the-artdeeplearn-
Inthissection,wepresentanddiscusstheevaluationresults
| ingarchitectures. |     | Allhyperparametersaretunedusingthe |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
validationdata,andthefinalmodelischosenbasedonits answeringthedefinedresearchquestions.
performanceagainstthemAPmetric.
5.4.1.VISUALBUGDETECTIONPERFORMANCE
| For multi-frame |     | pop data, | the pop | bug | only | becomes ap- |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
COMPARISONWITHBASELINES:
| parent when | analyzing | sequences |     | of frames. |     | Therefore, |     |     |     |     |     |     |     |
| ----------- | --------- | --------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
using a single image as input is insufficient for detecting WeanswerRQ1byassessingtheCFTmodelperformance
comparedtoAzureAutoMLbaselinesintermsofkeyeval-
theissue. However,AzureAutoMLobjectdetectionmodels
uationmetrics—meanAveragePrecision(mAP)(Evering-
| require input | images | to have | exactly | three | channels. | To  |     |     |     |     |     |     |     |
| ------------- | ------ | ------- | ------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
address this, we construct a three-channel image using a hametal.,2010)andF1score (Goutte&Gaussier,2005).
AmodelisconsideredeffectiveifitachieveshighermAP
| grayscaledifferencestackingapproach. |         |     |         |       | Theideaistouse |             |        |        |          |           |          |      |        |
| ------------------------------------ | ------- | --- | ------- | ----- | -------------- | ----------- | ------ | ------ | -------- | --------- | -------- | ---- | ------ |
|                                      |         |     |         |       |                |             | and F1 | scores | than the | baseline. | However, | even | if the |
| a sequence                           | of four | RGB | images, | where | the            | pop bug oc- |        |        |          |           |          |      |        |
CFTmodeldeliverscomparableperformance,itmaystill
| curs in the | third         | frame. These | four  | RGB        | images | are first    |               |     |                |               |     |              |       |
| ----------- | ------------- | ------------ | ----- | ---------- | ------ | ------------ | ------------- | --- | -------------- | ------------- | --- | ------------ | ----- |
|             |               |              |       |            |        |              | be preferable |     | if it requires | significantly |     | less labeled | data. |
| converted   | to grayscale. |              | Then, | we compute |        | the absolute |               |     |                |               |     |              |       |
differencesbetweenconsecutivegrayscaleframestocap- Thisconsiderationisparticularlyimportantinthegaming
|                                |     |     |     |                      |     |     | domain,                         | where | acquiring | labeled | bug data             | is  | both time- |
| ------------------------------ | --- | --- | --- | -------------------- | --- | --- | ------------------------------- | ----- | --------- | ------- | -------------------- | --- | ---------- |
| turemotionorchangesacrosstime. |     |     |     | Thesedifferentimages |     |     |                                 |       |           |         |                      |     |            |
|                                |     |     |     |                      |     |     | consumingandresource-intensive. |       |           |         | Therefore,amodelthat |     |            |

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
|     | Culling Pop Bug Example |     | Loss Of Detail (LOD) Pop Bug Example |     |
| --- | ----------------------- | --- | ------------------------------------ | --- |
Figure6.TwoexamplesofpopvisualbugsfromtheGiantMapgame.Ontheleft,acullingpopbugexample.Ontheright,aLoDpop
example.
|     | Training | Validation | Testing | Numberof |
| --- | -------- | ---------- | ------- | -------- |
GameTitle
UnlabeledImages
|            | #ofpop #ofimage | #ofpop #ofimage | #ofpop #ofimage |      |
| ---------- | --------------- | --------------- | --------------- | ---- |
| GiantMap   | 4503 4491       | 500 500         | 503 499         | 2000 |
| CombatGame | 4661 1574       | 547 146         | 507 247         | 2000 |
| Highrise   | 2866 2856       | 351 347         | 352 345         | 2000 |
Table1. Train-Validation-Testdatasplitsandnumberofunlabeledsamplesacrosstheexperimentalgamingdatasets.
RGB
image
Step 1: Grayscale
image
Step 2: Absolute
difference image
Step 3: Combined
image
Figure7.Anillustrationoftheinputslidingwindowpreparationprocedure.RGBimagesarefirstconvertedtograyscale,thenabsolute
deltasarecomputed,andfinally,thesedeltasarecombinedintoathree-channelimage.

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
maintainscompetitiveperformancewhilereducingtheneed strategy,determiningwhetherafixedoradaptiveweighting
forlabeleddataoffersasubstantialpracticaladvantage. approachyieldssuperiorresultsandifmodelperformance
|     |     |     |     |     |     |     | issensitivetothesechoices. |     |     |     | Thisinvestigationwillclarify |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | ---------------------------- | --- | --- |
AzureAutoMLautomaticallyevaluatesbothFasterR-CNN
|     |     |     |     |     |     |     | whether | the | mixing | strategy | should | be considered | a criti- |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ------ | -------- | ------ | ------------- | -------- |
andYOLOV5forbugdetectionandselectsthebestper-
|                                             |     |     |     |     |     |       | calhyperparameterfortheCFTmodel. |     |     |     |     | Wekeptallother |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ----- | -------------------------------- | --- | --- | --- | --- | -------------- | --- |
| formingbaselinebasedonthevalidationdataset. |     |     |     |     |     | Weuse |                                  |     |     |     |     |                |     |
algorithmicparametersfixedandsystematicallyvariedthe
| mean average | precision |     | (mAP) with | an intersection |     | over |     |     |     |     |     |     |     |
| ------------ | --------- | --- | ---------- | --------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
weightsassignedtotheco-supervisedlearning(CSL)and
| union (IoU) | threshold |     | of 0.5 for | pop bug | detection. | Ad- |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ---------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
self-supervisedlearning(SSL)components,denotedasα
| ditionally,    | we measure |     | the F1 score | with   | IoU=0.5     | and a |                                |     |     |     |                     |     |     |
| -------------- | ---------- | --- | ------------ | ------ | ----------- | ----- | ------------------------------ | --- | --- | --- | ------------------- | --- | --- |
|                |            |     |              |        |             |       | andβ,respectively(seeFigure2). |     |     |     | Todeterminetheopti- |     |     |
| classification | threshold  |     | of 0.25. We  | select | a threshold | of    |                                |     |     |     |                     |     |     |
malvaluesforthesehyperparameters,weconductedagrid
0.25forresultcomparisonbecauserecallisusuallymore
searchoverapredefinedrangeofαandβ,spanningfrom
| importantforvisualbugclassification. |     |     |     | Theresultsforthese |     |     |      |        |            |     |               |             |     |
| ------------------------------------ | --- | --- | --- | ------------------ | --- | --- | ---- | ------ | ---------- | --- | ------------- | ----------- | --- |
|                                      |     |     |     |                    |     |     | 0 to | 0.6 in | increments | of  | 0.1. The best | combination | was |
metrics,basedonthetestingdatasetforAzureAutoMLand
|     |     |     |     |     |     |     | selected | based | on  | performance | on the | validation | datasets |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | --- | ----------- | ------ | ---------- | -------- |
theco-finetuning(CFT)method,arepresentedinTable2.
acrossthreedistinctgametitles.
Inordertoperformastatisticalsignificancet-testformAP
Table4summarizestheresults,indicatingthattheoptimal
| and F1 metrics | for       | each   | pair, we     | normalized | each          | metric |                                                          |     |                                             |     |     |     |     |
| -------------- | --------- | ------ | ------------ | ---------- | ------------- | ------ | -------------------------------------------------------- | --- | ------------------------------------------- | --- | --- | --- | --- |
|                |           |        |              |            |               |        | β valueremainsrelativelyconsistentacrosstitles,centering |     |                                             |     |     |     |     |
| value for      | each game | title. | For example, |            | we normalized |        |                                                          |     |                                             |     |     |     |     |
|                |           |        |              |            |               |        | around0.2.                                               |     | Conversely,αdemonstratesgreatervariability, |     |     |     |     |
themAPvalues[0.662,0.938]fromdifferentalgorithmsto
suggestingitsoptimalvalueismoresensitivetoindividual
[0.413=0.662/(0.662+0.938),0.586=0.938/(0.662+
|                              |     |     |                         |     |     |     | game | title | characteristics. |     | The magnitude | of  | α generally |
| ---------------------------- | --- | --- | ----------------------- | --- | --- | --- | ---- | ----- | ---------------- | --- | ------------- | --- | ----------- |
| 0.938)]forgametitleGiantMap. |     |     | Thisnormalizationisnec- |     |     |     |      |       |                  |     |               |     |             |
exceedsβ,implyingtheCSLcomponentholdsamorein-
essarybecauseeachgametitlehasitsowntestingdataset,
|     |     |     |     |     |     |     | fluentialroleinbugpredictionperformance. |     |     |     |     | Thesefindings |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | ------------- | --- |
resultinginvariedscalesthatmakecross-titlecomparisons
suggestthatwhileβcanbefixedat0.2fornewtitles,careful
| incomparable. | TheresultsareshowninTable3. |      |            |              | Here,three |          |        |     |                  |     |             |             |      |
| ------------- | --------------------------- | ---- | ---------- | ------------ | ---------- | -------- | ------ | --- | ---------------- | --- | ----------- | ----------- | ---- |
|               |                             |      |            |              |            |          | tuning | of  | α is recommended |     | for dataset | adaptation. | This |
| samples       | were used,                  | with | each title | contributing |            | a single |        |     |                  |     |             |             |      |
insightcanstreamlinehyperparameteroptimizationwhen
| valuetothestatisticaltests. |     |     | ItcanbeseenfromTable3that |     |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
extendingthevisualbugdetectionframeworktonewgame
thedifferencebetweentheresultsfromAzureAutoMLand
titles.
CFTisstatisticallysignificantatthe0.05level,evenwith
50%trainingdatainCFT,indicatingthatCFTachievesbet-
|     |     |     |     |     |     |     |     | Title |     | mAP | F1  | β   | α   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
terresultsthanAzureAutoML.Furthermore,thedifference
| between | CFT using | the | full training | data | and 50% | of the |     |          |     |       |       |     |     |
| ------- | --------- | --- | ------------- | ---- | ------- | ------ | --- | -------- | --- | ----- | ----- | --- | --- |
|         |           |     |               |      |         |        |     | GiantMap |     | 0.941 | 0.890 | 0.3 | 0.4 |
trainingdataisnotstatisticallysignificant,suggestingthat
|     |     |     |     |     |     |     |     | CombatGame |     | 0.164 | 0.404 | 0.2 | 0.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----- | ----- | --- | --- |
evenwithlesstrainingdata,CFTcanstillproducecompa-
| rable results. | Additional |     | t-tests were | conducted |     | on these |     |          |     |       |       |     |     |
| -------------- | ---------- | --- | ------------ | --------- | --- | -------- | --- | -------- | --- | ----- | ----- | --- | --- |
|                |            |     |              |           |     |          |     | Highrise |     | 0.384 | 0.471 | 0.2 | 0.3 |
results,asshowninTable3.Itcanbeobservedthatreducing
the training dataset does not significantly degrade perfor- Table4.OptimalweightingschemesforCSLandSSLacrossex-
manceinmostcasesforCFTintermsofmAP.However, perimentalgamingenvironments.
whenthetrainingdatasetishalvedinAzureAutoML,the
performancedropsconsiderably.Incontrast,CFTmaintains
5.4.3.ABLATIONSTUDY:
betterperformanceintermsofmAPmetricscomparedto
theAzureAutoMLbaselinewhentrainedononlyhalfof
ToaddressRQ3,whichaimstoassesstheimpactoftheCFT
thedataset.
|     |     |     |     |     |     |     | model’s | constituent |     | components, | we  | conduct | an ablation |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | ----------- | --- | ------- | ----------- |
studyevaluatingthenecessityandcontributionofitscore
5.4.2.ASSESSINGTHEDATAMIXINGSTRATEGYFOR
|     |     |     |     |     |     |     | elements: |     | co-supervisedlearning(CSL)andself-supervised |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | -------------------------------------------- | --- | --- | --- | --- |
CO-FINETUNING:
|     |     |     |     |     |     |     | learning | (SSL). | This | involves | incrementally |     | adding CSL |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---- | -------- | ------------- | --- | ---------- |
TheCFTmodelincorporatesbothco-supervisedandself- andSSLcomponentstodeterminetheirinfluenceonperfor-
|            |           |          |            |     |             |     | mance. | Additionally,weinvestigatetheeffectofdifferent |     |     |     |     |     |
| ---------- | --------- | -------- | ---------- | --- | ----------- | --- | ------ | ---------------------------------------------- | --- | --- | --- | --- | --- |
| supervised | learning. | However, | optimizing |     | the balance | of  |        |                                                |     |     |     |     |     |
thesecomponents,specificallytheirweightingduringtrain- backbonearchitectures,specificallyViT-Base(Dosovitskiy
etal.,2020)andResNet-50(Heetal.,2016),toassessthe
| ing, remainsanopenquestionasindicatedinRQ2. |     |     |     |     |     | This |     |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
model’ssensitivitytobackbonechoiceandidentifyoptimal
studyinvestigatestheimpactofexplicitlytuningthismix-
ingstrategyonmodelperformance. Anunsuitableweight- architecturesforthegiventasks. Finally,weexploretheim-
pactofvarioustargetencoderswithintheSSLcomponent,
ingschemecouldeitherunderutilizelabeleddataorfailto
fully leverage self-supervised learning benefits. Through evaluating pretrained encoders from state-of-the-art self-
simulations,weaimtounderstandtheroleofthismixing supervisedlearningmethodssuchasDINOv1(Caronetal.,
2021),DINOv2(Oquabetal.,2023),MAE(Heetal.,2022),

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
|     |     |     | mAP |     |     |     | F1  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Dataset
|     |            | AutoML      | CFT   |       |       | AutoML |       |       | CFT   |     |     |
| --- | ---------- | ----------- | ----- | ----- | ----- | ------ | ----- | ----- | ----- | --- | --- |
|     |            | 100% 50%    | 100%  | 50%   | 100%  |        | 50%   | 100%  | 50%   |     |     |
|     | Giantmap   | 0.662 0.560 | 0.938 | 0.945 | 0.747 |        | 0.777 | 0.976 | 0.969 |     |     |
|     | CombatGame | 0.159 0.106 | 0.164 | 0.158 | 0.418 |        | 0.337 | 0.445 | 0.450 |     |     |
|     | Highrise   | 0.209 0.202 | 0.349 | 0.235 | 0.312 |        | 0.355 | 0.533 | 0.455 |     |     |
Table2.VisualbugdetectionperformanceresultscomparedtothebestperformingAzureAutoMLbaselineusingfullandhalfthesizeof
thetrainingdatasets.
|                         |     |     |         | We        | also   | experimented |           | with        | the widely | adopted    | ResNet-     |
| ----------------------- | --- | --- | ------- | --------- | ------ | ------------ | --------- | ----------- | ---------- | ---------- | ----------- |
| Metric T-test           |     |     | P-value |           |        |              |           |             |            |            |             |
|                         |     |     |         | 50        | (He et | al., 2016)   | backbone. |             | It         | is crucial | to note the |
| AutoML(100%)vsCFT(100%) |     |     | 0.007   |           |        |              |           |             |            |            |             |
|                         |     |     |         | differing |        | input        | image     | dimensions: |            | 600 × 600  | pixels for  |
AutoML(100%)vsCFT(50%) 0.026 ResNet-50versus224×224pixelsforViT.Thecorrespond-
mAP
| CFT(100%)vsCFT(50%) |     |     | 0.054 |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
ingperformancemetrics,includingmeanAveragePrecision
| AutoML(50%)vsCFT(50%)     |     |     | 0.009 |                                       |     |     |     |     |     |     |           |
| ------------------------- | --- | --- | ----- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --------- |
|                           |     |     |       | (mAP)andF1score,arepresentedinTable6. |     |     |     |     |     |     | Acompari- |
| AutoML(100%)vsAutoML(50%) |     |     | 0.007 |                                       |     |     |     |     |     |     |           |
sonoftheseresultswiththoseobtainedusingtheViT-base
AutoML(100%)vsCFT(100%) 0.004 backbone(Table2)revealsrelativelyminordifferencesin
AutoML(100%)vsCFT(50%) 0.001 mAPandF1score.However,themetricsforeachgametitle
F1
CFT(100%)vsCFT(50%) 0.079 appear slightly better when using the ViT-base backbone
AutoML(50%)vsCFT(50%) 0.000 comparedtoResNet-50. Torigorouslyevaluatethisobser-
AutoML(100%)vsAutoML(50%) 0.965 vation,weconductedapairedt-testonthemAPscoresob-
|     |     |     |     | tainedfrombothbackbones. |     |     |     | Theresultingp-valueof0.041 |     |     |     |
| --- | --- | --- | --- | ------------------------ | --- | --- | --- | -------------------------- | --- | --- | --- |
indicatesthattheperformancedifferenceisstatisticallysig-
Table3.Statisticalsignificancet-testanalysiscomparingtheCFT
|     |     |     |     | nificant | atthe | conventionalp-value=0.05threshold. |     |     |     |     | This |
| --- | --- | --- | --- | -------- | ----- | ---------------------------------- | --- | --- | --- | --- | ---- |
methodwiththebestperformingbaselineselectedbyAzureAu-
findingsuggeststhattheViT-basebackboneyieldssuperior
toMLusingfullandhalfthesizeofthetrainingdata.
visualbugdetectionperformancerelativetoResNet-50,re-
inforcingitspotentialasamoreeffectivearchitecturefor
thistask.
andSAM(Kirillovetal.,2023),allbasedontheViT-Base
|     |     |     |     | To  | evaluate | the | individual | contributions |     | of CSL | and SSL |
| --- | --- | --- | --- | --- | -------- | --- | ---------- | ------------- | --- | ------ | ------- |
architecture. Thisanalysiswillclarifyhowtargetencoder
|     |     |     |     | to  | visual | bug detection, |     | we  | conducted | an ablation | study |
| --- | --- | --- | --- | --- | ------ | -------------- | --- | --- | --------- | ----------- | ----- |
selectioninfluencesthequalityoflearnedrepresentations
andoveralleffectiveness. usingaResNet-50backbone. WeassessedtheCFTmodel’s
|     |     |     |     | performance |     | across | four | configurations: |     | with | both CSL |
| --- | --- | --- | --- | ----------- | --- | ------ | ---- | --------------- | --- | ---- | -------- |
andSSLenabled,withonlyCSL,withonlySSL,andwith
neither.
mAP
F1
| 0.35 |     |     |     | Table     | 6 summarizes |             | these | results, | where     | ”True” | denotes    |
| ---- | --- | --- | --- | --------- | ------------ | ----------- | ----- | -------- | --------- | ------ | ---------- |
|      |     |     |     | inclusion |              | and ”False” |       | denotes  | exclusion | of a   | component. |
Thehighestperformance,intermsofbothmeanAverage
0.30
Precision(mAP)andF1score,isobservedwhenbothCSL
|     |     |     |     | andSSLareenabled. |     |     | Conversely,theabsenceofbothcom- |     |     |     |     |
| --- | --- | --- | --- | ----------------- | --- | --- | ------------------------------- | --- | --- | --- | --- |
erocS 0.25
ponentsyieldsthelowestperformance,underscoringtheir
collectiveimportance.
0.20
Interestingly,enablingonlySSLdoesnotsignificantlyim-
|     |     |     |     | prove | performance |     | over | the | baseline | (neither | component |
| --- | --- | --- | --- | ----- | ----------- | --- | ---- | --- | -------- | -------- | --------- |
0.15
enabled),suggestingthatSSLalonemaybeinsufficientin
|      |            |            |     | this                                                 | context. | However, |     | the inclusion |     | of CSL, | even with- |
| ---- | ---------- | ---------- | --- | ---------------------------------------------------- | -------- | -------- | --- | ------------- | --- | ------- | ---------- |
| 0.10 |            |            |     | outSSL,leadstosubstantialperformancegains,indicating |          |          |     |               |     |         |            |
|      | MAE Dinov1 | Dinov2 SAM |     |                                                      |          |          |     |               |     |         |            |
CSL’smoredominantroleinenhancingthemodel’scom-
Target Vision Encoder
|     |     |     |     | prehensionofvisualbugs. |     |     |     | Nevertheless,SSLprovidescom- |     |     |     |
| --- | --- | --- | --- | ----------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- |
plementarybenefits,asitsadditiontoaCSL-enabledmodel
Figure8.Assessingtheimpactofusingdifferenttargetvisionen-
codersontheCFTmethodperformance. furtherboostsperformance. Thisdemonstratesthatwhile

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
CSL is highly impactful independently, SSL contributes floating object artifacts and texture distortions. Floating
additionalvaluesynergistically. object bugs manifest when objects, typically expected to
restonasurface,appearsuspendedaboveit,creatingavis-
|          |     |     |              |     |             |     | ible gap.        | Texture bugs  | are categorized |               | as low-resolution |        |
| -------- | --- | --- | ------------ | --- | ----------- | --- | ---------------- | ------------- | --------------- | ------------- | ----------------- | ------ |
|          |     |     | P-Value(mAP) |     | P-Value(F1) |     |                  |               |                 |               |                   |        |
|          |     |     |              |     |             |     | texture defects, | characterized |                 | by blurriness | or lack           | of de- |
| MAEvsSAM |     |     |              | 0.0 | 0.0077      |     |                  |               |                 |               |                   |        |
tail,andstretchedtexturedistortions,wheretexturesappear
unnaturallyelongatedordistortedonanobject’ssurface.
| DINOv2vsSAM |     |     | 0.5036 |     | 0.6184 |     |     |     |     |     |     |     |
| ----------- | --- | --- | ------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
DINOv1vsMAE 0.3084 0.1834 We evaluated the CFT model on these single-frame bug
|             |     |     |     |     |        |     | categoriesusingtheGiantMapandHighRisedatasets. |     |     |     |     | The |
| ----------- | --- | --- | --- | --- | ------ | --- | ---------------------------------------------- | --- | --- | --- | --- | --- |
| DINOv2vsMAE |     |     |     | 0.0 | 0.0145 |     |                                                |     |     |     |     |     |
GiantMapdatasetincludes1,320training,120validation,
DINOv1vsDINOv2 0.0 0.0025 and960testingsamples. TheHighRisedatasetcomprises
|     |     |     |     |     |     |     | 3,326training, | 287validation, |     | and2,450testingsamples. |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------------- | --- | ----------------------- | --- | --- |
Table5.Statisticalsignificancet-testanalysisforusingdifferent Evaluation results, measured by mean Average Precision
targetvisionencodersintheself-supervisedlearningobjectiveof (mAP)onthetestsets,arepresentedinTable7. Asshown,
theCFTmethod.
CFTconsistentlyoutperformsAutoMLontheGiantMapti-
tleforbothfloatingandtexturesingle-framebugcategories,
|     |     |     |     |     |     |     | regardless | of the training | dataset | size (full | or half). | This |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------- | ------- | ---------- | --------- | ---- |
Wefurtherinvestigatetheimpactofdifferenttargetvision
encoders used in the SSL component of the CFT model. highlightsCFT’srobustnessandeffectivenessinthiscon-
|               |     |          |             |         |            |     | text. Conversely,fortheHighRisetitle,CFTandAutoML |     |     |     |     |     |
| ------------- | --- | -------- | ----------- | ------- | ---------- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- |
| Specifically, | we  | evaluate | four widely | adopted | pretrained |     |                                                   |     |     |     |     |     |
exhibitcomparableperformance,achievingsimilarresults,
| Vision Transformer |     | (ViT) | encoders: | DINOv1, |     | DINOv2, |     |     |     |     |     |     |
| ------------------ | --- | ----- | --------- | ------- | --- | ------- | --- | --- | --- | --- | --- | --- |
particularlywithinthetexturebugcategory.
| MAE, and    | SAM. | Each vision    | encoder | is        | seamlessly  | inte- |     |     |     |     |     |     |
| ----------- | ---- | -------------- | ------- | --------- | ----------- | ----- | --- | --- | --- | --- | --- | --- |
| grated into | the  | CFT framework. |         | To ensure | statistical | ro-   |     |     |     |     |     |     |
bustness,weperformfiveindependentsimulationrunsfor 6.IMPLEMENTATIONDETAIL
eachconfigurationusingthehalfHighrisetrainingdataset,
Modeltrainingwasprimarilyconductedonaserverfeatur-
| which accelerates |     | simulation | without | compromising |     | gen- |     |     |     |     |     |     |
| ----------------- | --- | ---------- | ------- | ------------ | --- | ---- | --- | --- | --- | --- | --- | --- |
inganNVIDIARTXA6000GPUwith49GBofmemory,
erality. Theresultsarevisualizedinthebox-and-whisker
|                      |     |     |              |     |               |     | runningUbuntu18.04. |     | Trainingspanned30epochswith |     |     |     |
| -------------------- | --- | --- | ------------ | --- | ------------- | --- | ------------------- | --- | --------------------------- | --- | --- | --- |
| plotsshowninFigure8. |     |     | FromFigure8, |     | weobservethat |     |                     |     |                             |     |     |     |
theMAEandDINOv1visionencodersyieldhighlyover- abaselearningrateof0.0001. Theper-devicebatchsize
|     |     |     |     |     |     |     | was initialized | to 10. | To achieve | a larger | effective | batch |
| --- | --- | --- | --- | --- | --- | --- | --------------- | ------ | ---------- | -------- | --------- | ----- |
lappingdistributionsinbothmAPandF1score,suggesting
sizewithoutexceedingGPUmemory,weutilizedgradient
| comparableperformance. |     |     | Tostatisticallyvalidatethisobser- |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accumulationwithanaccumulationstepof10,resultingin
vation,weperformatwo-samplet-testbetweentheresults
|     |     |     |     |     |     |     | aneffectivebatchsizeof100(10×10=100). |     |     |     | Whenadapting |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | ------------ | --- |
ofDINOv1andMAEmAP.Theresultingp-valueof0.3084
indicatesthattheperformancedifferencebetweenthesetwo to different hardware, the per-device batch size was ad-
justed,whilemaintaininganeffectivebatchsizeof100by
| vision encoders |     | is not statistically |     | significant | at  | the 0.05 |     |     |     |     |     |     |
| --------------- | --- | -------------------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- |
proportionallymodifyingtheaccumulationstep,ensuring
level. Incontrast,theperformanceofDINOv2andSAM
|          |            |        |          |           |     |     | consistenttrainingdynamics. |     | Foroptimization,theAdamW |     |     |     |
| -------- | ---------- | ------ | -------- | --------- | --- | --- | --------------------------- | --- | ------------------------ | --- | --- | --- |
| encoders | is notably | lower. | A t-test | comparing | MAE | and |                             |     |                          |     |     |     |
optimizer(Loshchilov&Hutter,2017)wasemployedalong-
| SAMmAPyieldsap-valueof |     |     | 0.0,confirmingastatistically |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
significant difference in performance. More t-test results sideacosineannealinglearningrateschedule(Loshchilov
|                   |     |                                  |     |     |     |     | &Hutter,2016). | Awarm-upphasewasappliedduringthe |     |                 |               |     |
| ----------------- | --- | -------------------------------- | --- | --- | --- | --- | -------------- | -------------------------------- | --- | --------------- | ------------- | --- |
| aregiveninTable5. |     | ThesefindingssuggestthatwhileDI- |     |     |     |     |                |                                  |     |                 |               |     |
|                   |     |                                  |     |     |     |     | initial 10     | epochs to stabilize              |     | early training. | Additionally, |     |
NOv2andSAMmaybeeffectiveinothercontexts,theyare
less suitable as target encoders in the SSL component of L2regularizationwithaweightdecaycoefficientof0.0005
wasusedtomitigateoverfittingandenhancegeneralization.
| theCFTmodel. |     | TheseresultsindicatethatbothMAEand |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
DINOv1serveasstrongcandidatesforthetargetencoderin
7.CONCLUSION
SSL,offeringsignificantlybetterperformancethanDINOv2
| and SAM. | Given | their similar | effectiveness, |     | either | MAE |     |     |     |     |     |     |
| -------- | ----- | ------------- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
orDINOv1canbeconfidentlyselectedforuseintheCFT Weintroduceahybridco-finetuning(CFT)methodformulti-
|     |     |     |     |     |     |     | framevisualbugdetection, |     | whichenhancesperformance |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | ------------------------ | --- | --- | --- |
framework.
anddataefficiencybyleveragingbothlabeledandunlabeled
|     |     |     |     |     |     |     | trainingdata. | Thisisachievedthroughahybridworkflow |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------------------------------ | --- | --- | --- | --- |
5.4.4.GENERALIZATIONTOOTHERVISUALBUG
thatfusessupervisedandself-supervisedlearningsignals
TYPESINGAMES:
fromthetargetgamedomainwithaco-domainderivedfrom
Answering research question RQ4, we evaluate the pro- amixtureofothergames.
| posed method’s |     | generalization |     | capabilities | for detecting |     |     |     |     |     |     |     |
| -------------- | --- | -------------- | --- | ------------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
single-frame visual bugs. These bugs primarily include Our comprehensive evaluation compared the proposed

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
SSL:True,CSL:True SSL:True,CSL:False SSL:False,CSL:True SSL:False,CSL:False
|            |     | mAP   |       | F1  | mAP   |     | F1    |     | mAP   |     | F1    | mAP   | F1    |     |
| ---------- | --- | ----- | ----- | --- | ----- | --- | ----- | --- | ----- | --- | ----- | ----- | ----- | --- |
| GiantMap   |     | 0.936 | 0.918 |     | 0.901 |     | 0.842 |     | 0.918 |     | 0.890 | 0.898 | 0.836 |     |
| CombatGame |     | 0.154 | 0.438 |     | 0.062 |     | 0.295 |     | 0.144 |     | 0.413 | 0.056 | 0.281 |     |
| Highrise   |     | 0.330 | 0.434 |     | 0.061 |     | 0.169 |     | 0.329 |     | 0.418 | 0.057 | 0.090 |     |
Table6.Performanceimpactofco-supervisedlearning(CSL)andself-supervised(SSL)objectivesontheCFTmodelperformance.
|     |     |     |     |     | Floating |     |     |     |     | Texture |     |     |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
GameTitle
|     |     |          |     | AutoML |       |       | CFT |       | AutoML |       |       | CFT   |     |     |
| --- | --- | -------- | --- | ------ | ----- | ----- | --- | ----- | ------ | ----- | ----- | ----- | --- | --- |
|     |     |          |     | 100%   | 50%   | 100%  |     | 50%   | 100%   | 50%   | 100%  | 50%   |     |     |
|     |     | Giantmap |     | 0.831  | 0.811 | 0.864 |     | 0.850 | 0.796  | 0.781 | 0.828 | 0.803 |     |     |
|     |     | Highrise |     | 0.733  | 0.690 | 0.721 |     | 0.618 | 0.965  | 0.954 | 0.968 | 0.956 |     |     |
Table7.SingleframevisualbugdetectionperformanceresultscomparingtheCFTmethodwiththebestperformingAzureAutoML
baseline.
| methodagainstestablishedbaselinesacrossthreedistinct |         |                 |     |         |          |     |      | References |     |     |     |     |     |     |
| ---------------------------------------------------- | ------- | --------------- | --- | ------- | -------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- |
| AAA game                                             | titles. | The performance |     | results | indicate |     | that |            |     |     |     |     |     |     |
Arnab,A.,Xiong,X.,Gritsenko,A.,Romijnders,R.,Djo-
ourmethodconsistentlyoutperformsthebestbaselineon
longa,J.,Dehghani,M.,Sun,C.,Lucˇic´,M.,andSchmid,
| alldatasets. | Notably,itmaintainsastatisticallysignificant |     |     |     |     |     |     |     |        |          |           |               |     |            |
| ------------ | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --------- | ------------- | --- | ---------- |
|              |                                              |     |     |     |     |     |     | C.  | Beyond | transfer | learning: | Co-finetuning |     | for action |
performanceadvantageevenwhentrainedwithhalfthesize
|                 |     |           |         |           |     |           |     | localisation. |     | arXivpreprintarXiv:2207.03807,2022. |     |     |     |     |
| --------------- | --- | --------- | ------- | --------- | --- | --------- | --- | ------------- | --- | ----------------------------------- | --- | --- | --- | --- |
| of the original |     | datasets. | We also | conducted | an  | extensive |     |               |     |                                     |     |     |     |     |
ablationstudytoevaluatetheimpactofdifferentarchitec-
Assran,M.,Duval,Q.,Misra,I.,Bojanowski,P.,Vincent,P.,
turalcomponentswithintheproposedmethod. Finally,we Rabbat,M.G.,LeCun,Y.,andBallas,N. Self-supervised
demonstratedthemethod’sgeneralizationpotentialbyap-
learningfromimageswithajoint-embeddingpredictive
| plying it | to other | types of | visual | bugs | sampled | from | two |               |     |     |          |            |             |     |
| --------- | -------- | -------- | ------ | ---- | ------- | ---- | --- | ------------- | --- | --- | -------- | ---------- | ----------- | --- |
|           |          |          |        |      |         |      |     | architecture. |     | In  | IEEE/CVF | Conference | on Computer |     |
additionalgamingenvironments. VisionandPatternRecognition,CVPR2023,Vancouver,
Ourfutureworkdirectionsareoutlined. Weaimtoinvesti- BC,Canada,June17-24,2023,pp.15619–15629.IEEE,
2023.
gatemethodologiesforlearningasharedembeddingspace
acrossmultiplevisionmodalities(Bachmannetal.,2022;
|         |         |              |          |      |       |           |     | Azizi,E.andZaman,L. |     |     | Automaticbugdetectioningames |     |     |     |
| ------- | ------- | ------------ | -------- | ---- | ----- | --------- | --- | ------------------- | --- | --- | ---------------------------- | --- | --- | --- |
| Girdhar | et al., | 2022) during | training | time | while | restrict- |     |                     |     |     |                              |     |     |     |
usinglstmnetworks.In2023IEEEConferenceonGames
inginferencetothepixelmodalityforruntimeefficiency.
(CoG),pp.1–4,2023.
Anotherdirectioninvolvesexploringadaptivedatamixing
strategies(Hejnaetal.,2024)toidentifyanoptimalscheme Azizi,E.andZaman,L. Astrobug: Automaticgamebug
tailoredtospecificdownstreamgamingdomains. Finally, IEEE Transactions on
|     |     |     |     |     |     |     |     | detection |     | using | deep learning. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----- | -------------- | --- | --- | --- |
weplantocoveradditionalmulti-framevisualbugtypes, Games,16(4):793–806,2024.
suchasZ-fightingorlightingbugs.Intermsoftrainingtime,
underidenticalhyperparametersettings,thebaselinemodel Bachmann,R.,Mizrahi,D.,Atanov,A.,andZamir,A. Mul-
|     |     |     |     |     |     |     |     | timae: | Multi-modalmulti-taskmaskedautoencoders. |     |     |     |     | In  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------------------------------------- | --- | --- | --- | --- | --- |
forGiantmaptrainsinabout1.5hours,whiletheCFTtakes
roughly 9.3 hours. Accelerating CFT training remains a Avidan, S., Brostow, G.J., Cisse´, M., Farinella, G.M.,
|     |     |     |     |     |     |     |     | and | Hassner, | T.  | (eds.), | Computer Vision | - ECCV | 2022 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------- | --------------- | ------ | ---- |
directionforfurtherstudy.
|                |     |         |        |             |              |     |     | - 17th | European |     | Conference, | Tel Aviv, | Israel, | October |
| -------------- | --- | ------- | ------ | ----------- | ------------ | --- | --- | ------ | -------- | --- | ----------- | --------- | ------- | ------- |
| In conclusion, |     | our CFT | method | effectively | demonstrates |     |     |        |          |     |             |           |         |         |
23-27,2022,Proceedings,PartXXXVII,volume13697
thebenefitsofsupervisedco-finetuningusingamixtureof
|              |     |                      |     |            |     |           |     | of  | Lecture | Notes | in Computer | Science, | pp. | 348–367. |
| ------------ | --- | -------------------- | --- | ---------- | --- | --------- | --- | --- | ------- | ----- | ----------- | -------- | --- | -------- |
| other games, |     | while simultaneously |     | leveraging |     | unlabeled |     |     |         |       |             |          |     |          |
Springer,2022.
datathroughself-supervisedlearningasanauxiliaryobjec-
tive. Caron, M., Touvron, H., Misra, I., Je´gou, H., Mairal, J.,
|     |     |     |     |     |     |     |     | Bojanowski, |     | P., | andJoulin, | A. Emergingpropertiesin |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ---------- | ----------------------- | --- | --- |
self-supervisedvisiontransformers.InProceedingsofthe
IEEE/CVFinternationalconferenceoncomputervision,
pp.9650–9660,2021.

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
Davarmanesh,P.,Jiang,K.,Ou,T.,Vysogorets,A.,Ivashke- Lin,T.-Y.,Maire,M.,Belongie,S.,Hays,J.,Perona,P.,Ra-
vich, S., Kiehn, M., Joshi, S. H., and Malaya, N. Au- manan,D.,Dolla´r,P.,andZitnick,C.L. Microsoftcoco:
tomatingartifactdetectioninvideogames.arXivpreprint Commonobjectsincontext. InComputervision–ECCV
arXiv:2011.15103,2020. 2014: 13th European conference, zurich, Switzerland,
September6-12,2014,proceedings,partv13,pp.740–
| Dawid, A. | and LeCun, | Y. Introduction | to latent variable |     |     |     |     |     |
| --------- | ---------- | --------------- | ------------------ | --- | --- | --- | --- | --- |
755.Springer,2014.
| energy-basedmodels: |     | Apathtowardsautonomousma- |     |     |     |     |     |     |
| ------------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
chineintelligence. CoRR,abs/2306.02572,2023. Ling,C.,Tollmar,K.,andGissle´n,L. Usingdeepconvolu-
tionalneuralnetworkstodetectrenderedglitchesinvideo
| Dosovitskiy, | A., Beyer, | L., Kolesnikov, | A., Weissenborn, |     |                                                  |     |     |     |
| ------------ | ---------- | --------------- | ---------------- | --- | ------------------------------------------------ | --- | --- | --- |
|              |            |                 |                  |     | games. InProceedingsoftheAAAIConferenceonArtifi- |     |     |     |
D.,Zhai,X.,Unterthiner,T.,Dehghani,M.,Minderer,M.,
cialIntelligenceandInteractiveDigitalEntertainment,
| Heigold,G.,Gelly,S.,etal. |     | Animageisworth16x16 |     |     |     |     |     |     |
| ------------------------- | --- | ------------------- | --- | --- | --- | --- | --- | --- |
volume16,pp.66–73,2020.
words:Transformersforimagerecognitionatscale.arXiv
preprintarXiv:2010.11929,2020. Loshchilov, I. and Hutter, F. Sgdr: Stochastic gra-
|             |           |                  |           |       | dient descent | with warm | restarts. arXiv | preprint |
| ----------- | --------- | ---------------- | --------- | ----- | ------------- | --------- | --------------- | -------- |
| Everingham, | M., Gool, | L. V., Williams, | C. K. I., | Winn, |               |           |                 |          |
arXiv:1608.03983,2016.
| J.M.,andZisserman,A. |     | Thepascalvisualobjectclasses |     |     |     |     |     |     |
| -------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- |
(VOC) challenge. Int. J. Comput. Vis., 88(2):303–338, Loshchilov,I.andHutter,F. Decoupledweightdecayregu-
| 2010. |     |     |     |     | larization. | arXivpreprintarXiv:1711.05101,2017. |     |     |
| ----- | --- | --- | --- | --- | ----------- | ----------------------------------- | --- | --- |
Girdhar, R., Singh, M., van der Maaten, L., Joulin, A., Oquab,M.,Darcet,T.,Moutakanni,T.,Vo,H.,Szafraniec,
andMisra,I. Omnivore: Asinglemodelformanyvisual M.,Khalidov,V.,Fernandez,P.,Haziza,D.,Massa,F.,El-
modalities.InIEEE/CVFConferenceonComputerVision Nouby,A.,etal. Dinov2: Learningrobustvisualfeatures
andPatternRecognition,CVPR2022,NewOrleans,LA, withoutsupervision. arXivpreprintarXiv:2304.07193,
| USA,June18-24,2022,pp.16081–16091.IEEE,2022. |     |     |     |     | 2023. |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- |
Goutte,C.andGaussier,E. Aprobabilisticinterpretationof Paduraru,C.,Paduraru,M.,andStefanescu,A. Automated
precision,recallandf-score,withimplicationforevalu- game testing using computer vision methods. In 2021
ation. InEuropeanconferenceoninformationretrieval, 36thIEEE/ACMInternationalConferenceonAutomated
pp.345–359.Springer,2005. Software Engineering Workshops (ASEW), pp. 65–72,
2021.
| He, K., | Zhang, X., | Ren, S., and Sun, | J. Deep residual |     |     |     |     |     |
| ------- | ---------- | ----------------- | ---------------- | --- | --- | --- | --- | --- |
learningforimagerecognition. In2016IEEEConference Qiu,W.andYuille,A.L. Unrealcv: Connectingcomputer
onComputerVisionandPatternRecognition,CVPR2016, visiontounrealengine. InHua,G.andJe´gou,H.(eds.),
Las Vegas, NV, USA, June 27-30, 2016, pp. 770–778. ComputerVision-ECCV2016Workshops-Amsterdam,
IEEEComputerSociety,2016. TheNetherlands,October8-10and15-16,2016,Proceed-
ings,PartIII,volume9915ofLectureNotesinComputer
He,K.,Chen,X.,Xie,S.,Li,Y.,Dolla´r,P.,andGirshick,
Science,pp.909–916,2016.
| R. Maskedautoencodersarescalablevisionlearners. |     |     |     | In  |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
ProceedingsoftheIEEE/CVFconferenceoncomputer Rahman,F. Weaksupervisionforlabelefficientvisualbug
visionandpatternrecognition,pp.16000–16009,2022. detection. arXivpreprintarXiv:2309.11077,2023.
Hejna,J.,Bhateja,C.A.,Jiang,Y.,Pertsch,K.,andSadigh, Redmon, J., Divvala, S.K., Girshick, R.B., andFarhadi,
D. Remix: Optimizing data mixtures for large scale A. Youonlylookonce: Unified,real-timeobjectdetec-
imitation learning. In Agrawal, P., Kroemer, O., and tion. In2016IEEEConferenceonComputerVisionand
Burgard, W. (eds.), Conference on Robot Learning, 6- PatternRecognition, CVPR2016, LasVegas, NV,USA,
9 November 2024, Munich, Germany, volume 270 of June27-30,2016,pp.779–788.IEEEComputerSociety,
| ProceedingsofMachineLearningResearch,pp.145–164. |     |     |     |     | 2016. |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | ----- | --- | --- | --- |
PMLR,2024.
|     |     |     |     |     | Ren,S.,He,K.,Girshick,R.B.,andSun,J. |     | FasterR-CNN: |     |
| --- | --- | --- | --- | --- | ------------------------------------ | --- | ------------ | --- |
Jocher,G.,Stoken,A.,Borovec,J.,Changyu,L.,Hogan,A., towardsreal-timeobjectdetectionwithregionproposal
Diaconu,L.,Poznanski,J.,Yu,L.,Rai,P.,Ferriday,R., networks. InAdvancesinNeuralInformationProcessing
etal. ultralytics/yolov5: v3.0. Zenodo,2020. Systems28: AnnualConferenceonNeuralInformation
|           |             |                    |              |     | Processing | Systems 2015, | December 7-12, | 2015, Mon- |
| --------- | ----------- | ------------------ | ------------ | --- | ---------- | ------------- | -------------- | ---------- |
| Kirillov, | A., Mintun, | E., Ravi, N., Mao, | H., Rolland, | C., |            |               |                |            |
treal,Quebec,Canada,pp.91–99,2015.
Gustafson,L.,Xiao,T.,Whitehead,S.,Berg,A.C.,Lo,
W.-Y., et al. Segment anything. In Proceedings of the Skwarczek, B. How the gaming industry has leveled up
IEEE/CVFinternationalconferenceoncomputervision, duringthepandemic.Forbes,2021. [Online;Accessed:
| pp.4015–4026,2023. |     |     |     |     | 2024-12-06]. |     |     |     |
| ------------------ | --- | --- | --- | --- | ------------ | --- | --- | --- |

AHybridCo-FinetuningApproachforVisualBugDetectioninVideoGames
Taesiri,M.,Macklon,F.,Wang,Y.,Shen,H.,andBezemer,
C.Largelanguagemodelsareprettygoodzero-shotvideo
gamebugdetectors(2022),2022.
| Taesiri,M.R.,Habibi,M.,andFazli,M.A. |     |     | Avideogame    |     |
| ------------------------------------ | --- | --- | ------------- | --- |
| testingmethodutilizingdeeplearning.  |     |     | IranJournalof |     |
ComputerScience,17,2020.
| Taesiri,      | M. R., Feng,                        | T., Bezemer, C.-P., | and Nguyen, | A.  |
| ------------- | ----------------------------------- | ------------------- | ----------- | --- |
| Glitchbench:  | Canlargemultimodalmodelsdetectvideo |                     |             |     |
| gameglitches? | InProceedingsoftheIEEE/CVFCon-      |                     |             |     |
ferenceonComputerVisionandPatternRecognition,pp.
22444–22455,2024.
| Tamm,                                      | M., Shamon,                            | O., Leon, H. | A., Tollmar, | K., and |
| ------------------------------------------ | -------------------------------------- | ------------ | ------------ | ------- |
| Gissle´n,L.                                | Automatictestingandvalidationoflevelof |              |              |         |
| detailreductionsthroughsupervisedlearning. |                                        |              |              | In2022  |
IEEEConferenceonGames(CoG),pp.191–198,2022.