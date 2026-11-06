---
title: "How Far Can VLMs Go for Visual Bug Detection Study"
author: "Lu"
year: "2026"
source_file: "04_benchmarks_and_datasets/Lu_2026_How_Far_Can_VLMs_Go_for_Visual_Bug_Detection_Study.pdf"
source_sha256: "b5665885632d3f22fca95dca46c51df43d305f918e75ef78a4f7c62665feb3f3"
converted_at: "2026-11-06T15:12:43.913318+00:00"
markitdown_version: "0.1.9"
char_count: 33568
---
|          | How Far             | Can VLMs  | Go for             | Visual   | Bug Detection? |                |        |
| -------- | ------------------- | --------- | ------------------ | -------- | -------------- | -------------- | ------ |
| Studying | 19,738              | Keyframes | from               | 41 Hours | of Gameplay    |                | Videos |
|          | WentaoLu            |           | AlexanderSenchenko |          |                | AlanSayle      |        |
|          | wlu4@ualberta.ca    |           | asenchenko@ea.com  |          |                | asayle@ea.com  |        |
|          | UniversityofAlberta |           | ElectronicArts     |          |                | ElectronicArts |        |
Edmonton,Alberta,Canada Vancouver,BritishColumbia,Canada Guildford,Surrey,UnitedKingdom
|     |     | AbramHindle              |     | Cor-PaulBezemer     |     |     |     |
| --- | --- | ------------------------ | --- | ------------------- | --- | --- | --- |
|     |     | abram.hindle@ualberta.ca |     | bezemer@ualberta.ca |     |     |     |
|     |     | UniversityofAlberta      |     | UniversityofAlberta |     |     |     |
6202 raM 42  ]VC.sc[  1v60722.3062:viXra
|          |     | Edmonton,Alberta,Canada |     | Edmonton,Alberta,Canada |     |     |     |
| -------- | --- | ----------------------- | --- | ----------------------- | --- | --- | --- |
| Abstract |     |                         |     | ACMReferenceFormat:     |     |     |     |
WentaoLu,AlexanderSenchenko,AlanSayle,AbramHindle,andCor-Paul
Video-basedqualityassurance(QA)forlong-formgameplayvideo
Bezemer.2026.HowFarCanVLMsGoforVisualBugDetection?Study-
islabor-intensiveanderror-prone,yetvaluableforassessinggame
ing19,738Keyframesfrom41HoursofGameplayVideos.InCompanion
stabilityandvisualcorrectnessoverextendedplaysessions.Vision
Proceedingsofthe34thACMSymposiumontheFoundationsofSoftware
languagemodels(VLMs)promisegeneral-purposevisualreasoning
Engineering(FSE’26),June5–9,2026,Montreal,Canada.ACM,NewYork,
| capabilitiesandthusappearattractivefordetectingvisualbugs |     |     |     | NY,USA,6pages. |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- |
directlyfromvideoframes.RecentbenchmarkssuggestthatVLMs
canachievepromisingresultsindetectingvisualglitchesoncu-
rateddatasets.Buildingonthesefindings,weconductareal-world
studyusingindustrialQAgameplayvideostoevaluatehowwell Bugframedetectedfromagameplayvideo
VLMsperforminpracticalscenarios.Ourstudysampleskeyframes
fromlonggameplayvideosandasksaVLMwhethereachkeyframe
containsabug.Startingfromasingle-promptbaseline,themodel
achievesaprecisionof0.50andanaccuracyof0.72.Wethenex-
aminetwocommonenhancementstrategiesusedtoimproveVLM
performancewithoutfine-tuning:(1)asecondaryjudgemodelthat
re-evaluatesVLMoutputs,and(2)metadata-augmentedprompting
throughtheretrievalofpriorbugreports.Across100videosto-
taling41hoursand19,738keyframes,thesestrategiesprovide
onlymarginalimprovementsoverthesimplebaseline,whilein-
troducingadditionalcomputationalcostandoutputvariance.Our
findingsindicatethatoff-the-shelfVLMsarealreadycapableof
detectingacertainrangeofvisualbugsinQAgameplayvideos,
butfurtherprogresslikelyrequireshybridapproachesthatbetter
| separatetextualandvisualanomalydetection. |     |     |     | Buglabel:True |     |     |     |
| ----------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- |
Imagedescription:Theframeshowsafirst-personviewinthe
CCSConcepts game,aimingupwardtowardsarockycliffface...Importantly,
theshadowcastonthelargerockfaceinthecenteroftheimage
•Softwareanditsengineering→Softwaredefectanalysis.
seemsirregularasitcreatesanunnaturaldarkrectangularpatch
thatdoesn’tconformtothenaturalshapeandtopologyofthe
Keywords
rocks.Thissuggeststheshadowmappingorrenderingmightbe
visualbugdetection,gameplayvideos,vision–languagemodels, glitching,asrealshadowswouldfollowthecontoursoftherock
softwaretesting,qualityassurance moresnuglyratherthanaflyingrectangularshape...
Bugdescription:Theframeshowsaclearlyunnatural,hard-
edgeddarkrectangularpatchontheclifffacethatdoesnotfollow
theunderlyingrockgeometryorlightinggradients;naturalter-
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed rainshadowswouldwrapandsoftenaroundcontours,whereas
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation thisshapelookslikeamisprojectedshadoworfailedshadowmap
| onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe |     |     |     | ... |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org.
FSE’26,Montreal,Canada Figure1:Exampleofadetectedvisualbugframeinagame-
©2026Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM. playvideousinggpt-4.1-mini.

FSE’26,June5–9,2026,Montreal,Canada WentaoLu,AlexanderSenchenko,AlanSayle,AbramHindle,andCor-PaulBezemer
1 Introduction captions[29].Insubsequentresearch,Guglielmietal.focusedon
Largevision–languagemodels(VLMs)haverapidlyimprovedin detectingspecificstutteringbugeventsanddevelopedHASTE[9],
open-endedvisualunderstandingtasks[16,23,27].Theirflexibility whichutilizesimagesimilaritytoidentifystutteringoccurrences.
andlowsetupcostsopenupnewopportunitiesforsoftwarequality Inadditiontocaption-basedmethods,deeplearningtechniques
assurance(QA),suchasautomaticallyanalyzinglonggameplay havebeenemployedtodetectvisualglitchesdirectlyfromren-
videostoidentifyvisualbugsduringautomatedQAtests. deredframes.Lingetal.proposedaneuralnetworkapproachto
Atypicalusecaseinvolveshundredsofhoursofautomatedruns identifyfourtypesofrenderedglitchesinvideogames[14],bytrain-
executedovernighttomonitorforruntimeexceptionsorclientin- ingconvolutionalneuralnetworksonlabeledimagedata.Recent
stability(soaktesting)[2].Inpractice,however,mostofthefootage workbyLietal.[31]exploresvisualbugdetectionusingsuper-
isneverreviewedend-to-endunlessacriticalerrorissuspected.As visedmachinelearningwithahybridco-finetuningapproachthat
aresult,thesevideosformalargebutunderusedsourceofevidence incorporatesbothlabeledandunlabeleddata.Theseapproaches
aboutoverallgamestabilityandvisualquality.Inthisreport,we generallydependondomain-specifictrainingdataandpredefined
presentourexperiencewithre-purposingthisexistingvideocor- bugcategories,whichrestrictstheirabilitytogeneralizeacross
pusforbroaderQAtasks,specifically,fordetectingvisiblein-game diversegamesortodetectpreviouslyunseenvisualanomalies.
anomalies using VLMs. We explore whether VLM analysis can VLM-basedbugdetection.Recentadvancementsinlarge-scale
capturevisualbugsfromtheserecordingswithoutanyadditional vision–languagemodels(VLMs)haveopenednewdirectionsfor
modeltraining.Althoughtrainingdatacanbeavailable,ourgoal visualbugdetection.Comparedtotraditionalapproaches,VLM-
istoevaluatetheout-of-the-boxeffectivenessofgeneral-purpose basedmethodsreducetheneedforexplicitMLtrainingandmanual
VLMsasplug-and-playcomponentsinanindustrialQAworkflow. annotation,makingthemsuitableforavarietyofvisualbugdetec-
Meanwhile,avoidingfine-tuningalsoreflectspracticaldeployment tiontasks.ModelssuchasGPT-4odemonstratestrongzero-shot
needswheregamebuildschangefrequently,andmaintainingup- understandingofcomplexscenesandcanidentifyvisualinconsis-
to-dateVLMknowledgethroughcontinuousretrainingwouldbe tenciesdirectlyfromrawimagesorvideoframes[23].Earlywork
costlyandoperationallyunsustainableinthelongrun,especially byTaesirietal.[28]demonstratedtheeffectivenessofusingthe
whennewermodelgenerationswillinevitablyreplaceolderones. ContrastiveLanguage–ImagePre-Training(CLIP)modeltoidentify
Wethereforeaskasimplequestion:HoweffectivelycanVLMs gamevideoscontainingbugsthroughtextqueries,andlanguage
analyzelargevolumesofgameplayvideotodetectvisual modelsaregoodasazero-shotbugdetector.Theylaterintroduced
bugs,andtowhatextentdoRetrieval-AugmentedGeneration VideoGameBunny[25],amodelfine-tunedonextensivevideogame
(RAG)orjudge-basedstrategiesimprovetheirperformance? image datasets and associated instruction pairs, demonstrating
Westudythisempiricallythroughacasestudyof100gameplay animprovedunderstandingofthegamecontextandbeingmore
videos(41hourswithatotalofof4,336,132frames). accuratein-gameresponses.Theirsubsequentstudiesintroduced
OurstudydemonstratesthatmodernVLMscanturnpreviously GlitchBench[26]andVideoGameQA-Bench[27],whichestablished
underusedgameplayrecordingsintoapracticalsourceofQAevi- benchmarksforevaluatingVLMsonarangeofgamequalityassur-
denceandshowthatasimplepromptingsetupenablesautomated ancetasks.Thesebenchmarksdemonstratedstrongperformance
triageoflong-formQAvideos.Thisapproachreducestheamount inidentifyingvisualglitches,particularlyinneedle-in-a-haystack
ofvideorequiringmanualinspectionfrommillionsofrawframes tasksthatrequirelocatingbuginstanceswithingameplayvideos.
toonlyafewthousandcandidateframesselectedbyVLMs. Buildingonthislineofresearch,ourpreviouswork[16]utilized
Ourmaincontributionsare: VLMstodetectpotentialbugframesingameplayvideosbyinte-
gratingbugdescriptionsfromreportswithkeyframesextracted
• Anexperience-basedcasestudydemonstratinghowgame-
fromvideos.
playrecordingsoriginallycollectedforstabilitytestingcan
Unlikepriorstudiesthatprimarilyrelyonpublicorsyntheti-
bere-purposedforlarge-scalevisualQAthroughautomated
callygenerateddatasets,ourworkbuildsuponindustrial,real-
VLManalysis.
world QA gameplay footage, a continuation from our previ-
• Apracticalassessmentoftwocommonenhancementstrate-
ous study [16]. We adapt the used keyframe-based strategy for
gies,RAGandjudge-based,appliedtoindustrialvideogame
extendedlonggameplayvideobyevaluatingVLMperformance
QAdata.
onproduction-scale,long-durationgameplayrecordingsthatare
automaticallycollectedoverhundredsofhours,andbyexploring
2 RelatedWork
methodstoenhancedetectionaccuracywithoutfine-tuning.Specif-
Traditionalbugdetection.Earlystudiesingamequalityassur- ically,twocomplementarytechniquesareinvestigated:RAGand
anceconcentratedonbugdetectionthroughhand-craftedrules, VLMasajudgemodel.
visualandtextfeatures,orspecializedmachinelearningmodels.Lin
etal.[13]conductedoneoftheearlieststudies,examiningwhether
3 Methodology
gameplayvideoscontainingbugscouldbeautomaticallyidentified
using publicly available metadata from online platforms. Build- Thissectionoutlinesourapproachfordetectingvisualbugsusing
ingonthisfoundation,Guglielmietal.introducedGELID[10,11], VLMsandkeyframesextractedfromlonggameplayvideos.Fig-
a method that extracts bug moments from gameplay videos by ure2illustratesthestepsofourapproach.Foreachlonggameplay
leveragingvideocaptiontexts.Similarly,Trueloveetal.proposed recording,we(1)extractkeyframes,(2)presenteachtoaVLM,and
classifyingvideosegmentsasbuggyornon-buggybasedonvideo (3)collectthemodel’sdecisiononwhetherabugispresent.

HowFarCanVLMsGoforVisualBugDetection?
Studying19,738Keyframesfrom41HoursofGameplayVideos FSE’26,June5–9,2026,Montreal,Canada
| Keyframe extraction |     |     |     | Bug frame detection |     |     |     |
| ------------------- | --- | --- | --- | ------------------- | --- | --- | --- |
Baseline
Judge and RAG enhancements
Gameplay
|     | Video |     |     |     |     | Text  | Image  |
| --- | ----- | --- | --- | --- | --- | ----- | ------ |
You are a senior AAA game QA expert...
|     |     |     |     |     |     | embedding | embedding |
| --- | --- | --- | --- | --- | --- | --------- | --------- |
Describe the frame and decide whether
it shows a player visible bug...
Similarity search
Extract keyframes
Judge
Response
|     |     |     |     | Bug label |     | Similar bug  |     |
| --- | --- | --- | --- | --------- | --- | ------------ | --- |
report
Image description
Keyframes
|     |     | Baseline model |     | Bug description |     |     |     |
| --- | --- | -------------- | --- | --------------- | --- | --- | --- |
Figure2:Overviewdiagramofourmethodology
Table1:Precisionandaccuracyacrossdifferentvariantsandjudgemodels
|     |                            |     |          | Precision |                 | Accuracy  |        |
| --- | -------------------------- | --- | -------- | --------- | --------------- | --------- | ------ |
|     | 4.1-mini(Baseline)         |     |          | 0.50      |                 | 0.72      |        |
|     | 5-mini                     |     |          | 0.35      |                 | 0.57      |        |
|     | Enhancements               |     | 4.1-mini | 4o-mini   | 5-mini 4.1-mini | 4o-mini   | 5-mini |
|     | +Judge                     |     | 0.47     | 0.48      | 0.55            | 0.72 0.71 | 0.74   |
|     | +ImageRAG                  |     | 0.37     | 0.35      | 0.46            | 0.67 0.67 | 0.71   |
|     | +TextRAG(Bugdescription)   |     | 0.47     | 0.47      | 0.57            | 0.71 0.71 | 0.75   |
|     | +TextRAG(Imagedescription) |     | 0.45     | 0.45      | 0.54            | 0.70 0.70 | 0.74   |
Table2:Distributionofprimarybugcategories(randomly thenumberofframesprocessedwhilepreservingthosemostlikely
sampled1,000resultsfrombaselineperformance) tocontainvisualanomalies.Thissamplingstrategyachieved98.79%
bugcoverageinpriorevaluations,andinthisstudy,weevaluated
| Category             |     | Percentage(%) |     | thesameFirstPersonShooter(FPS)game. |                   |     |     |
| -------------------- | --- | ------------- | --- | ----------------------------------- | ----------------- | --- | --- |
| Logmessage(s)        |     | 46.80         |     |                                     |                   |     |     |
|                      |     |               |     | 3.2                                 | Bugframedetection |     |     |
| Othervisualanomalies |     | 53.20         |     |                                     |                   |     |     |
Thebugframedetectiontaskisformulatedasasinglebinaryde-
| -Rendering&Texture |     | 18.60 |     |     |     |     |     |
| ------------------ | --- | ----- | --- | --- | --- | --- | --- |
cisionaccompaniedbyabriefjustification:givenakeyframe,the
18.10
-UI&HUD model must classify it as buggy or normal and provide a ratio-
6.10
-Animation&VFX nalizationinoneortwosentences.Thistaskinstructionremains
-Lighting&Shadow 5.90 consistentacrossallexperiments.Subsequenttechniquesonly(1)
| -Physics&Collision |     | 3.10 |     |     |     |     |     |
| ------------------ | --- | ---- | --- | --- | --- | --- | --- |
re-evaluatethemodel’sansweror(2)modifytheinformationpro-
| -GameCrash&Logic |     | 0.70 |     |     |     |     |     |
| ---------------- | --- | ---- | --- | --- | --- | --- | --- |
videdtothemodel.ToenhanceVLMperformanceinthistask,two
0.60
-Performance complementarystrategiesareincorporated,motivatedbyrecent
0.10
| -Other |     |     |     | advancesinmodelevaluationandcontextenrichment: |     |     |     |
| ------ | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
Judgemodels:WeintroducesecondaryVLMstore-evaluate
theprimaryoutput.Previous’LLM-as-a-Judge’studieshavedemon-
3.1 Keyframeextraction
stratedthatmodelscanserveasreliableevaluators,exhibitinghigh
Keyframescapturemajorvisualchangesinthevideo,enabling agreementwithhumanjudgments[5,6,12,30].Inthisstudy,the
analysistofocusonthemostrepresentativemomentsofgame- judgemodelreceivestheframe,thedecisionlabel,anditsrationale,
play.LongQAtestrecordingsoftenspantensofminutesorhours, andtheneitherconfirmsoroverturnsthedecision.Thisverification
resultinginsubstantialredundancyacrossadjacentframes.Ana- isprimarilydesignedtoreducefalsepositivesinbugdetection.
lyzingeveryframeiscomputationallyintensiveandunnecessary Metadata-augmentedpromptingusingRAG:Toexpandthe
fordetectingvisibleanomalies.Buildingonourpreviouswork[16], model’s knowledge base without fine-tuning, prior bug reports
keyframesareextractedusingFFmpeg[1]tosignificantlyreduce mostsimilarinvisualortextualcontentareretrievedandappended

FSE’26,June5–9,2026,Montreal,Canada WentaoLu,AlexanderSenchenko,AlanSayle,AbramHindle,andCor-PaulBezemer
tothepromptcontext[4,7,15,18].Providingmetadataandtex- introducedanadditionalcategorytoourstudybeyondtheseven
tualdescriptionsofexpectedbehaviorhasbeenshowntoimprove categoriesusedinourpreviouswork[16],showninTable2.
VLMreasoningregardinganomalies[16,17].Inpractice,foreach Bugreports:Inadditiontothislabeledgameplayvideocorpus,
keyframe,asimilarbugreportisretrievedfromthedatabaseand weutilizeadatabaseofhistoricalbugreportscollectedfromthe
providedalongsidethetaskinstruction.Themodelthenissuesthe internalJIRAsystem,awidelyadoptedplatformforbugreports[3].
samebinarydecisionwithabriefjustification. Each report includes a bug description, optional screenshot ar-
tifacts, and associated developer metadata. The database is pre-
3.2.1 Baseline. Thebaselineservesasthesimplestreferencepipeline.
vectorizedforinternalservices:textisembeddedusinggte-qwen2-
EachextractedkeyframeisdirectlypresentedtotheVLM(gpt-4.1-
1.5b-instruct-embed-f16[20],andimagesareembeddedusingclip-
mini[22])usingtheabovetaskinstruction,producing:
vit-base-patch32[21].EmbeddingsarestoredinanElasticSearch
• Buglabel(True/False):Whethertheframecontainsavisi- (ES)index[8].Thisvectorizeddatabaseenablessimilaritysearch
blebug. queriesbasedoncosinesimilarityandunderpinstheRAGprompt-
• Imagedescription:Adetaileddescriptionofthekeyframe. ingstrategiesevaluatedinSection5.Duetolegalconstraints,we
• Glitchdescription:Ashortrationaleexplainingtheob- cannotpublishourdataorprovideamoredetaileddescriptionof
servedbug,iflabeledTrue. theembeddingstrategy.
Thisbaselinereflectsthemodel’sout-of-the-boxabilitytogen- Usedmodels:Alljudgeandbaselinemodelsusedinthisstudy
eralizetothegameQAdomain. aresourcedfromOpenAI[24],accessedthroughAPIversion“2025-
04-01-preview"(thelatestversionatthetime)[19],whichprovides
3.2.2 JudgeandRAGenhancements. Withthegoalofimproving
industry-leading,production-gradeVLMs.Thisensuresthatmodel
thebaselineperformance,wefirstapplythejudgestepdirectly
behaviorandevaluationresultsarebasedonstandardized,widely
overthebaselineresults.Subsequently,weaugmentedthebaseline
recognizedarchitectures.Wespecificallyselecttheminivariantsto
approachwithanadditionalretrieval-augmentedpromptingstep.
balanceperformanceandcost,reflectingpracticalconsiderations
Threecomplementaryretrievalstrategiesareusedtoidentifythe
fordeploymentinlarge-scale,production-readyQAenvironments.
mostrelevantpriorbugreportsforeachkeyframe:
Duetointernalaccessrestrictions,wearelimitedtousingOpenAI
(1) Imagesimilarity:ThekeyframeisembeddedusingaCLIP models.
imageencoder[21]andcompared(basedoncosinesimilarity Performancemetrics:Allmetricsarereportedasper-video
betweentwovectors)againststoredimageembeddingsof meanstoensurethatlongerrecordingswithmorekeyframesdonot
historicalimagesattachedtobugreports. disproportionatelyinfluencetheoverallresults.Wefocusontwo
(2) Imagedescriptionsimilarity:Thedescriptionofthekeyframe keymetrics:precision(fractionofdetectedbugsthatareactual
producedbythebaselinemodelisembeddedusingatext bugs)andaccuracy(fractionofcorrectdetectionoverall).
embedderandmatchedagainsthistoricalbugreportdescrip-
tionstocapturesemanticsimilarity.Unlikethenextstrategy, 5 Results
thisgivesallkeyframesachancetoretrievesimilarreports
5.1 Baselineperformance
regardlessofanypotentialbugs.
(3) Bugdescriptionsimilarity:Whenthebaselinemodeliden- Motivation:Priortoevaluatingenhancementstrategies,theperfor-
tifiesabug(labelisTrue),itsgeneratedbugdescriptionis manceofaVLMonthebugdetectiontaskusingonlyvisualinput
embeddedandcomparedtohistoricalreporttextstoretrieve isevaluated.Thisbaselineestablishestheminimumperformance
exampleswithsimilarbugs. achievablewithoutexternalguidance.
Finally,were-runthetaskusinganupdatedpromptthatincludes Approach:EachextractedkeyframeisanalyzedbytheVLMusing
(1)thekeyframeimage,(2)thebaselinemodel’sinitialdecisionand thepromptdesigndetailedinSection3.Thegpt-4.1-minimodelis
rationale,and(3)theretrievedbugreport. selectedasthebaselineduetoitshighranking(#3)intheprevious
VideoGameQABenchstudy[27]anditscostefficiency.Forcompari-
4 Experimentalsetup
son,wealsoevaluatethesamebaselineconfigurationusing5-mini,
Gameplayvideodataset:Ourevaluationisconductedonacor- butomit4o-miniduetoitssignificantlyhighercost(approximately
pusof100longgameplaytestvideosdrawnatrandomfromdaily 20xmoretokensthan4.1-mini,asaknownissuetoOpenAI).
automatedrunswithinanindustrialQApipeline.Thesevideos AsshowninTable1,thebaselineachievesaprecisionof0.50
compriseatotalof41hoursoffootage,encompassing4,336,132 andanaccuracyof0.72across100gameplayvideos.Theseresults
videoframes,withameanvideolengthof24minutesand5sec- indicatethatoff-the-shelfVLMsgeneralizeeffectivelytogame
onds.SegmentationusingFFmpeg[1],consistentwithourprior QA videos. With a precision of 0.50, half of the model-flagged
work[16],yields19,738keyframes.Toestablishagroundtruth, framescorrespondtotruebugs.Reviewingonlytheflaggedframes
allextractedkeyframesweremanuallyreviewedandlabelledby reduces human inspection from 4,336,132 total frames to 2,002
oneoftheauthors.Eachframeisannotatedwithabinarylabel (≈0.05%),therebyconvertingrecordingsintoamanageabletriage
indicatingthepresenceorabsenceofaplayer-visiblebug. queuewithcandidatebugdescriptionsgeneratedbythemodel.
Bugcategories:Unlikeregulargameplayrecordings,automated Inadditiontoperformancemetrics,thetypesofvisualbugsthat
QAtestrunsconstantlydisplayon-screenlogmessagesgenerated theVLMiscapableofdetectingareexamined.Table2presentsthe
bybackendloggingsystems.Whenthesemessagesindicatecriti- distributionofprimarydetectedbugcategoriesfrombaselinere-
calerrorsorfailures,theyareconsideredbugs.Consequently,we sults.Nearlyhalfoftheidentifiedbugs(46.8%)areon-screenerror

HowFarCanVLMsGoforVisualBugDetection?
Studying19,738Keyframesfrom41HoursofGameplayVideos FSE’26,June5–9,2026,Montreal,Canada
messagesgeneratedbybackendloggingsystems.Theseoverlays as“needles,”whichareamongthousandsofnormalframessampled
typicallyindicatelower-levelsystemorengineerrors,suchasmiss- uniformlyatoneframepersecond.Withinthisframework,4.1-mini
ingassets,nullreferences,ornetworkfailures,ratherthanvisual achievedanaccuracyofonly10%.Ourstudyconstitutesavariant
anomalies.However,suchtextoverlaybugsarereadilydetectedby oftheNIAHtask.Insteadofuniformsampling,ouranalysisfocuses
themodel,indicatingthatVLMscaneffectivelyrecognizeinterface onextractedkeyframesthatcapturemajorvisualscenesandsub-
overlaystodiagnosticandprioritizederrormessages.However, stantiallyreduceredundancy.Second,ourindustrialQAdataset
thesecasescouldpotentiallybeaddressedmoreefficientlyusing differsqualitatively.Alargeportionofdetectedanomaliesareon-
traditionalopticalcharacterrecognition(OCR),whichwouldallow screenlogmessages,whicharevisuallyeasilyrecognizedbythe
VLMstofocusonnon-textualanomalies.Theremaining53.2%of model.Finally,ourformulationanalyzeseachkeyframe,similarto
detectedbugscomprisesadiverserangeofvisualanomalies.The image-baseddetectioninVideoGameQA-Benchthatscores76.8%in
VLMcanidentifymanyofthesecasesbasedsolelyonvisualcontext. accuracy.Bugframesremainrarewithinthesekeyframesequences,
Notably,visualbugswithinHUD&UIoftenpersistacrossmultiple andourresultachieves74%accuracy,substantiallyoutperforming
consecutivekeyframes,resultinginduplicatedetections.Apromis- theNIAHbaselinebutcomparabletoimage-basedglitchdetection.
ingdirectionforfutureresearchistoclusterbugkeyframesbased Additionally,theuseofkeyframespreservestimestampmetadata
onvisualsimilarityorbugtype,mergingredundantdetectionsand fromtheoriginalvideos,enablingdirectbuglocalizationwithout
thuseffectivelycapturingrecurringorpersistentvisualanomalies. requiringthemodeltoinfer.
Anoff-the-shelfVLMcanachieves50%precisionwhilereducingman-
ualreviewtoamanageablesubsetofframes,anddiscoverbugsthat 7 ThreatstoValidity
wouldotherwiseremainunseeninunreviewedQArecordings.
Internalvalidity:Apotentialthreatisthegroundtruthlabeling
process.Allkeyframeswerelabeledbyasingleauthor,whichrisks
5.2 JudgeandRAGperformance
annotationmistakesandsubjectivebias.Somelabelnoiseislikely
5.2.1 Judgemodels. Inthissetting,thejudgemodelreceivesthe presentandmayaffecttheperformanceevaluation.
keyframe,thebaselinepredictedlabel,andtheassociatedreasoning, Externalvalidity:OurdatasetconsistsoflongQArecordings
andthenre-evaluatesthedecision. from a single game within one industrial pipeline. Other game
Overall,judgemodelsyieldmixedoutcomes.Both4.1-mini genres or earlier development stages may exhibit different bug
and4o-miniperformslightlybelowthebaseline(precision0.47–0.48, typesandvisualstyles,whichcouldchangeVLMbehaviour.
accuracy0.71–0.72),whereas5-minidemonstratesamodestim- AnotherthreatisthatouranalysisislimitedtoOpenAIminiVLM
provement,achieving0.55precisionand0.74accuracy.However, variantsbecauseofinternalaccessconstraints.Othermodelfamilies
when5-miniisuseddirectlyasthebaselinedetectormodelinstead withlarger-capacitymodelsmightexhibitdifferentperformance
of4.1-mini,itsperformanceissubstantiallylower(0.35precision, and different sensitivity to RAG and judge strategies. Similarly,
0.57accuracy).Thisresultsuggeststhat5-miniismoreeffectiveas ourRAGsetupsdependononespecificembeddingconfiguration
anevaluatorthanasapredictor. andJIRA-basedreportstructure.Differentbugtrackingsystemsor
5.2.2 Retrieval-augmentedprompting. ResultsindicatethatRAG embeddingstrategiesmightyielddifferentRAGquality.
oftenintroducesnoise.Image-basedretrievaldecreasesperfor-
mance(precision=0.38,accuracy=0.68)becausevisuallysimi-
8 Conclusion
larimagesareoftenretrieved,yetthecorrespondingbugreport
descriptionsareunrelated.Text-basedretrievalyieldsimproved Inthisstudy,weevaluatedthecapabilityoflargevision-language
performance,particularlywhenretrievedusingbugdescription modelstodetectvisualbugsdirectlyfromindustrialQAgameplay
similarityandreviewedby5-mini,achieving0.57precisionand videos.Usingadatasetof100videos,41hoursand19,738keyframes,
0.75accuracy.Thisresultslightlysurpassesboththebaselineand weshowedthatasimplebaselinewithgpt-4.1-minicanreduce
thejudge-onlytechnique. manualinspectionofentirevideostoamanageabletriagequeueof
BothjudgeandRAGstepsdoubleinferencetimeandcostcom- frames.
paredtothebaseline,sincetheyrequireasecondmodelcallandad- Wefurther examined two widely used strategies for improv-
ditionalembeddingretrievalqueries.Giventhemarginalaccuracy inglargemodelperformance:judge-basedre-evaluationandRAG.
gains,thishighlightsatrade-offbetweenperformanceimprove- Acrosstheconfigurationsweevaluated,image-basedretrievalde-
mentandpracticaldeployabilityinQApipelines. gradedperformance,whiletext-basedretrievalyieldedonlymar-
ginalgains.Similarly,astrongerjudge(gpt-5-mini)couldrefine
JudgeandRAGstrategiesyieldonlymarginal,model-specificgains.A
baselineresults,butimprovementsweremodest.
capablejudgecanrefinebaselineoutputs,whereastext-basedretrieval
Overall,thesefindingshighlightthepracticalpotentialofVLM-
cansometimesimproveresults.
basedtriageforindustrialQAworkflows,substantiallyreducing
thevolumeofvideothatrequireshumanreview.However,our
6 Discussion
findingsalsoshowthatimprovingVLMperformanceisnottrivial.
Comparisontopriorwork:Taesirietal.introducedVideoGameQA- Furtherprogresswillrequiremoretargetedhybriddesigns,such
Bench[27],whichfeaturesthechallengingNeedle-in-a-Haystack asseparatingtextualOCR,incorporatingtemporalreasoningover
(NIAH)task.Inthistask,amodelisrequiredtoidentifyanomalous sequencesofframes,andclusteringredundantbugkeyframesto
framesandtheircorrespondingtimestampsinavideo,referredto betterexploitthestructureofQAgameplayrecordings.

FSE’26,June5–9,2026,Montreal,Canada WentaoLu,AlexanderSenchenko,AlanSayle,AbramHindle,andCor-PaulBezemer
References
[28] MohammadRezaTaesiri,FinlayMacklon,andCor-PaulBezemer.2022. CLIP
[1] 2025.FFmpeg. https://ffmpeg.org/ meetsGamePhysics:Towardsbugidentificationingameplayvideosusingzero-
[2] SimonAmey.2022. SoftwareTestDesign:WriteComprehensiveTestPlansto shottransferlearning.InInternationalConferenceonMiningSoftwareRepositories
UncoverCriticalBugsinWeb,Desktop,andMobileApps.PacktPublishing,Birm- (MSR)(2022-03-24).
ingham,UK. [29] AndrewTruelove,ShiyueRong,EduardoSantanadeAlmeida,andIftekhar
[3] Atlassian.2025.Jira. https://www.atlassian.com/software/jira Ahmed.2023.FindingtheNeedleinaHaystack:DetectingBugOccurrencesin
[4] MircoBonomoandSimoneBianco.2025.VisualRAG:ExpandingMLLMvisual GameplayVideos.arXiv:2311.10926[cs.SE] https://arxiv.org/abs/2311.10926
knowledgewithoutfine-tuning.arXiv:2501.10834[cs.CV] https://arxiv.org/abs/ [30] PatVerga,SebastianHofstatter,SophiaAlthammer,YixuanSu,AleksandraPiktus,
2501.10834 ArkadyArkhangorodsky,MinjieXu,NaomiWhite,andPatrickLewis.2024.
[5] DongpingChen,RuoxiChen,ShilinZhang,YaochenWang,YinuoLiu,Huichi ReplacingJudgeswithJuries:EvaluatingLLMGenerationswithaPanelofDiverse
Zhou,QihuiZhang,YaoWan,PanZhou,andLichaoSun.2024.MLLM-as-a-Judge: Models.arXiv:2404.18796[cs.CL] https://arxiv.org/abs/2404.18796
AssessingMultimodalLLM-as-a-JudgewithVision-LanguageBenchmark.In [31] FaliuYi,SherifAbdelfattah,WeiHuang,andAdrianBrown.2025. Ahybrid
Forty-firstInternationalConferenceonMachineLearning. https://openreview.net/ co-finetuningapproachforvisualbugdetectioninvideogames.InProceedingsof
forum?id=dbFEFHAD79 theTwenty-FirstAAAIConferenceonArtificialIntelligenceandInteractiveDigital
[6] LauraDietz,OlegZendel,PeterBailey,CharlesL.A.Clarke,ElleseCotterill,Jeff Entertainment(Edmonton,Alberta,Canada)(AIIDE’25).AAAIPress,Article17,
Dalton,FaeghehHasibi,MarkSanderson,andNickCraswell.2025.Principlesand 11pages. doi:10.1609/aiide.v21i1.36820
GuidelinesfortheUseofLLMJudges.InProceedingsofthe2025InternationalACM
SIGIRConferenceonInnovativeConceptsandTheoriesinInformationRetrieval
(ICTIR)(Padua,Italy)(ICTIR’25).AssociationforComputingMachinery,New
York,NY,USA,218–229. doi:10.1145/3731120.3744588
[7] ZongcanDing,HaodongZhang,PengWu,GuansongPang,ZhiweiYang,Peng
Wang,andYanningZhang.2025. SlowFastVAD:VideoAnomalyDetection
viaIntegratingSimpleDetectorandRAG-EnhancedVision-LanguageModel.
arXiv:2504.10320[cs.CV] https://arxiv.org/abs/2504.10320
[8] elastic.2025.OPENSOURCESEARCH,ANALYTICS,ANDAIPLATFORM. https:
//www.elastic.co/elasticsearch
[9] EmanuelaGuglielmi,GabrieleBavota,RoccoOliveto,andSimoneScalabrino.
2025.AutomaticIdentificationofGameStutteringviaGameplayVideosAnalysis.
ACMTrans.Softw.Eng.Methodol.34,2,Article38(Jan.2025),29pages. doi:10.
1145/3695992
[10] EmanuelaGuglielmi,SimoneScalabrino,GabrieleBavota,andRoccoOliveto.
2022. TowardsUsingGameplayVideosforDetectingIssuesinVideoGames.
arXiv:2204.04182[cs.SE] https://arxiv.org/abs/2204.04182
[11] EmanuelaGuglielmi,SimoneScalabrino,GabrieleBavota,andRoccoOliveto.
2023.Usinggameplayvideosfordetectingissuesinvideogames.EmpiricalSoftw.
Engg.28,6(Oct.2023),32pages. doi:10.1007/s10664-023-10365-0
[12] HaitaoLi,QianDong,JunjieChen,HuixueSu,YujiaZhou,QingyaoAi,ZiyiYe,
andYiqunLiu.2024.LLMs-as-Judges:AComprehensiveSurveyonLLM-based
EvaluationMethods.arXiv:2412.05579[cs.CL] https://arxiv.org/abs/2412.05579
[13] DayiLin,Cor-PaulBezemer,andAhmedE.Hassan.2019.Identifyinggameplay
videosthatexhibitbugsincomputergames.EmpiricalSoftwareEngineering(12
2019).doi:10.1007/s10664-019-09733-6
[14] CarlosGarcíaLing,KonradTollmar,andLinusGisslén.2020.Usingdeepconvolu-
tionalneuralnetworkstodetectrenderedglitchesinvideogames.InProceedings
oftheSixteenthAAAIConferenceonArtificialIntelligenceandInteractiveDigital
Entertainment(AIIDE’20).AAAIPress,Article10,8pages.
[15] JingyuLiu,JiaenLin,andYongLiu.2024.HowMuchCanRAGHelptheReasoning
ofLLM?arXiv:2410.02338[cs.CL] https://arxiv.org/abs/2410.02338
[16] WentaoLu,AlexanderSenchenko,AbramHindle,andCor-PaulBezemer.2025.
AutomatedBugFrameRetrievalfromGameplayVideosUsingVision-Language
Models.arXiv:2508.04895[cs.SE] https://arxiv.org/abs/2508.04895
[17] FinlayMacklonandCor-PaulBezemer.2025. ExploringtheCapabilitiesof
Vision-LanguageModelstoDetectVisualBugsinHTML5<canvas>Applications.
arXiv:2501.09236[cs.SE] https://arxiv.org/abs/2501.09236
[18] AigerimMansurova,AiganymMansurova,andAliyaNugumanova.2024.QA-
RAG:ExploringLLMRelianceonExternalKnowledge.BigDataandCognitive
Computing8,9(2024). doi:10.3390/bdcc8090115
[19] Microsoft.2025.Azure. https://azure.microsoft.com/en-ca
[20] Ollama.2024.gte-Qwen2-1.5B-instruct.https://ollama.com/rjmalagon/gte-qwen2-
1.5b-instruct-embed-f16
[21] OpenAI.2021.clip-vit-base-patch32. https://huggingface.co/openai/clip-vit-base-
patch32
[22] OPENAI.2024.GPT-4.1mini. https://platform.openai.com/docs/models/gpt-4.1-
mini
[23] OpenAI.2024.HelloGPT-4o. https://openai.com/index/hello-gpt-4o
[24] OpenAI.2025.OpenAI. https://openai.com/
[25] MohammadRezaTaesiriandCor-PaulBezemer.2025. VIDEOGAMEBUNNY:
Towardsvisionassistantsforvideogames.InProceedingsoftheIEEE/CVFWinter
ConferenceonApplicationsofComputerVision(2025-03-01).
[26] MohammadRezaTaesiri,TianjunFeng,Cor-PaulBezemer,andAnhNguyen.2024.
GlitchBench:CanLargeMultimodalModelsDetectVideoGameGlitches?.In
ProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition
(CVPR).22444–22455.
[27] MohammadRezaTaesiri,AbhijayGhildyal,SamanZadtootaghaj,NabajeetBar-
man,andCor-PaulBezemer.2025. VideoGameQA-Bench:EvaluatingVision-
LanguageModelsforVideoGameQualityAssurance.arXiv:2505.15952[cs.CV]
https://arxiv.org/abs/2505.15952