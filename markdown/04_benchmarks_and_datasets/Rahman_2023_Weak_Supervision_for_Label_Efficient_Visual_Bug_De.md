---
title: "Weak Supervision for Label Efficient Visual Bug De"
author: "Rahman"
year: "2023"
source_file: "04_benchmarks_and_datasets/Rahman_2023_Weak_Supervision_for_Label_Efficient_Visual_Bug_De.pdf"
source_sha256: "dbee8822da0b7b03f8dea88479354ae695e806fa7dc0f8ff17797c2ebf253ffd"
converted_at: "2026-11-06T15:12:47.752205+00:00"
markitdown_version: "0.1.9"
char_count: 39111
---
RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION 1
Weak Supervision for Label Efficient Visual
Bug Detection
FarrukhRahman XboxStudiosQuAIL
farrukh.rahman@microsoft.com
Abstract
Asvideogamesevolveintoexpansive,detailedworlds,visualqualitybecomesessen-
tial,yetincreasinglychallenging.Traditionaltestingmethods,limitedbyresources,face
difficultiesinaddressingtheplethoraofpotentialbugs.Machinelearningoffersscalable
solutions; however, heavyrelianceonlargelabeleddatasetsremainsaconstraint. Ad-
dressingthischallenge, weproposeanovelmethod, utilizingunlabeledgameplayand
domain-specific augmentations to generate datasets & self-supervised objectives used
during pre-training or multi-task settings for downstream visual bug detection. Our
methodologyusesweak-supervisiontoscaledatasetsforthecraftedobjectivesandfa-
cilitatesbothautonomousandinteractiveweak-supervision,incorporatingunsupervised
clustering and/or an interactive approach based on text and geometric prompts. We
demonstrateonfirst-personplayerclipping/collisionbugs(FPPC)withintheexpansive
Giantmapgameworld,thatourapproachisveryeffective,improvingoverastrongsu-
pervisedbaselineinapractical,verylow-prevalence,lowdataregime(0.336→0.550F1
score).Withjust5labeled"good"exemplars(i.e.,0bugs),ourself-supervisedobjective
alonecapturesenoughsignaltooutperformthelow-labeledsupervisedsettings.Building
onlarge-pretrainedvisionmodels,ourapproachisadaptableacrossvariousvisualbugs.
Ourresultssuggestapplicabilityincuratingdatasetsforbroaderimageandvideotasks
withinvideogamesbeyondvisualbugs.
1 Background & Introduction
Visualqualityinvideogamesisoneofthekeydriversofsatisfactionwithcustomers. With
moderngamestransitioningtowardsexpansive,openworldswithintricatevisualsandsys-
tems,thepotentialforbugsrapidlygrows. Traditionalmanualtestingmethods,constrained
by time and resources, grapple with these challenges. Advances in Computer Vision (CV)
andMachineLearning(ML)presentpromisingalternatives,offeringautomatedandscalable
visual testing solutions, thereby reallocating resources to explore other game dimensions
[24]. Notably, the success of deep learning in CV is largely credited to extensive labeled
datasets[11,22],oftencuratedfromthevastquantititesofdigitalcontentontheweb. How-
ever,curatingthesemassivelabeleddatasetsforasinglegameisimpractical. Manualcap-
turingandlabelingofvisualbugsatscalewouldrenderdetectionmethodsredundant,more
sogiventherarityofsuchbugs. Computervisionbasedmethodsrecentlyproposedfacilitate
automatedvisualtestingatscaleby1. leveraginggameenginestoincreasedataavailability
amenable to deep learning approaches [23, 33, 34, 39] and/or 2. using anomaly detection
basedapproachestreatingbugsasoutofdistribution(OOD)occurrencesfromnormalframes
©2023.Thecopyrightofthisdocumentresideswithitsauthors.
Itmaybedistributedunchangedfreelyinprintorelectronicforms.
3202
peS
02
]VC.sc[
1v77011.9032:viXra

2 RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION
[40]. Whileaccesstogameenginesendowgreaterdataavailabilityandcontroloverdiver-
sity,thenon-stationarynatureofgamesrequiresanevolvingsetofdatageneratedforevery
newassetacrossmultiplefactors(environment,lighting,etc.) foranygivengametitle. Ad-
ditionally,thelimitedtestingwindowinagamedevelopmentcycleplacesemphasisonthe
speedofadaptationofanyparticulardetectionmethod.Addressingthesechallenges,wepro-
poseusingunlabeledgameplayvideopairedwithdomain-specificaugmentationtechniques
to derive objectives for visual bug detection models. This strategy is useful in the low-
labeled settings often present during game development. Specifically, our method (fig. 1)
utilizes large-pretrained vision models [20, 29] also termed foundation models [5] along
withdomainspecificaugmentationstrategiesmotivatedby[14]toformulateself-supervised
objectivesforwhichwescaledatasetsthroughweak-supervision. Self-supervisedlearning
(SSL) seeks to learn from unlabeled data through optimization of a defined surrogate ob-
jective, which is then transferred to downstream target tasks [2]. SSL has shown to learn
transferable representations across multiple domains including CV [8, 15, 17, 18]. Weak
Supervisionleveragesnoisyannotationsourcestoexpedientlygenerateandscalenoisilyla-
beled datasets [32, 41], recently demonstrating effectivenessin training large-scale models
acrossmultipledomains[20,29,30]. Interactiveweaksupervisionfurthersthisviaaninter-
active process [4, 27] merging domain expertise with scalability of weak supervision. Our
methodologyusesdomain-specificSSLobjectivesthatarescaledthroughweaksupervision,
leveraginglargepre-trainedmodelsandintegratingtextandgeometricpromptsforefficient
interaction. Wedemonstratethegeneralityofourmethodbytargetingmultiplevisualbug-
types, egocentric/first-personplayerclippingandtextureissues. Moreover, fromanalyzing
ourresultswesuggestourmethodcanbeadaptedtocurateextensivedatasetsforarangeof
imageandvideoanalysistasksinvideogames,extendingbeyondvisualbugdetection.
Themaincontributionsofthisworkaresummarizedasfollows:
1. Empirical Observations on ViT Performance: We observe that when trained with
aself-supervisedmethod,DINOv1,a. ViTsurpassestraditionalResNetarchitectures,
andb.DINOrivalstheperformanceofsupervisedpre-trainingonIN1Kinlow-labeled
andfew-shotsettingsforvisualbugs.
2. Development of a Novel Methodology: Building on the aforementioned observa-
tions, we introduce a flexible technique that uses weak-supervision to scale a self-
supervisedobjective.Thisapproachmeldszero-shotsegmentation(Segment-Anything)
anddomain-specificaugmentations. Notably,ourmethodconsistentlydeliversstrong
resultsacrosspracticalout-of-distribution(OOD)contexts.
3. Extension via Clustering and Filtering: We integrate a filtering step to enhance
performance using unsupervised clustering and text-image models such as CLIP, of-
feringtwodistinctavenues:automatedortext-interactiveweaksupervision.Thelatter
enables non-ML practitioners to add preferable inductive biases to guide the system
throughsimpletextandgeometricprompts.
4. EfficientDatasetCuration:Ourresearchunderscoresthepotentialforefficientdataset
curation. Given a handful of labeled "good" exemplars and a small amount of do-
mainexpertise,datasetscanbecuratedautonomously. Fromthesewecancraftobjec-
tivesforstandalonefew-shotmodels,pre-training,ormulti-taskscenariosinlow-data
regimes.

RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION 3
Figure1:Generaloverviewofourmethod:1.SegmentationStage:Givenunlabeledgameplayvideo,
weapplyageometricpromptablesegmentationmodel(SAM)toautomaticallyextractmasks. 2. Fil-
teringStage:Theobtainedmasksarethenfilteredeitherinanunsupervisedmannerand/oroptionally
viatext-interactivefilteringusingtext-imagemodel(CLIP).3. AugmentationStage: Labeled‘good’
targetinstances,and/orunlabeledtargetinstances,areaugmentedusingthefilteredmasksproducing
samplesusedtotrainasurrogateobjective.
2 Approach
Several practical challenges arise in the domain of visual bug detection, which shape our
objectives. Firstly, thereistheissueoflimitedlabeleddata. Thetimeframesduringwhich
visualtestingcanbeconductedarenarrow,especiallywithfreshcontent.Methodsamenable
tolow-dataregimesand/orfastertransferlearningarehighlycoveted. Asecondisaccessto
sourcecode; enginessuchas[13,36]continuetointegrateMLfeaturesincreasingdatafor
modelstoconsume,yetthisisimpracticaltoscaleacrosseverygame(eg.buildinghooksinto
everynewsub-releaseofagivengame). Weseekmethodsthatcanbeappliedinscenarios
where access to the source code is not guaranteed. Related to this is the notion of out-
of-distribution (OOD) scenarios, namely that even if we could gather data at a given point
duringdevelopment,asnewcontentisaddedwewantourmodeltoadapttonewscenarios
with minimal new data. An additional point here is that our input data during test time is
constrainedtoRGBframes. Moreover,athirdpracticalconstraintisthenotionthatbugsare
oftenrareandperformantmethodsinlow-prevalencescenariosarevaluable.
2.1 Datasets
WeusetheGiantmap-5(nowGM4asoneobjectwasremoved)environmentandactivearea
asintroducedin[1],developedinUnreal[13]. Wefurtherextenditbyintroducing46new
objectsofinterest(OOI)showninfig.2. Inthisstudy,wetreattheGiantmapenvironment
asourtargetvideogametitleforourchosenvisualbug,first-personplayerclipping(FPPC).
FPPCmanifestswhencollisionmeshesforeithertheplayerorobjectaresetincorrectlyor
naivelycreatingvisualaberrationsthatwouldnotoccurinthephysicalworld, seefig.2of
FPPC on the 4 objects on our GM4 environment. From this environment we create i.i.d.
screenshotsprogrammaticallybyfirstgeneratinganobjectdistributionoverthemapwitha
specified density, then spawning the player near objects within a certain distance from the

4 RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION
Figure2: (left4images)in-distributionClippingexamplesfromGM-4set. (Rightimage)46Out-of-
distributionobjectsaddedinGM-50.
center of the object to sample varied clipping and normal samples. This capability allows
us to scale data generation significantly however we seek to push the boundaries of label
efficiencytreatingGiantmapasourtargettitle. Howfarcanwepushin-distributionperfor-
manceandhowdoesitfareinOODscenarios?Tothiseffect,weconstraintrainingdatato15
totalsamplesforGM4-tinydatasetand156samplesforGM4-basedatasetwhilstgenerating
3kvalidationandtestin-distributionsets. Moreover,wegeneratealow-prevalence(0.007)
videodeploymentsetonGM50(4ID+46OODobjects)toevaluateourmethods,ineffortto
mimicwhatadevelopermightcollectfromautomatedorhumanplaytesting. Additionally
wegatherseparatehumangameplayonGM50tousewiththesmallamountoflabeleddata
generated. Insummary,wearegivenasmallamountofi.i.dscreenshotin-distributiondata,
UnlabeledOODvideo,andareexpectedtoevaluateonanOOD,low-prevalencevideo.
2.2 Method
Ourmethodcanbeviewedasaself-supervisedobjectivescaledthroughweak-supervision.
As shown generally in fig.1, it consists of 3 main stages, and is described in more detail
below. Weusethefirst-personplayerclippingtasktoshowtheefficacyoftheapproachasit
isachallengingvisualbug.
SegmentationStage:Givenunlabeledgameplayvideoofatargetvideogame,weapply
apre-trained, promptablesegmentationmodelSAM[20]toextractmasksinanautomated
manner.SAMtakesasinputanimageandoneormoregeometricprompts.Inabsenceofany
prompt,pointsareplaceduniformlyacrosstheimagewhichrepresentstheautomatic/zero-
shotsegmentationprompt. PriorscanbeinjectedintotheprompttoguideSAMtoignoreor
furthersamplecertainregionsoftheinputframe.
Filtering Stage: Since the environment is an outdoor park set in the spring, certain
semanticvisualfeaturesareabundant,eg. trees,walkingtrails,orgrass. Wedevelopafilter-
ing&deduplicationstepusingCLIP[29],atext-imagemodeltoextractembeddingsofeach
maskedregion.Forautonomousfiltering,wefirstclusterembeddingsusingHierarchicalAg-
glomerative Clustering (HAC) [19, 28], then re-sample masks from each cluster aiming to
balancethemaskdistribution. Forinteractivefiltering,ausermayapplypriorknowledgeto
selectfororagainstcertainmasksviaatextprompt,afterwhichweperformclustering. The
textpromptsareembeddedusingtheCLIPtextencoderandcosinedistancesarecomputed
witheachmaskembedding. Text-promptingcapabilitycanautonomouslyincorporateprior
knowledge; for instance, if prior knowledge indicates that foliage, trees, and grass aren’t
relevant, text-promptsaroundthesesemanticscanbecachedandappliedaspre-processing
prior to unsupervised clustering. The final set of masks represents the set of semantics on
the playthrough/game-level expected to be observed in a scene, intrinsically making them
goodcandidatesforvisualbugaugmentation. Moreover,thepolicyunderwhichthedatais
collectedalsocontributestothemaskdistribution;wemakeanexplicitassumptionthatthe
semanticsofatargetgamearecapturedintheunsupervisedplaythroughs.
AugmentationStage:Masksalongwithtargetimagesareusedtocreateaself-supervised

RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION 5
Figure 3: Our method from fig.1 instantiated w.r.t. first-person player clipping. From an unlabeled
video, 5 target frames (2 shown) are labeled and processed by SAM (in dark blue) with geometric
prompts. SourcegeometricpromptsguideSAMtodisregardthe’priorregion’(i.e. weaponregion),
whiletargetpromptsemphasizeonlythatregion. Afterfiltering,sourcemasks,alongwithwithtarget
masks and target images, proceed to the augmentation phase. Here, positives are created by over-
laying the source mask over the target image’s weapon area, while negatives are positioned behind
theweapon,respectingthetargetweaponmask. Classifyingpositivesvsnegativesserveasourself-
supervisedobjectiveforFPPC.
objectivethroughdomain-specificaugmentation.Targetimagescanbeobtainedfromasmall
labeledset,ordirectlyfromthesourceunlabeleddata. Asthemasksrepresentsemanticsof
the target game we utilize them to create augmented positive examples denoting bugs and
negativeexamplesdenoting"normal"or"no-bug". Ifvariantsofaparticularbugexist(e.g.,
stretchedvslow-restexture),multipleclassescanbeaugmented. Asthemethodistailored
to the downstream task, in certain scenarios, the source and target image can be identical.
Ourmethodisflexibleandcanbeappliedacrossavarietyofvisualbugtypes.
First-personWeaponClippingapproach:WeinstantiateourgeneralmethodforFirst-
Person (or egocentric) player clipping (FPPC), fig. 3. During segmentation prompting we
prefertoignorethebottom-rightcorneroftheimagetypicallywheretheweaponisplaced;
thuspreventingsaturatingdetectedmaskswithweaponmasks.Fromtheunsupervisedgame-
playvideo,firstthevideowasdown-sampledtemporallyasvideosnaturallyhavevisualin-
formation redundancy among adjacent frames. Semantic redundancy however is useful as
the same object viewed from a different view increases both the probability of acquiring a
good mask, as well as instance diversity. From said subsample, two further sets are sam-
pled,300framestobuildatinydatasetof217masks,and20kframestobuildalargersetof
17kmasks. Thefilteringstepisunchangedfromfig.1. Forourspecificsetting,weelectto
pastethemaskovertheweaponinagiventargetimage. Thiscreatesa"peudo-clipping",or
"weaponobstruction"signalwhichwehypothesizeiscorrelatedwithourtargetdownstream
clipping task. Conversely, the mask is copied under the weapon (respecting the weapon’s
mask)tocreateanegativesample. Inordertoachievethis,werequirelabeled-goodimages
astargets.Welabel5randomframesfromthehumangameplayvideoandusethemastarget
images. Eachtargetimageispairedwitheachmaskfor2roundsofaugmentation(pseudo-
clipvsno-clip). Duringtheaugmentation,thesourcemaskcanbefurtheraugmentedbefore
itispastedontothetargetimages.Weapplyrandomrotationandrandomhorizontalflipaug-
mentations. Post augmentation the tiny mask set generates 2.2k total samples, while large
generates170k;whichareusedtopre-train,multi-taskandfew-shotonourtargettask.

6 RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION
| ModelArchitecture | PretrainMethod | Prior Accuracy        |       |                   |                      |          |
| ----------------- | -------------- | --------------------- | ----- | ----------------- | -------------------- | -------- |
|                   |                |                       |       | ModelArchitecture | PretrainMethod Prior | Accuracy |
| R e s N e t - 5 0 | I n 1 k s u p  | C r o p 0 . 8 1 1 ± 0 | . 0 6 |                   |                      |          |
R e s N e t - 5 0 I n 1 k s u p A1 C r o p 0 . 7 9 6 ± 0 . 0 3 R e s N e t - 5 0 I n 1 k s u p C r o p 0 . 9 5 8
R e s N e t - 1 8 I n 1 k s u p C r o p 0 . 7 5 3 ± 0 . 0 4 v i t - b a s e - 1 6 I n 1 k s u p C r o p 0 . 9 6 5 7
v i t - b a s e - 1 6 I n 1 k s u p C r o p 0 . 9 1 3 ± 0 . 0 3 v i t - b a s e - 1 6 C L I P C r o p 0 . 9 7 9
|     |     |     |     | v i t - b a s e - 1 6 | D I N O v 1 C r o | p 0 . 9 7 6 |
| --- | --- | --- | --- | --------------------- | ----------------- | ----------- |
v i t - b a s e - 1 6 C L I P C r o p 0 . 9 4 9 ± 0 . 0 3 v i t - b a s e - 1 6 I n 1 k s u p C r o p 0 . 9 1 4 8
v i t - b a s e - 1 6 D I N O v 1 C r o p 0 . 9 5 2 ± 0 . 0 3 R e s N e t - 5 0 D I N O v 1 C r o p 0 . 9 6 6 4
| v i t - b a s e - 1 6 | I n 1 k s u p | C r o p 0 . 8 2 5 ± 0 | . 0 3 |                   |                 |           |
| --------------------- | ------------- | --------------------- | ----- | ----------------- | --------------- | --------- |
|                       |               |                       |       | R e s N e t - 5 0 | I n 1 k s u p - | 0 . 9 2 2 |
R e s N e t - 5 0 I n 1 k s u p - 0 . 7 3 3 ± 0 . 0 5 v i t - b a s e - 1 6 D I N O v 1 - 0 . 9 6 7
| v i t - b a s e - 1 6 | D I N O v 1 | - 0 . 8 2 4 ± 0 | . 0 5 |     |     |     |
| --------------------- | ----------- | --------------- | ----- | --- | --- | --- |
v i t - b a s e - 1 6 C L I P - 0 . 6 7 5 ± 0 . 0 2 v i t - b a s e - 1 6 C L I P - 0 . 8 9
v i t - b a s e - 1 6 I n 1 k s u p - 0 . 7 3 8 ± 0 . 0 2 v i t - b a s e - 1 6 I n 1 k s u p - 0 . 9 6 1
|                          |      |             | Table | 2: In-distribution | test performance | for |
| ------------------------ | ---- | ----------- | ----- | ------------------ | ---------------- | --- |
| Table 1: In-distribution | test | performance | for   |                    |                  |     |
trainingonGM4-TinyDataset(15totalsamples). trainingonGM5-baseDataset,156totalsamples.
| Resultsover3trials. |     |         | ±0.02over3trials. |     |     |     |
| ------------------- | --- | ------- | ----------------- | --- | --- | --- |
| 3 Experiments       | &   | Results |                   |     |     |     |
In-DistributionperformanceonGiantMap-4: Wereportthein-distributionbalancedtest
accuracy of the various architectures evaluated in tab. 1, 2. We evaluate ResNet [16] vari-
antsandVisionTransformer(ViT)[12]. Withineacharchitecturewefurtherevaluatevari-
ouspre-trainingmethodologyincludingsupervised,weakly-supervisedandself-supervised
learningmethods. Specifically,IN1k[11]supervisedpre-trainingusingthetraditional[16]
andA1ResNettrainingrecipefrom[37, 38], DINOv1[7]self-supervisedpretexttask(for
bothResNetandViT)aswellasweakly-supervisedCLIP’s[29]ViTbasedimage-encoder.
Weuseafew-shotfinetuningapproachgivenrecentresultsindicatingitssuperioritywhen
trainingintheseregimes[9, 35]. Moreover, weevaluateusingacroppriorcomparedwith
thefullframe. SpecificallyregardingFPPC,givenitmainlymanifestswiththeweapon,we
can ignore the other parts of the frame. Naturally, the prior is significantly more data effi-
cient, see tab. 1. In parallel, treating the problem as an object detection problem was also
exploredhoweverthecroppriorapproachshowsgreaterdataefficiencygivennoregression
ofbboxcoordinatesisrequired(ref. supplemental).Ourresultsshow1. few-shotfinetuning
canbeefficientand2. whenpre-trained,Visiontransformersseemtooutperformtraditional
CNNsinlow-labeledsettings, similartoobservationsinothervisualdomains[25, 31, 42].
Moreover, we observe that self-supervised pretraining (DINOv1) is competitive or slightly
surpasses supervised pretraining when transfer learning to our task. i.e., DINO is able to
extractrelevantfeaturesthattransferwellintothelow-dataregime,tab.2. Givenourstrong
baselineforbalancedlow-labeledin-distributionperformance, weselectViTpretrainedon
DINO as our backbone for all future experiments where we will evaluate in a challenging
out of distribution (OOD), low-prevalence setting observed in practice. In this imbalanced
setting,weuseF1score(harmonicmeanofprecisionandrecall)asourprimarymetric.
3.1 WeakSupervision
Given the supervised fine-tuning (SFT) performance on our low-prevalence deployment
tabs.3,5weseektoimproveitbyapplyingourmethodfromsection2.2.
MaskFiltering: ToanalyzethemasksproducedbySAM[20], wesample30kframes
from an unlabeled human gameplay video from GM50, generate masks using SAM and
label them. Our labeling scheme was a combination of GM50 Objects of Interest (OOI)
along with other general semantic categories. As observed in fig. 4a, firestand, pathway,
ground, and trees dominate the distribution. The latter two are omnipresent in scenes and
theformer,duetothedatagatheringpolicy. Thiscreatesredundancyinthesignalweinject
viaaugmentation. Tocombatthis, weuseCLIP[29]toextractembeddingsandHAC[19]

RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION 7
(k=50) with cosine distance to cluster masks in an unsupervised manner, k was selected
naivelywithaprioriknowledgeof50OOIonthemap. Realisticallyk>50asothernon-
OOI are contribute to visual semantics of GM50. We observe that resampling after using
eithertheheuristicfig.4btoselectkoroverclusteringfig.4c(k=100)somewhatameliorates
class imbalance. See fig. 5 for qualitative examples of our clusters. Interestingly, clusters
capturemultipleviewsofbothOOIfig.5andalsoothermapobjectsfig.5d,thefoodstandis
notanOOIyetitiscaptured,apromisingsignforOODgeneralization. Further,weobserve
thatobjectswithoverlappingvisualsemantics,especiallyfine-grainedonessuchasvariants
of statues fig. 5b, tend to cluster together. We explore explicit removal of non-relevant yet
highlyfrequentmaskssuchassky,trees,pathways,inhopestofurtherincreasesignalinour
weak dataset. As we are already using CLIP image-encoder to extract visual features, we
canpairwithtextencoderembeddingsthatmaybesuppliedinteractivelyorstoredasapriori
knowledge. eg. Clippingwithgrassandfoliageisnearuniversallyanon-issue. Wefiltervia
storedtextpromptstailoredtowardspathways,trees,etc. resultinginadistributionfig.4d.
While the non-relevant masks have been filtered, overall class balance has gotten worse.
Byremovingomnipresentnon-relevantclasses(∼50%ofthemasks),anyremainingover-
represented classes (fire stand) overwhelm the distribution. We rebalance by performing
clustering and resampling post text filtering. There exist other interesting approaches not
explored,eg. clusteringfollowedbyinteractivelabelingtopruneawayentireclusters.
(a) (b)
(c) (d)
Figure 4: Mask label frequencies. (a) ground truth (b) 50 re-sampled from k=50 clusters, (c) 50
samplesre-sampledfromk=100clusters,(d)textpromptbasedfilteringonsemanticcategoriestrees,
foliage,roads,sky
Self-supervision: Pre-trainingvsmulti-task: Giventwomasksets,Tiny(217masks)
and Large (17k masks), we create multiple datasets to serve the self-supervised objective.
(a) (b) (c) (d)
Figure5: Maskclustering(k=50): (a)multipleviewsofobjectsarecaptured,(b)certainfine-grained
objectstendtoclustertogether,(c)thesky,an"object"notrelevanttoourvisualbug,(d)mapobject.

8 RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION
|                    |              |       |     | Dataset          | F1    |     |
| ------------------ | ------------ | ----- | --- | ---------------- | ----- | --- |
|                    |              |       |     | LargeAug-Raw     | 0.054 |     |
| Dataset            | TrainMethod  | F1    |     | LargeAug         | 0.429 |     |
| SupervisedGM4-tiny | SFT          | 0.153 |     | TinyAug-Raw      | 0.296 |     |
| TinyAug+GM4-tiny   | Pretrain+SFT | 0.479 |     | TinyHeavyAug-Raw | 0.480 |     |
|                    |              |       |     | TinyAug          | 0.529 |     |
| LargeAug+GM4-tiny  | Pretrain+SFT | 0.397 |     |                  |       |     |
| TinyAug+GM4-tiny   | multi-task   | 0.484 |     | TinyHeavyAug     | 0.493 |     |
LargeAug+GM4-tiny multi-task 0.484 Table 4: Low-prevalence, OOD deployment F1
| Table 3: Low-prevalence, | OOD               | deployment | F1                       |                       |                     |              |
| ------------------------ | ----------------- | ---------- | ------------------------ | --------------------- | ------------------- | ------------ |
|                          |                   |            | scores                   | on GM50 in            | few-shot setting    | (ie. self-   |
| results on GM50.         | GM4-tiny training | dataset    |                          |                       |                     |              |
|                          |                   |            | supervisedobjectiveonly. |                       | 5labelednegativeex- |              |
| (15 labeled examples).   | LargeAug=17k      | masks,     |                          |                       |                     |              |
|                          |                   |            | amples,                  | 0 positive examples). |                     | LargeAug=17k |
TinyAug=217masks.
Masks,TinyAug=217masks.Rawsuffixdenotes
unfiltered.
|     | Dataset              |     | TrainMethod  | F1    |     |     |
| --- | -------------------- | --- | ------------ | ----- | --- | --- |
|     | SupervisedGM4        |     | SFT          | 0.336 |     |     |
|     | LargeAug+GM4         |     | multi-task   | 0.419 |     |     |
|     | TinyHeavyAug+GM4     |     | multi-task   | 0.516 |     |     |
|     | TinyHeavyAug-raw+GM4 |     | multi-task   | 0.510 |     |     |
|     | LargeAug+GM4         |     | multi-task   | 0.533 |     |     |
|     | TinyHeavyAug+GM4     |     | Pretrain+SFT | 0.492 |     |     |
|     | TinyAug+GM4          |     | Pretrain+SFT | 0.550 |     |     |
Table 5: Low-prevalence, OOD deployment F1 results on GM-50. GM4-base training dataset (175
totallabeledexamples). Multi-taskandpre-trainingontheself-supervisedobjectivegreatlyincreases
performanceoverbaseline0.336F1scoreobtainedfromSFT.TinyAug=smallmaskset. Rawsuffix
=unfiltered.
The first TinyAug and LargeAug consist of paired data with limited rotation augmentation
oftheindividualmasks. ThesecondHeavyTinyandHeavyLargeconsistofheavyrotations
to influence diversity. We pair these objectives with labeled GM4-tiny and GM4-base in a
sequentialpre-trainingorsimultaneousmulti-tasktrainingsetting. Themulti-taskobjective
isaweightedcombinationL=λL +(1−λ)L whereL denotesourSSLobjective,L is
|     |     | w   | t   | w   |     | t   |
| --- | --- | --- | --- | --- | --- | --- |
thetargetobjective. Weevaluateourmodelsinthelow-prevalenceOODsettingonGM50
across3settings,eachdenotingsomeamountof"real"labeleddataavailableduringtraining.
1. onlyafew(5)labeled"good"exemplarsand0positives(i.e.,0realbugssamples)trained
withweaksupervisiononlytab.4,2. tinyamountoflabeleddataisavailable(15examples
total)tab.3,and3. smallamountoflabeleddataisavailable(156samplestotal),tab.5. Our
resultsindicatethatourself-supervisionaloneabsentanypositive(bugs)examplesissuffi-
cienttosurpassthebestfullysupervisedtraininginthelow-labeled,low-prevalenceregime,
0.529 vs 0.336 F1. Further fine-tuning on a small amount of labeled data tab. 5 enhances
performanceto0.550. Overallbothpre-trainingandmulti-taskarecompetitivewithonean-
other,howeverpre-trainingedgesout. Inaddition,weobservethatpre-trainingwassimpler
to optimize, as the loss weight (λ) is a sensitive hyperparameter. LargeAug, created from
thousands of masks produces worse results overall than Tiny which has 217 masks. This
islikelyduetotheaforementioneddistributionimbalanceinthemasksproducinginforma-
tion redundant samples, further exacerbated by scale. Similarly, for raw unfiltered masks,
resultsindicaterebalancingandfilteringasaprogressivestep;howeverwiththerightmask
augmentations, sufficient diversity is introduced to make it competitive. We make similar
| observationswithourmethodontexturebugs(ref. |     |     | supplemental.) |     |     |     |
| ------------------------------------------- | --- | --- | -------------- | --- | --- | --- |

RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION 9
4 Discussion, Limitations and Future work
Our method, which utilizes weak-supervision to scale up a self-supervised objective im-
proves performance both through multi-task and pre-training. It consistently demonstrates
superiorperformancecomparedtosolelyusingasupervisedlow-labeleddataset. Ourself-
supervisionhoweverisdomain-craftedincontrastwithadvancesinrecentgeneral, lessbi-
ased approaches [3, 7, 18, 26]; we only make use of unlabeled data as a means to obtain
representativeobjectcentricmasks. Additionalinformationexistsinunsupervisedvideosto
becapturedthroughgeneralself-supervisedobjectives, forinstancewecanuserebalanced
masks with DINO [7, 26] to adapt the backbone. Our GM environment has shared, yet
inverted objectives to PUG [6]; [6] use interactive Unreal environments to serve as simu-
lators to obtain photorealistic data in a controlled manner whereas our target distributions
arethesimulatorsthemselves. Alimitationofourapproachisrelianceonthepolicyunder
whichdatawasgathered. TheintegrationofReinforcementLearningagents,suchas[1],is
an intriguing avenue for future research. Additionally, Fig. 5b highlights a challenge: our
filtering approach allows text-prompts to specify preference-based semantics, yet it strug-
gles when these semantics are fine-grained or not well-represented within the embedding.
Thus, the text-image model has difficulty performing in a zero-shot context. Future work
mightconsideradvancedtext-imagemodelsorexploringstrategiesthatcombinetext-image
prompting with other learning methods. Additionally, models adapted from SAM [10, 21]
canbeappliedduringsegmentationstagetoenhanceextractionofsemanticmasks.
The rapid testing cycles and cadence of new content make traditional label-intensive
learning impractical for visual bug detection. Despite game engines increasingly integrat-
ing ML capabilities, relying solely on integration isn’t scalable; our work moves towards
techniquesnotreliant onsourcecodeaccess. Further, newgamecontent canbeviewedas
OODdataandwehavetakenstepstowardsmethodsthatarerobustandgeneralizetosuch
scenarios,specificallyobjects. Futureworkmayexplorethescalabilityandgeneralityofour
methodology across various visual bug-types and OOD settings. What data requirements
existfordomainadaptationtoartstyles(eg. non-photorealisticgames),environments,light-
ing? Moreover,constrainingourselvestoRGB-onlyforpracticalreasonsfailstoexploitthe
richnessofmultimodality,limitingthedepthofvisualcuesourmodelsmaycapture. Multi-
modaldatacanbeusedduringtrainingandconstrainedorestimatedattesttime,maintain-
ingpracticality. Further,ouraugmentationstrategyusestraditionalCVtechniques,however
othersyntheticorgenerativemethodsmayalsobeaninterestinglineoffuturework.
5 Conclusion
Visualbugdetectionposesuniquechallengesduetorapidlyevolvingcontent,constraintsin
labeled data availability, and generalization to out-of-distribution scenarios. In this study,
weexploredaweakly-supervised,three-stagedapproachtoaddressthesechallenges,specif-
icallytargetingfirst-personplayerclipping(FPPC)withinGiantmap. Ourfindingsharness
the potential of large-pretrained visual models to enhance our training data. Our approach
allowsfortheinjectionofpriorsthroughprompting,bothgeometricandtext-based. Asig-
nificantadvantageofpromptablefilteringisitssimplicity,makingitaccessiblefornon-ML
professionals, allowing them to integrate their expert knowledge into the self-supervised
objective. Additionally, our framework shows promise in generating expansive, curated
datasets within video games, with the potential to foster both, comprehensive understand-
ingofvideogamescenesanddevelopingvisualbugdetectionmodels.

10 RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION
References
[1] Sherif Abdelfattah, Adrian Brown, and Pushi Zhang. Preference-conditioned pixel-
basedaiagentforgametesting,2023.
[2] RandallBalestriero, MarkIbrahim, VladSobal, AriMorcos, ShashankShekhar, Tom
Goldstein, Florian Bordes, Adrien Bardes, Gregoire Mialon, Yuandong Tian, Avi
Schwarzschild, Andrew Gordon Wilson, Jonas Geiping, Quentin Garrido, Pierre Fer-
nandez,AmirBar,HamedPirsiavash,YannLeCun,andMicahGoldblum.Acookbook
ofself-supervisedlearning,2023.
[3] AdrienBardes,JeanPonce,andYannLeCun. Vicreg: Variance-invariance-covariance
regularizationforself-supervisedlearning,2022.
[4] Benedikt Boecking, Willie Neiswanger, Eric Xing, and Artur Dubrawski. Interactive
weaksupervision: Learningusefulheuristicsfordatalabeling,2021.
[5] Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Syd-
ney von Arx, Michael S Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brun-
skill, et al. On the opportunities and risks of foundation models. arXiv preprint
arXiv:2108.07258,2021.
[6] FlorianBordes,ShashankShekhar,MarkIbrahim,DianeBouchacourt,PascalVincent,
andAriS.Morcos. Pug:Photorealisticandsemanticallycontrollablesyntheticdatafor
representationlearning,2023.
[7] Mathilde Caron, Hugo Touvron, Ishan Misra, Hervé Jégou, Julien Mairal, Piotr Bo-
janowski, and Armand Joulin. Emerging properties in self-supervised vision trans-
formers,2021.
[8] Ting Chen, Simon Kornblith, Mohammad Norouzi, and Geoffrey Hinton. A simple
frameworkforcontrastivelearningofvisualrepresentations,2020.
[9] Wei-YuChen,Yen-ChengLiu,ZsoltKira,Yu-ChiangFrankWang,andJia-BinHuang.
Acloserlookatfew-shotclassification,2020.
[10] Ho Kei Cheng, Seoung Wug Oh, Brian Price, Alexander Schwing, and Joon-Young
Lee. Trackinganythingwithdecoupledvideosegmentation,2023.
[11] JiaDeng, WeiDong, RichardSocher, Li-JiaLi, KaiLi, andLiFei-Fei. Imagenet: A
large-scalehierarchicalimagedatabase. In2009IEEEconferenceoncomputervision
andpatternrecognition,pages248–255.Ieee,2009.
[12] AlexeyDosovitskiy,LucasBeyer,AlexanderKolesnikov,DirkWeissenborn,Xiaohua
Zhai,ThomasUnterthiner,MostafaDehghani,MatthiasMinderer,GeorgHeigold,Syl-
vainGelly,JakobUszkoreit,andNeilHoulsby.Animageisworth16x16words:Trans-
formersforimagerecognitionatscale,2021.
[13] EpicGames. Unrealengine. URLhttps://www.unrealengine.com.
[14] Golnaz Ghiasi, Yin Cui, Aravind Srinivas, Rui Qian, Tsung-Yi Lin, Ekin D. Cubuk,
QuocV.Le,andBarretZoph. Simplecopy-pasteisastrongdataaugmentationmethod
forinstancesegmentation,2021.

RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION 11
[15] Spyros Gidaris, Praveer Singh, and Nikos Komodakis. Unsupervised representation
learningbypredictingimagerotations,2018.
[16] KaimingHe,XiangyuZhang,ShaoqingRen,andJianSun. Deepresiduallearningfor
imagerecognition,2015.
[17] Kaiming He, Haoqi Fan, Yuxin Wu, Saining Xie, and Ross Girshick. Momentum
contrastforunsupervisedvisualrepresentationlearning,2020.
[18] KaimingHe, XinleiChen, SainingXie, YanghaoLi, PiotrDollár, andRossGirshick.
Maskedautoencodersarescalablevisionlearners,2021.
[19] S C Johnson. Hierarchical clustering schemes. Psychometrika, 32:241–254, 1967.
URLhttps://api.semanticscholar.org/CorpusID:930698.
[20] Alexander Kirillov, Eric Mintun, Nikhila Ravi, Hanzi Mao, Chloe Rolland, Laura
Gustafson,TeteXiao,SpencerWhitehead,AlexanderC.Berg,Wan-YenLo,PiotrDol-
lár,andRossGirshick. Segmentanything,2023.
[21] Feng Li, Hao Zhang, Peize Sun, Xueyan Zou, Shilong Liu, Jianwei Yang, Chunyuan
Li, LeiZhang, andJianfengGao. Semantic-sam: Segmentandrecognizeanythingat
anygranularity,2023.
[22] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva Ra-
manan, Piotr Dollár, and C Lawrence Zitnick. Microsoft coco: Common objects in
context. InEuropeanconferenceoncomputervision,pages740–755.Springer,2014.
[23] CarlosLing,KonradTollmar,andLinusGisslén. Usingdeepconvolutionalneuralnet-
workstodetectrenderedglitchesinvideogames. InProceedingsoftheAAAIConfer-
enceonArtificialIntelligenceandInteractiveDigitalEntertainment,volume16,pages
66–73,2020.
[24] AlfredoNantes,RossBrown,andFredericMaire.Aframeworkforthesemi-automatic
testing of video games. In Proceedings of the AAAI Conference on Artificial Intelli-
genceandInteractiveDigitalEntertainment,volume4,pages197–202,2008.
[25] Muhammad Muzammal Naseer, Kanchana Ranasinghe, Salman H Khan, Munawar
Hayat, Fahad Shahbaz Khan, and Ming-Hsuan Yang. Intriguing properties of vision
transformers. AdvancesinNeuralInformationProcessingSystems, 34:23296–23308,
2021.
[26] MaximeOquab,TimothéeDarcet,ThéoMoutakanni,HuyVo,MarcSzafraniec,Vasil
Khalidov, Pierre Fernandez, Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby,
Mahmoud Assran, Nicolas Ballas, Wojciech Galuba, Russell Howes, Po-Yao Huang,
Shang-WenLi,IshanMisra,MichaelRabbat,VasuSharma,GabrielSynnaeve,HuXu,
Hervé Jegou, Julien Mairal, Patrick Labatut, Armand Joulin, and Piotr Bojanowski.
Dinov2: Learningrobustvisualfeatureswithoutsupervision,2023.
[27] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela
Mishkin,ChongZhang,SandhiniAgarwal,KatarinaSlama,AlexRay,etal. Training
language models to follow instructions with human feedback. Advances in Neural
InformationProcessingSystems,35:27730–27744,2022.

12 RAHMAN:WEAKSUPERVISIONFORLABELEFFICIENTVISUALBUGDETECTION
[28] F.Pedregosa,G.Varoquaux,A.Gramfort,V.Michel,B.Thirion,O.Grisel,M.Blon-
del, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau,
M.Brucher, M.Perrot, andE.Duchesnay. Scikit-learn: MachinelearninginPython.
JournalofMachineLearningResearch,12:2825–2830,2011.
[29] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sand-
hini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen
Krueger, and Ilya Sutskever. Learning transferable visual models from natural lan-
guagesupervision,2021.
[30] Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, and
IlyaSutskever. Robustspeechrecognitionvialarge-scaleweaksupervision,2022.
[31] Farrukh Rahman, Ömer Mubarek, and Zsolt Kira. On the surprising effectiveness of
transformersinlow-labeledvideorecognition,2022.
[32] Alexander Ratner, Stephen H Bach, Henry Ehrenberg, Jason Fries, Sen Wu, and
Christopher Ré. Snorkel: Rapid training data creation with weak supervision. In
Proceedings of the VLDB Endowment. International Conference on Very Large Data
Bases,volume11,page269.NIHPublicAccess,2017.
[33] MohammadRezaTaesiri,MoslemHabibi,andMohammadAminFazli. Avideogame
testingmethodutilizingdeeplearning. IranJournalofComputerScience,17(2),2020.
[34] MatildaTamm,OliviaShamon,HectorAnadonLeon,KonradTollmar,andLinusGiss-
lén. Automatictestingandvalidationoflevelofdetailreductionsthroughsupervised
learning. In 2022 IEEE Conference on Games (CoG), pages 191–198, 2022. doi:
10.1109/CoG51982.2022.9893682.
[35] Yonglong Tian, Yue Wang, Dilip Krishnan, Joshua B Tenenbaum, and Phillip Isola.
Rethinkingfew-shotimageclassification: agoodembeddingisallyouneed? InCom-
puter Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28,
2020,Proceedings,PartXIV16,pages266–282.Springer,2020.
[36] Unity. Unrealengine. URLhttps://unity.com/.
[37] Ross Wightman. Pytorch image models. https://github.com/rwightman/
pytorch-image-models,2019.
[38] RossWightman,HugoTouvron,andHervéJégou. Resnetstrikesback: Animproved
trainingprocedureintimm,2021.
[39] Benedict Wilkins and Kostas Stathis. World of bugs: A platform for automated bug
detectionin3dvideogames,2022.
[40] Benedict Wilkins, Chris Watkins, and Kostas Stathis. A metric learning approach to
anomalydetectioninvideogames,2020.
[41] JieyuZhang,Cheng-YuHsieh,YueYu,ChaoZhang,andAlexanderRatner. Asurvey
onprogrammaticweaksupervision,2022.
[42] Hong-YuZhou,ChixiangLu,SibeiYang,andYizhouYu. Convnetsvs.transformers:
Whosevisualrepresentationsaremoretransferable? InProceedingsoftheIEEE/CVF
InternationalConferenceonComputerVision,pages2230–2238,2021.