---
title: "VideoGameQA Bench Evaluating Vision Language Model"
author: "Taesiri"
year: "2025"
source_file: "04_benchmarks_and_datasets/Taesiri_2025_VideoGameQA_Bench_Evaluating_Vision_Language_Model.pdf"
source_sha256: "fee2a10c257ac85e9adce0fd00291268b51bd71999e0e26fe47bba5b445cf1d6"
converted_at: "2026-11-06T15:12:53.234824+00:00"
markitdown_version: "0.1.9"
char_count: 154896
---
| VideoGameQA-Bench:     |           | Evaluating                                 | Vision-Language |     |
| ---------------------- | --------- | ------------------------------------------ | --------------- | --- |
| Models                 | for Video | Game Quality                               | Assurance       |     |
| MohammadRezaTaesiri    |           | AbhijayGhildyal                            |                 |     |
| UniversityofAlberta,CA |           | SonyInteractiveEntertainment,AlisoViejo,US |                 |     |
| mtaesiri@gmail.com     |           | abhijay.ghildyal@sony.com                  |                 |     |
5202 ceD 81  ]VC.sc[  2v25951.5052:viXra
| SamanZadtootaghaj |     |     | NabajeetBarman |     |
| ----------------- | --- | --- | -------------- | --- |
SonyInteractiveEntertainment,Berlin,Germany SonyInteractiveEntertainment,London,UK
| saman.zadtootaghaj@sony.com |     | nabajeet.barman@sony.com |     |     |
| --------------------------- | --- | ------------------------ | --- | --- |
Cor-PaulBezemer
UniversityofAlberta,CA
bezemer@ualberta.ca
Abstract
Withvideogamesnowgeneratingthehighestrevenuesintheentertainmentindus-
try,optimizinggamedevelopmentworkflowshasbecomeessentialforthesector’s
| sustainedgrowth. | RecentadvancementsinVision-LanguageModels(VLMs)offer |     |     |     |
| ---------------- | ---------------------------------------------------- | --- | --- | --- |
considerablepotentialtoautomateandenhancevariousaspectsofgamedevelop-
ment,particularlyQualityAssurance(QA),whichremainsoneoftheindustry’s
| most labor-intensive | processes | with limited automation | options. | To accurately |
| -------------------- | --------- | ----------------------- | -------- | ------------- |
evaluatetheperformanceofVLMsinvideogameQAtasksanddeterminetheir
effectivenessinhandlingreal-worldscenarios,thereisaclearneedforstandardized
benchmarks,asexistingbenchmarksareinsufficienttoaddressthespecificrequire-
| mentsofthisdomain. | Tobridgethisgap,weintroduceVideoGameQA-Bench, |     |     |     |
| ------------------ | --------------------------------------------- | --- | --- | --- |
acomprehensivebenchmarkthatcoversawidearrayofgameQAactivities,includ-
ingvisualunittesting,visualregressiontesting,needle-in-a-haystacktasks,glitch
detection,andbugreportgenerationforbothimagesandvideosofvariousgames.
| Codeanddataareavailableat: |     | https://asgaardlab.github.io/videogameqa-bench/. |     |     |
| -------------------------- | --- | ------------------------------------------------ | --- | --- |
1 Introduction
The global video game industry continues to expand rapidly, with its market value projected to
reach$257billionby2028[11]. Alongsidethissubstantialgrowth,theprocessofdevelopinghigh-
qualityvideogamesremainsinherentlycomplexanddemanding. Acriticalchallengewithingame
developmentistoensurevisualqualityandconsistencythrougharigorousvisualtestingandquality
assurance(QA)process. AutomationofvisualQAtasksremainsparticularlychallenging[6,23,25,
29,31,37,39,43–45,47,55,67]andcurrently,mostvisualQAreliesheavilyonmanualinspection,
makingtheprocesstime-consuming,costly,labor-intensive,andpronetohumanerror[35,36].
ThevisualQAprocessforvideogamescangenerallybeabstractedintothreemaintypesoftasks:
(1) verifying scene integrity by comparing the visual representation of scenes against intended
configurationsandknownreferencestates,suchasanoracle(Fig.1-a)orpreviouslyrenderedversions
ofthesamescenes(Fig.1-b);(2)detectingglitchesthroughopen-endedexploration—theseglitches
areunintendedgameplay(Fig.1-e)orvisualartifacts(Fig.1-h)withoutspecificreferencepoints,
requiringtesterstorelyoncommonsenseandgeneralknowledgefordetection;and(3)systematically
Preprint.

Figure 1: Sample tasks from VideoGameQA-Bench. (a) A unit test where the model should
verify small details in the image, such as character’s orientation and background. (b) A visual
regressiontestwherethemodelshoulddetectunacceptablechangesbetweentwoversionsofthe
samescene. (c) AUIunittestinwhichthemodelmustvisuallyverifyuserinterfacecomponents,
suchasachemistrygraphbetweenplayers.(d) Abugreportgenerationtaskwherethemodelneeds
togenerateabugreportforaglitch. (e) Twoglitchdetectiontasks,wherethemodelmustidentify
visualanomalies,suchasunnaturalbodyconfiguration(left)orobjectclipping(right,fingersclipping
theapple). (f) Twoglitchdetectiontasks,wherethemodelisrequiredtoverifytheglitch-freestatus
ofimageswithintentionalobjectclippingandhighscenecomplexity. (g) Aparametrictestthat
evaluateswhetherthemodelcandetectclippingatvariousobjectproximities. (h) Aneedle-in-a-
haystacktask,whichrequiresthemodeltoidentifythefirstframeinwhichaglitchoccurs.
reportinganddocumentingallidentifiedglitches(Fig.1-d),ensuringdevelopersreceiveclearand
actionableinformationtoaddressproblemseffectivelyduringgamedevelopment.
Recent advancements in vision-language models (VLMs) [3, 9, 16, 32, 68] present promising
opportunities to automate and significantly enhance the efficiency of video game QA. However,
progressinapplyingVLMstogameQAhasbeenlimitedbythelackofstandardizedbenchmarks.
Currentmultimodalbenchmarkstendtofocusheavilyoncomplexmathematicalortextualreasoning
tasks[27,61,62],overlookingessentialvisualcomprehensiontasksfundamentaltovideogameQA.
Similarly,existinggame-specificbenchmarks[5,45–47]oftenrepresentonlynarrowaspectsofQA
tasks,thusinadequatelyevaluatingandtrackingVLMperformanceacrossdiverseQAscenarios.
Inthispaper,weintroduceVideoGameQA-Bench,abenchmarkdesignedtofillthegapinevaluat-
ingVLMsforvideogameQA.Ourkeyfindingsandcontributionsareasfollows:
1. WepresentVideoGameQA-Benchfeaturing9distincttasksand4,786questionsdesigned
considering real-world video game development scenarios, such as visual unit testing,
regressiontesting,UIvalidation,videoneedle-in-a-haystack,andglitchdetection.
2

2. While VLMs show promising performance on various multimodal benchmarks and can
functionasOCRsystems,theyperformpoorlyatdetectingfinedetailsrequiredforaccurate
sceneunderstandingandparsingcomplexUIelements. (Sec.5.1)
3. FrontierVLMsshowgoodperformanceontheglitchdetectiontaskusingimages(upto
82.8%)andvideos(upto78.1%);however,allstrugglewhenitcomestoglitchesrelatedto
bodyconfiguration,intricateobjectclipping,andcommon-sensereasoning. (Sec.5.2)
4. VisualregressiontestingremainsoneofthemostchallengingtasksforVLMs. (Sec.5.3)
5. Locating specific glitch moments in videos remains a challenge, both in detecting and
accuratelypinpointingtheglitch. (Sec.5.4)
6. FrontierVLMscangenerateusefulbugreportsforupto50%ofreal-worldglitches,provid-
ingaccurateanddescriptivesummariesoftheglitches. (Sec.5.5)
2 Background
Weuseglitchasanumbrellatermforunintended,user-visibleanomaliesthatoccurduringgameplay.
Theanomaliesweconsiderarevisuallyevidencedinimagesorvideos. Thisincludesboth(i)low-
levelgraphicaldefectsdirectlyobservableinpixelsand(ii)higher-levelsceneinconsistenciesthat
violatephysics,gameplaylogic,orcommonsensebutstillmanifestvisually(e.g.,anNPCfloating
mid-air). Non-visualanomalies(e.g.,audio-relatedanomalies)areoutofscopeforourevaluation.
Tobalanceclarityforreaders,wegroupglitchesintotwobroadfamiliesbasedonhowtheyappear
inimagesorvideos;thecategoriesarenotmutuallyexclusive,andasinglefailurecanexhibittraits
of both. We make this choice to help readers interpret the examples more easily, since industry
taxonomies—oftenorganizedbyunderlyingcausesuchasrendering,physics,orAIlogic—donot
alwaysalignwithwhatcanbedirectlyobservedinvisualdata.
Graphicalglitches: Local,pixel-orgeometry-levelfailuresinimageformationthatdegradevisual
fidelitywithoutnecessarilychangingtheintendedscenesemantics.
• Missingorcorruptedassets/textures: gray/purple“checkerboard”materials,blacked-out
meshes,textureswimming/smudging(Sec.F.1).
• Geometryandrasterizationissues: z-fighting,explodedorinside-outmeshes,vertexnormal
errors,shadowacne(Sec.F.2).
• Temporal instability: flicker between LODs/materials, aliasing or shimmer that persists
acrossframes(Sec.F.3).
• Post-processing and UI artifacts: ghosting, overdraw halos, HUD elements duplicat-
ed/misalaligned,compression/mipmapartifacts(Sec.F.4).
Logical(semantic)glitches: Visuallycoherentpixelsarrangedintoscenesthatviolatephysics,
gameplayrules,orcommonsense,yieldingcontextuallyincorrectoutcomes.
• Physicsandcollisionfailures: characterorpropsintersectingwalls(“clipping”), falling
throughfloors,floatingobjects,zero-gravityactors(Sec.F.5).
• Animation/stateerrors: frozenT-poses,limbcontortions,mocapdesync,ragdollssnapping
upright,rapidteleportation/jumps(Sec.F.6).
• Worldandruleviolations: doorsopenwithnotrigger, enemiesspawninsidetheplayer,
itemsduplicateorvanishwithouteffect(Sec.F.7).
3 VideoGameQA-Bench
We designed VideoGameQA-Bench ’s tasks by simulating realistic QA scenarios encountered
duringactualvideogamedevelopment.However,tomakethebenchmarkmorerelevantforfutureQA
automationtasks,wealsoincludedtasksthatmaychallengecurrentsoftwareengineeringpractices
while also remaining highly relevant. Tab. 1 gives an overview of the contents of each task. In
summary, VideoGameQA-Bench contains 2,236 image-based samples and 1,200 video-based
samplesfrommorethan800gamesand9syntheticgamescenes.
3

3.1 Tasks
Image-BasedTasks
1. Visualunittesting: Visualunittestsverifyvisualattributesincludingpresence,placement,
positioning,colors,conditions,andotherrelevantpropertiesofvariousimageelements.
2. UIunittesting: UI(visual)unittestsverifyin-gameUIelementssuchasmenus,subtitles,
heads-updisplays(HUDs),andinterfacecomponentslikegraphsandcharts. Wesimulate
the(UI)unittestingtasksbyaskingtheVLMquestionsaboutgamescreenshots.
3. Visual regression testing: Visual regression tests check for unintended visual changes
afterachangetothegame. Asimplepixel-by-pixelcomparisonoftwoscreenshotsisnot
sufficient,assomevariations(e.g.,becauseofcharactercustomizationorweatherconditions
inthegame)maybeacceptable. Visualregressionsmayoccurincinematicpartsofthe
game,suchascutscenesthathaveadefinedsequenceflow. Wesimulatethistaskbyasking
theVLMtocomparewhethertwoscreenshotsaresimilar,takingintoaccountthespecified
(un)acceptablevariations.
4. Glitchdetection: Glitchdetectionistheprocessofidentifyingunintendedvisualerrors,
suchasrenderingissues,clipping,orphysics/logicalbugsthatexpressthemselvesvisually.
WesimulatethistaskbyaskingtheVLMwhetherglitchandglitch-freeimagescontaina
glitch.
5. Parametricclippingdetection: Giventhecommonoccurrenceofclippingingames,our
benchmarkincludesadedicatedtasktoevaluateamodel’sabilitytodetectsuchglitches. In
thistask,imagesfeatureanobject(e.g.,acube,sphere,orcharacter)positionedatvarying
distancesfromahumancharacter–fromfaraparttofullyoverlapping/clipping. TheVLM
isaskedwhetheritdetectsclippingacrosseachofthesedistances.
6. Bugreportgeneration: Inadditiontotesting/detectiontasks,apotentialapplicationof
VLMsistoassistQAengineerswithwritingreportsfordetectedbugs. Wesimulatethistask
byaskingtheVLMtowriteadescriptionofaglitchimagethatcanbeusedinabugreport.
Video-BasedTasks
1. Glitchdetection: Glitchdetectioninvideoscanbedonetoverify(autonomous)gameplay
sessions from bots. Detecting glitches in videos is significantly more complex due to
challenges such as analyzing motion (patterns), and may require identifying transient
glitchesthatappearonlybrieflyinafewframes. WesimulatethistaskbyaskingtheVLM
whetheritdetectsaglitchinavideo.
2. Needle-in-a-haystack(NIAH):NIAHisamorechallenginglong-contextretrieval[53,66]
versionoftheglitchdetectiontask. WesimulatethistaskbyaskingtheVLMwhetherit
detectsaglitchinavideo,andinwhichframetheglitchoccursforthefirsttime.
3. Bugreportgeneration: Inthistask,theVLMisaskedtoprovideadescriptionofaglitch
videothatcanbeusedinabugreport.
3.2 DataCollection
WeconstructedVideoGameQA-Benchusingreal-worldandsyntheticsourcestoensurediversity,
realism,andcontrolledconditions. Wenextdetailthecompositionandcollectionprocessesforeach
datatype. Itshouldbenotedthatthedatacollectionprocesswassolelycarriedoutbyresearchers
fromtheUniversityofAlberta.
Real-worldsamples:Wesourcedreal-worlddataforthevisual&UIunittesting,glitchdetectionand
bugreportgenerationtasks. Forimage-basedtasks,wegathereddiversescreenshotsfromtheSteam
Community( )imagegallery. Tofindimageswithpossibleglitches,weusedkeywordsearchto
findrecentimagestaggedwiththeword“bug”. Forthevideo-basedglitchdetectiontask,weutilized
gameplayvideosfromtheGamePhysics( )dataset[45]. Tocomplementthissetwithglitch-free
videos,werandomlyextracted15-secondgameplayvideos—matchingthemediandurationofvideos
in the GamePhysics dataset—from gameplay walkthroughs available on YouTube ( ). We also
randomlyselected100imagesand100videosfromthesesetsforthebugreportgenerationtask.
Syntheticsamples: WeusedtheUnity( )gameenginetocreatesyntheticsamplesfortasksrequir-
ingcontrolledsettings. Fortheclippingdetectiontask,wesystematicallyvariedthespatialproximity
4

Table1: Overviewoftasks,theirdatasources,andexpectedformat/contentsoftheresponsestothe
questionsinVideoGameQA-Bench. AllresponsesmustbeformattedinJSON.
Type Task N Source Diversity Annotation ExpectedResponse Samples
egamI
Visualunit 100 92games , Objectproperties Sec.H.1
UIunit 100 94games , UIproperties Sec.H.2
Visualregression 250 9scenes , Pass/fail Sec.H.3
Glitchdetection 1,000 507games Detected/notdetected Sec.H.4
Parametricclippingdet. 686 9scenes,4games Clipping/notclipping Sec.H.5
Bug-reportgeneration 100 61games Free-formatdescription Sec.H.6
oediV
Glitchdetection 1,000 778games Detected/notdetected Sec.H.7
Detected/notdetected
NIAH 100 9scenes Sec.H.8
+framenumber
Bug-reportgeneration 100 70games Free-formatdescription Sec.H.9
between3DobjectswithinUnityscenes. Ahumancharactermodelispositionedcentrally,andwe
incrementallymovedotherobjects—includingacube,sphere,2Dplane,andanothercharacter—from
aninitialdistanceof15unitstowardsthecentralcharacter. Thismovementcontinuedprogressively
untiltheobjectsfullyclippedintoandbecameembeddedwithinthecharactermodel.
FortheNIAHtask,wecreated50-secondgameplayclipsinUnityandintentionallyinjectedglitches
asthe“needle”atknowntimestamps.Forthisset,weusedfourtypesofglitches:(1)flickering,which
causespartsofagameobjecttoflickerrapidly;(2)suddendisappearance,whereanobjectsuddenly
vanishes;(3)objectjump,whereagameobjectisrapidlythrownintotheair;and(4)missingtexture,
wherethetextureofagameobjectismissing.
Mix of real-world and synthetic samples: For the visual regression testing task, we combine
Unity-generatedcontentwithcutsceneglitchessourcedfromYouTubevideos. Weselectednine
distinct scenes from the Unity Asset Store, generating modified versions by randomly removing
specificobjects. Wethenpairedcapturedimagesfromthesemodifiedsceneswithimagesfromtheir
unalteredreferenceversions. Wefurtheraugmentedthissetwith70glitchinstancesfromcutscenes
invariousgamesonYouTube. Here,framesfromglitchedcutscenerecordingswerematchedwith
correspondingframesfromtheglitch-freecutscenes,creatingadatasetofpairedframes.
3.3 DataAnnotationandLabelVerification
Manualannotationandverification: We( )manuallyreviewedthecollectedimagesandvideos,
labelingthemaseitherglitchorglitch-free. Forbugreportgeneration,weincludeabriefdescription
oftheglitch.
Wefollowedamulti-stepverificationprocess,regardlessofexistinglabelsorannotations. Allimages
andvideosunderwentasequentialreviewinvolvingthreeauthorstovalidatetheirqualityandconfirm
accuratelabeling. Thisprocesshelpedpreventthepropagationofincorrectannotationsfromprevious
datasetsintoVideoGameQA-Bench.
VLM and human in the loop: Visual unit tests and UI unit tests require constructing both the
question and the answer. For these tasks, we used Gemini-2.5-Pro ( ) to initially draft a set of
questionsbasedoncomprehensiveinstructions(Sec.B).Wethenanalyzedthedraftedquestions,
mergedandrefinedthem,andfixedthegroundtruthtocreateafinalquestionbasedontheinitial
samplesprovidedbyGemini-2.5-Pro.
Automatedannotation: ForsyntheticdatageneratedviaUnity,weexportedannotationsdirectly
fromtheUnitygameengine. Thisensuredexactalignmentbetweentheannotationsandthevisual
stateoftheimagesorvideos,preciselyindicatingthepresenceorabsenceofglitches. Forexample,
fortheNIAHsamples,adedicatedC#scriptsystematicallystartstherecording,injectsaglitchata
randomtimeframe,andexportsboththevideosandtimestamps.
5

JSONstructure: Tofacilitateinteroperabilityandautomation,weexplicitlyenforcethatallground
truthlabels(andtherefore,eachexpectedmodeloutput)inourdatasetarevalidJSONobjects. To
guidethemodelstowardthedesiredJSONschema,eachquestionincludesanemptyJSONtemplate,
andweinstructthemodeltoreturnitsfinalresponseinthatformat.
To avoid suppression of chain-of-thought (CoT) [54], we include a Reasoning field in the JSON
response,allowingthemodeltousetheallocatedspaceto“think”[2]beforereturningtheresponse
fortasksthatrequireheavyreasoning. Alltasks,exceptforvisual(UI)unittests,containthisfield.
4 Experiments
VLMs:Weevaluatedatotalof11proprietaryand5open-weightmodelsonVideoGameQA-Bench.
Ourevaluationincludesbothstandardmodelsandthosedesignedforextendedreasoning[1,8,42,58].
Promptingvideos: OnlytheGeminifamilyacceptsvideoasanativeinputformat;othermodels
processvideosassequencesofframes. Toevaluatenon-Geminimodels,wesampleoneframeper
secondforallvideo-basedtasks. Foropen-weightmodels,wereducethesamplingratetoensurethey
canhandletheimages(seeSec.Afordetails).
Videoframesamplingrate: Weadoptedauniformsamplingstrategyof1FPS,meaningthateach
secondofgameplaycontributesoneframetotheevaluationinput,ensuringfairnessacrossmodels
withvaryinginputconstraints.
GlitchvisibilityatlowFPS:Sincemostevaluatedmodelscannotprocesslongframesequences,we
standardizedvideosamplingat1FPS.Toverifythatthisdownsamplingdoesnotobscureanomalies,
wemanuallyreviewedasubsetofglitch-containingvideosandfoundthatin95%ofcases,theglitch
remainedclearlyvisibleat1FPS.
ValidJSONoutput: Allbenchmarkquestionsexplicitlyrequiremodelstooutputresponsesina
validJSONformat. AnyresponsesnotinJSONorcontainingmalformedJSONstructureswillbe
disregarded,evenifthemodel’soutputisonlyslightlydifferentfromthegroundtruthlabel.
LLM-as-a-judge: Both bug-reporting tasks require models to generate descriptive bug reports
basedonprovidedglitchyimagesorvideos. Evaluatingthesereportsposeschallengesduetotheir
open-endednature,makinghumanverificationoranLLM-basedjudgenecessary. Followingrecent
literature[17],weuseanLLM-basedjudge,specificallytheOpenAIo3model,toassesstheaccuracy
ofthegeneratedreportsbycomparingthemtotextualgroundtruthreferencesdetailingtheglitches.
DetailsaboutpromptconstructionareavailableinSec.E.
Modelranking: Werankedmodelsbyaveragingaccuraciesacrossimageandvideotasks. Task-wise
accuracieswerefirstaveragedwithineachtype,thencombinedforthefinalscore.
DetailsregardingmodelinferenceandpromptdesignareprovidedinSecs.A,CandD.
5 Results
Tab.2summarizesresultsacrossallbenchmarktasks;wehighlightkeyfindingsandexaminemodel
strengthsandlimitationsintheremainderofthissection. Allmodelsreliablyproducedtask-specific
JSONoutputs,withmalformedresponsesbeingrareandmostlylimitedtocomplexUIandunit-test
tasks. DetailedstatisticsonmodelrefusalratesandmalformedoutputsareprovidedinSec.G.3.
5.1 VLMsMostlyFailtoDetect,Translate,andRepresentIntricateSceneDetails
Whydoesthismatter: Insoftwareengineering,unittestsareassertionsthatverifyanisolatedpiece
ofcodebehavesasintended. Applyingthesamedisciplinetorenderedframesisequallyvaluable:
visualunittestscanassertthattheappearanceandon-screentextofvisualelements(includingthe
UI)meetaspecification. VLMscouldmakethispractical:whenpromptedwithaspecificimage,they
candescribefine-grainedvisualdetails(e.g.,acharacter’sattireorpose)andreadtextualelements.
Thiscapabilitywouldallowteststocomparetheseoutputsagainstreferencedescriptions,flagging
mismatchesearlyinthepipeline.
6

Table2: Accuracy(%)scoresofmodelsonVideoGameQA-Bench. VU:Visualunittesting;UI:
UIunittesting;VR:Visualregressiontesting;IGD:Image-basedglitchdetection;PCD:Parametric
clippingdetection;IBR:Image-basedbugreportgeneration;VGD:Video-basedglitchdetection;
NIAH:Needle-in-a-haystack;VBR:Video-basedbugreportgeneration. Numbershighlightedwith
†indicatethatthescorefortheNIAHtaskwassetto0. TheTotalcolumnshowsthemeanofthe
averagescoresfromtheimageandvideotasks.
Image Video Average
VU UI VR IGD PCD IBR VGD NIAH VBR Img. Vid. Total
Model/#Samples 100 100 250 1,000 686 100 1,000 100 100 2,236 1,200 3,436
GPT-4.1 43.0 28.0 28.8 81.3 87.8 51.0 75.8 19.0 51.0 53.3 48.6 51.0
GPT-4.1-mini 42.0 30.0 20.4 76.8 66.9 46.0 71.8 10.0 26.0 47.0 35.9 41.5
GPT-4.1-nano 9.0 14.0 19.2 57.0 66.9 16.0 49.1 4.0 14.0 30.4 22.4 26.4
GPT-4o 39.0 23.0 31.6 82.8 82.5 54.0 57.0 1.0 52.0 52.2 36.7 44.4
o4-mini 50.0 35.0 45.2 76.4 65.0 38.0 70.0 18.0 28.0 51.6 38.7 45.1
o3 43.0 28.0 39.6 73.7 80.5 53.0 76.8 13.0 45.0 53.0 44.9 48.9
Gemini-2.5-Pro 53.0 40.0 30.8 75.4 72.2 33.0 78.1 34.0 36.0 50.7 49.4 50.0
Gemini-2.5-Flash 47.0 24.0 26.4 66.3 72.2 24.0 64.7 35.0 23.0 43.3 40.9 42.1
Gemini-2.0-Flash 44.0 28.0 12.0 68.1 78.0 20.0 54.5 36.0 26.0 41.7 38.8 40.3
Sonnet-3.7 23.0 22.0 24.0 65.1 76.4 29.0 66.9 31.0 22.0 39.9 40.0 39.9
Sonnet-3.5 23.0 29.0 14.0 70.1 72.9 33.0 61.2 27.0 26.0 40.3 38.1 39.2
Llama-4-Scout 32.0 23.0 13.6 55.8 71.6 8.0 58.6 – 5.0 34.0 21.2† 27.6†
Llama-4-Maverick 21.0 22.0 18.4 53.2 65.7 7.0 56.6 – 15.0 31.2 23.9† 27.5†
Gemma-3(27B) 12.0 12.0 12.8 46.7 69.7 10.0 51.3 – 9.0 27.2 20.1† 23.6†
Mistral-Small-3.1(24B) 15.0 17.0 25.6 59.7 62.5 9.0 61.4 – 14.0 31.5 25.1† 28.3†
Qwen-2.5-VL(72B) 38.0 27.0 21.2 70.0 76.0 19.0 47.9 – 17.0 41.9 21.6† 31.7†
Results:OurexperimentsshowthatVLMsconsistentlystrugglewithfine-graineddetails,particularly
whentaskedwithtranslatingspecificdetailsandpropertiesofobjects,aswellasreadingcharts,text,
andotherinformationinthescene. OnboththevisualandUIunittestingtasks,allmodelsperform
poorly,withGemini-2.5-Probeingthebestmodel(53.0%onvisualand40.0%onUIunittesting).
VLMsoftenstrugglewithfine-grainedsceneunderstanding,especiallywhenitcomestointerpreting
objectconfiguration,spatialrelationships,andsubtlevisualcues[19]. Theyfrequentlymisinterpret
characterposture(e.g.,numberofvisibleeyes,handposition,ororientation),objectplacement(e.g.,
whetheranobjectisinsideoroutsidearoom),andthestateofelementslikewhetheracardooris
openorclosed(Fig.A19). Theseerrorsaremorepronouncedwhenpropertiesaresmallorvisually
ambiguous, though failures also occur in clearer scenarios. Even seemingly simple tasks—like
determiningthedirectionanobjectisfacingorcountingelements—oftenleadtoinconsistentresults,
highlightinglimitationsincurrentmodelcapabilitiesfordetailedvisualreasoning.
DespitethepromisingperformanceofVLMsforOCRtasks[30,41],accuratelyextractingstructured
informationfromcomplexgameUIelementsremainsasignificantchallenge. WhileVLMshandle
plaintextandsimpleinterfaceslikebasicgamemenusreasonablywell,theirperformancedeclines
withlayoutsinvolvinglargetables,progressbars,andelementssuchasminimaps. Interpretingcharts
andgraphswithinterconnectednodesandedgesisalsounreliable,asmodelsconsistentlystruggleto
followedgesinthegraphandunderstandtheinformationpresentedinthisformat(Fig.A20).
OurfindingsalignwithpriorstudieshighlightingthelimitationsofVLMsinfine-grainedperception
andspatialreasoning[38,49]. Improvementsinspatialreasoningandlocalizationareessentialbefore
VLMscanbereliablyusedindetail-sensitivetaskslikevisual(UI)unittesting.
5.2 VLMsCanDetectManyVisualGlitches,ButStrugglewithCertainTypes
Whydoesthismatter: GlitchdetectionisacorecomponentofgameQA,oftenrequiringextensive
manualreviewduetothecomplexityandvarietyofvisualerrorsthatcanariseduringgameplay[20].
LeveragingVLMsforglitchdetectioncouldgreatlyreducetheneedformanualreview.
Results: VLMs,especiallyproprietaryones,demonstrategoodperformanceinidentifyingvisual
glitches(e.g.,withGPT-4oachievinganaccuracyof82.8%). Thisshowsastepforwardinglitch
detectioncapability: priorworkshowedthatthebest-performingmodelcouldreachaglitchdetection
accuracyofonly57.2%[47]. Thebest-performingopen-weightmodel,Qwen-2.5-VL,achievesan
7

(a) Spatial reasoning (d) Body configuration (images and videos)
1 2 3
(b) Complex UI (items in the grid) (e) Detecting changes
(c) Common-sense (f) Temporal analysis (object movement/shaking)
1 2 3
Figure2: SamplesfromchallengingcasesthatmostVLMsconsistentlystrugglewith. (a)Failureto
understandspatialreasoning,suchasobjectorientation(whetheranairplaneisfacingtowardthe
cameraoraway). (b)FailuretoreadUIswithcomplexlayoutsandobjectsarrangedingrids. (c)
Failuretodetectcommon-senseinconsistencies,suchasamissingguninthehand. (d)Failureto
detectunnaturalbodyconfigurations. (e)Failuretodetectmissingforegroundobjects(candles).
(f)Failuretodetectandanalyzeobjectmovementsuchasshakingorbouncing.
accuracyof70.0%matchingtheperformanceofSonnet-3.5. Incontrast,Gemma-3labelsnearly
allsamplesas“glitch,”resultingin100%recallbutlessthan2%specificity. Conversely,Llama-4-
MaverickandLlama-4-Scoutlabelalmostallsamplesas“clean,”exhibitingrecallatorbelow14%
andspecificityexceeding95%. FurtherdetailsonperformancemetricsareprovidedinSec.G.4.
Inthevideo-basedsetting,Gemini-2.5-Proachievesthehighestperformanceat78.1%. Comparedto
image-basedtasks,proprietarymodelsgenerallyperformslightlyworseonthistask: GPT-4.1(–5.5),
o4-mini(–6.4),withtheexceptionofo3(+3.1)andGemini-2.5-Pro(+2.7).
A major limitation observed across models in video-based glitch detection is that they process
individualframesratherthanentirevideosnatively, resultinginthelossoftemporalcontextand
audiosignals(Fig.2-f). Additionally,somemodels,suchasGPT-4o,frequentlyrefusetogenerate
validresponsestovideo-basedqueries.
Duringourmanualanalysis,weobservedthatcertaintypesofvisualglitchesremainparticularly
challengingforeventhebest-performingmodel,inbothimage-andvideo-basedsettings:
1. Unusualbodyconfiguration: Charactersappearwithhighlyunnaturaljointalignmentsor
distortedposes,typicallyresultingfromragdollphysicssimulationsorincorrectanimation
states(e.g. anunusualpositionofhandsorarmsinFig.1-eandFig.2-d).
2. Intricateobjectclipping: Twoormoreobjectsintersectslightly,forexample,characters
renderedinoverlappingpositions,propspenetratinghands,orlimbspassingthroughsolid
geometry(e.g. anappleclippingwithahandinFig.1-e).
3. Semantic glitches: Contextual inconsistencies that require common-sense reasoning to
interpret. For instance, a character may appear to be holding a weapon based on their
posture,buttheweaponiseithermissingorfailstorenderproperly(Fig.2-c).
Weusedo3toidentifycommonpatternsamongfalse-positivecasesproducedbythetop-performing
models. Specifically, we prompt o3 to summarize the reasoning field from the JSON outputs of
8

GPT-4o,GPT-4.1,andGemini-2.5-Pro. Themostcommonfalse-positivepatternsstemfrommodel
hallucinations about clipping glitches that do not actually exist (Secs. G.6 and G.8). To further
stress-testthemodelsforclippingglitches,weconductedparametricclippingdetectiontoanalyze
modelbehavioracrossvariousdistancesandcomplexities.
Ourparametrictestshowsthatwhilemodelscangenerallydetectclippingglitches,theylackrobust-
ness. Inparticular,onborderlinecases(i.e. wheretwoobjectsonlyslightlyoverlap),modelsusually
failtorecognizeclippingissues. Forexample,althoughGPT-4.1—achieving87.8%—isthemost
robustmodel,itstillconsistentlyfailstodetectsuchboundarycases(Sec.G.11).
Despitetheimprovementsinglitchdetectionperformance,fullyautonomousglitchdetectionusing
onlyVLMsmightnotyetbefeasibleforreal-worlduse. Highfalse-positiverates(seeSec.G.4for
details)continuetoposeasignificantissue,potentiallyoverwhelminghumantesterswithunnecessary
reviews, especially given that most frames in real-world gameplay are glitch-free. Additional
considerationsforreal-worldapplicabilityarediscussedinSec.G.5.
5.3 VLMsAreBadatVisualRegressionTesting
Why does this matter: Verifying an image against a previously approved reference is a highly
desirableformoftestingincomputergraphicsandvideogames[13,48,50]. Thisneedisespecially
acute in video games, where recurring sequences often include customizable elements, such as
characterappearances,ordynamicenvironmentalchangeslikeday/nightcyclesandweathervariations.
RecentadvancementsinimagecomparisoncapabilitiesofVLMs[3,21,63,68]showthatVLMs
maybewell-suitedtothistaskbecause,throughcarefullydesignedpromptsandin-contextexamples,
weshouldbeabletoeffectivelyprogramthemtoignorepermissiblevariations,suchaschangesin
weatherorlighting,whilestillverifyingallothercriticalaspectsoftheimage.
Results: OurresultsindicatethatvisualregressiontestingwithVLMsdoesnotyetperformwell:
o4-mini, the best-performing model, achieves an accuracy of 45.2%. Qualitative analysis further
showsthatallmodelsconsistentlyfailtodetectarangeofchanges,whethersubtle,likeanobjectin
thebackground(Fig.A39),orpronounced,closetothecamera(Fig.2-e).
Anotabletrendisthatreasoningvariantsconsistentlyoutperformtheirnon-reasoningcounterparts
withinthesamemodelfamily—forexample,o3versusGPT-4o(39.6%vs. 31.6%)andSonnet-3.7
versusSonnet-3.5(24.0%vs. 14.0%). Thistrenddoesnotappearintheglitchdetectiontask. A
plausibleexplanationisthatareasoningmodelcaniterativelyexaminemultipleaspectsandobjects
inthetwoimagesbeforereachingafinaldecision;nevertheless,overallperformanceremainspoor.
5.4 VLMsCanDetectGlitchesinGameplayVideos,butStruggletoPinpointTheirOnset
Whydoesthismatter: OneofthegoalsinvideogameQAistoaugmentgame-playingbots(e.g.
usingreinforcementlearning[4])withautomaticglitchdetectionsystems. Game-playingbotscan
interactwiththegameandgeneratemanylengthyvideorecordings. Avaluablecapabilityinthis
contextwouldbeasystemthatcanefficientlylocalizeglitchesinsuchvideos.
Results: TheresultsfromtheNIAHtasksindicatethatmostmodelsstrugglesignificantlywiththis
task. Gemini-2.0-FlashandGemini-2.5-Flasharethebest-performingmodels,yettheyachieveonly
36.0%and35.0%accuracyinlocatingthefaultyframewithina5-seconderrormargin.Thisrelatively
lowperformanceprimarilystemsfromtwofactors: (1)themodelcompletelyfailstodetecttheglitch
inthevideo,or(2)itdetectsthatthereisaglitchbutfailstocorrectlylocatethecorrespondingframes.
Forinstance,GPT-4.1detectsglitchesin72outof100videos(72%detectionrate),butamongthese,
itaccuratelylocatesthefaultyframeinonly19cases(26.5%)(seeSec.G.10).
5.5 VLMsCanCorrectlyDescribeGlitchesinBugReportsforMoreThanHalfoftheCases
Whydoesthismatter: VLMsshouldbeabletoassistintheaccuratedocumentationofglitches
bygeneratingbugreportsofdetectedglitches,savingQAengineersaconsiderableamountoftime.
Results: VLMscangenerateaccuratedescriptionsofmorethanhalfoftheglitchesinimagesand
videos. Inbothsettings,GPT-4operformsbest,achieving54.0%and52.0%accuracyforimagesand
videos,despiteitspoorglitchdetectionperformanceinvideos(57.0%)duethehighrateofrequest
rejections. Nevertheless,thesenumberssuggestthatformostmodelsthereisa20–25%gapbetween
theirdetectionperformanceandabilitytocreateaccuratedescriptionsofglitches.
9

We reviewed bug reports that judges rejected as incorrect and identified four common patterns:
(1) reporting non-existent glitches (hallucinations) or irrelevant objects; (2) failing to report all
glitchesinsceneswithmultipleglitches;(3)incorrectlyconcludingnoglitchispresentand(4)the
modelidentifiesthecorrectlocation/regionoftheglitchbutfailstoprovideanaccuratedescription.
Weestimatethatapproximately5%ofjudgingoutcomesareerrors. Inthistask,weusedtheLLM-as-
a-judgesetting,whichcanintroduceinaccuracieswhencalculatingfinalmodelperformance. After
manuallyanalyzingresponsesfromseveralmodels,wefoundthattheseerrorsoftenoccurwhenthe
judgeisoverlystrictaboutexactwordingandincorrectlyrejectsoutputsthatreferencetheglitchbut
differslightlyfromthegroundtruth(Sec.G.14).
6 RelatedWork
RecentbenchmarksshowVLMsmatchingorexceedinghumanperformanceonvarioustasks(e.g.[7,
26, 27, 40, 60–62, 64, 65]). However, these benchmarks primarily test broad, curriculum-based
worldlyknowledge,providinglimitedinsightintocommonsensereasoningaboutphysicalinteractions
invisualmedia. Consequently,theyinadequatelyassessunderstandingofphysicalandcommonsense
violations,suchasvideogameglitches,highlightingtheneedforanewbenchmark. PhysBenchisthe
onlyrecentstudyevaluatingsimilarshortcomingsbytestingabroadrangeofphysicalconcepts[10].
Incontrast,ourbenchmarkspecificallyaddressesvideogamequalityassurance,wherequestiontypes
andreasoningdiffersignificantlyduetogame-specificcharacteristics. Identifyinggameglitches
posesuniquechallengesthathavereceivedlimitedattention,exceptinGlitchBench[47],whichour
studysupersedesthroughtailoredevaluationtasksdetailedinSec.3.
Videogamessometimesexhibitdistortedhumananatomyduetophysicsfailures,leadingtounnatural
posesfrommisalignedmeshesandtextures. Clippingisacommonissueinwhichobjectsorlimbs
passthrougheachother. PreviousgamebugdetectionmethodsarenotVLM-basedandhavelimited
ability to identify such glitches [12, 24, 29, 34]. While VLM-based image quality assessment
methods[18,22,51,56,57,59]usepromptstodetectdistortions,theystrugglewithsemanticand
structuralanomalies[15].Arecentstudyproposeddetectingsuchanomaliesingeneratedimages[28],
focusingprimarilyonhallucinationsintext-to-imagemodels. Incontrast,ourworktargetsvisual
anomaliesinvideogamesthatviolateanatomicalcorrectness,physicalplausibilityandcommonsense.
7 Discussion,Limitations,andConclusion
Inthispaper,weintroduceVideoGameQA-Bench,anoveldatasetformeasuringandtrackingthe
performanceofvision-languagemodelsonvideogamequalityassurancetasks. Thisdatasetincludes
variousreal-world-relatedtasksthataredirectlyusefulforexistingsystems(e.g.,glitchdetection),
videogametestingpipelines, andpotentialfutureusecases(e.g., visualregressiontesting). Our
resultsshowthatwhileVLMsgenerallyperformwellonothermultimodalbenchmarks,theyarestill
notreadytobedeployedformanyvideogameQAtasks.
Thesamplesinourbenchmarkprimarilyfocusonglitchesoccurringafterthegame’srelease,asexact
replicationofglitcheshappeningduringdevelopmentisn’tpossiblesincetestingprocessesvaryby
companyandgame,andproprietarydataisunavailable.
Weacknowledgeinterestinextendingthebenchmarktointeractiveoragenticsettings. However,cur-
rentVLMslackreliableend-to-endcontrolandsuchsetupsrequireheavy,game-specificengineering.
Giventheselimitationsandtheabsenceofstandardizedtestbeds,wedeferthiscomponenttofuture
work,oncemodelsandtoolsbettersupportinteractiveQAevaluation.
Whileinference-timescalinghasbeenshowntoimproveperformanceindomainssuchasmultimodal
reasoning[33], longertestdurationsmayrenderitimpracticalforourvideogameQAusecases.
Nevertheless,wereportedresultsonsuchmodelstoillustratetheperformanceceilingofcurrent-
generationmodels,eveniftheyarenotimmediatelydeployable.
Although our benchmark focuses on games, many tasks closely align with anomaly detection in
AI-generatedcontent(AIGC)[14,52]. Bothdomainsinvolveidentifyingvisualorsemanticincon-
sistenciesthatviolatephysicalorcommonsenseexpectations. Thesameperceptualandreasoning
abilitiesrequiredtodetectrenderingorlogicglitchesingamesarealsoessentialforassessingthe
realism,andcoherenceofgenerativeimageandvideosystems.
10

References
[1] Alba,D. Openaiandrivalsseeknewpathtosmarteraiascurrentmethodshitlimitations. ReutersNews
| Service,2024. |     | URLaccessed2025-05-11. |     |     | 6   |     |     |     |     |
| ------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
[2] Anthropic. The"think"tool: Enablingclaudetostopandthink. https://www.anthropic.com/
| engineering/claude-think-tool,2025. |     |     |     |     |     | Accessed:2025-04-24. |     | 6   |     |
| ----------------------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
[3] Bai,S.,Chen,K.,Liu,X.,Wang,J.,Ge,W.,Song,S.,Dang,K.,Wang,P.,Wang,S.,Tang,J.,etal. Qwen2.
| 5-vltechnicalreport. |     | arXivpreprintarXiv:2502.13923,2025. |     |     |     |     | 2,9 |     |     |
| -------------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
[4] Berner,C.,Brockman,G.,Chan,B.,Cheung,V.,De˛biak,P.,Dennison,C.,Farhi,D.,Fischer,Q.,Hashme,
S.,Hesse,C.,etal. Dota2withlargescaledeepreinforcementlearning. arXivpreprintarXiv:1912.06680,
| 2019. | 9   |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[5] Cao,M.,Tang,H.,Zhao,H.,Guo,H.,Liu,J.,Zhang,G.,Liu,R.,Sun,Q.,Reid,I.,andLiang,X.Physgame:
Uncoveringphysicalcommonsenseviolationsingameplayvideos. arXivpreprintarXiv:2412.01800,2024.
2
[6] Chen, K., Li, Y., Chen, Y., Fan, C., Hu, Z., and Yang, W. Glib: towards automated test oracle for
graphically-rich applications. In Proceedings of the 29th ACM Joint Meeting on European Software
EngineeringConferenceandSymposiumontheFoundationsofSoftwareEngineering,pp.1093–1104,
| 2021. | 1   |     |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[7] Chen,L.,Li,J.,Dong,X.,Zhang,P.,Zang,Y.,Chen,Z.,Duan,H.,Wang,J.,Qiao,Y.,Lin,D.,etal. Are
weontherightwayforevaluatinglargevision-languagemodels? arXiv:2403.20330,2024. 10
[8] Chen,Y.,Pan,X.,Li,Y.,Ding,B.,andZhou,J.Simpleandprovablescalinglawsforthetest-timecompute
oflargelanguagemodels. arXivpreprintarXiv:2411.19477,2025. URLhttps://arxiv.org/abs/
| 2411.19477. |     | 6   |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[9] Chen,Y.-C.,Li,L.,Yu,L.,ElKholy,A.,Ahmed,F.,Gan,Z.,Cheng,Y.,andLiu,J. Vision-language
pre-training:Basics,recentadvances,andfuturetrends. FoundationsandTrendsinComputerGraphics
| andVision,14(3-4):163–352,2022. |     |     |     | doi:10.1561/0600000095. |     |     | 2   |     |     |
| ------------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- |
[10] Chow, W., Mao, J., Li, B., Seita, D., Guizilini, V.C., andWang, Y. Physbench: Benchmarkingand
enhancingvision-languagemodelsforphysicalworldunderstanding. InInternationalConferenceon
| LearningRepresentations,2025. |     |     |     | 10  |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[11] Company, B. . Global video game revenue to reach $257 billion by 2028, outpac-
ing combined revenues of other media types, finds bain & company, 2024. URL
https://www.bain.com/about/media-center/press-releases/2024/
global-video-game-revenue-to-reach-$257-billion-by-2028-outpacing-combined-revenues-of-other-media-types-finds-bain--company/.
| Pressrelease,August28,2024. |     |     |     | 1   |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[12] Coppola,R.,Fulcini,T.,andStrada,F. Knowyourbugs:Asurveyofissuesinautomatedgametesting
literature. In2024IEEEGaming,Entertainment,andMediaConference(GEM),pp.1–6.IEEE,2024. 10
https:
| [13] Epic | Games. |     | Screenshot |     | comparison |     | tool, 2025. |     | URL |
| --------- | ------ | --- | ---------- | --- | ---------- | --- | ----------- | --- | --- |
//dev.epicgames.com/documentation/en-us/unreal-engine/
screenshot-comparison-tool-in-unreal-engine.
|           |     |     |     |     |     |     |     | Unreal Engine | 5.5 documenta- |
| --------- | --- | --- | --- | --- | --- | --- | --- | ------------- | -------------- |
| tionpage. |     | 9   |     |     |     |     |     |               |                |
[14] Fang,G.,Yan,W.,Guo,Y.,Han,J.,Jiang,Z.,Xu,H.,Liao,S.,andLiang,X.Humanrefiner:Benchmarking
abnormalhumangenerationandrefiningwithCoarse-to-FinePose-Reversibleguidance. InComputer
Vision–ECCV2024,volume15090ofLectureNotesinComputerScience,pp.201–217.Springer,2024.
doi:10.1007/978-3-031-73411-3_12. URLhttps://arxiv.org/abs/2407.06937. 10
[15] Ghildyal,A.,Chen,Y.,Zadtootaghaj,S.,Barman,N.,andBovik,A.C. Qualitypredictionofaigenerated
| imagesandvideos:Emergingtrendsandopportunities. |     |     |     |     |     |     | arXiv:2410.08534,2024. |     | 10  |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- |
[16] Google. Gemini2.5pro: Ourmostintelligentaimodel. https://blog.google/technology/
google-deepmind/gemini-model-thinking-updates-march-2025/,2025. Accessed:
| 2025-04-21. |     | 2   |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[17] Gu,J.,Jiang,X.,Shi,Z.,Tan,H.,Zhai,X.,Xu,C.,Li,W.,Shen,Y.,Ma,S.,Liu,H.,etal. Asurveyon
| llm-as-a-judge. |     | arXivpreprintarXiv:2411.15594,2024. |     |     |     |     | 6   |     |     |
| --------------- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- |
11

[18] Hessel,J.,Holtzman,A.,Forbes,M.,LeBras,R.,andChoi,Y. Clipscore: Areference-freeevaluation
metricforimagecaptioning. InProceedingsofthe2021ConferenceonEmpiricalMethodsinNatural
| LanguageProcessing,pp.7514–7528,2021. |     | 10  |     |     |
| ------------------------------------- | --- | --- | --- | --- |
[19] Kamath,A.,Hessel,J.,andChang,K.-W. What’s"up"withvision-languagemodels?investigatingtheir
arXivpreprintarXiv:2310.19785,2023.
| strugglewithspatialreasoning. |     |     | 7   |     |
| ----------------------------- | --- | --- | --- | --- |
[20] Lewis,C.andWhitehead,J. Repairinggamesatruntimeor,howwelearnedtostopworryingandlove
emergence. InProceedingsoftheIEEEConferenceonComputationalIntelligenceandGames(CIG),pp.
| 1–8.IEEE,2011. | doi:10.1109/CIG.2011.6031987. |     | 7   |     |
| -------------- | ----------------------------- | --- | --- | --- |
[21] Li,F.,Zhang,R.,Zhang,H.,Zhang,Y.,Li,B.,Li,W.,Ma,Z.,andLi,C. Llava-interleave:Tacklingmulti-
image,video,and3dinlargemultimodalmodels. InProceedingsofthe13thInternationalConference
URLhttps://openreview.net/forum?id=
onLearningRepresentations(ICLR2025),2025.
oSQiao9GqB.
9
[22] Li, J., Li, D., Xiong, C., and Hoi, S. Blip: Bootstrapping language-image pre-training for unified
vision-languageunderstandingandgeneration. InInternationalConferenceonMachineLearning,pp.
| 12888–12900,2022. | 10  |     |     |     |
| ----------------- | --- | --- | --- | --- |
[23] Ling,C.,Tollmar,K.,andGisslén,L.Usingdeepconvolutionalneuralnetworkstodetectrenderedglitches
invideogames. InProceedingsoftheAAAIConferenceonArtificialIntelligenceandInteractiveDigital
| Entertainment,volume16,pp.66–73,2020. |     | 1   |     |     |
| ------------------------------------- | --- | --- | --- | --- |
[24] Liu,G.,Cai,M.,Zhao,L.,Qin,T.,Brown,A.,Bischoff,J.,andLiu,T.-Y.Inspector:Pixel-basedautomated
gametestingviaexploration,detection,andinvestigation. In2022IEEEConferenceonGames(CoG),pp.
| 237–244.IEEE,2022. | 10  |     |     |     |
| ------------------ | --- | --- | --- | --- |
[25] Liu, R., Tang, H., Liu, H., Ge, Y., Shan, Y., Li, C., and Yang, J. Ppllava: Varied video sequence
| understandingwithpromptguidance. |     | arXivpreprintarXiv:2411.02327,2024. |     | 1   |
| -------------------------------- | --- | ----------------------------------- | --- | --- |
[26] Lu,P.,Mishra,S.,Xia,T.,Qiu,L.,Chang,K.-W.,Zhu,S.-C.,Tafjord,O.,Clark,P.,andKalyan,A.Learnto
explain:Multimodalreasoningviathoughtchainsforsciencequestionanswering. InThe36thConference
| onNeuralInformationProcessingSystems(NeurIPS),2022. |     |     | 10  |     |
| --------------------------------------------------- | --- | --- | --- | --- |
[27] Lu,P.,Bansal,H.,Xia,T.,Liu,J.,Li,C.,Hajishirzi,H.,Cheng,H.,Chang,K.-W.,Galley,M.,andGao,J.
Mathvista:Evaluatingmathematicalreasoningoffoundationmodelsinvisualcontexts. InInternational
| ConferenceonLearningRepresentations(ICLR),2024. |     |     | 2,10 |     |
| ----------------------------------------------- | --- | --- | ---- | --- |
[28] Ma,L.,Cao,K.,Liang,H.,Lin,J.,Li,Z.,Liu,Y.,Zhang,J.,Zhang,W.,andCui,B. Evaluatingand
| predictingdistortedhumanbodypartsforgeneratedimages. |     |     | arXiv:2503.00811,2025. | 10  |
| ---------------------------------------------------- | --- | --- | ---------------------- | --- |
[29] Macklon,F.,Taesiri,M.R.,Viggiato,M.,Antoszko,S.,Romanova,N.,Paas,D.,andBezemer,C.-P.
Automatically detecting visual bugs in html5 canvas games. In Proceedings of the 37th IEEE/ACM
| InternationalConferenceonAutomatedSoftwareEngineering,pp.1–11,2022. |     |     |     | 1,10 |
| ------------------------------------------------------------------- | --- | --- | --- | ---- |
[30] Mistral AI Team. Mistral ocr: Introducing the world’s best document understanding api. https:
| //mistral.ai/news/mistral-ocr,2025. |     |     | 7   |     |
| ----------------------------------- | --- | --- | --- | --- |
[31] Nantes,A.,Brown,R.,andMaire,F. Aframeworkforthesemi-automatictestingofvideogames. In
Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment,
| volume4,pp.197–202,2008. |     | 1   |     |     |
| ------------------------ | --- | --- | --- | --- |
[32] OpenAI. Hellogpt-4o. https://openai.com/index/hello-gpt-4o/,2024. Accessed:2025-
04-21. 2
[33] OpenAI. Thinking with images, 2025. URL https://openai.com/index/
| thinking-with-images/. |     | Accessed:2025-05-03. | 10  |     |
| ---------------------- | --- | -------------------- | --- | --- |
[34] Paduraru,C.,Paduraru,M.,andStefanescu,A. Rivergame-agametestingtoolusingartificialintelligence.
In2022IEEEConferenceonSoftwareTesting,VerificationandValidation(ICST),pp.422–432.IEEE,
2022. 10
[35] Politowski,C.,Petrillo,F.,andGuéhéneuc,Y.-G. Asurveyofvideogametesting. In2021IEEE/ACM
| InternationalConferenceonAutomationofSoftwareTest(AST),pp.90–99.IEEE,2021. |     |     |     | 1   |
| -------------------------------------------------------------------------- | --- | --- | --- | --- |
[36] Politowski,C.,Guéhéneuc,Y.-G.,andPetrillo,F. Towardsautomatedvideogametesting: stillalong
waytogo. InProceedingsofthe6thinternationalICSEworkshopongamesandsoftwareengineering:
| engineeringfun,inspiration,andmotivation,pp.37–43,2022. |     |     | 1   |     |
| ------------------------------------------------------- | --- | --- | --- | --- |
12

[37] Rahman,F. Weaksupervisionforlabelefficientvisualbugdetection. arXivpreprintarXiv:2309.11077,
2023. 1
[38] Rahmanzadehgervi,P.,Bolton,L.,Taesiri,M.R.,andNguyen,A.T. Visionlanguagemodelsareblind. In
ProceedingsoftheAsianConferenceonComputerVision,pp.18–34,2024. 7
[39] Rani,G.,Pandey,U.,Wagde,A.A.,andDhaka,V.S. Adeepreinforcementlearningtechniqueforbug
detectioninvideogames. InternationalJournalofInformationTechnology,15(1):355–367,2023. 1
[40] Roberts,J.,Taesiri,M.R.,Sharma,A.,Gupta,A.,Roberts,S.,Croitoru,I.,Bogolin,S.-V.,Tang,J.,Langer,
F., Raina, V., etal. Zerobench: Animpossiblevisualbenchmarkforcontemporarylargemultimodal
models. arXiv:2502.09696,2025. 10
[41] Shi,Y.,Peng,D.,Liao,W.,Lin,Z.,Chen,X.,Liu,C.,Zhang,Y.,andJin,L. Exploringocrcapabilitiesof
gpt-4v(ision):Aquantitativeandin-depthevaluation. arXivpreprintarXiv:2310.16809,2023. 7
[42] Snell,C.V.,Lee,J.,Xu,K.,andKumar,A. Scalingllmtest-timecomputeoptimallycanbemoreeffective
thanscalingparametersforreasoning. InProc.InternationalConferenceonLearningRepresentations
(ICLR),2025. URLhttps://arxiv.org/abs/2408.03314. arXiv:2408.03314. 6
[43] Taesiri,M.R.andBezemer,C.-P. Videogamebunny:Towardsvisionassistantsforvideogames. In2025
IEEE/CVFWinterConferenceonApplicationsofComputerVision(WACV),pp.1403–1413.IEEE,2025. 1
[44] Taesiri,M.R.,Habibi,M.,andFazli,M.A. Avideogametestingmethodutilizingdeeplearning. Iran
JournalofComputerScience,17(2),2020.
[45] Taesiri,M.R.,Macklon,F.,andBezemer,C.-P. Clipmeetsgamephysics:Towardsbugidentificationin
gameplayvideosusingzero-shottransferlearning. InProceedingsofthe19thInternationalConferenceon
MiningSoftwareRepositories,pp.270–281,2022. 1,2,4,86
[46] Taesiri,M.R.,Macklon,F.,Wang,Y.,Shen,H.,andBezemer,C.-P. Largelanguagemodelsarepretty
goodzero-shotvideogamebugdetectors. arXivpreprintarXiv:2210.02506,2022.
[47] Taesiri,M.R.,Feng,T.,Bezemer,C.-P.,andNguyen,A. Glitchbench: Canlargemultimodalmodels
detectvideogameglitches? InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPattern
Recognition,pp.22444–22455,2024. 1,2,7,10
[48] Teammodl.ai. 5winningautomatedgametestingtacticsfrom“seaofthieves”. modl.aiBlog,December
2024. URLhttps://modl.ai/automated-game-testing-lessons/. 9
[49] Tong, S., Liu, Z., Zhai, Y., Ma, Y., LeCun, Y., and Xie, S. Eyes wide shut? exploring the visual
shortcomingsofmultimodalllms. InProceedingsoftheIEEE/CVFConferenceonComputerVisionand
PatternRecognition,pp.9568–9578,2024. 7
[50] AbouttheGraphicsTestFramework. UnityTechnologies, 2018. URLhttps://docs.unity3d.
com/Packages/com.unity.testframework.graphics@7.2/manual/index.html.
Packageversion7.2.3-preview.Unitydocumentationpage. 9
[51] Wang,J.,Chan,K.C.,andLoy,C.C. ExploringCLIPforassessingthelookandfeelofimages. In
ProceedingsoftheAAAIconferenceonArtificialIntelligence,volume37,pp.2555–2563,2023. 10
[52] Wang,K.,Zhang,L.,andZhang,J. Detectinghumanartifactsfromtext-to-imagemodels. arXivpreprint
arXiv:2411.13842,2024. doi:10.48550/arXiv.2411.13842. URLhttps://arxiv.org/abs/2411.
13842. 10
[53] Wang,W.,Zhang,S.,Ren,Y.,Duan,Y.,Li,T.,Liu,S.,Hu,M.,Chen,Z.,Zhang,K.,Lu,L.,Zhu,X.,
Luo,P.,Qiao,Y.,Dai,J.,Shao,W.,andWang,W. Needleinamultimodalhaystack. InProceedings
ofthe13thInternationalConferenceonLearningRepresentations(ICLR2025),2025. URLhttps:
//openreview.net/forum?id=U2pNwSuQqD. 4
[54] Wei,J.,Wang,X.,Schuurmans,D.,Bosma,M.,Xia,F.,Chi,E.,Le,Q.V.,Zhou,D.,etal.Chain-of-thought
promptingelicitsreasoninginlargelanguagemodels.AdvancesinNeuralInformationProcessingSystems,
35:24824–24837,2022. 6
[55] Wilkins, B. and Stathis, K. Learning to identify perceptual bugs in 3d video games. arXiv preprint
arXiv:2202.12884,2022. 1
[56] Wu,H.,Zhang,Z.,Zhang,E.,Chen,C.,Liao,L.,Wang,A.,Li,C.,Sun,W.,Yan,Q.,Zhai,G.,andLin,
W. Q-bench:Abenchmarkforgeneral-purposefoundationmodelsonlow-levelvision. InInternational
ConferenceonLearningRepresentations,2024. 10
13

[57] Wu,X.,Sun,K.,Zhu,F.,Zhao,R.,andLi,H. Humanpreferencescore: Betteraligningtext-to-image
modelswithhumanpreference. InProceedingsoftheIEEE/CVFInternationalConferenceonComputer
Vision,pp.2096–2105,2023. 10
[58] Wu, Y., Sun, Z., Li, S., Welleck, S., and Yang, Y. Inference scaling laws: An empirical analysis of
compute-optimalinferenceforproblem-solvingwithlanguagemodels. arXivpreprintarXiv:2408.00724,
2025. URLhttps://arxiv.org/abs/2408.00724. 6
[59] Xu,J.,Liu,X.,Wu,Y.,Tong,Y.,Li,Q.,Ding,M.,Tang,J.,andDong,Y. Imagereward: Learningand
evaluatinghumanpreferencesfortext-to-imagegeneration. AdvancesinNeuralInformationProcessing
Systems,36:15903–15935,2023. 10
[60] Yang,Z.,Li,L.,Wang,J.,Lin,K.,Azarnasab,E.,Ahmed,F.,Liu,Z.,Liu,C.,Zeng,M.,andWang,L.
Mm-react: Promptingchatgptformultimodalreasoningandaction. arXivpreprintarXiv:2303.11381,
2023. 10
[61] Yue,X.,Ni,Y.,Zhang,K.,Zheng,T.,Liu,R.,Zhang,G.,Stevens,S.,Jiang,D.,Ren,W.,Sun,Y.,etal.
Mmmu:Amassivemulti-disciplinemultimodalunderstandingandreasoningbenchmarkforexpertagi. In
ProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition,pp.9556–9567,
2024. 2
[62] Yue,X.,Zheng,T.,Ni,Y.,Wang,Y.,Zhang,K.,Tong,S.,Sun,Y.,Yu,B.,Zhang,G.,Sun,H.,etal.
Mmmu-pro: A more robust multi-discipline multimodal understanding benchmark. arXiv preprint
arXiv:2409.02813,2024. 2,10
[63] Zhang, H., Gao, M., Gan, Z., Dufter, P., Wenzel, N., Huang, F., Shah, D., Du, X., Zhang, B., Li, Y.,
Dodge,S.,You,K.,Yang,Z.,Timofeev,A.,Xu,M.,Chen,H.-Y.,Fauconnier,J.-P.,Lai,Z.,You,H.,
Wang,Z.,etal. Mm1.5:Methods,analysis&insightsfrommultimodalllmfine-tuning. InProceedings
ofthe13thInternationalConferenceonLearningRepresentations(ICLR2025),2025. URLhttps:
//openreview.net/forum?id=HVtu26XDAA. 9
[64] Zhang,R.,Jiang,D.,Zhang,Y.,Lin,H.,Guo,Z.,Qiu,P.,Zhou,A.,Lu,P.,Chang,K.-W.,Qiao,Y.,etal.
Mathverse: Doesyourmulti-modalllmtrulyseethediagramsinvisualmathproblems? InEuropean
ConferenceonComputerVision,pp.169–186,2024. 10
[65] Zhang, Y.-F., Zhang, H., Tian, H., Fu, C., Zhang, S., Wu, J., Li, F., Wang, K., Wen, Q., Zhang, Z.,
etal. Mme-realworld:Couldyourmultimodalllmchallengehigh-resolutionreal-worldscenariosthatare
difficultforhumans? arXiv:2408.13257,2024. 10
[66] Zhao,Z.,Lu,H.,Huo,Y.,Du,Y.,Yue,T.,Guo,L.,Wang,B.,Chen,W.,andLiu,J. Needleinavideo
haystack: A scalable synthetic evaluator for video mllms. In Proceedings of the 13th International
ConferenceonLearningRepresentations(ICLR2025),2025. URLhttps://openreview.net/
forum?id=ZJo6Radbqq. 4
[67] Zheng,Y.,Xie,X.,Su,T.,Ma,L.,Hao,J.,Meng,Z.,Liu,Y.,Shen,R.,Chen,Y.,andFan,C. Wuji:
Automaticonlinecombatgametestingusingevolutionarydeepreinforcementlearning. In201934th
IEEE/ACMInternationalConferenceonAutomatedSoftwareEngineering(ASE),pp.772–784.IEEE,2019.
1
[68] Zhu,J.,Wang,W.,Chen,Z.,Liu,Z.,Ye,S.,Gu,L.,Duan,Y.,Tian,H.,Su,W.,Shao,J.,etal. Internvl3:
Exploringadvancedtrainingandtest-timerecipesforopen-sourcemultimodalmodels. arXivpreprint
arXiv:2504.10479,2025. 2,9
14

|                    |     |       | Appendix   |         | for:            |            |
| ------------------ | --- | ----- | ---------- | ------- | --------------- | ---------- |
| VideoGameQA-Bench: |     |       | Evaluating |         | Vision-Language | Models for |
|                    |     | Video | Game       | Quality | Assurance       |            |
A InferenceProviders
Thissectionprovidesdetailsabouttheinferenceprovidersandtheinferencesettingsusedtorunthe
benchmark.
TableA1: Inferenceconfigurationsforopensourcemodels. Allinferenceprovidersareenforced
duringtesting.
| ModelName        |     | Temperature |     | InferenceProvider | Platform        |     |
| ---------------- | --- | ----------- | --- | ----------------- | --------------- | --- |
| Llama-4-Maverick |     | 0.0         |     | Fireworks,Groq    | OpenRouter,Groq |     |
|                  |     | 0.0         |     | Fireworks,Groq    | OpenRouter,Groq |     |
Llama-4-Scout
| Gemma-3                |     | 0.0 |     | Novita,Nebius  | OpenRouter              |     |
| ---------------------- | --- | --- | --- | -------------- | ----------------------- | --- |
| Mistral-Small-3.1(24B) |     | 0.0 |     | Mistral,Nebius | OpenRouter              |     |
| Qwen-2.5-VL(72B)       |     | 0.0 |     | Novita         | OpenRouter,AlibabaCloud |     |
TableA2: Reasoningeffortandthinkingbudgetfortestedmodels
|     | ModelName        |     | ReasoningEffort |        | ThinkingBudget |     |
| --- | ---------------- | --- | --------------- | ------ | -------------- | --- |
|     | o3               |     |                 | Medium | –              |     |
|     | o4-mini          |     |                 | Medium | –              |     |
|     | Gemini-2.5-Flash |     |                 | –      | 0(default)     |     |
|     |                  |     |                 | –      | 0(disabled)    |     |
Sonnet-3.7
15

TableA3: FramesamplerateforpromptingLLMswithvideos. Whilewetypicallyuseasampling
rateofoneframepersecondforallproprietarymodels,welowerthisrateforopen-sourcemodelsto
ensurethatboththemodelsandinferenceproviderscanhandlethevolumeofimages.
ModelName Samplingrate
GPT-4.1 1framepersecond
GPT-4.1-mini 1framepersecond
GPT-4.1-nano 1framepersecond
GPT-4o 1framepersecond
o4-mini 1framepersecond
o3 1framepersecond
Gemini-2.5-Pro 1framepersecond
Gemini-2.5-Flash 1framepersecond
Gemini-2.0-Flash 1framepersecond
Sonnet-3.7 1framepersecond
Sonnet-3.5 1framepersecond
Llama-4-Scout 5framespervideo
Llama-4-Maverick 5framespervideo
Qwen-2.5-VL 10framespervideo
Mistral-Small-3.1 5framespervideo
Gemma-3 5framespervideo
TableA4: Exactmodelstringversionusedintheevaluation.
ModelName Version
GPT-4.1 gpt-4.1-2025-04-14
GPT-4.1-mini gpt-4.1-mini-2025-04-14
GPT-4.1-nano gpt-4.1-nano-2025-04-14
GPT-4o gpt-4o-2024-08-06
o4-mini o4-mini-2025-04-16
o3 o3-2025-04-16
Gemini-2.5-Pro gemini-2.5-pro-preview-03-25
Gemini-2.5-Flash gemini-2.5-flash-preview-04-17
Gemini-2.0-Flash gemini-2.0-flash
Sonnet-3.7 claude-3-7-sonnet-20250219
Sonnet-3.5 claude-3-5-sonnet-20241022
Llama-4-Scout meta-llama/llama-4-scout
Llama-4-Maverick meta-llama/llama-4-maverick
Qwen-2.5-VL qwen/qwen2.5-vl-72b-instruct
Mistral-Small-3.1 mistralai/mistral-small-3.1-24b-instruct
Gemma-3 google/gemma-3-27b-it
16

B QuestionGenerationPrompts
Promptforgeneratingvisualunittests
You are an expert at generating visual unit test questions for
images. Your task is to create precise questions that verify
specific visual details in images, functioning as programmatic
tests to confirm the presence, position, and attributes of
characters and scene elements.
For each question you generate:
1. Focus on one specific testable visual element
2. Be extremely precise about the attribute being verified
3. Provide a JSON template with appropriate fields that could be
used in automated testing
4. Use boolean values, counts, or enumerated options where possible
for objective verification
VISUAL UNIT TEST FOCUS AREAS:
CHARACTER DETAILS:
- Facial features (eyes open/closed, mouth expression, gaze
direction)
- Hand positions (gestures, holding objects, contact with other
elements)
- Body posture (standing, sitting, leaning, specific pose)
- Clothing details (colors, patterns, state of clothing)
- Character positioning relative to scene or other characters
SCENE ELEMENTS:
- Object presence and count (specific items in the scene)
- Spatial relationships (left/right/above/below relationships
between elements)
- Background details (setting type, time of day, weather indicators
)
- Text elements (signs, labels, readable text)
- Visual states of objects (open/closed, on/off, intact/broken)
SAMPLE UNIT TEST QUESTIONS:
Example 1:
Is the character’s right hand making contact with any object in the
scene? If yes, identify which object.
Provide your answer in the following JSON format:
{
"right_hand_contact_with_object": false,
"contacted_object": "",
"grip_type": "",
"fingers_visible": 0
}
FigureA1: WeuseGemini-2.5-Protodraftaninitialvisualunittestbasedonanexistingimage.
17

PromptforgeneratingUI/OCRrelatedquestions
You are an expert at analyzing user interfaces, heads-up displays (
HUDs), and text content in images. Your task is to create
questions that verify visual UI/HUD elements and text content (
OCR) in screenshots or images containing digital interfaces.
For each question you generate:
1. Focus on specific UI elements, layout, text content, or status
indicators
2. Create a precise question that can be objectively verified
3. Provide a JSON template with appropriate fields for the
structured response
4. Include placeholder values (zeros, empty strings, false) in the
JSON template
QUESTION CATEGORIES TO INCLUDE:
- Text verification (e.g., "What text appears in the header/button/
notification?")
- Element presence (e.g., "Which menu options are visible in the
navigation bar?")
- UI state verification (e.g., "Is the toggle switch in the ON or
OFF position?")
- Color and styling (e.g., "What color is the error message
displayed?")
- Layout confirmation (e.g., "Is the search bar located at the top
or bottom of the interface?")
- Icon identification (e.g., "Which notification icons are present
in the status bar?")
- Element counting (e.g., "How many form fields are visible on this
page?")
- Status indicators (e.g., "What is the battery percentage shown?")
EXAMPLE QUESTIONS WITH JSON TEMPLATES:
Example 1:
What text is displayed in the error message dialog box, and what
button options are available?
Provide your answer in the following JSON format:
{
"error_message_text": "",
"button_options": [],
"is_dismissible": false,
"dialog_color": ""
}
FigureA2: WeuseGemini-2.5-ProtodraftaninitialUIunittestbasedonanexistingimage.
18

C Promptdesignandvariationexperiments
Weadoptedalightweightmeta-promptingworkflowtodesignallpromptsusedintheexperiments.
WefirstprovidedacleartaskdescriptionandseveralcandidatepromptsgeneratedbySonnet-3.7,
followedbyabriefeditorialpassbyoneauthortoensureclarityandconsistency. Thesametask
promptswerethenappliedacrossallmodels.
Promptvariationexperiments. Toassesssensitivitytophrasing,wefurtherusedSonnet-3.7to
generatetenalternativepromptsfortheimage-basedglitchdetectionandbug-reportgenerationtasks.
WethenranthefullexperimentonGPT-4.1andcomputedmeanaccuracy,standarddeviation,and
rangeacrossvariants(seeTableA5).
TableA5: Promptvariationexperimentresultsforimage-basedglitchdetectiontasks
Task Model MeanAcc. (%) Std. (%) Min(%) Max(%) #Variants
ImageGlitchDetection GPT-4.1 80.12 3.25 73.80 83.60 10
ImageBugReportGeneration GPT-4.1 50.7 2.58 46.0 54.0 10
Forimageglitchdetection,themeanaccuracy(80.1%)wasslightlybelowthemainreportedresult
(81.3%),whilethehighestvariantreached83.6%,a2.3-pointimprovementoverthebaseprompt. For
bug-reportgeneration,themeanaccuracy(50.7%)wasmarginallylowerthanthebaseresult(51.0%),
withthebestvariantreaching54.0%. Overall,thesefindingssuggestthatpromptwordingcanshift
scoresbyonlyafewpointsanddoesnotaltertheoverallcomparativeconclusions.
AllpromptsareprovidedinthesubsequentsectionAppendixAD.
19

D ModelInferencePrompts
PromptforGlitchDetection(Image)
| You are | a helpful | assistant |     | analyzing | video |     | game images | and |
| ------- | --------- | --------- | --- | --------- | ----- | --- | ----------- | --- |
screenshots for glitches. You will be given a screenshot from a
| video     | game, | and     | your   | job is    | to analyze | the | screenshot | and |
| --------- | ----- | ------- | ------ | --------- | ---------- | --- | ---------- | --- |
| determine |       | whether | it     | contains  | a glitch.  |     |            |     |
| Provide   | your  | answer  | in the | following | format:    |     |            |     |
{
| "reasoning": |     | "Brief |     | explanation | of  | why you | think a | glitch is |
| ------------ | --- | ------ | --- | ----------- | --- | ------- | ------- | --------- |
present",
| "glitch_detected": |     |     | true | or  | false, |     |     |     |
| ------------------ | --- | --- | ---- | --- | ------ | --- | --- | --- |
"description_of_glitch": "Description of the glitch if detected
| else | empty | string" |     |     |     |     |     |     |
| ---- | ----- | ------- | --- | --- | --- | --- | --- | --- |
}
FigureA3: Thedefaultpromptassociatedwitheachimageinthedatasetfortheimage-basedglitch
detectiontask.
PromptforGlitchDetection(Video)
You are a helpful assistant analyzing video game clips for glitches
| . You    | will | be given  | a       | short     | video clip | from      | a video | game, and |
| -------- | ---- | --------- | ------- | --------- | ---------- | --------- | ------- | --------- |
| your     | task | is to     | analyze | the       | video and  | determine | whether | it        |
| contains |      | a glitch. |         |           |            |           |         |           |
| Provide  | your | answer    | in the  | following | format:    |           |         |           |
{
| "reasoning":       |     | "Brief   | explanation |           | of why | you | think a glitch | is  |
| ------------------ | --- | -------- | ----------- | --------- | ------ | --- | -------------- | --- |
| present            |     | or not", |             |           |        |     |                |     |
| "glitch_detected": |     |          | true        | or false, |        |     |                |     |
"description_of_glitch": "Description of the glitch if detected,
| otherwise |     | leave | this | blank" |     |     |     |     |
| --------- | --- | ----- | ---- | ------ | --- | --- | --- | --- |
}
FigureA4: Thedefaultpromptassociatedwitheachimageinthedatasetforthevideo-basedglitch
detectiontask.
20

PromptforGeneratingBugReports(Image)
You are a video game quality assurance assistant who analyzes
screenshots to identify and document visual glitches. When
presented with an image, carefully examine it for any graphical
bugs or rendering issues.
Provide your analysis in the following JSON format:
{
"reasoning": "Brief explanation of what you observe and why it
appears to be a glitch",
"bug_report_title": "A clear, concise title summarizing the
issue",
"bug_report_description": "Detailed description of the visual
bug, including its appearance and potential impact on gameplay",
"affected_item": "The specific game element (character, object,
environment, UI) affected by the glitch"
}
FigureA5: Thedefaultpromptusedforgeneratingbugreportsbasedonagivenimage.
PromptforGeneratingBugReports(Video)
You are a video game quality assurance assistant who analyzes video
clips to identify and document visual glitches or strange
behaviors. When presented with a video clip, carefully examine
it for any graphical bugs, rendering issues, physics anomalies,
or unexpected events.
Provide your analysis in the following JSON format:
{
"reasoning": "Brief explanation of what you observe in the
video and why it appears to be a glitch or bug",
"bug_report_title": "A clear, concise title summarizing the
issue",
"bug_report_description": "Detailed description of the visual
bug or behavioral anomaly, including its appearance and
potential impact on gameplay",
"affected_item": "The specific game element (character, object,
environment, UI, physics) affected by the glitch"
}
FigureA6: Thedefaultpromptusedforgeneratingbugreportsbasedonagivenvideo.
21

PromptforVisualRegressionTask
You are an image comparison tool for video game quality assurance.
Given two screenshots from the same game scene, evaluate whether
the second image represents an acceptable variation of the
first (reference) image.
Consider these variations ACCEPTABLE:
- Player character customization elements
- Environmental conditions (weather, day/night cycle)
- Slight positional or animation differences
- Lighting and shadow adjustments
- Minor variations in non-critical background elements
Consider these variations UNACCEPTABLE:
- Interface corruption or element misalignment
- Textual content changes (unless expected, e.g., dynamic text)
- Significant visual artifacts or rendering errors (e.g., missing
textures, z-fighting)
- Major structural changes to scene geometry not attributable to
gameplay state
- Missing or grossly incorrect key scene elements compared to the
reference
Provide your assessment as JSON:
{
"reasoning": "Concise explanation of detected differences and
justification for your decision based on the criteria.",
"test_pass": true/false
}
FigureA7:Asamplepromptusedinthevisualregressiontasktodetectchangesbetweentwoversions
ofthesamescene.Dependingonthecomplexityandsourceofthescene—whethergeneratedinUnity
orextractedfromaYouTubevideo—theitemslistedunderacceptableandunacceptablecategories
vary.
PromptforDetectingClipping(ParametricTest)
You are a visual analysis assistant specializing in detecting
object clipping in video game screenshots. Your task is to
examine each provided image and determine whether any part of
the white cube is intersecting with the character model,
indicating a clipping issue.
Based on your analysis, respond using the following format:
{
"reasoning": "Brief explanation of why you think clipping is
present or not",
"clipping_detected": true or false
}
FigureA8: Thedefaultpromptusedforparametricteststodetectobjectclippingatvariousproximi-
ties.
22

PromptforNeedleInaHaystack
You are a specialized video game quality assurance analyst trained
to detect visual anomalies in gameplay footage. Your task is to
analyze the provided video clip to identify any bugs, glitches,
| visual      | artifacts, | or        | unexpected | behaviors.  |           |
| ----------- | ---------- | --------- | ---------- | ----------- | --------- |
| ## What to  | Look       | For       |            |             |           |
| Examine the | video      | carefully | for        | any:        |           |
| - Visual    | artifacts  | (texture  | issues,    | flickering, | clipping) |
| - Animation | problems   | (jerky    | movements, | T-poses)    |           |
| - Rendering | glitches   | (missing  | textures,  | lighting    | errors)   |
- Gameplay anomalies (collision failures, object teleportation)
| ## Response | Format |     |     |     |     |
| ----------- | ------ | --- | --- | --- | --- |
After your thorough analysis, provide your findings in this exact
| JSON | format: |     |     |     |     |
| ---- | ------- | --- | --- | --- | --- |
‘‘‘json
{
"reasoning": "Brief explanation of what you observed in the video
| and                | why it | appears     | to be a glitch", |     |     |
| ------------------ | ------ | ----------- | ---------------- | --- | --- |
| "glitch_detected": |        | true|false, |                  |     |     |
| "timestamp":       | 0      |             |                  |     |     |
}
‘‘‘
FigureA9: ThedefaultpromptusedforNeedleInaHaystackteststodetectandlocateglitchesina
videoclips
23

E LLM-as-a-Judge
DeveloperPromptMessageforEvaluatingBugReports
You are a quality assurance verification assistant that evaluates
| bug reports     | against |        | known | issues.  | When  | provided     | with | both a    |
| --------------- | ------- | ------ | ----- | -------- | ----- | ------------ | ---- | --------- |
| generated       | bug     | report | and   | a ground | truth | description, |      | your task |
| is to determine |         | if     | they  | describe | the   | same bug.    |      |           |
Compare the generated bug report with the ground truth description
| carefully.     | Focus     | on  | whether      | they | identify | the     | same | core issue, |
| -------------- | --------- | --- | ------------ | ---- | -------- | ------- | ---- | ----------- |
| even if        | expressed |     | differently. |      |          |         |      |             |
| Respond *only* | with      | the | following    |      | JSON     | format: |      |             |
{
| "reasoning": |              | "Detailed |            | explanation   |              | of why the | bug          | report does |
| ------------ | ------------ | --------- | ---------- | ------------- | ------------ | ---------- | ------------ | ----------- |
| or does      | not match    |           | the ground | truth         | description, |            | highlighting |             |
| specific     | similarities |           | or         | differences", |              |            |              |             |
| "match":     | true         | or        | false      |               |              |            |              |             |
}
FigureA10: Asampledevelopermessageusedwitho3tojudgetheaccuracyofabugreportgivena
groundtruthlabel.
24

DeveloperPromptMessageforEvaluatingBugReports
You are a quality assurance verification assistant that evaluates
bug reports against known issues. Your task is to determine if a
generated bug report and a ground truth description refer to
the same underlying bug.
When comparing:
- Focus on the core issue or behavior rather than exact wording
- Consider if they describe the same symptoms, affected features,
and conditions
- A match exists even if details like error messages or steps
differ slightly
- Pay attention to technical specifics that distinguish similar-
looking bugs
Two descriptions may use different terminology but still describe
the same bug. Conversely, reports with similar symptoms might
describe different bugs if they have different root causes.
Your final response should be a JSON object with the following
format:
{
"reasoning": "Detailed explanation of why the bug report does
or does not match the ground truth description, highlighting
specific similarities or differences",
"match": true or false
}
FigureA11: Asampledevelopermessageusedwitho3tojudgetheaccuracyofavideo-basedbug
reportgenerationtask,givenagroundtruthlabel.
25

F Samplesfordifferentglitchtypes
F.1 Missingorcorruptedassets/textures
|            | (a)                                   | (b)               |
| ---------- | ------------------------------------- | ----------------- |
| FigureA12: | Examplesofmissingorcorruptedtextures. | Sources: (a),(b). |
F.2 Geometryandrasterizationissues
|     | (a) | (b) |
| --- | --- | --- |
FigureA13: Examplesofgeometryandrasterizationissues(z-fightingandshadowacne). Sources:
(a),(b).
F.3 Temporalinstability
|     | (a) | (b) |
| --- | --- | --- |
FigureA14: Examplesoftemporalinstability. 3Dmeshesstarttoappearslowlyinthegamewitha
noticeabledelay. Pleasewatchthevideoformoredetails.
26

F.4 Post-processingandUIartifacts
|            | (a)                                      | (b)               |
| ---------- | ---------------------------------------- | ----------------- |
| FigureA15: | Examplesofpost-processingandUIartifacts. | Sources: (a),(b). |
F.5 Physicsandcollisionfailures
|            | (a)                                    | (b)               |
| ---------- | -------------------------------------- | ----------------- |
| FigureA16: | Examplesofphysicsandcollisionfailures. | Sources: (a),(b). |
F.6 Animation/stateerrors
|            | (a)                              | (b)               |
| ---------- | -------------------------------- | ----------------- |
| FigureA17: | Examplesofanimation/stateerrors. | Sources: (a),(b). |
27

F.7 Worldandruleviolations
| (a)        |                                   | (b)               |
| ---------- | --------------------------------- | ----------------- |
| FigureA18: | Examplesofworldandruleviolations. | Sources: (a),(b). |
28

G AdditionalResults
G.1 AdditionalResultsfortheVisualUnitTestingTask
(a) (b)
(c) (d)
(e) (f)
Figure A19: Common failures among tested models for visual unit testing include: (a) models
strugglingtoaccuratelyreportthecharacter’sposture,direction,timeofday,andotherscenedetails;
(b)modelsstrugglingtoreportwhethertheshuttleorientationisupwardordownward;(c)models
failingtoreportwhetherthedoorontherightisopenorclosed;(d)modelsfailingtodetectwhether
theorientationoftheaircraftisfacingtowardorawayfromthecamera;(e)modelsfailingtonotice
smalldetailsoncharacters’clothing;and(f)modelsfailingtodescribethefacialhairofthecharacter.
29

G.2 AdditionalResultsfortheUIUnitTestingTask
(a) (b)
(c) (d)
(e) (f)
FigureA20: CommonfailuresamongthetestedmodelsforUIunittestinginclude: (a)modelsfailing
toreadUIelementsatthetopoftheimagetocalculatethenumberofobjectivescapturedandthe
remainingobjectives; (b)modelsfailingtorecognizealltextualelementsinthescene, including
the exact positions of numbers on the orange and blue tiles; (c) models failing to recognize the
current values of various customized progress bars; (d) models failing to read information from
grids,suchastilepieces,dicenumbers,orconfigurationsofgameboards;(e)modelsstrugglingto
readspeedometervaluesandextractpositionalinformationfrommaps;(f)modelsfailingtoextract
positionalinformationfrommapsanddeterminerelationshipsbetweenspecificnodes.
30

G.3 ModelrefusalratesandmalformedJSON
Tab. A6 shows unified parse-error rate that combines two related failure modes: (i) the model
generatessyntacticallyinvalidJSON,or(ii)itrefusestoproduceananswer.Weunifybothmalformed
outputsandrefusalsunderasingleparse-errorratemetricbecausebothpreventdownstreamscoring.
Overall,errorratesarelowandconfirmthatrequiringJSONstructuredoesnotmeaningfullyreduce
taskperformance. Formostmodels,parseerrorsremainbelow3%,primarilyarisingfromminor
bracketorquotationmismatchesinUI/unit-testtasks. TheonlynotableoutlierisGemma-3,which
showsan8.7%errorrateinimage-basedglitchdetectiontask;however,manualinspectionreveals
thatnearlyallcasescorrespondtorefusals(Icannothelpwiththat)ratherthantruesyntaxfailures.
Among video-based tasks, and exhibit elevated refusal rates (14% and 28%,
Sonnet-3.5 GPT-4.1
respectively)onlongerclips,reflectingtemporaryrefusaltriggersratherthanstructuraldecoding
issues.
Insummary, structuredoutputcomplianceremainsrobustacrossalltasks,andparsingerrorsare
dominatedbyrefusalsratherthansyntax, indicatingthatenforcingaJSONschemaisasafeand
informativediagnosticratherthanalimitingfactor.
TableA6: Parse-errorrates(%)causedbymodelsproducingmalformedJSONorrefusingtoanswer.
Overallerrorratesarelow, confirmingthatenforcingaJSONschemadoesnotitselfreducetask
performance. GPT-4.1exhibitsthehighesterrorrateonvideo-basedtasks,primarilyduetorefusals
toanswer.
|                        |           | Image |      |      |       | Video |
| ---------------------- | --------- | ----- | ---- | ---- | ----- | ----- |
|                        | VU        | UI VR | IGD  | PCD  | VGD   | NIAH  |
| Model/#Samples         | 100 100   | 250   | 1000 | 686  | 1000  | 100   |
| GPT-4.1                | 0.0 0.00  | 0.00  | 0.00 | 0.0  | 0.00  | 4.00  |
| GPT-4.1-mini           | 0.0 0.00  | 0.00  | 0.10 | 0.0  | 0.00  | 0.00  |
| GPT-4.1-nano           | 0.0 1.00  | 0.00  | 0.00 | 0.0  | 0.00  | 0.00  |
| GPT-4o                 | 0.0 1.00  | 0.00  | 0.10 | 0.0  | 28.20 | 93.00 |
| o4-mini                | 0.0 4.00  | 0.00  | 0.00 | 0.0  | 0.20  | 0.00  |
| o3                     | 0.0 1.00  | 0.00  | 0.00 | 0.0  | 0.00  | 0.00  |
| Gemini-2.5-Pro         | 0.0 1.00  | 0.00  | 0.00 | 0.0  | 0.00  | 0.00  |
| Gemini-2.5-Flash       | 0.0 1.00  | 0.00  | 0.00 | 0.0  | 0.00  | 0.00  |
| Gemini-2.0-Flash       | 0.0 0.00  | 0.00  | 0.00 | 0.0  | 0.00  | 0.00  |
| Sonnet-3.7             | 0.0 0.00  | 0.80  | 0.00 | 0.0  | 0.40  | 0.00  |
| Sonnet-3.5             | 0.0 0.00  | 0.00  | 0.10 | 0.0  | 14.00 | 1.00  |
| Llama-4-Scout          | 4.00 2.00 | 0.00  | 0.10 | 0.14 | 4.00  | –     |
| Llama-4-Maverick       | 4.00 1.00 | 0.00  | 0.10 | 0.58 | 5.30  | –     |
| Gemma-3(27B)           | 2.00 0.00 | 0.00  | 8.70 | 0.00 | 0.20  | –     |
| Mistral-Small-3.1(24B) | 0.00 0.00 | 0.00  | 0.00 | 0.00 | 3.60  | –     |
| Qwen-2.5-VL(72B)       | 0.00 2.00 | 0.80  | 0.20 | 0.00 | 13.10 | –     |
31

G.4 AdditionalPerformanceMetricsfortheGlitchDetectionTasks
Inthissection,weprovideperformancemetricsfordifferentmodels. Thetotalnumberoftestcases
inbothimage-andvideo-basedglitchdetectionis1,000. The#samplescolumnisnotalways1,000
becausesomemodelseithergeneratedinvalidJSONorrefusedtoprovideavalidanswertothegiven
questionforvariousreasons.
Table A7: Performance metrics for different models on the image-based glitch detection task.
MetricsincludeAccuracy(Acc), TruePositives(TP),TrueNegatives(TN),FalsePositives(FP),
FalseNegatives(FN),Precision(Prec),Recall(Rec),F1Score(F1),andSpecificity(Spec).
| Model        | Acc. TP  | FP FN TN Prec.  | Rec. F1   | Spec. #Samples |
| ------------ | -------- | --------------- | --------- | -------------- |
| GPT-4.1      | 81.3 374 | 61 126 439 86.0 | 74.8 80.0 | 87.8 1,000     |
| GPT-4o-mini  | 76.9 468 | 199 32 300 70.2 | 93.6 80.2 | 60.1 999       |
| GPT-4.1-nano | 57.0 413 | 343 87 157 54.6 | 82.6 65.8 | 31.4 1,000     |
| GPT-4o       | 82.9 417 | 89 82 411 82.4  | 83.6 83.0 | 82.2 999       |
|              | 76.4 331 | 67 169 433 83.2 | 66.2 73.7 | 86.6 1,000     |
o4-mini
| o3               | 73.7 253 | 16 247 484 94.1 | 50.6 65.8 | 96.8 1,000 |
| ---------------- | -------- | --------------- | --------- | ---------- |
| Gemini-2.5-Pro   | 75.5 418 | 164 81 336 71.8 | 83.8 77.3 | 67.2 999   |
| Gemini-2.5-Flash | 66.4 215 | 52 284 448 80.5 | 43.1 56.1 | 89.6 999   |
| Gemini-2.0-Flash | 68.1 259 | 78 241 422 76.9 | 51.8 61.9 | 84.4 1,000 |
| Sonnet-3.7       | 65.1 177 | 26 323 474 87.2 | 35.4 50.4 | 94.8 1,000 |
|                  | 70.2 238 | 37 261 463 86.5 | 47.7 61.5 | 92.6 999   |
Sonnet-3.5
| Llama-4-Scout     | 55.9 74  | 16 425 484 82.2  | 14.8 25.1  | 96.8 999   |
| ----------------- | -------- | ---------------- | ---------- | ---------- |
| Llama-4-Maverick  | 53.3 44  | 11 456 488 80.0  | 8.8 15.9   | 97.8 999   |
| Gemma-3           | 51.2 460 | 446 0 7 50.8     | 100.0 67.3 | 1.5 913    |
| Mistral-Small-3.1 | 59.7 230 | 133 270 367 63.4 | 46.0 53.3  | 73.4 1,000 |
|                   | 70.1 254 | 52 246 446 83.0  | 50.8 63.0  | 89.6 998   |
Qwen-2.5-VL
TableA8: Performancemetricsfordifferentmodelsonthevideo-basedglitchdetectiontask. Metrics
include Accuracy (Acc), True Positives (TP), True Negatives (TN), False Positives (FP), False
Negatives(FN),Precision(Prec),Recall(Rec),F1Score(F1),andSpecificity(Spec).
| Model        | Acc. TP  | FP FN TN Prec. | Rec. F1        | Spec. #Samples |
| ------------ | -------- | -------------- | -------------- | -------------- |
| GPT-4.1      | 76.6 411 | 149 83 347     | 73.4 83.2 78.0 | 70.0 990       |
| GPT-4o-mini  | 72.2 346 | 124 153 372    | 73.6 69.3 71.4 | 75.0 995       |
| GPT-4.1-nano | 49.9 466 | 468 24 25      | 49.9 95.1 65.5 | 5.1 983        |
| GPT-4o       | 79.9 356 | 53 90 214      | 87.0 79.8 83.3 | 80.2 713       |
|              | 73.1 330 | 115 143 370    | 74.2 69.8 71.9 | 76.3 958       |
o4-mini
| o3               | 77.2 298 | 27 200 470 | 91.7 59.8 72.4 | 94.6 995   |
| ---------------- | -------- | ---------- | -------------- | ---------- |
| Gemini-2.5-Pro   | 78.1 334 | 53 166 447 | 86.3 66.8 75.3 | 89.4 1,000 |
| Gemini-2.5-Flash | 64.7 426 | 279 74 221 | 60.4 85.2 70.7 | 44.2 1,000 |
| Gemini-2.0-Flash | 54.5 477 | 432 23 68  | 52.5 95.4 67.7 | 13.6 1,000 |
| Sonnet-3.7       | 67.4 250 | 79 245 419 | 76.0 50.5 60.7 | 84.1 993   |
|                  | 73.6 266 | 70 150 346 | 79.2 63.9 70.7 | 83.2 832   |
Sonnet-3.5
| Llama-4-Scout     | 61.0 117 | 25 349 469  | 82.4 25.1 38.5 | 94.9 960 |
| ----------------- | -------- | ----------- | -------------- | -------- |
| Llama-4-Maverick  | 59.8 82  | 6 375 484   | 93.2 17.9 30.1 | 98.8 947 |
| Gemma-3           | 51.4 498 | 484 1 15    | 50.7 99.8 67.2 | 3.0 998  |
| Mistral-Small-3.1 | 63.7 238 | 112 238 376 | 68.0 50.0 57.6 | 77.0 964 |
|                   | 55.1 99  | 2 388 380   | 98.0 20.3 33.7 | 99.5 869 |
Qwen-2.5-VL
32

G.5 IsGPT-4oReadytoBeDeployedasanAutonomousGlitch-DetectionSystem?
Giventheobservedtestaccuracyof82.9%forGPT-4oinglitchdetectiontask(withanequalnumber
ofglitchandglitch-freeimages),thenaturalquestionarises: Isthisperformancesufficientforreal-
worldautonomousdeployment? Toaddressthisquestion,itisimportanttoconsiderthereal-world
scenariowhereglitchesarerelativelyrare.
Ifweassumethataglitchappearsinonly5%ofnormalgameplaysessions,thisprevalenceassumption
significantlychangestheperformancecharacteristics. Specifically,theconfusionmatrixobtained
fromourcontrolledbenchmarktest(Tab.A7)translatespoorlytoreal-worldprecision. Giventhe
currentmodel:
Deploymenttargets
• Recall≥95%onthebalancedbenchmark.
• False-positiverate≤0.5%(≤2FPin500normals).
• Precision≥90%whenprevalenceis5%.
• Balancedaccuracy≥97%.
Balanced-benchmarkperformanceofGPT-4o
FromTab.A7(999images,499glitch/500normal):
TP=417, FP=89,
FN=82, TN=411.
• Recall=417/(417+82)=83.6%(11.4ppbelowthe95%target).
• False-positiverate=89/(89+411)=17.8%(35.6×theallowable0.5%).
| • Balancedaccuracy= | 1(83.6+82.2)=82.9%(14.1ppshortof97%). |     |     |     |
| ------------------- | ------------------------------------- | --- | --- | --- |
2
• Precision=417/(417+89)=82.4%.
Projectedreal-worldperformance(5%prevalence)
Letp = 0.05betherealglitchrateandα = 17.8%themeasuredFPR.Withprevalenceshiftwe
obtain
|           | pRecall |     | 0.05×0.836 |         |
| --------- | ------- | --- | ---------- | ------- |
| Precision | =       | =   |            | =19.8%. |
p=0.05
|     | pRecall+(1−p)α | 0.05×0.836+0.95×0.178 |     |     |
| --- | -------------- | --------------------- | --- | --- |
Interpretation: inliveuse,roughly∼5alarmswillbefalseforeverytrueglitchdetected.
Assessment: GPT-4ofallsshortofallfourdeploymenttargets:
|     | Metric             | Target GPT-4o | Gap            |     |
| --- | ------------------ | ------------- | -------------- | --- |
|     | Recall(balanced)   | ≥95% 83.6%    | −11.4pp        |     |
|     | False-positiverate | ≤0.5% 17.8%   | +17.3pp(35.6×) |     |
|     | Precision(5%)      | ≥90% 19.8%    | −70.2pp        |     |
|     | Balancedaccuracy   | ≥97% 82.9%    | −14.1pp        |     |
Despiterelativityhighaccuracyinbalanced-benchmark,GPT-4o’shighfalse-positiveratedominates
underreal-worldclassimbalance,crushingprecisionto∼20%.
Conclusion: GPT-4o,initspresentconfiguration,isnotyetreadyfor standaloneautonomousbug
detection. Substantialimprovementsinbothsensitivity(recall)andspecificity(false–positivecontrol)
arerequiredbeforedeploymentcanbeconsidered.
33

G.6 CommonFalsePositivePatterns,asSummarizedbyo3
PromptforSummarizingFalsePositiveCases
Analyze false positive cases from the glitch detection system to
|     | identify           | recurring | patterns.    | Create         | a structured | summary that: |
| --- | ------------------ | --------- | ------------ | -------------- | ------------ | ------------- |
|     | 1. Lists the       | 3-5 most  | common       | false positive | types        |               |
|     | 2. Notes frequency |           | and severity | patterns       |              |               |
Keep your summary under 500 words with clear, actionable insights.
FigureA21: Thepromptusedwitho3toreadthereasoningfieldsforfalsepositivecasesfromtop
modelsandsummarizetheircommonpatterns.
|      | TableA9:           | Recurringfalse–positivethemesinGPT-4.1’soutput(N |           |           |                        | =61). |
| ---- | ------------------ | ------------------------------------------------ | --------- | --------- | ---------------------- | ----- |
| Rank | False-positivetype |                                                  | Frequency | Severity† | Typicaltrigger/pattern |       |
1 Model/propclipping&intersection 27(44%) Low–Moderate Meshoverlapflaggedevenwhenbrieforhidden
behindUI.
2 Missing/distortedtextures&artifacts 14(23%) Moderate Largeplaceholdercoloursorhigh-contrastpatterns;
mis-classifiesVFX/debugoverlays.
3 Floating/mis-alignedactorsorobjects 12(20%) Low Heightcheckstoostrict;intentionaloffsetsonun-
eventerrainreported.
4 UI/text-renderissues 9(15%) Low–Moderate AnymismatchbetweenworldandHUDlayers(over-
lays,mods)triggersalert.
†Severitygaugesplayerimpact:cosmetic(low)togameplay-blocking(high).
|      | TableA10:          | Recurringfalse–positivethemesinGPT-4o’soutput(N |           |           |                        | =90). |
| ---- | ------------------ | ----------------------------------------------- | --------- | --------- | ---------------------- | ----- |
| Rank | False-positivetype |                                                 | Frequency | Severity† | Typicaltrigger/pattern |       |
1 Floating/unsupportedentities ∼40% Moderate Characters,vehiclesorsceneryhoveringabove
terrainorwater
2 Clipping&collisionoverlaps ∼30% Moderate–High Limbs,weaponsorduplicatemodelsintersect-
inggeometryoreachother
3 Missing/placeholdertextures ∼15% High Bright-pink or solid-blue fallback materials,
transparent/missingwalls
4 UI/textanomalies ∼10% Low HUD layers visible through world, “????”
strings,overlappingmenus
5 Model/texturedistortions ∼5% Medium Elongatedlimbs/necks,stretchedterrain,unnat-
uralglobalcolortints
†SeverityisqualitativeandreflectstypicalimpactongameplayandQAtriageeffort.
34

TableA11: Recurringfalse–positivethemesinGemini-2.5-Pro’soutput(N =165).
Rank False-positivetype Frequency Severity† Typicaltrigger/pattern
1 Modelclipping/interpenetration 27(44%) Low–Medium Limbs,weapons,orvehiclesintersectingter-
rainorothermeshes;descriptionsusing“clip-
ping”,“inside”,“passingthrough”.
2 UI&text-layouterrors 15(25%) Low–Medium Overlapping chat/tooltips, truncated strings,
cursorordebuglabelsdrawnonwronglayer.
3 Physics/collisionanomalies 9(15%) Medium Floatingcharactersorprops,impossibleresting
angles,ragdollsstuckingeometry.
4 Numericalorlogicalinconsistencies 6(10%) Medium Impossible values (e.g. 100.58% accuracy,
“00:16:65”timers,“+0points→promotion”).
5 Rendering/textureartifacts 3(5%) Low Rainbow shaders, corrupted textures, over-
bloomormissingmaterialsvisibleonlyonsur-
faces.
†Severityranksthetypicalgameplayimpact:Low=cosmetic,Medium=maymisleadorsoft-lock,High=
blocksprogressorcrashes.
35

G.7 AdditionalResultsfortheGlitchDetectionTask
GPT-4o’soutput:
{
"reasoning": "The vehicle is floating above the trees, which is
| not typical              |         | behavior | in    | the | game.", |             |     |         |
| ------------------------ | ------- | -------- | ----- | --- | ------- | ----------- | --- | ------- |
| "glitch_detected":       |         |          | true, |     |         |             |     |         |
| "description_of_glitch": |         |          |       | "A  | vehicle | is floating | in  | mid-air |
| above the                | trees." |          |       |     |         |             |     |         |
}
o4-mini’soutput:
{
"reasoning": "There’s an unexpected blank white bar at the bottom
of the HUD where game info (such as health or status) should be
| rendered,          | indicating |     | a     | missing | or corrupted |     | UI texture.", |     |
| ------------------ | ---------- | --- | ----- | ------- | ------------ | --- | ------------- | --- |
| "glitch_detected": |            |     | true, |         |              |     |               |     |
"description_of_glitch": "A plain white rectangle is displayed at
| the bottom | center     |     | of the | screen  | instead | of  | the normal     | HUD |
| ---------- | ---------- | --- | ------ | ------- | ------- | --- | -------------- | --- |
| element,   | suggesting |     | a UI   | texture | failed  | to  | load or render |     |
properly."
}
GPT-4.1’soutput:
{
"reasoning": "The vehicle visible through the scope appears to be
| floating | above | the | trees, | which | is not | typical | behavior | for |
| -------- | ----- | --- | ------ | ----- | ------ | ------- | -------- | --- |
vehicles in the game. Normally, vehicles should be on the ground
| , not suspended    |     | in  | mid-air.", |     |     |     |     |     |
| ------------------ | --- | --- | ---------- | --- | --- | --- | --- | --- |
| "glitch_detected": |     |     | true,      |     |     |     |     |     |
"description_of_glitch": "A vehicle is floating above the trees,
| indicating      | a   | physics | or  | rendering | glitch        | where | the vehicle | is  |
| --------------- | --- | ------- | --- | --------- | ------------- | ----- | ----------- | --- |
| not interacting |     | with    | the | terrain   | as expected." |       |             |     |
}
FigureA22:Samplesuccessfulglitchdetectionsbyvariousmodelsthatidentifiedthefloatingvehicle.
36

Gemini-2.5-Pro’soutput:
{
"reasoning": "The player character appears to be holding both a
knife and a pistol simultaneously in a way that suggests a
visual glitch. The knife model seems to be superimposed or
clipping through the hand that is holding the pistol. In most
first-person games, including Payday 2 (which this game appears
to be), players switch between melee and ranged weapons rather
than wielding them concurrently in this manner.",
"glitch_detected": true,
"description_of_glitch": "The character model is incorrectly
displaying both a melee weapon (knife) and a firearm (pistol) as
actively wielded at the same time, with the knife model
appearing to clip through or be superimposed on the hand holding
the pistol."
}
Qwen-2.5-VL’soutput:
{
"reasoning": "The screenshot shows a player holding both a
knife and a gun simultaneously, which is not typical in most
games where players can only wield one weapon at a time. This
suggests a potential glitch in the game’s weapon handling system
.",
"glitch_detected": true,
"description_of_glitch": "The player is holding a knife and a
gun at the same time, which is not a standard feature in the
game and indicates a glitch in the weapon system."
}
GPT-4.1-mini’soutput:
{
"reasoning": "The knife held by the character is unusually
large and appears to be clipping through the hand, which is not
typical for the game’s weapon models. This suggests a graphical
or model scaling glitch.",
"glitch_detected": true,
"description_of_glitch": "The knife model is abnormally large
and clips through the character’s hand, indicating a weapon
model scaling or rendering glitch."
}
FigureA23: Samplesuccessfulglitchdetectionsbyvariousmodelsthatidentifiedaclippingknife
overlappingwithagun.
37

Llama-4-Maverick’soutput:
{
"reasoning": "The screenshot appears to be a scene from a video
game where a police officer is standing in the middle of a road
with an ambulance and a police car nearby. The image does not
show any obvious graphical distortions, texture issues, or
abnormal behavior that would typically be associated with
glitches. The scene looks like it is part of the game’s intended
content, with the character and vehicles positioned in a
plausible scenario. The text at the bottom of the screen
suggests a narrative or dialogue element, further indicating it
is part of the game’s story or interaction.",
"glitch_detected": false,
"description_of_glitch": ""
}
Gemini-2.0-Flash’soutput:
{
"reasoning": "Based on the image, there is no indication of any
glitches. The graphics appear normal, and there are no visual
artifacts or anomalies that would suggest a problem with the
game’s rendering or programming.",
"glitch_detected": false,
"description_of_glitch": ""
}
Sonnet-3.7’soutput:
{
"reasoning": "The screenshot appears to show normal gameplay
from what seems to be a police or emergency services simulation
game. The scene shows a character in a police uniform standing
on a street with an ambulance and police vehicle parked nearby.
The UI elements, including mission text (in what appears to be
Chinese characters), progress bars, and resource counters are
all displaying normally. The vehicles and environment are
rendering as expected without any visual artifacts, texture
issues, or clipping problems.",
"glitch_detected": false,
"description_of_glitch": ""
}
FigureA24: Sampleimagewheremodelsfailedtodetectaclippingglitchbetweentwocars.
38

o4-mini’soutput:
{
| "reasoning": | "One of | the | soldiers | on  | the | left | is clipping |     |
| ------------ | ------- | --- | -------- | --- | --- | ---- | ----------- | --- |
through the lower bunk rather than standing or climbing normally
| , and their              | arms and       | torso | intersect  |     | the bed | mesh     | in  | an          |
| ------------------------ | -------------- | ----- | ---------- | --- | ------- | -------- | --- | ----------- |
| unnatural                | way.",         |       |            |     |         |          |     |             |
| "glitch_detected":       | true,          |       |            |     |         |          |     |             |
| "description_of_glitch": |                |       | "Character |     | model   | is stuck |     | in the bunk |
| bed, clipping            | through        | the   | mattress   | and | frame   | instead  |     | of          |
| animating                | a proper climb | or    | stand."    |     |         |          |     |             |
}
Gemini-2.5-Pro’soutput:
{
| "reasoning": | "The character |     | on  | the | bottom | left | bunk | bed has |
| ------------ | -------------- | --- | --- | --- | ------ | ---- | ---- | ------- |
their legs and lower torso clipping through the mattress and bed
| frame,                   | which is a common    |     | visual         | glitch.", |         |        |         |             |
| ------------------------ | -------------------- | --- | -------------- | --------- | ------- | ------ | ------- | ----------- |
| "glitch_detected":       | true,                |     |                |           |         |        |         |             |
| "description_of_glitch": |                      |     | "A character’s |           | lower   |        | body    | is clipping |
| through                  | a bed. Specifically, |     | the            | character |         | on the | bottom  | left        |
| bunk bed                 | has their legs       | and | lower          | torso     | passing |        | through | the         |
| mattress                 | and bed frame."      |     |                |           |         |        |         |             |
}
Sonnet-3.5’soutput:
{
| "reasoning":       | "The image    | shows |             | characters |           | clipping       | through/ |     |
| ------------------ | ------------- | ----- | ----------- | ---------- | --------- | -------------- | -------- | --- |
| intersecting       | with hospital |       | beds,       | which      | is        | not physically |          |     |
| possible           | and appears   | to be | a collision |            | detection |                | issue",  |     |
| "glitch_detected": | true,         |       |             |            |           |                |          |     |
"description_of_glitch": "Character models are clipping through
| the hospital | beds instead    |     | of lying |          | properly | on         | top | of them. |
| ------------ | --------------- | --- | -------- | -------- | -------- | ---------- | --- | -------- |
| This appears | to be happening |     | with     | multiple |          | characters |     | in the   |
scene, suggesting a collision detection or character positioning
glitch."
}
Figure A25: Sample image where various models incorrectly reported the presence of a glitch,
althoughtheimageisglitch-free.
39

Llama-4-Scout’soutput:
{
| "reasoning": | "The | image | appears | to  | be  | a normal | in-game |     |     |
| ------------ | ---- | ----- | ------- | --- | --- | -------- | ------- | --- | --- |
screenshot from MotoGP24, showing a motorcycle race with a rider
| on a track. | There              | are no        | obvious   |      | visual | artifacts, |          | clipping |     |
| ----------- | ------------------ | ------------- | --------- | ---- | ------ | ---------- | -------- | -------- | --- |
| issues,     | or other graphical |               | anomalies |      | that   | would      | indicate |          | a   |
| glitch.     | The scene          | is consistent |           | with | what   | is         | expected | in       | a   |
racing game.",
| "glitch_detected":       |     | false, |     |     |     |     |     |     |     |
| ------------------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| "description_of_glitch": |     |        | ""  |     |     |     |     |     |     |
}
o4-mini’soutput:
{
| "reasoning": | "The | scene | shows | a well-rendered |     |     | MotoGP | bike |     |
| ------------ | ---- | ----- | ----- | --------------- | --- | --- | ------ | ---- | --- |
leaning on the track with proper textures, lighting, and depth-
of-field. There are no visible clipping issues, missing textures
| , or geometry            | errors.", |        |     |     |     |     |     |     |     |
| ------------------------ | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| "glitch_detected":       |           | false, |     |     |     |     |     |     |     |
| "description_of_glitch": |           |        | ""  |     |     |     |     |     |     |
}
Qwen-2.5-VL’soutput:
{
| "reasoning": | "The          | image  | appears      | to  | be    | a normal | scene    | from    | the    |
| ------------ | ------------- | ------ | ------------ | --- | ----- | -------- | -------- | ------- | ------ |
| game MotoGP  | 24, showing   |        | a motorcycle |     | racer | on       | a track  | with    | a      |
| large bull   | statue        | in the | background.  |     | There | are      | no       | visible |        |
| anomalies    | or unexpected |        | behaviors    |     | that  | would    | indicate | a       | glitch |
.",
| "glitch_detected":       |     | false, |     |     |     |     |     |     |     |
| ------------------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
| "description_of_glitch": |     |        | ""  |     |     |     |     |     |     |
}
FigureA26: Sampleimagewherevariousmodelscorrectlyreportedtheimageasglitch-free.
40

G.8 SampleFalsePositiveandFalseNegativeCasesintheImage-basedGlitchDetectionTask
thatMostModelsLabeledIncorrectly
Inthissection,weprovidesampleimagesfromcommonfalsepositiveandfalsenegativecases,where
mostmodelsareconfusedaboutthecorrectlabeloftheimage.
FigureA27: Sampleimagesfromimage-basedglitchdetection,wheremodelsreportedtheimageas
glitchydespiteitbeingglitch-free(falsepositive).
41

FigureA28: Sampleimagesfromimage-basedglitchdetection,wherethemajorityofmodelsfailed
todetecttheglitchintheimage(falsenegative).
42

G.9 AdditionalResultsfortheVideo-basedGlitchDetectionTask
GPT-4.1’soutput:
{
"reasoning": "In the sequence of images, the player character’s
model appears to be severely distorted, particularly around the
torso and back area, which is unnaturally enlarged and misshapen
. This is not consistent with normal character models in video
games and suggests a graphical or animation glitch affecting the
character’s mesh or skeleton.",
"glitch_detected": true,
"description_of_glitch": "The player character’s body is
unnaturally deformed, with an exaggerated and misshapen torso
and back, indicating a character model or animation glitch."
}
Gemini-2.0-Flash’soutput:
{"description_of_glitch": "The character’s back is unnaturally
deformed, suggesting a glitch in the character model or
animation.", "glitch_detected": true, "reasoning": "The
character’s back appears to have a large, unnatural bulge, which
is not typical of human anatomy and suggests a graphical or
animation error."}
Figure A29: Sample from a video-based glitch detection task in which various models correctly
identifiedaglitchrelatedtothecharacter’sbody.
43

o3’soutput:
{
"reasoning": "After the skater bails, the board no longer behaves
normally. It repeatedly clips halfway into the sidewalk,
jitters and spins in place, and even drifts around on its own
while the player simply stands or walks nearby. At times the
character’s feet also sink slightly into the pavement. These
collision/physics oddities are not part of normal gameplay and
indicate a bug in the board-to-ground physics.",
"glitch_detected": true,
"description_of_glitch": "Skateboard becomes stuck half-inside
the ground, jittering, spinning and sliding by itself;
occasional foot clipping through the pavement."
}
o4-mini’soutput:
{
"description_of_glitch": "After the player dismounts the
skateboard, the board begins to move erratically on its own,
spinning and flipping rapidly on the ground.",
"glitch_detected": true,
"reasoning": "The skateboard’s movement is unnatural and not
caused by player input or expected physics interactions. It
appears to be a physics engine glitch where the board’s
collision or state becomes unstable."
}
GPT-4.1’soutput:
{
"reasoning": "In the sequence of images, the skateboard is seen
moving and spinning on its own, without any interaction from the
player character. It even clips through the ground and other
objects, which is not normal behavior for a skateboard in a
skateboarding game. This indicates a physics or collision glitch
.",
"glitch_detected": true,
"description_of_glitch": "The skateboard exhibits erratic,
unintended movement and clips through the ground and other
objects, behaving independently of the player character. This is
likely due to a physics or collision detection glitch."
}
Figure A30: Sample from a video-based glitch detection task in which various models correctly
identifiedaglitchrelatedtoaskateboard.
44

G.10 AdditionalResultsfortheNeedleInAHaystackTask
Table A12: Model performance on the needle in a haystack task, reporting accuracy based on
thedistancebetweenthemodel-reportedframeandthegroundtruthframe,evaluatedatdifferent
thresholds(1secondsto5seconds).
|                  |     | Acc@ | Acc@ Acc@ | Glitches |     | Glitches    |     |
| ---------------- | --- | ---- | --------- | -------- | --- | ----------- | --- |
| ModelName        |     | #    |           |          |     |             |     |
|                  |     | ≤1s  | ≤2s ≤5s   | Detected |     | NotDetected |     |
| GPT-4.1          | 100 | 6    | 11        | 19       | 72  |             | 28  |
| GPT-4.1-mini     | 100 | 5    | 6         | 10       | 28  |             | 72  |
| GPT-4.1-nano     | 100 | 0    | 1         | 4        | 78  |             | 22  |
| GPT-4o           | 100 | 1    | 1         | 1        | 7   |             | 93  |
| o3               | 100 | 1    | 2         | 13       | 58  |             | 42  |
| Gemini-2.0-Flash | 100 | 28   | 31        | 35       | 56  |             | 44  |
| Gemini-2.5-Flash | 100 | 32   | 32        | 35       | 42  |             | 58  |
| Gemini-2.5-Pro   | 100 | 31   | 32        | 34       | 34  |             | 66  |
|                  | 100 | 8    | 15        | 27       | 39  |             | 61  |
Sonnet-3.5
| Sonnet-3.7 | 100 | 18  | 24  | 31  | 39  |     | 61  |
| ---------- | --- | --- | --- | --- | --- | --- | --- |
TableA13: Modelperformance(accuracy@differentthresholds)ontheneedleinahaystacktask,
evaluatedonthesubsetwherethemodeldetectedtheglitch. Accuracyindicateswhetherthemodel
cancorrectlylocatetheglitchframewithina50-framewindow.
| ModelName    |     | # Acc@≤1s | Acc@≤2s |      | Acc@≤5s |      |     |
| ------------ | --- | --------- | ------- | ---- | ------- | ---- | --- |
| GPT-4.1      |     | 72        | 8.3     | 15.3 |         | 26.4 |     |
| GPT-4.1-mini |     | 28        | 17.9    | 21.4 |         | 28.6 |     |
| GPT-4.1-nano |     | 78        | 0.0     | 1.3  |         | 5.1  |     |
|              |     | 7         | 14.3    | 14.3 |         | 14.3 |     |
GPT-4o
| o3               |     | 58  | 1.7  | 3.4  |     | 20.7 |     |
| ---------------- | --- | --- | ---- | ---- | --- | ---- | --- |
| Gemini-2.5-Pro   |     | 34  | 91.2 | 91.2 |     | 91.2 |     |
| Gemini-2.5-Flash |     | 42  | 76.2 | 76.2 |     | 78.6 |     |
| Gemini-2.0-Flash |     | 56  | 50.0 | 53.6 |     | 55.4 |     |
| Sonnet-3.7       |     | 39  | 46.2 | 59.0 |     | 74.4 |     |
| Sonnet-3.5       |     | 39  | 20.5 | 38.5 |     | 61.5 |     |
45

G.11 AdditionalResultsfortheParametricClippingDetectionTask
Inthissection,weprovideheatmapvisualizationsforparametricrobustnesstasks,wherewevarythe
proximityofanobjecttoatargethumancharactertoevaluatewhetherthemodelscanrobustlydetect
whenaclippingglitchoccurs. Intheheatmaps,thereddatapointsindicatewrongresultsandgreen
datapointsindicatecorrectresultsfromtheVLM.
GPT-4.1
GPT-4.1-mini
GPT-4.1-nano
GPT-4o
o4-mini
o3
Gemini-2.5-Pro
Gemini-2.5-Flash
Gemini-2.0-Flash
Sonnet-3.7
Sonnet-3.5
Llama-4-Scout
Llama-4-Maverick
Gemma-3-27B
Mistral-Small
Qwen-2.5-VL
1 49 98 146 195 243 292 340 389 449 498 546 594 643 691 740 788 837 885 934 982 1030 1079 1127 1176
Frame
FigureA31: Heatmapfortestingclippingbetweenawhite3Dcubeandahumancharacter. The
dashedlineontheheatmapindicatestheframewhereclippingoccurs.
GPT-4.1
GPT-4.1-mini
GPT-4.1-nano
GPT-4o
o4-mini
o3
Gemini-2.5-Pro
Gemini-2.5-Flash
Gemini-2.0-Flash
Sonnet-3.7
Sonnet-3.5
Llama-4-Scout
Llama-4-Maverick
Gemma-3-27B
Mistral-Small
Qwen-2.5-VL
1 49 98 146 195 243 292 340 389 449 498 546 594 643 691 740 788 837 885 934 982 1030 1079 1127 1176
Frame
FigureA32: Heatmapfortestingclippingbetweenawhite3Dcubeandahumancharacter. The
dashedlineontheheatmapindicatestheframewhereclippingoccurs.
46

GPT-4.1
GPT-4.1-mini
GPT-4.1-nano
GPT-4o
o4-mini
o3
Gemini-2.5-Pro
Gemini-2.5-Flash
Gemini-2.0-Flash
Sonnet-3.7
Sonnet-3.5
Llama-4-Scout
Llama-4-Maverick
Gemma-3-27B
Mistral-Small
Qwen-2.5-VL
1 49 98 146 195 243 292 340 389 437 510 558 607 655 703 752 800 849 897 946 994 1043 1091 1139 1188
Frame
FigureA33: Heatmapfortestingclippingbetweenawhite3Dsphereandahumancharacter. The
dashedlineontheheatmapindicatestheframewhereclippingoccurs.
GPT-4.1
GPT-4.1-mini
GPT-4.1-nano
GPT-4o
o4-mini
o3
Gemini-2.5-Pro
Gemini-2.5-Flash
Gemini-2.0-Flash
Sonnet-3.7
Sonnet-3.5
Llama-4-Scout
Llama-4-Maverick
Gemma-3-27B
Mistral-Small
Qwen-2.5-VL
1 49 98 146 195 243 292 340 389 437 510 558 607 655 703 752 800 849 897 946 994 1043 1091 1139 1188
Frame
FigureA34: Heatmapfortestingclippingbetweenawhite3Dsphereandahumancharacter. The
dashedlineontheheatmapindicatestheframewhereclippingoccurs.
GPT-4.1
GPT-4.1-mini
GPT-4.1-nano
GPT-4o
o4-mini
o3
Gemini-2.5-Pro
Gemini-2.5-Flash
Gemini-2.0-Flash
Sonnet-3.7
Sonnet-3.5
Llama-4-Scout
Llama-4-Maverick
Gemma-3-27B
Mistral-Small
Qwen-2.5-VL
1 17 33 49 65 82 98 114 130 146 162 178 194 211 235 251 267 283 299 315 331 348 364 380 396
Frame
FigureA35: Heatmapfortestingclippingbetweenawhite2Dplane(quad)andahumancharacter.
Thedashedlineontheheatmapindicatestheframewhereclippingoccurs.
47

GPT-4.1
GPT-4.1-mini
GPT-4.1-nano
GPT-4o
o4-mini
o3
Gemini-2.5-Pro
Gemini-2.5-Flash
Gemini-2.0-Flash
Sonnet-3.7
Sonnet-3.5
Llama-4-Scout
Llama-4-Maverick
Gemma-3-27B
Mistral-Small
Qwen-2.5-VL
1 29 57 86 114 142 170 199 227 255 283 312 340 368 396 425 453 495 545 573 601 629 658 686
Frame
FigureA36: Heatmapfortestingclippingbetweenawhite2Dplane(quad)andahumancharacter.
Thedashedlineontheheatmapindicatestheframewhereclippingoccurs.
GPT-4.1
GPT-4.1-mini
GPT-4.1-nano
GPT-4o
o4-mini
o3
Gemini-2.5-Pro
Gemini-2.5-Flash
Gemini-2.0-Flash
Sonnet-3.7
Sonnet-3.5
Llama-4-Scout
Llama-4-Maverick
Gemma-3-27B
Mistral-Small
Qwen-2.5-VL
1 17 33 49 65 82 98 114 134 150 166 182 198 215 231 247 263 279 295 311 327 344 360 376 392
Frame
FigureA37: Heatmapfortestingclippingbetweentwohumancharacters. Thedashedlineonthe
heatmapindicatestheframewhereclippingoccurs.
48

G.12 AdditionalResultsfortheVisualRegressionTask
Sonnet-3.7’soutput:
{
"reasoning":"While both images show the same urban scene with
similar lighting (sunset/dusk), environment, and dialogue
subtitle, there are significant character differences that
exceed acceptable customization. The first image shows a
character in a white t-shirt and light pants, while the second
image shows a completely different character wearing a red
basketball jersey with the number 7, blue sleeves, and a cap.
This appears to be an entirely different character model rather
than just customization. The scene composition and background
environment remain consistent, but the character change is
substantial enough to be considered a major difference.",
"test_pass":false
}
GPT-4o’soutput:
{
"reasoning":"The second image shows a significant change in
character positions and actions, indicating a major scene
composition change. The character on the left is now in a
different pose, suggesting a different action or event is
occurring. These differences go beyond acceptable minor position
adjustments or character customization.",
"test_pass":false
}
o4-mini’soutput:
{
"reasoning":"The background and lighting remain the same, but
the primary character in the shot has been completely replaced
by two different characters, which constitutes a major scene
composition change rather than a simple customization or
animation tweak.",
"test_pass":false
}
FigureA38: Samplesuccessfultestrunbyvariousmodelsthatsuccessfullydetectedunacceptable
changesbetweentwoimages.
49

o4-mini’soutput:
{
| "reasoning":"Both |     | images    | show      | the | same | wooden | interior   | scene |     |
| ----------------- | --- | --------- | --------- | --- | ---- | ------ | ---------- | ----- | --- |
| with identical    |     | geometry, | lighting, |     | and  | asset  | placement. | There |     |
are only negligible framing and exposure differences, no missing
| textures,  | no           | UI corruption |     | or structural |     |     | changes. | This is | an  |
| ---------- | ------------ | ------------- | --- | ------------- | --- | --- | -------- | ------- | --- |
| acceptable | variation.", |               |     |               |     |     |          |         |     |
"test_pass":true
}
GPT-4.1’soutput:
{
| "reasoning":"The |     | two | images | depict | the | same | game | scene from | an  |
| ---------------- | --- | --- | ------ | ------ | --- | ---- | ---- | ---------- | --- |
identical perspective. The only noticeable difference is a very
slight change in the lighting and shadow patterns, likely due to
| minor       | adjustments | in             | the environmental |           |     | lighting  |         | or rendering |     |
| ----------- | ----------- | -------------- | ----------------- | --------- | --- | --------- | ------- | ------------ | --- |
| pass. There |             | are no missing |                   | textures, |     | interface | issues, |              |     |
misaligned elements, or significant changes to scene geometry or
| key objects. |             | All critical |     | scene | elements |     | are present | and |     |
| ------------ | ----------- | ------------ | --- | ----- | -------- | --- | ----------- | --- | --- |
| correctly    | rendered.", |              |     |       |          |     |             |     |     |
"test_pass":true
}
Gemini-2.5-Pro’soutput:
{
"reasoning":"TThe two provided screenshots are identical. There
are no discernible differences in geometry, lighting, textures,
| object    | placement, | or         | any other |     | visual | elements | between | the |     |
| --------- | ---------- | ---------- | --------- | --- | ------ | -------- | ------- | --- | --- |
| reference | and        | the second | image.",  |     |        |          |         |     |     |
"test_pass":true
}
FigureA39: Samplevisualregressiontestthattop-performingmodelslikeGPT-4o,GPT-4.1,o4-mini,
andGemini-2.5-Profailtoanswercorrectly. Themodelspassthetestwhentheyshouldfaildueto
oneofthewoodenpillarsoftheroofbeingmissinginthealternativeimage.
50

o4-mini’soutput:
{
"reasoning":"The only differences are environmental: the right-
side doorway is open to show the night sky and the railing
beyond, and a few cans are scattered further out on the floor.
No UI errors, missing textures, or structural issues. These are
minor background and lighting/scene-state variations, which are
acceptable.",
"test_pass":true
}
GPT-4.1’soutput:
{
"reasoning":"The primary difference between the two images is
the environmental condition visible through the window on the
right side. In the first image, the window shows an interior
wall, while in the second image, the window reveals an outdoor
night scene with mountains and sky. The rest of the scene,
including the vending machine, signage, and interior elements,
remains unchanged. This change is attributable to a possible
door or window being opened, which is a plausible gameplay or
environmental variation. There are no signs of interface
corruption, rendering errors, or missing key elements. The
variation is acceptable as it falls under environmental
condition changes.",
"test_pass":true
}
Gemini-2.5-Pro’soutput:
{
"reasoning":"The primary difference between the two images is
the background visible through the window on the right. In the
second image, a daytime sky and landscape are visible, whereas
the first image shows a dark exterior. This change is consistent
with acceptable environmental variations, such as a day/night
cycle. Other minor differences in debris placement are
negligible.",
"test_pass":true
}
FigureA40: Samplevisualregressiontestthattop-performingmodelslikeGPT-4o,GPT-4.1,o4-mini,
andGemini-2.5-Profailtoanswercorrectly. Themodelspassthetestwhentheyshouldfaildueto
incorrectwallrenderingontherightsideoftheimage.
51

o4-mini’soutput:
{
"reasoning":"The two images depict the same game scene with
only a very minor difference: in the first image, there is a red
cup on the ground near the bottom center, which is missing in
the second image. This is a minor variation in a non-critical
background element (debris/trash), which is acceptable according
to the criteria. There are no signs of interface corruption,
text changes, rendering errors, or missing key scene elements.",
"test_pass":true
}
GPT-4.1’soutput:
{
"reasoning":"The two shots are visually identical in
composition and geometry, with only very slight lighting/shadow
differences. No UI corruption, missing textures, text changes or
structural alterations are present. This falls under acceptable
lighting variation",
"test_pass":true
}
Gemini-2.5-Pro’soutput:
{
"reasoning":"The two images provided are identical. There are
no visual differences, rendering errors, or content changes
between the reference and the second image. Therefore, the
second image is an acceptable variation.",
"test_pass":true
}
FigureA41: Samplevisualregressiontestthattop-performingmodelslikeGPT-4o,GPT-4.1,o4-mini,
andGemini-2.5-Profailtoanswercorrectly. Themodelspassthetestwhentheyshouldfaildueto
missingthetableinthecenteroftheimage.
52

o4-mini’soutput:
{
"reasoning":"Both images depict the same scene with two
characters near a poolside, with consistent background elements
such as the hedge, tiled ground, and umbrella. The differences
observed are acceptable: the characters have different clothing
and are in slightly different positions, which can be attributed
to character customization and minor animation or timing
differences. The lighting is also different, which is an
acceptable change in time of day or weather. There are no
missing or corrupt UI elements, no graphical glitches, and the
environment structure remains unchanged.",
"test_pass":true
}
GPT-4.1’soutput:
{
"reasoning": "The second frame introduces an unexpected UI
overlay (the green FPS counter) and a significant composition
change (a standing character’s legs obstructing the view)
compared to the first image. These constitute unacceptable
differences.",
"test_pass":false
}
Gemini-2.5-Pro’soutput:
{
"reasoning":"The core scene composition, background environment
, and character presence remain consistent. The primary
difference is the clothing worn by the character on the left,
which falls under the acceptable category of character
customization. Minor variations in character position and
lighting are also within acceptable limits.",
"test_pass":true
}
FigureA42: Samplevisualregressiontestthattop-performingmodelslikeGPT-4o,GPT-4.1,and
Gemini-2.5-Profail,buto4-minianswerscorrectly.
53

G.13 AdditionalResultsfortheBugReportGenerationTask
GPT-4o’soutput:
{
| "reasoning": | "The | weapon | model | appears | to be missing | a part of |
| ------------ | ---- | ------ | ----- | ------- | ------------- | --------- |
its barrel, which is not consistent with the expected design of
the MP 3008. This could be due to a rendering issue or a missing
texture.",
| "bug_report_title":       |     | "MP | 3008 | Weapon  | Model Incomplete", |                 |
| ------------------------- | --- | --- | ---- | ------- | ------------------ | --------------- |
| "bug_report_description": |     |     |      | "The MP | 3008 weapon        | model displayed |
in the inventory screen is missing a section of its barrel. This
visual glitch may confuse players about the weapon’s appearance
| and could        | affect | immersion. |        | ",  |     |     |
| ---------------- | ------ | ---------- | ------ | --- | --- | --- |
| "affected_item": |        | "Weapon    | Model" |     |     |     |
}
Judge’s(o3)output:
{
| "reasoning": | "Ground | truth |     | bug is | about two weapons | visually |
| ------------ | ------- | ----- | --- | ------ | ----------------- | -------- |
clipping into each other (overlap). Generated report concerns a
| single weapon | model | (MP | 3008) | missing | part of its | barrel, no |
| ------------- | ----- | --- | ----- | ------- | ----------- | ---------- |
mention of clipping with another weapon. The core issues differ
.",
| "match": | false |     |     |     |     |     |
| -------- | ----- | --- | --- | --- | --- | --- |
}
FigureA43: Asamplemodelresponsefortheimage-basedbugreportgenerationtask,alongwith
thejudge’sevaluation. Themodelprovidesaninaccuratedescriptionoftheglitch,andthejudge
correctlyrejectsit.
54

GPT-4o’soutput:
{
"reasoning": "The image shows a vehicle with a character inside
, but the character appears to be clipping through the vehicle’s
windshield. This suggests a rendering issue where the character
model is not properly constrained within the vehicle model.",
"bug_report_title": "Character Clipping Through Vehicle
Windshield",
"bug_report_description": "A character inside a vehicle is
visibly clipping through the windshield. This graphical glitch
disrupts the visual realism and may affect gameplay by causing
confusion about the character’s position and interactions with
the environment. ",
"affected_item": "Character and Vehicle"
}
Judge’s(o3)output:
{
"reasoning": "Ground truth issue concerns the car model
intersecting with the ground, i.e., the vehicle itself is
partially submerged/clipping into terrain. The generated report
instead describes a character model intersecting with the
vehicle’s windshield. The objects involved (car vs. character)
and the intersection context (ground vs. windshield) do not
align, so they are different bugs.",
"match": false
}
FigureA44: Asamplemodelresponsefortheimage-basedbugreportgenerationtask,alongwith
thejudge’sevaluation. Themodelprovidesaninaccuratedescriptionoftheglitch,andthejudge
correctlyrejectsit.
55

Gemini-2.5-Pro’soutput:
{
"reasoning": "The character model’s left shoulder and arm are
intersecting with the wooden wall geometry behind them. This
indicates a clipping issue where the character model is
positioned incorrectly relative to the environment’s collision
boundaries.",
"bug_report_title": "Character Model Clipping Through Wall",
"bug_report_description": "The NPC standing behind the
workbench has their left shoulder and arm partially embedded
within the wooden wall texture behind them. This is a visual
clipping error.",
"affected_item": "Character Model (NPC)"
}
Judge’s(o3)output:
{
"reasoning": "Ground truth: character is clipping into the wall
. Generated report: NPC character model’s shoulder and arm are
embedded in wall (visual clipping error). Both describe same
issue: character clipping with wall geometry. Details (NPC,
workbench) do not contradict core issue.",
"match": true
}
FigureA45: Asamplemodelresponsefortheimage-basedbugreportgenerationtask,alongwiththe
judge’sevaluation. Themodelprovidesadescriptionthatmatchesourgroundtruth,andthejudge
correctlyacceptsit.
56

Gemini-2.5-Pro’soutput:
{
"reasoning": "The character on the right, riding a horse, is
displayed in a static ’A-pose’ or ’T-pose’ with arms
outstretched horizontally. This is not a natural pose for riding
a horse and indicates an animation or character model rigging
glitch. ",
"bug_report_title": "Character Stuck in A-Pose/T-Pose While
Riding Horse",
"bug_report_description": "A character model (potentially an
NPC or another player) is observed riding a horse but is stuck
in a default A-pose or T-pose animation state. Their arms are
extended straight out to the sides instead of holding reins or
resting naturally. This is a visual bug affecting character
animation.",
"affected_item": "Character Model/Animation "
}
Judge’s(o3)output:
{
"reasoning": "Both descriptions talk about a rider-character
who is on a horse but is frozen in the default T-/A-pose instead
of playing the correct riding animation. The ground truth
additionally notes that the lower half of the character’s body
is clipping/merging into the horse, but this is a consequence of
the same faulty pose state; the generated report simply omits
that extra detail. The central bug---character stuck in T-pose
while mounted---is the same in both descriptions.",
"match": true
}
FigureA46: Asamplemodelresponsefortheimage-basedbugreportgenerationtask,alongwiththe
judge’sevaluation. Themodelprovidesadescriptionthatmatchesourgroundtruth,andthejudge
correctlyacceptsit.
57

G.14 ObservationAbouttheJudgeintheBugReportGenerationTask
Gemini-2.5-Pro’soutput:
{
"reasoning": "The character standing behind the player
character ’Haz-man’ is rendered as a solid black silhouette,
lacking textures and appropriate lighting for the environment.
This suggests a graphical glitch related to texture loading or
shader application.",
"bug_report_title": "Character Model Renders as Solid Black
Silhouette",
"bug_report_description": "A character model positioned behind
the player character ’Haz-man’ is displayed as a completely
black, untextured silhouette. The lighting present in the room
does not affect this character model, unlike the player
character and the surrounding environment which are correctly
lit and textured. This appears to be a rendering bug. ",
"affected_item": "Character Model"
}
Judge’s(o3)output:
{
"reasoning": "Ground truth bug concerns the rendered SHADOW of
a character: part of the shadow (specifically the face area) is
transparent, letting the background show through. Expected
shadow should be opaque. Generated report concerns an entirely
different symptom: a whole character model itself appears as a
solid black, unlit silhouette (overly opaque), not about
transparency in a shadow. It addresses lighting on the model,
not shadow transparency. Therefore the two reports describe
different issues.",
"match": false
}
FigureA47: Samplemodelresponsefortheimage-basedbugreportgenerationtaskalongwiththe
judge’sevaluation. Whilecertainglitchesarechallengingtodescribeprecisely,themodelcorrectly
identifiesandhighlightstherelevantaspectsandregionsintheimage. However,thejudgestrictly
evaluatesthewording,entirelyrejectingtheresponsedespitethemodelcorrectlypinpointingthe
problematicregions.
58

Gemini-2.5-Pro’soutput:
{
"reasoning": "The video shows the pre-race vehicle selection
screen. The player’s chosen vehicle, a Karin Sultan RS, is
displayed precariously balanced on top of a large wind turbine
blade. This is an highly unusual and physically improbable
location for a vehicle preview, suggesting a glitch in how the
game stages the vehicle for this specific race menu.",
"bug_report_title": "Vehicle Preview Incorrectly Positioned on
Wind Turbine Blade in Pre-Race Menu",
"bug_report_description": "In the pre-race setup menu for the ’
Wallrider (Turbines) XB1’ race, the vehicle selected by the
player is shown positioned on top of a wind turbine blade in the
background environment instead of a standard display area. This
appears to be a staging error for the vehicle preview,
potentially specific to this custom race or location.",
"affected_item": "Vehicle Preview / UI Staging"
}
Judge’s(o3)output:
{
"reasoning": "Ground truth describes an in-game physics/
clipping issue: during gameplay the car becomes physically stuck
inside a wind-turbine blade, with its body intersecting the
geometry. Generated report describes a UI/preview staging issue
that occurs in the pre-race menu: the vehicle model is merely
rendered on top of a wind turbine blade background instead of
the normal display area. It is about an incorrect camera/
placement in the menu, not about gameplay collision or clipping.
Because they concern different contexts (menu preview vs.
gameplay), different symptoms (visual staging vs. physical
clipping), and likely different root causes, they do not refer
to the same underlying bug.",
"match": false
}
FigureA48: Samplemodelresponsefortheimage-basedbugreportgenerationtaskalongwiththe
judge’sevaluation. Whilethemodel’sgeneratedreportisaccurate,thejudgeincorrectlyrejectsitfor
beingtoostrictaboutsmalldetailsandwordingthatarecorrectbutmissingfromthegroundtruth.
59

VideoGameQA-BenchSamples
H
H.1 VisualUnitTests
Basedontheimage,answerthefollowingquestions:
1.Whatisthecharacter’sposture?
2.Isthecharacterfacingtowardsorawayfromthecamera?
3.Istheredebris(likeleaves)visibleonthewalkway?
4.Whatobjectisimmediatelyinfrontofthecharacter,borderingtheedge?
5.Istherealargemetalgatevisibleontheleftsideofthescene?
6.Whattimeofdayisdepicted?
7.Isacityscapewithlitbuildingsvisibleinthebackground?
8.Whatistheconditionofthemetalgateontheleft?
ProvideyouranswerinthefollowingJSONformat:
{
| "character_posture": | "",           | // options: | ["standing", | "walking", | "   |
| -------------------- | ------------- | ----------- | ------------ | ---------- | --- |
| sitting",            | "crouching"], |             |              |            |     |
"character_facing_direction": "", // options: ["towards", "away
"],
| "debris_on_walkway": | false, | // options: | [true, | false], |     |
| -------------------- | ------ | ----------- | ------ | ------- | --- |
"object_in_front_of_character": "", // options: ["railing", "wall
| ", "open space",         | "door"], |                  |             |                |     |
| ------------------------ | -------- | ---------------- | ----------- | -------------- | --- |
| "gate_visible_left":     | false,   | // options:      | [true,      | false],        |     |
| "time_of_day":           | "", //   | options: ["day", | "night",    | "dawn/dusk"],  |     |
| "lit_cityscape_visible": |          | false,           | // options: | [true, false], |     |
"left_gate_condition": "" // options: ["new", "rusty/weathered",
"broken"]
}
FigureA49: Sampletestfromavisualunittest,wherethemodelisaskedtosummarizesomevisual
propertiesintoaJSONstructure.
60

Basedontheimageanswerthefollowingquestions:
1.Howmanybirdsarevisibleinsidetheroom(includinginsidethecage)?
2.Howmanybirdsarevisibleoutsidethewindow?
3.Isthebirdcagedooropen?
4.Whatistheprimarycolorofthebirdinsidethecage?
5.Isthereapieceofwoodleaningontheinsidewindowsill?
6.Whatisthemaincoloroftheblossomsseenoutsidethewindow?
7.Isthewallpaperontheleftwallpatterned?
8.Whereisthegreybirdpositioned?
ProvideyouranswerinthefollowingJSONformat
{
| "birds_inside_count":  |     | 0 //  | Integer    | count, |        |     |
| ---------------------- | --- | ----- | ---------- | ------ | ------ | --- |
| "birds_outside_count": |     | 0     | // Integer | count, |        |     |
| "birdcage_door_open":  |     | false | // true    | or     | false, |     |
"bird_in_cage_color": "" // options: ["yellow", "grey", "blue", "
brown"],
| "wood_on_sill_present": |     | false | //  | true or | false, |     |
| ----------------------- | --- | ----- | --- | ------- | ------ | --- |
"blossom_color": "" // options: ["pink", "white", "yellow", "red
"],
| "left_wallpaper_patterned": |          |          | false       | // true     | or false, |     |
| --------------------------- | -------- | -------- | ----------- | ----------- | --------- | --- |
| "grey_bird_location":       |          | ""       | // options: | ["inside    | cage",    | "on |
| windowsill",                | "outside | window", |             | "on floor"] |           |     |
}
FigureA50: Sampletestfromavisualunittest,wherethemodelisaskedtosummarizesomevisual
propertiesintoaJSONstructure.
61

Basedontheimageanswerthefollowingquestions:
1.Whatistheprimarycoloroftherallycar?
2.Isthedriver-sidedoorofthecaropenorclosed?
3.Whatnumberisdisplayedinlargefontonthecar’sdoor?
4.Whatbrandnameisvisibleontheyellowdecalabovethe’elf’logoonthecar’sside?
5.Isthereacoiledorangeairhosehangingfromtheceilingontheleftside?
6.Whattypeofpatternisonthefloordirectlybeneaththecar?
7.Isthereascreenormonitormountedonthewalldisplayinggraphs?
ProvideyouranswerinthefollowingJSONformat
{
"car_primary_color": "" // options: ["light blue", "dark blue", "
| white", "red",       | "black"], |                |        |                     |
| -------------------- | --------- | -------------- | ------ | ------------------- |
| "driver_door_state": |           | "" // options: |        | ["open", "closed"], |
| "car_door_number":   | 0         | // Integer     | value, |                     |
"yellow_decal_brand": "" // String value representing the text,
| "coiled_hose_visible": |     | false | // true | or false, |
| ---------------------- | --- | ----- | ------- | --------- |
"floor_pattern": "" // options: ["plain", "checkered", "tiled", "
textured_metal"],
| "wall_monitor_visible": |     | false | // true | or false |
| ----------------------- | --- | ----- | ------- | -------- |
}
FigureA51: Sampletestfromavisualunittest,wherethemodelisaskedtosummarizesomevisual
propertiesintoaJSONstructure.
62

H.2 UIUnitTests
ReadthedashboardandfilltheJSONvaluesbelow:
{
"tire_pressure": {
"front_left": 0,
"front_right": 0,
"rear_left": 0,
"rear_right": 0
},
"brake_temps": {
"front_left": 0,
"front_right": 0,
"rear_left": 0,
"rear_right": 0
},
"break_bias": 0,
"break_sl": 0,
"settings": {
"map": 0,
"mix": 0,
"tc1": 0,
"tc2": 0
},
"gear": 0,
"rpm": 0,
"speed_mph": 0
}
FigureA52: SampleUIunittest,wherethemodelisaskedtoextractandsummarizevisualinforma-
tionfromgameUIelementsintoaJSONstructure.
63

Pleaseprovidethevaluesofthediceinthetopmostrowfromlefttoright,andreturnthemasaJSON
list.
FigureA53: SampleUIunittest,wherethemodelisaskedtoextractandsummarizevisualinforma-
tionfromgameUIelementsintoaJSONstructure.
Basedontheimage,extractthelistofweapons(singleword)andreturnitinthefollowingJSON
format:
{ "items": ["weapon"] }
FigureA54: SampleUIunittest,wherethemodelisaskedtoextractandsummarizevisualinforma-
tionfromgameUIelementsintoaJSONstructure.
64

H.3 VisualRegressionTests
Youareanimagecomparisontoolforvideogamequalityassurance.Giventwoscreenshotsfromthe
samegamescene,evaluatewhetherthesecondimagerepresentsanacceptablevariationofthefirst
(reference)image.
ConsiderthesevariationsACCEPTABLE:
-Playercharactercustomizationelements
-Environmentalconditions(weather,day/nightcycle)
-Slightpositionaloranimationdifferences
-Lightingandshadowadjustments
-Minorvariationsinnon-criticalbackgroundelements
ConsiderthesevariationsUNACCEPTABLE:
-Interfacecorruptionorelementmisalignment
-Textualcontentchanges(unlessexpected,e.g.,dynamictext)
-Significantvisualartifactsorrenderingerrors(e.g.,missingtextures,z-fighting)
-Majorstructuralchangestoscenegeometrynotattributabletogameplaystate
-Missingorgrosslyincorrectkeysceneelementscomparedtothereference
ProvideyourassessmentasJSON:
{
"reasoning": "Concise explanation of detected differences and
justification for your decision based on the criteria.",
"test_pass": true/false
}
Where‘test_pass’istrueifthedifferencesareacceptableandfalseifunacceptabledifferencesare
detected.
FigureA55: Sampletestfromavisualregressiontask,wherethemodelisaskedtocomparetwo
versionsofthesamescenetoverifywhetherthechangesareacceptableorunacceptable.
65

Youareanimagecomparisontoolforvideogamequalityassurance.Giventwoscreenshotsfromthe
samegamescene,evaluatewhetherthesecondimagerepresentsanacceptablevariationofthefirst
(reference)image.
ConsiderthesevariationsACCEPTABLE:
-Playercharactercustomizationelements
-Environmentalconditions(weather,day/nightcycle)
-Slightpositionaloranimationdifferences
-Lightingandshadowadjustments
-Minorvariationsinnon-criticalbackgroundelements
ConsiderthesevariationsUNACCEPTABLE:
-Interfacecorruptionorelementmisalignment
-Textualcontentchanges(unlessexpected,e.g.,dynamictext)
-Significantvisualartifactsorrenderingerrors(e.g.,missingtextures,z-fighting)
-Majorstructuralchangestoscenegeometrynotattributabletogameplaystate
-Missingorgrosslyincorrectkeysceneelementscomparedtothereference
ProvideyourassessmentasJSON:
{
"reasoning": "Concise explanation of detected differences and
justification for your decision based on the criteria.",
"test_pass": true/false
}
Where‘test_pass’istrueifthedifferencesareacceptableandfalseifunacceptabledifferencesare
detected.
FigureA56: Sampletestfromavisualregressiontask,wherethemodelisaskedtocomparetwo
versionsofthesamescenetoverifywhetherthechangesareacceptableorunacceptable.
66

Youareanimagecomparisontoolforvideogamequalityassurance.Giventwoscreenshotsfromthe
samegamescene,evaluatewhetherthesecondimagerepresentsanacceptablevariationofthefirst
(reference)image.
ConsiderthesevariationsACCEPTABLE:
-Playercharactercustomizationelements
-Environmentalconditions(weather,day/nightcycle)
-Slightpositionaloranimationdifferences
-Lightingandshadowadjustments
-Minorvariationsinnon-criticalbackgroundelements
ConsiderthesevariationsUNACCEPTABLE:
-Interfacecorruptionorelementmisalignment
-Textualcontentchanges(unlessexpected,e.g.,dynamictext)
-Significantvisualartifactsorrenderingerrors(e.g.,missingtextures,z-fighting)
-Majorstructuralchangestoscenegeometrynotattributabletogameplaystate
-Missingorgrosslyincorrectkeysceneelementscomparedtothereference
ProvideyourassessmentasJSON:
{
"reasoning": "Concise explanation of detected differences and
justification for your decision based on the criteria.",
"test_pass": true/false
}
Where‘test_pass’istrueifthedifferencesareacceptableandfalseifunacceptabledifferencesare
detected.
FigureA57: Sampletestfromavisualregressiontask,wherethemodelisaskedtocomparetwo
versionsofthesamescenetoverifywhetherthechangesareacceptableorunacceptable.
67

H.4 Image-basedGlitchDetection
Youareahelpfulassistantanalyzingvideogameimagesandscreenshotsforglitches.Youwillbegiven
ascreenshotfromavideogame,andyourjobistoanalyzethescreenshotanddeterminewhetherit
containsaglitch.
Provideyouranswerinthefollowingformat:
{
| "reasoning": | "Brief explanation | of why you | think a glitch | is  |
| ------------ | ------------------ | ---------- | -------------- | --- |
present",
| "glitch_detected": | true or false, |     |     |     |
| ------------------ | -------------- | --- | --- | --- |
"description_of_glitch": "Description of the glitch if detected
| else empty | string" |     |     |     |
| ---------- | ------- | --- | --- | --- |
}
| FigureA58: | Samplefortheimage-basedglitchdetectiontask. |     |     |     |
| ---------- | ------------------------------------------- | --- | --- | --- |
68

Youareahelpfulassistantanalyzingvideogameimagesandscreenshotsforglitches.Youwillbegiven
ascreenshotfromavideogame,andyourjobistoanalyzethescreenshotanddeterminewhetherit
containsaglitch.
Provideyouranswerinthefollowingformat:
{
| "reasoning": | "Brief explanation | of why you | think a glitch | is  |
| ------------ | ------------------ | ---------- | -------------- | --- |
present",
| "glitch_detected": | true or false, |     |     |     |
| ------------------ | -------------- | --- | --- | --- |
"description_of_glitch": "Description of the glitch if detected
| else empty | string" |     |     |     |
| ---------- | ------- | --- | --- | --- |
}
| FigureA59: | Samplefortheimage-basedglitchdetectiontask. |     |     |     |
| ---------- | ------------------------------------------- | --- | --- | --- |
69

Youareahelpfulassistantanalyzingvideogameimagesandscreenshotsforglitches.Youwillbegiven
ascreenshotfromavideogame,andyourjobistoanalyzethescreenshotanddeterminewhetherit
containsaglitch.
Provideyouranswerinthefollowingformat:
{
| "reasoning": | "Brief explanation | of why you | think a glitch | is  |
| ------------ | ------------------ | ---------- | -------------- | --- |
present",
| "glitch_detected": | true or false, |     |     |     |
| ------------------ | -------------- | --- | --- | --- |
"description_of_glitch": "Description of the glitch if detected
| else empty | string" |     |     |     |
| ---------- | ------- | --- | --- | --- |
}
| FigureA60: | Samplefortheimage-basedglitchdetectiontask. |     |     |     |
| ---------- | ------------------------------------------- | --- | --- | --- |
70

H.5 ParametricClippingDetectionTests
Youareavisualanalysisassistantspecializingindetectingobjectclippinginvideogamescreenshots.
Yourtaskistoexamineeachprovidedimageanddeterminewhetheranypartofthewhitecubeis
intersectingwiththecharactermodel,indicatingaclippingissue.
Basedonyouranalysis,respondusingthefollowingformat:
{
| "reasoning":         | "Brief explanation | of why you | think clipping | is  |
| -------------------- | ------------------ | ---------- | -------------- | --- |
| present or           | not",              |            |                |     |
| "clipping_detected": | true or            | false      |                |     |
}
FigureA61:Sampletestfromaparametricclippingdetectiontask,wherethemodelisaskedtodetect
clippingglitcheswhenanobjectisplacedatvariousdistancesfromahumancharacter, toverify
whetherthemodelcanrobustlydetectsuchglitches.
71

Youareavisualanalysisassistantspecializingindetectingobjectclippinginvideogamescreenshots.
Yourtaskistoexamineeachprovidedimageanddeterminewhetheranypartofthewhitecubeis
intersectingwiththecharactermodel,indicatingaclippingissue.
Basedonyouranalysis,respondusingthefollowingformat:
{
| "reasoning":         | "Brief explanation | of why you | think clipping | is  |
| -------------------- | ------------------ | ---------- | -------------- | --- |
| present or           | not",              |            |                |     |
| "clipping_detected": | true or            | false      |                |     |
}
FigureA62:Sampletestfromaparametricclippingdetectiontask,wherethemodelisaskedtodetect
clippingglitcheswhenanobjectisplacedatvariousdistancesfromahumancharacter, toverify
whetherthemodelcanrobustlydetectsuchglitches.
72

H.6 Image-basedBugReportGeneration
Youareavideogamequalityassuranceassistantwhoanalyzesscreenshotstoidentifyanddocument
visualglitches.Whenpresentedwithanimage,carefullyexamineitforanygraphicalbugsorrendering
issues.
ProvideyouranalysisinthefollowingJSONformat:
{
| "reasoning":        | "Brief explanation | of             | what you observe  | and why it |
| ------------------- | ------------------ | -------------- | ----------------- | ---------- |
| appears to          | be a glitch",      |                |                   |            |
| "bug_report_title": | "A                 | clear, concise | title summarizing | the        |
issue",
| "bug_report_description": |     | "Detailed | description | of the visual |
| ------------------------- | --- | --------- | ----------- | ------------- |
bug, including its appearance and potential impact on gameplay",
"affected_item": "The specific game element (character, object,
| environment, | UI) affected | by the | glitch" |     |
| ------------ | ------------ | ------ | ------- | --- |
}
| FigureA63: | Samplefortheimage-basedbugreportgenerationtask. |     |     |     |
| ---------- | ----------------------------------------------- | --- | --- | --- |
73

Youareavideogamequalityassuranceassistantwhoanalyzesscreenshotstoidentifyanddocument
visualglitches.Whenpresentedwithanimage,carefullyexamineitforanygraphicalbugsorrendering
issues.
ProvideyouranalysisinthefollowingJSONformat:
{
| "reasoning":        | "Brief explanation | of             | what you observe  | and why it |
| ------------------- | ------------------ | -------------- | ----------------- | ---------- |
| appears to          | be a glitch",      |                |                   |            |
| "bug_report_title": | "A                 | clear, concise | title summarizing | the        |
issue",
| "bug_report_description": |     | "Detailed | description | of the visual |
| ------------------------- | --- | --------- | ----------- | ------------- |
bug, including its appearance and potential impact on gameplay",
"affected_item": "The specific game element (character, object,
| environment, | UI) affected | by the | glitch" |     |
| ------------ | ------------ | ------ | ------- | --- |
}
| FigureA64: | Samplefortheimage-basedbugreportgenerationtask. |     |     |     |
| ---------- | ----------------------------------------------- | --- | --- | --- |
74

Youareavideogamequalityassuranceassistantwhoanalyzesscreenshotstoidentifyanddocument
visualglitches.Whenpresentedwithanimage,carefullyexamineitforanygraphicalbugsorrendering
issues.
ProvideyouranalysisinthefollowingJSONformat:
{
| "reasoning":        | "Brief explanation | of             | what you observe  | and why it |
| ------------------- | ------------------ | -------------- | ----------------- | ---------- |
| appears to          | be a glitch",      |                |                   |            |
| "bug_report_title": | "A                 | clear, concise | title summarizing | the        |
issue",
| "bug_report_description": |     | "Detailed | description | of the visual |
| ------------------------- | --- | --------- | ----------- | ------------- |
bug, including its appearance and potential impact on gameplay",
"affected_item": "The specific game element (character, object,
| environment, | UI) affected | by the | glitch" |     |
| ------------ | ------------ | ------ | ------- | --- |
}
| FigureA65: | Samplefortheimage-basedbugreportgenerationtask. |     |     |     |
| ---------- | ----------------------------------------------- | --- | --- | --- |
75

H.7 Video-basedGlitchDetection
Youareahelpfulassistantanalyzingvideogameclipsforglitches.Youwillbegivenashortvideoclip
fromavideogame,andyourtaskistoanalyzethevideoanddeterminewhetheritcontainsaglitch.
Provideyouranswerinthefollowingformat:
{
| "reasoning": | "Brief explanation | of why you | think a glitch | is  |
| ------------ | ------------------ | ---------- | -------------- | --- |
present",
| "glitch_detected": | true or false, |     |     |     |
| ------------------ | -------------- | --- | --- | --- |
"description_of_glitch": "Description of the glitch if detected
| else empty | string" |     |     |     |
| ---------- | ------- | --- | --- | --- |
}
FigureA66: Sampleforthevideo-basedglitchdetectiontask. Inthisvideo(only6sampleframes
areshown),ahorseismovingupanddown,whichisaglitch.
76

Youareahelpfulassistantanalyzingvideogameclipsforglitches.Youwillbegivenashortvideoclip
fromavideogame,andyourtaskistoanalyzethevideoanddeterminewhetheritcontainsaglitch.
Provideyouranswerinthefollowingformat:
{
| "reasoning": | "Brief explanation | of why you | think a glitch | is  |
| ------------ | ------------------ | ---------- | -------------- | --- |
present",
| "glitch_detected": | true or false, |     |     |     |
| ------------------ | -------------- | --- | --- | --- |
"description_of_glitch": "Description of the glitch if detected
| else empty | string" |     |     |     |
| ---------- | ------- | --- | --- | --- |
}
FigureA67:Sampleforthevideo-basedglitchdetectiontask. Inthisvideo(only6framesareshown),
thenon-playercharacterisperforminganaction,buttheanimationandtablearemisaligned.
77

Youareahelpfulassistantanalyzingvideogameclipsforglitches.Youwillbegivenashortvideoclip
fromavideogame,andyourtaskistoanalyzethevideoanddeterminewhetheritcontainsaglitch.
Provideyouranswerinthefollowingformat:
{
| "reasoning": | "Brief explanation | of why you | think a glitch | is  |
| ------------ | ------------------ | ---------- | -------------- | --- |
present",
| "glitch_detected": | true or false, |     |     |     |
| ------------------ | -------------- | --- | --- | --- |
"description_of_glitch": "Description of the glitch if detected
| else empty | string" |     |     |     |
| ---------- | ------- | --- | --- | --- |
}
FigureA68:Sampleforthevideo-basedglitchdetectiontask. Inthisvideo(only6framesareshown),
the objects in the water are shaking violently, which is caused by a glitch in the physics engine
simulation.
78

H.8 NeedleInAHaystack
You are a specialized video game quality assurance analyst trained to detect visual anomalies in
gameplayfootage.Yourtaskistoanalyzetheprovidedvideocliptoidentifyanybugs,glitches,visual
artifacts,orunexpectedbehaviors.
WhattoLookFor
Examinethevideocarefullyforany:
-Visualartifacts(textureissues,flickering,clipping)
-Animationproblems(jerkymovements,T-poses)
-Renderingglitches(missingtextures,lightingerrors)
-Gameplayanomalies(collisionfailures,objectteleportation)
ResponseFormat
Afteryourthoroughanalysis,provideyourfindingsinthisexactJSONformat:
{
"reasoning": "Brief explanation of what you observed in the video
and why it appears to be a glitch",
"glitch_detected": true|false,
"timestamp": 0
}
FigureA69: Samplefromtheneedle-in-a-haystacktask. Pleasenotethatonly6outof50framesare
showntohighlighttheglitch.
79

You are a specialized video game quality assurance analyst trained to detect visual anomalies in
gameplayfootage.Yourtaskistoanalyzetheprovidedvideocliptoidentifyanybugs,glitches,visual
artifacts,orunexpectedbehaviors.
WhattoLookFor
Examinethevideocarefullyforany:
-Visualartifacts(textureissues,flickering,clipping)
-Animationproblems(jerkymovements,T-poses)
-Renderingglitches(missingtextures,lightingerrors)
-Gameplayanomalies(collisionfailures,objectteleportation)
ResponseFormat
Afteryourthoroughanalysis,provideyourfindingsinthisexactJSONformat:
{
"reasoning": "Brief explanation of what you observed in the video
and why it appears to be a glitch",
"glitch_detected": true|false,
"timestamp": 0
}
FigureA70: Samplefromtheneedle-in-a-haystacktask. Pleasenotethatonly6outof50framesare
showntohighlighttheglitch.
80

You are a specialized video game quality assurance analyst trained to detect visual anomalies in
gameplayfootage.Yourtaskistoanalyzetheprovidedvideocliptoidentifyanybugs,glitches,visual
artifacts,orunexpectedbehaviors.
WhattoLookFor
Examinethevideocarefullyforany:
-Visualartifacts(textureissues,flickering,clipping)
-Animationproblems(jerkymovements,T-poses)
-Renderingglitches(missingtextures,lightingerrors)
-Gameplayanomalies(collisionfailures,objectteleportation)
ResponseFormat
Afteryourthoroughanalysis,provideyourfindingsinthisexactJSONformat:
{
"reasoning": "Brief explanation of what you observed in the video
and why it appears to be a glitch",
"glitch_detected": true|false,
"timestamp": 0
}
FigureA71: Samplefromtheneedle-in-a-haystacktask. Pleasenotethatonly6outof50framesare
showntohighlighttheglitch.
81

You are a specialized video game quality assurance analyst trained to detect visual anomalies in
gameplayfootage.Yourtaskistoanalyzetheprovidedvideocliptoidentifyanybugs,glitches,visual
artifacts,orunexpectedbehaviors.
WhattoLookFor
Examinethevideocarefullyforany:
-Visualartifacts(textureissues,flickering,clipping)
-Animationproblems(jerkymovements,T-poses)
-Renderingglitches(missingtextures,lightingerrors)
-Gameplayanomalies(collisionfailures,objectteleportation)
ResponseFormat
Afteryourthoroughanalysis,provideyourfindingsinthisexactJSONformat:
{
"reasoning": "Brief explanation of what you observed in the video
and why it appears to be a glitch",
"glitch_detected": true|false,
"timestamp": 0
}
FigureA72: Samplefromtheneedle-in-a-haystacktask. Pleasenotethatonly6outof50framesare
showntohighlighttheglitch.
82

H.9 Video-basedBugReportGeneration
Youareavideogamequalityassuranceassistantwhoanalyzesvideoclipstoidentifyanddocument
visualglitchesorstrangebehaviors. Whenpresentedwithavideoclip,carefullyexamineitforany
graphicalbugs,renderingissues,physicsanomalies,orunexpectedevents.
ProvideyouranalysisinthefollowingJSONformat:
{
| "reasoning":        | "Brief | explanation |        | of      | what you  | observe     | in the |
| ------------------- | ------ | ----------- | ------ | ------- | --------- | ----------- | ------ |
| video and           | why it | appears     | to     | be a    | glitch or | bug",       |        |
| "bug_report_title": |        | "A          | clear, | concise | title     | summarizing | the    |
issue",
| "bug_report_description": |            |               | "Detailed |           | description |            | of the visual |
| ------------------------- | ---------- | ------------- | --------- | --------- | ----------- | ---------- | ------------- |
| bug or                    | behavioral | anomaly,      |           | including | its         | appearance | and           |
| potential                 | impact     | on gameplay", |           |           |             |            |               |
"affected_item": "The specific game element (character, object,
| environment, | UI, | physics) |     | affected | by the | glitch" |     |
| ------------ | --- | -------- | --- | -------- | ------ | ------- | --- |
}
FigureA73: Sampleforthevideo-basedbugreportgenerationtask. Inthisvideo(only6framesare
shown),ahelicopteremergesfromtheground.
83

Youareavideogamequalityassuranceassistantwhoanalyzesvideoclipstoidentifyanddocument
visualglitchesorstrangebehaviors. Whenpresentedwithavideoclip,carefullyexamineitforany
graphicalbugs,renderingissues,physicsanomalies,orunexpectedevents.
ProvideyouranalysisinthefollowingJSONformat:
{
| "reasoning":        | "Brief | explanation |        | of      | what you  | observe     | in the |
| ------------------- | ------ | ----------- | ------ | ------- | --------- | ----------- | ------ |
| video and           | why it | appears     | to     | be a    | glitch or | bug",       |        |
| "bug_report_title": |        | "A          | clear, | concise | title     | summarizing | the    |
issue",
| "bug_report_description": |            |               | "Detailed |           | description |            | of the visual |
| ------------------------- | ---------- | ------------- | --------- | --------- | ----------- | ---------- | ------------- |
| bug or                    | behavioral | anomaly,      |           | including | its         | appearance | and           |
| potential                 | impact     | on gameplay", |           |           |             |            |               |
"affected_item": "The specific game element (character, object,
| environment, | UI, | physics) |     | affected | by the | glitch" |     |
| ------------ | --- | -------- | --- | -------- | ------ | ------- | --- |
}
FigureA74: Sampleforthevideo-basedbugreportgenerationtask. Inthisvideo(only6framesare
shown),ahelicopterisstuckunderthebridge.
84

Youareavideogamequalityassuranceassistantwhoanalyzesvideoclipstoidentifyanddocument
visualglitchesorstrangebehaviors. Whenpresentedwithavideoclip,carefullyexamineitforany
graphicalbugs,renderingissues,physicsanomalies,orunexpectedevents.
ProvideyouranalysisinthefollowingJSONformat:
{
| "reasoning":        | "Brief | explanation |        | of      | what you  | observe     | in the |
| ------------------- | ------ | ----------- | ------ | ------- | --------- | ----------- | ------ |
| video and           | why it | appears     | to     | be a    | glitch or | bug",       |        |
| "bug_report_title": |        | "A          | clear, | concise | title     | summarizing | the    |
issue",
| "bug_report_description": |            |               | "Detailed |           | description |            | of the visual |
| ------------------------- | ---------- | ------------- | --------- | --------- | ----------- | ---------- | ------------- |
| bug or                    | behavioral | anomaly,      |           | including | its         | appearance | and           |
| potential                 | impact     | on gameplay", |           |           |             |            |               |
"affected_item": "The specific game element (character, object,
| environment, | UI, | physics) |     | affected | by the | glitch" |     |
| ------------ | --- | -------- | --- | -------- | ------ | ------- | --- |
}
FigureA75: Sampleforthevideo-basedbugreportgenerationtask. Inthisvideo(only6framesare
shown),aplayercharacterisstuckinafallingposition,descendingfromthewaterintotheair.
85

I DatasetLicense
Inthissection,weprovidedetailsaboutthevariousdatasourcesusedtoconstructourdataset,along
withtheirrespectivelicenses.
TableA14: DataSourcesandTheirLicenses
Source License
SteamScreenshots SteamSubscriberAgreement
GamePhysics[45] CC-BY-NC4.0
YouTubeVideos YouTubeStandardLicense
WecreatedseveralimagesusingtheUnitygameenginewithassetspurchasedfromtheUnityAsset
Store.
86