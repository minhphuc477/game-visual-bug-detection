---
title: "Automatically Detecting Visual Bugs HTML5 Canvas Games"
author: "Macklon"
year: "2022"
source_file: "02_glitch_and_anomaly_detection/Macklon_2022_Automatically_Detecting_Visual_Bugs_HTML5_Canvas_Games.pdf"
source_sha256: "73bdcceda7a9a613872b10d0ce74c7d6f9470ed2e16cae288db92ee4092697d9"
converted_at: "2026-11-06T15:09:57.616787+00:00"
markitdown_version: "0.1.9"
char_count: 56642
---
| Automatically       | Detecting | Visual              | Bugs in | HTML5 | <canvas>             | Games |
| ------------------- | --------- | ------------------- | ------- | ----- | -------------------- | ----- |
| FinlayMacklon       |           | MohammadRezaTaesiri |         |       | MarkosViggiato       |       |
| macklon@ualberta.ca |           | taesiri@ualberta.ca |         |       | viggiato@ualberta.ca |       |
| UniversityofAlberta |           | UniversityofAlberta |         |       | UniversityofAlberta  |       |
| Edmonton,AB,Canada  |           | Edmonton,AB,Canada  |         |       | Edmonton,AB,Canada   |       |
| StefanAntoszko      |           | NataliaRomanova     |         |       | DalePaas             |       |
santoszk@ualberta.ca natalia.romanova@prodigygame.com dale.paas@prodigygame.com
| UniversityofAlberta |     | ProdigyEducation  |     |     | ProdigyEducation  |     |
| ------------------- | --- | ----------------- | --- | --- | ----------------- | --- |
| Edmonton,AB,Canada  |     | Toronto,ON,Canada |     |     | Toronto,ON,Canada |     |
Cor-PaulBezemer
bezemer@ualberta.ca
UniversityofAlberta
Edmonton,AB,Canada
ABSTRACT
TheHTML5<canvas>isusedtodisplayhighqualitygraphicsin
webapplicationssuchaswebgames(i.e.,<canvas>games).How-
ever,automaticallytesting<canvas>gamesisnotpossiblewith
existingwebtestingtechniquesandtools,andmanualtestingis
laborious.ManywidelyusedwebtestingtoolsrelyontheDocu-
mentObjectModel(DOM)todrivewebtestautomation,butthe
contentsofthe<canvas>arenotrepresentedintheDOM.The
mainalternativeapproach,snapshottesting,involvescomparing
oraclesnapshotimageswithtest-timesnapshotimagesusinganim-
agesimilaritymetrictocatchvisualbugs,i.e.,bugsinthegraphics
ofthewebapplication.However,creatingandmaintainingora-
clesnapshotimagesfor<canvas>gamesisonerous,defeatingthe
(a)Screenshotofourtest<canvas>game
purposeoftestautomation.Inthispaper,wepresentanovelap-
|     |     |     | <!DOCTYPE | html> |     |     |
| --- | --- | --- | --------- | ----- | --- | --- |
proachtoautomaticallydetectvisualbugsin<canvas>games.By
<html>
| leveraginganinternalrepresentationofobjectsonthe<canvas>, |     |     | <head> |     |     |     |
| --------------------------------------------------------- | --- | --- | ------ | --- | --- | --- |
wedecomposesnapshotimagesintoasetofobjectimages,each <style> body { margin: 0; display: flex; } </style>
|     |     |     | <script | src="main.js"></script> |     |     |
| --- | --- | --- | ------- | ----------------------- | --- | --- |
ofwhichiscomparedwitharespectiveoracleasset(e.g.,asprite)
</head>
usingfoursimilaritymetrics:percentageoverlap,meansquared
<body>
|     |     |     | <canvas | width="1280px" | height="720px"></canvas> |     |
| --- | --- | --- | ------- | -------------- | ------------------------ | --- |
error,structuralsimilarity,andembeddingsimilarity.Weevaluate
</body>
| ourapproachbyinjecting24visualbugsintoacustom<canvas> |     |     | </html> |     |     |     |
| ----------------------------------------------------- | --- | --- | ------- | --- | --- | --- |
game,andfindthatourapproachachievesanaccuracyof100%,
comparedtoanaccuracyof44.6%withtraditionalsnapshottesting.
(b)HTMLcodeforourtest<canvas>game
CCSCONCEPTS
Figure1:Thegraphicsofa<canvas>gamearerepresentedas
•Softwareanditsengineering→Softwaretestinganddebug- abitmap,andnotintheDOM,whilethegame’ssourcecode
residesinthescriptmain.js.
ging.
KEYWORDS
commonlyusedwebtestingtechniquesleveragetheDocument
visualbugs,testautomation,HTMLcanvas,webgames
ObjectModel(DOM)todrivetestautomation,butasdemonstrated
inFigure1,thecontentsofthe<canvas>arenotrepresentedin
1 INTRODUCTION
theDOM.
TheHTML<canvas>isusedtodisplayhigh-qualitygraphicsin Toovercomethischallenge,snapshottestinghasbecomethe
web applications, and is particularly useful for web games (i.e., industrystandardapproachtovisualtestingfor<canvas>applica-
<canvas>games)[13,18,30,31,50].HTML5<canvas>gamesare
tions,asitdoesnotrelyontheDOM,butinsteadreliesonscreen-
receivinggrowingattentionfromindustry[26,33],butitischalleng- shotsofthewebapplication.Snapshottestingtargetsvisualbugs,
ingtoautomaticallytest<canvas>games,aswidelyusedwebtest- i.e.,bugsthatarerelatedtothegraphicsoftheapplication,byauto-
ingtechniquesandtoolsdonotworkforthe<canvas>[23].Many maticallycomparingoraclescreenshotswithscreenshotsthatare

FinlayMacklon,MohammadRezaTaesiri,MarkosViggiato,StefanAntoszko,NataliaRomanova,DalePaas,andCor-PaulBezemer
recordedduringtheexecutionofatestcase.However,aswediscuss 2 BACKGROUND
inSection2.2andshowinFigure2,snapshottestingcannotdeal In this section, we give background information about HTML5
withthedynamicnatureof <canvas>games,asthisdynamism <canvas>gamesandsnapshottesting.
causesvariationbetweenthescreenshotsthatishardtoaccount
forautomatically.
2.1 HTML5<canvas>games
Becauseofthetechnicalchallengesof <canvas>testing,and
theinherentdifficultiesoftestinggames[16,19,28,32,34,39], By combining the high-quality graphics of the <canvas> with
<canvas>gamesaremostlytestedmanually.Manualtestingre- browserevents,suchasmouseclicks,gamedeveloperscancre-
quireslargeamountsofmanualtimeandeffort,limitingtheamount atecompletegamesthatruninawebbrowser.
ofbugsthatqualityassurance(QA)analystscanrealisticallydis-
Open-sourceframeworks. Itisdifficulttointegratethe<canvas>
coverandreport.
withotherpartsofawebapplication[23],andso<canvas>frame-
Therefore,weproposeanautomatedapproachforthevisual
worksareusedtoeasethedevelopmentof<canvas>games.There
testingof<canvas>games.Ratherthan(manually)curatingoracle
existseveralfreeandopen-source(FOSS)<canvas>frameworks
screenshots,weusegameassets(seeSection2.1)toautomatically
that are widely-used to develop <canvas> games. For example,
generatevisualtestoraclesduringthetest,andautomaticallycom-
PixiJSandPhaserreceivemuchattentionfromgamedevelopers,
paretheseoracleassetswithindividualobjectsonascreenshot
asindicatedbythehighnumberofforumpostsrelatedtoeach
ofthe<canvas>.Ourapproachleveragesthegame’sinternalrep-
frameworkontheHTML5GameDevs[10]andStackOverflow[1]
resentationofobjectsonthe<canvas>,i.e.,the<canvas>objects
forums.Such <canvas>frameworkstypicallyprovideacustom
representation(COR),todecomposescreenshotsofthe<canvas>
internalrepresentationofobjectsonthe<canvas>,i.e.,a<canvas>
intoindividualobjectimages.
objectsrepresentation(COR),whichcanbemanipulatedbydevel-
Weevaluatedourapproachbyinjecting24uniquevisualbugs
operstoeasilycreateanimationsonthe<canvas>.Forexample,in
from4differentbugtypes(state,appearance,layout,rendering)as
PixiJS,theCORistermedscenegraph,andhasatreestructure.
definedbyMacklonetal.[23]intoacustom<canvas>testgame.
Our approach performed automated visual comparisons of the
Assets. Acommonwaytointegrategraphicsintoavideogameis
oracleassetsandtherenderedobjectsusingfoursimilaritymetrics:
usingsourceimages(assets)thatareusedtodisplayobjectsinthe
percentageoverlap,meansquarederror,structuralsimilarity,and
game.For<canvas>games,assetsareloadedbythewebapplication
embeddingsimilarity.Wecomparedourapproachwithabaseline
clientfromsomefileserverthroughwebrequests,likeanyother
approachthatistheindustrystandard,i.e.,snapshottesting.We
imageinawebapplication.However,assetsarenotrenderedas
foundthatwhenusingmeansquarederror,structuralsimilarity,
image(<img>)elementsonawebpage,butinsteadareusedas
or embedding similarity as the similarity metric, our approach
sourcebitmapsthataredisplayedonthe<canvas>bitmap.
achievesanaccuracyof100%forthe24injectedbugsinourtest
game,comparedtoanaccuracyof44.6%withthebaselineapproach.
2.2 Snapshottesting
Themaincontributionsofourpaperareasfollows:
Snapshottesting,e.g.,usingPercy,istheindustrystandardfor
• Wedesigned24syntheticvisualbugstoevaluateautomated visuallytestingwebapplications[36].Visualtestingisusedtotar-
testingapproachesfor<canvas>games,andweconfirmed getvisualbugs;visualbugsaremismatchesbetweenactualand
withanindustrialpartnerthatthesebugswererepresenta- expectedvisualpropertiesinthegraphicsofasoftwareapplica-
tiveofthebugsfoundinreal<canvas>games. tion[15].Traditionalsnapshottestingtypicallyinvolvescomparing
• We created a testbed for evaluating visual testing tech- screenshotsofthewebapplicationfromthesametestacrossdif-
niques for <canvas> games, i.e., a test <canvas> game, ferentruns,aftersomechange(s)tothesourcecode(e.g.,apull
whichincludesanon-buggyversionandabuggyversion request).Toperformtraditionalsnapshottesting,firstasetoforacle
ofthegamecontainingthe24syntheticbugs. screenshotsthathavebeencollectedduringatestrunmustbeman-
• Weextensivelyevaluatedcombinationsoffourwidely-used uallyverified,andthennewtestscreenshotscanbeautomatically
similaritymetricsforautomaticallydetectingvisualbugs collectedandcomparedatalatertimeusinganimagecompari-
in<canvas>games. sonalgorithm.Ifascreenshotdoesnotpasstheimagecomparison
• Forreproducibility,weopen-sourcedourtestbedandvi- check,thatscreenshot(ortestcase)isflaggedformanualreview.
sualbugsdatasetatthefollowinglink:https://github.com/ Figure2showshowmostofthevisualdifferencesbetweenthe
asgaardlab/canvas-visual-bugs-testbed. oracleandtestscreenshotsoccurduetorandomelementsofthe
• Aliveversionofourtest<canvas>gameisavailableatthe <canvas>game,whicharedesiredfunctionality,ratherthanthe
followinglink:https://asgaardlab.github.io/canvas-visual- injected visual bug. It is difficult to distinguish between visual
bugs-testbed/game. bugsandintendedfunctionalityfor<canvas>gameswhenusing
snapshottesting.Thisproblemcanleadtomanyfalsepositives,
Theremainderofourpaperisstructuredasfollows.Section2 increasingthemanualworkload(duetooraclere-verification)and
discussesbackgroundinformation.Section3discussesrelatedwork. reducingthebenefitofusingsnapshottestingasanautomated
Section4presentsourapproach.Section5detailsourexperiment testingapproach.Therefore,theindustry-standardapproachfor
setup.Section6presentsourresults.Section7containsthreatsto snapshottestingisfarfromidealfortestingmany<canvas>appli-
validity.Section8istheconclusiontoourpaper. cations,particularly<canvas>games.

AutomaticallyDetectingVisualBugsinHTML5<canvas>Games
(a)Oraclescreenshot (b)Testscreenshot (c)Imagedifference(inpink)
Figure2:Twoscreenshotsfromourtestgame.Inthetestscreenshot,thevikingcharacterismissingalogonhisshoulders
(injectedvisualbugS4inTable3,vikinganimationnotupdating).However,asobservedinthethirdscreenshot,thein-game
randomnesscausesalargerdifferencebetweenthescreenshotsthanthebugitself.
3 RELATEDWORK ofawebpageinsteadofentirescreenshots.Theydecomposedthe
Inthissection,wediscussrelatedworkon<canvas>testing,visual DOMalongwithscreenshotsandperformedautomaticstructural
webandGUItesting,andvisualgametesting. andvisualcomparisonsbetweenautomaticallyinferredwebpage
states. Bajammal and Mesbah [3] automatically inferred the se-
manticroleofregionsinawebpageandautomatedthetestingof
3.1 <canvas>testing
webaccessibilityrequirements.InanotherworkbyBajammaland
Macklonetal.[23]analyzedopensourceprojectsonGitHubthat Mesbah[2],theycombinedvisualanalysiswithDOMattributes
utilizethe<canvas>,andproposedataxonomyof<canvas>bugs.
toimproveautomatedwebpagesegmentation,whichcanassist
Theyshowedthatthemostfrequentlyreportedbugsintheopen withbuglocalization.Theseworksfocusonsegmentingandtesting
sourceprojectsarevisualbugs,i.e.,bugsthatarerelatedtothe thestructureofwebpages,i.e.,whatisrepresentedintheDOM,
graphicsofanapplication.Theirfindingsemphasizethatresearch butaspreviouslyexplained,thecontentsofthe<canvas>arenot
on<canvas>testingisatanearlystageandhasmanyopportunities,
representedintheDOM,meaningtheseapproachescannotbeused
andthatvisualbugsareaprimaryconcernfor<canvas>testing. toautomaticallycatchvisualbugsin<canvas>games.
Onlyonepriorstudyhasinvestigatedtestingmethodsforthe Severalpriorstudiesproposedtheuseofcomputervisionto
<canvas>.BajammalandMesbahproposeanapproachtoenable
leverage the visual aspect of a software application in an auto-
DOM-basedtestingofthe<canvas>byleveragingtraditionalcom-
matedtestingprocess.Mazinanianetal.[25]automaticallypre-
puter vision techniques to detect objects on the <canvas>, and dictedactionableelementsonawebpagethroughasupervised
subsequentlyaugmenttheDOMwitharepresentationofthose deeplearningapproach.Whiteetal.[46]proposedasupervised
objects[4].Theyreporthighaccuracyindetectingobjectsonthe deeplearningapproachandautomaticallyidentifiedGUIcompo-
<canvas>thatshouldnotbepresent(similartovisualbugS6in
nentstoimprovethecoverageofrandomtesting.Xueetal.[47]
Table3),howeveranyothertypeofoverlappingvisualbugonthe proposedasuperviseddeeplearningapproachtoassistinperform-
<canvas>wouldposechallengesfortheirvisualinferencealgo-
ingrecord-and-replayGUItestinginamobileorwebapplication.
rithm.Incontrast,weevaluateourapproachon24uniquebugs MozgovoyandPyshkin[27]usedtemplatematchingtorecognize
from4visualbugstypes,andfindthatourapproachshowsstrong objectsandGUIelementsinascreenshotofamobilegame,which
performanceforcatchingawidevarietyofvisualbugsthatare allowtestassertionstobemadeagainstthevisualcontentofthe
representativeofbugsfoundinreal-world<canvas>games.
game.Yeetal.[49]proposedasimilarGUIwidgetdetectionap-
proachformobilegames,inwhichtheyinstrumentedthesource
3.2 VisualwebandGUItesting codeofamobilegametoautomaticallyextractsamplesofGUIwid-
Aspreviouslyoutlined,existingautomatedwebtestingtechniques gets,andsubsequentlytrainedasuperviseddeeplearningmodel
andtoolsdonotworkforthe<canvas>,butpriorresearchhasalso forGUIwidgetdetection.Visualbugswouldinterferewiththe
indicatedthat<canvas>bugsoverlapwithvisualbugsfoundin GUIelementidentificationmethodsintheaforementionedworks,
graphicaluserinterfaces(GUIs)andgenericwebapplications[23].
whileourapproachinsteadtargetsvisualbugsin<canvas>games
Werefertothesurveyofcomputervisionapplicationsinsoftware withouttraininganynewmodels.
engineeringbyBajammaletal.[5]andthegreyliteraturereview Zhaoetal.proposedtheuseofunsuperviseddeeplearningmeth-
of AI-based test automation techniques by Ricca et al. [36] for odstodetectanomalousGUIanimations,whichrequiresonlysev-
anoverviewofvisualtestingforGUIsandwebapps.Here,we eralgroundtruthsamplesofacorrectGUIanimationtodetectthe
onlydiscussrelatedworkthatwasnotcoveredinthesurveyby
anomalousanimations[52].Giventhedynamicnatureof<canvas>
Bajammaletal.[5]. games,itwouldbeextremelychallengingtocollectgroundtruth
Severalpriorstudieshaveproposedtheuseofvisualanalysisto
samplesofallcorrectanimationsina<canvas>game,whichdoes
assistinautomatedtestingmethodsforwebapplications.Yandra- notsolvetheproblemsposedbysnapshottesting.Weavoidthis
pallyandMesbah[48]proposedamethodtoautomaticallydetect probleminourapproachbyautomaticallygeneratingvisualtest
near-duplicatestatesinwebapplicationsbycomparingfragments oraclesduringthetest.

FinlayMacklon,MohammadRezaTaesiri,MarkosViggiato,StefanAntoszko,NataliaRomanova,DalePaas,andCor-PaulBezemer
3.3 Visualgametesting Collecting data Preprocessing Detecting
images visual bugs
Given that the <canvas> is often used to build web games, we
provideanoverviewofvisualtestinginvideogames. Collect Preprocess Calculate
Automatedmethodsforgraphicsglitchdetectioninvideogames Game assets assets similarities
havebeenproposedinpriorwork.Nantesetal.proposeasemi-
automatedapproachtodetectshadowglitchesinavideogame
usingtraditionalcomputervisiontechniques[29].However,inour Execute Similarity
test case scores
workweproposeafullyautomatedapproachtodetectawider
rangeofvisualbugsthatarerelevantto<canvas>games. Assets Oracle asset
Otherstudieshaveutilizedrelativelyrecentadvancementsin
deeplearningtodetectgraphicsglitchesinvideogames[7,9,20] Collect COR Preprocess Detect visual
snapshots objects bugs
ortoleveragethevisualaspectofvideogamesforspriteandevent
extraction[17,21,22,38,41].However,thesemethodsallrequire
eithersignificantmanualefforttopreparethedataorin-house
machinelearningexpertisetotrainandfine-tunethemodels,or
theytargetonlyalimitedsetofvisualbugs(whencomparedto
Screenshot Object image
thefourtypesevaluatedinourpaper).Asourapproachutilizes
apre-trainedmodel,itrequiresonlyverybasicappliedmachine
learningknowledge,anditdoesnotrequiremuchdatapreparation. Figure3:Overviewofourapproach(shownwithvisualbug
L4inTable3,Vikinghaswrongrotation).
4 OURAPPROACH
Inthissection,wepresentourapproachforautomaticallydetecting
We automatically preprocess game assets to generate oracle
visualbugsin<canvas>games.Figure3showsanoverviewofthe
assetsduringtheexecutionofatestusingthefollowingprocess:
stepsofourapproach.
(1) ApplytransformationstotheassetasspecifiedintheCOR.
4.1 Collectingdata Forexample,crop,scale,tile,and/orrotatetheasset.
(2) Pastetheassetontoablankimagethatisthesamesize
Webeginbyautomaticallyinstrumentingtherenderingloopof
asthe<canvas>.Thepastelocationisdeterminedbythe
the<canvas>gamewithourcustomcodetocollectsnapshotsand
COR,andwillmatchthelocationofthegameobjectinthe
assets.Eachsnapshotcontainsascreenshotofthe<canvas>anda
screenshotifnobugsarepresent.
respective<canvas>objectsrepresentation(COR)fromthesame
(3) Generateanimagemaskfromthepastedasset(i.e.,the
pointintime.
resultfromthepreviousstep)andsaveforlatermasking
Foreachsnapshot,weautomaticallycollectascreenshotand
operations.
itsrespectiveCOR.Figure4illustrateswhataCORcontainsin
(4) Foranyoverlappingobjects,applytheirsavedmasksover
ourapproach.ACORisusedbya<canvas>gametodetermine
topofthepastedasset.Figure6showsanexampleofwhat
howtorendergameobjectstothe<canvas>,suchastheplayer
thismightlooklike.
character,backgroundlayers,andprojectiles.Eachobjectinthe
(5) Cropthepastedasset.
CORhaspropertiessuchasposition,size,androtation.
Weautomaticallydecomposescreenshotsintoasetofindividual
Whileperformingasnapshot,wepreventnewanimationframes
objectimagesaccordingtothefollowingprocess:
frombeingrendered,andsaveafrozencopyoftheCORalong
withasynchronizedscreenshotofthecurrentanimationframe (1) Applythebackgroundmask,i.e.,themaskgeneratedfrom
(asrenderedtothe<canvas>).Althoughoursnapshotoperation theobject’srespectiveasset.
brieflypreventstherenderingofafewnewframes,itdoesnot (2) Applytheforegroundmasks,i.e.,themasksthatweregen-
necessarilyinterruptthemaingameloop(dependinguponhowa eratedfromassetsbelongingtooverlappingobjects.
gameisimplemented). (3) Croptheobjectimageoutofthescreenshot.
As described in Section 2.1 of our paper, assets in <canvas> Afterpreprocessing,wehaveasetofimagepairs,witheachpair
gamesareservedthroughwebrequests,andsowecreatedacustom containinganoracleassetandobjectimage,whichshouldbeexactly
crawlertocollectassetsbasedontheresourceURLsofobjectsina thesameifnovisualbugsarepresent.
<canvas>game.AscanbeseeninFigure4,gameobjectsarelinked
totheirrespectiveassetsintheCOR,meaningassociatingagame 4.3 Detectingvisualbugs
objectwithitsrespectiveassetisstraightforward. Foreachpairoforacleassetandobjectimage,weuseanimage
similaritymetrictoautomaticallyperformavisualcomparisonof
4.2 Preprocessingimages
theimages.Ourapproachreliesonathresholdforthissimilarity
Foreachsnapshot,weleveragetheCORtoautomaticallygenerate metrictodecideifavisualtestcaseshouldpassorfail.Thisthresh-
oracleassetsandextractobjectimagesforcomparison.Figure5 oldshouldbedefinedempiricallyandforeachgame,asdifferent
showsourautomatedimageprocessingpipeline.Below,wedetail gamesmayhavedifferentlevelsofin-gamerandomnessthatcould
ourpreprocessingstepsfororacleassetsandobjectimages. affectthesimilaritymetric.

AutomaticallyDetectingVisualBugsinHTML5<canvas>Games
| HTMLCanvasElement |     | <canvas> objects representation (COR) |     |     |     |     |     |
| ----------------- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
1
| id: String[0..1] |     | view: HTMLCanvasElement |     |     |     |     |     |
| ---------------- | --- | ----------------------- | --- | --- | --- | --- | --- |
| width: Number    |     | objects: Object[*]      |     |     |     |     |     |
height: Number
*
| Frame          | 1   |                          | Texture | 1   | Object         |             | Scale |
| -------------- | --- | ------------------------ | ------- | --- | -------------- | ----------- | ----- |
| x: Number      |     | frame: Frame             |         |     | x: Number      | x: Number   |       |
| y: Number      |     | baseTexture: BaseTexture |         |     | y: Number      | 1 y: Number |       |
| width: Number  |     |                          | 1       |     | width: Number  |             |       |
| height: Number |     |                          |         |     | height: Number |             |       |
Anchor
|     |     | BaseTexture |     |     | rotation: Number |     |     |
| --- | --- | ----------- | --- | --- | ---------------- | --- | --- |
x: Number
texture: Texture
|     |     | scaleMode: Number |     |     |              | 1         |     |
| --- | --- | ----------------- | --- | --- | ------------ | --------- | --- |
|     |     |                   |     |     | scale: Scale | y: Number |     |
asset: Asset[0..1]
anchor: Anchor
0..1
|     |     |                     |       |     | tilePosition: TilePosition[0..1] |           | TilePosition |
| --- | --- | ------------------- | ----- | --- | -------------------------------- | --------- | ------------ |
|     |     |                     | Asset |     |                                  | x: Number |              |
|     |     | resourceUrl: String |       |     |                                  | y: Number |              |
0..1
Figure4:Unifiedmodelinglanguage(UML)classdiagramfora<canvas>objectsrepresentation(COR).
|     | Apply |     |     |     | Apply      |      |     |
| --- | ----- | --- | --- | --- | ---------- | ---- | --- |
|     |       |     |     |     | foreground | Crop |     |
transforms
masks
| Assets |     |     | Transformed asset |     |     |          | Oracle asset |
| ------ | --- | --- | ----------------- | --- | --- | -------- | ------------ |
| COR    |     |     |                   |     |     | Generate |              |
|        |     |     | Paste asset       |     |     |          | Saved masks  |
mask
Pasted asset
|            | Apply      |     | Apply      |     |      |     |              |
| ---------- | ---------- | --- | ---------- | --- | ---- | --- | ------------ |
|            | background |     | foreground |     | Crop |     |              |
|            | mask       |     | masks      |     |      |     |              |
| Screenshot |            |     |            |     |      |     | Object image |
Figure5:Automatedimagepreprocessingpipeline(shownwithvisualbugS1,player-characterisinvisible).
(a)Inputscreenshot (b)Thebackgroundmask (c)Oneoftheforegroundmasks (d)Outputobjectimage
Figure6:Abackgroundmaskandalloverlayingforegroundmasksareappliedtoisolateobjectimagesinourapproach.

FinlayMacklon,MohammadRezaTaesiri,MarkosViggiato,StefanAntoszko,NataliaRomanova,DalePaas,andCor-PaulBezemer
5 EXPERIMENTSETUP Table1:Visualbugtypesfoundin<canvas>applications[23].
Inthissection,wedescribeourexperimentsetupforevaluating
theperformanceofourapproachandthebaselineapproachfor Type ExampleDescription
automaticallydetectingvisualbugs.Weselectedsnapshottesting
State Objectvisiblebutshouldbeinvisible.
asthebaselineapproachforcomparisonwithourapproach,as
Appearance Objecthasincorrectcolour.
snapshottestingistheindustrystandardapproachfordetecting
Layout Objecthasincorrectposition,size,layer,etc.
visualbugsin<canvas>applications.
Rendering Objectisdistorted,blurry,orcontainsartifacts.
5.1 Thetestgame
Toevaluateourapproach,wecreatedacustom<canvas>game
usingthePixiJS1libraryandafreelyavailableassetpack2.PixiJS
isapopularfreeandopen-source<canvas>renderinglibraryfor
creating 2D animations with the <canvas>. Figure 8 shows the
statemachinediagramforourtestgame.Ourtestgameisaso-
calledcatchinggame,i.e.,agameinwhichprojectilesarerandomly
thrownfortheplayertocatch.Thetestgamecontainsavariety (a)RenderingbugR3inTable3. (b) Layout bug L5 in Table 3.
of animations, including animated sprites, rotating sprites, and Vikingandlogsareblurred. Treesareinthewronglayer.
backgroundtilingsprites.Thetestgamewasdesignedtobeplayed
ataresolutionof720p,withamaximumframerateof60FPS.
5.2 Thetestcase
Wewroteanautomatedtestcaseforour<canvas>game.Inour
testcase,thegamewasautomaticallyopenedinabrowserwindow
withsize1280𝑝𝑥×720𝑝𝑥.Next,thegamewasstartedthroughan
(c)StatebugS5inTable3.Fallen (d) Appearance bug A4 in Ta-
automateduserclick,andthentheplayer-characterwasmoved
loganimationisnotupdating. ble3.Logsareadifferentcolour.
backandforthacrossthescreenwithautomatedmousemovements
untiltheplayerlostalife(afterwhich,thetestcaseended).During
Figure7:Sampleinstancesofourinjectedvisualbugs.
eachtestcaseexecution,10snapshotsweretaken.
5.3 Injectedvisualbugs
meaningourinjectedvisualbugsweresuitableforevaluatingour
Weevaluatedtheperformanceoftheapproachesbyinjectingvisual approach.
bugsintoourtestgame.Totargetbugsthatarerelevantto<canvas>
games,weusedthetaxonomyof <canvas>bugsconstructedby 5.4 Similaritymetrics
Macklonetal.[23],andverifiedwithanindustrialpartnerthat Inourexperimentsweusedfoursimilaritymetricstocompare
ourinjectedbugswererelevanttoindustrial<canvas>games.In images.
Table1,weprovideeachvisualbugtypeandanexampledescription
ofabugofthattypeasdefinedinthetaxonomyof<canvas>bugs. Percentageoverlap(PCT). Weselectedpercentageoverlapasasimi-
laritymetricbecauseitisthesimplestmethodforcalculatingthe
Foreachofthefourvisualbugtypesdefinedinthetaxonomyof
<canvas>bugs,weinjectedsixdifferentbugs,withsomeprimarily similarityoftwoimages,andisusedinindustry-standardtools
suchasPercy.WecalculatedthePCTforapairofimagesbycal-
affectingforegroundobjects,andothersprimarilyaffectingback-
culatingthepercentageofpixelsthatexactlymatchbetweenthe
groundobjects.Intotal,weinjected24visualbugs.Figure7shows
twoimages.
fourexampleinstancesofvisualbugsweinjectedintothetestgame,
whileTable3providesdetaileddescriptionsofeachinjectedbug. Meansquarederror(MSE). Weselectedmeansquarederrorasa
Weinjectedmostofthevisualbugsbyalteringanassetduring similaritymetricbecauseitiswidelyusedinimageprocessingasan
testexecution,andthenreplaceditwiththenon-bugged(original) imagequalityindex[11,44],i.e.,tomeasuredegradationbetween
assetatthepreprocessingstageofourapproach.Weinjectedmost originalandreconstructedimages.TheMSEactuallycapturesthe
ofthevisualbugsthiswaybecauserealvisualbugscanbevery amountofdifference(i.e.,lowerisbetter)insteadofsimilarity(i.e.,
complexanddifficulttoreproduce[23].Someofourvisualbugs higherisbetter).Wecalculatedthemeansquarederrorforapair
wereinjectedthroughmodificationsinthetestgame’ssourcecode, ofimagesusingthescikit-image3library.
forexample,forrenderingbugR1(objectsaredistorted)wein-
jectedroundingerrorsintheimagescaling.Althoughourinjected Structuralsimilarity(SSIM). Weselectedstructuralsimilarityasa
visualbugshadadifferentrootcausethanrealvisualbugsonthe similaritymetricbecauseitisintendedtobecomplementaryto
<canvas>,weconfirmedwithanindustrialpartnerthatthevisual meansquarederrorasanimagequalityindex[45].Weusedthe
effectsweresimilartovisualbugsfoundinreal<canvas>games, scikit-imagelibrarytocalculatestructuralsimilarityforeach
pairofimages.
1https://pixijs.com/
2https://raventale.itch.io/parallax-background 3https://scikit-image.org/

AutomaticallyDetectingVisualBugsinHTML5<canvas>Games
|     |     |     |          | [Catch] |     |          |     | [Catch] |          |
| --- | --- | --- | -------- | ------- | --- | -------- | --- | ------- | -------- |
|     |     |     | Caught 0 |         |     | Caught 1 |     |         | Caught 2 |
Title screen
| [Load] |     | [Start] | projectiles |     |           | projectile |     |           | projectiles |
| ------ | --- | ------- | ----------- | --- | --------- | ---------- | --- | --------- | ----------- |
|        |     |         |             |     | [Collect] |            |     | [Collect] |             |
[Collect] [Catch]
|     |     | [play again] |        | [has more lives] |     |     |     |     |          |
| --- | --- | ------------ | ------ | ---------------- | --- | --- | --- | --- | -------- |
|     |     |              | [else] |                  |     |     |     |     | Caught 3 |
Crushed
|     |     |     |     | [Lose life] |     |     |     |     | projectiles |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- | ----------- |
[else]
[Collect] [Catch]
[Catch]
[Collect]
|     |     |     |     |     |     | Caught 5 |     |     | Caught 4 |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- | -------- |
Game over
|     |     |     |     |     |     | projectiles |     |     | projectiles |
| --- | --- | --- | --- | --- | --- | ----------- | --- | --- | ----------- |
[Catch]
Figure8:Finitestatemachinediagramforourtest<canvas>game.
Embeddingsimilarity(ESIM). Ourfourthandfinalmetric,embed- Statisticalsignificanceandeffectsizes. WeusedtheMann-Whitney
dingsimilarity,wasthesimilarityoftwoimageswhenrepresented Utest[24]todetermineifthepopulationsofsimilarityscoreswere
asembeddingsofanimageclassificationmodel,i.e.,adeeplearn- statisticallysignificantlydifferent.TheMann-WhitneyUtestisa
ingvisionmodel.Embeddingsarethevisionmodel’sinner-layer non-parametrictestthatcomparestwodistributionsofunrelated
representation(s)ofanimage,i.e.,thefeaturerepresentationsofthe populationstodeterminehowmuchthepopulationsstatistically
overlap,withsomeprobability𝑝.Generally,a𝑝valueoflessthan
imagebeforetheclassificationlayer.Weimplementedembedding
0.05indicatesthatthepopulationsdisplayastatisticallysignificant
similarityinourexperimentsbyencodingtheimagesastheem-
beddingsofthefinalconvolutionallayeroftheResNet-50model difference,asaverylow𝑝valueindicatesitisveryunlikelythat
pre-trainedontheImageNetdataset[14].Theseimageembeddings twopopulationsarestatisticallysimilar.
hadafeaturevolumeof (2048,7,7).Weselectedthepre-trained TobetterunderstandtheresultsoftheMann-WhitneyUtest,
ResNet-50modelastheResNetarchitectureiswidelyusedfor wealsocalculatedCliff’sdelta[8]todeterminetheextenttowhich
transferlearningapplications[6,22,35].Weextractedtheembed- thepopulationsofbuggyandnon-buggysimilarityscoreswere
dingsofthefinalconvolutionallayeroftheResNet-50model,as differentpermetric.TointerprettheCliff’sdeltavalues(𝑑),we
isdoneinpriorwork[12,40].Tocalculatethesimilarityofthe usedthethresholdsprovidedbyRomanoetal.[37]todetermine
embeddings,weselectedcosinesimilarity,awidelyusedsimilarity theeffectsizes,asdoneinpriorwork[16].Thethresholdsused
| metric[41,42,43,51]. |     |     |     |     | wereasfollows: |     |     |     |     |
| -------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
|𝑑 .1
W e u se d th e p re - tr a in e d m o d el i n i n f e r e n c e m o d e , m e a n in g w e  n eg l i gible i f | ≤ 0 4 7
did n ot h a ve to p e rf o r m a n y d at a la b e l li n g , t r a in in g , o r fi n e -t u ni ng , sm a l l i f 0 .1 4 7 < | 𝑑 | ≤0.33
Effectsize=
| i.e . , w e u | se d t h e m od e l   | o u t - o f- th e -b o | x . W e pe r fo r m | ed i n fe re n c e |     |         |         |               |               |
| ------------- | --------------------- | ---------------------- | ------------------- | ------------------ | --- | ------- | ------- | ------------- | ------------- |
|               |                       |                        |                     |                    |     |  m | e d ium | i f 0 . 3 3 < | |𝑑 | ≤ 0 .474 |
| w i t h th e  | p re -t r a in ed R e | s N e t - 5 0 m o d e  | l o n an N V I D    | IA T i ta n R T X  |     |         |         |               |               |
|               |                       |                        |                     |                    |     |         |         | .             | < |𝑑 | ≤      |
graphicscard.Weloadedthemodelfromthetorchvision4library lar g e i f 0 4 74 1

andusedthePyTorch5librarytocalculatecosinesimilarity.
Accuracy. Ourchoiceofthresholdselection(Section5.5)meant
5.5 Empiricalthresholdselection thatitwasonlypossiblefortheretobetruepositive(TP)andfalse
negative(FN)casesinourresultsforvisualbugdetection.There-
Weempiricallyselectedasinglethresholdforeachsimilaritymetric
fore,thebestchoiceofevaluationmetricwasaccuracy,whichwas
usedineachapproachtodecidewhetheratestcaseisbuggy.To
|     |     |     |     |     |     |     |     |     | ( # t r u e po s it i ve s ) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- |
empiricallydeterminethethresholds,wecalculatedthesimilarities calculatedasfollows:accuracy = .
|     |     |     |     |     |     |     |     | (#truepos | it iv e s ) + ( # f a ls e negatives) |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------------------------------- |
ofallimagepairsfor10repetitionsoftestdatawithnobugsinjected
(i.e.,withnon-buggysnapshots),andtooktheoveralllowest(or
6 RESULTS
highestforMSE)similarityscoreforeachmetricasourthresholds.
Hence, we chose the thresholds to yield zero false positives, as Inthissection,wepresentourexperimentalresultsforautomat-
falsepositivesresultinawastedeffortfromthegamedeveloper’s icallydetectingvisualbugswithourapproachandthebaseline
perspective(astheyneedtoinvestigatethefalsepositive). approach.WhenusingMSE,SSIM,orESIMasthesimilaritymetric,
wefindthatourapproachachievesanaccuracyof100%forour
24injectedvisualbugs,comparedtoanaccuracyof44.6%with
5.6 Evaluatingtheexperiments
|     |     |     |     |     | the baseline | approach | (with | PCT as the | similarity metric). Our |
| --- | --- | --- | --- | --- | ------------ | -------- | ----- | ---------- | ----------------------- |
Herewedescribethemethodsweusedtoevaluateourexperiments.
resultsshowthatourapproachismuchmoreeffectiveforautomat-
4https://pytorch.org/vision/stable/index.html icallydetectingvisualbugsin<canvas>-basedapplicationsthan
5https://pytorch.org/ thebaselineapproach(traditionalsnapshottesting).

FinlayMacklon,MohammadRezaTaesiri,MarkosViggiato,StefanAntoszko,NataliaRomanova,DalePaas,andCor-PaulBezemer
Table2:Mann-WhitneyUtestandCliff’sdeltaresults. 7 THREATSTOVALIDITY
Constructvalidity. Ourresultsmaybebiasedtowardsthesetof
Mann-WhitneyUtest Cliff’sdelta visualbugsthatweinjectedinourexperiments.However,ourin-
Metric Significantdifference Effectsize jectedvisualbugscoveredallfourvisualbugtypesthatarerelevant
tothe<canvas>,asdefinedinpriorwork[23].Whilethevisual
Snapshot PCT yes small
bugsweinjectedmaynothavethesamecauseasrealvisualbugs
Testing MSE yes medium
foundin<canvas>applications,thevisualeffectsarethesame;
SSIM yes small
eachinjectedvisualbugwasdesignedtoresemblearealworld
Our PCT yes medium example.Tomitigatethethreatofinjectingunrealisticbugswealso
Approach MSE yes medium confirmedwithanindustrialpartnerthatourinjectedbugswere
SSIM yes medium representativeofrealvisualbugsinindustrial<canvas>games.
ESIM yes large Therearedifferentpossiblechoicesofimagecomparisonmetrics
forsnapshottesting,thebaselineapproachusedinourexperiments.
WeselectedPCTasanimagecomparisonmetricbecausePercy,
awidelyusedsnapshottestingtool,usesathreshold-basedimage
6.1 Similarityscores
comparisonmetricthatissimilartoPCT.Wealsoempiricallyeval-
Figure9showsthedistributionsofthesimilarityscoresforeach uatedMSEandSSIMforsnapshottesting,anddeterminedthat
oftheevaluatedsimilaritymetrics,withtheminimumsimilarity neitherwerebetterthanPCTforsnapshottesting.
fornormalsnapshotsprovidingthethresholdsforbugdetection,
as described in Section 5.5. For each distribution, scores above Internalvalidity. Inourapproach,weutilizedthe<canvas>objects
thesetthreshold(withinthegreyed-outareas)wouldbeaccepted representation(COR)combinedwiththegameassetstoautomati-
aswithinthenormalrange,whereasscoresbelowthethreshold callygeneratevisualtestoracles(i.e.,oracleassets).Ourapproach
would indicate a visual bug is present. While the distributions thereforeassumesthatnobugsoriginateinthesepartsofthegame.
aresignificantlydifferentforallsimilaritymetrics,theeffectsizes Itisfairtoassumethattheassetsprovideaccuratebaselinesfor
showthatthereisalotofoverlapbetweenthemetricswhenusing comparisonwiththerenderedgameobjectsonthe<canvas>.In
thesnapshottestingapproach.Asaresult,athresholdismuch addition,itisfairtoassumethattheCORcanbeusedtogenerate
hardertoselectforsnapshottesting,andtherewillalwaysbea testoraclesfordetectingvisualbugs,asanybugpresentintheCOR
trade-offbetweenprecisionandrecall.Forourapproach,theeffect wouldnotbeavisualbug.
size(Table2)ismuchlargerindicatingthereisfarlessoverlap A threat to internal validity is our choice of background fill
betweenthedistributions,allowingustochoosebetter-performing colourwhenapplyingmasksduringimagepreprocessinginour
thresholds (which can also be observed from Figure 9). Clearly, experiments.Afillcolourmustbeselectedtofilltheblankspace
thereismuchmoreoverlapbetweennormalandbuggycaseswhen thatresultsfromthemaskingoperations.Toaddressthisthreat,we
usingsnapshottestingthanwhenusingourapproachwithanyof ranourexperimentswiththreedifferentfillcoloursin8-bitRGBA
thesimilaritymetrics. format:(0,0,0,255),(255,255,255,255),and(255,0,0,255).Weem-
piricallydeterminedthatforourtestgame,changingthefillcolour
6.2 Bugdetection formaskingonlyaffectedourresultswithembeddingsimilarity
(ESIM),indicatingthatouruseofESIMmaynotbeappropriatedue
Table3showstheresultsforbugdetectionwitheachevaluated
toourextensivepreprocessing.
approachandsimilaritymetric.Ourapproachachievesaconsid-
Athreattointernalvalidityisrelatedtohowwehandleassets
erablyhigheraccuracy(withanyofourfourevaluatedsimilarity
thathavepartialtransparencyinourexperiments.Inourexperi-
metrics)thansnapshottesting.Inparticular,ourapproachshows
ments,wechosetoremoveallpartialtransparency(i.e.,makeit
excitingpotentialfordetectingvisualbugswhenMSE,SSIM,or
fullytransparent),asweempiricallydeterminedthatthischoice
ESIMisusedasthesimilaritymetric.Ourresultsindicatethatonly
providedthebestperformance.However,thismeansthatwemay
asinglesimilaritymetricisneededforourapproach–combining
misssomevisualbugsthat(primarily)affectthepartiallytrans-
severalmetricsdoesnotimproveouroverallresults.
parentareasofanobjectonthe<canvas>.Moreworkisrequired
tobetterhandleassetswithpartialtransparencywhengenerating
6.3 Executionduration
masks.
Tobetterunderstandtheperformanceofourapproach,wetimed
theexecutionsofourapproachandthebaselineapproach.Our External validity. Our approach has only been evaluated with a
approachtookconsiderablylonger(3additionalsecondspersnap- single<canvas>game.Thresholdsfordetectingvisualbugswith
shot)torunthanthebaselineapproach.However,theaccuracyof ourapproachwillmostlikelydifferonaper-gamebasis,andnot
thebaselineapproachindicatesthatitisnotaveryusefulonein allgamesmayhaveasclearsimilaritythresholdsasthosefound
practice.Thebulkoftimeinourapproachisspentpreprocessing forourtestgame.Therefore,automaticallysettingthethresholds
theimages,whereascalculatingthesimilaritiesisrelativelyquick, todetectvisualbugsmaynotbeaseffectiveforother<canvas>
withtheexceptionofSSIM.Inpractice,wewouldnothavetocom- games,meaningmanualadjustmentmayberequired.Wedesigned
puteSSIM,becauseMSE,SSIM,andESIMprovidesimilaraccuracy ourtestgamewiththerandomnessandavarietyofanimationsthat
inourexperiments. wereinspiredbythevisualstylesandeffectsofindustrial<canvas>

AutomaticallyDetectingVisualBugsinHTML5<canvas>Games
Percentage Overlap Mean Squared Error Structural Similarity Embedding Similarity
| 1.0 |     |     | 7000 | Ground Truth |     |     | 1.0 |     | 1.0 |     |     |
| --- | --- | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- | --- |
okay
buggy
| 0.9 |     |     | 6000 |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
0.9
0.9
5000
0.8
|     |     |     | 4000 |     |     |     | 0.8 |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
0.8
0.7
3000
0.7
0.6
0.7
2000
| 0.5 |     |     |     |     |     |     | 0.6 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1000
0.6
| 0.4 | Ground Truth |          |     |          |          |     | Ground Truth |          |     | Ground Truth |     |
| --- | ------------ | -------- | --- | -------- | -------- | --- | ------------ | -------- | --- | ------------ | --- |
|     | okay         |          |     |          |          |     | 0.5 okay     |          |     | okay         |     |
|     | buggy        |          | 0   |          |          |     | buggy        |          |     | buggy        |     |
|     | Snapshot     | Our      |     | Snapshot | Our      |     | Snapshot     | Our      |     | Our Approach |     |
|     | Testing      | Approach |     | Testing  | Approach |     | Testing      | Approach |     |              |     |
Figure9:Boxplotsofsimilarityscoresforeachevaluatedsimilaritymetricineachapproach.Ourselectedthresholdsare
indicatedbythegreydottedlines.Similarityscoresinthegreyed-outrangesareclassifiedasnon-buggybyeachapproach.
Table3:Numberofrepetitions(outof10)eachvisualbugwasdetectedforeachapproachwitheachsimilaritymetric.As
detailedinSection5.4,weusethefollowingsimilaritymetrics:percentageoverlap(PCT),meansquarederror(MSE),structural
similarity(SSIM),andembeddingsimilarity(ESIM).
|      |     |                |     |     |     | SnapshotTesting |     | OurApproach |     |      |      |
| ---- | --- | -------------- | --- | --- | --- | --------------- | --- | ----------- | --- | ---- | ---- |
| Type | Key | BugDescription |     |     |     | PCT             | MSE | SSIM PCT    | MSE | SSIM | ESIM |
S1
|       |     | Vikingisinvisible.               |     |     |     |     | 1     | 0 0 | 10  | 10 10 | 10  |
| ----- | --- | -------------------------------- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- |
|       | S2  | Abackgroundhillisinvisible.      |     |     |     |     | 8     | 4 6 | 0   | 10 10 | 10  |
| etatS | S3  | Shipisinvisible.                 |     |     |     |     | 10 10 | 10  | 10  | 10 10 | 10  |
|       | S4  | Vikinganimationisnotupdating.    |     |     |     |     | 1     | 0 2 | 10  | 10 10 | 10  |
|       | S5  | Fallenloganimationisnotupdating. |     |     |     |     | 7     | 3 5 | 10  | 10 10 | 10  |
S6
|     |     | Buttonshouldbehidden.         |     |     |     |     | 5 10 | 8   | 0   | 10 10 | 10  |
| --- | --- | ----------------------------- | --- | --- | --- | --- | ---- | --- | --- | ----- | --- |
|     | A1  | Vikinghasthewrongbeardcolour. |     |     |     |     | 1    | 4 4 | 10  | 10 10 | 10  |
ecnaraeppA
|     | A2  | Entirevikinghasthewrongcolour.  |     |     |     |     | 2   | 7 3 | 10  | 10 10 | 10  |
| --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
|     | A3  | Vikingandlogsaregrey-scaled.    |     |     |     |     | 3   | 0 3 | 10  | 10 10 | 10  |
|     | A4  | Logshavethewrongcolour.         |     |     |     |     | 3   | 1 4 | 10  | 10 10 | 10  |
|     | A5  | Theship’ssailhasthewrongcolour. |     |     |     |     | 9   | 3 7 | 10  | 10 10 | 10  |
A6
|     |     | Abackgroundbunnyhasthewrongcolour. |     |     |     |     | 3     | 3 5 | 0   | 10 10 | 10  |
| --- | --- | ---------------------------------- | --- | --- | --- | --- | ----- | --- | --- | ----- | --- |
|     | L1  | Shipisinthewronglocation.          |     |     |     |     | 10 10 | 10  | 10  | 10 10 | 10  |
|     | L2  | Vikingisinthewronglocation.        |     |     |     |     | 2     | 2 2 | 10  | 10 10 | 10  |
tuoyaL
|     | L3  | Backgroundcloudsareinthewronglocation. |     |     |     |     | 10  | 5 3  | 10  | 10 10 | 10  |
| --- | --- | -------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | ----- | --- |
|     | L4  | Vikinghasthewrongrotation.             |     |     |     |     | 2   | 0 2  | 10  | 10 10 | 10  |
|     | L5  | Backgroundtreesareinthewronglayer.     |     |     |     |     | 8   | 7 10 | 10  | 10 10 | 10  |
|     | L6  | Logshavethewrongrotation.              |     |     |     |     | 2   | 1 1  | 10  | 10 10 | 10  |
|     | R1  | Vikingandlogsareverydistorted.         |     |     |     |     | 2   | 1 2  | 10  | 10 10 | 10  |
gniredneR R2 Vikingandlogsareslightlydistorted. 2 1 3 10 10 10 10
|          | R3  | Vikingandlogsareblurred.         |     |     |     |       | 2     | 0 0         | 10     | 10 10  | 10     |
| -------- | --- | -------------------------------- | --- | --- | --- | ----- | ----- | ----------- | ------ | ------ | ------ |
|          | R4  | Backgroundtreescoveredinpatches. |     |     |     |       | 7     | 8 8         | 0      | 10 10  | 10     |
|          | R5  | Backgroundbusheshaveartifacts.   |     |     |     |       | 2     | 0 2         | 0      | 10 10  | 10     |
|          | R6  | Backgroundbeachhastearing.       |     |     |     |       | 5     | 0 7         | 0      | 10 10  | 10     |
| Accuracy |     |                                  |     |     |     | 44.6% | 33.3% | 44.6% 75.0% | 100.0% | 100.0% | 100.0% |

FinlayMacklon,MohammadRezaTaesiri,MarkosViggiato,StefanAntoszko,NataliaRomanova,DalePaas,andCor-PaulBezemer
games. However, future studies should investigate further how ConferenceandSymposiumontheFoundationsofSoftwareEngineering,1093–
differentstylesofgamesimpacttheperformanceofourapproach. 1104.
[8] NormanCliff.1993.Dominancestatistics:ordinalanalysestoanswerordinal
Ourapproachisevaluatedonlya2D<canvas>gamethatwas
questions.Psychologicalbulletin,114,3,494.
builtwiththePixiJS<canvas>renderingframework.Morework [9] ParmidaDavarmanesh,KuanhaoJiang,TingtingOu,ArtemVysogorets,Stanislav
isrequiredtounderstandhowwellourapproachworksforother2D Ivashkevich,MaxKiehn,ShantanuHJoshi,andNicholasMalaya.2020.Au-
tomatingartifactdetectioninvideogames.arXivpreprintarXiv:2011.15103.
<canvas>games,3D<canvas>games,andnon-<canvas>games.
[10] HTML5GameDevs.2022.Forum-frameworks.Lastaccessed4May2022.
Inourexperimentsweleverageanexisting<canvas>objects (2022).https://www.html5gamedevs.com/forum/13-frameworks/.
representation(COR)providedbyPixiJS.IfaCORisnotavail- [11] AhmetMEskiciogluandPaulSFisher.1995.Imagequalitymeasuresandtheir
performance.IEEETransactionsoncommunications,43,12,2959–2965.
ableina<canvas>game,ourapproachwouldnotworkforthat [12] MohammadAminFazli,AliOwfi,andMohammadRezaTaesiri.2021.Under
game.Similarly,inourexperimentsweleverageexisting<canvas> theskinoffoundationNFTauctions.arXivpreprintarXiv:2109.12321.
[13] SteveFultonandJeffFulton.2013.HTML5canvas:nativeinteractivityand
gameassetstogeneratevisualtestoraclesduringthetest,butifa
animationfortheweb.O’ReillyMedia,Inc.
<canvas>gamedoesnotuseassetsforitsgraphicsrendering,then [14] KaimingHe,XiangyuZhang,ShaoqingRen,andJianSun.2015.Deepresidual
ourapproachwouldnotworkforthatgame. learningforimagerecognition.arxiv2015.arXivpreprintarXiv:1512.03385.
[15] AymanIssa,JonathanSillito,andVahidGarousi.2012.Visualtestingofgraphi-
Sometypesofgraphics(e.g.,skeletalanimations,particleeffects) caluserinterfaces:anexploratorystudytowardssystematicdefinitionsand
arenotinourtestgame,andarethereforenotaccountedforin approaches.In201214thIEEEInternationalSymposiumonWebSystemsEvolu-
tion(WSE).IEEE,11–15.
the implementation of our approach. More work is required to
[16] ArthurKamienskiandCor-PaulBezemer.2021.AnempiricalstudyofQ&A
understandhowourmethodperformswhenimplementedforother websitesforgamedevelopers.EmpiricalSoftwareEngineering,26,6,1–39.
typesofgraphicsthatarecommonin2D<canvas>games. [17] ChanhaKim,JadenKim,andJosephCOsborn.2020.Synthesizingretrogame
screenshotdatasetsforspritedetection.InAIIDEWorkshops.
[18] EvdokimosIKonstantinidis,GiorgosBamparopoulos,andPanagiotisDBamidis.
8 CONCLUSION 2016.Movingrealexergamingenginesontheweb:thewebFitForAllcase
studyinanactiveandhealthyageinglivinglabenvironment.IEEEjournalof
Inthispaper,wepresentanovelapproachforautomaticallydetect-
biomedicalandhealthinformatics,21,3,859–866.
ingvisualbugsin<canvas>games.Byleveragingthe<canvas> [19] ChrisLewis,JimWhitehead,andNoahWardrip-Fruin.2010.Whatwentwrong:
objectsrepresentation(COR),weareabletoautomaticallygen- ataxonomyofvideogamebugs.InProceedingsofthefifthinternationalconfer-
enceonthefoundationsofdigitalgames,108–115.
erate oracle assets for comparison with isolated object images [20] CarlosLing,KonradTollmar,andLinusGisslén.2020.Usingdeepconvolutional
(asrenderedtothe<canvas>)anddetectawidevarietyofvisual neuralnetworkstodetectrenderedglitchesinvideogames.InProceedingsofthe
bugsin<canvas>games.Wefoundthatourapproachfaroutper- AAAIConferenceonArtificialIntelligenceandInteractiveDigitalEntertainment
number1.Volume16,66–73.
formsthecurrentindustrystandardapproach(traditionalsnap- [21] ZijinLuo,MatthewGuzdial,NicholasLiao,andMarkRiedl.2018.Playerexpe-
shottesting)forautomaticallydetectingvisualbugsin<canvas> rienceextractionfromgameplayvideo.InFourteenthArtificialIntelligenceand
InteractiveDigitalEntertainmentConference.
games.Weevaluatedfoursimilaritymetricswithourapproach,
[22] ZijinLuo,MatthewGuzdial,andMarkRiedl.2019.Makingcnnsforvideo
and found that mean squared error (MSE), structural similarity parsingaccessible:eventextractionfromdota2gameplayvideousingtrans-
(SSIM),andembeddingsimilarity(ESIM)eachprovidedanaccu- fer,zero-shot,andnetworkpruning.InProceedingsofthe14thInternational
ConferenceontheFoundationsofDigitalGames,1–10.
racyof100%forour24injectedvisualbugs.Animplementation [23] FinlayMacklon,MarkosViggiato,NataliaRomanova,ChrisBuzon,DalePaas,
ofourapproachandourtestbedisavailableatthefollowinglink: andCor-PaulBezemer.2022.AtaxonomyofHTML5canvasbugs.arXivpreprint
arXiv:2201.07351.
https://github.com/asgaardlab/canvas-visual-bugs-testbed.
[24] HenryBMannandDonaldRWhitney.1947.Onatestofwhetheroneof
tworandomvariablesisstochasticallylargerthantheother.Theannalsof
ACKNOWLEDGMENTS mathematicalstatistics,50–60.
[25] DavoodMazinanian,MohammadBajammal,andAliMesbah.2021.Style-
TheresearchreportedinthisarticlehasbeensupportedbyProdigy guidedwebapplicationexploration.arXivpreprintarXiv:2111.12184.
Education and the Natural Sciences and Engineering Research [26] AniMohan.2020.GameSnacksbringsquick,casualgamestoanydevice.Last
accessed4May2022.(February2020).https://blog.google/technology/area-
CouncilofCanadaundertheAllianceGrantprojectALLRP550309.
120/gamesnacks-brings-quick-casual-games-any-device/.
[27] MaximMozgovoyandEvgenyPyshkin.2017.Unityapplicationtestingau-
REFERENCES tomationwithappiumandimagerecognition.InInternationalConferenceon
ToolsandMethodsforProgramAnalysis.Springer,139–150.
[1] FaragAlmansoury,SèglaKpodjedo,andGhizlaneElBoussaidi.2020.Investi- [28] EmersonMurphy-Hill,ThomasZimmermann,andNachiappanNagappan.
gatingWeb3DtopicsonStackOverflow:apreliminarystudyofWebGLand 2014.Cowboys,anklesprains,andkeepersofquality:howisvideogame
Three.js.InThe25thInternationalConferenceon3DWebTechnology,1–2. developmentdifferentfromsoftwaredevelopment?InProceedingsofthe36th
[2] MohammadBajammalandAliMesbah.2021.Pagesegmentationusingvisual InternationalConferenceonSoftwareEngineering,1–11.
adjacencyanalysis.arXivpreprintarXiv:2112.11975. [29] AlfredoNantes,RossBrown,andFredericMaire.2008.Aframeworkforthe
[3] MohammadBajammalandAliMesbah.2021.Semanticwebaccessibilitytesting semi-automatictestingofvideogames.InAIIDE.
viahierarchicalvisualanalysis.In2021IEEE/ACM43rdInternationalConference [30] TonyParisi.2014.Programming3DApplicationswithHTML5andWebGL:3D
onSoftwareEngineering(ICSE).IEEE,1610–1621. AnimationandVisualizationforWebPages.O’ReillyMedia,Inc.
[4] MohammadBajammalandAliMesbah.2018.Webcanvastestingthrough [31] TonyParisi.2012.WebGL:upandrunning.O’ReillyMedia,Inc.
visualinference.In2018IEEE11thInternationalConferenceonSoftwareTesting, [32] FábioPetrillo,MarceloPimenta,FranciscoTrindade,andCarlosDietrich.2009.
VerificationandValidation(ICST).IEEE,193–203. Whatwentwrong?asurveyofproblemsingamedevelopment.Computersin
[5] MohammadBajammal,AndreaStocco,DavoodMazinanian,andAliMesbah. Entertainment(CIE),7,1,1–22.
2020.Asurveyontheuseofcomputervisiontoimprovesoftwareengineering [33] Playco.2021.Playco,globalleaderininstantgames,acquiresGoodboyDigital,
tasks.IEEETransactionsonSoftwareEngineering. creatorsofPixiJS,thenumberoneHTML5gameengine.Lastaccessed5May
[6] JieshanChen,ChunyangChen,ZhenchangXing,XiweiXu,LimingZhut, 2022.(September2021).https://www.play.co/press/playco-official-press-
GuoqiangLi,andJinshuiWang.2020.Unblindyourapps:predictingnatural- release-210928-en?utm_sq=guxn7m9l5r.
languagelabelsformobileguicomponentsbydeeplearning.In2020IEEE/ACM [34] CristianoPolitowski,FabioPetrillo,GabrielCavalheiroUllmann,Josiasde
42ndInternationalConferenceonSoftwareEngineering(ICSE).IEEE,322–334. AndradeWerly,andYann-GaëlGuéhéneuc.2020.Datasetofvideogamedevel-
[7] KeChen,YufeiLi,YingfengChen,ChangjieFan,ZhipengHu,andWeiYang. opmentproblems.InProceedingsofthe17thInternationalConferenceonMining
2021.GLIB:towardsautomatedtestoracleforgraphically-richapplications.In SoftwareRepositories,553–557.
Proceedingsofthe29thACMJointMeetingonEuropeanSoftwareEngineering

AutomaticallyDetectingVisualBugsinHTML5<canvas>Games
[35] EdmarRezende,GuilhermeRuppert,TiagoCarvalho,FabioRamos,andPaulo [44] ZhouWangandAlanCBovik.2002.Auniversalimagequalityindex.IEEE
DeGeus.2017.Malicioussoftwareclassificationusingtransferlearningof signalprocessingletters,9,3,81–84.
resnet-50deepneuralnetwork.In201716thIEEEInternationalConferenceon [45] ZhouWang,AlanCBovik,HamidRSheikh,andEeroPSimoncelli.2004.
MachineLearningandApplications(ICMLA).IEEE,1011–1014. Imagequalityassessment:fromerrorvisibilitytostructuralsimilarity.IEEE
[36] FilippoRicca,AlessandroMarchetto,andAndreaStocco.2021.AI-basedtest transactionsonimageprocessing,13,4,600–612.
automation:agreyliteratureanalysis.In2021IEEEInternationalConferenceon [46] ThomasDWhite,GordonFraser,andGuyJBrown.2019.Improvingrandom
SoftwareTesting,VerificationandValidationWorkshops(ICSTW).IEEE,263–270. guitestingwithimage-basedwidgetdetection.InProceedingsofthe28thACM
[37] JeanineRomano,JeffreyDKromrey,JesseCoraggio,JeffSkowronek,andLinda SIGSOFTInternationalSymposiumonSoftwareTestingandAnalysis,307–317.
Devine.2006.Exploringmethodsforevaluatinggroupdifferencesonthensse [47] FengXue,JunshengWu,andTaoZhang.2022.Learning-replaybasedauto-
andothersurveys:arethet-testandcohen’sdindicesthemostappropriate matedrobotictestingformobileapp.MobileInformationSystems,2022.
choices.InannualmeetingoftheSouthernAssociationforInstitutionalResearch. [48] RahulkrishnaYandrapallyandAliMesbah.2021.Fragment-basedtestgenera-
Citeseer,1–51. tionforwebapps.arXivpreprintarXiv:2110.14043.
[38] DmitriySmirnov,MichaelGharbi,MatthewFisher,VitorGuizilini,Alexei [49] JiamingYe,KeChen,XiaofeiXie,LeiMa,RuochenHuang,YingfengChen,Yinx-
Efros,andJustinMSolomon.2021.Marionette:self-supervisedspritelearning. ingXue,andJianjunZhao.2021.AnempiricalstudyofGUIwidgetdetection
AdvancesinNeuralInformationProcessingSystems,34. forindustrialmobilegames.InProceedingsofthe29thACMJointMeetingon
[39] PatrickStaceyandJoeNandhakumar.2009.Atemporalperspectiveofthe EuropeanSoftwareEngineeringConferenceandSymposiumontheFoundations
computergamedevelopmentprocess.InformationSystemsJournal,19,5,479– ofSoftwareEngineering,1427–1437.
497. [50] ResaYogyaandRaymondKosala.2014.Comparisonofphysicsframeworks
[40] MohammadRezaTaesiri,MoslemHabibi,andMohammadAminFazli.2020.A forWebGL-basedgameengine.InEPJWebofConferences.Volume68.EDP
videogametestingmethodutilizingdeeplearning.IranJournalofComputer Sciences,00035.
Science,17,2. [51] RichardZhang,PhillipIsola,AlexeiAEfros,EliShechtman,andOliverWang.
[41] MohammadRezaTaesiri,FinlayMacklon,andCor-PaulBezemer.2022.CLIP 2018.Theunreasonableeffectivenessofdeepfeaturesasaperceptualmetric.
meetsGamePhysics:towardsbugidentificationingameplayvideosusing InProceedingsoftheIEEEconferenceoncomputervisionandpatternrecognition,
zero-shottransferlearning.In2022IEEE/ACM19thInternationalConferenceon 586–595.
MiningSoftwareRepositories(MSR).IEEE. [52] DehaiZhao,ZhenchangXing,ChunyangChen,XiweiXu,LimingZhu,Guo-
[42] MarkosViggiato,DalePaas,ChrisBuzon,andCor-PaulBezemer.2022.Identi- qiangLi,andJinshuiWang.2020.Seenomaly:vision-basedlintingofguiani-
fyingsimilartestcasesthatarespecifiedinnaturallanguage.IEEETransactions mationeffectsagainstdesign-don’tguidelines.In2020IEEE/ACM42ndInterna-
onSoftwareEngineering. tionalConferenceonSoftwareEngineering(ICSE).IEEE,1286–1297.
[43] MarkosViggiato,DalePaas,ChrisBuzon,andCor-PaulBezemer.2022.Using
naturallanguageprocessingtechniquestoimprovemanualtestcasedescrip-
tions.InInternationalConferenceonSoftwareEngineering-SoftwareEngineering
inPractice(ICSE-SEIP)Track.(May8,2022).