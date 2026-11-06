---
title: "RefGlitch Bench A Benchmark for Reference based Ga"
author: "Yu"
year: "2026"
source_file: "04_benchmarks_and_datasets/Yu_2026_RefGlitch_Bench_A_Benchmark_for_Reference_based_Ga.pdf"
source_sha256: "845576c79db39fc9cac5c002adfa82b4bba5a660b3bfd7a550bfd34912829f50"
converted_at: "2026-11-06T15:13:16.309750+00:00"
markitdown_version: "0.1.9"
char_count: 74713
---
RefGlitch-Bench: A Benchmark for Reference-based Gameplay Glitch Detection
|     |         |     | with Vision-Language |     |     | Models |                       |     |     |     |
| --- | ------- | --- | -------------------- | --- | --- | ------ | --------------------- | --- | --- | --- |
|     | YakunYu |     | AshleyWiens          |     |     |        | Adria´nBarahona-R´ıos |     |     |     |
UniversityofAlberta UniversityofAlberta SonyInteractiveEntertainment
|     |     | BenedictWilkins |     |     |     | SamanZadtootaghaj |     |     |     |     |
| --- | --- | --------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
6202 peS 51  ]VC.sc[  2v28011.4062:viXra
|     | SonyInteractiveEntertainment |                              |     |     | SonyInteractiveEntertainment |                     |     |     |     |     |
| --- | ---------------------------- | ---------------------------- | --- | --- | ---------------------------- | ------------------- | --- | --- | --- | --- |
|     |                              | NabajeetBarman               |     |     |                              | Cor-PaulBezemer     |     |     |     |     |
|     |                              | SonyInteractiveEntertainment |     |     |                              | UniversityofAlberta |     |     |     |     |
Abstract frequent content updates also introduce a steady stream of
|     |     |     |     |     | visualglitches. | Glitchessuchasclipping, |     |     | corruptedUIel- |     |
| --- | --- | --- | --- | --- | --------------- | ----------------------- | --- | --- | -------------- | --- |
Visual glitches in video games degrade player experience ements,andabnormallightingundermineperceivedquality
andperceivedquality,yetmanualqualityassurancecannot andplayertrust,andcantriggernegativereviews,refundre-
quests,andcostlycustomersupportinteractions[1,16,19].
| keep pace with | the growing | test surface | of modern | game |     |     |     |     |     |     |
| -------------- | ----------- | ------------ | --------- | ---- | --- | --- | --- | --- | --- | --- |
development. Prior automation efforts, particularly those Atthesametime,manualqualityassurance(QA)isbecom-
ingincreasinglycostlyandtime-consuming.Moderngames
| using vision-language |     | models (VLMs), | largely operate | on  |     |     |     |     |     |     |
| --------------------- | --- | -------------- | --------------- | --- | --- | --- | --- | --- | --- | --- |
isolated frames without sufficient context to judge whether ship frequent builds across platforms, hardware configura-
aglitchispresent.WeintroduceRefGlitch-Bench,abench- tions,andgraphicssettings,whichmakesexhaustivehuman
|                          |     |            |                  |      | review infeasible |     | and expands | the testing | surface | beyond |
| ------------------------ | --- | ---------- | ---------------- | ---- | ----------------- | --- | ----------- | ----------- | ------- | ------ |
| mark for reference-based |     | video game | glitch detection | with |                   |     |             |             |         |        |
VLMs. The key idea is to formulate glitch detection as what teams can reliably cover [5, 24, 26]. Together, these
an explicit within-video comparison problem: given a test pressures create a clear demand for accurate and scalable
frame, a reference frame provides a visual baseline that automatedgameplayglitchdetection.
helps the model distinguish true glitches from benign vi- Prior research on automated gameplay glitch detection,
sualvariation. RefGlitch-Benchincludesacontrolledsyn- particularly those using VLMs, has largely operated in a
thetic dataset with five injected glitch types and manually single-imagesetting: givenonescreenshot, themodelpre-
annotated reference/test frame pairs, enabling an oracle- dicts whether it contains a visual artifact [17, 20, 23, 25].
referenceevaluationthatisolatesthepotentialbenefitofref- This paradigm is inherently limited for accurate and con-
erenceguidance. Wefurtherestablishfourinitialbaselines textualQA.First,asingleimageoftenlackssufficientcon-
forautomaticallyselectingreferencesfromearlierframesin texttodistinguishtrueglitchesfrombenignvariation(e.g.,
thesamevideo, withLastCleanFrameperformingbestand camera motion or stylistic effects). Second, many glitches
transferring across VLMs. Finally, we evaluate automatic arerelativeortemporalinnature,andarethereforedifficult
reference guidance on real-world gameplay data, where it todiagnosefromasinglescreenshot. Forexample, GPT-5
improvesframe-levelglitchdetectionbeyondthecontrolled predictsthemissing-objecttestframeinFigure1asglitch-
settingwhilerevealingreferencereliabilityanderrorprop- freewhenevaluatedinisolation,becausethemissingrobot
| agationaskeychallenges. |     |     |     |     | armisnotobviouswithoutareference. |             |               |                    |        |               |
| ----------------------- | --- | --- | --- | --- | --------------------------------- | ----------- | ------------- | ------------------ | ------ | ------------- |
|                         |     |     |     |     | These                             | limitations | motivate      | a reference-guided |        | view of       |
|                         |     |     |     |     | gameplay                          | glitch      | detection.    | Rather than        | asking | a VLM to      |
|                         |     |     |     |     | judge a                           | test frame  | in isolation, | we formulate       |        | glitch detec- |
1.Introduction
|     |     |     |     |     | tionasanexplicitwithin-videocomparisonproblem: |     |     |     |     | given |
| --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | ----- |
Video games are the most widely consumed form of in- a test frame, the model is also provided with a reference
teractivemedia,buttheirincreasinglycomplexvisualsand framethatservesasanexpectedvisualbaseline. Intheex-
1

Missing Object
Reasoning (NoRef)
"Inspected the robot and surrounding catwalk. Its
Reference foot appears properly on the ground while the other
is mid-stride (not floating). No parts of the robot
intersect with rails, walls, or steps (no clipping). All
geometry is present, textures look consistent, and
lighting matches the industrial interior."
Reasoning (Ref)
"In the reference image the robot clearly has two
arms visible. In the test image the robot’s right arm
Test
(screen-right) is absent, with only the shoulder
socket visible and nothing occluding it. Other
scene elements match, so this indicates a missing
object rather than occlusion or lighting."
Clipping Floating Corrupted texture Lighting issue
Reference
Test
Figure1. Reference/testpairsfromthesyntheticRefGlitch-Benchdataset. Top: amissing-object(partsofacharacter/objectareunex-
pectedlyabsent)examplewithGPT-5’sjudgmentswith(Ref)andwithout(NoRef)areference. Bottom: pairedexamplesforclipping(a
character/objectintersectsorpassesthroughasolidsurface),floating(acharacter/objectisnotincontactwiththesurfaceitshouldrest
on),corruptedtexture(visiblybrokenorincorrectsurfacetexturing),andlightingissue(abnormalsceneilluminationnotexplainableby
anaturalchange).
ampleinFigure1, providingareferenceframewithanin- dering conditions and balanced coverage across glitch cat-
tact robot in a similar scene makes the discrepancy clear, egories. Crucially, it includes manually labeled refer-
allowingtheVLMtocorrectlydetectthemissingrightarm. ence/testframepairs,enablingcontrolledevaluationofref-
This design aligns with how humans often perform QA: erenceguidanceandperformingfine-grainedcategory-level
we identify visual failures by comparing the current scene analysis of which glitches benefit most from reference-
againstwhatthesameobject,lighting,geometry,orlayout basedcomparison.
shouldlooklikeundernormalgameplay. Moreover, exist-
The manually constructed pairs define an oracle-
ingbenchmarksdonotprovideapairedreference/teststruc-
referencecondition. Eachtestframeispairedwithaman-
tureneededtostudytheimpactofareferenceimage.
uallyselected,visuallyrelated,andverifiedglitch-freeref-
Therefore, we introduce RefGlitch-Bench, a bench- erence. This condition deliberately removes reference se-
markforreference-basedvideogameglitchdetectionwith lection error so that we can isolate the potential value of
VLMs. RefGlitch-Bench is a controlled synthetic dataset reference guidance itself. It should therefore be inter-
built from an open-source game environment with five in- preted as an empirical upper-bound condition under our
jected glitch types. Unlike existing multi-game bench- fixed single-reference evaluation protocol, rather than as a
marksthatmixdiversevisualstylesandprovidelimitedper- realistic deployment assumption or a solution to reference
category samples, RefGlitch-Bench offers consistent ren- selection. We then define an open automatic-reference-
2

selectionsettinginwhichamethodselectsareferencefrom multimodalreasoningproblem,buttheyprimarilyevaluate
earlier frames in the same video to aid the prediction of a glitches from isolated frames and therefore do not directly
test frame. We provide four initial baselines: LastClean- testwhetheradditionalvisualcontextimprovesdetection.
Frame, PreviousFrame, RandomFrame, and MostSimilar- Video-levelbenchmarksextendthissettingbyevaluating
Frame. Among these simple policies, LastCleanFrame, glitchesovergameplayclips,buttheyremaincomparatively
whichselectsthemostrecentprecedingframepredictedto limited. Severalapproaches[9,10,30]firstsegmentgame-
be glitch-free, performs best. Nevertheless, it remains be- playvideosusingauxiliarymetadatasuchasstreamercap-
low the oracle-reference condition and depends on poten- tions, andthenclassifysegmentsasglitchyornon-glitchy.
tiallyincorrectpredictionsaboutearlierframes. However, such metadata is often unavailable during game
We further evaluate automatic reference guidance on development. More recent benchmarks study gameplay
framesfromreal-worldgameplayvideos. Thisexperiment videos directly. PhysGame [4] focuses on physical com-
examines whether the frame-level benefits observed in the monsense violations in gameplay videos. VideoGameQA-
controlled benchmark transfer to more diverse visual con- Bench[27]includesvideo-levelglitchdetectionaspartofa
ditionsand,crucially,howthecorrectnessofaselectedref- broadervideogameQAbenchmark.TempGlitch[33]intro-
erence affects its corresponding test-frame prediction. In duces a controlled gameplay video benchmark specifically
summary,wemakethefollowingmajorcontributions: for temporal glitch detection. Together, these datasets ad-
• We introduce RefGlitch-Bench, a controlled benchmark vancevideo-basedgameplayunderstanding,buttheydonot
for reference-based frame-level gameplay glitch detec- explicitlyprovidepairedreference/testframesforstudying
tion,comprisingcompletesyntheticvideos,andbalanced whetheravisualbaselinehelpsglitchdetection.
reference/testpairs.Itcansupportfutureresearchonboth RefGlitch-Benchiscomplementarytothesebenchmarks.
improvedframe-levelreferenceselectionandtheseparate Ratherthanevaluatingmodelsonlyonisolatedscreenshots
problem of aggregating frame-level signals into reliable orunpairedframesequences,RefGlitch-Benchintroducesa
video-leveldecisions. reference-based setting in which each test frame is paired
• We define an oracle-reference condition that uses manu- with a reference frame from the same video. This de-
ally scene-matched and verified glitch-free references to signenablescontrolledanalysisofwhethervisuallyrelated
removereference-selectionerrorandisolatethepotential context helps VLMs distinguish true glitches from benign
effectofreferenceguidanceacrossvariousVLMs. scenevariation. Moreover,existingbenchmarksoftenspan
• We establish an open automatic-reference-selection set- many games and mix diverse visual styles. Their samples
ting, provide several initial baselines, and identify Last- withinanysinglegameenvironmentorglitchcategoryare
CleanFrame as the strongest among the simple policies also limited. In contrast, RefGlitch-Bench provides bal-
tested,whileretainingtheoracleconditionasanempiri- anced coverage across five glitch categories within a con-
calupperbound. sistent game environment, enabling fine-grained category-
• Weevaluateautomaticreferenceguidanceonframe-level levelanalysisofglitches.
examplesfromreal-worldgameplayvideosandquantify
how incorrect references propagate to subsequent frame 2.2.Vision-LanguageModelsforGameQA
predictions, identifying reliable reference retrieval and
VLMs have rapidly evolved from contrastive image–text
verificationascentralopenproblems.
pretraining [13, 15, 21, 34, 35] into instruction-following
multimodalassistants[6,7,14,36],withdownstreamadap-
2.RelatedWork
tationtypicallyachievedthroughpromptengineering[3,31,
32], instruction tuning [7, 14, 36], and parameter-efficient
2.1.GameplayGlitchDetectionBenchmarks
fine-tuning [11, 12]. Closed-source systems such as GPT-
Existing resources for gameplay glitch detection can be family models [22] and Gemini [29] demonstrate strong
broadly grouped into image-level and video-level bench- multimodalreasoningcapabilities,whileopen-weightfam-
marks. Image-level benchmarks evaluate whether mod- ilies such as Qwen-VL [2] and Ministral [18] provide in-
elscanidentifyvisualglitchesfromindividualscreenshots. creasingly competitive alternatives with lower deployment
For example, GlitchBench [25] introduced a benchmark cost. These capabilities have motivated growing interest
of glitch-free and glitchy screenshots from many games in applying VLMs to game QA, including glitch detec-
to evaluate whether large multimodal models can detect tion, and physical commonsense evaluation in gameplay
image-levelanomalies. VideoGameBunny[23]furtherex- videos. Despite this progress, current evidence suggests
pandsgame-imageunderstandingbyreleasingalarge-scale thatVLM-basedgameplayglitchdetectionremainsfarfrom
collectionofgameplayimagesandimage-instructionpairs solved. GlitchBench[25]andVideoGameBunny[23]show
acrosshundredsoftitles. Thesedatasetshaveplayedanim- that prompting-based methods can struggle with visual
portant role in establishing gameplay glitch detection as a glitchesacrossdiversegamesandscenes. VideoGameQA-
3

| Bench [27] | reports | substantial |     | headroom | for | video glitch |                     |     |                                       |     |     |     |
| ---------- | ------- | ----------- | --- | -------- | --- | ------------ | ------------------- | --- | ------------------------------------- | --- | --- | --- |
|            |         |             |     |          |     |              | Keyframe Extraction |     | Reference-guided Sequential Prompting |     |     |     |
detection,andPhysGame[4]showsthatevenstrongVLMs
Reference Pool
Gameplay Video
| have difficulty        |     | identifying | physical                     |     | commonsense | viola- |     |     |     |     |     |     |
| ---------------------- | --- | ----------- | ---------------------------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
| tionsingameplayvideos. |     |             | Thesefindingssuggestthatsim- |     |             |        |     |     |     |     | ... |     |
plyapplyinggeneral-purposeVLMstogameplaydataisin- Pred. Pred. Pred.
sufficientforrobustQAautomation.
Theselimitationspointtoanevaluationgap,ratherthan
FFmpeg
| solely a | modeling | gap. | RefGlitch-Bench |     | addresses | this |     |     |     |     |     |     |
| -------- | -------- | ---- | --------------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- |
gapwhileretainingaVLM-basedevaluationsettingbyin-
VLM
Pred.
| troducing   | a new           | dataset   | with        | manually  | selected  | reference      |     |     |     |     |     |     |
| ----------- | --------------- | --------- | ----------- | --------- | --------- | -------------- | --- | --- | --- | --- | --- | --- |
| frames for  | reference-based |           | evaluation. |           | It        | further estab- |     |     |     |     |     |     |
| lishes four | initial         | baselines | for         | automatic | reference | selec-         |     |     |     |     |     |     |
Keyframes
tion,providingafoundationforfutureworkonmoreeffec- Loop Over Keyframes
Reference Selection
tivereference-selectionstrategies.
|     |     |     |     |     |     |     |     | Reference Deposit |     |     | Final Prediction |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ---------------- | --- |
3.RefGlitch-BenchBenchmark
Figure2. Overviewofourautomaticreferenceselectionmethod
Existingbenchmarks[4,23,25,27]spanmanygames,ren- thatconsistsoftwostages. (1)Keyframeextraction: weextracta
|                              |     |        |            |            |                 |             | compact set         | of representative | frames. | (2)       | Reference-guided | se-       |
| ---------------------------- | --- | ------ | ---------- | ---------- | --------------- | ----------- | ------------------- | ----------------- | ------- | --------- | ---------------- | --------- |
| dering styles,               | and | camera | behaviors, |            | and they        | rarely pro- |                     |                   |         |           |                  |           |
|                              |     |        |            |            |                 |             | quential prompting: | we                | process | frames in | temporal         | order and |
| videexplicitreferenceframes. |     |        |            | Asaresult, | itisdifficultto |             |                     |                   |         |           |                  |           |
promptaVLMtopredictwhetherthecurrenttestframeisglitchy,
| isolate the | effect | of reference |     | guidance. | Moreover, | anal- |     |     |     |     |     |     |
| ----------- | ------ | ------------ | --- | --------- | --------- | ----- | --- | --- | --- | --- | --- | --- |
conditionedonanadditionalreferenceframeselectedfromaref-
| ysis across     | glitch | categories | is         | often | underpowered | due to        |                            |     |                                 |     |     |     |
| --------------- | ------ | ---------- | ---------- | ----- | ------------ | ------------- | -------------------------- | --- | ------------------------------- | --- | --- | --- |
|                 |        |            |            |       |              |               | erencepoolofearlierframes. |     | Eachstoredreferenceisassociated |     |     |     |
| limited samples |        | within     | any single | game. | To           | address these |                            |     |                                 |     |     |     |
withitspredictedlabel(“Pred.”);redarrowsdenotereferencese-
gaps, we introduce RefGlitch-Bench, a controlled bench- lectionandbluearrowsdenotedepositingnewlyprocessedframes
| markspecificallydesignedforreference-basedglitchdetec- |     |     |     |     |     |     | backintothepool. |     |     |     |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
tion,featuring(i)syntheticgameplayvideoswithmanually
annotatedreference/testframepairs,(ii)balancedcoverage
offiveglitchtypeswithinasingle,consistentgameenviron- remains active for several seconds. A few seconds before
|     |     |     |     |     |     |     | theend,thegamereturnstonormalbehavior. |     |     |     |     | Werecorded |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | ---------- |
ment,and(iii)fourinitialbaselinesforautomaticreference
selectionandreference-baseddetection. 100videosforeachglitchtype.Foreachvideo,wesampled
framesat5FPStocoverbothglitch-freeandglitchyinter-
| Concretely, |     | we used | the open-source |     | Godot | engine and |     |     |     |     |     |     |
| ----------- | --- | ------- | --------------- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
theThirdPersonShooter(TPS)demoassetasabaseenvi- vals. Twoannotatorsmanuallyconstructedthepairsbyfirst
ronment. We modified the source code to implement each identifyingatestframeinwhichthetargetglitchwasclearly
visibleoraclearlyglitch-freeframefornegativeexamples,
| glitch with | fast | in-engine | toggling | (See | the supplementary |     |     |     |     |     |     |     |
| ----------- | ---- | --------- | -------- | ---- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
material for implementation details), enabling recordings andthenselectingatemporallynearby, verifiedglitch-free
framefromthesamevideowithasimilarsceneconfigura-
| underthesamecameraandrenderingconditions. |     |     |     |     |     | Wegen- |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
eratedfiveglitchtypes: tionandaclearvisualcontrasttothetestframe. Following
thisprocedure,wecollected500pairswithaglitchand500
| 1. Missingobject: |     | partsofthecharacterorobjectareun- |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
withoutaglitch,yielding1,000pairedsamplesintotal.Fig-
expectedlymissing.
ure1showsexamplepairsforeachglitchtype.
| 2. Clipping:                      | a   | character | or  | object | visibly         | intersects or |     |     |     |     |     |     |
| --------------------------------- | --- | --------- | --- | ------ | --------------- | ------------- | --- | --- | --- | --- | --- | --- |
| passesthroughanothersolidsurface, |     |           |     |        | orgeometryover- |               |     |     |     |     |     |     |
4.AutomaticReferenceSelection
lapsinawaythatcouldnotoccurwithcorrectdepth/oc-
clusion.
|              |     |           |           |     |         |                | Manually   | selected reference | frames | establish |          | an informa- |
| ------------ | --- | --------- | --------- | --- | ------- | -------------- | ---------- | ------------------ | ------ | --------- | -------- | ----------- |
| 3. Floating: | a   | character | or object | is  | visibly | not in contact |            |                    |        |           |          |             |
|              |     |           |           |     |         |                | tive upper | bound on how       | much   | a visual  | baseline | can help    |
withthegroundorsurfaceitshouldberestingon,defy-
|     |     |     |     |     |     |     | gameplay | glitch detection, | but | selecting | references | manu- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- | --- | --------- | ---------- | ----- |
ingexpectedphysicsorgravity.
|     |     |     |     |     |     |     | allyisnotpracticalatscale. |     | Therefore,weestablishabase- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --------------------------- | --- | --- | --- |
4. Corrupted texture: a surface shows clearly broken or lineapproachforautomaticreferenceselectionthatallows
incorrecttexturing.
|                   |     |                    |     |     |         |          | VLMs to   | be evaluated   | on gameplay | videos |       | when manual  |
| ----------------- | --- | ------------------ | --- | --- | ------- | -------- | --------- | -------------- | ----------- | ------ | ----- | ------------ |
| 5. Lightingissue: |     | thescenelightingis |     |     | clearly | wrongand |           |                |             |        |       |              |
|                   |     |                    |     |     |         |          | reference | labels are not | available.  | As     | shown | in Figure 2, |
notexplainablebynaturalscenechange. the approach consists of two stages. First, we extract rep-
Werecordedgameplayvideosof5to18secondswithin- resentativekeyframesfromeachgameplayvideo. Second,
jectedglitches.Eachvideoclipstartswithnormalbehavior. we process keyframes sequentially and obtain frame-level
About one-third into the video, the glitch is triggered and glitchpredictionsviareference-guidedprompting.
4

Keyframe Extraction. Gameplay videos often contain Because PhysGame contains only glitchy clips, we
substantial frame-to-frame redundancy, making direct complemented it with 500 glitch-free videos from
dense-frame analysis inefficient and computationally ex- VideoGameQA-Bench. To match the size of our bench-
pensive. Tomakedetectiontractable,wereduceeachvideo mark,werandomlysampled87videosandannotated1,000
intoacompactsetofT keyframes. Specifically,weextract frames,comprising500glitchyand500glitch-freeframes.
I-frames (intra-coded frames) from the video using FFm- Annotatorsassignedabinarylabeltoeachframebasedon
peg [8]. I-frames are self-contained and can be decoded visible evidence: a frame was labeled glitchy only when a
independently,yieldingasparsesequenceofrepresentative glitch was visually present, and otherwise labeled glitch-
framesdeterminedbythevideo’sencodingsettings. free, even when it came from a video labeled positive by
PhysGame.
Reference-guided Sequential Prompting. Each
Evaluation Metrics. We evaluate glitch detection as a
keyframe is evaluated via reference-guided prompt-
binary classification task, where each frame is labeled as
ing, where the VLM judges the current frame using
glitchy or glitch-free. We report the performance using
contextual evidence from an earlier frame in the same
standardclassificationmetrics: accuracy,F1,precisionand
video. Specifically, foreachextractedkeyframe, weselect
recall. WeprimarilyuseaccuracyandF1asheadlinemet-
a reference frame from a reference pool that stores earlier
rics for model comparison. We report precision and re-
frames along with their predicted labels (“Pred.”) as
callnotasstandaloneoptimizationtargets,butasdiagnostic
illustrated in Figure 2. For the first frame I , the pool is
1
metricsthathelpinterpretperformancedifferences.
empty, so we use an adapted version of the prompt (see
the supplementary material) that takes a single frame and
askstheVLMtodeterminewhetherI containsanyglitch VLM Backbones and Compute. We evaluate five
1
evidence based solely on observable visual cues. Once VLMs, including two proprietary models and three open-
a prediction is produced, I and its predicted label are weight models. The proprietary models are GPT-5 [22]
1
depositedintothepool. Startingfromkeyframet ≥ 2,we andGemini3FlashPreview[29]. Theopen-weightmodels
perform reference-guided prompting. For each test frame are Qwen3-VL-8B [2], Ministral-3-8B [18], and Gemma-
I ,weselectareferenceframeR fromthepoolaccording 3-12B [28]. For proprietary models, we use the official
t t
to a reference selection policy (described in Section 6.2). APIs. For open-weight VLMs, we use the public Unsloth
WethenprompttheVLMwiththepair(R ,I ). TheVLM AI framework. All experiments with open-weight models
t t
outputs a frame-level prediction yˆ (glitchy vs. glitch-free) arerunon4NVIDIAL40SGPUs.
t
togetherwithabriefrationaledescribinghowthereference
6.Results
supportsthedecision.
Since a glitchy reference would otherwise mislead the 6.1.RQ1: Doesamanuallyselectedreferenceframe
model, the prompt is conditioned on R t ’s predicted status. improveframe-levelglitchdetection?
IfR ispredictedglitch-free,theVLMisinstructedtotreat
t
Motivation. Manygameplayglitchesaresubtleandeas-
itasanormalbaselineandflagvisualdiscrepanciesinI as
t
ilyconfusedwithbenignvisualvariations(e.g.,cameramo-
evidenceofaglitch. IfR ispredictedglitchy, theprompt
t
tion or changes in lighting). A matched reference frame
warns the model accordingly and asks it to judge whether
fromthesamevideoandsimilarscenecanprovideabase-
I also contains evidence of a glitch. After prediction, I
t t
line,enablingtheVLMtoattributemeaningful,unusualdif-
anditspredictedlabelaredepositedintothereferencepool
ferences to glitches rather than to normal gameplay varia-
(blue arrows in Figure 2), so that subsequent frames can
tion. RQ1askswhethersuchareferenceisusefulwhenthe
drawonareferencethatistemporallyclosetothem.
referenceitselfisreliable. Importantly, weformulateRQ1
asanoracle-referenceevaluationwhichprovidesanupper-
5.ExperimentalSetup
bound condition that isolates whether a VLM can benefit
Real-worldDataset. Toevaluatewhetherreferenceguid- fromarelevantvisualreferencewhenoneisavailable.
ance improves glitch detection under realistic QA condi-
tions, we further evaluated it on two state-of-the-art real- Design. We used RefGlitch-Bench to evaluate RQ1 un-
world gameplay video benchmarks: PhysGame [4] and dercontrolledconditions. Eachtestframeisevaluatedun-
VideoGameQA-Bench [27]. PhysGame targets physical der three prompting strategies: Ref (with a relevant refer-
commonsenseviolationsingameplayfootageandcontains enceframethatwasmanuallycherry-pickedfromasimilar
880videoswithglitchesfromdiversegames,spanningfour scene), NoRef (test frame only), and IrRef (with a refer-
domains(mechanics,kinematics,optics,andmaterialprop- enceframeunrelatedtotheevaluatedgameplayvideo,with
erties)across12physicalcommonsensecategories. nomeaningfulconnectiontothegame,scene,orobjects).
5

GPT−5 Gemini3 Flash Preview Qwen3−VL−8B Ministral−3−8B Gemma−3−12B
M i s s i n g M i s s i n g M i s s i n g M i s s i n g M i s s i n g
Floating 1.0 o b j e c t Floating 1.0 o b j e c t Floating 1.0 o b j e c t Floating 1.0 o b j e c t Floating 1.0 o b j e c t
|     | 0.8 |     |     | 0.8 |     | 0.8 |     |     | 0.8 |     |     |     | 0.8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | 0.6 |     |     | 0.6 |     | 0.6 |     |     | 0.6 |     |     |     | 0.6 |
|     | 0.4 |     |     | 0.4 |     | 0.4 |     |     | 0.4 |     |     |     | 0.4 |
|     | 0.2 |     |     | 0.2 |     | 0.2 |     |     | 0.2 |     |     |     | 0.2 |
G l it c h−Clipping G l it c h−Clipping G l it c h−Clipping G l it c h−Clipping G l it c h−
| Clipping |     | f r e e |     |     | f r e e |     | f r e e |     |     |     | f r e e |     | f r e e |
| -------- | --- | ------- | --- | --- | ------- | --- | ------- | --- | --- | --- | ------- | --- | ------- |
Corrupted Lighting Corrupted Lighting Corrupted Lighting Corrupted Lighting Corrupted Lighting
texture issue texture issue texture issue texture issue texture issue
|     |     |     |     |     | Ref | NoRef | IrRef |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- |
Figure3. Per-categorybehavioroftheVLMsvisualizedasradarplotsoversixclasses(Glitch-free,Missingobject,Clipping,Floating,
Corruptedtexture,Lightingissue),withlinescolor-codedbysettings.Pleasezoom-inforabetterview.
Model Setting Accuracy F1 Precision Recall minorviewpointorUIchanges)asevidenceofaglitch.
|       |     | Ref            | 0.77 | 0.74 | 0.87 0.64 |     |            |           |     |        |       |                   |     |
| ----- | --- | -------------- | ---- | ---- | --------- | --- | ---------- | --------- | --- | ------ | ----- | ----------------- | --- |
| GPT-5 |     | LastCleanFrame | 0.70 | 0.62 | 0.85 0.48 |     |            |           |     |        |       |                   |     |
|       |     | NoRef          | 0.65 | 0.49 | 0.88 0.34 |     |            |           |     |        |       |                   |     |
|       |     | IrRef          | 0.66 | 0.51 | 0.88 0.36 |     |            |           |     |        |       |                   |     |
|       |     |                |      |      |           |     | Irrelevant | reference |     | frames | often | hurt performance, |     |
|       |     | Ref            | 0.63 | 0.73 | 0.58 0.98 |     |            |           |     |        |       |                   |     |
LastCleanFrame 0.59 0.68 0.56 0.86 confirming that reference matching is critical. Table 1
Gemini3FlashPreview
NoRef 0.67 0.65 0.70 0.61 shows that for the smaller open models, IrRef is always
|     |     | IrRef | 0.68 | 0.65 | 0.72 0.60 |                       |     |     |                              |     |     |     |     |
| --- | --- | ----- | ---- | ---- | --------- | --------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- |
|     |     |       |      |      |           | worsethanthebaseline. |     |     | Forinstance,Qwen3-VL-8Bdrops |     |     |     |     |
|     |     | Ref   | 0.73 | 0.74 | 0.72 0.76 |                       |     |     |                              |     |     |     |     |
by-0.08accuracyand-0.23F1,drivenbya-0.17recallde-
| Qwen3-VL-8B |     | LastCleanFrame | 0.70 | 0.69 | 0.70 0.69 |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
NoRef 0.62 0.42 0.88 0.28 crease. Gemma-3-12B shows a similar pattern, with -0.07
|     |     | IrRef | 0.54 | 0.19 | 0.83 0.11 |          |     |           |         |          |         |       |          |
| --- | --- | ----- | ---- | ---- | --------- | -------- | --- | --------- | ------- | -------- | ------- | ----- | -------- |
|     |     |       |      |      |           | accuracy |     | and -0.34 | recall, | yielding | a large | -0.34 | F1 drop. |
Ref 0.68 0.58 0.83 0.45 Incontrast,GPT-5remainsrelativelystablefromNoRef to
|     |     | LastCleanFrame | 0.63 | 0.45 | 0.86 0.30 |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Ministral-3-8B
NoRef 0.57 0.35 0.73 0.23 IrRef,andGemini3FlashPreviewdoesnotdegrade. One
|     |     | IrRef | 0.50 | 0.03 | 0.44 0.02 |     |     |     |     |     |     |     |     |
| --- | --- | ----- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
plausiblereasonisthatstrongerinstruction-followingmod-
Ref 0.63 0.63 0.63 0.63 elscandown-weighttheirrelevantreferencewhenitisun-
|     |     | LastCleanFrame | 0.61 | 0.60 | 0.62 0.58 |     |     |     |     |     |     |     |     |
| --- | --- | -------------- | ---- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Gemma-3-12B NoRef 0.58 0.48 0.64 0.38 informative,whereasmorereference-dependentmodelsan-
IrRef 0.51 0.14 0.60 0.08 chortheirjudgmenttotheirrelevantreferenceandgetmis-
ledbyscene-inconsistentcomparisons.
| Table 1.             | Overall | performance under                   | different | reference | settings |     |     |     |     |     |     |     |     |
| -------------------- | ------- | ----------------------------------- | --------- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| acrossdifferentVLMs. |         | TheLastCleanFramesettingisdiscussed |           |           |          |     |     |     |     |     |     |     |     |
inRQ2.
Oraclereferenceguidanceimprovesdetectionacross
|           |        |           |          |          |         | all   | five glitch | types. | Figure | 3         | shows consistent |     | category-     |
| --------- | ------ | --------- | -------- | -------- | ------- | ----- | ----------- | ------ | ------ | --------- | ---------------- | --- | ------------- |
| Findings. | Oracle | reference | guidance | improves | overall |       |             |        |        |           |                  |     |               |
|           |        |           |          |          |         | level | benefits    | from   | Ref.   | Detection | improves         |     | for lighting, |
detection for most VLMs, with the largest gains in re- floating, clipping, and missing-object glitches in 5/5 mod-
| call. Table1showsthatRef |     | increasesrecallandF1forall |     |     |     |      |         |         |          |     |             |     |           |
| ------------------------ | --- | -------------------------- | --- | --- | --- | ---- | ------- | ------- | -------- | --- | ----------- | --- | --------- |
|                          |     |                            |     |     |     | els, | and for | texture | glitches | in  | 4/5 models; | the | remaining |
evaluatedmodels.Theimprovementisparticularlylargefor
|     |     |     |     |     |     | model | already | detects | 100% | of  | texture | glitches | both with |
| --- | --- | --- | --- | --- | --- | ----- | ------- | ------- | ---- | --- | ------- | -------- | --------- |
Qwen3-VL-8B,whichgains+0.11accuracyand+0.32F1, and without a reference. Lighting glitches exhibit particu-
| driven by | a +0.49 | increase in | recall. | Substantial | improve- |       |        |                |     |       |         |        |            |
| --------- | ------- | ----------- | ------- | ----------- | -------- | ----- | ------ | -------------- | --- | ----- | ------- | ------ | ---------- |
|           |         |             |         |             |          | larly | strong | and consistent |     | gains | because | subtle | global ap- |
mentsarealsoobservedformuchlargerproprietarymodels pearance changes can be difficult to identify from a single
| suchasGPT-5, |     | whichgains+0.12accuracyand+0.25F1, |     |     |     |       |     |        |      |         |               |     |           |
| ------------ | --- | ---------------------------------- | --- | --- | --- | ----- | --- | ------ | ---- | ------- | ------------- | --- | --------- |
|              |     |                                    |     |     |     | frame | but | become | more | salient | when compared |     | against a |
primarilyduetoa+0.30increaseinrecallwithonlya-0.01
|     |     |     |     |     |     | visual | baseline. | Floating |     | and clipping |     | also benefit | consis- |
| --- | --- | --- | --- | --- | --- | ------ | --------- | -------- | --- | ------------ | --- | ------------ | ------- |
changeinprecision. tentlybecauseascene-matchedreferencehelpsestablishthe
Gemini3FlashPreviewisthemainexceptionintermsof expected geometric and physical configuration of the en-
accuracy. AlthoughRef increasesitsrecallby+0.37,italso vironment. Improvements for texture and missing object
introducessubstantiallymorefalsepositives, resultingina glitches are somewhat less uniform because they depend
-0.04changeinaccuracy. Oneplausibleexplanationisthat more on whether the relevant object or material is visible
themodelover-emphasizesdiscrepanciesbetweentherefer- in both frames and on the model’s ability to perform fine-
enceandtestframesandinterpretsbenigndifferences(e.g., grainedvisualcomparisonundersmallviewpointchanges.
6

RQ1 takeaway: A manually selected reference provides an Strategy Accuracy F1 Precision Recall
oracleupperboundforreference-basedframe-levelglitchde-
|     |     |     |     |     |     |     |     | Ref |     |     | 0.73 | 0.74 | 0.72 | 0.76 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | ---- |
tection. Thisoracleconditionyieldsgainsofupto+0.32F1 LastCleanFrame 0.70 0.69 0.70 0.69
and+0.12accuracy.Category-wise,oraclereferencesimprove PreviousFrame 0.61 0.57 0.64 0.51
lighting,floating,clipping,andmissingobjectin5/5models, RandomFrame 0.67 0.66 0.68 0.63
|     |     |     |     |     |     |     |     | MostSimilarFrame |     |     | 0.60 | 0.54 | 0.64 | 0.47 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | ---- | ---- | ---- | ---- |
andimprovetexturein4/5models.
|          |                       |     |     |     |               |     |     | NoRef    |             |     | 0.62      | 0.42      | 0.88       | 0.28  |
| -------- | --------------------- | --- | --- | --- | ------------- | --- | --- | -------- | ----------- | --- | --------- | --------- | ---------- | ----- |
| 6.2.RQ2: | Amongsimplebaselines, |     |     |     | whichstrategy |     |     |          |             |     |           |           |            |       |
|          |                       |     |     |     |               |     |     | Table 2. | Performance | of  | reference | selection | strategies | using |
bestselectsareferenceframeautomatically?
|     |     |     |     |     |     |     |     | Qwen3-VL-8BonRefGlitch-Bench.Ref |     |     |     | denotesthemanuallyse- |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --------------------- | --- | --- |
lectedreferenceframeusedinSection6.1.
| Motivation. | RQ1establishesthatamanuallyselectedref- |     |         |             |     |        |        |     |     |     |     |     |     |     |
| ----------- | --------------------------------------- | --- | ------- | ----------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| erence can  | substantially                           |     | improve | frame-level |     | glitch | detec- |     |     |     |     |     |     |     |
tion,providinganoracleupperboundonthepotentialbene-
| fitofreferenceguidance. |     |     | However,suchmanuallyselected |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
references are not available in practical deployment. The object configuration, and animation state, while the clean-
remaining challenge is therefore to identify a useful refer- frame constraint makes the comparison more meaningful
ence automatically from earlier frames in the video. RQ2 fordetectingabnormalvisualchanges.
studiesthisproblembyestablishingfoursimpleautomatic
|     |     |     |     |     |     |     |     | In contrast, |     | PreviousFrame |     | performs | substantially |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------- | --- | -------- | ------------- | --- |
reference-selectionbaselinesandquantifyinghowmuchof
theoracle-referencebenefittheycanrecover. worse. Although the immediately previous frame is often
visuallysimilartothetestframe,temporaladjacencyalone
|             |                                             |         |     |                  |        |             |       | does not  | guarantee   | that           | the reference | is        | useful.   | The previ- |
| ----------- | ------------------------------------------- | ------- | --- | ---------------- | ------ | ----------- | ----- | --------- | ----------- | -------------- | ------------- | --------- | --------- | ---------- |
| Design.     | Weevaluatefourstrategiesforautomaticallyse- |         |     |                  |        |             |       |           |             |                |               |           |           |            |
|             |                                             |         |     |                  |        |             |       | ous frame | may         | itself contain |               | a glitch, | or may    | provide an |
| lecting     | a reference                                 | frame   | on  | RefGlitch-Bench: |        | (1)         | Last- |           |             |                |               |           |           |            |
|             |                                             |         |     |                  |        |             |       | ambiguous | comparison. |                | When          | both the  | reference | and test   |
| CleanFrame, | which                                       | selects |     | the most         | recent | glitch-free |       |           |             |                |               |           |           |            |
framescontainthesameabnormalpattern,theabnormality
| frame; (2) | PreviousFrame, |                  | which | selects |       | the immediately |        |              |              |     |        |           |           |     |
| ---------- | -------------- | ---------------- | ----- | ------- | ----- | --------------- | ------ | ------------ | ------------ | --- | ------ | --------- | --------- | --- |
|            |                |                  |       |         |       |                 |        | is no longer | contrastive, |     | making | the model | recognize | the |
| preceding  | frame;         | (3) RandomFrame, |       |         | which | samples         | a ref- |              |              |     |        |           |           |     |
erence randomly from earlier frames; and (4) MostSimi- glitch from the test frame itself rather than from a clean-
|           |                                            |         |       |     |               |     |         | versus-glitchy |          | comparison. | This | may    | explain   | why Previ- |
| --------- | ------------------------------------------ | ------- | ----- | --- | ------------- | --- | ------- | -------------- | -------- | ----------- | ---- | ------ | --------- | ---------- |
| larFrame, | whichselectsthevisuallymostsimilarprevious |         |       |     |               |     |         |                |          |             |      |        |           |            |
|           |                                            |         |       |     |               |     |         | ousFrame       | improves | recall      | over | NoRef, | but still | performs   |
| frame.    | We also                                    | include | NoRef | as  | the baseline, |     | and Ref |                |          |             |      |        |           |            |
farbelowLastCleanFrame.
| as the oracle | upper | bound. | All | strategies |     | use our | sequen- |     |     |     |     |     |     |     |
| ------------- | ----- | ------ | --- | ---------- | --- | ------- | ------- | --- | --- | --- | --- | --- | --- | --- |
tialpromptingoutputsfromearlierframestodecidewhich
|     |     |     |     |     |     |     |     | A particularly |     | surprising | result | is the | poor performance |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------- | ------ | ------ | ---------------- | --- |
frameistreatedasthereferenceframe.
ofMostSimilarFrame,suggestingthatselectingthevisually
| We first     | compare                                | these       | strategies |           | using | the Qwen3-VL- |     |              |          |        |            |              |              |           |
| ------------ | -------------------------------------- | ----------- | ---------- | --------- | ----- | ------------- | --- | ------------ | -------- | ------ | ---------- | ------------ | ------------ | --------- |
|              |                                        |             |            |           |       |               |     | most similar | previous | frame  | is         | insufficient | as an        | effective |
| 8B backbone. |                                        | This choice | is         | motivated | by    | practical     | QA  |              |          |        |            |              |              |           |
|              |                                        |             |            |           |       |               |     | reference.   | Although | visual | similarity |              | can retrieve | frames    |
| constraints: | videoanalysisoftenrequiresmanyVLMcalls |             |            |           |       |               |     |              |          |        |            |              |              |           |
withsimilarglobalappearance,objectlayout,orscenecon-
perclip,sodeployingalargeproprietarymodellikeGPT-5
|          |               |      |     |        |           |          |     | tent,itdoesnotguaranteethereferenceisclean. |     |     |     |     |     | Ifthemost |
| -------- | ------------- | ---- | --- | ------ | --------- | -------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --------- |
| is often | prohibitively | slow | and | costly | at scale. | Qwen3VL- |     |                                             |     |     |     |     |     |           |
similarframeisglitchy,orcontainsthesameartifactasthe
| 8B offers     | a more | realistic   | performance–cost |         |          | trade-off | for    |             |                                             |                |     |             |     |               |
| ------------- | ------ | ----------- | ---------------- | ------- | -------- | --------- | ------ | ----------- | ------------------------------------------- | -------------- | --- | ----------- | --- | ------------- |
|               |        |             |                  |         |          |           |        | test frame, | then                                        | the comparison |     | may provide |     | little useful |
| deployment,   | and    | it exhibits |                  | a large | benefit  | from      | refer- |             |                                             |                |     |             |     |               |
|               |        |             |                  |         |          |           |        | contrast.   | Moreover,visualsimilaritymeasuredbyageneric |                |     |             |     |               |
| ence guidance | in     | Table       | 1, making        | it      | a strong | backbone  | for    |             |                                             |                |     |             |     |               |
imageembeddingmaynotcapturethealignmentneededfor
| studying | how reference |     | selection | affects | downstream |     | per- |     |     |     |     |     |     |     |
| -------- | ------------- | --- | --------- | ------- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
glitchdetection,suchasmatchingthecorrectanimation,ob-
| formance. | After | identifying | the | strongest |     | baseline, | we ap- |     |     |     |     |     |     |     |
| --------- | ----- | ----------- | --- | --------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
jectstate,orlocalmotioncontext.
plyitsselectedreferencesacrossallVLMstoevaluatetheir
robustnessacrossmodels.
|           |                |     |     |          |      |       |     | LastCleanFrame |           | transfers |       | across VLM     | families,      | but       |
| --------- | -------------- | --- | --- | -------- | ---- | ----- | --- | -------------- | --------- | --------- | ----- | -------------- | -------------- | --------- |
|           |                |     |     |          |      |       |     | the oracle     | gap       | remains.  | After | selecting      | LastCleanFrame |           |
| Findings. | LastCleanFrame |     |     | performs | best | among | the |                |           |           |       |                |                |           |
|           |                |     |     |          |      |       |     | as the best    | automatic | baseline, |       | we re-evaluate |                | it across |
fourautomaticbaselines,butremainsbelowtheoracle- multiple VLMs in Table 1. LastCleanFrame improves F1
reference condition. Table 2 shows that LastCleanFrame relative to NoRef for all models and improves accuracy
outperforms PreviousFrame, RandomFrame, MostSimilar- for 4/5 models, indicating that its benefit transfers beyond
Frame, and NoRef on the Qwen3-VL-8B backbone. One theQwen3-VL-8Bbackboneusedforbaselinecomparison.
possiblereasonisthatLastCleanFramesatisfiestwoimpor- However,theremaininggapbetweenLastCleanFrameand
tant conditions for an effective reference: it is likely to be Ref reinforces the central benchmark challenge revealed
clean, and it is temporally close to the test frame. Tempo- by RQ2: automatically identifying a reference that is both
ralproximityhelpspreservescenelayout,cameraposition, cleanandrelevantremainsanopenproblem.
7

Strategy Accuracy F1 Precision Recall Group #Frames GT=1 GT=0 TPR FPR
LastCleanFrame 0.60 0.70 0.56 0.91 LastCleanFrame 1,000 500 500 0.91 0.71
NoRef 0.54 0.67 0.52 0.92 Hasareference 551 303 248 0.88 0.62
|     |     |     |     |     |     |     | Glitch-freereference |     |     | 367 | 156 | 211 | 0.94 0.58 |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --------- |
Table3.PerformanceofLastCleanFrameandNoRef ontheman- Glitchyreference 184 147 37 0.82 0.84
|     |     |     |     |     |     |     | Hasnoreference |     |     | 449 | 197 | 252 | 0.94 0.78 |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --------- |
uallylabeledreal-worldsubsetof1,000frames.
|     |     |     |     |     |     |     | Table 4. | Reference | reliability | analysis. |     | TPR is | measured on |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----------- | --------- | --- | ------ | ----------- |
glitchyframes,andFPRismeasuredonglitch-freeframes.
| RQ2 takeaway:  |            | Among          | four simple | automatic   |             | reference- |         |         |          |          |         |              |       |
| -------------- | ---------- | -------------- | ----------- | ----------- | ----------- | ---------- | ------- | ------- | -------- | -------- | ------- | ------------ | ----- |
| selection      | baselines, | LastCleanFrame |             | performs    | best        | and im-    |         |         |          |          |         |              |       |
| proves F1      | over       | NoRef for      | 5/5 VLMs    | and         | accuracy    | for 4/5    |         |         |          |          |         |              |       |
|                |            |                |             |             |             |            | provide | initial | evidence | that the | benefit | of reference | guid- |
| VLMs. Together |            | with the       | oracle      | upper bound | established | in         |         |         |          |          |         |              |       |
anceisnotconfinedtothecontrolledRefGlitch-Benchenvi-
RQ1,theseresultsidentifyreliablejointreferenceretrievaland
|     |     |     |     |     |     |     | ronment | and can | transfer | to gameplay |     | videos collected | in- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | -------- | ----------- | --- | ---------------- | --- |
verificationasanimportantopendirectionforfuturework.
dependentlyofoursyntheticgenerationprocedure.
|           |      |           |     |           |     |          | However, | automatically |     | selected | references |     | are imper- |
| --------- | ---- | --------- | --- | --------- | --- | -------- | -------- | ------------- | --- | -------- | ---------- | --- | ---------- |
| 6.3. RQ3: | Does | automatic |     | reference |     | guidance |          |               |     |          |            |     |            |
transfertoreal-worldgameplaydata? fect. As shown in Table 4, among the 1,000 evaluated
|     |     |     |     |     |     |     | frames, | 551 are | evaluated | with | a selected | reference, | while |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | --------- | ---- | ---------- | ---------- | ----- |
Motivation. RQ1 establishes the potential benefit of ref- 449havenoreferencebecausetheyareeitherthefirstframe
erenceguidanceunderanoraclecondition. RQ2theneval- or no prior frame has been predicted as glitch-free and
uates four initial strategies for obtaining such references is therefore available for reference selection. Among the
| automatically | on  | the controlled |     | RefGlitch-Bench |     | bench- |                           |     |     |        |     |               |         |
| ------------- | --- | -------------- | --- | --------------- | --- | ------ | ------------------------- | --- | --- | ------ | --- | ------------- | ------- |
|               |     |                |     |                 |     |        | 551 reference-conditioned |     |     | cases, | 367 | use a correct | glitch- |
mark,withLastCleanFrameemergingasthestrongestbase- free reference, whereas 184 use a wrong reference whose
line. RQ3 examines whether this benefit transfers beyond ground-truth label is glitchy, corresponding to a wrong-
| the controlled | benchmark |     | to real-world |     | gameplay | videos, |           |          |     |               |     |          |            |
| -------------- | --------- | --- | ------------- | --- | -------- | ------- | --------- | -------- | --- | ------------- | --- | -------- | ---------- |
|                |           |     |               |     |          |         | reference | use rate | of  | 33.4%. Hence, |     | although | LastClean- |
where visual conditions are less constrained, scene transi- Frame is effective, it introduces error propagation: frames
tionsaremorediverse,andsuitablereferencesmaybemore
thatareincorrectlypredictedasglitch-freearestoredinthe
difficult to identify. This setting also provides a natural referencepoolandusedasreferencesforlaterpredictions.
stress test of reference reliability. LastCleanFrame relies To assess how reference reliability affects downstream
onpredictionsfromearlierframesratherthanground-truth
prediction,wefurtherconductaclass-conditionedanalysis
labels:aframepredictedtobeglitch-freemayactuallycon- using true positive rate (TPR) on glitchy test frames and
tainaglitchandcansubsequentlybeselectedasareference.
|     |     |     |     |     |     |     | false positive | rate | (FPR) | on glitch-free |     | test frames. | For |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ---- | ----- | -------------- | --- | ------------ | --- |
Such errors may therefore propagate to later predictions. glitchytestframes,wrongreferencesreduceTPRfrom0.94
Weconsequentlyevaluateboththeoverallframe-levelben- to 0.82, indicating that glitchy references can make the
efitofautomaticreferenceguidanceandthedownstreamef-
|     |     |     |     |     |     |     | model less | sensitive | to  | actual glitches. |     | For glitch-free | test |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ---------------- | --- | --------------- | ---- |
fectofcorrectversusincorrectreferences. frames, wrong references increase FPR from 0.58 to 0.84,
|     |     |     |     |     |     |     | showing | that unreliable |     | references | can | also cause | normal |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------------- | --- | ---------- | --- | ---------- | ------ |
Design. Weevaluatethe1,000manuallyannotatedframes framestobemisclassifiedasglitchy. Together,theseresults
|          |            |         |       |     |             |       | demonstrate | that | reference | quality | directly | affects | down- |
| -------- | ---------- | ------- | ----- | --- | ----------- | ----- | ----------- | ---- | --------- | ------- | -------- | ------- | ----- |
| from our | real-world | dataset | under | two | conditions: | Last- |             |      |           |         |          |         |       |
CleanFrame and NoRef. To understand the reliability of streampredictionreliability.
| automatic | reference | selection, | we  | additionally |     | inspect the |               |     |           |           |          |           |     |
| --------- | --------- | ---------- | --- | ------------ | --- | ----------- | ------------- | --- | --------- | --------- | -------- | --------- | --- |
|           |           |            |     |              |     |             | RQ3 takeaway: |     | Automatic | reference | guidance | transfers | be- |
ground-truthlabelsofthereferencesselectedbyLastClean-
Frame after inference. This post-hoc analysis allows us yond RefGlitch-Bench, improving frame-level accuracy on
|     |     |     |     |     |     |     | real-worldgameplaydata. |     |     | However,itsreliabilitydependson |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------------------- | --- | --- | --- |
toquantifybothhowoftenautomaticselectionsuppliesan
thequalityoftheselectedreferences,identifyingreferencere-
| unreliable | reference | and | how such | reference | errors | affect |     |     |     |     |     |     |     |
| ---------- | --------- | --- | -------- | --------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
liabilityanderrorpropagationaskeyopenchallenges.
downstreamtest-framepredictions.
7.Conclusion
| Findings. | Automatic | reference |     | guidance | remains | use- |     |     |     |     |     |     |     |
| --------- | --------- | --------- | --- | -------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
ful on real-world data, although its effectiveness de- We introduced RefGlitch-Bench, a benchmark for
pends on reference reliability. As shown in Table 3, on reference-based glitch detection with VLMs. Our central
the manually labeled real-world subset, LastCleanFrame motivation is that many glitches are difficult to identify
achieves higher accuracy and F1 than NoRef. The im- from an isolated frame: a test frame may appear plausible
provement comes mainly from higher precision, while re- on its own but become clearly abnormal when compared
call remains comparable for both settings. These results with an appropriate visual reference. To study this setting
8

systematically, RefGlitch-Bench provides a controlled [8] FFmpegDevelopers. FFmpeg. https://ffmpeg.org/,2026. 5
synthetic dataset spanning five glitch types with manually [9] Emanuela Guglielmi, Simone Scalabrino, Gabriele Bavota,
annotated reference/test frame pairs, enabling an oracle- and Rocco Oliveto. Using gameplay videos for detecting
reference evaluation that isolates the potential benefit of issuesinvideogames. EmpiricalSoftwareEngineering,28
reference guidance. Across five VLMs, our experiments (6):136,2023. 3
|           |                   |     |           |         |             |     | [10] Emanuela |     | Guglielmi, | Gabriele | Bavota, | Rocco | Oliveto, and |
| --------- | ----------------- | --- | --------- | ------- | ----------- | --- | ------------- | --- | ---------- | -------- | ------- | ----- | ------------ |
| show that | oracle references |     | generally | improve | frame-level |     |               |     |            |          |         |       |              |
glitch detection. We further establish four initial baselines SimoneScalabrino. Automaticidentificationofgamestut-
|                |           |           |       |          |               |            | teringviagameplayvideosanalysis.           |     |     |     | ACMTransactionson |     |     |
| -------------- | --------- | --------- | ----- | -------- | ------------- | ---------- | ------------------------------------------ | --- | --- | --- | ----------------- | --- | --- |
| for automatic  | reference | selection |       | and find | that          | LastClean- |                                            |     |     |     |                   |     |     |
|                |           |           |       |          |               |            | SoftwareEngineeringandMethodology,34,2024. |     |     |     |                   |     | 3   |
| Frame performs | best,     | while     | still | leaving  | a substantial | gap        |                                            |     |     |     |                   |     |     |
[11] NeilHoulsby,AndreiGiurgiu,StanislawJastrzebski,Bruna
| totheoraclereferences. |     | Finally,experimentsonreal-world |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Morrone,QuentinDeLaroussilhe,AndreaGesmundo,Mona
gameplaydatashowthatautomaticreferenceguidancecan
|     |     |     |     |     |     |     | Attariyan, |     | and Sylvain | Gelly. | Parameter-efficient |     | transfer |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | ------ | ------------------- | --- | -------- |
improveframe-levelglitchdetectionbeyondthecontrolled
|     |     |     |     |     |     |     | learning | for | nlp. | In International | conference |     | on machine |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | ---------------- | ---------- | --- | ---------- |
synthetic setting, while also revealing reference reliability learning,pages2790–2799.PMLR,2019. 3
| and error | propagation | as              | key challenges. |     | Together,    | these |             |     |            |       |                 |        |        |
| --------- | ----------- | --------------- | --------------- | --- | ------------ | ----- | ----------- | --- | ---------- | ----- | --------------- | ------ | ------ |
|           |             |                 |                 |     |              |       | [12] Edward | J   | Hu, Yelong | Shen, | Phillip Wallis, | Zeyuan | Allen- |
| findings  | position    | RefGlitch-Bench |                 | as  | a foundation | for   |             |     |            |       |                 |        |        |
Zhu,YuanzhiLi,SheanWang,LiangWang,WeizhuChen,
future research on reference-based game QA. Promising etal. Lora: Low-rankadaptationoflargelanguagemodels.
directions include more reliable joint reference retrieval Iclr,1(2):3,2022. 3
| and verification, | conservative |     | reference-pool |     | management, |     |     |     |     |     |     |     |     |
| ----------------- | ------------ | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
[13] ChaoJia,YinfeiYang,YeXia,Yi-TingChen,ZaranaParekh,
and broader evaluation across diverse games, engines, HieuPham, QuocLe, Yun-HsuanSung, ZhenLi, andTom
glitchtypes,andvisualstyles. Duerig. Scaling up visual and vision-language representa-
|     |     |     |     |     |     |     | tion | learning | with | noisy text | supervision. | In  | International |
| --- | --- | --- | --- | --- | --- | --- | ---- | -------- | ---- | ---------- | ------------ | --- | ------------- |
conferenceonmachinelearning,pages4904–4916.PMLR,
References
|     |     |     |     |     |     |     | 2021. | 3   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
[1] Jessica Backus. Players’ perception of bugs and glitches [14] BruceWLee, HyunsooCho, andKangMinYoo. Instruc-
in video games: An exploratory study. arXiv preprint tiontuningwithhumancurriculum. InFindingsoftheAsso-
arXiv:2504.15408,2025. 1 ciationforComputationalLinguistics: NAACL2024,pages
[2] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, 1281–1309,2024. 3
Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei [15] Junnan Li, Ramprasaath Selvaraju, Akhilesh Gotmare,
Huang, et al. Qwen technical report. arXiv preprint Shafiq Joty, Caiming Xiong, and Steven Chu Hong Hoi.
arXiv:2309.16609,2023. 3,5 Alignbeforefuse:Visionandlanguagerepresentationlearn-
[3] Maciej Besta, Nils Blach, Ales Kubicek, Robert Gersten- ingwithmomentumdistillation. Advancesinneuralinfor-
berger,MichalPodstawski,LukasGianinazzi,JoannaGajda, mationprocessingsystems,34:9694–9705,2021. 3
Tomasz Lehmann, Hubert Niewiadomski, Piotr Nyczyk, [16] DayiLin,Cor-PaulBezemer,YingZou,andAhmedEHas-
etal. Graphofthoughts: Solvingelaborateproblemswith san. An empirical study of game reviews on the steam
largelanguagemodels. InProceedingsoftheAAAIconfer- platform. EmpiricalSoftwareEngineering,24(1):170–207,
| enceonartificialintelligence,pages17682–17690,2024. |     |     |     |     |     | 3   | 2019. | 1   |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
[4] Meng Cao, Haoran Tang, Haoze Zhao, Hangyu Guo, Jia- [17] CarlosLing,KonradTollmar,andLinusGissle´n.Usingdeep
convolutionalneuralnetworkstodetectrenderedglitchesin
| heng | Liu, Ge | Zhang, | Ruyang | Liu, Qiang | Sun, | Ian Reid, |     |     |     |     |     |     |     |
| ---- | ------- | ------ | ------ | ---------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- |
andXiaodanLiang. Physgame: Uncoveringphysicalcom- video games. In Proceedings of the AAAI Conference on
monsense violations in gameplay videos. arXiv preprint ArtificialIntelligenceandInteractiveDigitalEntertainment,
| arXiv:2412.01800,2024. |     |     | 3,4,5 |     |     |     | pages66–73,2020. |     |        | 1      |             |         |          |
| ---------------------- | --- | --- | ----- | --- | --- | --- | ---------------- | --- | ------ | ------ | ----------- | ------- | -------- |
|                        |     |     |       |     |     |     | [18] Alexander   |     | H Liu, | Kartik | Khandelwal, | Sandeep | Subrama- |
[5] KennethChang,BatuAytemiz,andAdamMSmith.Reveal-
more: Amplifyinghumaneffortinqualityassurancetesting nian, Victor Jouault, Abhinav Rastogi, Adrien Sade´, Alan
usingautomatedexploration. In2019IEEEConferenceon Jeffares, AlbertJiang, AlexandreCahill, AlexandreGavau-
Games(CoG),pages1–8.IEEE,2019. 1 dan, et al. Ministral 3. arXiv preprint arXiv:2601.08584,
|     |     |     |     |     |     |     | 2026. | 3,5 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
[6] ZheChen,JiannanWu,WenhaiWang,WeijieSu,GuoChen,
Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou Zhu, [19] WentaoLu,AlexanderSenchenko,AbramHindle,andCor-
LeweiLu,etal.Internvl:Scalingupvisionfoundationmod- Paul Bezemer. Automatedbug frame retrievalfrom game-
elsandaligningforgenericvisual-linguistictasks. InPro- play videos using vision-language models. arXiv preprint
ceedings of the IEEE/CVF conference on computer vision arXiv:2508.04895,2025. 1
andpatternrecognition,pages24185–24198,2024. 3 [20] Ciprian Paduraru. A state-aware, hierarchical deep learn-
[7] WenliangDai,JunnanLi,DongxuLi,AnthonyTiong,Junqi ing framework for automated visual glitch detection in
Zhao, Weisheng Wang, Boyang Li, Pascale N Fung, and games. Engineering Applications of Artificial Intelligence,
| Steven | Hoi. Instructblip: |     | Towards | general-purpose |     | vision- | 166:113497,2026. |     |     | 1   |     |     |     |
| ------ | ------------------ | --- | ------- | --------------- | --- | ------- | ---------------- | --- | --- | --- | --- | --- | --- |
languagemodelswithinstructiontuning.Advancesinneural [21] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya
informationprocessingsystems,36:49250–49267,2023. 3 Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,
9

Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen models for temporal glitch detection in gameplay videos.
Krueger, and Ilya Sutskever. Learning transferable visual arXivpreprintarXiv:2605.21443,2026. 3
modelsfromnaturallanguagesupervision. InProceedings [34] XiaohuaZhai,XiaoWang,BasilMustafa,AndreasSteiner,
ofthe38thInternationalConferenceonMachineLearning, Daniel Keysers, Alexander Kolesnikov, and Lucas Beyer.
pages8748–8763.PMLR,2021. 3 Lit: Zero-shot transfer with locked-image text tuning. In
[22] AadityaSingh,AdamFry,AdamPerelman,AdamTart,Adi Proceedings of the IEEE/CVF conference on computer vi-
Ganesh,AhmedEl-Kishky,AidanMcLaughlin,AidenLow, sionandpatternrecognition,pages18123–18133,2022. 3
AJOstrow, AkhilaAnanthram, etal. Openaigpt-5system [35] Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, and
card. arXivpreprintarXiv:2601.03267,2025. 3,5 LucasBeyer. Sigmoidlossforlanguageimagepre-training.
[23] Mohammad Reza Taesiri and Cor-Paul Bezemer. InProceedingsoftheIEEE/CVFinternationalconferenceon
Videogamebunny: Towards vision assistants for video computervision,pages11975–11986,2023. 3
games. In2025IEEE/CVFWinterConferenceonApplica- [36] ShengyuZhang,LinfengDong,XiaoyaLi,SenZhang,Xi-
tionsofComputerVision(WACV),pages1403–1413.IEEE, aofeiSun,ShuheWang,JiweiLi,RunyiHu,TianweiZhang,
2025. 1,3,4 Guoyin Wang, et al. Instruction tuning for large language
[24] Mohammad Reza Taesiri, Finlay Macklon, and Cor-Paul models: A survey. ACM Computing Surveys, 58(7):1–36,
Bezemer. Clipmeetsgamephysics: Towardsbugidentifica- 2026. 3
tioningameplayvideosusingzero-shottransferlearning.In
Proceedingsofthe19thInternationalConferenceonMining
SoftwareRepositories,pages270–281,2022. 1
[25] Mohammad Reza Taesiri, Tianjun Feng, Cor-Paul Beze-
mer,andAnhNguyen. Glitchbench: Canlargemultimodal
models detect video game glitches? In Proceedings of
theIEEE/CVFConferenceonComputerVisionandPattern
Recognition,pages22444–22455,2024. 1,3,4
[26] Mohammad Reza Taesiri, Finlay Macklon, Sarra Habchi,
and Cor-Paul Bezemer. Searching bug instances in game-
play video repositories. IEEE Transactions on Games, 16
(3):697–710,2024. 1
[27] Mohammad Reza Taesiri, Abhijay Ghildyal, Saman Zad-
tootaghaj, Nabajeet Barman, and Cor-Paul Bezemer.
VideogameQA-bench: Evaluating vision-language models
for video game quality assurance. In The Thirty-ninth An-
nualConferenceonNeuralInformationProcessingSystems
DatasetsandBenchmarksTrack,2025. 3,4,5
[28] GemmaTeam. Gemma3technicalreport,2025. 5
[29] Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-
BaptisteAlayrac,JiahuiYu,RaduSoricut,JohanSchalkwyk,
AndrewMDai,AnjaHauth,KatieMillican,etal.Gemini:a
familyofhighlycapablemultimodalmodels. arXivpreprint
arXiv:2312.11805,2023. 3,5
[30] Andrew Truelove, Shiyue Rong, Eduardo Santana de
Almeida, and Iftekhar Ahmed. Finding the needle in a
haystack: Detecting bug occurrences in gameplay videos.
arXivpreprintarXiv:2311.10926,2023. 3
[31] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al.
Chain-of-thought prompting elicits reasoning in large lan-
guage models. Advances in neural information processing
systems,35:24824–24837,2022. 3
[32] YakunYu,Shi-angQi,BaochunLi,andDiNiu.Peprec:Pro-
gressiveenhancementofpromptingforrecommendation. In
Proceedingsofthe2024ConferenceonEmpiricalMethods
inNaturalLanguageProcessing,pages17941–17953,2024.
3
[33] Yakun Yu, Ashley Wiens, Adria´n Barahona-R´ıos, Bene-
dict Wilkins, Saman Zadtootaghaj, Nabajeet Barman, and
Cor-PaulBezemer. Tempglitch: Evaluatingvision-language
10