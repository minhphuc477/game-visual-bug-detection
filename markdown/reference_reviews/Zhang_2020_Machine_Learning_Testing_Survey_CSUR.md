---
title: "Machine Learning Testing Survey CSUR"
author: "Zhang"
year: "2020"
source_file: "Zhang_2020_Machine_Learning_Testing_Survey_CSUR.pdf"
source_sha256: "5a97aa008639501b6b171309eb970bf58a00d31ab944e51b1afeb1018d6ee9b9"
converted_at: "2026-11-06T15:44:52.764601+00:00"
markitdown_version: "0.1.9"
char_count: 332483
---
1
|     |         |     | Machine |            | Learning     |     |     | Testing: |          |     |     |     |     |
| --- | ------- | --- | ------- | ---------- | ------------ | --- | --- | -------- | -------- | --- | --- | --- | --- |
|     | Survey, |     |         | Landscapes |              |     | and |          | Horizons |     |     |     |     |
|     |         |     | Jie     | M. Zhang*, | Mark Harman, |     | Lei | Ma, Yang | Liu      |     |     |     |     |
Abstract—Thispaperprovidesacomprehensivesurveyoftechniquesfortestingmachinelearningsystems;MachineLearningTesting
(MLtesting)research.Itcovers144papersontestingproperties(e.g.,correctness,robustness,andfairness),testingcomponents
(e.g.,thedata,learningprogram,andframework),testingworkflow(e.g.,testgenerationandtestevaluation),andapplicationscenarios
(e.g.,autonomousdriving,machinetranslation).Thepaperalsoanalysestrendsconcerningdatasets,researchtrends,andresearch
focus,concludingwithresearchchallengesandpromisingresearchdirectionsinMLtesting.
9102 ceD 12  ]GL.sc[  2v24701.6091:viXra
IndexTerms—machinelearning,softwaretesting,deepneuralnetwork,
(cid:70)
1 INTRODUCTION
The prevalent applications of machine learning arouse inherently follows a data-driven programming paradigm,
natural concerns about trustworthiness. Safety-critical ap- wherethedecisionlogicisobtainedviaatrainingprocedure
plications such as self-driving systems [1], [2] and medical from training data under the machine learning algorithm’s
treatments[3],increasetheimportanceofbehaviourrelating architecture [8]. The model’s behaviour may evolve over
to correctness, robustness, privacy, efficiency and fairness. time, in response to the frequent provision of new data [8].
Software testing refers to any activity that aims to detect While this is also true of traditional software systems, the
thedifferencesbetweenexistingandrequiredbehaviour[4]. core underlying behaviour of a traditional system does not
With the recent rapid rise in interest and activity, testing typicallychangeinresponsetonewdata,inthewaythata
has been demonstrated to be an effective way to expose machinelearningsystemcan.
problemsandpotentiallyfacilitatetoimprovethetrustwor- Testingmachinelearningalsosuffersfromaparticularly
thinessofmachinelearningsystems. perniciousinstanceoftheOracleProblem[9].Machinelearn-
For example, DeepXplore [1], a differential white-box ing systems are difficult to test because they are designed
testing technique for deep learning, revealed thousands of to provide an answer to a question for which no previous
incorrect corner case behaviours in autonomous driving answer exists [10]. As Davis and Weyuker said [11], for
|          |          |        |        |                  |           | these | kinds | of systems |     | ‘There would | be  | no need | to write |
| -------- | -------- | ------ | ------ | ---------------- | --------- | ----- | ----- | ---------- | --- | ------------ | --- | ------- | -------- |
| learning | systems; | Themis | [5], a | fairness testing | technique |       |       |            |     |              |     |         |          |
fordetectingcausaldiscrimination,detectedsignificantML such programs, if the correct answer were known’. Much
modeldiscriminationtowardsgender,maritalstatus,orrace of the literature on testing machine learning systems seeks
tofindtechniquesthatcantackletheOracleproblem,often
forasmanyas77.2%oftheindividualsindatasetstowhich
| itwasapplied. |     |     |     |     |     | drawingontraditionalsoftwaretestingapproaches. |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Infact,someaspectsofthetestingproblemformachine Thebehavioursofinterestformachinelearningsystems
arealsotypifiedbyemergentproperties,theeffectsofwhich
| learning | systems | are shared | with | well-known | solutions |     |     |     |     |     |     |     |     |
| -------- | ------- | ---------- | ---- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
already widely studied in the software engineering literat- can only be fully understood by considering the machine
ure.Nevertheless,thestatisticalnatureofmachinelearning learning system as a whole. This makes testing harder,
|         |           |         |         |            |           | because | it  | is less | obvious | how to | break | the system | into |
| ------- | --------- | ------- | ------- | ---------- | --------- | ------- | --- | ------- | ------- | ------ | ----- | ---------- | ---- |
| systems | and their | ability | to make | autonomous | decisions |         |     |         |         |        |       |            |      |
raise additional, and challenging, research questions for smallercomponentsthatcanbetested,asunits,inisolation.
softwaretesting[6],[7]. From a testing point of view, this emergent behaviour has
|          |               |           |       |            |              | a tendency |        | to migrate  |     | testing challenges |        | from         | the unit |
| -------- | ------------- | --------- | ----- | ---------- | ------------ | ---------- | ------ | ----------- | --- | ------------------ | ------ | ------------ | -------- |
| Machine  | learning      | testing   | poses | challenges | that arise   |            |        |             |     |                    |        |              |          |
|          |               |           |       |            |              | level      | to the | integration |     | and system         | level. | For example, | low      |
| from the | fundamentally | different |       | nature and | construction |            |        |             |     |                    |        |              |          |
of machine learning systems, compared to traditional (rel- accuracy/precisionofamachinelearningmodelistypically
|              |               |     |          |                           |     | a composite |     | effect, | arising | from a | combination | of  | the be- |
| ------------ | ------------- | --- | -------- | ------------------------- | --- | ----------- | --- | ------- | ------- | ------ | ----------- | --- | ------- |
| atively more | deterministic |     | and less | statistically-orientated) |     |             |     |         |         |        |             |     |         |
havioursofdifferentcomponentssuchasthetrainingdata,
| software | systems. | For instance, | a   | machine learning | system |     |     |     |     |     |     |     |     |
| -------- | -------- | ------------- | --- | ---------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
thelearningprogram,andeventhelearningframework/lib-
rary[8].
•
Jie M. Zhang and Mark Harman are with CREST, University College Errors may propagate to become amplified or sup-
London,UnitedKingdom.MarkHarmanisalsowithFacebookLondon.
E-mail:jie.zhang,mark.harman@ucl.ac.uk pressed, inhibiting the tester’s ability to decide where the
*JieM.Zhangisthecorrespondingauthor. fault lies. These challenges also apply in more traditional
|     |     |     |     |     |     | software |     | systems, | where, | for example, |     | previous work | has |
| --- | --- | --- | --- | --- | --- | -------- | --- | -------- | ------ | ------------ | --- | ------------- | --- |
•
LeiMaiswithKyushuUniversity,Japan.
E-mail:malei@ait.kyushu-u.ac.jp considered failed error propagation [12], [13] and the sub-
|     |     |     |     |     |     | tleties | introduced |     | by fault | masking | [14], | [15]. However, |     |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | -------- | ------- | ----- | -------------- | --- |
• YangLiuiswithNanyangTechnologicalUniversity,Singapore. these problems are far-reaching in machine learning sys-
E-mail:yangliu@ntu.edu.sg tems, since they arise out of the nature of the machine

2
learningapproachandfundamentallyaffectallbehaviours,
rather than arising as a side effect of traditional data and
controlflow[8].
For these reasons, machine learning systems are thus
sometimes regarded as ‘non-testable’ software. Rising to
these challenges, the literature has seen considerable pro-
gressandanotableupturnininterestandactivity:Figure1
shows the cumulative number of publications on the topic
oftestingmachinelearningsystemsbetween2007andJune
2019 (we introduce how we collected these papers in Sec-
tion 4.2). From this figure, we can see that 85% of papers
have appeared since 2016, testifying to the emergence of
new software testing domain of interest: machine learning
testing.
144
118
47
21
2 3 5 5 6 8 8 9 12
Year
snoitacilbup
gnitset
LM
fo
rebmuN
papers, we mention them in all the aspects correlated (in
differentsections).Thisensuresthateachaspectiscomplete.
Additionally, we summarise research distribution (e.g.,
among testing different machine learning categories),
trends, and datasets. We also identify open problems and
challenges for the emerging research community working
at the intersection between techniques for software testing
and problems in machine learning testing. To ensure that
oursurveyisself-contained,weaimedtoincludesufficient
material to fully orientate software engineering researchers
who are interested in testing and curious about testing
techniques for machine learning applications. We also seek
to provide machine learning researchers with a complete
surveyofsoftwaretestingsolutionsforimprovingthetrust-
worthinessofmachinelearningsystems.
There has been previous work that discussed or sur-
150
veyedaspectsoftheliteraturerelatedtoMLtesting.Hainset
al.[21],Maetal.[22],andHuangetal.[23]surveyedsecure
deeplearning,inwhichthefocuswasdeeplearningsecurity
withtestingbeingoneoftheassurancetechniques.Masuda
100
etal.[24]outlinedtheircollectedpapersonsoftwarequality
for machine learning applications in a short paper. Ishi-
kawa [25] discussed the foundational concepts that might
50 be used in any and all ML testing approaches. Braiek and
Khomh[26]discusseddefectdetectioninmachinelearning
data and/or models in their review of 39 papers. As far as
weknow,nopreviousworkhasprovidedacomprehensive
0
2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 surv
In
ey
su
p
m
ar
m
tic
a
u
r
l
y
a
,
rl
t
y
he
fo
p
cu
ap
se
e
d
r
o
m
n
a
m
ke
a
s
ch
th
in
e
e
f
l
o
e
l
a
lo
rn
w
in
in
g
g
te
c
s
o
t
n
in
t
g
ri
.
bu-
tions:
1)Definition.ThepaperdefinesMachineLearningTest-
Figure 1: Machine Learning Testing Publications (accumu- ing (ML testing), overviewing the concepts, testing work-
lative)during2007-2019 flow, testing properties, and testing components related to
machinelearningtesting.
Inthispaper,weusetheterm‘Machine Learning Test- 2) Survey. The paper provides a comprehensive sur-
ing’ (ML testing) to refer to any activity aimed at detect- vey of 144 machine learning testing papers, across various
ing differences between existing and required behaviours publishing areas such as software engineering, artificial
of machine learning systems. ML testing is different from intelligence,systemsandnetworking,anddatamining.
testing approaches that use machine learning or those that 3) Analyses. The paper analyses and reports data on
are guided by machine learning, which should be referred the research distribution, datasets, and trends that charac-
to as ‘machine learning-based testing’. This nomenclature terise the machine learning testing literature. We observed
accords with previous usages in the software engineering a pronounced imbalance in the distribution of research
literature. For example, the literature uses the terms ‘state- efforts: among the 144 papers we collected, around 120
based testing’ [16] and ‘search-based testing’ [17], [18] to of them tackle supervised learning testing, three of them
refertotestingtechniquesthatmakeuseofconceptsofstate tackle unsupervised learning testing, and only one paper
and search space, whereas we use the terms ‘GUI testing’ testsreinforcementlearning.Additionally,mostofthem(93)
[19] and ‘unit testing’ [20] to refer to test techniques that centreoncorrectnessandrobustness,butonlyafewpapers
tacklechallengesoftestingGUIs(GraphicalUserInterfaces) testinterpretability,privacy,orefficiency.
andcodeunits. 4)Horizons.Thepaperidentifieschallenges,openprob-
This paper seeks to provide a comprehensive survey lems,andpromisingresearchdirectionsforMLtesting,with
of ML testing. We draw together the aspects of previous theaimoffacilitatingandstimulatingfurtherresearch.
work that specifically concern software testing, while sim- Figure2depictsthepaperstructure.Moredetailsofthe
ultaneously covering all types of approaches to machine reviewschemacanbefoundinSection4.
learning that have hitherto been tackled using testing. The
literature is organised according to four different aspects:
2 PRELIMINARIES OF MACHINE LEARNING
the testing properties (such as correctness, robustness, and
fairness), machine learning components (such as the data, This section reviews the fundamental terminology in ma-
learning program, and framework), testing workflow (e.g., chinelearningsoastomakethesurveyself-contained.
testgeneration,testexecution,andtestevaluation),andap- Machine Learning (ML) is a type of artificial intelli-
plication scenarios (e.g., autonomous driving and machine gence technique that makes decisions or predictions from
translation).Somepapersaddressmultipleaspects.Forsuch data [27], [28]. A machine learning system is typically

3
|     |     |     | Preliminaries of  |     |     |     | ingdata,thelearningprogram,andframeworks. |     |     |     |     |     |     |     |
| --- | --- | --- | ----------------- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Definition
Machine  There are different types of machine learning. From the
|     |     |     | Learning | Comparison with software testing  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Introduction
of MLT How to test: MLT workflow perspective of training data characteristics, machine learn-
|     |     |     | C o n t e n ts  of  | Where to test: MLT components |     |     |              |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------- | ----------------------------- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | M a c h in e        |                               |     |     | ingincludes: |     |     |     |     |     |     |     |
What to test: MLT properties
Learning  Supervisedlearning:atypeofmachinelearningthatlearns
Testing
Test input generation
|     |     |     |     |     |     |     | from training |     | data with | labels | as  | learning | targets. | It is the |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ------ | --- | -------- | -------- | --------- |
Test oracle generation
mostwidelyusedtypeofmachinelearning[34].
Test adequacy evaluation
|     |     |     | Testing   |                                   |     |     | Unsupervisedlearning:alearningmethodologythatlearns |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --------------------------------- | --- | --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     | workflow  | Test prioritisation and reduction |     |     |                                                     |     |     |     |     |     |     |     |
(how to test)
Bug report analysis fromtrainingdatawithoutlabelsandreliesonunderstand-
|     |     |     |          | Debug and repair |     |     | ingthedataitself. |     |                                      |     |     |     |     |     |
| --- | --- | --- | -------- | ---------------- | --- | --- | ----------------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
|     |     |     |          |                  |     |     | Reinforcement     |     | learning:atypeofmachinelearningwhere |     |     |     |     |     |
|     |     |     | Testing  | Data testing     |     |     |                   |     |                                      |     |     |     |     |     |
components  Learning program testing the data are in the form of sequences of actions, observa-
| M a c h i n e |   W a y s  o | f   | ( w h e re to  |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
L e a r n i n g   te s t ) Framework testing tions, and rewards, and the learner learns how to take ac-
Or g a n is i ng
Testing Related  tionstointeractinaspecificenvironmentsoastomaximise
|     | Work |     |     | Correctness     |     |     |                      |     |     |     |     |     |     |     |
| --- | ---- | --- | --- | --------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |      |     |     | Model Relevance |     |     | thespecifiedrewards. |     |     |     |     |     |     |     |
Testing
properties  Robustness&Security Let X = (x 1 ,...,x m ) be the set of unlabelled training
(what to test) Efficiency data. Let Y = (c(x ),...,c(x )) be the set of labels cor-
|     |     |     |     |          |     |     |            |     | 1          |     | m        |      |     |             |
| --- | --- | --- | --- | -------- | --- | --- | ---------- | --- | ---------- | --- | -------- | ---- | --- | ----------- |
|     |     |     |     | Fairness |     |     |            |     |            |     |          |      | x   |             |
|     |     |     |     |          |     |     | responding | to  | each piece | of  | training | data | i.  | Let concept |
Interpretability
|     |     |     |     |     |     |     | C : X | → Y bethemappingfromX |     |     |     | toY | (therealpattern). |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------------------- | --- | --- | --- | --- | ----------------- | --- |
Privacy
|     |     |     |     |     |     |     | The task | of  | supervised | learning |     | is to | learn | a mapping |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | -------- | --- | ----- | ----- | --------- |
Autonomous driving pattern,i.e.,amodel,hbasedonX andYsothatthelearned
Application
|     |     |     | Scenario | Machine translation |     |     |       | h          |     |          |         | C   |      |              |
| --- | --- | --- | -------- | ------------------- | --- | --- | ----- | ---------- | --- | -------- | ------- | --- | ---- | ------------ |
|     |     |     |          |                     |     |     | model | is similar | to  | its true | concept |     | with | a very small |
Natural language inference
generalisationerror.Thetaskofunsupervisedlearningisto
|     |     |     |     |     |     |     | learn | patterns | or clusters | from | the | data | without | knowing |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ----------- | ---- | --- | ---- | ------- | ------- |
Machine learning categories
|     | Analysis  |     | Machine learning properties |     |     |     | theexistenceoflabelsY. |     |     |     |     |     |     |     |
| --- | --------- | --- | --------------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
and
|     | Comparison |     | Data sets |     |     |     |               |     |          |     |        |     |       |          |
| --- | ---------- | --- | --------- | --- | --- | --- | ------------- | --- | -------- | --- | ------ | --- | ----- | -------- |
|     |            |     |           |     |     |     | Reinforcement |     | learning |     | guides | and | plans | with the |
Open-source tools
learneractivelyinteractingwiththeenvironmenttoachieve
Research
Directions
|     |     |     |     |     |     |     | a certain | goal. | It is usually |     | modelled | as   | a Markov | decision    |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------------- | --- | -------- | ---- | -------- | ----------- |
|     |     |     |     |     |     |     | process.  | Let S | be a set      | of  | states,  | A be | a series | of actions. |
Figure2:Treestructureofthecontentsinthispaper
|     |     |     |     |     |     |     | Let s and | s(cid:48) be | two states. |     | Let r (s,s(cid:48)) |     | be the | reward after |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ----------- | --- | ------------------- | --- | ------ | ------------ |
a
|     |     |     |     |     |     |     |            |      | s   | s(cid:48) |        | a ∈ | A.            |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | --- | --------- | ------ | --- | ------------- | --- |
|     |     |     |     |     |     |     | transition | from | to  | with      | action |     | Reinforcement |     |
composedfromfollowingelementsorterms.Dataset:Aset learning is to learn how to take actions in each step to
maximisethetargetawards.
| of instances                               | for   | building | or evaluating | a          | machine learning |         |                                                  |                 |     |           |            |     |     |               |
| ------------------------------------------ | ----- | -------- | ------------- | ---------- | ---------------- | ------- | ------------------------------------------------ | --------------- | --- | --------- | ---------- | --- | --- | ------------- |
| model.                                     |       |          |               |            |                  |         | Machinelearningcanbeappliedtothefollowingtypical |                 |     |           |            |     |     |               |
| Atthetoplevel,thedatacouldbecategorisedas: |       |          |               |            |                  |         | tasks[28]1:                                      |                 |     |           |            |     |     |               |
|                                            |       |          |               |            |                  |         | 1)                                               | Classification: |     | to assign | a category |     | to  | each data in- |
| • Training                                 | data: | the      | data used     | to ‘teach’ | (train)          | the al- |                                                  |                 |     |           |            |     |     |               |
stance;E.g.,imageclassification,handwritingrecognition.
gorithmtoperformitstask.
|              |     |       |          |         |          |        | 2) Regression: |     | to predict |     | a value | for | each data | instance; |
| ------------ | --- | ----- | -------- | ------- | -------- | ------ | -------------- | --- | ---------- | --- | ------- | --- | --------- | --------- |
| • Validation |     | data: | the data | used to | tune the | hyper- |                |     |            |     |         |     |           |           |
E.g.,temperature/age/incomeprediction.
parametersofalearningalgorithm.
Test data: the data used to validate machine learning 3) Clustering: to partition instances into homogeneous
•
|     |     |     |     |     |     |     | regions; | E.g., | pattern | recognition, |     | market/image |     | segmenta- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ------- | ------------ | --- | ------------ | --- | --------- |
modelbehaviour.
tion.
| Learning | program:thecodewrittenbydeveloperstobuild |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4)Dimensionreduction:toreducethetrainingcomplex-
andvalidatethemachinelearningsystem.
ity;E.g.,datasetrepresentation,datapre-processing.
Framework:thelibrary,orplatformbeingusedwhenbuild-
5)Control:tocontrolactionstomaximiserewards;E.g.,
|               |          |     |             | Pytorch |       | Tensor- |     |     |     |     |     |     |     |     |
| ------------- | -------- | --- | ----------- | ------- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| ing a machine | learning |     | model, such | as      | [29], |         |     |     |     |     |     |     |     |     |
gameplaying.
Flow[30],Scikit-learn[31],Keras[32],andCaffe[33].
|        |           |     |               |         |             |     | Figure  | 3 shows    | the      | relationship |         | between |         | different cat- |
| ------ | --------- | --- | ------------- | ------- | ----------- | --- | ------- | ---------- | -------- | ------------ | ------- | ------- | ------- | -------------- |
| In the | remainder | of  | this section, | we give | definitions | for |         |            |          |              |         |         |         |                |
|        |           |     |               |         |             |     | egories | of machine | learning |              | and the | five    | machine | learning       |
otherMLterminologyusedthroughoutthepaper.
|     |     |     |     |     |     |     | tasks. | Among | the five | tasks, | classification |     | and | regression |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | -------- | ------ | -------------- | --- | --- | ---------- |
Instance:apieceofdatarecordingtheinformationaboutan
|     |     |     |     |     |     |     | belong | to supervised |     | learning; | Clustering |     | and | dimension |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | --- | --------- | ---------- | --- | --- | --------- |
object.
|     |     |     |     |     |     |     | reduction | belong | to unsupervised |     |     | learning. | Reinforcement |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------ | --------------- | --- | --- | --------- | ------------- | --- |
Feature:
a measurable property or characteristic of a phe- learning is widely adopted to control actions, such as to
nomenonbeingobservedtodescribetheinstances.
controlAI-gameplayerstomaximisetherewardsforagame
Label:valueorcategoryassignedtoeachdatainstance.
agent.
Test error:
the difference ratio between the real conditions Inaddition,machinelearningcanbeclassifiedintoclas-
andthepredictedconditions.
|                |                                         |     |     |     |     |     | sic machine |      | learning  | and   | deep learning. |            | Algorithms | like      |
| -------------- | --------------------------------------- | --- | --- | --- | --- | --- | ----------- | ---- | --------- | ----- | -------------- | ---------- | ---------- | --------- |
| Generalisation | error:theexpecteddifferenceratiobetween |     |     |     |     |     |             |      |           |       |                |            |            |           |
|                |                                         |     |     |     |     |     | Decision    | Tree | [35], SVM | [27], | linear         | regression |            | [36], and |
therealconditionsandthepredictedconditionsofanyvalid
|     |     |     |     |     |     |     | Naive | Bayes | [37] all | belong | to classic |     | machine | learning. |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | -------- | ------ | ---------- | --- | ------- | --------- |
data.
| Model: | the learned | machine | learning | artefact | that encodes |     |             |     |               |     |            |     |              |        |
| ------ | ----------- | ------- | -------- | -------- | ------------ | --- | ----------- | --- | ------------- | --- | ---------- | --- | ------------ | ------ |
|        |             |         |          |          |              | 1   | These tasks | are | defined based | on  | the nature | of  | the problems | solved |
decisionorpredictionlogicwhichistrainedfromthetrain-
insteadofspecificapplicationscenariossuchaslanguagemodelling.

4
Machine Learning Testing
|     |     |     |     |     |     |     |     |     |     | testing, | because | it is | not only | the | code | that | may contain |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | ----- | -------- | --- | ---- | ---- | ----------- | --- |
machine learning
bugs,butalsothedata.Whenwetrytodetectbugsindata,
| supervised  | unsupervised  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reinforcement  onemayevenuseatrainingprogramasatestinputtocheck
| learning  | learning |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
testing testing le a r n in g somepropertiesrequiredforthedata.
|             |         | te s t in g |     |     | supervised  | unsupervised  | reinforcement  |          |     |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | ----------- | --- | --- | ----------- | ------------- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| (106/108 )  | (2/108) |             |     |     | learning    | learning      |                | learning |     |     |     |     |     |     |     |     |     |     |
3.2 MLTestingWorkflow
dimension
classification regression clustering reduction control dimension  ML testing workflow is about how to conduct ML testing
|     |     |     | classification |     | regression | clustering | reduction |     | control |                |     |         |             |     |         |          |     |       |
| --- | --- | --- | -------------- | --- | ---------- | ---------- | --------- | --- | ------- | -------------- | --- | ------- | ----------- | --- | ------- | -------- | --- | ----- |
|     |     |     |                |     |            |            |           |     |         | with different |     | testing | activities. |     | In this | section, | we  | first |
Figure3:Machinelearningcategoriesandtasks briefly introduce the role of ML testing when building
|     |     |     |     |     |     |     |     |     |     | ML models, | then     | present      | the | key  | procedures | and | activities  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ------------ | --- | ---- | ---------- | --- | ----------- | --- |
|     |     |     |     |     |     |     |     |     |     | in ML      | testing. | We introduce |     | more | details    | of  | the current |     |
Deep learning [38] applies Deep Neural Networks (DNNs) researchrelatedtoeachprocedureinSection5.
|     |     |     | that uses | multiple | layers | of nonlinear | processing |     | units for |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | -------- | ------ | ------------ | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
3.2.1 RoleofTestinginMLDevelopment
featureextractionandtransformation.Typicaldeeplearning
algorithms often follow some widely used neural network Figure4showsthelifecycleofdeployingamachinelearn-
structureslikeConvolutionalNeuralNetworks(CNNs)[39]
|     |     | component |     |     |     |     |     |     |     | ingsystemwithMLtestingactivitiesinvolved.Atthevery |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
and Recurrent Neural Networks (RNNs) [40]. The scope of beginning, a prototype model is generated based on his-
data framework training program thispaperinvolvesbothclassicmachinelearninganddeep torical data; before deploying the model online, one needs
learning. toconductofflinetesting,suchascross-validation,tomake
|     |     |     |     |     |     |     |     |     |     | sure that | the | model | meets | the required |     | conditions. |     | After |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----- | ----- | ------------ | --- | ----------- | --- | ----- |
research
algorithm deployment, the model makes predictions, yielding new
|     |     |     | 3 MACHINE |     | LEARNING | TESTING |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
classic learning datathatcanbeanalysedviaonlinetestingtoevaluatehow
| applied machine learning |     | machine learning |              |       |              |     |          |     |             |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | ---------------- | ------------ | ----- | ------------ | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                          |     |                  | This section | gives | a definition | and | analyses | of  | ML testing. |     |     |     |     |     |     |     |     |     |
themodelinteractswithuserbehaviours.
| theoretical machine learning |     |     | deepI lteardninegscribes |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the testing workflow (how to test), testing Thereareseveralreasonsthatmakeonlinetestingessen-
properties (what to test), and testing components (where tial.First,offlinetestingusuallyreliesontestdata,whiletest
totest).
classification datausuallyfailstofullyrepresentfuturedata[42];Second,
|     |             |                              |     |     |     |     |     |     |     | offline | testing | is not | able to | test | some | circumstances |     | that |
| --- | ----------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ------ | ------- | ---- | ---- | ------------- | --- | ---- |
|     | supervised  | unsupervised  reinforcement  |     |     |     |     |     |     |     |         |         |        |         |      |      |               |     |      |
learning learning learning may be problematic in real applied scenarios, such as data
3.1 Definition
lossandcalldelays.Inaddition,offlinetestinghasnoaccess
|     |     |     | A software | bug  | refers | to an imperfection |         | in  | a computer   |         |          |         |      |     |      |               |     |       |
| --- | --- | --- | ---------- | ---- | ------ | ------------------ | ------- | --- | ------------ | ------- | -------- | ------- | ---- | --- | ---- | ------------- | --- | ----- |
|     |     |     |            |      |        |                    |         |     |              | to some | business | metrics | such | as  | open | rate, reading |     | time, |
|     |     |     | program    | that | causes | a discordance      | between |     | the existing |         |          |         |      |     |      |               |     |       |
andclick-throughrate.
andtherequiredconditions[41].Inthispaper,wereferthe
|     |     |     |     |     |     |     |     |     |     | In the | following, |     | we present |     | an ML | testing | workflow |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | ---------- | --- | ----- | ------- | -------- | --- |
term‘bug’tothedifferencesbetweenexistingandrequired
|     |     |     |     |     |     |     |     |     |     | adapted | from | classic | software | testing | workflows. |     | Figure | 5   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ------- | -------- | ------- | ---------- | --- | ------ | --- |
behavioursofanMLsystem2.
|     |     |     |            |       |       |           |        |        |           | shows          | the workflow, |     | including |     | both offline |     | testing | and |
| --- | --- | --- | ---------- | ----- | ----- | --------- | ------ | ------ | --------- | -------------- | ------------- | --- | --------- | --- | ------------ | --- | ------- | --- |
|     |     |     | Definition | 1 (ML | Bug). | An ML bug | refers | to any | imperfec- | onlinetesting. |               |     |           |     |              |     |         |     |
tioninamachinelearningitemthatcausesadiscordance
betweentheexistingandtherequiredconditions.
3.2.2 OfflineTesting
WedefineMLtestingasanyactivityaimedtodetectML The workflow of offline testing is shown by the top dotted
bugs. rectangle of Figure 5. At the very beginning, developers
needtoconductrequirementanalysistodefinetheexpecta-
|     |     |     | Definition | 2 (ML | Testing). | Machine | Learning |     | Testing (ML |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | ----- | --------- | ------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
testing)referstoanyactivitydesignedtorevealmachine tionsoftheusersforthemachinelearningsystemundertest.
Inrequirementanalysis,specificationsofamachinelearning
learningbugs.
|     |     |     |     |     |     |     |     |     |     | system | are analysed |     | and the | whole | testing |     | procedure | is  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------ | --- | ------- | ----- | ------- | --- | --------- | --- |
ThedefinitionsofmachinelearningbugsandMLtesting
planned.Afterthat,testinputsareeithersampledfromthe
indicate three aspects of machine learning: the required collecteddataorgeneratedbasedonaspecificpurpose.Test
conditions, the machine learning items, and the testing oracles are then identified or generated (see Section 5.2 for
activities. A machine learning system may have different more details of test oracles in machine learning). When the
|     |     |     | types of | ‘required | conditions’, | such | as  | correctness, | robust- |           |        |      |         |             |     |                |     |     |
| --- | --- | --- | -------- | --------- | ------------ | ---- | --- | ------------ | ------- | --------- | ------ | ---- | ------- | ----------- | --- | -------------- | --- | --- |
|     |     |     |          |           |              |      |     |              |         | tests are | ready, | they | need to | be executed |     | for developers |     | to  |
ness, and privacy. An ML bug may exist in the data, the collect results. The test execution process involves building
learning program, or the framework. The testing activities a model with the tests (when the tests are training data) or
mayincludetestinputgeneration,testoracleidentification,
|     |     |     |     |     |     |     |     |     |     | running | a built | model | against | the | tests | (when | the tests | are |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ----- | ------- | --- | ----- | ----- | --------- | --- |
testadequacyevaluation,andbugtriage.Inthissurvey,we test data), as well as checking whether the test oracles are
refertotheabovethreeaspectsastestingproperties,testing violated.Aftertheprocessoftestexecution,developersmay
|     |     |     | components, | and | testing | workflow, | respectively, |     | according |                |     |         |          |     |         |     |              |     |
| --- | --- | --- | ----------- | --- | ------- | --------- | ------------- | --- | --------- | -------------- | --- | ------- | -------- | --- | ------- | --- | ------------ | --- |
|     |     |     |             |     |         |           |               |     |           | use evaluation |     | metrics | to check | the | quality | of  | tests, i.e., | the |
towhichwecollectandorganisetherelatedwork. abilityoftheteststoexposeMLproblems.
Note that a test input in ML testing can be much more The test execution results yield a bug report to help
|     |     |     | diverse | in its | form than | that used | in traditional |     | software |            |      |            |          |      |           |     |          |       |
| --- | --- | --- | ------- | ------ | --------- | --------- | -------------- | --- | -------- | ---------- | ---- | ---------- | -------- | ---- | --------- | --- | -------- | ----- |
|     |     |     |         |        |           |           |                |     |          | developers | to   | duplicate, | locate,  | and  | solve     | the | bug.     | Those |
|     |     |     |         |        |           |           |                |     |          | identified | bugs | will be    | labelled | with | different |     | severity | and   |
2 Theexistingrelatedpapersmayuseothertermslike‘defect’or‘issue’.
assignedfordifferentdevelopers.Oncethebugisdebugged
|     |     |     | This paper | uses | ‘bug’ as | a representative | of  | all such | related terms |               |     |            |         |     |           |     |      |      |
| --- | --- | --- | ---------- | ---- | -------- | ---------------- | --- | -------- | ------------- | ------------- | --- | ---------- | ------- | --- | --------- | --- | ---- | ---- |
|     |     |     |            |      |          |                  |     |          |               | and repaired, |     | regression | testing | is  | conducted | to  | make | sure |
consideringthat‘bug’hasamoregeneralmeaning[41].

5
MLdevelopmentbecausethecomponentsaremoreclosely
bondedwitheachotherthantraditionalsoftware[8],which
historical prototype offline deployed
data model testing model indicatestheimportanceoftestingeachoftheMLcompon-
ents.WeintroducethebugdetectionineachMLcomponent
below:
user request BugDetectioninData.Thebehavioursofamachinelearn-
online data a m da o p d t e e l d t o e n s l t i i n n e g predictions ing system largely depends on data [8]. Bugs in data affect
the quality of the generated model, and can be amplified
to yield more serious problems over a period a time [45].
Bug detection in data checks problems such as whether
Figure4:RoleofMLtestinginMLsystemdevelopment
the data is sufficient for training or test a model (also
called completeness of the data [46]), whether the data is
the repair solves the reported problem and does not bring representative of future data, whether the data contains a
new problems. If no bugs are identified, the offline testing lot of noise such as biased labels, whether there is skew
processends,andthemodelisdeployed. betweentrainingdataandtestdata[45],andwhetherthere
formula formula frequent objec i t s ive d ata su p bj o ec is ti o ve n ing [47] or adversary information that may
3.2.3 OnlineTestinexgtraction transformation subtree mining analyasfifsectthanealmysoisdel’sperformance.
BugDetectioninFrameworks.MachineLearningrequiresa
Offline testing tests the model with historical data without
lotofcomputations.AsshownbyFigure6,MLframeworks
in the real application environment. It also lacks the data
offer algorithms to help write the learning program, and
collection process of user behaviours. Online testing com-
database formula set formula frequent plat fi f lt o e r re m d stoknhoewlpledtgreainthemachinelearningmodel,making
plements the shortage of offline testintgre,ea gnrdaphasims topdaetteterncst patterns
it easier for developers to build solutions for designing,
bugsafterthemodelisdeployedonline.
training and validating algorithms and models for com-
Theworkflowofonlinetestingisshownbythebottomof
plex problems. They play a more important role in ML
Figure 5. There are different methods of conducting online
developmentthanintraditionalsoftwaredevelopment.ML
testing for different purposes. For example, runtime mon-
Framework testing thus checks whether the frameworks of
itoring keeps checking whether the running ML systems
machine learning have bugs that may lead to problems in
meet the requirements or violate some desired runtime
thefinalsystem[48].
properties. Another commonly used scenario is to monitor
Bug Detection in Learning Program. A learning program
userresponses,basedonwhichtofindoutwhetherthenew
can be classified into two parts: the algorithm designed
modelissuperiortotheoldmodelundercertainapplication
by the developer or chosen from the framework, and the
contexts. A/B testing is one typical type of such online
actual code that developers write to implement, deploy, or
testing [43]. It splits customers to compare two versions of
configure the algorithm. A bug in the learning program
thesystem(e.g.,webpages).WhenperformingA/Btesting
mayariseeitherbecausethealgorithmisdesigned,chosen,
on ML systems, the sampled users will be split into two
or configured improperly, or because the developers make
groupsusingthenewandoldMLmodelsseparately.
typosorerrorswhenimplementingthedesignedalgorithm.
MAB (Multi-Armed Bandit) is another online testing
approach[44].ItfirstconductsA/Btestingforashorttime
and finds out the best model, then put more resources on 3.4 MLTestingProperties
thechosenmodel. Testing properties refer to what to test in ML testing:
for what conditions ML testing needs to guarantee for a
3.3 MLTestingComponents trained model. This section lists some typical properties
that the literature has considered. We classified them into
To build a machine learning model, an ML software de-
basic functional requirements (i.e., correctness and model
veloperusuallyneedstocollectdata,labelthedata,design
relevance) and non-functional requirements (i.e., efficiency,
learningprogramarchitecture,andimplementtheproposed
robustness3,fairness,interpretability).
architecturebasedonspecificframeworks.Theprocedureof
These properties are not strictly independent of each
machine learning model development requires interaction
other when considering the root causes, yet they are dif-
with several components such as data, learning program,
ferent external manifestations of the behaviours of an ML
and learning framework, while each component may con-
system and deserve being treated independently in ML
tainbugs.
testing.
Figure 6 shows the basic procedure of building an ML
model and the major components involved in the process.
3.4.1 Correctness
Data are collected and pre-processed for use; the learning
Correctness measures the probability that the ML system
program is the code for running to train the model; the
undertest‘getsthingsright’.
framework (e.g., Weka, scikit-learn, and TensorFlow) offers
Definition 3 (Correctness). Let D be the distribution of
algorithms and other libraries for developers to choose
future unknown data. Let x be a data item belonging
from,whenwritingthelearningprogram.
to D. Let h be the machine learning model that we are
Thus, when conducting ML testing, developers may
need to try to find bugs in every component including
3 weadoptthemoregeneralunderstandingfromsoftwareengineering
the data, the learning program, and the framework. In
community [49], [50], and regard robustness as a non-functional re-
particular, error propagation is a more serious problem in quirement.

6
test evaluation
start
test generation
test input
requirements generation model report bugs No
analysis training/prediction generation identified
test oracle
generation
yes
debug and model
regression testing bug triage
repair deployment
model result metric value test metric
end user split
selection analysis collection design
gnitset
enilffo
gnitset
enilno
Figure5:IdealisedWorkflowofMLtesting
DATA
data collection algorithm selection/design
data preparation learning program generation
model training
FRAMEWORK
3.4.2 ModelRelevance
LEARNING PROGRAM
A machine learning model comes from the combination
of a machine learning algorithm and the training data. It
is important to ensure that the adopted machine learning
algorithm be not over-complex than just needed [51]. Oth-
erwise, the model may fail to have good performance on
futuredata,orhaveverylargeuncertainty.
The algorithm capacity represents the number of func-
Figure 6: Components (shown by the grey boxes) involved
tions that a machine learning model can select (based on
inMLmodelbuilding.
the training data at hand) as a possible solution. It is
usuallyapproximatedbyVC-dimension[52]orRademacher
Complexity[53]forclassificationtasks.VC-dimensionisthe
testing. h(x) is the predicted label of x, c(x) is the true
formula F: =IF(A1,SUM(B1,B2),C1)+C2 cardinality of the largest set of points that the algorithm
label.ThemodelcorrectnessE(h)istheprobabilitythat
can shatter. Rademacher Complexity is the cardinality of
h(x)andc(x)areidentical:
formula F formula Fthe largest set of training data with fixed features that the
E(h)=Pr x∼D [h(x)=c(x)] (1) algorithmshatters.
We define the relevance between a machine learning
IF + C2 IF math range
algorithmcapacityandthedatadistributionastheproblem
Achieving acceptable correctness is the fundamental re- ofmodelrelevance.
quirement of an ML sAy1stemSU.MTheC1real performranagenceSUoMf anrange
Definition 5 (Model Relevance). Let D be the training
MLsystemshouldbeevaluatedonfuturedata.Sincefuture
data distribution. Let R(D,A) be the simplest required
dataareoftennotavailabA1le,thecuA1rrentbestpractriacnegeusualrlaynge
capacity of any machine learning algorithm A for D.
splits the data into training data and test data (or training
R(cid:48)(D,A(cid:48)) is the capacity of the machine learning al-
data, validation data, and test data), and uses test data to
gorithmA(cid:48) undertest.Modelrelevanceisthedifference
simulatefuturedata.Thisdatasplitapproachiscalledcross-
betweenR(D,A)andR(cid:48)(D,A(cid:48)).
validation.
f =|(R(D,A)−R(cid:48)(D,A(cid:48))| (3)
Definition 4 (Empirical Correctness). Let X = (x 1 ,...,x m )
be the set of unlabelled test data sampled from D.
L (1 e ) t h be th (2 e ) machine lea(r3)ning model u(n4)der test.(5L)et Model ( r 6) elevance aims to measure how well a machine
HLOYOK(cid:48)U=P (h(xIF 1 E)R,R.O.R.,h(x m ))be A t N h D esetofpredic IF tedlabelsc IF or- l i e s a u rn su in a g lly faorlm c gu a o u ri s t e h d m by fits ov t e h r e fit d ti a n t g a , . w A h l e o r w e t m he od m e o l d r e e l le i v s an to c o e
respondingtoeachtrainingitemx i.LetY =(y
1
,...,y
m
)
complex for the data, which thereby fails to generalise to
RbOeWthe trHuLeOOlKaUbPels, IwSNhUMeBreEReaIScNhUMyBE
i
R∈ YISNcUoMrBrEeRspondOsRto GE
f
T
u
P
t
IV
u
O
r
T
e
DA
d
TA
at
m
a
a
o
th
r
G
to
ETP
p
IV
r
O
e
T
d
D
i
A
c
T
t
A
observationsrobustly.
t ( h d e en ( l 7 o a ) b te e d l o a f s x Eˆ i ( ∈ h ( ) 8 ) ) X is . : The (9 e ) mpirica (1 l 0) corre ( c 11 t ) ness of m (12 o ) del (1O3)f course, R(1 (cid:48) 4()D,A), the minimum complexity that is
formu IF IF IF IF GETPIVOTDATA ‘juINsDtEXsufficient’DiAsTEhard to determine, and is typically ap-
COUNTIF math COUNTIF Eˆ S ( U h M )=
m
1 COU (cid:88) m NT I(h( A x NDi )= IS y BiL ) ANK CONCATEN(2AT)E p he r M o l A p x TC i a m H ll a e t v e Y i E a [ A t 4 R e 2] t , h M e [ O 5 N p 4 TH ] r . o W b D le e AY m di o s f cu o s v s er m fi o tt r i e ng st i r n at S e e g c i t e i s on th 6 a . t 2. could
i=1
(15) (16) (17) (18) (19) 3.4.3(20)Robustnes(s21)
wher I e F Iisthe A in ND dicatorf V u L n OO c K ti U o P n;apr I e SE d R i R c O a R tereturns IF 1 ER i R f OpR is Ro I b SE u R s R t O n R ess is d VL e O fi O n K e UP d by the IEEE standard glossary of
true,andreturns0otherwise. software engineering terminology [55], [56] as: ‘The degree
VLOOKUP IF MATCH GETPIVOTDATA VLOOKUP VLOOKUP VLOOKUP

7
to which a system or component can function correctly in issues also include other aspects such as model stealing or
the presence of invalid inputs or stressful environmental extraction. This survey focuses on the testing techniques
conditions’. Adopting a similar spirit to this definition, we on detecting ML security problems, which narrows the
definetherobustnessofMLasfollows: security scope to robustness-related security. We combine
|            |                 |          |        | S           |                    |           |      | theintroductionofrobustnessandsecurityinSection6.3. |             |     |     |     |     |     |     |
| ---------- | --------------- | -------- | ------ | ----------- | ------------------ | --------- | ---- | --------------------------------------------------- | ----------- | --- | --- | --- | --- | --- | --- |
| Definition | 6 (Robustness). |          | Let    |             | be a machine       | learning  |      |                                                     |             |     |     |     |     |     |     |
| system.    | Let             | E(S)     | be the | correctness |                    | of S. Let | δ(S) |                                                     |             |     |     |     |     |     |     |
| be the     | machine         | learning |        | system      | with perturbations |           | on   | 3.4.5                                               | DataPrivacy |     |     |     |     |     |     |
any machine learning components such as the data, the Privacy in machine learning is the ML system’s ability to
learning program, or the framework. The robustness preserveprivatedatainformation.Fortheformaldefinition,
of a machine learning system is a measurement of the differential privacy
|     |     |     |     |     |     |     |     | we use | the most | popular |     |     |     | taken from | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ------- | --- | --- | --- | ---------- | --- |
differencebetweenE(S)andE(δ(S)):
workofDwork[58].
r =E(S)−E(δ(S)) (4) Definition9((cid:15)-DifferentialPrivacy).LetAbearandomised
|            |     |               |     |                |     |          |      | algorithm.LetD |      |        | andD      | betwotrainingdatasetsthat |        |        |        |
| ---------- | --- | ------------- | --- | -------------- | --- | -------- | ---- | -------------- | ---- | ------ | --------- | ------------------------- | ------ | ------ | ------ |
|            |     |               |     |                |     |          |      |                |      | 1      | 2         |                           |        |        |        |
|            |     |               |     |                |     |          |      | differ         | only | on one | instance. | Let                       | S be a | subset | of the |
| Robustness |     | thus measures |     | the resilience |     | of an ML | sys- |                |      |        |           |                           |        |        |        |
tem’scorrectnessinthepresenceofperturbations. outputsetofA.Agives(cid:15)-differentialprivacyif
Apopularsub-categoryofrobustnessiscalledadversarial
|     |     |     |     |     |     |     |     |     | Pr[A(D | )∈S]≤exp((cid:15))∗Pr[A(D |     |     |     | )∈S] |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------------------- | --- | --- | --- | ---- | --- |
robustness.Foradversarialrobustness,theperturbationsare 1 2 (7)
| designed     | to be      | hard to  | detect.     | Following | the         | work of     | Katz  |               |        |             |                       |         |               |        |              |
| ------------ | ---------- | -------- | ----------- | --------- | ----------- | ----------- | ----- | ------------- | ------ | ----------- | --------------------- | ------- | ------------- | ------ | ------------ |
|              |            |          |             |           |             |             |       | In other      | words, |             | (cid:15)-Differential | privacy | is            | a form | of (cid:15)- |
| et al. [57], | we         | classify | adversarial |           | robustness  | into        | local |               |        |             |                       |         |               |        |              |
|              |            |          |             |           |             |             |       | contained     | bound  | on          | output change         |         | in responding | to     | single       |
| adversarial  | robustness |          | and global  |           | adversarial | robustness. |       |               |        |             |                       |         |               |        |              |
|              |            |          |             |           |             |             |       | input change. |        | It provides | a way                 | to      | know whether  |        | any one      |
Localadversarialrobustnessisdefinedasfollows.
individual’sdatahashasasignificanteffect(boundedby(cid:15))
x
| Definition | 7 (Local | Adversarial |     | Robustness). |     | Let | a test | ontheoutcome. |     |     |     |     |     |     |     |
| ---------- | -------- | ----------- | --- | ------------ | --- | --- | ------ | ------------- | --- | --- | --- | --- | --- | --- | --- |
x(cid:48)
| input | for an | ML model | h.  | Let | be another | test | input |      |         |     |      |           |     |     |         |
| ----- | ------ | -------- | --- | --- | ---------- | ---- | ----- | ---- | ------- | --- | ---- | --------- | --- | --- | ------- |
|       |        |          |     |     |            |      |       | Data | privacy | has | been | regulated | by  | law | makers, |
generatedviaconductingadversarialperturbationonx.
|     |     |     |     |     |     |     |     | for example, |     | the EU | General | Data | Protection |     | Regula- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ------- | ---- | ---------- | --- | ------- |
Modelhisδ-localrobustatinputxifforanyx(cid:48).
|     |     |     |     |     |     |     |     | tion (GDPR) | [59] | and | California | Consumer |     | Privacy | Act |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | --- | ---------- | -------- | --- | ------- | --- |
∀x(cid:48) :||x−x(cid:48)|| ≤δ →h(x)=h(x(cid:48)) (5) (CCPA) [60]. Current research mainly focuses on how to
p
|     |     |     |     |     |     |     |     | present | privacy-preserving |     |     | machine | learning, | instead | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------------ | --- | --- | ------- | --------- | ------- | --- |
||·|| represents p-norm for distance measurement. The detecting privacy violations. We discuss privacy-related re-
p
commonlyusedpcasesinmachinelearningtestingare0,2, searchopportunitiesandresearchdirectionsinSection10.
| and∞.Forexample,whenp |     |     |     | = 2,i.e. | ||x−x(cid:48)|| | represents |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | -------- | --------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2
| the Euclidean | distance |     | of x | and x(cid:48). | In the | case of | p = 0,     | 3.4.6 | Efficiency |     |     |     |     |     |     |
| ------------- | -------- | --- | ---- | -------------- | ------ | ------- | ---------- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
|               |          |     |      |                |        | x       | x(cid:48). |       |            |     |     |     |     |     |     |
it calculates the element-wise difference between and The efficiency of a machine learning system refers to its
| When p | = ∞, | it measures |     | the the | largest | element-wise |     |              |     |            |        |     |               |         |     |
| ------ | ---- | ----------- | --- | ------- | ------- | ------------ | --- | ------------ | --- | ---------- | ------ | --- | ------------- | ------- | --- |
|        |      |             |     |         |         |              |     | construction | or  | prediction | speed. |     | An efficiency | problem |     |
distanceamongallelementsofxandx(cid:48).
happenswhenthesystemexecutesslowlyoreveninfinitely
Local adversarial robustness concerns the robustness at duringtheconstructionorthepredictionphase.
| one specific | test       | input,  | while | global      | adversarial | robustness |        |          |                 |     |              |     |          |             |     |
| ------------ | ---------- | ------- | ----- | ----------- | ----------- | ---------- | ------ | -------- | --------------- | --- | ------------ | --- | -------- | ----------- | --- |
|              |            |         |       |             |             |            |        | With     | the exponential |     | growth       | of  | data and | complexity  | of  |
| measures     | robustness | against |       | all inputs. | We          | define     | global |          |                 |     |              |     |          |             |     |
|              |            |         |       |             |             |            |        | systems, | efficiency      | is  | an important |     | feature  | to consider | for |
adversarialrobustnessasfollows. model selection and framework selection, sometimes even
| Definition | 8 (Global | Adversarial |     | Robustness). |     | Let x | a test |                |     |      |          |       |              |     |        |
| ---------- | --------- | ----------- | --- | ------------ | --- | ----- | ------ | -------------- | --- | ---- | -------- | ----- | ------------ | --- | ------ |
|            |           |             |     |              |     |       |        | more important |     | than | accuracy | [61]. | For example, | to  | deploy |
|            |           |             | h.  | x(cid:48)    |     |       |        |                |     |      |          |       |              |     |        |
input for an ML model Let be another test input a large model to a mobile device, optimisation, compres-
generatedviaconductingadversarialperturbationonx. sion, and device-oriented customisation may be performed
Modelhis(cid:15)-globalrobustifforanyxandx(cid:48). to make it feasible for the mobile device execution in a
∀x,x(cid:48) :||x−x(cid:48)|| →h(x)−h(x(cid:48))≤(cid:15) reasonabletime,butaccuracymaysacrificetoachievethis.
|     |     |     | ≤δ  |     |     |     | (6) |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
p
|     |     |     |     |     |     |     |     | 3.4.7 | Fairness |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- |
3.4.4 Security Machine learning is a statistical method and is widely
The security of an ML system is the system’s resilience adopted to make decisions, such as income prediction and
against potential harm, danger, or loss made via manipu- medical treatment prediction. Machine learning tends to
latingorillegallyaccessingMLcomponents. learn what humans teach it (i.e., in form of training data).
Security and robustness are closely related. An ML sys- However, humans may have bias over cognition, further
temwithlowrobustnessmaybeinsecure:ifitislessrobust affecting the data collected or labelled and the algorithm
in resisting the perturbations in the data to predict, the designed,leadingtobiasproblems.
system may more easily fall victim to adversarial attacks; The characteristics that are sensitive and need to be
Forexample,ifitislessrobustinresistingtrainingdataper- protected against unfairness are called protected character-
turbations,itmayalsobevulnerabletodatapoisoning(i.e., istics [62] or protected attributes and sensitive attributes. Ex-
changestothepredictivebehaviourcausedbyadversarially amplesoflegallyrecognisedprotectedclassesincluderace,
modifyingthetrainingdata). colour, sex, religion, national origin, citizenship, age, preg-
Nevertheless,lowrobustnessisjustonecauseofsecurity nancy, familial status, disability status, veteran status, and
vulnerabilities. Except for perturbations attacks, security geneticinformation.

8
Fairness is often domain specific. Regulated domains notlimitedto,testdata.Whentestingthelearningprogram,
includecredit,education,employment,housing,andpublic atestcasemaybeasingletestinstancefromthetestdataor
accommodation4.
atoytrainingset;whentestingthedata,thetestinputcould
Toformulatefairnessisthefirststeptosolvethefairness bealearningprogram.
problemsandbuildfairmachinelearningmodels.Theliter- 4) Test oracle: traditional software testing usually assumes
aturehasproposedmanydefinitionsoffairnessbutnofirm the presence of a test oracle. The output can be verified
consensus is reached at this moment. Considering that the against the expected values by the developer, and thus the
definitions themselves are the research focus of fairness in oracleisusuallydeterminedbeforehand.Machinelearning,
machinelearning,wediscusshowtheliteratureformulates however,isusedtogenerateanswersbasedonasetofinput
andmeasuresdifferenttypesoffairnessinSection6.5. values after being deployed online. The correctness of the
|     |     |     |     |     |     |     | large number |     | of generated |     | answers is | typically | manually |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- | ---------- | --------- | -------- |
3.4.8 Interpretability confirmed. Currently, the identification of test oracles re-
Machine learning models are often applied to assist/make mainschallenging,becausemanydesiredpropertiesaredif-
decisions in medical treatment, income prediction, or per- ficulttoformallyspecify.Evenforaconcretedomainspecific
sonal credit assessment. It may be important for humans problem, the oracle identification is still time-consuming
to understand the ‘logic’ behind the final decisions, so that and labour-intensive, because domain-specific knowledge
they can build trust over the decisions made by ML [64], is often required. In current practices, companies usually
[65],[66]. rely on third-party data labelling companies to get manual
The motives and definitions of interpretability are di- labels,whichcanbeexpensive. Metamorphicrelations[71]
verseandstillsomewhatdiscordant[64].Nevertheless,un- areatypeofpseudooracleadoptedtoautomaticallymitig-
likefairness,amathematicaldefinitionofMLinterpretabil- atetheoracleprobleminmachinelearningtesting.
|     |     |     |     |     |     |     | 5) Test | adequacy | criteria: |     | test adequacy | criteria | are used |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --------- | --- | ------------- | -------- | -------- |
ityremainselusive[65].ReferringtotheworkofBiranand
Cotton [67] as well as the work of Miller [68], we describe to provide quantitative measurement on the degree of
theinterpretabilityofMLasthedegreetowhichanobserver the target software that has been tested. Up to present,
can understand the cause of a decision made by an ML many adequacy criteria are proposed and widely adopted
system. in industry, e.g., line coverage, branch coverage, dataflow
Interpretabilitycontainstwoaspects:transparency(how coverage.However,duetofundamentaldifferencesofpro-
themodelworks)andposthocexplanations(otherinform- gramming paradigm and logic representation format for
ation that could be derived from the model) [64]. Inter- machine learning software and traditional software, new
pretability is also regarded as a request by regulations like testadequacycriteriaarerequiredtotakethecharacteristics
GDPR [69], where the user has the legal ‘right to explana- ofmachinelearningsoftwareintoconsideration.
|     |     |     |     |     |     |     | 6) False | positives | in  | detected | bugs:duetothedifficultyin |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------- | --- | -------- | ------------------------- | --- | --- |
tion’toaskforanexplanationofanalgorithmicdecisionthat
wasmadeaboutthem.AthoroughintroductionofMLinter- obtaining reliable oracles, ML testing tends to yield more
pretabilitycanbereferredtointhebookofChristoph[70]. falsepositivesinthereportedbugs.
|     |     |     |     |     |     |     | 7) Roles | of testers: |     | the bugs | in ML testing | may | exist not |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | -------- | ------------- | --- | --------- |
3.5 SoftwareTestingvs.MLTesting only in the learning program, but also in the data or the
|             |          |         |     |     |             |           | algorithm, | and | thus | data scientists | or algorithm |     | designers |
| ----------- | -------- | ------- | --- | --- | ----------- | --------- | ---------- | --- | ---- | --------------- | ------------ | --- | --------- |
| Traditional | software | testing | and | ML  | testing are | different |            |     |      |                 |              |     |           |
couldalsoplaytheroleoftesters.
| in many | aspects. | To understand |     | the | unique features | of  |     |     |     |     |     |     |     |
| ------- | -------- | ------------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
MLtesting,wesummarisetheprimarydifferencesbetween
|                                                 |     |     |     |     |     |     | 4 PAPER | COLLECTION |     |     | REVIEW | SCHEMA |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --- | --- | ------ | ------ | --- |
| traditionalsoftwaretestingandMLtestinginTable1. |     |     |     |     |     |     |         |            |     |     | AND    |        |     |
1)Componenttotest(wherethebugmayexist):traditional
|     |     |     |     |     |     |     | This section | introduces |     | the | scope, the paper | collection | ap- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---------- | --- | --- | ---------------- | ---------- | --- |
software testing detects bugs in the code, while ML testing proach, an initial analysis of the collected papers, and the
detects bugs in the data, the learning program, and the organisationofoursurvey.
framework,eachofwhichplayanessentialroleinbuilding
| anMLmodel.    |      |             |           |            |                 |     | 4.1 SurveyScope |        |     |         |               |     |           |
| ------------- | ---- | ----------- | --------- | ---------- | --------------- | --- | --------------- | ------ | --- | ------- | ------------- | --- | --------- |
| 2) Behaviours |      | under       | test: the | behaviours | of traditional  |     |                 |        |     |         |               |     |           |
|               |      |             |           |            |                 |     | An ML           | system | may | include | both hardware | and | software. |
| software      | code | are usually | fixed     | once       | the requirement |     | is              |        |     |         |               |     |           |
Thescopeofourpaperissoftwaretesting(asdefinedinthe
fixed,whilethebehavioursofanMLmodelmayfrequently
introduction)appliedtomachinelearning.
changeasthetrainingdataisupdated.
Weapplythefollowinginclusioncriteriawhencollecting
| 3) Test | input: | the test inputs | in  | traditional | software | testing |     |     |     |     |     |     |     |
| ------- | ------ | --------------- | --- | ----------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
papers.Ifapapersatisfiesanyoneormoreofthefollowing
areusuallytheinputdatawhentestingcode;inMLtesting,
criteria,wewillincludeit.Whenspeakingofrelated‘aspects
| however, | the | test inputs | in may | have | more diverse | forms. |     |     |     |     |     |     |     |
| -------- | --- | ----------- | ------ | ---- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
ofMLtesting’,werefertotheMLproperties,MLcompon-
| Note that    | we  | separate    | the definition |              | of ‘test input’ | and    |                                               |                      |     |     |             |     |            |
| ------------ | --- | ----------- | -------------- | ------------ | --------------- | ------ | --------------------------------------------- | -------------------- | --- | --- | ----------- | --- | ---------- |
|              |     |             |                |              |                 |        | ents,andMLtestingprocedureintroducedinSection |                      |     |     |             |     | 2.         |
| ‘test data’. | In  | particular, | we use         | ‘test input’ | to refer        | to the |                                               |                      |     |     |             |     |            |
|              |     |             |                |              |                 |        | 1) The paper                                  | introduces/discusses |     |     | the general |     | idea of ML |
inputsinanyformthatcanbeadoptedtoconductmachine
testingoroneoftherelatedaspectsofMLtesting.
| learning  | testing; | while    | ‘test data’ | specially | refers | to the  |              |          |         |              |           |            |             |
| --------- | -------- | -------- | ----------- | --------- | ------ | ------- | ------------ | -------- | ------- | ------------ | --------- | ---------- | ----------- |
|           |          |          |             |           |        |         | 2) The paper | proposes |         | an approach, | study,    | or         | tool/frame- |
| data used | to       | validate | ML model    | behaviour | (see   | more in |              |          |         |              |           |            |             |
|           |          |          |             |           |        |         | work that    | targets  | testing | one          | of the ML | properties | or com-     |
Section2).Thus,testinputsinMLtestingcouldbe,butare
ponents.
|     |     |     |     |     |     |     | 3) The paper |     | presents | a dataset | or benchmark |     | especially |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | --------- | ------------ | --- | ---------- |
4 Toprohibitdiscrimination‘inaplaceofpublicaccommodationonthe
designedforthepurposeofMLtesting.
basisofsexualorientation,genderidentity,orgenderexpression’[63].

9
Table1:ComparisonbetweenTraditionalSoftwareTestingandMLTesting
Characteristics TraditionalTesting MLTesting
Componenttotest code dataandcode(learningprogram,framework)
Behaviourundertest usuallyfixed changeovertime
Testinput inputdata dataorcode
Testoracle definedbydevelopers definedbydevelopersandlabellingcompanies
Adequacycriteria coverage/mutationscore unknown
Falsepositivesinbugs rare prevalent
Tester developer datascientist,algorithmdesigner,developer
Table2:PaperQueryResults
4) The paper introduces a set of measurement criteria that
couldbeadoptedtotestoneoftheMLproperties. KeyWords Hits Title Body
SomepapersconcerntraditionalvalidationofMLmodel
machinelearningtest 211 17 13
performance such as the introduction of precision, recall,
machinelearningbug 28 4 4
and cross-validation. We do not include these papers be-
machinelearningtrustworthiness 1 0 0
causetheyhavehadalongresearchhistoryandhavebeen deeplearningtest 38 9 8
thoroughly and maturely studied. Nevertheless, for com- deeplearningbug 14 1 1
pleteness,weincludetheknowledgewhenintroducingthe deeplearningtrustworthiness 2 1 1
backgroundtosetthecontext.Wedonotincludethepapers neuralnetworktest 288 10 9
neuralnetworkbug 22 0 0
that adopt machine learning techniques for the purpose
neuralnetworktrustworthiness 5 1 1
of traditional software testing and also those target ML
[MLproperties]+test 294 5 5
problems,whichdonotusetestingtechniquesasasolution. [MLproperties]+bug 10 0 0
Some recent papers also target the formal guarantee on [MLcomponents]+test 77 5 5
the desired properties of a machine learning system, i.e., [MLcomponents]+bug 8 2 2
to formally verify the correctness of the machine learning
Query - - 50
systemsaswellasotherproperties.Testingandverification Snowball - - 59
ofmachinelearning,asintraditionaltesting,havetheirown Authorfeedback - - 35
advantages and disadvantages. For example, verification Overall - - 144
usuallyrequiresawhite-boxscenario,butsuffersfrompoor
scalability, while testing may scale, but lacks completeness.
The size of the space of potential behaviours may render authors may tend to use very diverse terms. To ensure a
currentapproachestoverificationinfeasibleingeneral[72], high coverage of ML testing related papers, we therefore
but specific safety critical properties will clearly benefit also performed snowballing [74] on each of the related
from focused research activity on scalable verification, as papersfoundbykeywordsearching.Wecheckedtherelated
well as testing. In this survey, we focus on the machine work sections in these studies and continue adding the
learning testing. More details for the literature review of related work that satisfies the inclusion criteria introduced
the verification of machine learning systems can be found inSection4.1,untilwereachedclosure.
intherecentworkofXiangetal.[73]. To ensure a more comprehensive and accurate survey,
weemailedtheauthorsofthepapersthatwerecollectedvia
4.2 PaperCollectionMethodology query and snowballing, and let them send us other papers
they are aware of which are related with machine learning
Tocollectthepapersacrossdifferentresearchareasasmuch
testingbuthavenotbeenincludedyet.Wealsoaskedthem
aspossible,westartedbyusingexactkeywordsearchingon
to check whether our description about their work in the
popularscientificdatabasesincludingGoogleScholar,DBLP
surveywasaccurateandcorrect.
and arXiv one by one. The keywords used for searching
are listed below. [ML properties] means the set of ML
testing properties including correctness, model relevance, 4.3 CollectionResults
robustness,efficiency,privacy,fairness,andinterpretability. Table 2 shows the details of paper collection results. The
We used each element in this set plus ‘test’ or ‘bug’ as paperscollectedfromGoogleScholarandarXivturnedout
the search query. Similarly, [ML components] denotes the to be subsets of those from DBLP so we only present the
set of ML components including data, learning program/- results of DBLP. Keyword search and snowballing resulted
code, and framework/library. Altogether, we conducted in 109 papers across six research areas till May 15th, 2019.
(3∗3+6∗2+3∗2)∗3 = 81 searches across the three We received over 50 replies from all the cited authors
repositoriesbeforeMay15th,2019. until June 4th, 2019, and added another 35 papers when
• machinelearning+test|bug|trustworthiness dealing with the author feedback. Altogether, we collected
• deeplearning+test|bug|trustworthiness 144papers.
• neuralnetwork+test|bug|trustworthiness Figure 7 shows the distribution of papers published in
• [MLproperties]+test|bug different research venues. Among all the papers, 38.2% pa-
• [MLcomponents]+test|bug pers are published in software engineering venues such as
Machinelearningtechniques havebeenappliedinvari- ICSE,FSE,ASE,ICST,andISSTA;6.9%papersarepublished
ous domains across different research areas. As a result, in systems and network venues; surprisingly, only 19.4%

10
of the total papers are published in artificial intelligence appliedinparticularapplicationscenariossuchasautonom-
venuessuchasAAAI,CVPR,andICLR.Additionally,22.9% ousdrivingandmachinetranslation.
ofthepapershavenotyetbeenpublishedviapeer-reviewed The four aspects have different focuses of ML testing,
venues(thearXivpart). eachofwhichisacompleteorganisationofthetotalcollec-
|     |     |     |     |     |     |     | ted papers |     | (see more | discussion |          | in Section | 3.1),    | as a   | single |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | ---------- | -------- | ---------- | -------- | ------ | ------ |
|     |     |     |     |     |     |     | ML testing |     | paper     | may fit    | multiple | aspects    | if being | viewed |        |
general
|     |     |     |     |     | Artificial Intelligence |     | fromdifferentangles. |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
3.5%
Systems and Network 19.4% 2) Statistical Analysis and Summary. We analyse and
| 6.9% |     |     |     |     |     |     | compare | the | number | of  | research | papers | on  | different | ma- |
| ---- | --- | --- | --- | --- | --- | --- | ------- | --- | ------ | --- | -------- | ------ | --- | --------- | --- |
arXiv Data Mining chine learning categories (supervised/unsupervised/rein-
4.9%
22.9% forcement learning), machine learning structures (clas-
Security
|     |     |     |     |     |     | 2.8% | sic/deep  | learning), |              | testing | properties | in      | Section | 9. We | also  |
| --- | --- | --- | --- | --- | --- | ---- | --------- | ---------- | ------------ | ------- | ---------- | ------- | ------- | ----- | ----- |
|     |     |     |     |     |     |      | summarise |            | the datasets |         | and tools  | adopted | so      | far   | in ML |
Theory
| 0.7% |     |     |     |     |     |     | testing. |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thefourdifferentanglesforpresentationofrelatedwork
Software Engineering
38.2%
aswellasthestatisticalsummary,analysis,andcomparison,
|     |     |     |     |     |     |     | enable | us to | observe | the | research | focus, | trend, | challenges, |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ------- | --- | -------- | ------ | ------ | ----------- | --- |
Figure7:PublicationVenueDistribution
|     |     |     |     |     |     |     | opportunities, |     | and | directions | of  | ML testing. |     | These | results |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ---------- | --- | ----------- | --- | ----- | ------- |
arepresentedinSection10.
4.4 PaperOrganisation
|            |        |            |               |         |     |               | 5 ML | TESTING |           | WORKFLOW |         |          |       |     |        |
| ---------- | ------ | ---------- | ------------- | ------- | --- | ------------- | ---- | ------- | --------- | -------- | ------- | -------- | ----- | --- | ------ |
| We present | the    | literature | review        | from    | two | aspects: 1)   | a    |         |           |          |         |          |       |     |        |
|            |        |            |               |         |     |               | This | section | organises | ML       | testing | research | based |     | on the |
| literature | review | of         | the collected | papers, | 2)  | a statistical |      |         |           |          |         |          |       |     |        |
testingworkflowasshownbyFigure5.
| analysis | of the | collected         | papers, | datasets, | and | tools. The   |              |         |          |          |      |           |            |          |      |
| -------- | ------ | ----------------- | ------- | --------- | --- | ------------ | ------------ | ------- | -------- | -------- | ---- | --------- | ---------- | -------- | ---- |
|          |        |                   |         |           |     |              | ML           | testing | includes | offline  |      | testing   | and online | testing. |      |
| sections | and    | the corresponding |         | contents  | are | presented in |              |         |          |          |      |           |            |          |      |
|          |        |                   |         |           |     |              | Albarghouthi |         | and      | Vinitsky | [75] | developed | a          | fairness | spe- |
Table3.
|     |     |     |     |     |     |     | cification  | language |             | that can | be        | used for | the     | development |        |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | ----------- | -------- | --------- | -------- | ------- | ----------- | ------ |
|     |     |     |     |     |     |     | of run-time |          | monitoring, | in       | detecting | fairness | issues. |             | Such a |
Table3:ReviewSchema
|                |     |     |       |     |     |     | kind     | of run-time   | monitoring |         | belongs  | to  | the area | of      | online |
| -------------- | --- | --- | ----- | --- | --- | --- | -------- | ------------- | ---------- | ------- | -------- | --- | -------- | ------- | ------ |
| Classification |     | Sec | Topic |     |     |     |          |               |            |         |          |     |          |         |        |
|                |     |     |       |     |     |     | testing. | Nevertheless, |            | current | research |     | mainly   | centres | on     |
5.1 TestInputGeneration offlinetestingasintroducedbelow.Theproceduresthatare
|     |     | 5.2 | TestOracle |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5.3 TestAdequacy notcoveredbasedonourpapercollection,suchasrequire-
TestingWorkflow
5.4 TestPrioritisationandReduction ment analysis and regression testing and those belonging
5.5 BugReportAnalysis to online testing are discussed as research opportunities in
|     |     | 5.6 | DebugandRepair |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Section10.
|     |     | 5.7 | TestingFrameworkandTools |     |     |     |     |                     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------------ | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 6.1 | Correctness              |     |     |     |     |                     |     |     |     |     |     |     |     |
|     |     | 6.2 | ModelRevelance           |     |     |     | 5.1 | TestInputGeneration |     |     |     |     |     |     |     |
|     |     | 6.3 | RobustnessandSecurity    |     |     |     |     |                     |     |     |     |     |     |     |     |
Weorganisethetestinputgenerationresearchbasedonthe
|     |     | 6.4 | Efficiency |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
TestingProperties
|     |     | 6.5 | Fairness         |     |     |     | techniquesadopted. |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 6.6 | Interpretability |     |     |     |                    |     |     |     |     |     |     |     |     |
|     |     | 6.7 | Privacy          |     |     |     |                    |     |     |     |     |     |     |     |     |
5.1.1 Domain-specificTestInputSynthesis
|     |     | 7.1 | BugDetectioninData |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7.2 BugDetectioninLearningProgram Test inputs of ML testing can be classified into two cat-
TestingComponents7.3 BugDetectioninFramework egories: adversarial inputs and natural inputs. Adversarial
inputsareperturbedbasedontheoriginalinputs.Theymay
|                        |     | 8.1 | AutonomousDriving        |     |     |     |            |               |           |           |              |            |        |             |        |
| ---------------------- | --- | --- | ------------------------ | --- | --- | --- | ---------- | ------------- | --------- | --------- | ------------ | ---------- | ------ | ----------- | ------ |
| ApplicationScenario8.2 |     |     | MachineTranslation       |     |     |     |            |               |           |           |              |            |        |             |        |
|                        |     |     |                          |     |     |     | not belong |               | to normal | data      | distribution |            | (i.e., | maybe       | rarely |
|                        |     | 8.3 | NaturalLanguageInference |     |     |     |            |               |           |           |              |            |        |             |        |
|                        |     |     |                          |     |     |     | exist      | in practice), |           | but could | expose       | robustness |        | or security |        |
9.1 Timeline flaws. Natural inputs, instead, are those inputs that belong
|                     |     | 9.2 | ResearchDistributionamongCategories |     |     |     |        |      |              |     |             |             |     |           |     |
| ------------------- | --- | --- | ----------------------------------- | --- | --- | --- | ------ | ---- | ------------ | --- | ----------- | ----------- | --- | --------- | --- |
|                     |     |     |                                     |     |     |     | to the | data | distribution | of  | a practical | application |     | scenario. |     |
| Summary&Analysis9.3 |     |     | ResearchDistributionamongProperties |     |     |     |        |      |              |     |             |             |     |           |     |
9.4 Datasets Here we introduce the related work that aims to generate
9.5 Open-sourceToolSupport naturalinputsviadomain-specifictestinputsynthesis.
DeepXplore[1]proposedawhite-boxdifferentialtesting
1) Literature Review. The papers in our collection are techniquetogeneratetestinputsforadeeplearningsystem.
organised and presented from four angles. We introduce Inspiredbytestcoverageintraditionalsoftwaretesting,the
the work about different testing workflow in Section 5. In authors proposed neuron coverage to drive test generation
Section6weclassifythepapersbasedontheMLproblems (we discuss different coverage criteria for ML testing in
they target, including functional properties like correctness Section 5.2.3). The test inputs are expected to have high
and model relevance and non-functional properties like neuron coverage. Additionally, the inputs need to expose
robustness, fairness, privacy, and interpretability. Section 7 differencesamongdifferentDNNmodels,aswellasbelike
introduces the testing technologies on detecting bugs in real-worlddataasmuchaspossible.Thejointoptimisation
data, learning programs, and ML frameworks, libraries, algorithm iteratively uses a gradient search to find a modi-
or platforms. Section 8 introduces the testing techniques fied input that satisfies all of these goals. The evaluation of

11
DeepXplore indicates that it covers 34.4% and 33.2% more 5.1.2 FuzzandSearch-basedTestInputGeneration
| neurons | than the | same | number of | randomly | picked | inputs |     |     |     |     |     |     |     |     |
| ------- | -------- | ---- | --------- | -------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
Fuzztestingisatraditionalautomatictestingtechniquethat
andadversarialinputs. generatesrandomdataasprograminputstodetectcrashes,
To create useful and effective data for autonomous memory leaks, failed (built-in) assertions, etc, with many
| driving | systems, | DeepTest | [76] performed |     | greedy | search |     |     |     |     |     |     |     |     |
| ------- | -------- | -------- | -------------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
sucessfullyapplicationtosystemsecurityandvulnerability
with nine different realistic image transformations: chan- detection [9]. As another widely used test generation tech-
ging brightness, changing contrast, translation, scaling, ho- nique,search-basedtestgenerationoftenusesmetaheuristic
| rizontal      | shearing, | rotation,   | blurring, | fog            | effect, | and rain |             |            |     |                 |          |         |             |       |
| ------------- | --------- | ----------- | --------- | -------------- | ------- | -------- | ----------- | ---------- | --- | --------------- | -------- | ------- | ----------- | ----- |
|               |           |             |           |                |         |          | search      | techniques | to  | guide           | the fuzz | process | for more    | ef-   |
| effect. There | are       | three types | of image  | transformation |         | styles   |             |            |     |                 |          |         |             |       |
|               |           |             |           |                |         |          | ficient and | effective  |     | test generation |          | [17],   | [87], [88]. | These |
providedinOpenCV5:linear,affine,andconvolutional.The
|     |     |     |     |     |     |     | two techniques |     | have | also been | proved | to  | be effective | in  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---- | --------- | ------ | --- | ------------ | --- |
evaluation of DeepTest uses the Udacity self-driving car exploringtheinputspaceofMLtesting:
challengedataset[77].Itdetectedmorethan1,000erroneous
Odenaetal.[89]presentedTensorFuzz.TensorFuzzuseda
behaviours on CNNs and RNNs with low false positive simplenearestneighbourhillclimbingapproachtoexplore
rates6. achievable coverage over valid input space for Tensorflow
| Generative |     | adversarial | networks | (GANs) | [78] | are al- |         |     |             |           |     |         |               |     |
| ---------- | --- | ----------- | -------- | ------ | ---- | ------- | ------- | --- | ----------- | --------- | --- | ------- | ------------- | --- |
|            |     |             |          |        |      |         | graphs, | and | to discover | numerical |     | errors, | disagreements |     |
gorithms to generate models that approximate the mani- betweenneuralnetworksandtheirquantizedversions,and
folds and distribution on a given set of data. GAN has surfacingundesirablebehaviourinRNNs.
been successfully applied to advanced image transforma- DLFuzz,proposedbyGuoetal.[90],isanotherfuzztest
tion (e.g., style transformation, scene transformation) that generationtoolbasedontheimplementationofDeepXplore
look at least superficially authentic to human observers. withnueroncoverageasguidance.DLFuzzaimstogenerate
Zhang et al. [79] applied GAN to deliver driving scene- adversarialexamples.Thegenerationprocessthusdoesnot
basedtestgenerationwithvariousweatherconditions.They require similar functional deep learning systems for cross-
sampled images from Udacity Challenge dataset [77] and referencing check like DeepXplore and TensorFuzz. Rather,
YouTubevideos(snowyorrainyscenes),andfedtheminto it needs only minimum changes over the original inputs
| theUNITframework7 |     | fortraining.Thetrainedmodeltakes |     |     |     |     |         |       |            |      |         |        |          |     |
| ----------------- | --- | -------------------------------- | --- | --- | --- | --- | ------- | ----- | ---------- | ---- | ------- | ------ | -------- | --- |
|                   |     |                                  |     |     |     |     | to find | those | new inputs | that | improve | neural | coverage | but |
the whole Udacity images as the seed inputs and yields have different predictive results from the original inputs.
transformedimagesasgeneratedtests. ThepreliminaryevaluationonMNISTandImageNetshows
| Zhou | et al. | [81] proposed | DeepBillboard |     | to generate | real- |     |     |     |     |     |     |     |     |
| ---- | ------ | ------------- | ------------- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
thatcomparedwithDeepXplore,DLFuzzisabletogenerate
worldadversarialbillboardsthatcantriggerpotentialsteer- 135% to 584.62% more inputs with 20.11% less time con-
| ingerrorsofautonomousdrivingsystems. |     |     |     |     |     |     | sumption. |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
Totestaudio-baseddeeplearningsystems,Duetal.[82] Xie et al. [91] presented a metamorphic transformation
designed a set of transformations tailored to audio in- based coverage guided fuzzing technique, DeepHunter,
puts considering background noise and volume variation. whichleveragesbothneuroncoverageandcoveragecriteria
Theyfirstabstractedandextractedaprobabilistictransition presented by DeepGauge [92]. DeepHunter uses a more
model from an RNN. Based on this, stateful testing criteria fine-grained metamorphic mutation strategy to generate
are defined and used to guide test generation for stateful tests, which demonstrates the advantage in reducing the
machinelearningsystem. false positive rate. It also demonstrates its advantage in
To test the image classification platform when classify- achievinghighcoverageandbugdetectioncapability.
ing biological cell images, Ding et al. [83] built a testing Wicker et al. [93] proposed feature-guided test gen-
framework for biological cell classifiers. The framework eration. They adopted Scale-Invariant Feature Transform
iteratively generates new images and uses metamorphic (SIFT) to identify features that represent an image with a
relationsfortesting.Forexample,theygeneratenewimages Gaussian mixture model, then transformed the problem of
byincreasingthenumber/shapeofartificialmitochondrion finding adversarial examples into a two-player turn-based
into the biological cell images, which can arouse easy-to- stochastic game. They used Monte Carlo Tree Search to
identifychangesintheclassificationresults. identify those elements of an image most vulnerable as the
Rabin et al. [84] discussed the possibilities of testing meansofgeneratingadversarialexamples.Theexperiments
code2vec(acodeembeddingapproach[85])withsemantic- show that their black-box approach is competitive with
preservingprogramtransformationsservingastestinputs. somestate-of-the-artwhite-boxmethods.
To test machine translation systems, Sun et al. [86] Instead of targeting supervised learning, Uesato et
automatically generate test inputs via mutating the words al.[94]proposedtoevaluatereinforcementlearningwithad-
|                |         |     |                   |     |             |       | versarial | example | generation. |     | The | detection | of catastrophic |     |
| -------------- | ------- | --- | ----------------- | --- | ----------- | ----- | --------- | ------- | ----------- | --- | --- | --------- | --------------- | --- |
| in translation | inputs. | In  | order to generate |     | translation | pairs |           |         |             |     |     |           |                 |     |
that ought to yield consistent translations, their approach failures is expensive because failures are rare. To alleviate
conductswordreplacementbasedonwordembeddingsim- the consequent cost of finding such failures, the authors
|     |     |     |     |     |     |     | proposed | to use | a failure | probability |     | predictor | to estimate |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | --------- | ----------- | --- | --------- | ----------- | --- |
ilarities.Manualinspectionindicatesthatthetestgeneration
has a high precision (99%) on generating input pairs with theprobabilitythattheagentfails,whichwasdemonstrated
| consistenttranslations. |     |     |     |     |     |     | tobebotheffectiveandefficient. |     |              |     |          |             |           |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | ------------ | --- | -------- | ----------- | --------- | --- |
|                         |     |     |     |     |     |     | There                          | are | also fuzzers | for | specific | application | scenarios |     |
5 https://github.com/itseez/opencv(2015)
|     |     |     |     |     |     |     | other than | image | classifications. |     | Zhou | et al. | [95] combined |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ---------------- | --- | ---- | ------ | ------------- | --- |
6 Theexamplesofdetectederroneousbehavioursareavailableathttps:
fuzzingandmetamorphictestingtotesttheLiDARobstacle-
//deeplearningtest.github.io/deepTest/.
|     |     |     |     |     |     |     | perception | module | of  | real-life | self-driving |     | cars, and | repor- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | --------- | ------------ | --- | --------- | ------ |
7 ArecentDNN-basedmethodtoperformimage-to-imagetransforma-
|     |     |     |     |     |     |     | ted previously |     | unknown | software |     | faults. | Jha et | al. [96] |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | -------- | --- | ------- | ------ | -------- |
tion[80]

12
investigated how to generate the most effective test cases listed three such challenges for neural networks in their
(thefaultsthataremostlikelytoleadtoviolationsofsafety paper, which work for other ML modes as well: (1) the
conditions) via modelling the fault injection as a Bayesian networkshave noexplicitbranching;(2) thenetworksmay
network. The evaluation, based on two production-grade be highly non-linear, with no well-developed solvers for
AV systems from NVIDIA and Baidu, revealed many situ- constraints; and (3) there are scalability issues because the
ationswherefaultsleadtosafetyviolations. structures of the ML models are usually very complex and
UdeshiandChattopadhyay[97]generateinputsfortext are beyond the capabilities of current symbolic reasoning
| classification |     | tasks and | produce | a   | fuzzing approach | that | tools. |     |     |     |     |     |     |     |
| -------------- | --- | --------- | ------- | --- | ---------------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
considers the grammar under test as well as the distance Consideringthesechallenges,Gopinath[108]introduced
betweeninputs.Nieetal.[98]andWangetal.[99]mutated DeepCheck. It transforms a Deep Neural Network (DNN)
the sentences in NLI (Natural Language Inference) tasks to into a program to enable symbolic execution to find pixel
generatetestinputsforrobustnesstesting.Chanetal.[100] attacksthathavethesameactivationpatternastheoriginal
generated adversarial examples for DNC to expose its ro- image.Inparticular,theactivationfunctionsinDNNfollow
bustness problems. Udeshi et al. [101] focused much on an IF-Elsebranch structure,which canbe viewedas apath
individualfairnessandgeneratedtestinputsthathighlight throughthetranslatedprogram.DeepCheckisabletocreate
the discriminatory nature of the model under test. We give 1-pixeland2-pixelattacksbyidentifyingmostofthepixels
details about these domain-specific fuzz testing techniques or pixel-pairs that the neural network fails to classify the
| inSection8. |     |     |     |     |     |     | correspondingmodifiedimages. |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
Tuncali et al. [102] proposed a framework for testing Similarly, Agarwal et al. [109] apply LIME [110], a local
autonomousdrivingsystems.Intheirworktheycompared explanation tool that approximates a model with linear
threetestgenerationstrategies:randomfuzztestgeneration, models, decision trees, or falling rule lists, to help get the
covering array [103] + fuzz test generation, and covering pathusedinsymbolicexecution.Theirevaluationbasedon
+
array search-based test generation (using Simulated An- 8opensourcefairnessbenchmarksshowsthatthealgorithm
nealing algorithm [104]). The results indicated that the test generates 3.72 times more successful test cases than the
generation strategy with search-based technique involved randomtestgenerationapproachTHEMIS[5].
hasthebestperformanceindetectingglancingbehaviours. Sun et al. [111] presented DeepConcolic, a dynamic
|     |     |     |     |     |     |     | symbolicexecution |     | testingmethodfor |     |     | DNNs.Concreteex- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------------- | --- | --- | ---------------- | --- | --- |
5.1.3 SymbolicExecutionBasedTestInputGeneration ecution is used to direct the symbolic analysis to particular
|          |           |      |         |          |           |         | MC/DC | criteria’ | condition, | through |     | concretely | evaluating |     |
| -------- | --------- | ---- | ------- | -------- | --------- | ------- | ----- | --------- | ---------- | ------- | --- | ---------- | ---------- | --- |
| Symbolic | execution | is a | program | analysis | technique | to test |       |           |            |         |     |            |            |     |
whether certain properties can be violated by the software givenpropertiesoftheMLmodels.DeepConcolicexplicitly
under test [105]. Dynamic Symbolic Execution (DSE, also takes coverage requirements as input. The authors report
thatityieldsover10%higherneuroncoveragethanDeepX-
| called concolic |     | testing) | is a | technique | used to | automatic- |     |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ---- | --------- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
ally generate test inputs that achieve high code coverage. plorefortheevaluatedmodels.
| DSE executes |     | the program |     | under | test with | random test |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------- | --- | ----- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
5.1.4 SyntheticDatatoTestLearningProgram
inputsandperformssymbolicexecutioninparalleltocollect
|          |             |          |     |      |            |           | Murphy | et al. | [112] generated |     | data with | repeating | values, |     |
| -------- | ----------- | -------- | --- | ---- | ---------- | --------- | ------ | ------ | --------------- | --- | --------- | --------- | ------- | --- |
| symbolic | constraints | obtained |     | from | predicates | in branch |        |        |                 |     |           |           |         |     |
statementsalongtheexecutiontraces.Theconjunctionofall missing values, or categorical data for testing two ML
symbolicconstraintsalongapathiscalledapathcondition. rankingapplications.Brecketal.[45]usedsynthetictraining
datathatadheretoschemaconstraintstotriggerthehidden
| When generating |     | tests, | DSE | randomly | chooses | one test |     |     |     |     |     |     |     |     |
| --------------- | --- | ------ | --- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
input from the input domain, then uses constraint solving assumptions in the code that do not agree with the con-
to reach a target branch condition in the path [106]. DSE straints. Zhang et al. [54] used synthetic data with known
|          |       |                |     |     |                |          | distributions |     | to test overfitting. |     | Nakajima | and | Bui | [113] |
| -------- | ----- | -------------- | --- | --- | -------------- | -------- | ------------- | --- | -------------------- | --- | -------- | --- | --- | ----- |
| has been | found | to be accurate |     | and | effective, and | has been |               |     |                      |     |          |     |     |       |
theprimarytechniqueusedbysomevulnerabilitydiscovery alsomentionedthepossibilityofgeneratingsimpledatasets
tools[107]. withsomepredictablecharacteristicsthatcanbeadoptedas
pseudooracles.
| In ML   | testing,  | the model’s |     | performance | is       | decided, not |     |     |     |     |     |     |     |     |
| ------- | --------- | ----------- | --- | ----------- | -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| only by | the code, | but also    | by  | the data,   | and thus | symbolic     |     |     |     |     |     |     |     |     |
execution has two application scenarios: either on the data 5.2 TestOracle
oronthecode. Test oracle identification is one of the key problems in ML
Symbolic analysis was applied to generate more effect- testing. It is needed in order to enable the judgement of
ive tests to expose bugs by Ramanathan and Pullum [7]. whether a bug exists. This is the so-called ‘Oracle Prob-
| They proposed |     | a combination |     | of symbolic | and | statistical |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
lem’[9].
approaches to efficiently find test cases. The idea is to In ML testing, the oracle problem is challenging, be-
distance-theoretically abstract the data using symbols to cause many machine learning algorithms are probabilistic
helpsearchforthosetestinputswhereminorchangesinthe
|     |     |     |     |     |     |     | programs. | In  | this section, | we  | list several | popular | types | of  |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | ------------ | ------- | ----- | --- |
inputwillcausethealgorithmtofail.Theevaluationofthe testoraclethathavebeenstudiedforMLtesting,i.e.,meta-
implementation of a k-means algorithm indicates that the morphic relations, cross-referencing, and model evaluation
| approachisabletodetectsubtleerrorssuchasbit-flips.The |     |     |     |     |     |     | metrics. |     |     |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
examinationoffalsepositivesmayalsobeafutureresearch
5.2.1 MetamorphicRelationsasTestOracles
interest.
When applying symbolic execution on the machine Metamorphic relations was proposed by Chen et al. [114]
learning code, there are many challenges. Gopinath [108] toamelioratethetestoracleproblemintraditionalsoftware

13
testing. A metamorphic relation refers to the relationship are necessary. The differences in the metamorphic relations
betweenthesoftwareinputchangeandoutputchangedur- between SVM and neural networks are also discussed in
ing multiple program executions. For example, to test the [120]. Dwarakanath et al. [121] applied metamorphic rela-
implementationofthefunctionsin(x),onemaycheckhow tions to image classifications with SVM and deep learning
thefunctionoutputchangeswhentheinputischangedfrom systems. The changes on the data include changing the
xtoπ−x.Ifsin(x)differsfromsin(π−x),thisobservation featureorinstanceorders,linearscalingofthetestfeatures,
signalsanerrorwithoutneedingtoexaminethespecificval- normalisation or scaling up the test data, or changing the
uescomputedbytheimplementation.sin(x) = sin(π−x) convolutionoperationorderofthedata.TheproposedMRs
is thus a metamorphic relation that plays the role of test are able to find 71% of the injected bugs. Sharma and
oracle(alsonamed‘pseudooracle’)tohelpbugdetection. Wehrheim [122] considered fine-grained data transforma-
InMLtesting,metamorphicrelationsarewidelystudied tions such as changing feature names, renaming feature
to tackle the oracle problem. Many metamorphic relations values to test fairness. They studied 14 classifiers, none of
arebasedontransformationsoftrainingortestdatathatare themwerefoundtobesensitivetofeaturenameshuffling.
expected to yield unchanged or certain expected changes Zhang et al. [54] proposed Perturbed Model Validation
in the predictive output. There are different granularities (PMV) which combines metamorphic relation and data
of data transformations when studying the correspond- mutation to detect overfitting. PMV mutates the training
ing metamorphic relations. Some transformations conduct data via injecting noise in the training data to create per-
coarse-grained changes such as enlarging the dataset or turbed training datasets, then checks the training accuracy
changingthedataorder,withoutchangingeachsingledata decreaseratewhenthenoisedegreeincreases.Thefasterthe
instance.Wecallthesetransformations‘Coarse-graineddata training accuracy decreases, the less the machine learning
transformations’.Sometransformationsconductdatatrans- modeloverfits.
formationsviasmallerchangesoneachdatainstance,such Al-Azani and Hassine [123] studied the metamorphic
as mutating the attributes, labels, or pixels of images, and relations of Naive Bayes, k-Nearest Neighbour, as well as
arereferredtoas‘fine-grained’datatransformationsinthis their ensemble classifier. It turns out that the metamorphic
paper.Therelatedworksofeachtypeoftransformationsare relations necessary for Naive Bayes and k-Nearest Neigh-
introducedbelow. bourmaybenotnecessaryfortheirensembleclassifier.
Coarse-grained Data Transformation. As early as in 2008, Tian et al. [76] and Zhang et al. [79] stated that the
Murphy et al. [115] discuss the properties of machine autonomousvehiclesteeringangleshouldnotchangesigni-
learning algorithms that may be adopted as metamorphic ficantly or stay the same for the transformed images under
relations. Six transformations of input data are introduced: differentweatherconditions.Ramanagopaletal.[124]used
additive, multiplicative, permutative, invertive, inclusive, the classification consistency of similar images to serve
and exclusive. The changes include adding a constant to as test oracles for testing self-driving cars. The evaluation
numerical values; multiplying numerical values by a con- indicates a precision of 0.94 when detecting errors in unla-
stant; permuting the order of the input data; reversing the belleddata.
order of the input data; removing a part of the input data; Additionally,Xieetal.[125]proposedMETTLE,ameta-
adding additional data. Their analysis is on MartiRank, morphic testing approach for unsupervised learning val-
SVM-Light, and PAYL. Although unevaluated in the initial idation. METTLE has six types of different-grained meta-
2008 paper, this work provided a foundation for determin- morphic relations that are specially designed for unsu-
ing the relationships and transformations that can be used pervisedlearners.Thesemetamorphicrelationsmanipulate
forconductingmetamorphictestingformachinelearning. instanceorder,distinctness,density,attributes,orinjectout-
Ding et al. [116] proposed 11 metamorphic relations liersofthedata.Theevaluationwasbasedonsyntheticdata
to test deep learning systems. At the dataset level, the generated by Scikit-learn, showing that METTLE is prac-
metamorphic relations were also based on training data or tical and effective in validating unsupervised learners. Na-
test data transformations that were not supposed to affect kajima et al. [113], [126] discussed the possibilities of using
classification accuracy,such as adding 10% trainingimages different-grainedmetamorphicrelationstofindproblemsin
into each category of the training data set or removing one SVM and neural networks, such as to manipulate instance
category of data from the dataset. The evaluation is based order or attribute order and to reverse labels and change
onaclassificationofbiologicalcellimages. attributevalues,ortomanipulatethepixelsinimages.
Murphy et al. [117] presented function-level meta- Metamorphic Relations between Different Datasets. The
morphic relations. The evaluation on 9 machine learning consistencyrelationsbetween/amongdifferentdatasetscan
applications indicated that functional-level properties were also be regarded as metamorphic relations that could be
170%moreeffectivethanapplication-levelproperties. applied to detect data bugs. Kim et al. [127] and Breck et
Fine-grained Data Transformation. In 2009, Xie et al. [118] al.[45]studiedthemetamorphicrelationsbetweentraining
proposedtousemetamorphicrelationsthatwerespecificto data and new data. If the training data and new data
a certain model to test the implementations of supervised have different distributions, the training data may not be
classifiers. The paper presents five types of metamorphic adequate. Breck et al. [45] also studied the metamorphic
relations that enable the prediction of expected changes to relations among different datasets that are close in time:
the output (such as changes in classes, labels, attributes) these datasets are expected to share some characteristics
based on particular changes to the input. Manual analysis because it is uncommon to have frequent drastic changes
of the implementation of KNN and Naive Bayes from tothedata-generationcode.
Weka [119] indicates that not all metamorphic relations Frameworks to Apply Metamorphic Relations. Murphy

14
et al. [128] implemented a framework called Amsterdam comparestheoutputs(i.e.,translations)ofdifferentmutated
to automate the process of using metamorphic relations to inputs,andpickstheoutputthatsharesthemostsimilarity
detect ML bugs. The framework reduces false positives via withothersasasuperiortranslationcandidate.
settingthresholdswhendoingresultcomparison.Theyalso
developedCorduroy[117],whichextendedJavaModelling 5.2.3 MeasurementMetricsforDesigningTestOracles
Languagetoletdevelopersspecifymetamorphicproperties
Someworkhaspresenteddefinitionsorstatisticalmeasure-
andgeneratetestcasesforMLtesting.
|     |           |      |         |     |      |                    |     | ments of | non-functional |     | features | of  | ML  | systems | including |     |
| --- | --------- | ---- | ------- | --- | ---- | ------------------ | --- | -------- | -------------- | --- | -------- | --- | --- | ------- | --------- | --- |
| We  | introduce | more | related |     | work | on domain-specific |     |          |                |     |          |     |     |         |           |     |
robustness[137],fairness[138],[139],[140],andinterpretab-
| metamorphic |     | relations | of testing |     | autonomous |     | driving, | Dif-        |        |       |              |     |     |            |         |     |
| ----------- | --- | --------- | ---------- | --- | ---------- | --- | -------- | ----------- | ------ | ----- | ------------ | --- | --- | ---------- | ------- | --- |
|             |     |           |            |     |            |     |          | ility [65], | [141]. | These | measurements |     | are | not direct | oracles |     |
ferentiableNeuralComputer(DNC)[100],machinetransla-
|              |       |        |        |            |     |      |                | for testing, | but | are essential |     | for testers | to  | understand |     | and |
| ------------ | ----- | ------ | ------ | ---------- | --- | ---- | -------------- | ------------ | --- | ------------- | --- | ----------- | --- | ---------- | --- | --- |
| tion systems | [86], | [129], | [130], | biological |     | cell | classification |              |     |               |     |             |     |            |     |     |
evaluatethepropertyundertest,andtoprovidesomeactual
| [83], and | audio-based |     | deep | learning |     | systems | [82] in | Sec-       |          |             |     |      |     |          |       |     |
| --------- | ----------- | --- | ---- | -------- | --- | ------- | ------- | ---------- | -------- | ----------- | --- | ---- | --- | -------- | ----- | --- |
|           |             |     |      |          |     |         |         | statistics | that can | be compared |     | with | the | expected | ones. | For |
tion8.
|     |     |     |     |     |     |     |     | example,thedefinitionsofdifferenttypesoffairness |       |         |     |     |         |        |        | [138], |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------ | ----- | ------- | --- | --- | ------- | ------ | ------ | ------ |
|     |     |     |     |     |     |     |     | [139], [140]                                     | (more | details | are | in  | Section | 6.5.1) | define | the    |
5.2.2 Cross-ReferencingasTestOracles
|     |     |     |     |     |     |     |     | conditions | an ML | system | has | to satisfy |     | without | which | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ------ | --- | ---------- | --- | ------- | ----- | --- |
Cross-ReferencingisanothertypeoftestoracleforMLtest-
systemisnotfair.Thesedefinitionscanbeadopteddirectly
| ing, including |     | differential |     | Testing | and | N-version | Program- |     |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | --- | ------- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
todetectfairnessviolations.
| ming. Differential |     | testing |     | is a traditional |     | software |     | testing |     |     |     |     |     |     |     |     |
| ------------------ | --- | ------- | --- | ---------------- | --- | -------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
ExceptforthesepopulartestoraclesinMLtesting,there
| technique    | that  | detects   | bugs | by      | observing | whether | similar   |          |                      |     |     |       |      |       |            |     |
| ------------ | ----- | --------- | ---- | ------- | --------- | ------- | --------- | -------- | -------------------- | --- | --- | ----- | ---- | ----- | ---------- | --- |
|              |       |           |      |         |           |         |           | are also | some domain-specific |     |     | rules | that | could | be applied |     |
| applications | yield | different |      | outputs | regarding |         | identical | in-      |                      |     |     |       |      |       |            |     |
todesigntestoracles.Wediscussedseveraldomain-specific
| puts [11], | [131]. | It is     | a testing |        | oracle | for detecting |     | com-       |        |            |        |            |           |        |       |      |
| ---------- | ------ | --------- | --------- | ------ | ------ | ------------- | --- | ---------- | ------ | ---------- | ------ | ---------- | --------- | ------ | ----- | ---- |
|            |        |           |           |        |        |               |     | rules that | could  | be adopted |        | as oracles | to        | detect | data  | bugs |
| piler bugs | [132]. | According |           | to the | study  | of Nejadgholi |     | and        |        |            |        |            |           |        |       |      |
|            |        |           |           |        |        |               |     | in Section | 7.1.1. | Kang       | et al. | [142]      | discussed | two    | types | of   |
Yang[133],5%to27%testoraclesfordeeplearninglibraries
|     |     |     |     |     |     |     |     | model assertions |     | under | the task | of  | car detection |     | in videos: |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----- | -------- | --- | ------------- | --- | ---------- | --- |
usedifferentialtesting.
|     |     |     |     |     |     |     |     | flickering | assertion | to  | detect | the flickering |     | in car | bounding |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | ------ | -------------- | --- | ------ | -------- | --- |
DifferentialtestingiscloselyrelatedwithN-versionpro-
box,andmulti-boxassertiontodetectnested-carbounding.
| gramming       | [134]:                  | N-version |                 | programming |          | aims         | to generate |               |           |           |          |                |          |          |              |      |
| -------------- | ----------------------- | --------- | --------------- | ----------- | -------- | ------------ | ----------- | ------------- | --------- | --------- | -------- | -------------- | -------- | -------- | ------------ | ---- |
|                |                         |           |                 |             |          |              |             | For example,  | if        | a car     | bounding | box            | contains |          | other boxes, |      |
| multiple       | functionally-equivalent |           |                 |             | programs | based        | on          | one           |           |           |          |                |          |          |              |      |
|                |                         |           |                 |             |          |              |             | the multi-box |           | assertion | fails.   | They           | also     | proposed |              | some |
| specification, | so                      | that      | the combination |             |          | of different | versions    |               |           |           |          |                |          |          |              |      |
|                |                         |           |                 |             |          |              |             | automatic     | fix rules | to        | set a    | new predictive |          | result   | when         | a    |
aremorefault-tolerantandrobust.
testassertionfails.
| Davis | and | Weyuker | [11] | discussed |     | the possibilities |     | of  |     |     |     |     |     |     |     |     |
| ----- | --- | ------- | ---- | --------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Therehasalsobeenadiscussionaboutthepossibilityof
| differential | testing     | for             | ‘non-testable’ |     |     | programs.    | The | idea       |     |          |       |             |     |         |          |     |
| ------------ | ----------- | --------------- | -------------- | --- | --- | ------------ | --- | ---------- | --- | -------- | ----- | ----------- | --- | ------- | -------- | --- |
|              |             |                 |                |     |     |              |     | evaluating | ML  | learning | curve | in lifelong |     | machine | learning |     |
| is that      | if multiple | implementations |                |     | of  | an algorithm |     | yield      |     |          |       |             |     |         |          |     |
astheoracle[143].AnMLsystemcanpassthetestoracleif
differentoutputsononeidenticalinput,thenatleastoneof
itcangrowandincreaseitsknowledgelevelovertime.
| the implementation |      |      | contains   | a defect. |           | Alebiosu | et al.       | [135] |     |     |     |     |     |     |     |     |
| ------------------ | ---- | ---- | ---------- | --------- | --------- | -------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| evaluated          | this | idea | on machine |           | learning, | and      | successfully |       |     |     |     |     |     |     |     |     |
found16faultsfrom7NaiveBayesimplementationsand13 5.3 TestAdequacy
faultsfrom19k-nearestneighbourimplementation.
|      |        |      |              |     |       |             |     | Test adequacy |     | evaluation | aims | to  | discover |     | whether | the |
| ---- | ------ | ---- | ------------ | --- | ----- | ----------- | --- | ------------- | --- | ---------- | ---- | --- | -------- | --- | ------- | --- |
| Pham | et al. | [48] | also adopted |     | cross | referencing |     | to test       |     |            |      |     |          |     |         |     |
existingtestshaveagoodfault-revealingability.Itprovides
| ML implementations, |     |     | but | focused | on  | the implementation |     |              |            |     |             |     |     |         |             |     |
| ------------------- | --- | --- | --- | ------- | --- | ------------------ | --- | ------------ | ---------- | --- | ----------- | --- | --- | ------- | ----------- | --- |
|                     |     |     |     |         |     |                    |     | an objective | confidence |     | measurement |     | on  | testing | activities. |     |
ofdeeplearninglibraries.TheyproposedCRADLE,thefirst
|     |     |     |     |     |     |     |     | The adequacy |     | criteria | can also | be  | adopted | to  | guide | test |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | -------- | -------- | --- | ------- | --- | ----- | ---- |
approachthatfocusesonfindingandlocalisingbugsindeep
|          |          |            |     |     |            |     |           | generation.    | Popular  |     | test adequacy |         | evaluation |          | techniques |     |
| -------- | -------- | ---------- | --- | --- | ---------- | --- | --------- | -------------- | -------- | --- | ------------- | ------- | ---------- | -------- | ---------- | --- |
| learning | software | libraries. |     | The | evaluation | was | conducted |                |          |     |               |         |            |          |            |     |
|          |          |            |     |     |            |     |           | in traditional | software |     | testing       | include | code       | coverage |            | and |
onthreelibraries(TensorFlow,CNTK,andTheano),11data-
mutationtesting,whicharealsoadoptedinMLtesting.
sets(includingImageNet,MNIST,andKGSGogame),and
| 30 pre-trained |     | models. | It turned |     | out that | CRADLE | detects |       |              |     |     |     |     |     |     |     |
| -------------- | --- | ------- | --------- | --- | -------- | ------ | ------- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
|                |     |         |           |     |          |        |         | 5.3.1 | TestCoverage |     |     |     |     |     |     |     |
104uniqueinconsistenciesand12bugs.
DeepXplore[1]andDLFuzz[90]useddifferentialtesting In traditional software testing, code coverage measures the
degreetowhichthesourcecodeofaprogramisexecutedby
astestoraclestofindeffectivetestinputs.Thosetestinputs
causingdifferentbehavioursamongdifferentalgorithmsor atestsuite[144].Thehighercoverageatestsuiteachieves,it
modelswerepreferredduringtestgeneration. ismoreprobablethatthehiddenbugscouldbeuncovered.
Most differential testing relies on multiple implementa- In other words, covering the code fragment is a necessary
tionsorversions,whileQinetal.[136]usedthebehaviours conditiontodetectthedefectshiddeninthecode.Itisoften
of ‘mirror’ programs, generated from the training data as desirabletocreatetestsuitestoachievehighercoverage.
pseudo oracles. A mirror program is a program generated Unlike traditional software, code coverage is seldom a
based on training data, so that the behaviours of the pro- demandingcriterionforMLtesting,sincethedecisionlogic
gramrepresentthetrainingdata.Ifthemirrorprogramhas of an ML model is not written manually but rather it is
similar behaviours on test data, it is an indication that the learned from training data. For example, in the study of
behaviour extracted from the training data suit test data as Pei et al. [1], 100% traditional code coverage is easy to
well. achieve with a single randomly chosen test input. Instead,
Sun et al. [86] applied cross reference in repairing researchersproposevarioustypesofcoverageforMLmod-
machine translation systems. Their approach, TransRepair, elsbeyondcodecoverage.

15
Neuron coverage. Pei et al. [1] proposed the first coverage the fundamental differences between neural networks and
criterion, neuron coverage, particularly designed for deep human-written programs. Their initial experiments with
learning testing. Neuron coverage is calculated as the ratio natural inputs found no strong correlation between the
ofthenumberofuniqueneuronsactivatedbyalltestinputs numberofmisclassifiedinputsinatestsetanditsstructural
and the total number of neurons in a DNN. In particular, a coverage.Duetotheblack-boxnatureofamachinelearning
neuron is activated if its output valueis larger than auser- system,itisnotclearhowsuchcriteriadirectlyrelatetothe
specifiedthreshold. system’sdecisionlogic.
Ma et al. [92] extended the concept of neuron coverage.
TheyfirstprofileaDNNbasedonthetrainingdata,sothat 5.3.2 MutationTesting
theyobtaintheactivationbehaviourofeachneuronagainst
In traditional software testing, mutation testing evalu-
the training data. Based on this, they propose more fine-
ates the fault-revealing ability of a test suite via injecting
grained criteria, k-multisection neuron coverage, neuron
faults [144], [151]. The ratio of detected faults against all
boundarycoverage,andstrongneuronactivationcoverage,
injectedfaultsiscalledtheMutationScore.
to represent the major functional behaviour and corner
In ML testing, the behaviour of an ML system depends
behaviourofaDNN.
on, not only the learning code, but also data and model
MC/DC coverage variants. Sun et al. [145] proposed four
structure. Ma et al. [152] proposed DeepMutation, which
testcoveragecriteriathataretailoredtothedistinctfeatures
mutates DNNs at the source level or model level, to make
of DNN inspired by the MC/DC coverage criteria [146].
minor perturbation on the decision boundary of a DNN.
MC/DC observes the change of a Boolean variable, while
Based on this, a mutation score is defined as the ratio of
their proposed criteria observe a sign, value, or distance
testinstancesofwhichresultsarechangedagainstthetotal
change of a neuron, in order to capture the causal changes
numberofinstances.
in the test inputs. The approach assumes the DNN to be a
Shen et al. [153] proposed five mutation operators for
fully-connectednetwork,anddoesnotconsiderthecontext
DNNsandevaluatedpropertiesofmutationontheMINST
of a neuron in its own layer as well as different neuron
dataset. They pointed out that domain-specific mutation
combinationswithinthesamelayer[147].
operatorsareneededtoenhancemutationanalysis.
Layer-level coverage. Ma et al. [92] also presented layer-
Comparedtostructuralcoveragecriteria,mutationtest-
levelcoveragecriteria,whichconsidersthetophyperactive
ing based criteria are more directly relevant to the decision
neurons and their combinations (or the sequences) to char-
boundaryofaDNN.Forexample,aninputdatathatisnear
acterisethebehavioursofaDNN.Thecoverageisevaluated
the decision boundary of a DNN, could more easily detect
to have better performance together with neuron coverage
theinconsistencybetweenaDNNanditsmutants.
basedondatasetMNISTandImageNet.Intheirfollowing-
up work [148], [149], they further proposed combinatorial
5.3.3 SurpriseAdequacy
testingcoverage,whichchecksthecombinatorialactivation
Kim et al. [127] introduced surprise adequacy to measure
statusoftheneuronsineachlayerviacheckingthefraction
the coverage of discretised input surprise range for deep
of neurons activation interaction in a layer. Sekhon and
learning systems. They argued that test diversity is more
Fleming[147]definedacoveragecriteriathatlooksfor1)all
meaningfulwhenbeingmeasuredwithrespecttothetrain-
pairsofneuronsinthesamelayerhavingallpossiblevalue
ingdata.A‘good’testinputshouldbe‘sufficientlybutnot
combinations, and 2) all pairs of neurons in consecutive
overly surprising’ comparing with the training data. Two
layershavingallpossiblevaluecombinations.
measurements of surprise were introduced: one is based
State-levelcoverage.Whileaftermentionedcriteria,tosome
on Keneral Density Estimation (KDE) to approximate the
extent, capture the behaviours of feed-forward neural net-
likelihoodofthesystemhavingseenasimilarinputduring
works, they do not explicitly characterise stateful machine
training,theotherisbasedonthedistancebetweenvectors
learning system like recurrent neural network (RNN). The
representingtheneuronactivationtracesofthegiveninput
RNN-based ML approach has achieved notable success
and the training data (e.g., Euclidean distance). These cri-
in applications that handle sequential inputs, e.g., speech
teriacanbeadoptedtodetectadversarialexamples.Further
audio, natural language, cyber physical control signals. In
investigationisrequiredtodeterminewhethersuchcriteria
order to analyse such stateful ML systems, Du et al. [82]
enable the behaviour boundaries of ML models to be ap-
proposedthefirstsetoftestingcriteriaspecialisedforRNN-
proximatedintermsofsurprise.Itwillalsobeinterestingfor
basedstatefuldeeplearningsystems.Theyfirstabstracteda
future work to study the relationship between adversarial
stateful deep learning system as a probabilistic transition
examples,naturalerrorsamples,andsurprise-basedcriteria.
system. Based on the modelling, they proposed criteria
based on the state and traces of the transition system, to
5.3.4 Rule-basedCheckingofTestAdequacy
capturethedynamicstatetransitionbehaviours.
LimitationsofCoverageCriteria.Althoughtherearediffer- To ensure the functionality of an ML system, there may be
enttypesofcoveragecriteria,mostofthemfocusonDNNs. some ‘typical’ rules that are necessary. Breck et al. [154]
Sekhon and Fleming [147] examined the existing testing offered 28 test aspects to consider and a scoring system
methods for DNNs and discussed the limitations of these usedbyGoogle.Theirfocusistomeasurehowwellagiven
criteria. machine learning system is tested. The 28 test aspects are
Most proposed coverage criteria are based on the struc- classifiedintofourtypes:1)thetestsfortheMLmodelitself,
ture of a DNN. Li et al. [150] pointed out the limitations 2) the tests for ML infrastructure used to build the model,
ofstructuralcoveragecriteriafordeepnetworkscausedby 3) the tests for ML data used to build the model, and 4)

16
theteststhatcheckwhethertheMLsystemworkscorrectly studied the symptoms and root causes of the bugs, the ex-
over time. Most of them are some must-to-check rules that istingchallengestodetectthebugsandhowthesebugsare
couldbeappliedtoguidetestgeneration.Forexample,the handled. They classified TensorFlow bugs into exceptions
trainingprocessshouldbereproducible;allfeaturesshould or crashes, low correctness, low efficiency, and unknown.
bebeneficial;thereshouldbenoothermodelthatissimpler Themajorcauseswerefoundtobeinalgorithmdesignand
but better in performance than the current one. Their re- implementations such as TensorFlow API misuse (18.9%),
searchindicatesthat,althoughMLtestingiscomplex,there unalignedtensor(13.7%),andincorrectmodelparameteror
aresharedpropertiestodesignsomebasictestcasestotest structure(21.7%)
thefundamentalfunctionalityoftheMLsystem. Banerjee et al. [161] analysed the bug reports of
autonomous driving systems from 12 autonomous vehicle
manufacturers that drove a cumulative total of 1,116,605
5.4 TestPrioritisationandReduction
milesin California.They usedNLP technologiestoclassify
Test input generation in ML has a very large input space thecausesofdisengagementsinto10types(Adisagreement
tocover.Ontheotherhand,weneedtolabeleverytestin- is a failure that causes the control of the vehicle to switch
stancesoastojudgepredictiveaccuracy.Thesetwoaspects from the software to the human driver). The issues in
lead to high test generation costs. Byun et al. [155] used machine learning systems and decision control account for
DNN metrics like cross entropy, surprisal, and Bayesian the primary cause of 64% of all disengagements based on
uncertainty to prioritise test inputs. They experimentally theirreportanalysis.
showedthatthesearegoodindicatorsofinputsthatexpose
unacceptable behaviours, which are also useful for retrain-
5.6 DebugandRepair
ing.
Generatingtestinputsisalsocomputationallyexpensive. Data Resampling. The generated test inputs introduced in
Zhang et al. [156] proposed to reduce costs by identi- Section 5.1 only expose ML bugs, but are also studied as
fying those test instances that denote the more effective a part of the training data and can improve the model’s
adversarial examples. The approach is a test prioritisation correctness through retraining. For example, DeepXplore
techniquethatranksthetestinstancesbasedontheirsensit- achieves up to 3% improvement in classification accuracy
ivity to noise, because the instances that are more sensitive by retraining a deep learning model on generated inputs.
tonoiseismorelikelytoyieldadversarialexamples. DeepTest[76]improvesthemodel’saccuracyby46%.
Li et. al [157] focused on test data reduction in oper- Ma et al. [162] identified the neurons responsible for
ational DNN testing. They proposed a sampling technique the misclassification and call them ‘faulty neurons’. They
guidedbytheneuronsinthelasthiddenlayerofaDNN,us- resampled training data that influence such faulty neurons
ingacross-entropyminimisationbaseddistributionapprox- tohelpimprovemodelperformance.
imation technique. The evaluation was conducted on pre- Debugging Framework Development. Dutta et al. [163]
trained models with three image datasets: MNIST, Udacity proposed Storm, a program transformation framework to
challenge, and ImageNet. The results show that, compared generate smaller programs that can support debugging for
to random sampling, their approach samples only half the machine learning testing. To fix a bug, developers usually
testinputs,yetitachievesasimilarlevelofprecision. need to shrink the program under test to write better bug
Ma et al. [158] proposed a set of test selection metrics reports and to facilitate debugging and regression testing.
basedonthenotionofmodelconfidence.Testinputsthatare Stormappliesprogramanalysisandprobabilisticreasoning
moreuncertaintothemodelsarepreferred,becausetheyare tosimplifyprobabilisticprograms,whichhelpstopinpoint
moreinformativeandshouldbeusedtoimprovethemodel theissuesmoreeasily.
if being included during retraining. The evaluation shows Caietal.[164]presentedtfdbg,adebuggerforMLmod-
that their test selection approach has 80% more gain than els built on TensorFlow, containing three key components:
randomselection. 1)theAnalyzer,whichmakesthestructureandintermediate
state of the runtime graph visible; 2) the NodeStepper,
whichenablesclientstopause,inspect,ormodifyatagiven
5.5 BugReportAnalysis
nodeofthegraph;3)theRunStepper,whichenablesclients
Thung et al. [159] were the first to study machine learning to take higher level actions between iterations of model
bugsviaanalysingthebugreportsofmachinelearningsys- training.Vartaketal.[165]proposedtheMISTIQUEsystem
tems.500bugreportsfromApacheMahout,ApacheLucene, to capture, store, and query model intermediates to help
and Apache OpenNLP were studied. The explored prob- the debug. Krishnan and Wu [166] presented PALM, a tool
lems included bug frequency, bug categories, bug severity, that explains a complex model with a two-part surrogate
and bug resolution characteristics such as bug-fix time, model: a meta-model that partitions the training data and
effort, and file number. The results indicated that incorrect a set of sub-models that approximate the patterns within
implementation counts for the largest proportion of ML eachpartition.PALMhelpsdevelopersfindoutthetraining
bugs,i.e.,22.6%ofbugsareduetoincorrectimplementation data that impacts prediction the most, and thereby target
of defined algorithms. Implementation bugs are also the the subset of training data that account for the incorrect
mostseverebugs,andtakelongertofix.Inaddition,15.6% predictionstoassistdebugging.
ofbugsarenon-functionalbugs.5.6%ofbugsaredatabugs. Fix Understanding. Fixing bugsin many machine learning
Zhang et al. [160] studied 175 TensorFlow bugs, based systems is difficult because bugs can occur at multiple
on the bug reports from Github or StackOverflow. They pointsindifferentcomponents.Nushietal.[167]proposed

17
ahuman-in-the-loopapproachthatsimulatespotentialfixes 6.1 Correctness
indifferentcomponentsthroughhumancomputationtasks:
Correctness concerns the fundamental function accuracy
humanswereaskedtosimulateimprovedcomponentstates.
of an ML system. Classic machine learning validation is
The improvements of the system are recorded and com-
the most well-established and widely-used technology for
pared,toprovideguidancetodesignersabouthowtheycan
correctnesstesting.Typicalmachinelearningvalidationap-
bestimprovethesystem.
proaches are cross-validation and bootstrap. The principle
Program Repair. Albarghouthi et al. [168] proposed a is to isolate test data via data sampling to check whether
distribution-guided inductive synthesis approach to repair the trained model fits new cases. There are several ap-
decision-making programs such as machine learning pro- proaches to perform cross-validation. In hold out cross-
grams.Thepurposeistoconstructanewprogramwithcor- validation [174], the data are split into two parts: one part
rect predictive output, but with similar semantics with the becomes the training data and the other part becomes test
original program. Their approach uses sampled instances data8. In k-fold cross-validation, the data are split into k
and the predicted outputs to drive program synthesis in equal-sized subsets: one subset used as the test data and
whichtheprogramisencodedbasedonSMT. the remaining k − 1 as the training data. The process is
then repeated k times, with each of the subsets serving
as the test data. In leave-one-out cross-validation, k-fold
5.7 GeneralTestingFrameworkandTools cross-validation is applied, where k is the total number
of data instances. In Bootstrapping, the data are sampled
There has also been work focusing on providing a testing with replacement [175], and thus the test data may contain
toolorframeworkthathelpsdeveloperstoimplementtest- repeatedinstances.
ingactivitiesinatestingworkflow.Thereisatestframework There are several widely-adopted correctness measure-
togenerateandvalidatetestinputsforsecuritytesting[169]. ments such as accuracy, precision, recall, and Area Under
Dreossi et al. [170] presented a CNN testing framework Curve (AUC). There has been work [176] analysing the
that consists of three main modules: an image generator, a disadvantagesofeachmeasurementcriterion.Forexample,
collectionofsamplingmethods,andasuiteofvisualisation accuracy does not distinguish between the types of errors
tools. Tramer et al. [171] proposed a comprehensive testing it makes (False Positive versus False Negatives). Precision
tooltohelpdeveloperstotestanddebugfairnessbugswith and Recall may be misled when data is unbalanced. An
aneasilyinterpretablebugreport.Nishietal.[172]proposed implication of this work is that we should carefully choose
a testing framework including different evaluation aspects performance metrics. Chen et al. studied the variability
such as allowability, achievability, robustness, avoidability of both training data and test data when assessing the
and improvability. They also discussed different levels of correctnessofanMLclassifier[177].Theyderivedanalytical
MLtesting,suchassystem,software,component,anddata expressions for the variance of the estimated performance
testing. and provided an open-source software implemented with
Thomas et al. [173] recently proposed a framework for an efficient computation algorithm. They also studied the
designing machine learning algorithms, which simplifies performance of different statistical methods when compar-
the regulation of undesired behaviours. The framework ing AUC, and found that the F-test has the best perform-
is demonstrated to be suitable for regulating regression, ance[178].
classification, and reinforcement algorithms. It allows one To better capture correctness problems, Qin et al. [136]
to learn from (potentially biased) data while guaranteeing proposed to generate a mirror program from the training
that, with high probability, the model will exhibit no bias data, and then use the behaviours this mirror program
whenappliedtounseendata.Thedefinitionofbiasisuser- to serve as a correctness oracle. The mirror program is
specified, allowing for a large family of definitions. For a expectedtohavesimilarbehavioursasthetestdata.
learning algorithm and a training data, the framework will There has been a study of the prevalence of correctness
eitherreturnsamodelwiththisguarantee,orawarningthat problemsamongallthereportedMLbugs:Zhangetal.[160]
itfailstofindsuchamodelwiththerequiredguarantee. studied175TensorflowbugreportsfromStackOverflowQA
(Question and Answer) pages and from Github projects.
Amongthe175bugs,40ofthemconcernpoorcorrectness.
Additionally, there have been many works on detecting
6 ML PROPERTIES TO BE TESTED
data bug that may lead to low correctness [179], [180],
[181] (see more in Section 7.1), test input or test oracle
MLpropertiesconcerntheconditionsweshouldcareabout
design [116], [120], [121], [123], [130], [154], [162], and test
for ML testing, and are usually connected with the beha-
tooldesign[165],[167],[182](seemoreinSection5).
viourofanMLmodelaftertraining.Thepoorperformance
in a property, however, may be due to bugs in any of the
6.2 ModelRelevance
MLcomponents(seemoreinIntroduction7).
Model relevance evaluation detects mismatches between
This section presents the related work of testing both
model and data. A poor model relevance is usually asso-
functionalMLpropertiesandnon-functionalMLproperties.
ciatedwithoverfittingorunderfitting.Whenamodelistoo
Functional properties include correctness (Section 6.1) and
overfitting (Section 6.2). Non-functional properties include
8 Sometimesavalidationsetisalsoneededtohelptrainthemodel,in
robustnessandsecurity(Section6.3),efficiency(Section6.4),
whichcircumstancesthevalidationsetwillbeisolatedfromthetraining
fairness(Section6.5). set.

18
complexforthedata,eventhenoiseoftrainingdataisfitted robustness, indicating the minimum input change a classi-
bythemodel[183].Overfittingcaneasilyhappen,especially fier fails to be robust; 2) adversarial frequency, indicating
whenthetrainingdataisinsufficient, [184],[185],[186]. how often changing an input changes a classifier’s results;
Cross-validationistraditionallyconsideredtobeauseful 3) adversarial severity, indicating the distance between an
way to detect overfitting. However, it is not always clear inputanditsnearestadversarialexample.
how much overfitting is acceptable and cross-validation Carlini and Wagner [190] created a set of attacks that
may be unlikely to detect overfitting if the test data is canbeusedtoconstructanupperboundontherobustness
unrepresentativeofpotentialunseendata. of a neural network. Tjeng et al. [137] proposed to use the
Zhangetal.[54]introducedPerturbedModelValidation distance between a test input and its closest adversarial
(PMV) to help model selection. PMV injects noise to the example to measure robustness. Ruan et al. [191] provided
training data, re-trains the model against the perturbed global robustness lower and upper bounds based on the
|     |     |     |     |     |     | test data | to quantify |     | the robustness. |     | Gopinath |     | [192] et al. |
| --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | --------------- | --- | -------- | --- | ------------ |
data,thenusesthetrainingaccuracydecreaseratetodetect
overfitting/underfitting. The intuition is that an overfitted proposed DeepSafe, a data-driven approach for assessing
learner tends to fit noise in the training sample, while an DNN robustness: inputs that are clustered into the same
groupshouldsharethesamelabel.
| underfitted | learner | will have low | training | accuracy | regard- |     |     |     |     |     |     |     |     |
| ----------- | ------- | ------------- | -------- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
less the presence of injected noise. Thus, both overfitting Morerecently,Mangaletal.[193]proposedthedefinition
and underfitting tend to be less insensitive to noise and of probabilistic robustness. Their work used abstract inter-
exhibit a small accuracy decrease rate against noise degree pretationtoapproximatethebehaviourofaneuralnetwork
on perturbed data. PMV was evaluated on four real-world andtocomputeanover-approximationoftheinputregions
datasets (breast cancer, adult, connect-4, and MNIST) and wherethenetworkmayexhibitnon-robustbehaviour.
| nine synthetic | datasets | in the classification |     | setting. | The res- |          |     |           |          |     |         |             |      |
| -------------- | -------- | --------------------- | --- | -------- | -------- | -------- | --- | --------- | -------- | --- | ------- | ----------- | ---- |
|                |          |                       |     |          |          | Banerjee | et  | al. [194] | explored |     | the use | of Bayesian | Deep |
ultsrevealthatPMVhasbetterperformanceandprovidesa Learning to model the propagation of errors inside deep
more recognisable signal for detecting both overfitting/un- neuralnetworkstomathematicallymodelthesensitivityof
derfittingcomparedto10-foldcross-validation. neural networks to hardware errors, without performing
An ML system usually gathers new data after deploy- extensivefaultinjectionexperiments.
ment,whichwillbeaddedintothetrainingdatatoimprove
correctness.Thetestdata,however,cannotbeguaranteedto
6.3.2 PerturbationTargetingTestData
representthefuturedata.Werpachowskietal.[42]presents
|     |     |     |     |     |     | The existence | of  | adversarial |     | examples | allows | attacks | that |
| --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | -------- | ------ | ------- | ---- |
anoverfittingdetectionapproachviageneratingadversarial
|     |     |     |     |     |     | may lead | to serious | consequences |     |     | in safety-critical |     | applic- |
| --- | --- | --- | --- | --- | --- | -------- | ---------- | ------------ | --- | --- | ------------------ | --- | ------- |
examplesfromtestdata.Ifthereweightederrorestimateon
|     |     |     |     |     |     | ations such | as  | self-driving |     | cars. There | is  | a whole | separate |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------------ | --- | ----------- | --- | ------- | -------- |
adversarialexamplesissufficientlydifferentfromthatofthe
literatureonadversarialexamplegenerationthatdeservesa
originaltestset,overfittingisdetected.Theyevaluatedtheir
surveyofitsown,andsothispaperdoesnotattempttofully
approachonImageNetandCIFAR-10.
|          |        |               |     |        |              | cover it. | Rather, | we focus | on  | those | promising | aspects | that |
| -------- | ------ | ------------- | --- | ------ | ------------ | --------- | ------- | -------- | --- | ----- | --------- | ------- | ---- |
| Gossmann | et al. | [187] studied | the | threat | of test data |           |         |          |     |       |           |         |      |
couldbefruitfulareasforfutureresearchattheintersection
reusepracticeinthemedicaldomainwithextensivesimula-
oftraditionalsoftwaretestingandmachinelearning.
tionstudies,andfoundthattherepeatedreuseofthesame
|           |                    |        |     |             |           | Carlini | and        | Wagner     | [190] | developed |          | adversarial | ex-        |
| --------- | ------------------ | ------ | --- | ----------- | --------- | ------- | ---------- | ---------- | ----- | --------- | -------- | ----------- | ---------- |
| test data | will inadvertently | result | in  | overfitting | under all |         |            |            |       |           |          |             |            |
|           |                    |        |     |             |           | ample   | generation | approaches |       | using     | distance |             | metrics to |
consideredsimulationsettings.
|     |     |     |     |     |     | quantify | similarity. | The | approach |     | succeeded | in  | generating |
| --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | -------- | --- | --------- | --- | ---------- |
Kirk[51]mentionedthatwecouldusetrainingtimeasa
|            |           |              |     |              |           | adversarial | examples |     | for all | images | on  | the recently | pro- |
| ---------- | --------- | ------------ | --- | ------------ | --------- | ----------- | -------- | --- | ------- | ------ | --- | ------------ | ---- |
| complexity | proxy for | an ML model; |     | it is better | to choose |             |          |     |         |        |     |              |      |
poseddefensivelydistillednetworks[195].
| the algorithm | with | equal correctness |     | but relatively | small |             |     |       |            |     |          |        |         |
| ------------- | ---- | ----------------- | --- | -------------- | ----- | ----------- | --- | ----- | ---------- | --- | -------- | ------ | ------- |
|               |      |                   |     |                |       | Adversarial |     | input | generation |     | has been | widely | adopted |
trainingtime.
|     |     |     |     |     |     | to test the | robustness |     | of autonomous |     | driving | systems | [1], |
| --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | ------------- | --- | ------- | ------- | ---- |
Maetal.[162]triedtorelievetheoverfittingproblemvia
[76],[79],[92],[93].Therehasalsobeenresearchongenerat-
re-samplingthetrainingdata.Theirapproachwasfoundto
ingadversarialinputsforNLImodels[98],[99](Section8.3),
| improve | test accuracy | from 75% | to 93% | on average, | based |         |           |        |     |                |     |        |      |
| ------- | ------------- | -------- | ------ | ----------- | ----- | ------- | --------- | ------ | --- | -------------- | --- | ------ | ---- |
|         |               |          |        |             |       | malware | detection | [169], | and | Differentiable |     | Neural | Com- |
onanevaluationusingthreeimageclassificationdatasets.
puter(DNC)[100].
Papernotetal.[196],[197]designedalibrarytostandard-
6.3 RobustnessandSecurity isetheimplementationofadversarialexampleconstruction.
|     |     |     |     |     |     | They pointed | out | that | standardising |     | adversarial |     | example |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | ------------- | --- | ----------- | --- | ------- |
6.3.1 RobustnessMeasurementCriteria
|     |     |     |     |     |     | generation | is important |     | because |     | ‘benchmarks | constructed |     |
| --- | --- | --- | --- | --- | --- | ---------- | ------------ | --- | ------- | --- | ----------- | ----------- | --- |
Unlike correctness or overfitting, robustness is a non- without a standardised implementation of adversarial ex-
functional characteristic of a machine learning system. A ample construction are not comparable to each other’: it is
natural way to measure robustness is to check the cor- not easy to tell whether a good result is caused by a high
rectness of the system with the existence of noise [137]; a level of robustness or by the differences in the adversarial
robustsystemshouldmaintainperformanceinthepresence exampleconstructionprocedure.
| ofnoise. |     |     |     |     |     | Other | techniques |     | to generate |     | test | data | that check |
| -------- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ----------- | --- | ---- | ---- | ---------- |
Moosavi-Dezfooli et al. [188] proposed DeepFool that the neural network robustness include symbolic execu-
computes perturbations (added noise) that ‘fool’ deep net- tion [108], [111], fuzz testing [90], combinatorial Test-
workssoastoquantifytheirrobustness.Bastanietal.[189] ing [148], and abstract interpretation [193]. In Section 5.1,
presentedthreemetricstomeasurerobustness:1)pointwise wecoverthesetestgenerationtechniquesinmoredetail.

19
6.3.3 PerturbationTargetingtheWholeSystem can offend and even harm users, and cause programmers
Jhaetal.[198]presentedAVFI,whichusedapplication/soft- and businesses embarrassment, mistrust, loss of revenue,
ware fault injection to approximate hardware errors in the andevenlegalviolations[171].
sensors, processors, or memory of the autonomous vehicle
(AV) systems to test the robustness. They also presented 6.5.1 FairnessDefinitionsandMeasurementMetrics
Kayotee [199], a fault injection-based tool to systemat-
There are several definitions of fairness proposed in the
ically inject faults into software and hardware compon-
literature, yet no firm consensus [202], [203], [204], [205].
ents of the autonomous driving systems. Compared with
Nevertheless, these definitions can be used as oracles to
AVFI,Kayoteeiscapableofcharacterisingerrorpropagation
detectfairnessviolationsinMLtesting.
and masking using a closed-loop simulation environment,
To help illustrate the formalisation of ML fairness, we
whichisalsocapableofinjectingbitflipsdirectlyintoGPU
use X to denote a set of individuals, Y to denote the true
andCPUarchitecturalstate.DriveFI[96],furtherpresented
label set when making decisions regarding each individual
byJhaetal.,isafault-injectionenginethatminessituations
in X. Let h be the trained machine learning predictive
andfaultsthatmaximallyimpactAVsafety.
model. Let A be the set of sensitive attributes, and Z be
Tuncalietal.[102]consideredtheclosed-loopbehaviour
theremainingattributes.
of the whole system to support adversarial example gener-
1) Fairness Through Unawareness. Fairness Through Un-
ation for autonomous driving systems, not only in image
awareness (FTU) means that an algorithm is fair so long
space,butalsoinconfigurationspace.
as the protected attributes are not explicitly used in the
decision-making process [206]. It is a relatively low-cost
6.4 Efficiency waytodefineandensurefairness.Nevertheless,sometimes
the non-sensitive attributes in X may contain information
TheempiricalstudyofZhangetal.[160]onTensorflowbug-
correlated to sensitive attributes that may thereby lead to
relatedartefacts(fromStackOverflowQApageandGithub)
discrimination [202], [206]. Excluding sensitive attributes
found that nine out of 175 ML bugs (5.1%) belong to effi-
may also impact model accuracy and yield less effective
ciency problems. The reasons may either be that efficiency
predictiveresults[207].
problems rarely occur or that these issues are difficult to
2)GroupFairness.Amodelundertesthasgroupfairnessif
detect.
groupsselectedbasedonsensitiveattributeshaveanequal
Kirk [51] pointed out that it is possible to use the
probabilityofdecisionoutcomes.Thereareseveraltypesof
efficiency of different machine learning algorithms when
groupfairness.
trainingthemodeltocomparetheircomplexity.
Spieker and Gotlieb [200] studied three training data Demographic Parity is a popular group fairness meas-
reduction approaches, the goal of which was to find a
urement[208].ItisalsonamedStatisticalParityorIndepend-
smaller subset of the original training data set with similar
enceParity.Itrequiresthatadecisionshouldbeindependent
characteristics during model training, so that model build- of the protected attributes. Let G 1 and G 2 be the two
ing speed could be improved for faster machine learning groups belonging to X divided by a sensitive attribute
testing.
a∈A.Amodelhundertestsatisfiesdemographicparityif
P{h(x
i
)=1|x
i
∈G
1
}=P{h(x
j
)=1|x
j
∈G
2
}.
EqualisedOddsisanothergroupfairnessapproachpro-
6.5 Fairness
posed by Hardt et al. [139]. A model under test h satisfies
Fairness is a relatively recently-emerging non-functional EqualisedOddsifhisindependentoftheprotectedattributes
characteristic. According to the work of Barocas and when a target label Y is fixed as y i: P{h(x i ) = 1|x i ∈
Selbst [201], there are the following five major causes of G 1 ,Y =y i }=P{h(x j )=1|x j ∈G 2 ,Y =y i }.
unfairness. When the target label is set to be positive, Equalised
1) Skewed sample: once some initial bias happens, such bias OddsbecomesEqualOpportunity[139].Itrequiresthatthe
maycompoundovertime. true positive rate should be the same for all the groups. A
2) Tainted examples: the data labels are biased because of model h satisfies Equal Opportunity if h is independent of
biasedlabellingactivitiesofhumans. the protected attributes when a target class Y is fixed as
3) Limited features: features may be less informative or beingpositive:P{h(x i )=1|x i ∈G 1 ,Y =1}=P{h(x j )=
reliably collected, misleading the model in building the 1|x j ∈G 2 ,Y =1}.
connectionbetweenthefeaturesandthelabels. 3) Counter-factual Fairness. Kusner et al. [206] introduced
4) Sample size disparity: if the data from the minority group Counter-factualFairness.AmodelsatisfiesCounter-factual
and the majority group are highly imbalanced, ML model Fairness if its output remains the same when the protected
maytheminoritygrouplesswell. attribute is flipped to a counter-factual value, and other
5) Proxies: some features are proxies of sensitive attributes variablesaremodifiedasdeterminedbytheassumedcausal
(e.g., neighbourhood in which a person resides), and may model. Let a be a protected attribute, a(cid:48) be the counterfac-
cause bias to the ML model even if sensitive attributes are tual attribute of a, x(cid:48) be the new input with a changed
i
excluded. into a(cid:48). Model h is counter-factually fair if, for any input
Researchonfairnessfocusesonmeasuring,discovering, x i and protected attribute a: P{h(x i ) a = y i |a ∈ A,x i ∈
understanding, and coping with the observed differences X}=P{h(x(cid:48) i ) a(cid:48) =y i |a∈A,x i ∈X}.Thismeasurementof
regarding different groups or individuals in performance. fairnessadditionallyprovidesamechanismtointerpretthe
Such differences are associated with fairness bugs, which causesofbias,becausethevariablesotherthantheprotected

20
attributes are controlled, and thus the differences in h(x i ) box.Thereductionsoptimisethetrade-offbetweenaccuracy
andh(x(cid:48))mustbecausedbyvariationsinA. andfairnessconstraints.
i
4) Individual Fairness. Dwork et al. [138] proposed a use Albarghouthi et al. [168] proposed an approach to re-
task-specific similarity metric to describe the pairs of indi- pair decision-making programs using distribution-guided
viduals that should be regarded as similar. According to inductivesynthesis.
Dwork et al., a model h with individual fairness should
give similar predictive results among similar individuals: 6.5.2 TestGenerationTechniquesforFairnessTesting
P{h(x i )|x i ∈X}=P{h(x j )=y i |x j ∈X}iffd(x i ,x j )<(cid:15), Galhotra et al. [5], [213] proposed Themis which considers
where d is a distance metric for individuals that measures group fairness using causal analysis [214]. It defines fair-
theirsimilarity,and(cid:15)istolerancetosuchdifferences. ness scores as measurement criteria for fairness and uses
Analysis and Comparison of Fairness Metrics. Although randomtestgenerationtechniquestoevaluatethedegreeof
there are many existing definitions of fairness, each has discrimination (based on fairness scores). Themis was also
its advantages and disadvantages. Which fairness is the reported to be more efficient on systems that exhibit more
most suitable remains controversial. There is thus some discrimination.
worksurveyingandanalysingtheexistingfairnessmetrics, Themis generates tests randomly for group fairness,
or investigate and compare their performance based on while Udeshi et al. [101] proposed Aequitas, focusing on
experimentalresults,asintroducedbelow. test generation to uncover discriminatory inputs and those
Gajane and Pechenizkiy [202] surveyed how fairness inputsessentialtounderstandindividualfairness.Thegen-
is defined and formalised in the literature. Corbett-Davies eration approach first randomly samples the input space
and Goel [62] studied three types of fairness definitions: to discover the presence of discriminatory inputs, then
anti-classification,classificationparity,andcalibration.They searchestheneighbourhoodoftheseinputstofindmorein-
pointedoutthedeepstatisticallimitationsofeachtypewith puts.Aswellasdetectingfairnessbugs,Aeqitasalsoretrains
examples.VermaandRubin[203]explainedandillustrated the machine-learning models and reduce discrimination in
theexistingmostprominentfairnessdefinitionsbasedona thedecisionsmadebythesemodels.
common,unifyingdataset. Agarwal et al. [109] used symbolic execution together
with local explainability to generate test inputs. The key
Saxena et al. [204] investigated people’s perceptions of
idea is to use the local explanation, specifically Local Inter-
three of the fairness definitions. About 200 recruited par-
pretableModel-agnosticExplanations10 toidentifywhether
ticipants from Amazon’s Mechanical Turk were asked to
factors that drive decisions include protected attributes.
choose their preference over three allocation rules on two
The evaluation indicates that the approach generates 3.72
individuals having each applied for a loan. The results
times more successful test cases than THEMIS across 12
demonstrate a clear preference for the way of allocating
benchmarks.
resources in proportion to the applicants’ loan repayment
Trameretal.[171]werethefirsttoproposedtheconcept
rates.
of ‘fairness bugs’. They consider a statistically significant
Support for Fairness Improvement. Metevier et al. [209]
associationbetweenaprotectedattributeandanalgorithmic
proposed RobinHood, an algorithm that supports mul-
output to be a fairness bug, specially named ‘Unwarran-
tiple user-defined fairness definitions under the scenario
ted Associations’ in their paper. They proposed the first
of offline contextual bandits9. RobinHood makes use of
comprehensive testing tool, aiming to help developers test
concentrationinequalities[211]tocalculatehigh-probability
and debug fairness bugs with an ‘easily interpretable’ bug
bounds and to search for solutions that satisfy the fairness
report.Thetoolisavailableforvariousapplicationareasin-
requirements.Itgivesuserwarningswhentherequirements
cluding image classification, income prediction, and health
areviolated.Theapproachisevaluatedunderthreeapplic-
careprediction.
ation scenarios: a tutoring system, a loan approval setting,
Sharma and Wehrheim [122] sought to identify causes
and the criminal recidivism, all of which demonstrate the
of unfairness via checking whether the algorithm under
superiorityofRobinHoodoverotheralgorithms.
test is sensitive to training data changes. They mutated the
AlbarghouthiandVinitsky[75]proposedtheconceptof
training data in various ways to generate new datasets,
‘fairness-aware programming’, in which fairness is a first-
suchaschangingtheorderofrows,columns,andshuffling
class concern. To help developers define their own fairness
featurenamesandvalues.12outof14classifierswerefound
specifications,theydevelopedaspecificationlanguage.Like
tobesensitivetothesechanges.
assertions in traditional testing, the fairness specifications
are developed into the run-time monitoring code to enable
6.6 Interpretability
multiple executions to catch violations. A prototype was
implementedinPython. Manual Assessment of Interpretability.Theexistingwork
Agarwal et al. [212] proposed to reduce fairness classi- on empirically assessing the interpretability property usu-
ficationintoaproblemofcost-sensitiveclassification(where ally includes humans in the loop. That is, manual assess-
the costs of different types of errors are differentiated). ment is currently the primary approach to evaluate in-
The application scenario is binary classification, with the terpretability. Doshi-Velez and Kim [65] gave a taxonomy
underlying classification method being treated as a black of evaluation (testing) approaches for interpretability:
10Local Interpretable Model-agnostic Explanations produces decision
9 A contextual bandit is a type of algorithm that learns to take actions treescorrespondingtoaninputthatcouldprovidepathsinsymbolic
basedonrewardssuchasuserclickrate[210]. execution[110]

21
application-grounded, human-grounded, and functionally- 7 ML TESTING COMPONENTS
| grounded. | Application-grounded |     |     | evaluation |     | involves | hu- |     |     |     |     |     |     |     |     |
| --------- | -------------------- | --- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ThissectionorganisestheworkonMLtestingbyidentifying
man experimentation with a real application scenario. the component (data, learning program, or framework) for
Human-groundedevaluationusesresultsfromhumaneval-
whichMLtestingmayrevealabug.
| uation on | simplified |     | tasks. Functionally-grounded |     |     |     | evalu- |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ---------------------------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
ationrequiresnohumanexperimentsbutusesaquantitative
|           |         |     |             |          |     |          |     | 7.1 BugDetectioninData |     |     |     |     |     |     |     |
| --------- | ------- | --- | ----------- | -------- | --- | -------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
| metric as | a proxy | for | explanation | quality, | for | example, |     | a                      |     |     |     |     |     |     |     |
proxy for the explanation of a decision tree model may be Data is a ‘component’ to be tested in ML testing, since the
thedepthofthetree. performanceoftheMLsystemlargelydependsonthedata.
Furthermore,aspointedoutbyBrecketal.[45],itisimport-
Friedleretal.[215]introducedtwotypesofinterpretabil-
ity:globalinterpretabilitymeansunderstandingtheentirety ant to detect data bugs early because predictions from the
ofatrainedmodel;localinterpretabilitymeansunderstand- trainedmodelareoftenloggedandusedtogeneratefurther
|     |     |     |     |     |     |     |     | data. This | subsequent |     | generation | creates | a   | feedback | loop |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ---------- | ------- | --- | -------- | ---- |
ingtheresultsofatrainedmodelonaspecificinputandthe
corresponding output. They asked 1000 users to produce thatmayamplifyevensmalldatabugsovertime.
the expected output changes of a model given an input Nevertheless, data testing is challenging [220]. Accord-
|         |          |          |          |     |                |     |      | ing to the | study | of Amershi |     | et al. | [8], the | management |     |
| ------- | -------- | -------- | -------- | --- | -------------- | --- | ---- | ---------- | ----- | ---------- | --- | ------ | -------- | ---------- | --- |
| change, | and then | recorded | accuracy |     | and completion |     | time |            |       |            |     |        |          |            |     |
andevaluationofdataisamongthemostchallengingtasks
| over varied | models. | Decision |     | trees and | logistic | regression |     |     |     |     |     |     |     |     |     |
| ----------- | ------- | -------- | --- | --------- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
models were found to be more locally interpretable than when developing an AI application in Microsoft. Breck et
|     |     |     |     |     |     |     |     | al. [45] | mentioned | that | data generation |     | logic | often | lacks |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ---- | --------------- | --- | ----- | ----- | ----- |
neuralnetworks.
|     |     |     |     |     |     |     |     | visibility | in the | ML pipeline; | the | data | are often | stored | in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------------ | --- | ---- | --------- | ------ | --- |
AutomaticAssessmentofInterpretability.Chengetal.[46]
presented a metric to understand the behaviours of an ML a raw-value format (e.g., CSV) that strips out semantic
informationthatcanhelpidentifybugs.
model.Themetricmeasureswhetherthelearnerhaslearned
theobjectinobjectidentificationscenarioviaoccludingthe
|     |     |     |     |     |     |     |     | 7.1.1 BugDetectioninTrainingData |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- |
surroundingsoftheobjects.
|           |              |          |       |             |                  |         |      | Rule-based | Data    | Bug   | Detection. | Hynes    | et      | al. [179] | pro- |
| --------- | ------------ | -------- | ----- | ----------- | ---------------- | ------- | ---- | ---------- | ------- | ----- | ---------- | -------- | ------- | --------- | ---- |
| Christoph | [70]         | proposed |       | to measure  | interpretability |         |      |            |         |       |            |          |         |           |      |
|           |              |          |       |             |                  |         |      | posed data | linter– | an ML | tool,      | inspired | by code | linters,  | to   |
| based on  | the category |          | of ML | algorithms. | He               | claimed | that |            |         |       |            |          |         |           |      |
‘the easiest way to achieve interpretability is to use only automatically inspect ML datasets. They considered three
a subset of algorithms that create interpretable models’. typesofdataproblems:1)miscodeddata,suchasmistyping
|               |         |     |        |      |                        |     |     | a number | or date | as a | string; 2) | outliers | and | scaling, | such |
| ------------- | ------- | --- | ------ | ---- | ---------------------- | --- | --- | -------- | ------- | ---- | ---------- | -------- | --- | -------- | ---- |
| He identified | several |     | models | with | good interpretability, |     |     |          |         |      |            |          |     |          |      |
includinglinearregression,logisticregressionanddecision as uncommon list length; 3) packaging errors, such as du-
treemodels. plicatevalues,emptyexamples,andotherdataorganisation
issues.
| Zhou | et al. | [216] defined | the | concepts | of  | Metamorphic |     |     |     |     |     |     |     |     |     |
| ---- | ------ | ------------- | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Relation Patterns (MRPs) and Metamorphic Relation Input Cheng et al. [46] presented a series of metrics to eval-
Patterns (MRIPs) that can be adopted to help end users uate whether the training data have covered all important
scenarios.
| understand | how | an  | ML system | works. | They | conducted |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --------- | ------ | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
casestudiesofvarioussystems,includinglargecommercial Performance-basedDataBugDetection.Tosolvetheprob-
websites, Google Maps navigation, Google Maps location- lems in training data, Ma et al. [162] proposed MODE.
|     |     |     |     |     |     |     |     | MODE | identifies | the ‘faulty | neurons’ |     | in neural | networks |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | ----------- | -------- | --- | --------- | -------- | --- |
basedsearch,imageanalysisforfacerecognition(including
|           |         |     |              |     |     |        |       | that are | responsible | for | the classification |     | errors, | and | tests |
| --------- | ------- | --- | ------------ | --- | --- | ------ | ----- | -------- | ----------- | --- | ------------------ | --- | ------- | --- | ----- |
| Facebook, | MATLAB, |     | and OpenCV), | and | the | Google | video |          |             |     |                    |     |         |     |       |
analysisserviceCloudVideoIntelligence. the training data via data resampling to analyse whether
thefaultyneuronsareinfluenced.MODEallowstoimprove
EvaluationofInterpretabilityImprovementMethods.Ma-
|                |             |     |            |      |     |      |         | test effectiveness |     | from | 75% to | 93% on | average, | based | on  |
| -------------- | ----------- | --- | ---------- | ---- | --- | ---- | ------- | ------------------ | --- | ---- | ------ | ------ | -------- | ----- | --- |
| chine learning | classifiers |     | are widely | used | in  | many | medical |                    |     |      |        |        |          |       |     |
applications, yet the clinical meaning of the predictive out- evaluation using the MNIST, Fashion MNIST, and CIFAR-
| comeisoftenunclear.Chenetal.[217]investigatedseveral |     |     |     |     |     |     |     | 10datasets. |     |     |     |     |     |     |     |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
interpretability-improvingmethodswhichtransformclassi-
|             |      |             |     |         |        |      |        | 7.1.2 BugDetectioninTestData |     |     |     |     |     |     |     |
| ----------- | ---- | ----------- | --- | ------- | ------ | ---- | ------ | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
| fier scores | to a | probability | of  | disease | scale. | They | showed |                              |     |     |     |     |     |     |     |
thatclassifierscoresonarbitraryscalescanbecalibratedto Metzenetal.[221]proposedtoaugmentDNNswithasmall
sub-network,speciallydesignedtodistinguishgenuinedata
| the probability |     | scale without |     | affecting | their | discrimination |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------- | --- | --------- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
performance. from data containing adversarial perturbations. Wang et
|     |     |     |     |     |     |     |     | al. [222] | used      | DNN model | mutation          |     | to expose | adversarial |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --------- | --------- | ----------------- | --- | --------- | ----------- | --- |
|     |     |     |     |     |     |     |     | examples  | motivated | by        | their observation |     | that      | adversarial |     |
6.7 Privacy
samplesaremoresensitivetoperturbations[223].Theeval-
Ding et al. [218] treat programs as grey boxes, and de- uationwasbasedontheMNISTandCIFAR10datasets.The
tect differential privacy violations via statistical tests. For approach detects 96.4%/90.6% adversarial samples with
the detected violations, they generate counter examples to 74.1/86.1mutationsforMNIST/CIFAR10.
illustrate these violations as well as to help developers Adversarial examples in test data raise security risks.
understand and fix bugs. Bichsel et al. [219] proposed to Detecting adversarial examples is thereby similar to bug
(cid:15)
estimate the parameter in differential privacy, aiming to detection. Carlini and Wagner [224] surveyed ten propos-
(x,x(cid:48),Φ)
find a triple that witnesses the largest possible als that are designed for detecting adversarial examples
privacy violation, where x and x(cid:48) are two test inputs and and compared their efficacy. They found that detection
Φisapossiblesetofoutputs. approachesrelyonlossfunctionsandcanthusbebypassed

22
whenconstructingnewlossfunctions.Theyconcludedthat provides a declarative API that combines common as well
adversarialexamplesaresignificantlyhardertodetectthan as user-defined quality constraints for data testing. Krish-
previouslyappreciated. nan and Wu [228] also targeted automatic data cleaning
The insufficiency of the test data may not able to detect and proposed AlphaClean. They used a greedy tree search
overfitting issues, and could also be regarded as a type of algorithm to automatically tune the parameters for data
data bugs. The approaches for detecting test data insuffi- cleaning pipelines. With AlphaClean, the user could focus
ciency were discussed in Section 5.3, such as coverage [1], on defining cleaning requirements and let the system find
[76],[92]andmutationscore[152]. the best configuration under the defined requirement. The
evaluationwasconductedonthreedatasets,demonstrating
7.1.3 SkewDetectioninTrainingandTestData thatAlphaCleanfindssolutionsofupto9Xbetterthanstate-
The training instances and the instances that the model of-the-artparametertuningmethods.
predictsshouldexhibitconsistentfeaturesanddistributions. Trainingdatatestingisalsoregardedasapartofawhole
Kimetal.[127]proposedtwomeasurementstoevaluatethe machinelearningworkflowintheworkofBayloretal.[182].
skewbetweentrainingandtestdata:oneisbasedonKernel They developed a machine learning platform that enables
Density Estimation (KDE) to approximate the likelihood of data testing, based on a property description schema that
thesystemhavingseenasimilarinputduringtraining,the captures properties such as the features present in the data
otherisbasedonthedistancebetweenvectorsrepresenting andtheexpectedtypeorvalencyofeachfeature.
the neuron activation traces of the given input and the Therearealsodatacleaningtechnologiessuchasstatist-
trainingdata(e.g.,Euclideandistance). ical or learning approaches from the domain of traditional
Breck [45] investigated the skew in training data and database and data warehousing. These approaches are not
servingdata(thedatathattheMLmodelpredictsafterde- speciallydesignedorevaluatedforML,buttheycanbere-
ployment). To detect the skew in features, they do key-join purposedforMLtesting[229].
feature comparison. To quantify the skew in distribution,
theyarguedthatgeneralapproachessuchasKLdivergence 7.2 BugDetectioninLearningProgram
or cosine similarity might not be sufficiently intuitive for Bug detection in the learning program checks whether the
produce teams. Instead, they proposed to use the largest algorithmiscorrectlyimplementedandconfigured,e.g.,the
change in probability as a value in the two distributions as modelarchitectureisdesignedwell,andwhetherthereexist
ameasurementoftheirdistance. codingerrors.
Unit Tests for ML Learning Program. McClure [230] in-
7.1.4 FrameworksinDetectingDataBugs
troduced ML unit testing with TensorFlow built-in testing
Breck et al. [45] proposed a data validation system for functionstohelpensurethat‘codewillfunctionasexpected’
detecting data bugs. The system applies constraints (e.g., tohelpbuilddevelopers’confidence.
type, domain, valency) to find bugs in single-batch (within Schaul et al. [231] developed a collection of unit tests
the training data or new data), and quantifies the distance speciallydesignedforstochasticoptimisation.Thetestsare
between training data and new data. Their system is de- small-scale, isolated with well-understood difficulty. They
ployed as an integral part of TFX (an end-to-end machine couldbeadoptedinthebeginninglearningstagetotestthe
learningplatformatGoogle).Thedeploymentinproduction learningalgorithmstodetectbugsasearlyaspossible.
providesevidencethatthesystemhelpsearlydetectionand AlgorithmConfigurationExamination.Sunetal.[232]and
debugging of data bugs. They also summarised the type Guoetal.[233]identifiedoperatingsystems,language,and
of data bugs, in which new feature column, unexpected hardware Compatibility issues. Sun et al. [232] studied 329
string values, and missing feature columns are the three real bugs from three machine learning frameworks: Scikit-
mostcommon. learn, Paddle, and Caffe. Over 22% bugs are found to
Krishnan et al. [225], [226] proposed a model train- be compatibility problems due to incompatible operating
ing framework, ActiveClean, that allows for iterative data systems,languageversions,orconflictswithhardware.Guo
cleaningwhilepreservingprovableconvergenceproperties. et al. [233] investigated deep learning frameworks such as
ActiveCleansuggestsasampleofdatatocleanbasedonthe TensorFlow, Theano, and Torch. They compared the learn-
data’svaluetothemodelandthelikelihoodthatitis‘dirty’. ing accuracy, model size, robustness with different models
Theanalystcanthenapplyvaluetransformationsandfilter- classifyingdatasetMNISTandCIFAR-10.
ing operations to the sample to ‘clean’ the identified dirty The study of Zhang et al. [160] indicates that the most
data. common learning program bug is due to the change of
In2017,Krishnanetal.[180]presentedasystemnamed TensorFlow API when the implementation has not been
BoostCleantodetectdomainvalueviolations(i.e.,whenan updated accordingly. Additionally, 23.9% (38 in 159) of
attributevalueisoutsideofanalloweddomain)intraining the bugs from ML projects in their study built based on
data. The tool utilises the available cleaning resources such TensorFlowarisefromproblemsinthelearningprogram.
asIsolationForest[227]toimproveamodel’sperformance. Karpov et al. [234] also highlighted testing algorithm
After resolving the problems detected, the tool is able to parameters in all neural network testing problems. The
improve prediction accuracy by up to 9% in comparison to parameters include the number of neurons and their types
thebestnon-ensemblealternative. based on the neuron layer types, the ways the neurons
ActiveClean and BoostClean may involve a human in interact with each other, the synapse weights, and the
theloopoftestingprocess.Schelteretal.[181]focusonthe activation functions. However, the work currently remains
automatic‘unit’testingoflarge-scaledatasets.Theirsystem unevaluated.

23
AlgorithmSelectionExamination.Developersusuallyhave systems, indicated that approximately 22.6% bugs are due
more than one learning algorithm to choose from. Fu and to incorrect algorithm implementations. Cheng et al. [240]
Menzies[235]compareddeeplearningandclassiclearning injected implementation bugs into classic machine learn-
onthetaskoflinkingStackOverflowquestions,andfound ing code in Weka and observed the performance changes
thatclassiclearningalgorithms(suchasrefinedSVM)could that resulted. They found that 8% to 40% of the logically
achieve similar (and sometimes better) results at a lower non-equivalent executable mutants (injected implementa-
cost. Similarly, the work of Liu et al. [236] found that the tion bugs) were statistically indistinguishable from their
k-Nearest Neighbours (KNN) algorithm achieves similar originalversions.
results to deep learning for the task of commit message Solutions for Implementation Bug Detection. Some work
generation. hasusedmultipleimplementationsordifferentialtestingto
Mutant Simulations of Learning Program Faults.Murphy detect bugs. For example, Alebiosu et al. [135] found five
et al. [117], [128] used mutants to simulate programming faults in 10 Naive Bayes implementations and four faults
code errors to investigate whether the proposed meta- in20k-nearestneighbourimplementations.Phametal.[48]
morphic relations are effective at detecting errors. They found12bugsinthreelibraries(i.e.,TensorFlow,CNTK,and
introduced three types of mutation operators: switching Theano),11datasets(includingImageNet,MNIST,andKGS
comparison operators, mathematical operators, and off-by- Gogame),and30pre-trainedmodels(seeSection5.2.2).
oneerrorsforloopvariables. However, not every algorithm has multiple implement-
Dolby et al. [237] extended WALA to support static ations.Murphyetal.[10],[115]werethefirsttodiscussthe
analysis of the behaviour of tensors in Tensorflow learning possibilities of applying metamorphic relations to machine
programs written in Python. They defined and tracked learning implementations. They listed several transform-
tensor types for machine learning, and changed WALA ations of the input data that should ought not to bring
to produce a dataflow graph to abstract possible program changes in outputs, such as multiplying numerical values
behavours. byaconstant,permutingorreversingtheorderoftheinput
data, and adding additional data. Their case studies found
7.3 BugDetectioninFramework that their metamorphic relations held on three machine
learningapplications.
Thecurrentresearchonframeworktestingfocusesonstudy-
Xie et al. [118] focused on supervised learning. They
ing framework bugs (Section 7.3.1) and detecting bugs in
proposed to use more specific metamorphic relations to
frameworkimplementation(Section7.3.2).
test the implementations of supervised classifiers. They
discussed five types of potential metamorphic relations on
7.3.1 StudyofFrameworkBugs
KNN and Naive Bayes on randomly generated data. In
Xiao et al. [238] focused on the security vulnerabilities of
2011, they further evaluated their approach using mutated
populardeeplearningframeworksincludingCaffe,Tensor-
machine learning code [241]. Among the 43 injected faults
Flow, and Torch. They examined the code of popular deep
in Weka [119] (injected by MuJava [242]), the metamorphic
learningframeworks.Thedependencyoftheseframeworks
relationswereabletoreveal39.Intheirwork,thetestinputs
was found to be very complex. Multiple vulnerabilities
wererandomlygenerateddata.
wereidentifiedintheirimplementations.Themostcommon
Dwarakanathetal.[121]appliedmetamorphicrelations
vulnerabilities are bugs that cause programs to crash, non-
to find implementation bugs in image classification. For
terminate,orexhaustmemory.
classic machine learning such as SVM, they conducted
Guo et al. [233] tested deep learning frameworks, in-
mutations such as changing feature or instance orders, and
cludingTensorFlow,Theano,andTorch,bycomparingtheir
linearscalingofthetestfeatures.Fordeeplearningmodels
runtimebehaviour,trainingaccuracy,androbustness,under
such as residual networks (which the data features are not
identical algorithm design and configuration. The results
directly available), they proposed to normalise or scale the
indicate that runtime training behaviours are different for
test data, or to change the convolution operation order of
each framework, while the prediction accuracies remain
the data. These changes were intended to bring no change
similar.
to the model performance when there are no implementa-
Low Efficiency is a problem for ML frameworks, which
tionbugs.Otherwise,implementationbugsareexposed.To
maydirectlyleadtoinefficiencyofthemodelsbuiltonthem.
evaluate, they used MutPy to inject mutants that simulate
Sun et al. [232] found that approximately 10% of reported
implementation bugs, of which the proposed metamorphic
framework bugs concern low efficiency. These bugs are
relationsareabletofind71%.
usually reported by users. Compared with other types of
bugs,theymaytakelongerfordeveloperstoresolve.
7.3.3 StudyofFrameworksTestOracles
7.3.2 ImplementationTestingofFrameworks NejadgholiandYang[133]studiedtheapproximatedoracles
Many learning algorithms are implemented inside ML offourpopulardeeplearninglibraries:Tensorflow,Theano,
frameworks. Implementation bugs in ML frameworks may PyTorch, and Keras. 5% to 24% oracles were found to be
cause neither crashes, errors, nor efficiency problems [239], approximated oracles with a flexible threshold (in contrast
makingtheirdetectionchallenging. tocertainoracles).5%-27%oftheapproximatedoraclesused
Challenges in Implementation Bug Detection. Thung et the outputs from other libraries/frameworks. Developers
al. [159] studied machine learning bugs in 2012. Their res- werealsofoundtomodifyapproximatedoraclesfrequently
ults,regarding500bugreportsfromthreemachinelearning duetocodeevolution.

24
8 APPLICATION SCENARIOS Wicker et al. [93] used feature-guided Monte Carlo Tree
|         |          |     |      |        |         |     |           | Search | to identify | elements |     | of an image | that | are most | vul- |
| ------- | -------- | --- | ---- | ------ | ------- | --- | --------- | ------ | ----------- | -------- | --- | ----------- | ---- | -------- | ---- |
| Machine | learning | has | been | widely | adopted | in  | different |        |             |          |     |             |      |          |      |
areas. This section introduces such domain-specific testing nerabletoaself-drivingsystem;adversarialexamples.Jhaet
|            |     |               |     |             |          |     |          | al. [96] | accelerated | the | process | of finding | ‘safety-critical’ |     | is- |
| ---------- | --- | ------------- | --- | ----------- | -------- | --- | -------- | -------- | ----------- | --- | ------- | ---------- | ----------------- | --- | --- |
| approaches | in  | three typical |     | application | domains: |     | autonom- |          |             |     |         |            |                   |     |     |
suesviaanalyticallymodellingtheinjectionoffaultsintoan
| ous driving, | machine |     | translation, | and | neural | language | in- |     |     |     |     |     |     |     |     |
| ------------ | ------- | --- | ------------ | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ference. AV system as a Bayesian network. The approach trains the
|     |     |     |     |     |     |     |     | network | to identify | safety |     | critical faults | automatically. |     | The |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------ | --- | --------------- | -------------- | --- | --- |
evaluationwasbasedontwoproduction-gradeAVsystems
8.1 AutonomousDriving from NVIDIA and Baidu, indicating that the approach can
Testing autonomous vehicles has a comparatively long his- findmanysituationswherefaultsleadtosafetyviolations.
tory. For example, in 2004, Wegener and Bühler compared Uesato et al. [94] aimed to find catastrophic failures
different fitness functions when evaluating the tests of in safety-critical agents like autonomous driving in rein-
autonomouscarparkingsystems[243].Testingautonomous forcement learning. They demonstrated the limitations of
vehicles also has many research opportunities and open traditional random testing, then proposed a predictive ad-
questions, as pointed out and discussed by Woehrle et versarial example generation approach to predict failures
| al.[244]. |     |     |     |     |     |     |     | andestimatereliablerisks.TheevaluationonTORCSsimu- |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
More recently, search-based test generation for AV test- lator indicates that the proposed approach is both effective
ing has been successfully applied. Abdessalem et al. [245], andefficientwithfewerMonteCarloruns.
|               |     |           |     |                |     |              |     | To test | whether | an  | algorithm | can | lead to | a problematic |     |
| ------------- | --- | --------- | --- | -------------- | --- | ------------ | --- | ------- | ------- | --- | --------- | --- | ------- | ------------- | --- |
| [246] focused | on  | improving |     | the efficiency |     | and accuracy | of  |         |         |     |           |     |         |               |     |
search-based testing of advanced driver assistance systems model, Dreossi et al. [170] proposed to generate training
(ADAS) in AVs. Their algorithms use classification models dataaswellastestdata.FocusingonConvolutionalNeural
toimprovetheefficiencyofthesearch-basedtestgeneration Networks (CNN), they build a tool to generate natural
for critical scenarios. Search algorithms are further used images and visualise the gathered information to detect
to refine classification models to improve their accuracy. blind spots or corner cases under the autonomous driving
Abdessalem et al. [247] also proposed FITEST, a multi- scenario.Althoughthereiscurrentlynoevaluation,thetool
hasbeenmadeavailable11.
objectivesearchalgorithmthatsearchesfeatureinteractions
whichviolatesystemrequirementsorleadtofailures. Tuncalietal.[102]presentedaframeworkthatsupports
Most of the current autonomous vehicle systems that bothsystem-leveltestingandthetestingofthoseproperties
have been put into the market are semi-autonomous ofanMLcomponent.Theframeworkalsosupportsfuzztest
vehicles, which require a human driver to serve as a fall- inputgenerationandsearch-basedtestingusingapproaches
back [161], as was the case with the work of Wegener and such as Simulated Annealing and Cross-Entropy optimisa-
tion.
Bühler[243].Anissuethatcausesthehumandrivertotake
controlofthevehicleiscalledadisengagement. While many other studies investigated DNN model
Banerjeeetal.[161]investigatedthecausesandimpacts testing for research purposes, Zhou et al. [95] combined
of 5,328 disengagements from the data of 12 AV manufac- fuzzing and metamorphic testing to test LiDAR, which is
turers for 144 vehicles that drove a cumulative 1,116,605 an obstacle-perception module of real-life self-driving cars,
autonomousmiles,42(0.8%)ofwhichledtoaccidents.They anddetectedreal-lifefatalbugs.
classifiedthecausesofdisengagementsinto10types.64%of Jhaetal.presentedAVFI[198]andKayotee[199],which
thedisengagementswerefoundtobecausedbythebugsin are fault injection-based tools to systematically inject faults
the machine learning system, among which the behaviours intoautonomousdrivingsystemstoassesstheirsafetyand
| of image | classification |     | (e.g., | improper | detection |     | of traffic | reliability. |     |     |     |     |     |     |     |
| -------- | -------------- | --- | ------ | -------- | --------- | --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
O’Kellyetal.[72]proposeda‘risk-basedframework’for
lights,lanemarkings,holes,andbumps)werethedominant
causes accounting for 44% of all reported disengagements. AVtestingtopredicttheprobabilityofanaccidentinabase
Theremaining20%wereduetothebugsinthecontroland distribution of traffic behaviour (derived from the public
|     |     |     |     |     |     |     |     | traffic data | collected |     | by the | US Department |     | of Transport- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | ------ | ------------- | --- | ------------- | --- |
decisionframeworksuchasimpropermotionplanning.
Pei et al. [1] used gradient-based differential testing to ation). They argued that formally verifying correctness of
generate test inputs to detect potential DNN bugs and an AV system is infeasible due to the challenge of formally
leveraged neuron coverage as a guideline. Tian et al. [76] defining“correctness”aswellasthewhite-boxrequirement.
proposed to use a set of image transformation to gener- Traditional testing AVs in a real environment requires pro-
ate tests, which simulate the potential noise that could be hibitive amounts of time. To tackle these problems, they
presentinimagesobtainedfromareal-worldcamera.Zhang view AV testing as rare-event simulation problem, then
et al. [79] proposed DeepRoad, a GAN-based approach to evaluate the accident probability to accelerate AV testing.
| generate | test images |            | for real-world |             | driving | scenes.    | Their  |     |     |     |     |     |     |     |     |
| -------- | ----------- | ---------- | -------------- | ----------- | ------- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| approach | is able     | to support |                | two weather |         | conditions | (i.e., |     |     |     |     |     |     |     |     |
snowy and rainy). The images were generated with the 8.2 MachineTranslation
| pictures | from | YouTube | videos. | Zhou | et  | al. [81] | proposed |         |             |     |               |            |     |         |        |
| -------- | ---- | ------- | ------- | ---- | --- | -------- | -------- | ------- | ----------- | --- | ------------- | ---------- | --- | ------- | ------ |
|          |      |         |         |      |     |          |          | Machine | translation |     | automatically | translates |     | text or | speech |
DeepBillboard,whichgeneratesreal-worldadversarialbill-
|     |     |     |     |     |     |     |     | from one | language | to  | another. | The | BLEU (BiLingual |     | Eval- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- | --- | -------- | --- | --------------- | --- | ----- |
boardsthatcantriggerpotentialsteeringerrorsofautonom- uation Understudy) score [248] is a widely-adopted meas-
ousdrivingsystems.Itdemonstratesthepossibilityofgen-
|         |            |     |           |                |     |     |           | urement | criterion | to  | evaluate | machine | translation | quality. |     |
| ------- | ---------- | --- | --------- | -------------- | --- | --- | --------- | ------- | --------- | --- | -------- | ------- | ----------- | -------- | --- |
| erating | continuous | and | realistic | physical-world |     |     | tests for |         |           |     |          |         |             |          |     |
practicalautonomous-drivingsystems. 11https://github.com/shromonag/FalsifyNN

25
It assessesthe correspondence between a machine’soutput 9 ANALYSIS OF LITERATURE REVIEW
andthatofahuman.
This section analyses the research distribution among dif-
Zhou et al. [129], [130] used self-defined metamorphic
ferenttestingpropertiesandmachinelearningcategories.It
relations in their tool ‘MT4MT’ to test the translation con-
also summarises the datasets (name, description, size, and
sistency of machine translation systems. The idea is that
usage scenario of each dataset) that have been used in ML
some changes to the input should not affect the overall
testing.
structureofthetranslatedoutput.Theirevaluationshowed
thatGoogleTranslateoutperformedMicrosoftTranslatorfor
long sentences whereas the latter outperformed the former 9.1 Timeline
for short and simple sentences. They hence suggested that
Figure 8 shows several key contributions in the develop-
the quality assessment of machine translations should con-
ment of ML testing. As early as in 2007, Murphy et al. [10]
sidermultipledimensionsandmultipletypesofinputs.
mentioned the idea of testing machine learning applica-
Sun et al. [86] combine mutation testing and meta-
tions.Theyclassifiedmachinelearningapplicationsas‘non-
morphictestingtotestandrepairtheconsistencyofmachine
testable’ programs considering the difficulty of getting test
translation systems. Their approach, TransRepair, enables
oracles. They primarily consider the detection of imple-
automatic test input generation, automatic test oracle gen-
mentationbugs,describedas“toensurethatanapplication
eration, as well as automatic translation repair. They first
using the algorithm correctly implements the specification
applied mutation on sentence inputs to find translation
and fulfils the users’ expectations”. Afterwards, Murphy
inconsistency bugs, then used translations of the mutated
et al. [115] discussed the properties of machine learning
sentencestooptimisethetranslationresultsinablack-boxor
algorithms that may be adopted as metamorphic relations
grey-boxmanner.EvaluationdemonstratesthatTransRepair
todetectimplementationbugs.
fixes28%and19%bugsonaverageforGoogleTranslateand
In2009,Xieetal.[118]alsoappliedmetamorphictesting
Transformer.
onsupervisedlearningapplications.
Compared with existing model retraining approaches,
Fairness testing was proposed in 2012 by Dwork et
TransRepair has the following advantages: 1) more effect-
al. [138]; the problem of interpretability was proposed in
ive than data augmentation; 2) source code in dependant
2016byBurrell[252].
(black box); 3) computationally cheap (avoids space and
In2017,Peietal.[1]publishedthefirstwhite-boxtesting
time expense of data collection and model retraining); 4)
paper on deep learning systems. Their work pioneered to
flexible(enablesrepairwithouttouchingotherwell-formed
proposecoveragecriteriaforDNN.Enlightenedbythispa-
translations).
per, a number of machine learning testing techniques have
The work of Zheng et al. [249], [250], [251] proposed
emerged, such as DeepTest [76], DeepGauge [92], Deep-
two algorithms for detecting two specific types of machine
Concolic [111], and DeepRoad [79]. A number of software
translation violations: (1) under-translation, where some
testing techniques has been applied to ML testing, such as
words/phrases from the original text are missing in the
different testing coverage criteria [76], [92], [145], mutation
translation, and (2) over-translation, where some words/-
testing[152],combinatorialtesting[149],metamorphictest-
phrases from the original text are unnecessarily translated
ing[100],andfuzztesting[89].
multiple times. The algorithms are based on a statistical
analysis of both the original texts and the translations, to
check whether there are violations of one-to-one mappings 9.2 Research Distribution among Machine Learning
inwords/phrases. Categories
Thissectionintroducesandcomparestheresearchstatusof
8.3 NaturalLanguageInference eachmachinelearningcategory.
A Nature Language Inference (NLI) task judges the infer-
9.2.1 Research Distribution between General Machine
ence relationship of a pair of natural language sentences.
LearningandDeepLearning
For example, the sentence ‘A person is in the room’ could
beinferredfromthesentence‘Agirlisintheroom’. ToexploreresearchtrendsinMLtesting,weclassifythecol-
SeveralworkshavetestedtherobustnessofNLImodels. lectedpapersintotwocategories:thosetargetingonlydeep
Nieetal.[98]generatedsentencemutants(called‘rule-based learning and those designed for general machine learning
adversaries’ in the paper) to test whether the existing NLI (includingdeeplearning).
modelshavesemanticunderstanding.Sevenstate-of-the-art Amongall144papers,56papers(38.9%)presenttesting
NLI models (with diverse architectures) were all unable to techniques that are specially designed for deep learning
recognise simple semantic differences when the word-level alone; the remaining 88 papers cater for general machine
informationremainsunchanged. learning.
Similarly, Wang et al. [99] mutated the inference target We further investigated the number of papers in each
pairbysimplyswappingthem.Theheuristicisthatagood category for each year, to observe whether there is a trend
NLImodelshouldreportcomparableaccuracybetweenthe of moving from testing general machine learning to deep
original and swapped test set for contradictory pairs and learning. Figure 9 shows the results. Before 2017, papers
forneutralpairs,butloweraccuracyinswappedtestsetfor mostly focus on general machine learning; after 2018, both
entailment pairs (the hypothesis may or may not be true generalmachinelearninganddeeplearningspecifictesting
givenapremise). notablyarise.

26
DeepXplore: the first
white-box DL testing
technique. Pei et al.
Interpretability
M M e u t r a p m hy o e rp t h a i l c . t & e s X ti i n e g e a t a p l p . lied a B w ur a r r e e ll ness. 2017 D D e e e e p p T R e o s a t, d D ... eepGauge,
F on ir s M t p L a te p s e t r i ng. 2008 F D a w ir o n r e k s e s t a a w l. areness. D ad e v e e p r F s o a o ria l o l e n x amples 2016 2018
Murphy et al. Moosavi-Dezfooli et al.
2007 2011 2015
2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019
2007 2020
Figure8:TimelineofMLtestingresearch
Year
snoitacilbup
fo
rebmuN
Table 4: Search hits and testing distribution of super-
general machine learning deep learning vised/unsupervised/reinforcementLearning
100 Category Scholarhits Googlehits Testinghits
Supervised 1,610k 73,500k 119/144
Unsupervised 619k 17,700k 3/144
75
Reinforcement 2,560k 74,800k 1/144
50
number/ratio of papers that touch each machine learning
25 category in ML testing. For example, 119 out of 144 papers
wereobservedforsupervisedlearningtestingpurpose.The
tablesuggeststhattestingpopularityofdifferentcategories
0
2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 is not related to their overall research popularity. In par-
ticular, reinforcement learning has higher search hits than
supervised learning, but we did not observe any related
workthatconductsdirectreinforcementlearningtesting.
Figure 9: Commutative trends in general machine learning
Theremaybeseveralreasonsforthisobservation.First,
anddeeplearning
supervised learning is a widely-known learning scenario
associatedwithclassification,regression,andrankingprob-
lems[28].Itisnaturalthatresearcherswouldemphasisethe
9.2.2 Research Distribution among Supervised/Unsuper- testing of widely-applied, known and familiar techniques
vised/ReinforcementLearningTesting at the beginning. Second, supervised learning usually has
labelsinthedataset.Itistherebyeasiertojudgeandanalyse
Wefurtherclassifiedthepapersbasedonthethreemachine
testeffectiveness.
learning categories: 1) supervised learning testing, 2) un-
Nevertheless, many opportunities clearly remain for re-
supervised learning testing, and 3) reinforcement learning
searchinthewidely-studiedareasofunsupervisedlearning
testing. One striking finding is that almost all the work
andreinforcementlearning(wediscussmoreinSection10).
we identified in this survey focused on testing supervised
machine learning. Among the 144 related papers, there are
9.2.3 DifferentLearningTasks
currently only three papers testing unsupervised machine
MLinvolvesdifferenttaskssuchasclassification,regression,
learning: Murphy et al. [115] introduced metamorphic re-
clustering,anddimensionreduction(seemoreinSection2).
lations that work for both supervised and unsupervised
Theresearchfocusondifferenttasksalsoappearstoexhibit
learningalgorithms.RamanathanandPullum[7]proposed
imbalance, with a large number of papers focusing on
a combination of symbolic and statistical approaches to
test the k-means clustering algorithm. Xie et al. [125] de- classification.
signed metamorphic relations for unsupervised learning.
We were able to find out only one paper that focused on 9.3 Research Distribution among Different Testing
reinforcement learning testing: Uesato et al. [94] proposed Properties
a predictive adversarial example generation approach to We counted the number of papers concerning each ML
predict failures and estimate reliable risks in reinforcement testingproperty.Figure10showstheresults.Theproperties
learning. in the legend are ranked based on the number of papers
Because of this notable imbalance, we sought to un- thatarespeciallyfocusedontestingtheassociatedproperty
derstand whether there was also an imbalance of research (‘general’referstothosepapersdiscussingorsurveyingML
popularity in the machine learning areas. To approximate testinggenerally).
theresearchpopularityofeachcategory,wesearchedterms From the figure, 38.7% of the papers test correctness.
‘supervised learning’, ‘unsupervised learning’, and ‘rein- 26.8%ofthepapersfocusonrobustnessandsecurityprob-
forcement learning’ in Google Scholar and Google. Table 4 lems.Fairnesstestingranksthethirdamongalltheproper-
showstheresultsofsearchhits.Thelastcolumnshowsthe ties,with12.0%ofthepapers.

27
| Nevertheless,   | for      | model | relevance, |          | interpretability |       | test- |     |     |     |     |     |     |     |     |
| --------------- | -------- | ----- | ---------- | -------- | ---------------- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
| ing, efficiency | testing, | and   | privacy    | testing, |                  | fewer | than  | 6   | 1   |     |     |     |     |     |     |
2
papersexistforeachcategoryinourpapercollection.
|     |     |     |     |     |     |     |     | stes atad fo rebmuN | 3   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
4
6
correctness
8
robustness&security
9
general
11
12.0%
| fairness |     |     |     |     |     |     |     |     | 12  |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
38.7%
| model relevance  |     |     |     |     |     |     |     |     | 13  |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| interpretability |     |     |     |     |     |     |     |     | 600 |     |     |     |     |     |     |
12.7%
efficiency
|     |     |     |     |     |     |     |     |     | 0   |     | 10  | 20  |     | 30  | 40  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Number of papers
26.8%
|     |     |     |     |     |     |     |     | Figure | 11: | Number of | papers | with | different | amounts | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --------- | ------ | ---- | --------- | ------- | --- |
Figure 10: Research distribution among different testing datasetsinexperiments
properties
mltest,
|     |     |     |     |     |     |     |     | simple | ML  | unit tests. | Similar | to  | there | is  | a testing |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----------- | ------- | --- | ----- | --- | --------- |
frameworkforwritingunittestsforpytorch-basedMLsys-
9.4 DatasetsUsedinMLTesting
|     |     |     |     |     |     |     |     | tems, | named | torchtest16. | Dolby | et al. | [237] extended |     | WALA |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ------------ | ----- | ------ | -------------- | --- | ---- |
Tables 5 to 8 show details concerning widely-adopted to enable static analysis for machine learning code using
datasetsusedinMLtestingresearch.Ineachtable,thefirst
TensorFlow.
| column shows | the | name | and link | of each | dataset. |     | The next |     |     |     |     |     |     |     |     |
| ------------ | --- | ---- | -------- | ------- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Comparedtotraditionaltesting,theexistingtoolsupport
three columns give a brief description, the size (the “+” in ML testing is relatively immature. There remains plenty
connectstrainingdataandtestdataifapplicable),thetesting
ofspacefortool-supportimprovementforMLtesting.
problem(s),theusageapplicationscenarioofeachdataset12.
| Table | 5 shows | the datasets |     | used for | image | classification |     |     |            |     |               |     |     |     |     |
| ----- | ------- | ------------ | --- | -------- | ----- | -------------- | --- | --- | ---------- | --- | ------------- | --- | --- | --- | --- |
|       |         |              |     |          |       |                |     | 10  | CHALLENGES |     | OPPORTUNITIES |     |     |     |     |
tasks. Datasets can be large (e.g., more than 1.4 million AND
| images in | ImageNet). | The | last | six rows | show | the | datasets |      |         |           |     |            |          |     |           |
| --------- | ---------- | --- | ---- | -------- | ---- | --- | -------- | ---- | ------- | --------- | --- | ---------- | -------- | --- | --------- |
|           |            |     |      |          |      |     |          | This | section | discusses | the | challenges | (Section |     | 10.1) and |
collected for autonomous driving system testing. Most im- researchopportunitiesinMLtesting(Section10.2).
agedatasetsareadoptedtotestcorrectness,overfitting,and
robustnessofMLsystems.
|       |         |          |         |            |     |          |      | 10.1 | ChallengesinMLTesting |     |     |     |     |     |     |
| ----- | ------- | -------- | ------- | ---------- | --- | -------- | ---- | ---- | --------------------- | --- | --- | --- | --- | --- | --- |
| Table | 6 shows | datasets | related | to natural |     | language | pro- |      |                       |     |     |     |     |     |     |
cessing.Thecontentsareusuallytext,sentences,ortextfiles, As this survey reveals, ML testing has experienced rapid
appliedtoscenarioslikerobustnessandcorrectness. recentgrowth.Nevertheless,MLtestingremainsatanearly
The datasets used to make decisions are introduced in stage in its development, with many challenges and open
Table6.Theyareusuallyrecordswithpersonalinformation, questionslyingahead.
and thus are widely adopted to test the fairness of the ML Challenges in Test Input Generation. Although a range
models. of test input generation techniques have been proposed
|         |           |     |      |          |     |       |         | (see | more | in Section | 5.1), | test input | generation |     | remains |
| ------- | --------- | --- | ---- | -------- | --- | ----- | ------- | ---- | ---- | ---------- | ----- | ---------- | ---------- | --- | ------- |
| We also | calculate | how | many | datasets |     | an ML | testing |      |      |            |       |            |            |     |         |
paper usually uses in its evaluation (for those papers with challenging because of the large behaviour space of ML
| an evaluation). | Figure   | 11  | shows | the          | results. | Surprisingly, |        | models.      |     |          |      |            |        |     |           |
| --------------- | -------- | --- | ----- | ------------ | -------- | ------------- | ------ | ------------ | --- | -------- | ---- | ---------- | ------ | --- | --------- |
|                 |          |     |       |              |          |               |        | Search-based |     | Software | Test | generation | (SBST) |     | [87] uses |
| most papers     | use only | one | or    | two datasets |          | in their      | evalu- |              |     |          |      |            |        |     |           |
ation; One reason might be training and testing machine a meta-heuristic optimising search technique, such as a
learningmodelshavehighcosts.Thereisonepaperwithas Genetic Algorithm, to automatically generate test inputs. It
manyas600datasets,butthatpaperusedthesedatasetsto is a test generation technique that has been widely used
evaluatedatacleaningtechniques,whichhasrelativelylow in research (and deployment [288]) for traditional software
cost[179]. testingparadigms.Aswellasgeneratingtestinputsfortest-
We also discuss research directions of building dataset ingfunctionalpropertieslikeprogramcorrectness,SBSThas
andbenchmarksforMLtestinginSection10. alsobeenusedtoexploretensionsinalgorithmicfairnessin
|     |     |     |     |     |     |     |     | requirement |         | analysis.  | [205],     | [289]. SBST | has     | been    | success- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ---------- | ---------- | ----------- | ------- | ------- | -------- |
|     |     |     |     |     |     |     |     | fully       | applied | in testing | autonomous |             | driving | systems | [245],   |
9.5 Open-sourceToolSupportinMLTesting
|           |               |       |           |          |                |        |          | [246],   | [247]. | There exist   | many | research    | opportunities |         | in    |
| --------- | ------------- | ----- | --------- | -------- | -------------- | ------ | -------- | -------- | ------ | ------------- | ---- | ----------- | ------------- | ------- | ----- |
| There are | several       | tools | specially | designed |                | for ML | testing. |          |        |               |      |             |               |         |       |
|           |               |       |           |          |                |        |          | applying | SBST   | on generating |      | test inputs | for           | testing | other |
| Angell et | al. presented |       | Themis    | [213],   | an open-source |        | tool     |          |        |               |      |             |               |         |       |
MLsystems,sincethereisaclearapparentfitbetweenSBST
fortestinggroupdiscrimination14.ThereisalsoanMLtest-
|     |     |     |     |     |     |     |     | and ML; | SBST | adaptively | searches | for | test | inputs | in large |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---- | ---------- | -------- | --- | ---- | ------ | -------- |
mltest15,
| ing framework | for | tensorflow, |     | named |     | for | writing |     |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | ----- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
inputspaces.
|     |     |     |     |     |     |     |     | Existing |     | test input | generation | techniques |     | focus | on gen- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---------- | ---------- | ---------- | --- | ----- | ------- |
12Thesetablesdonotlistdatasetsadoptedindatacleaningevaluation,
|     |     |     |     |     |     |     |     | erating | adversarial | inputs | to  | test the | robustness |     | of an ML |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------ | --- | -------- | ---------- | --- | -------- |
becausesuchstudiesusuallyinvolvehundredsofdatasets[180]
14http://fairness.cs.umass.edu/
15https://github.com/Thenerdstation/mltest 16https://github.com/suriyadeepan/torchtest

28
Table5:Datasets(1/4):ImageClassification
Dataset Description Size Usage
MNIST[253] Imagesofhandwrittendigits 60,000+10,000 correctness, overfit-
ting,robustness
FashionMNIST[254] MNIST-likedatasetoffashionimages 70,000 correctness, overfit-
ting
CIFAR-10[255] Generalimageswith10classes 50,000+10,000 correctness, overfit-
ting,robustness
ImageNet[256] Visualrecognitionchallengedataset 14,197,122 correctness, robust-
ness
IRISflower[257] TheIrisflowers 150 overfitting
SVHN[258] Housenumbers 73,257+26,032 correctness,robustness
Fruits360[259] Datasetwith65,429imagesof95fruits 65,429 correctness,robustness
HandwrittenLetters[260] ColourimagesofRussianletters 1,650 correctness,robustness
BalanceScale[261] Psychologicalexperimentalresults 625 overfitting
DSRC[262] Wirelesscommunicationsbetweenvehiclesandroad 10,000 overfitting, robust-
sideunits ness
Udacitychallenge[77] UdacitySelf-DrivingCarChallengeimages 101,396+5,614 robustness
Nexar traffic light chal- Dashboardcamera 18,659+500,000 robustness
lenge[263]
MSCOCO[264] Objectrecognition 160,000 correctness
Autopilot-TensorFlow[265] RecordedtotesttheNVIDIADavemodel 45,568 robustness
KITTI[266] SixdifferentscenescapturedbyaVWPassatstation 14,999 robustness
wagonequippedwithfourvideocameras
Table6:Datasets(2/4):NaturalLanguageProcessing
Dataset Description Size Usage
bAbI[267] questionsandanswersforNLP 1000+1000 robustness
TinyShakespeare[268] SamplesfromactualShakespeare 100,000 char- correctness
acter
Stack Exchange Data StackOverflowquestionsandanswers 365files correctness
Dump[269]
SNLI[270] StanfordNaturalLanguageInferenceCorpus 570,000 robustness
MultiNLI[271] Crowd-sourcedcollectionofsentencepairsannotated 433,000 robustness
withtextualentailmentinformation
DMVfailurereports[272] AV failure reports from 12 manufacturers in Califor- keep correctness
nia13 updating
system. However, adversarial examples are often criticised of test data (see more in Section 5.3). However, there is
because they do not represent real input data. Thus, an in- still a lack of systematic evaluation about how different as-
terestingresearchdirectionistohowtogeneratenaturaltest sessmentmetricscorrelate,orhowtheseassessmentmetrics
inputsandhowtoautomaticallymeasurethenaturalnessof correlate with tests’ fault-revealing ability, a topic that has
thegeneratedinputs. been widely studied in traditional software testing [290].
Therehasbeenworkthattriestogeneratetestinputsto The relation between test assessment criteria and test suf-
beasnaturalaspossibleunderthescenarioofautonomous ficiency remains unclear. In addition, assessment criteria
driving,suchasDeepTest[76],DeepHunter[92]andDeep- may provide a way of interpreting and understanding
Road [79], yet the generated images could still suffer from behaviours of ML models, which might be an interesting
unnaturalness: sometimes even humans may not recognise directionforfurtherexploration.
the images generated by these tools. It is both interesting Challenges Relating to The Oracle Problem. The oracle
and challenging to explore whether such kinds of test data problem remains a challenge in ML testing. Metamorphic
thataremeaninglesstohumansshouldbeadopted/validin relations are effective pseudo oracles but, in most cases,
MLtesting. theyneedtobedefinedbyhumaningenuity.Aremaining
Challenges on Test Assessment Criteria. There has been a challenge is thus to automatically identify and construct
lotofworkexploringhowtoassessthequalityoradequacy reliabletestoraclesforMLtesting.

29
Table7:Datasets(3/4):RecordsforDecisionMaking
| Dataset |     | Description |     |     | Size |     | Usage |
| ------- | --- | ----------- | --- | --- | ---- | --- | ----- |
GermanCredit[273] Descriptions of customers with good and bad credit 1,000 fairness
risks
| Adult [274] |     | Censusincome |     |     | 48,842 |     | fairness |
| ----------- | --- | ------------ | --- | --- | ------ | --- | -------- |
BankMarketing[275] Bankclientsubscriptiontermdepositdata 45,211 fairness
USExecutions[276] Records of every execution performed in the United 1,437 fairness
States
FraudDetection[277] EuropeanCreditcardstransactions 284,807 fairness
Berkeley Admissions Graduateschoolapplicationstothesixlargestdepart- 4,526 fairness
| Data[278] |     | mentsatUniversityofCalifornia,Berkeleyin1973 |     |     |     |     |     |
| --------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |
Broward County Scoretodeterminewhethertoreleaseadefendant 18,610 fairness
COMPAS[279]
MovieLensDatasets[280] People’spreferencesformovies 100k-20m fairness
Zestimate[281] data about homes and Zillow’s in-house price and 2,990,000 correctness
predictions
FICOscores[282] UnitedStatescreditworthiness 301,536 fairness
Lawschoolsuccess[283] Information concerning law students from 163 law 21,790 fairness
schoolsintheUnitedStates
Table8:Datasets(4/4):Others
| Dataset         |     | Description            |     |     | Size   |     | Usage      |
| --------------- | --- | ---------------------- | --- | --- | ------ | --- | ---------- |
| VirusTotal[284] |     | MaliciousPDFfiles      |     |     | 5,000  |     | robustness |
| Contagio[285]   |     | Cleanandmaliciousfiles |     |     | 28,760 |     | robustness |
Drebin[286] Applicationsfromdifferentmalwarefamilies 123,453 robustness
Chess[287] Chess game data: King+Rook versus King+Pawn on 3,196 correctness
a7
Waveform[261] CARTbook’sgeneratedwaveformdata 5,000 correctness
Murphy et al. [128] discussed how flaky tests are likely thesizeoftestcaseswithoutaffectingthetestcorrectness.
to arise in metamorphic testing whenever floating point MoreMLsolutionsaredeployedtodiversedevicesand
calculations are involved. Flaky test detection is a chal- platforms(e.g.,mobiledevice,IoTedgedevice).Duetothe
lenging problem in traditional software testing [288]. It is resourcelimitationofatargetdevice,howtoeffectivelytest
perhaps more challenging in ML testing because of the ML model on diverse devices as well as the deployment
| oracleproblem.  |              |                        |                | processwouldbealsoachallenge. |     |     |     |
| --------------- | ------------ | ---------------------- | -------------- | ----------------------------- | --- | --- | --- |
| Even without    | flaky tests, | pseudo oracles         | may be inac-   |                               |     |     |     |
| curate, leading | to many      | false positives. There | is, therefore, |                               |     |     |     |
10.2 ResearchOpportunitiesinMLtesting
| a need to explore | how to | yield more accurate | test oracles |     |     |     |     |
| ----------------- | ------ | ------------------- | ------------ | --- | --- | --- | --- |
and how to reduce the false positives among the reported There remain many research opportunities in ML testing.
issues.WecouldevenuseMLalgorithmbtolearntodetect
|     |     |     |     | These are | not necessarily | research | challenges, but may |
| --- | --- | --- | --- | --------- | --------------- | -------- | ------------------- |
false-positiveoracleswhentestingMLalgorithma. greatly benefit machine learning developers and users as
Challenges in Testing Cost Reduction. In traditional soft- wellasthewholeresearchcommunity.
ware testing, the cost problem remains a big problem, Testing More Application Scenarios. Much current re-
yielding many cost reduction techniques such as test selec- search focuses on supervised learning, in particular clas-
tion,testprioritisation,andpredictingtestexecutionresults. sification problems. More research is needed on problems
| In ML testing,  | the cost | problem could     | be more serious, |            |              |              |                   |
| --------------- | -------- | ----------------- | ---------------- | ---------- | ------------ | ------------ | ----------------- |
|                 |          |                   |                  | associated | with testing | unsupervised | and reinforcement |
| especially when | testing  | the ML component, | because ML       | learning.  |              |              |                   |
component testing usually requires model retraining or The testing tasks currently tackled in the literature,
repeatingofthepredictionprocess.Itmayalsorequiredata
primarilycentreonimageclassification.Thereremainopen
generationtoexploretheenormousmodebehaviourspace. excitingtestingresearchopportunitiesinmanyotherareas,
A possible research direction for cost reduction is to suchasspeechrecognition,naturallanguageprocessingand
represent an ML model as an intermediate state to make agent/gameplay.
iteasierfortesting. Testing More ML Categories and Tasks. We observed
We could also apply traditional cost reduction tech- pronounced imbalance regarding the coverage of testing
niques such as test prioritisation or minimisation to reduce techniques for different machine learning categories and

30
tasks,asdemonstratedbyTable4.Therearebothchallenges al. [205], [289], a good requirements analysis may tackle
and research opportunities for testing unsupervised and manynon-functionalpropertiessuchasfairness.
reinforcementlearningsystems. Existing work is focused on off-line testing. Online-
For instance, transfer learning, a topic gaining much testingdeservesmoreresearchefforts.
recent interest, focuses on storing knowledge gained while AccordingtotheworkofAmershietal.[8],datatesting
|         |             |     |     |          |     |                |     | is especially | important. |     | This | topic | certainly | deserves | more |
| ------- | ----------- | --- | --- | -------- | --- | -------------- | --- | ------------- | ---------- | --- | ---- | ----- | --------- | -------- | ---- |
| solving | one problem |     | and | applying | it  | to a different | but |               |            |     |      |       |           |          |      |
related problem [291]. Transfer learning testing is also im- research effort. Additionally, there are also many oppor-
portant,yetpoorlycoveredintheexistingliterature. tunitiesforregressiontesting,bugreportanalysis,andbug
triageinMLtesting.
| Testing | Other | Properties. |     | From Figure |     | 10, we can | see that |     |     |     |     |     |     |     |     |
| ------- | ----- | ----------- | --- | ----------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
mostworktestsrobustnessandcorrectness,whilerelatively Due to the black-box nature of machine learning al-
fewpapers(lessthan3%)studyefficiency,modelrelevance, gorithms, ML testing results are often more difficult for
developerstounderstand,comparedtotraditionalsoftware
orinterpretability.
Modelrelevancetestingischallengingbecausethedistri- testing.Visualisationoftestingresultsmightbeparticularly
|     |     |     |     |     |     |     |     | helpful in | ML  | testing | to help | developers |     | understand | the |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | ------- | ---------- | --- | ---------- | --- |
butionofthefuturedataisoftenunknown,whilethecapa-
bugsandhelpwiththebuglocalisationandrepair.
cityofmanymodelsisalsounknownandhardtomeasure.
It might be interesting to conduct empirical studies on the Mutating Investigation in Machine Learning System.
Therehavebeensomestudiesdiscussingmutatingmachine
| prevalence | of     | poor model |         | relevance | among | ML        | models as |           |             |          |           |     |             |          |          |
| ---------- | ------ | ---------- | ------- | --------- | ----- | --------- | --------- | --------- | ----------- | -------- | --------- | --- | ----------- | -------- | -------- |
|            |        |            |         |           |       |           |           | learning  | code [128], | [240],   | but       | no  | work has    | explored | how      |
| well as    | on the | balance    | between | poor      | model | relevance | and       |           |             |          |           |     |             |          |          |
|            |        |            |         |           |       |           |           | to better | design      | mutation | operators |     | for machine |          | learning |
highsecurityrisks.
|     |     |     |     |     |     |     |     | code so | that the | mutants | could | better | simulate |     | real-world |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------- | ----- | ------ | -------- | --- | ---------- |
Fortestingefficiency,thereisaneedtotesttheefficiency
machinelearningbugs.Thisisanotherresearchopportunity.
| at different | levels    | such       | as  | the efficiency |          | when        | switching |               |     |     |     |     |     |     |     |
| ------------ | --------- | ---------- | --- | -------------- | -------- | ----------- | --------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| among        | different | platforms, |     | machine        | learning | frameworks, |           |               |     |     |     |     |     |     |     |
|              |           |            |     |                |          |             |           | 11 CONCLUSION |     |     |     |     |     |     |     |
andhardwaredevices.
Fortestingpropertyinterpretability,existingapproaches
|     |     |     |     |     |     |     |     | We provided | a   | comprehensive |     | overview |     | and | analysis of |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | -------- | --- | --- | ----------- |
relyprimarilyonmanualassessment,whichcheckswhether
|     |     |     |     |     |     |     |     | research | work | on ML | testing. | The | survey | presented | the |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ----- | -------- | --- | ------ | --------- | --- |
humans could understand the logic or predictive results of definitionsandcurrentresearchstatusofdifferentMLtest-
an ML model. It will be also interesting to investigate the ing properties, testing components, and testing workflows.
| automatic | assessment |     | of interpretability |     |     | and the | detection |                    |     |     |          |      |     |             |     |
| --------- | ---------- | --- | ------------------- | --- | --- | ------- | --------- | ------------------ | --- | --- | -------- | ---- | --- | ----------- | --- |
|           |            |     |                     |     |     |         |           | It also summarised |     | the | datasets | used | for | experiments | and |
ofinterpretabilityviolations. the available open-source testing tools/frameworks, and
Thereisalackofconsensusregardingthedefinitionsand analysed the research trends, directions, opportunities, and
understandingoffairnessandinterpretability.Thereisthus
|     |     |     |     |     |     |     |     | challenges | in ML | testing. | We  | hope | this | survey | will help |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | -------- | --- | ---- | ---- | ------ | --------- |
a need for clearer definitions, formalisation, and empirical software engineering and machine learning researchers to
studiesunderdifferentcontexts. becomefamiliarwiththecurrentstatusandopenopportun-
There has been a discussion that machine learning test- itiesofandforofMLtesting.
| ing and      | traditional |        | software  | testing | may         | have | different |     |     |     |     |     |     |     |     |
| ------------ | ----------- | ------ | --------- | ------- | ----------- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| requirements |             | in the | assurance | to      | be expected | for  | different |     |     |     |     |     |     |     |     |
ACKNOWLEDGEMENT
properties[292].Therefore,moreworkisneededtoexplore
|              |          |                  |     |          |         |                |          | Before submitting, |       | we           | sent | the paper | to       | those | whom we   |
| ------------ | -------- | ---------------- | --- | -------- | ------- | -------------- | -------- | ------------------ | ----- | ------------ | ---- | --------- | -------- | ----- | --------- |
| and identify |          | those properties |     | that     | are     | most important | for      |                    |       |              |      |           |          |       |           |
|              |          |                  |     |          |         |                |          | cited, to          | check | our comments |      | for       | accuracy | and   | omission. |
| machine      | learning | systems,         |     | and thus | deserve | more           | research |                    |       |              |      |           |          |       |           |
andtesteffort. Thisalsoprovidedonefinalstageinthesystematictrawling
|            |      |         |     |            |     |         |           | of the literature |     | for relevant |     | work. | Many | thanks | to those |
| ---------- | ---- | ------- | --- | ---------- | --- | ------- | --------- | ----------------- | --- | ------------ | --- | ----- | ---- | ------ | -------- |
| Presenting | More | Testing |     | Benchmarks |     | A large | number of |                   |     |              |     |       |      |        |          |
membersofthecommunitywhokindlyprovidedcomments
| datasets | have | been adopted |     | in the | existing | ML testing | pa- |     |     |     |     |     |     |     |     |
| -------- | ---- | ------------ | --- | ------ | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andfeedbackonearlierdraftsofthispaper.
| pers.AsTables5to                                 |              | 8show,thesedatasetsareusuallythose |         |          |     |          |           |            |     |     |     |     |     |     |     |
| ------------------------------------------------ | ------------ | ---------------------------------- | ------- | -------- | --- | -------- | --------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| adopted                                          | for building |                                    | machine | learning |     | systems. | As far as |            |     |     |     |     |     |     |     |
| weknow,thereareveryfewbenchmarkslikeCleverHans17 |              |                                    |         |          |     |          |           | REFERENCES |     |     |     |     |     |     |     |
thatarespeciallydesignedforMLtestingresearchpurposes, [1] KexinPei,YinzhiCao,JunfengYang,andSumanJana. Deepx-
suchasadversarialexampleconstruction. plore:Automatedwhiteboxtestingofdeeplearningsystems. In
More benchmarks are needed, that are specially de- Proceedingsofthe26thSymposiumonOperatingSystemsPrinciples,
pages1–18.ACM,2017.
signedforMLtesting.Forexample,arepositoryofmachine [2] Chenyi Chen, Ari Seff, Alain Kornhauser, and Jianxiong Xiao.
learning programs with real bugs would present a good Deepdriving: Learning affordance for direct perception in
benchmark for bug-fixing techniques. Such an ML testing autonomous driving. In Proceedings of the IEEE International
ConferenceonComputerVision,pages2722–2730,2015.
| repository, | would | play | a   | similar | (and | equally-important) |     |           |          |       |       |                 |     |           |        |
| ----------- | ----- | ---- | --- | ------- | ---- | ------------------ | --- | --------- | -------- | ----- | ----- | --------------- | --- | --------- | ------ |
|             |       |      |     |         |      |                    |     | [3] Geert | Litjens, | Thijs | Kooi, | Babak Ehteshami |     | Bejnordi, | Arnaud |
role to that played by data sets such as Defects4J18 in ArindraAdiyosoSetio,FrancescoCiompi,MohsenGhafoorian,
traditionalsoftwaretesting. Jeroen Awm Van Der Laak, Bram Van Ginneken, and Clara I
|          |      |         |             |     |     |        |           | Sánchez. | Asurveyondeeplearninginmedicalimageanalysis. |     |     |     |     |     |     |
| -------- | ---- | ------- | ----------- | --- | --- | ------ | --------- | -------- | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
| Covering | More | Testing | Activities. |     | As  | far we | know, re- |          |                                              |     |     |     |     |     |     |
Medicalimageanalysis,42:60–88,2017.
| quirement | analysis | for | ML  | systems | remains | absent | in the |          |        |     |              |              |     |             |          |
| --------- | -------- | --- | --- | ------- | ------- | ------ | ------ | -------- | ------ | --- | ------------ | ------------ | --- | ----------- | -------- |
|           |          |     |     |         |         |        |        | [4] Paul | Ammann | and | Jeff Offutt. | Introduction |     | to software | testing. |
ML testing literature. As demonstrated by Finkelstein et CambridgeUniversityPress,2016.
|     |     |     |     |     |     |     |     | [5] SainyamGalhotra,YuriyBrun,andAlexandraMeliou. |     |     |     |     |     |                    | Fairness |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | -------- |
|     |     |     |     |     |     |     |     | testing:testingsoftwarefordiscrimination.         |     |     |     |     |     | InProceedingsofthe |          |
17https://github.com/tensorflow/cleverhans
|     |     |     |     |     |     |     |     | 2017 | 11th Joint | Meeting | on  | Foundations | of  | Software | Engineering, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---------- | ------- | --- | ----------- | --- | -------- | ------------ |
18https://github.com/rjust/defects4j
pages498–510.ACM,2017.

31
[6] Maciej Pacula. Unit-Testing Statistical Software. http://blog. [29] Adam Paszke, Sam Gross, Soumith Chintala, Gregory Chanan,
mpacula.com/2011/02/17/unit-testing-statistical-software/, Edward Yang, Zachary DeVito, Zeming Lin, Alban Desmaison,
2011. Luca Antiga, and Adam Lerer. Automatic differentiation in
[7] A. Ramanathan, L. L. Pullum, F. Hussain, D. Chakrabarty, and pytorch. 2017.
|     |     |     |     |     |     |     |     | [30] Martín | Abadi, | Ashish | Agarwal, | Paul | Barham, | Eugene | Brevdo, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------ | -------- | ---- | ------- | ------ | ------- |
S.K.Jha.Integratingsymbolicandstatisticalmethodsfortesting
intelligentsystems:Applicationstomachinelearningandcom- ZhifengChen,CraigCitro,GregS.Corrado,AndyDavis,Jeffrey
putervision. In2016Design,AutomationTestinEuropeConference Dean, Matthieu Devin, Sanjay Ghemawat, Ian Goodfellow, An-
Exhibition(DATE),pages786–791,March2016. drew Harp, Geoffrey Irving, Michael Isard, Yangqing Jia, Rafal
[8] Saleema Amershi, Andrew Begel, Christian Bird, Rob DeLine, Jozefowicz, Lukasz Kaiser, Manjunath Kudlur, Josh Levenberg,
|     |     |     |     |     |     |     |     | Dan | Mané, | Rajat | Monga, | Sherry | Moore, | Derek | Murray, Chris |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ------ | ------ | ------ | ----- | ------------- |
HaraldGall,EceKamar,NachiNagappan,BesmiraNushi,and
|                |     |     |                                        |     |     |     |     | Olah, | Mike | Schuster, | Jonathon | Shlens, | Benoit | Steiner, | Ilya Sut- |
| -------------- | --- | --- | -------------------------------------- | --- | --- | --- | --- | ----- | ---- | --------- | -------- | ------- | ------ | -------- | --------- |
| TomZimmermann. |     |     | Softwareengineeringformachinelearning: |     |     |     |     |       |      |           |          |         |        |          |           |
Acasestudy. InProc.ICSE(IndustryTrack),pages291–300,2019. skever, Kunal Talwar, Paul Tucker, Vincent Vanhoucke, Vijay
[9] Earl T Barr, Mark Harman, Phil McMinn, Muzammil Shahbaz, Vasudevan,FernandaViégas,OriolVinyals,PeteWarden,Mar-
andShinYoo. Theoracleprobleminsoftwaretesting:Asurvey. tin Wattenberg, Martin Wicke, Yuan Yu, and Xiaoqiang Zheng.
TensorFlow:Large-scalemachinelearningonheterogeneoussys-
IEEEtransactionsonsoftwareengineering,41(5):507–525,2015.
|                                                 |     |     |     |     |     |     |            | tems,2015. |     | Softwareavailablefromtensorflow.org. |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
| [10] ChristianMurphy,GailEKaiser,andMartaArias. |     |     |     |     |     |     | Anapproach |            |     |                                      |     |     |     |     |     |
[31] F.Pedregosa,G.Varoquaux,A.Gramfort,V.Michel,B.Thirion,
| to  | software | testing | of machine | learning | applications. |     | In Proc. |     |     |     |     |     |     |     |     |
| --- | -------- | ------- | ---------- | -------- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
SEKE,volume167,2007. O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg,
[11] MartinD.DavisandElaineJ.Weyuker. Pseudo-oraclesfornon- J.Vanderplas,A.Passos,D.Cournapeau,M.Brucher,M.Perrot,
testableprograms. InProceedingsoftheACM81Conference,ACM and E. Duchesnay. Scikit-learn: Machine Learning in Python .
JournalofMachineLearningResearch,12:2825–2830,2011.
81,pages254–257,1981.
|            |                  |        |          |        |          |                   |              | [32] FrançoisCholletetal. |       |           | Keras.     | https://keras.io,2015. |             |        |            |
| ---------- | ---------------- | ------ | -------- | ------ | -------- | ----------------- | ------------ | ------------------------- | ----- | --------- | ---------- | ---------------------- | ----------- | ------ | ---------- |
| [12] Kelly | Androutsopoulos, |        | David    | Clark, | Haitao   | Dan,              | Mark Har-    |                           |       |           |            |                        |             |        |            |
|            |                  |        |          |        |          |                   |              | [33] Yangqing             |       | Jia, Evan | Shelhamer, | Jeff                   | Donahue,    | Sergey | Karayev,   |
| man,       | and              | Robert | Hierons. | An     | analysis | of the            | relationship |                           |       |           |            |                        |             |        |            |
|            |                  |        |          |        |          |                   |              | Jonathan                  | Long, | Ross      | Girshick,  | Sergio                 | Guadarrama, |        | and Trevor |
| between    | conditional      |        | entropy  | and    | failed   | error propagation |              | in                        |       |           |            |                        |             |        |            |
softwaretesting.InProc.ICSE,pages573–583,Hyderabad,India, Darrell.Caffe:Convolutionalarchitectureforfastfeatureembed-
arXivpreprintarXiv:1408.5093,2014.
| June2014. |     |     |     |     |     |     |     | ding. |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
[34] MichaelIJordanandTomMMitchell.Machinelearning:Trends,
[13] JeffreyM.VoasandKeithW.Miller.Softwaretestability:Thenew
|               |       |                                   |        |             |              |     |            | perspectives,andprospects.             |     |     |     | Science,349(6245):255–260,2015. |     |                   |     |
| ------------- | ----- | --------------------------------- | ------ | ----------- | ------------ | --- | ---------- | -------------------------------------- | --- | --- | --- | ------------------------------- | --- | ----------------- | --- |
| verification. |       | IEEESoftware,12(3):17–28,May1995. |        |             |              |     |            |                                        |     |     |     |                                 |     |                   |     |
|               |       |                                   |        |             |              |     |            | [35] SRasoulSafavianandDavidLandgrebe. |     |     |     |                                 |     | Asurveyofdecision |     |
| [14] David    | Clark | and                               | Robert | M. Hierons. | Squeeziness: |     | An inform- |                                        |     |     |     |                                 |     |                   |     |
treeclassifiermethodology.IEEEtransactionsonsystems,man,and
| ationtheoreticmeasureforavoidingfaultmasking. |     |     |     |     |     |     | Information |     |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
ProcessingLetters,112(8–9):335–340,2012. cybernetics,21(3):660–674,1991.
[15] Yue Jia and Mark Harman. Constructing subtle faults using [36] John Neter, Michael H Kutner, Christopher J Nachtsheim, and
|        |       |          |         |       |       |       |          | William | Wasserman. |     | Applied | linear | statistical | models, | volume 4. |
| ------ | ----- | -------- | ------- | ----- | ----- | ----- | -------- | ------- | ---------- | --- | ------- | ------ | ----------- | ------- | --------- |
| higher | order | mutation | testing | (best | paper | award | winner). | In      |            |     |         |        |             |         |           |
IrwinChicago,1996.
| 8th          | International | Working    |     | Conference     | on Source | Code     | Analysis and |                                      |     |     |     |     |                    |     |     |
| ------------ | ------------- | ---------- | --- | -------------- | --------- | -------- | ------------ | ------------------------------------ | --- | --- | --- | --- | ------------------ | --- | --- |
|              |               |            |     |                |           |          |              | [37] AndrewMcCallum,KamalNigam,etal. |     |     |     |     | Acomparisonofevent |     |     |
| Manipulation |               | (SCAM’08), |     | pages 249–258, |           | Beijing, | China, 2008. |                                      |     |     |     |     |                    |     |     |
modelsfornaivebayestextclassification.InAAAI-98workshopon
IEEEComputerSociety.
learningfortextcategorization,volume752,pages41–48.Citeseer,
| [16] Christopher |     | D Turner | and | David | J Robson. | The | state-based | 1998. |     |     |     |     |     |     |     |
| ---------------- | --- | -------- | --- | ----- | --------- | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
testingofobject-orientedprograms.In1993ConferenceonSoftware
|     |     |     |     |     |     |     |     | [38] YannLeCun,YoshuaBengio,andGeoffreyHinton. |     |     |     |     |     |     | Deeplearn- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | ---------- |
Maintenance,pages302–310.IEEE,1993.
ing. nature,521(7553):436,2015.
| [17] MarkHarmanandBryanFJones. |                                                       |     |              |     | Search-basedsoftwareengin- |     |           |               |                                    |                                                  |     |          |     |          |         |
| ------------------------------ | ----------------------------------------------------- | --- | ------------ | --- | -------------------------- | --- | --------- | ------------- | ---------------------------------- | ------------------------------------------------ | --- | -------- | --- | -------- | ------- |
|                                |                                                       |     |              |     |                            |     |           | [39] YoonKim. |                                    | Convolutionalneuralnetworksforsentenceclassific- |     |          |     |          |         |
| eering.                        | InformationandsoftwareTechnology,43(14):833–839,2001. |     |              |     |                            |     |           |               |                                    |                                                  |     |          |     |          |         |
|                                |                                                       |     |              |     |                            |     |           | ation.        | arXivpreprintarXiv:1408.5882,2014. |                                                  |     |          |     |          |         |
| [18] Mark                      | Harman                                                | and | Phil McMinn. |     | A theoretical              | and | empirical |               |                                    |                                                  |     |          |     |          |         |
|                                |                                                       |     |              |     |                            |     |           | [40] Alex     | Graves,                            | Abdel-rahman                                     |     | Mohamed, | and | Geoffrey | Hinton. |
study of search-based testing: Local, global, and hybrid search. Speech recognition with deep recurrent neural networks. In
IEEETransactionsonSoftwareEngineering,36(2):226–247,2010.
|           |          |     |              |          |     |          |           | 2013 | IEEE | international | conference |     | on acoustics, | speech | and signal |
| --------- | -------- | --- | ------------ | -------- | --- | -------- | --------- | ---- | ---- | ------------- | ---------- | --- | ------------- | ------ | ---------- |
| [19] Atif | M Memon. |     | Gui testing: | Pitfalls | and | process. | Computer, |      |      |               |            |     |               |        |            |
processing,pages6645–6649.IEEE,2013.
(8):87–88,2002.
|              |      |       |          |     |           |       |            | [41] Ieee | standard | classification |     | for software |     | anomalies. | IEEE Std |
| ------------ | ---- | ----- | -------- | --- | --------- | ----- | ---------- | --------- | -------- | -------------- | --- | ------------ | --- | ---------- | -------- |
| [20] Koushik | Sen, | Darko | Marinov, | and | Gul Agha. | Cute: | a concolic |           |          |                |     |              |     |            |          |
1044-2009(RevisionofIEEEStd1044-1993),pages1–23,Jan2010.
| unittestingengineforc. |     |     |     | InACMSIGSOFTSoftwareEngineering |     |     |     |            |               |     |        |         |     |       |             |
| ---------------------- | --- | --- | --- | ------------------------------- | --- | --- | --- | ---------- | ------------- | --- | ------ | ------- | --- | ----- | ----------- |
|                        |     |     |     |                                 |     |     |     | [42] Roman | Werpachowski, |     | András | György, | and | Csaba | Szepesvári. |
Notes,volume30,pages263–272.ACM,2005. Detecting overfitting via adversarial examples. arXiv preprint
[21] G. Hains, A. Jakobsson, and Y. Khmelevsky. Towards formal arXiv:1903.02380,2019.
methods and software engineering for deep learning: Security, [43] Juan Cruz-Benito, Andrea Vázquez-Ingelmo, José Carlos
| safety | and | productivity | for | DL systems | development. |     | In 2018 |                 |     |         |     |                   |     |                      |     |
| ------ | --- | ------------ | --- | ---------- | ------------ | --- | ------- | --------------- | --- | ------- | --- | ----------------- | --- | -------------------- | --- |
|        |     |              |     |            |              |     |         | Sánchez-Prieto, |     | Roberto |     | Therón, Francisco |     | José García-Peñalvo, |     |
AnnualIEEEInternationalSystemsConference(SysCon),pages1–5,
andMartínMartín-González.Enablingadaptabilityinwebforms
April2018.
basedonusercharacteristicsdetectionthrougha/btestingand
[22] Lei Ma, Felix Juefei-Xu, Minhui Xue, Qiang Hu, Sen Chen, machinelearning. IEEEAccess,6:2251–2265,2018.
Bo Li, Yang Liu, Jianjun Zhao, Jianxiong Yin, and Simon See. [44] Emilie Kaufmann, Olivier Cappé, and Aurélien Garivier. On
Securedeeplearningengineering:Asoftwarequalityassurance thecomplexityofbest-armidentificationinmulti-armedbandit
| perspective. |     | arXivpreprintarXiv:1810.04538,2018. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
models.TheJournalofMachineLearningResearch,17(1):1–42,2016.
| [23] Xiaowei | Huang, | Daniel | Kroening, |     | Marta | Kwiatkowska, | Wenjie |           |        |         |            |       |      |        |            |
| ------------ | ------ | ------ | --------- | --- | ----- | ------------ | ------ | --------- | ------ | ------- | ---------- | ----- | ---- | ------ | ---------- |
|              |        |        |           |     |       |              |        | [45] Eric | Breck, | Neoklis | Polyzotis, | Sudip | Roy, | Steven | Whang, and |
Ruan, Youcheng Sun, Emese Thamo, Min Wu, and Xinping Yi. Martin Zinkevich. Data Validation for Machine Learning. In
| Safety | and | trustworthiness |     | of deep | neural | networks: | A survey. | SysML,2019. |     |     |     |     |     |     |     |
| ------ | --- | --------------- | --- | ------- | ------ | --------- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
arXivpreprintarXiv:1812.08342,2018. [46] Chih-HongCheng,GeorgNührenberg,Chung-HaoHuang,and
[24] Satoshi Masuda, Kohichi Ono, Toshiaki Yasue, and Nobuhiro Hirotoshi Yasuoka. Towards dependability metrics for neural
| Hosokawa.     |     | A survey | of   | software      | quality    | for machine | learning    |            |         |                                     |      |          |          |      |           |
| ------------- | --- | -------- | ---- | ------------- | ---------- | ----------- | ----------- | ---------- | ------- | ----------------------------------- | ---- | -------- | -------- | ---- | --------- |
|               |     |          |      |               |            |             |             | networks.  |         | arXivpreprintarXiv:1806.02338,2018. |      |          |          |      |           |
| applications. |     | In 2018  | IEEE | International | Conference |             | on Software |            |         |                                     |      |          |          |      |           |
|               |     |          |      |               |            |             |             | [47] Scott | Alfeld, | Xiaojin                             | Zhu, | and Paul | Barford. | Data | poisoning |
Testing,VerificationandValidationWorkshops(ICSTW),pages279– attacksagainstautoregressivemodels.InAAAI,pages1452–1458,
| 284.IEEE,2018. |     |     |     |     |     |     |     | 2016. |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
[25] Fuyuki Ishikawa. Concepts in quality assessment for machine [48] WeizhenQiLinTanVietHungPham,ThibaudLutellier. Cradle:
learning-fromtestdatatoarguments. InInternationalConference Cross-backend validation to detect and localize bugs in deep
onConceptualModeling,pages536–544.Springer,2018.
|     |     |     |     |     |     |     |     | learninglibraries. |     |     | InProc.ICSE,2019. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | ----------------- | --- | --- | --- | --- |
[26] HoussemBraiekandFoutseKhomh.Ontestingmachinelearning
[49] LawrenceChung,BrianANixon,EricYu,andJohnMylopoulos.
programs. arXivpreprintarXiv:1812.02257,2018. Non-functional requirements in software engineering, volume 5.
[27] John Shawe-Taylor, Nello Cristianini, et al. Kernel methods for SpringerScience&BusinessMedia,2012.
patternanalysis. Cambridgeuniversitypress,2004. [50] Wasif Afzal, Richard Torkar, and Robert Feldt. A systematic
[28] Mehryar Mohri, Afshin Rostamizadeh, and Ameet Talwalkar. review of search-based testing for non-functional system prop-
Foundationsofmachinelearning. MITpress,2012. erties. InformationandSoftwareTechnology,51(6):957–976,2009.

32
[51] MatthewKirk. Thoughtfulmachinelearning:Atest-drivenapproach. cars. InProceedingsofthe40thInternationalConferenceonSoftware
"O’ReillyMedia,Inc.",2014. Engineering,pages303–314.ACM,2018.
[52] VladimirVapnik,EstherLevin,andYannLeCun.Measuringthe [77] udacity. Udacity challenge. https://github.com/udacity/self-
| vc-dimensionofalearningmachine.Neuralcomputation,6(5):851– |     |     |     |     |     |     |     | driving-car. |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
876,1994.
|                                        |     |     |     |     |                   |     |     | [78] Ian | Goodfellow, | Jean | Pouget-Abadie, |     | Mehdi | Mirza, | Bing Xu, |
| -------------------------------------- | --- | --- | --- | --- | ----------------- | --- | --- | -------- | ----------- | ---- | -------------- | --- | ----- | ------ | -------- |
| [53] DavidSRosenbergandPeterLBartlett. |     |     |     |     | Therademachercom- |     |     |          |             |      |                |     |       |        |          |
DavidWarde-Farley,SherjilOzair,AaronCourville,andYoshua
plexity of co-regularized kernel classes. In Artificial Intelligence Bengio. Generative adversarial nets. In Advances in neural
andStatistics,pages396–403,2007. informationprocessingsystems,pages2672–2680,2014.
[54] JieZhang,EarlTBarr,BenjaminGuedj,MarkHarman,andJohn [79] MengshiZhang,YuqunZhang,LingmingZhang,CongLiu,and
Shawe-Taylor. PerturbedModelValidation:ANewFramework SarfrazKhurshid. DeepRoad:GAN-basedMetamorphicTesting
| to Validate | Model | Relevance. |     | working | paper | or  | preprint, May |     |     |     |     |     |     |     |     |
| ----------- | ----- | ---------- | --- | ------- | ----- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
andInputValidationFrameworkforAutonomousDrivingSys-
2019. tems.InProceedingsofthe33rdACM/IEEEInternationalConference
[55] Ieeestandardglossaryofsoftwareengineeringterminology.IEEE onAutomatedSoftwareEngineering,ASE2018,pages132–142,2018.
Std610.12-1990,pages1–84,Dec1990. [80] Ming-Yu Liu, Thomas Breuel, and Jan Kautz. Unsupervised
[56] AliShahrokniandRobertFeldt.Asystematicreviewofsoftware image-to-image translation networks. In Advances in Neural
robustness. InformationandSoftwareTechnology,55(1):1–17,2013. InformationProcessingSystems,pages700–708,2017.
[57] GuyKatz,ClarkBarrett,DavidLDill,KyleJulian,andMykelJ
|               |     |           |     |           |     |        |               | [81] Husheng | Zhou,  | Wei | Li, Yuankun |      | Zhu, Yuqun     | Zhang,     | Bei Yu, |
| ------------- | --- | --------- | --- | --------- | --- | ------ | ------------- | ------------ | ------ | --- | ----------- | ---- | -------------- | ---------- | ------- |
| Kochenderfer. |     | Reluplex: | An  | efficient | smt | solver | for verifying |              |        |     |             |      |                |            |         |
|               |     |           |     |           |     |        |               | Lingming     | Zhang, |     | and Cong    | Liu. | Deepbillboard: | Systematic |         |
deep neural networks. In International Conference on Computer physical-world testing of autonomous driving systems. arXiv
AidedVerification,pages97–117.Springer,2017. preprintarXiv:1812.10812,2018.
[58] CynthiaDwork.Differentialprivacy.EncyclopediaofCryptography [82] XiaoningDu,XiaofeiXie,YiLi,LeiMa,JianjunZhao,andYang
andSecurity,pages338–340,2011.
|                                          |     |     |     |     |                      |                    |     | Liu.                                       | Deepcruiser: |                                     | Automated | guided | testing | for stateful | deep |
| ---------------------------------------- | --- | --- | --- | --- | -------------------- | ------------------ | --- | ------------------------------------------ | ------------ | ----------------------------------- | --------- | ------ | ------- | ------------ | ---- |
| [59] PaulVoigtandAxelvondemBussche.      |     |     |     |     | TheEUGeneralDataPro- |                    |     |                                            |              |                                     |           |        |         |              |      |
|                                          |     |     |     |     |                      |                    |     | learningsystems.                           |              | arXivpreprintarXiv:1812.05339,2018. |           |        |         |              |      |
| tectionRegulation(GDPR):APracticalGuide. |     |     |     |     |                      | SpringerPublishing |     |                                            |              |                                     |           |        |         |              |      |
|                                          |     |     |     |     |                      |                    |     | [83] JunhuaDing,DongmeiZhang,andXin-HuaHu. |              |                                     |           |        |         | Aframework   |      |
Company,Incorporated,1stedition,2017.
|     |     |     |     |     |     |     |     | for | ensuring | the quality | of  | a big | data service. | In  | 2016 IEEE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | --- | ----- | ------------- | --- | --------- |
[60] wikipedia. California Consumer Privacy Act. https://en. InternationalConferenceonServicesComputing(SCC),pages82–89.
| wikipedia.org/wiki/California_Consumer_Privacy_Act. |     |        |          |                    |     |     |            | IEEE,2016. |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | ------ | -------- | ------------------ | --- | --- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| [61] R. Baeza-Yates                                 |     | and Z. | Liaghat. | Quality-efficiency |     |     | trade-offs | in         |     |     |     |     |     |     |     |
[84] MdRafiqulIslamRabin,KeWang,andMohammadAminAli-
| machinelearningfortextprocessing. |     |     |     |     | In2017IEEEInternational |     |     |       |                                     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | ----------------------- | --- | --- | ----- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
|                                   |     |     |     |     |                         |     |     | pour. | Testingneuralprogramanalyzers,2019. |     |     |     |     |     |     |
ConferenceonBigData(BigData),pages897–904,Dec2017.
|          |                |     |            |       |     |         |          | [85] Uri                                           | Alon, | Meital | Zilberstein, | Omer | Levy, | and Eran | Yahav.   |
| -------- | -------------- | --- | ---------- | ----- | --- | ------- | -------- | -------------------------------------------------- | ----- | ------ | ------------ | ---- | ----- | -------- | -------- |
| [62] Sam | Corbett-Davies |     | and Sharad | Goel. | The | measure | and mis- |                                                    |       |        |              |      |       |          |          |
|          |                |     |            |       |     |         |          | code2vec:Learningdistributedrepresentationsofcode. |       |        |              |      |       |          | Proceed- |
measure of fairness: A critical review of fair machine learning. ingsoftheACMonProgrammingLanguages,3(POPL):40,2019.
arXivpreprintarXiv:1808.00023,2018. [86] Zeyu Sun, Jie M. Zhang, Mark Harman, Mike Papadakis, and
| [63] DrewSDaysIII.   |                        | Feedbackloop:Thecivilrightsactof1964and |     |     |     |     |       |              |         |                             |         |          |             |                  |         |
| -------------------- | ---------------------- | --------------------------------------- | --- | --- | --- | --- | ----- | ------------ | ------- | --------------------------- | ------- | -------- | ----------- | ---------------- | ------- |
|                      |                        |                                         |     |     |     |     |       | Lu           | Zhang.  | Automatic                   | testing | and      | improvement | of               | machine |
| itsprogeny.          | .LouisULJ,49:981,2004. |                                         |     |     |     |     |       |              |         |                             |         |          |             |                  |         |
|                      |                        |                                         |     |     |     |     |       | translation. |         | InProc.ICSE(toappear),2020. |         |          |             |                  |         |
| [64] ZacharyCLipton. |                        | Themythosofmodelinterpretability.       |     |     |     |     | arXiv |              |         |                             |         |          |             |                  |         |
|                      |                        |                                         |     |     |     |     |       | [87] Phil    | McMinn. | Search-based                |         | software | test        | data generation: | a       |
preprintarXiv:1606.03490,2016.
|                                   |     |     |     |                           |     |     |     | survey. | Software | testing, | Verification |     | and reliability, | 14(2):105–156, |     |
| --------------------------------- | --- | --- | --- | ------------------------- | --- | --- | --- | ------- | -------- | -------- | ------------ | --- | ---------------- | -------------- | --- |
| [65] FinaleDoshi-VelezandBeenKim. |     |     |     | Towardsarigorousscienceof |     |     |     |         |          |          |              |     |                  |                |     |
2004.
| interpretablemachinelearning. |     |     |     | arXivpreprintarXiv:1702.08608, |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2017. [88] Kiran Lakhotia, Mark Harman, and Phil McMinn. A multi-
|     |     |     |     |     |     |     |     | objective | approach |     | to search-based |     | test data | generation. | In  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | --------------- | --- | --------- | ----------- | --- |
[66] ThibaultSellam,KevinLin,IanYiranHuang,MichelleYang,Carl
Proceedingsofthe9thannualconferenceonGeneticandevolutionary
| Vondrick,andEugeneWu. |     |     | Deepbase:Deepinspectionofneural |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
computation,pages1098–1105.ACM,2007.
| networks.                       | InProc.SIGMOD,2019. |     |     |                               |     |     |     |               |       |     |                 |     |             |           |     |
| ------------------------------- | ------------------- | --- | --- | ----------------------------- | --- | --- | --- | ------------- | ----- | --- | --------------- | --- | ----------- | --------- | --- |
|                                 |                     |     |     |                               |     |     |     | [89] Augustus | Odena | and | Ian Goodfellow. |     | TensorFuzz: | Debugging |     |
| [67] OrBiranandCourtenayCotton. |                     |     |     | Explanationandjustificationin |     |     |     |               |       |     |                 |     |             |           |     |
machinelearning:Asurvey. InIJCAI-17WorkshoponExplainable NeuralNetworkswithCoverage-GuidedFuzzing. arXivpreprint
| AI(XAI),page8,2017. |     |     |     |     |     |     |     | arXiv:1807.10875,2018. |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
[68] Tim Miller. Explanation in artificial intelligence: Insights from [90] JianminGuo,YuJiang,YueZhao,QuanChen,andJiaguangSun.
|                    |     |                              |     |     |     |     |     | Dlfuzz:differentialfuzzingtestingofdeeplearningsystems. |     |     |     |     |     |     | In  |
| ------------------ | --- | ---------------------------- | --- | --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| thesocialsciences. |     | ArtificialIntelligence,2018. |     |     |     |     |     |                                                         |     |     |     |     |     |     |     |
Proc.FSE,pages739–743.ACM,2018.
| [69] BryceGoodmanandSethFlaxman. |     |     |     |     | Europeanunionregulations |     |     |     |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[91] XiaofeiXie,LeiMa,FelixJuefei-Xu,HongxuChen,MinhuiXue,
| on algorithmic |     | decision-making |     | and | a" right | to  | explanation". |     |     |     |     |     |     |     |     |
| -------------- | --- | --------------- | --- | --- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
arXivpreprintarXiv:1606.08813,2016. Bo Li, Yang Liu, Jianjun Zhao, Jianxiong Yin, and Simon See.
[70] Christoph Molnar. Interpretable Machine Learning. Coverage-guided fuzzing for deep neural networks. arXiv pre-
printarXiv:1809.01266,2018.
| https://christophm.github.io/interpretable-ml-book/, |     |     |     |     |     |     | 2019. |          |           |            |        |     |               |      |        |
| ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | -------- | --------- | ---------- | ------ | --- | ------------- | ---- | ------ |
|                                                      |     |     |     |     |     |     |       | [92] Lei | Ma, Felix | Juefei-Xu, | Fuyuan |     | Zhang, Jiyuan | Sun, | Minhui |
https://christophm.github.io/interpretable-ml-book/.
|                     |        |       |                                   |      |         |        |           | Xue,                | Bo Li, | Chunyang | Chen,                              | Ting | Su, Li Li, | Yang Liu, | Jianjun |
| ------------------- | ------ | ----- | --------------------------------- | ---- | ------- | ------ | --------- | ------------------- | ------ | -------- | ---------------------------------- | ---- | ---------- | --------- | ------- |
| [71] Jie Zhang,     | Junjie | Chen, | Dan                               | Hao, | Yingfei | Xiong, | Bing Xie, |                     |        |          |                                    |      |            |           |         |
|                     |        |       |                                   |      |         |        |           | Zhao,andYadongWang. |        |          | DeepGauge:Multi-granularityTesting |      |            |           |         |
| LuZhang,andHongMei. |        |       | Search-basedinferenceofpolynomial |      |         |        |           |                     |        |          |                                    |      |            |           |         |
metamorphic relations. In Proceedings of the 29th ACM/IEEE Criteria for Deep Learning Systems. In Proceedings of the 33rd
international conference on Automated software engineering, pages ACM/IEEE International Conference on Automated Software Engin-
eering,ASE2018,pages120–131,2018.
701–712.ACM,2014.
|              |          |      |        |          |     |           |      | [93] Matthew | Wicker, |     | Xiaowei | Huang, | and Marta | Kwiatkowska. |     |
| ------------ | -------- | ---- | ------ | -------- | --- | --------- | ---- | ------------ | ------- | --- | ------- | ------ | --------- | ------------ | --- |
| [72] Matthew | O’Kelly, | Aman | Sinha, | Hongseok |     | Namkoong, | Russ |              |         |     |         |        |           |              |     |
Feature-guidedblack-boxsafetytestingofdeepneuralnetworks.
| Tedrake, | and | John C | Duchi. | Scalable | end-to-end |     | autonomous |     |     |     |     |     |     |     |     |
| -------- | --- | ------ | ------ | -------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
vehicle testingviarare-eventsimulation. InAdvancesinNeural InInternationalConferenceonToolsandAlgorithmsfortheConstruc-
InformationProcessingSystems,pages9827–9838,2018. tionandAnalysisofSystems,pages408–426,2018.
[73] WeimingXiang,PatrickMusau,AyanaAWild,DiegoManzanas [94] Jonathan Uesato, Ananya Kumar, Csaba Szepesvari, Tom Erez,
Lopez,NathanielHamilton,XiaodongYang,JoelRosenfeld,and AvrahamRuderman,KeithAnderson,NicolasHeess,Pushmeet
|                 |     |                                          |     |     |     |     |     | Kohli,etal. |     | Rigorousagentevaluation:Anadversarialapproach |     |     |     |     |     |
| --------------- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | ----------- | --- | --------------------------------------------- | --- | --- | --- | --- | --- |
| TaylorTJohnson. |     | Verificationformachinelearning,autonomy, |     |     |     |     |     |             |     |                                               |     |     |     |     |     |
and neural networks survey. arXiv preprint arXiv:1810.01989, to uncover catastrophic failures. In International Conference on
| 2018. |     |     |     |     |     |     |     | LearningRepresentations,2019. |     |     |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
[74] ClaesWohlin.Guidelinesforsnowballinginsystematicliterature [95] ZhiQuanZhouandLiqunSun. Metamorphictestingofdriver-
studiesandareplicationinsoftwareengineering. InProceedings lesscars. CommunicationsoftheACM,62(3):61–67,2019.
of the 18th international conference on evaluation and assessment in [96] Saurabh Jha, Subho S Banerjee, Timothy Tsai, Siva KS Hari,
softwareengineering,page38.Citeseer,2014. MichaelBSullivan,ZbigniewTKalbarczyk,StephenWKeckler,
[75] Aws Albarghouthi and Samuel Vinitsky. Fairness-aware pro- andRavishankarKIyer.Ml-basedfaultinjectionforautonomous
gramming. In Proceedings of the Conference on Fairness, Account- vehicles. InProc.DSN,2019.
ability,andTransparency,pages211–219.ACM,2019. [97] Sakshi Udeshi and Sudipta Chattopadhyay. Grammar based
[76] YuchiTian,KexinPei,SumanJana,andBaishakhiRay.DeepTest: directed testing of machine learning systems. arXiv preprint
Automated testing of deep-neural-network-driven autonomous arXiv:1902.10027,2019.

33
[98] Yixin Nie, Yicheng Wang, and Mohit Bansal. Analyzing [119] Mark Hall, Eibe Frank, Geoffrey Holmes, Bernhard Pfahringer,
compositionality-sensitivity of nli models. arXiv preprint PeterReutemann,andIanHWitten. Thewekadataminingsoft-
arXiv:1811.07033,2018. ware:anupdate. ACMSIGKDDexplorationsnewsletter,11(1):10–
[99] HaohanWang,DaSun,andEricPXing.Whatifwesimplyswap 18,2009.
the two text fragments? a straightforward yet effective way to [120] ShinNakajima. Generalizedoraclefortestingmachinelearning
testtherobustnessofmethodstoconfoundingsignalsinnature computerprograms.InInternationalConferenceonSoftwareEngin-
languageinferencetasks. arXivpreprintarXiv:1809.02719,2018. eeringandFormalMethods,pages174–179.Springer,2017.
[100] Alvin Chan, Lei Ma, Felix Juefei-Xu, Xiaofei Xie, Yang Liu, [121] Anurag Dwarakanath, Manish Ahuja, Samarth Sikand, Rag-
and Yew Soon Ong. Metamorphic relation based adversarial hothamM.Rao,R.P.JagadeeshChandraBose,NevilleDubash,
attacks on differentiable neural computer. arXiv preprint andSanjayPodder.Identifyingimplementationbugsinmachine
arXiv:1809.02444,2018. learning based image classifiers using metamorphic testing. In
[101] Sakshi Udeshi, Pryanshu Arora, and Sudipta Chattopadhyay. Proceedingsofthe27thACMSIGSOFTInternationalSymposiumon
Automated directed fairness testing. In Proceedings of the 33rd SoftwareTestingandAnalysis,pages118–128,2018.
ACM/IEEE International Conference on Automated Software Engin- [122] ArnabSharmaandHeikeWehrheim. Testingmachinelearning
eering,pages98–108.ACM,2018. algorithmsforbalanceddatausage.InProc.ICST,pages125–135,
[102] Cumhur Erkan Tuncali, Georgios Fainekos, Hisahiro Ito, and 2019.
James Kapinski. Simulation-based adversarial test generation [123] Sadam Al-Azani and Jameleddine Hassine. Validation of ma-
forautonomousvehicleswithmachinelearningcomponents. In chine learning classifiers using metamorphic testing and fea-
IEEEIntelligentVehiclesSymposium(IV),2018. ture selection techniques. In International Workshop on Multi-
[103] AlanHartman. Softwareandhardwaretestingusingcombinat- disciplinaryTrendsinArtificialIntelligence,pages77–91.Springer,
orialcoveringsuites.InGraphtheory,combinatoricsandalgorithms, 2017.
pages237–266.Springer,2005. [124] Manikandasriram Srinivasan Ramanagopal, Cyrus Anderson,
[104] ScottKirkpatrick,CDanielGelatt,andMarioPVecchi. Optimiz- Ram Vasudevan, and Matthew Johnson-Roberson. Failing to
ationbysimulatedannealing. science,220(4598):671–680,1983. learn: Autonomously identifying perception failures for self-
[105] JamesCKing.Symbolicexecutionandprogramtesting.Commu- drivingcars.IEEERoboticsandAutomationLetters,3(4):3860–3867,
nicationsoftheACM,19(7):385–394,1976. 2018.
[106] LingmingZhang,TaoXie,LuZhang,NikolaiTillmann,Jonathan [125] XiaoyuanXie,ZhiyiZhang,TsongYuehChen,YangLiu,Pak-Lok
DeHalleux,andHongMei. Testgenerationviadynamicsym- Poon,andBaowenXu. Mettle:Ametamorphictestingapproach
bolic execution for mutation testing. In Software Maintenance tovalidatingunsupervisedmachinelearningmethods,2018.
(ICSM),2010IEEEInternationalConferenceon,pages1–10.IEEE, [126] Shin Nakajima. Dataset diversity for metamorphic testing of
2010. machine learning software. In International Workshop on Struc-
[107] TingChen,Xiao-songZhang,Shi-zeGuo,Hong-yuanLi,andYue tured Object-Oriented Formal Language and Method, pages 21–38.
Wu. Stateoftheart:Dynamicsymbolicexecutionforautomated Springer,2018.
testgeneration. FutureGenerationComputerSystems,29(7):1758– [127] Jinhan Kim, Robert Feldt, and Shin Yoo. Guiding deep learn-
1773,2013. ing system testing using surprise adequacy. arXiv preprint
[108] DivyaGopinath,KaiyuanWang,MengshiZhang,CorinaSPas- arXiv:1808.08444,2018.
areanu, and Sarfraz Khurshid. Symbolic execution for deep [128] Christian Murphy, Kuang Shen, and Gail Kaiser. Automatic
neuralnetworks. arXivpreprintarXiv:1807.10439,2018. System Testing of Programs Without Test Oracles. In 18th In-
[109] Aniya Agarwal, Pranay Lohia, Seema Nagar, Kuntal Dey, and ternationalSymposiumonSoftwareTestingandAnalysis,ISSTA’09,
DiptikalyanSaha.Automatedtestgenerationtodetectindividual pages189–200,2009.
discriminationinaimodels.arXivpreprintarXiv:1809.03260,2018. [129] L.SunandZ.Q.Zhou. MetamorphicTestingforMachineTrans-
[110] Marco Tulio Ribeiro, Sameer Singh, and Carlos Guestrin. Why lations: MT4MT. In 2018 25th Australasian Software Engineering
shoulditrustyou?:Explainingthepredictionsofanyclassifier. Conference(ASWEC),pages96–100,Nov2018.
InProceedingsofthe22ndACMSIGKDDinternationalconferenceon [130] Daniel Pesu, Zhi Quan Zhou, Jingfeng Zhen, and Dave Towey.
knowledgediscoveryanddatamining,pages1135–1144.ACM,2016. A monte carlo method for metamorphic testing of machine
[111] Youcheng Sun, Min Wu, Wenjie Ruan, Xiaowei Huang, Marta translationservices.InProceedingsofthe3rdInternationalWorkshop
Kwiatkowska, and Daniel Kroening. Concolic testing for deep onMetamorphicTesting,pages38–45.ACM,2018.
neuralnetworks.InProceedingsofthe33rdACM/IEEEInternational [131] WilliamMMcKeeman. Differentialtestingforsoftware. Digital
Conference on Automated Software Engineering, ASE 2018, pages TechnicalJournal,10(1):100–107,1998.
109–119,2018. [132] VuLe,MehrdadAfshari,andZhendongSu.Compilervalidation
[112] ChristianMurphy,GailKaiser,andMartaArias. Parameterizing via equivalence modulo inputs. In ACM SIGPLAN Notices,
Random Test Data According to Equivalence Classes. In Proc. volume49,pages216–226.ACM,2014.
ASE,RT’07,pages38–41,2007. [133] Mahdi Nejadgholi and Jinqiu Yang. A study of oracle approx-
[113] ShinNakajimaandHaiNgocBui. Datasetcoveragefortesting imationsintestingdeeplearninglibraries. InProc.ASE,pages
machinelearningcomputerprograms. In201623rdAsia-Pacific 785–796,2019.
Software Engineering Conference (APSEC), pages 297–304. IEEE, [134] AlgirdasAvizienis.Themethodologyofn-versionprogramming.
2016. Softwarefaulttolerance,3:23–46,1995.
[114] Tsong Y Chen, Shing C Cheung, and Shiu Ming Yiu. Meta- [135] SiwakornSrisakaokul,ZhengkaiWu,AngelloAstorga,Oreoluwa
morphictesting:anewapproachforgeneratingnexttestcases. Alebiosu,andTaoXie.Multiple-implementationtestingofsuper-
Technicalreport,TechnicalReportHKUST-CS98-01,Department visedlearningsoftware.InProc.AAAI-18WorkshoponEngineering
of Computer Science, Hong Kong University of Science and DependableandSecureMachineLearningSystems(EDSMLS),2018.
Technology,HongKong,1998. [136] Yi Qin, Huiyan Wang, Chang Xu, Xiaoxing Ma, and Jian Lu.
[115] ChristianMurphy,GailE.Kaiser,LifengHu,andLeonWu.Prop- Syneva: Evaluating ml programs by mirror program synthesis.
erties of machine learning applications for use in metamorphic In2018IEEEInternationalConferenceonSoftwareQuality,Reliability
testing. InSEKE,2008. andSecurity(QRS),pages171–182.IEEE,2018.
[116] JunhuaDing,XiaojunKang,andXin-HuaHu. Validatingadeep [137] Vincent Tjeng, Kai Xiao, and Russ Tedrake. Evaluating robust-
learning framework by metamorphic testing. In Proceedings of nessofneuralnetworkswithmixedintegerprogramming. arXiv
the 2Nd International Workshop on Metamorphic Testing, MET ’17, preprintarXiv:1711.07356,2017.
pages28–34,2017. [138] CynthiaDwork,MoritzHardt,ToniannPitassi,OmerReingold,
[117] Christian Murphy, Kuang Shen, and Gail Kaiser. Using JML andRichardZemel.Fairnessthroughawareness.InProceedingsof
RuntimeAssertionCheckingtoAutomateMetamorphicTesting the3rdinnovationsintheoreticalcomputerscienceconference,pages
inApplicationsWithoutTestOracles. InProc.ICST,pages436– 214–226.ACM,2012.
445.IEEEComputerSociety,2009. [139] Moritz Hardt, Eric Price, Nati Srebro, et al. Equality of oppor-
[118] XiaoyuanXie,JoshuaHo,ChristianMurphy,GailKaiser,Baowen tunity in supervised learning. In Advances in neural information
Xu,andTsongYuehChen. Applicationofmetamorphictesting processingsystems,pages3315–3323,2016.
tosupervisedclassifiers. InQualitySoftware,2009.QSIC’09.9th [140] IndreZliobaite. Fairness-awaremachinelearning:aperspective.
InternationalConferenceon,pages135–144.IEEE,2009. arXivpreprintarXiv:1708.00754,2017.

34
[141] BerneaseHerman. Thepromiseandperilofhumanevaluation [164] ShanqingCai,EricBreck,EricNielsen,MichaelSalib,andDScul-
formodelinterpretability. arXivpreprintarXiv:1711.07414,2017. ley. Tensorflow debugger: Debugging dataflow graphs for ma-
[142] DanielKang,DeeptiRaghavan,PeterBailis,andMateiZaharia. chinelearning. InProceedingsoftheReliableMachineLearningin
Model assertions for debugging machine learning. In NeurIPS theWild-NIPS2016Workshop,2016.
MLSysWorkshop,2018. [165] Manasi Vartak, Joana M F da Trindade, Samuel Madden, and
|                |     |           |       |          |         |          |       | Matei | Zaharia. | Mistique: | A   | system | to store | and query | model |
| -------------- | --- | --------- | ----- | -------- | ------- | -------- | ----- | ----- | -------- | --------- | --- | ------ | -------- | --------- | ----- |
| [143] Lianghao | Li  | and Qiang | Yang. | Lifelong | machine | learning | test. |       |          |           |     |        |          |           |       |
InProceedingsoftheWorkshoponâA˘IJBeyondtheTuringTestâA˘I˙of intermediates for model diagnosis. In Proceedings of the 2018
AAAIConferenceonArtificialIntelligence,2015. InternationalConferenceonManagementofData,pages1285–1300.
| [144] Jie | Zhang, | Ziyi Wang, | Lingming | Zhang, | Dan | Hao, Lei | Zang, | ACM,2018. |     |     |     |     |     |     |     |
| --------- | ------ | ---------- | -------- | ------ | --- | -------- | ----- | --------- | --- | --- | --- | --- | --- | --- | --- |
ShiyangCheng,andLuZhang. Predictivemutationtesting. In [166] Sanjay Krishnan and Eugene Wu. Palm: Machine learning
Proceedingsofthe25thInternationalSymposiumonSoftwareTesting explanations for iterative debugging. In Proceedings of the 2nd
|     |     |     |     |     |     |     |     | Workshop | on  | Human-In-the-Loop |     | Data | Analytics, | page | 4. ACM, |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------------- | --- | ---- | ---------- | ---- | ------- |
andAnalaysis,ISSTA2016,pages342–353,2016.
2017.
| [145] Youcheng |     | Sun, Xiaowei | Huang, | and | Daniel Kroening. |     | Testing |     |     |     |     |     |     |     |     |
| -------------- | --- | ------------ | ------ | --- | ---------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
deepneuralnetworks. arXivpreprintarXiv:1803.04792,2018. [167] BesmiraNushi,EceKamar,EricHorvitz,andDonaldKossmann.
[146] ArnaudDupuyandNancyLeveson. Anempiricalevaluationof On human intellect and machine failures: Troubleshooting in-
themc/dccoveragecriteriononthehete-2satellitesoftware. In tegrativemachinelearningsystems. InAAAI,pages1017–1025,
| DigitalAvionicsSystemsConference,2000.Proceedings.DASC.The |     |     |     |     |     |     |     | 2017. |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
AwsAlbarghouthi,LorisDâA˘Z´Antoni,andSamuelDrews.
| 19th,volume1,pages1B6–1.IEEE,2000. |     |     |     |     |                        |     |     | [168]   |                 |     |          |     |                    |     | Re-       |
| ---------------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | ------- | --------------- | --- | -------- | --- | ------------------ | --- | --------- |
|                                    |     |     |     |     |                        |     |     | pairing | decision-making |     | programs |     | under uncertainty. |     | In Inter- |
| [147] JasmineSekhonandCodyFleming. |     |     |     |     | Towardsimprovedtesting |     |     |         |                 |     |          |     |                    |     |           |
fordeeplearning. InProc.ICSE(NIERtrack),pages85–88,2019. nationalConferenceonComputerAidedVerification,pages181–200.
[148] Lei Ma, Fuyuan Zhang, Minhui Xue, Bo Li, Yang Liu, Jianjun Springer,2017.
Zhao,andYadongWang.Combinatorialtestingfordeeplearning [169] Wei Yang and Tao Xie. Telemade: A testing framework for
systems. arXivpreprintarXiv:1806.07723,2018. learning-basedmalwaredetectionsystems. InAAAIWorkshops,
2018.
[149] LeiMa,FelixJuefei-Xu,MinhuiXue,BoLi,LiLi,YangLiu,and
|         |       |         |             |     |               |         |     | [170] Tommaso |     | Dreossi, | Shromona | Ghosh, | Alberto | Sangiovanni- |     |
| ------- | ----- | ------- | ----------- | --- | ------------- | ------- | --- | ------------- | --- | -------- | -------- | ------ | ------- | ------------ | --- |
| Jianjun | Zhao. | Deepct: | Tomographic |     | combinatorial | testing | for |               |     |          |          |        |         |              |     |
InProc.SANER,pages614–618,022019. Vincentelli, and Sanjit A Seshia. Systematic testing of convo-
deeplearningsystems.
[150] Zenan Li, Xiaoxing Ma, Chang Xu, and Chun Cao. Structural lutionalneuralnetworksforautonomousdriving. arXivpreprint
coverage criteria for neural networks could be misleading. In arXiv:1708.03309,2017.
Proc.ICSE(NIERtrack),pages89–92,2019. [171] Florian Tramer, Vaggelis Atlidakis, Roxana Geambasu, Daniel
[151] Yue Jia and Mark Harman. An analysis and survey of the Hsu, Jean-Pierre Hubaux, Mathias Humbert, Ari Juels, and
|             |     |             |          |      |              |     |          | Huang       | Lin. | Fairtest:     | Discovering |           | unwarranted | associations | in  |
| ----------- | --- | ----------- | -------- | ---- | ------------ | --- | -------- | ----------- | ---- | ------------- | ----------- | --------- | ----------- | ------------ | --- |
| development |     | of mutation | testing. | IEEE | transactions | on  | software |             |      |               |             |           |             |              |     |
|             |     |             |          |      |              |     |          | data-driven |      | applications. | In          | 2017 IEEE | European    | Symposium    | on  |
engineering,37(5):649–678,2011.
SecurityandPrivacy(EuroS&P),pages401–416.IEEE,2017.
| [152] Lei | Ma, Fuyuan | Zhang, | Jiyuan | Sun, | Minhui | Xue, Bo | Li, Felix |     |     |     |     |     |     |     |     |
| --------- | ---------- | ------ | ------ | ---- | ------ | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Juefei-Xu,ChaoXie,LiLi,YangLiu,JianjunZhao,andYadong [172] YasuharuNishi,SatoshiMasuda,HidetoOgawa,andKeijiUet-
Wang. DeepMutation:MutationTestingofDeepLearningSys- suki. Atestarchitectureformachinelearningproduct. In2018
tems,2018. IEEE International Conference on Software Testing, Verification and
ValidationWorkshops(ICSTW),pages273–278.IEEE,2018.
| [153] Weijun              | Shen, | Jun Wan, | and | Zhenyu                         | Chen. | MuNN: | Mutation |              |           |       |        |     |        |            |          |
| ------------------------- | ----- | -------- | --- | ------------------------------ | ----- | ----- | -------- | ------------ | --------- | ----- | ------ | --- | ------ | ---------- | -------- |
|                           |       |          |     |                                |       |       |          | [173] Philip | S Thomas, | Bruno | Castro | da  | Silva, | Andrew     | G Barto, |
| AnalysisofNeuralNetworks. |       |          |     | In2018IEEEInternationalConfer- |       |       |          |              |           |       |        |     |        |            |          |
|                           |       |          |     |                                |       |       |          | Stephen      | Giguere,  | Yuriy | Brun,  | and | Emma   | Brunskill. | Pre-     |
enceonSoftwareQuality,ReliabilityandSecurityCompanion(QRS-
C),pages108–115.IEEE,2018. venting undesirable behavior of intelligent machines. Science,
[154] EricBreck,ShanqingCai,EricNielsen,MichaelSalib,andDScul- 366(6468):999–1004,2019.
ley. The ml test score: A rubric for ml production readiness [174] RonKohavietal. Astudyofcross-validationandbootstrapfor
andtechnicaldebtreduction. InBigData(BigData),2017IEEE accuracy estimation and model selection. In Ijcai, volume 14,
pages1137–1145.Montreal,Canada,1995.
InternationalConferenceon,pages1123–1132.IEEE,2017.
|               |       |         |         |          |              |     |        | [175] Bradley | Efron | and | Robert | J Tibshirani. | An  | introduction | to the |
| ------------- | ----- | ------- | ------- | -------- | ------------ | --- | ------ | ------------- | ----- | --- | ------ | ------------- | --- | ------------ | ------ |
| [155] Taejoon | Byun, | Vaibhav | Sharma, | Abhishek | Vijayakumar, |     | Sanjai |               |       |     |        |               |     |              |        |
Rayadurgam,andDarrenCofer. Inputprioritizationfortesting bootstrap. CRCpress,1994.
neuralnetworks. arXivpreprintarXiv:1901.03768,2019. [176] NathalieJapkowicz. Whyquestionmachinelearningevaluation
[156] Long Zhang, Xuechao Sun, Yong Li, Zhenyu Zhang, and Yang methods. In AAAI Workshop on Evaluation Methods for Machine
Feng. Anoise-sensitivity-analysis-basedtestprioritizationtech- Learning,pages6–11,2006.
niquefordeepneuralnetworks. arXivpreprintarXiv:1901.00054, [177] WeijieChen,BrandonDGallas,andWaleedAYousef. Classifier
|     |     |     |     |     |     |     |     | variability:accountingfortrainingandtesting. |     |     |     |     |     | PatternRecogni- |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --------------- | --- |
2019.
tion,45(7):2661–2671,2012.
[157] ZenanLi,XiaoxingMa,ChangXu,ChunCao,JingweiXu,and
JianLu. BoostingOperationalDNNTestingEfficiencythrough [178] Weijie Chen, Frank W Samuelson, Brandon D Gallas, Le Kang,
Conditioning. InProc.FSE,pagetoappear,2019. BerkmanSahiner,andNicholasPetrick.Ontheassessmentofthe
[158] WeiMa,MikePapadakis,AnestisTsakmalis,MaximeCordy,and addedvalueofnewpredictivebiomarkers. BMCmedicalresearch
YvesLeTraon. Testselectionfordeeplearningsystems,2019. methodology,13(1):98,2013.
[159] Ferdian Thung, Shaowei Wang, David Lo, and Lingxiao Jiang. [179] Nick Hynes, D Sculley, and Michael Terry. The data linter:
|     |           |       |         |            |          |          |     | Lightweight,automatedsanitycheckingformldatasets. |     |     |     |     |     |     | 2017. |
| --- | --------- | ----- | ------- | ---------- | -------- | -------- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- |
| An  | empirical | study | of bugs | in machine | learning | systems. |     | In                                                |     |     |     |     |     |     |       |
2012 IEEE 23rd International Symposium on Software Reliability [180] SanjayKrishnan,MichaelJFranklin,KenGoldberg,andEugene
Engineering(ISSRE),pages271–280.IEEE,2012. Wu. Boostclean: Automated error detection and repair for ma-
[160] YuhaoZhang,YifanChen,Shing-ChiCheung,YingfeiXiong,and chinelearning. arXivpreprintarXiv:1711.01299,2017.
LuZhang. Anempiricalstudyontensorflowprogrambugs. In [181] Sebastian Schelter, Dustin Lange, Philipp Schmidt, Meltem Ce-
Proceedingsofthe27thACMSIGSOFTInternationalSymposiumon likel, Felix Biessmann, and Andreas Grafberger. Automating
SoftwareTestingandAnalysis,pages129–140,2018. large-scale data quality verification. Proceedings of the VLDB
Endowment,11(12):1781–1794,2018.
| [161] S. | S. Banerjee, | S. Jha, | J. Cyriac, | Z.  | T. Kalbarczyk, | and | R.  | K.  |     |     |     |     |     |     |     |
| -------- | ------------ | ------- | ---------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Iyer. Handsoffthewheelinautonomousvehicles?:Asystems [182] Denis Baylor, Eric Breck, Heng-Tze Cheng, Noah Fiedel,
perspective on over a million miles of field data. In 2018 48th ChuanYuFoo,ZakariaHaque,SalemHaykal,MustafaIspir,Vi-
Annual IEEE/IFIP International Conference on Dependable Systems hanJain,LeventKoc,etal. Tfx:Atensorflow-basedproduction-
andNetworks(DSN),pages586–597,June2018. scalemachinelearningplatform. InProceedingsofthe23rdACM
[162] Shiqing Ma, Yingqi Liu, Wen-Chuan Lee, Xiangyu Zhang, and SIGKDDInternationalConferenceonKnowledgeDiscoveryandData
Mining,pages1387–1395.ACM,2017.
| Ananth | Grama. | MODE: | Automated |     | Neural | Network | Model |     |     |     |     |     |     |     |     |
| ------ | ------ | ----- | --------- | --- | ------ | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Debugging via State Differential Analysis and Input Selection. [183] Douglas M Hawkins. The problem of overfitting. Journal of
pages175–186,2018. chemicalinformationandcomputersciences,44(1):1–12,2004.
[163] SaikatDutta,WenxianZhang,ZixinHuang,andSasaMisailovic. [184] Heang-PingChan,BerkmanSahiner,RobertFWagner,andNich-
Storm: Program reduction for testing and debugging probabil- olas Petrick. Classifier design for computer-aided diagnosis:
isticprogrammingsystems. 2019. Effectsoffinitesamplesizeonthemeanperformanceofclassical

35
andneuralnetworkclassifiers. Medicalphysics,26(12):2654–2668, [204] NripsutaSaxena,KarenHuang,EvanDeFilippis,GoranRadan-
1999. ovic,DavidParkes,andYangLiu. Howdofairnessdefinitions
[185] BerkmanSahiner,Heang-PingChan,NicholasPetrick,RobertF fare?examiningpublicattitudestowardsalgorithmicdefinitions
Wagner,andLubomirHadjiiski. Featureselectionandclassifier offairness. arXivpreprintarXiv:1811.03654,2018.
performance in computer-aided diagnosis: The effect of finite [205] AnthonyFinkelstein,MarkHarman,AfshinMansouri,JianRen,
samplesize. Medicalphysics,27(7):1509–1522,2000. andYuanyuanZhang. Fairnessanalysisinrequirementsassign-
[186] KeinosukeFukunagaandRaymondR.Hayes. Effectsofsample ments. In16th IEEEInternationalRequirementsEngineeringCon-
sizeinclassifierdesign. IEEETransactionsonPatternAnalysis& ference,pages115–124,LosAlamitos,California,USA,September
MachineIntelligence,(8):873–885,1989. 2008.
[187] AlexejGossmann,AriaPezeshk,andBerkmanSahiner.Testdata [206] Matt J Kusner, Joshua Loftus, Chris Russell, and Ricardo Silva.
reuse for evaluation of adaptive machine learning algorithms: Counterfactual fairness. In Advances in Neural Information Pro-
over-fitting to a fixed’test’dataset and a potential solution. In cessingSystems,pages4066–4076,2017.
MedicalImaging2018:ImagePerception,ObserverPerformance,and [207] NinaGrgic-Hlaca,MuhammadBilalZafar,KrishnaPGummadi,
TechnologyAssessment,volume10577,page105770K.International and Adrian Weller. The case for process fairness in learning:
SocietyforOpticsandPhotonics,2018. Featureselectionforfairdecisionmaking.InNIPSSymposiumon
[188] Seyed-Mohsen Moosavi-Dezfooli, Alhussein Fawzi, and Pascal MachineLearningandtheLaw,Barcelona,Spain,volume8,2016.
Frossard. Deepfool:asimpleandaccuratemethodtofooldeep [208] MuhammadBilalZafar,IsabelValera,ManuelGomezRodriguez,
neuralnetworks.InProceedingsoftheIEEEConferenceonComputer andKrishnaPGummadi. Fairnessconstraints:Mechanismsfor
VisionandPatternRecognition,pages2574–2582,2016. fairclassification. arXivpreprintarXiv:1507.05259,2015.
[189] OsbertBastani,YaniIoannou,LeonidasLampropoulos,Dimitrios [209] Blossom Metevier, Stephen Giguere, Sarah Brockman, Ari
Vytiniotis, Aditya Nori, and Antonio Criminisi. Measuring Kobren,YuriyBrun,EmmaBrunskill,andPhilipThomas.Offline
neural net robustness with constraints. In Advances in neural Contextual Bandits with High Probability Fairness Guarantees.
informationprocessingsystems,pages2613–2621,2016. InProceedingsofthe33rdAnnualConferenceonNeuralInformation
[190] Nicholas Carlini and David Wagner. Towards evaluating the ProcessingSystems(NeurIPS),December2019.
robustness of neural networks. In 2017 IEEE Symposium on [210] Lihong Li, Wei Chu, John Langford, and Robert E Schapire. A
SecurityandPrivacy(SP),pages39–57.IEEE,2017. contextual-banditapproachtopersonalizednewsarticlerecom-
[191] Wenjie Ruan, Min Wu, Youcheng Sun, Xiaowei Huang, Daniel mendation. In Proceedings of the 19th international conference on
Kroening, and Marta Kwiatkowska. Global robustness evalu- Worldwideweb,pages661–670.ACM,2010.
ation of deep neural networks with provable guarantees for l0 [211] PascalMassart. Concentrationinequalitiesandmodelselection.
norm. arXivpreprintarXiv:1804.05805,2018. 2007.
[192] DivyaGopinath,GuyKatz,CorinaSPa˘sa˘reanu,andClarkBar- [212] AlekhAgarwal,AlinaBeygelzimer,MiroslavDudík,JohnLang-
rett. Deepsafe:Adata-drivenapproachforassessingrobustness ford,andHannaWallach.Areductionsapproachtofairclassific-
of neural networks. In International Symposium on Automated ation. arXivpreprintarXiv:1803.02453,2018.
TechnologyforVerificationandAnalysis,pages3–19.Springer,2018. [213] Rico Angell, Brittany Johnson, Yuriy Brun, and Alexandra
[193] RaviMangal,AdityaNori,andAlessandroOrso. Robustnessof Meliou. Themis:Automaticallytestingsoftwarefordiscrimina-
neural networks: A probabilistic and practical perspective. In tion.InProceedingsofthe201826thACMJointMeetingonEuropean
Proc.ICSE(NIERtrack),pages93–96,2019. SoftwareEngineeringConferenceandSymposiumontheFoundations
[194] SubhoSBanerjee,JamesCyriac,SaurabhJha,ZbigniewTKalbar- ofSoftwareEngineering,pages871–875.ACM,2018.
czyk,andRavishankarKIyer. Towardsabayesianapproachfor [214] Brittany Johnson, Yuriy Brun, and Alexandra Meliou. Causal
assessingfaulttoleranceofdeepneuralnetworks. InProc.DSN testing:Findingdefects’rootcauses.CoRR,abs/1809.06991,2018.
(extendedabstract),2019. [215] Sorelle A. Friedler, Chitradeep Dutta Roy, Carlos Scheidegger,
[195] Nicolas Papernot, Patrick McDaniel, Xi Wu, Somesh Jha, and andDylanSlack.AssessingtheLocalInterpretabilityofMachine
AnanthramSwami. Distillationasadefensetoadversarialper- LearningModels. CoRR,abs/1902.03501,2019.
turbationsagainstdeepneuralnetworks.In2016IEEESymposium [216] ZhiQuanZhou,LiqunSun,TsongYuehChen,andDaveTowey.
onSecurityandPrivacy(SP),pages582–597.IEEE,2016. Metamorphicrelationsforenhancingsystemunderstandingand
[196] NicolasPapernot,IanGoodfellow,RyanSheatsley,ReubenFein- use. IEEETransactionsonSoftwareEngineering,2018.
man, and Patrick McDaniel. cleverhans v1.0.0: an adversarial [217] WeijieChen,BerkmanSahiner,FrankSamuelson,AriaPezeshk,
machinelearninglibrary. arXivpreprintarXiv:1610.00768,2016. andNicholasPetrick.Calibrationofmedicaldiagnosticclassifier
[197] NicolasPapernot,FartashFaghri,NicholasCarlini,IanGoodfel- scorestotheprobabilityofdisease. Statisticalmethodsinmedical
low,ReubenFeinman,AlexeyKurakin,CihangXie,YashSharma, research,27(5):1394–1409,2018.
TomBrown,AurkoRoy,AlexanderMatyasko,VahidBehzadan, [218] ZeyuDing,YuxinWang,GuanhongWang,DanfengZhang,and
Karen Hambardzumyan, Zhishuai Zhang, Yi-Lin Juang, Zhi Li, Daniel Kifer. Detecting violations of differential privacy. In
Ryan Sheatsley, Abhibhav Garg, Jonathan Uesato, Willi Gierke, Proceedingsofthe2018ACMSIGSACConferenceonComputerand
Yinpeng Dong, David Berthelot, Paul Hendricks, Jonas Rauber, CommunicationsSecurity,pages475–489.ACM,2018.
and Rujun Long. Technical report on the cleverhans v2.1.0 [219] Benjamin Bichsel, Timon Gehr, Dana Drachsler-Cohen, Petar
adversarial examples library. arXiv preprint arXiv:1610.00768, Tsankov,andMartinVechev. Dp-finder:Findingdifferentialpri-
2018. vacyviolationsbysamplingandoptimization. InProceedingsof
[198] Saurabh Jha, Subho S Banerjee, James Cyriac, Zbigniew T Kal- the2018ACMSIGSACConferenceonComputerandCommunications
barczyk, and Ravishankar K Iyer. AVFI: Fault injection for Security,pages508–524.ACM,2018.
autonomousvehicles.In201848thAnnualIEEE/IFIPInternational [220] NeoklisPolyzotis,SudipRoy,StevenEuijongWhang,andMartin
Conference on Dependable Systems and Networks Workshops (DSN- Zinkevich. Datamanagementchallengesinproductionmachine
W),pages55–56.IEEE,2018. learning. InProceedingsofthe2017ACMInternationalConference
[199] Saurabh Jha, Timothy Tsai, Siva Hari, Michael Sullivan, Zbig- onManagementofData,pages1723–1726.ACM,2017.
niew Kalbarczyk, Stephen W Keckler, and Ravishankar K Iyer. [221] JanHendrikMetzen,TimGenewein,VolkerFischer,andBastian
Kayotee:Afaultinjection-basedsystemtoassessthesafetyand Bischoff. Ondetectingadversarialperturbations. arXivpreprint
reliability of autonomous vehicles to faults and errors. In 3rd arXiv:1702.04267,2017.
IEEEInternationalWorkshoponAutomotiveReliability&Test,2018. [222] JingyiWang,GuoliangDong,JunSun,XinyuWang,andPeixin
[200] Helge Spieker and Arnaud Gotlieb. Towards testing of deep Zhang. Adversarial sample detection for deep neural network
learning systems with training set reduction. arXiv preprint throughmodelmutationtesting. InProc.ICSE,pages1245–1256,
arXiv:1901.04169,2019. 2019.
[201] SolonBarocasandAndrewDSelbst.Bigdata’sdisparateimpact. [223] JingyiWang,JunSun,PeixinZhang,andXinyuWang.Detecting
Cal.L.Rev.,104:671,2016. adversarialsamplesfordeepneuralnetworksthroughmutation
[202] Pratik Gajane and Mykola Pechenizkiy. On formalizing fair- testing. CoRR,abs/1805.05010,2018.
ness in prediction with machine learning. arXiv preprint [224] Nicholas Carlini and David Wagner. Adversarial examples are
arXiv:1710.03184,2017. noteasilydetected:Bypassingtendetectionmethods.InProceed-
[203] SahilVermaandJuliaRubin. Fairnessdefinitionsexplained. In ingsofthe10thACMWorkshoponArtificialIntelligenceandSecurity,
InternationalWorkshoponSoftwareFairness,2018. AISec’17,pages3–14.ACM,2017.

36
[225] SanjayKrishnan,JiannanWang,EugeneWu,MichaelJFranklin, IEEE/ACM International Conference on Automated Software Engin-
andKenGoldberg.Activeclean:interactivedatacleaningforstat- eering,pages63–74.ACM,2016.
isticalmodeling. ProceedingsoftheVLDBEndowment,9(12):948– [247] RajaBenAbdessalem,AnnibalePanichella,ShivaNejati,LionelC
959,2016. Briand,andThomasStifter. Testingautonomouscarsforfeature
[226] Sanjay Krishnan, Michael J Franklin, Ken Goldberg, Jiannan interactionfailuresusingmany-objectivesearch.InProceedingsof
Wang,andEugeneWu.Activeclean:Aninteractivedatacleaning the33rdACM/IEEEInternationalConferenceonAutomatedSoftware
framework for modern machine learning. In Proceedings of the Engineering,pages143–154.ACM,2018.
2016InternationalConferenceonManagementofData,pages2117– [248] KishorePapineni,SalimRoukos,ToddWard,andWei-JingZhu.
2120.ACM,2016. Bleu:amethodforautomaticevaluationofmachinetranslation.
[227] FeiTonyLiu,KaiMingTing,andZhi-HuaZhou.Isolationforest. InProceedingsofthe40thannualmeetingonassociationforcompu-
tationallinguistics,pages311–318.AssociationforComputational
In2008EighthIEEEInternationalConferenceonDataMining,pages
| 413–422.IEEE,2008. |     |     |     |     |     |     |     | Linguistics,2002. |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
[228] SanjayKrishnanandEugeneWu. Alphaclean:automaticgener- [249] Wujie Zheng, Wenyu Wang, Dian Liu, Changrong Zhang, Qin-
ationofdatacleaningpipelines. arXivpreprintarXiv:1904.11827, song Zeng, Yuetang Deng, Wei Yang, Pinjia He, and Tao Xie.
2019. Testinguntestableneuralmachinetranslation:Anindustrialcase.
| [229] Erhard | Rahm | and Hong | Hai Do. | Data | cleaning: | Problems | and | 2018. |     |     |     |     |
| ------------ | ---- | -------- | ------- | ---- | --------- | -------- | --- | ----- | --- | --- | --- | --- |
currentapproaches. IEEEDataEng.Bull.,23(4):3–13,2000. [250] Wujie Zheng, Wenyu Wang, Dian Liu, Changrong Zhang, Qin-
|            |          |            |         |     |          |           |       | song Zeng, | Yuetang Deng, | Wei Yang, | Pinjia He, | and Tao Xie. |
| ---------- | -------- | ---------- | ------- | --- | -------- | --------- | ----- | ---------- | ------------- | --------- | ---------- | ------------ |
| [230] Nick | McClure. | TensorFlow | machine |     | learning | cookbook. | Packt |            |               |           |            |              |
PublishingLtd,2017. Testinguntestableneuralmachinetranslation:Anindustrialcase.
[231] TomSchaul,IoannisAntonoglou,andDavidSilver.Unittestsfor InICSE(postertrack),2019.
stochasticoptimization. InICLR2014,2014. [251] Wenyu Wang, Wujie Zheng, Dian Liu, Changrong Zhang, Qin-
[232] X.Sun,T.Zhou,G.Li,J.Hu,H.Yang,andB.Li. Anempirical song Zeng, Yuetang Deng, Wei Yang, Pinjia He, and Tao Xie.
Detectingfailuresofneuralmachinetranslationintheabsenceof
| studyonrealbugsformachinelearningprograms. |     |          |             |            |          | In201724th |      |                        |                                            |     |     |     |
| ------------------------------------------ | --- | -------- | ----------- | ---------- | -------- | ---------- | ---- | ---------------------- | ------------------------------------------ | --- | --- | --- |
|                                            |     |          |             |            |          |            |      | referencetranslations. | InProc.DSN(industrytrack),2019.            |     |     |     |
| Asia-Pacific                               |     | Software | Engineering | Conference | (APSEC), | pages      | 348– |                        |                                            |     |     |     |
|                                            |     |          |             |            |          |            |      | [252] JennaBurrell.    | HowthemachineâA˘ŸthinksâA˘Z´:Understanding |     |     |     |
357,2017.
|     |     |     |     |     |     |     |     | opacity in | machine learning | algorithms. | Big Data | & Society, |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------- | ----------- | -------- | ---------- |
[233] AnOrchestratedEmpiricalStudyonDeepLearningFrameworks
andLeiMaQiangHuRuitaoFengLiLiYangLiuJianjunZhao 3(1):2053951715622512,2016.
XiaohongLiPlatformsQianyuGuo,XiaofeiXie.Anorchestrated [253] Yann LeCun and Corinna Cortes. MNIST handwritten digit
| empirical | study | on  | deep learning | frameworks |     | and | platforms. | database. | 2010. |     |     |     |
| --------- | ----- | --- | ------------- | ---------- | --- | --- | ---------- | --------- | ----- | --- | --- | --- |
arXivpreprintarXiv:1811.05187,2018. [254] Han Xiao, Kashif Rasul, and Roland Vollgraf. Fashion-mnist:
|              |         |       |             |     |              |            |     | a novel image | dataset for | benchmarking | machine | learning al- |
| ------------ | ------- | ----- | ----------- | --- | ------------ | ---------- | --- | ------------- | ----------- | ------------ | ------- | ------------ |
| [234] Yu. L. | Karpov, | L. E. | Karpov, and | Yu. | G. Smetanin. | Adaptation |     |               |             |              |         |              |
ofgeneralconceptsofsoftwaretestingtoneuralnetworks. Pro- gorithms. CoRR,abs/1708.07747,2017.
grammingandComputerSoftware,44(5):324–334,Sep2018. [255] Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton. Cifar-10
[235] WeiFuandTimMenzies. Easyoverhard:Acasestudyondeep (canadianinstituteforadvancedresearch).
learning. InProc.FSE,ESEC/FSE2017,pages49–60.ACM,2017. [256] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei. Im-
[236] ZhongxinLiu,XinXia,AhmedE.Hassan,DavidLo,Zhenchang ageNet:ALarge-ScaleHierarchicalImageDatabase. InCVPR09,
2009.
| Xing,andXinyuWang. |          |               | Neural-machine-translation-basedcom- |         |        |             |          |                    |           |                                      |     |     |
| ------------------ | -------- | ------------- | ------------------------------------ | ------- | ------ | ----------- | -------- | ------------------ | --------- | ------------------------------------ | --- | --- |
|                    |          |               |                                      |         |        |             |          | [257] R.A. Fisher. | Iris Data | Set . http://archive.ics.uci.edu/ml/ |     |     |
| mit message        |          | generation:   | How                                  | far are | we? In | Proceedings | of the   |                    |           |                                      |     |     |
| 33rd               | ACM/IEEE | International | Conference                           |         | on     | Automated   | Software | datasets/iris.     |           |                                      |     |     |
Engineering,ASE2018,pages373–384.ACM,2018. [258] Yuval Netzer, Tao Wang, Adam Coates, Alessandro Bissacco,
[237] JulianDolby,AvrahamShinnar,AllisonAllain,andJennaReinen. Bo Wu, and Andrew Y Ng. Reading digits in natural images
Ariadne:Analysisformachinelearningprograms. InProceedings withunsupervisedfeaturelearning. 2011.
HoreaMureÈZ´anandMihaiOltean.
of the 2Nd ACM SIGPLAN International Workshop on Machine [259] Fruitrecognitionfromim-
Learning and Programming Languages, MAPL 2018, pages 1–10, agesusingdeeplearning.ActaUniversitatisSapientiae,Informatica,
| 2018. |     |     |     |     |     |     |     | 10:26–42,062018. |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
[238] Qixue Xiao, Kang Li, Deyue Zhang, and Weilin Xu. Security [260] Olga Belitskaya. Handwritten Letters. https://www.kaggle.
risks in deep learning implementations. In 2018 IEEE Security com/olgabelitskaya/handwritten-letters.
andPrivacyWorkshops(SPW),pages123–128.IEEE,2018. [261] BalanceScaleDataSet.http://archive.ics.uci.edu/ml/datasets/
[239] ChaseRoberts. Howtounittestmachinelearningcode,2017. balance+scale.
[240] DaweiCheng,ChunCao,ChangXu,andXiaoxingMa.Manifest- [262] Sharaf Malebary. DSRC Vehicle Communications Data
ing bugs in machine learning code: An explorative study with Set . http://archive.ics.uci.edu/ml/datasets/DSRC+Vehicle+
| mutationtesting.In2018IEEEInternationalConferenceonSoftware |     |     |     |     |     |     |     | Communications. |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- |
Quality,ReliabilityandSecurity(QRS),pages313–324.IEEE,2018. [263] Nexar.thenexardataset.https://www.getnexar.com/challenge-
| [241] XiaoyuanXie,JoshuaW.K.Ho,ChristianMurphy,GailKaiser, |     |     |     |     |     |     |     | 1/. |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Baowen Xu, and Tsong Yueh Chen. Testing and validating [264] Tsung-YiLin,MichaelMaire,SergeBelongie,JamesHays,Pietro
machine learning classifiers by metamorphic testing. J. Syst. Perona, Deva Ramanan, Piotr Dollár, and C. Lawrence Zitnick.
Softw.,84(4):544–558,April2011. Microsoft coco: Common objects in context. In David Fleet,
TomasPajdla,BerntSchiele,andTinneTuytelaars,editors,Com-
| [242] Yu-Seung | Ma, | Jeff | Offutt, and | Yong | Rae Kwon. | Mujava: | an  |     |     |     |     |     |
| -------------- | --- | ---- | ----------- | ---- | --------- | ------- | --- | --- | --- | --- | --- | --- |
automated class mutation system. Software Testing, Verification puterVision–ECCV2014,pages740–755,Cham,2014.Springer
| andReliability,15(2):97–133,2005. |     |     |     |     |     |     |     | InternationalPublishing. |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
[243] Joachim Wegener and Oliver Bühler. Evaluation of different [265] Xinlei Pan, Yurong You, Ziyan Wang, and Cewu Lu. Virtual
fitnessfunctionsfortheevolutionarytestingofanautonomous to real reinforcement learning for autonomous driving. arXiv
parkingsystem. InGeneticandEvolutionaryComputationConfer- preprintarXiv:1704.03952,2017.
ence,pages1400–1412.Springer,2004. [266] AGeiger,PLenz,CStiller,andRUrtasun.Visionmeetsrobotics:
|                |          |           |     |           |     |           |         | The kitti | dataset. The International |     | Journal of Robotics | Research, |
| -------------- | -------- | --------- | --- | --------- | --- | --------- | ------- | --------- | -------------------------- | --- | ------------------- | --------- |
| [244] Matthias | Woehrle, | Christoph |     | Gladisch, | and | Christian | Heinze- |           |                            |     |                     |           |
mann. Open questions in testing of learned computer vision 32(11):1231–1237,2013.
functions for automated driving. In International Conference on [267] Facebook research. the babi dataset. https://research.fb.com/
| ComputerSafety,Reliability,andSecurity,pages333–345.Springer, |     |     |     |     |     |     |     | downloads/babi/. |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- |
2019. [268] Andrej Karpathy, Justin Johnson, and Li Fei-Fei. Visualiz-
[245] RajaBenAbdessalem,ShivaNejati,LionelCBriand,andThomas ing and understanding recurrent networks. arXiv preprint
arXiv:1506.02078,2015.
| Stifter. | Testing | vision-based |     | control | systems | using | learnable |     |     |     |     |     |
| -------- | ------- | ------------ | --- | ------- | ------- | ----- | --------- | --- | --- | --- | --- | --- |
evolutionaryalgorithms. InProc.ICSE,pages1016–1026.IEEE, [269] Stack Exchange Data Dump . https://archive.org/details/
| 2018. |     |     |     |     |     |     |     | stackexchange. |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- |
[246] RajaBenAbdessalem,ShivaNejati,LionelCBriand,andThomas [270] SamuelRBowman,GaborAngeli,ChristopherPotts,andChris-
Stifter. Testingadvanceddriverassistancesystemsusingmulti- topherDManning.Alargeannotatedcorpusforlearningnatural
objective search and neural networks. In Proceedings of the 31st languageinference. arXivpreprintarXiv:1508.05326,2015.

37
[271] AdinaWilliams,NikitaNangia,andSamuelBowman. Abroad-
coverage challenge corpus for sentence understanding through
inference. In Proceedings of the 2018 Conference of the North
American Chapter of the Association for Computational Linguistics:
HumanLanguageTechnologies,Volume1(LongPapers),pages1112–
1122.AssociationforComputationalLinguistics,2018.
[272] Califormia dmv failure reports. https://www.dmv.ca.gov/
portal/dmv/detail/vr/autonomous/autonomousveh_ol316.
[273] Dr.HansHofmann.Statlog(germancreditdata)dataset.http://
archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data).
[274] Ron Kohav. Adult data set. http://archive.ics.uci.edu/ml/
datasets/adult.
[275] Sérgio Moro, Paulo Cortez, and Paulo Rita. A data-driven
approachtopredictthesuccessofbanktelemarketing. Decision
SupportSystems,62:22–31,2014.
[276] Executions in the united states. https://deathpenaltyinfo.org/
views-executions.
[277] AndreaDalPozzolo,OlivierCaelen,ReidAJohnson,andGian-
lucaBontempi. Calibratingprobabilitywithundersamplingfor
unbalancedclassification.InComputationalIntelligence,2015IEEE
SymposiumSerieson,pages159–166.IEEE,2015.
[278] Peter J Bickel, Eugene A Hammel, and J William O’Connell.
Sex bias in graduate admissions: Data from Berkeley. Science,
187(4175):398–404,1975.
[279] propublica. dataforthepropublicastory‘machinebias’. https:
//github.com/propublica/compas-analysis/.
[280] FMaxwellHarperandJosephAKonstan. Themovielensdata-
sets:Historyandcontext.Acmtransactionsoninteractiveintelligent
systems(tiis),5(4):19,2016.
[281] Zillow. Zillow Prize:ZillowâA˘Z´sHome ValuePrediction (Zes-
timate). https://www.kaggle.com/c/zillow-prize-1/overview.
[282] USFederalReserve.Reporttothecongressoncreditscoringand
itseffectsontheavailabilityandaffordabilityofcredit. Boardof
GovernorsoftheFederalReserveSystem,2007.
[283] Law School Admission Council. Lsac national longitudinal
barpassagestudy(nlbps). http://academic.udayton.edu/race/
03justice/legaled/Legaled04.htm.
[284] VirusTotal. Virustotal. https://www.virustotal.com/#/home/
search.
[285] contagio malware dump. http://contagiodump.blogspot.com/
2013/03/16800-clean-and-11960-malicious-files.html.
[286] Daniel Arp, Michael Spreitzenbarth, Malte Hubner, Hugo Gas-
con, Konrad Rieck, and CERT Siemens. Drebin: Effective and
explainable detection of android malware in your pocket. In
Ndss,volume14,pages23–26,2014.
[287] Alen Shapiro. UCI chess (king-rook vs. king-pawn) data
set. https://archive.ics.uci.edu/ml/datasets/Chess+%28King-
Rook+vs.+King-Pawn%29,1989.
[288] MarkHarmanandPeterO’Hearn. Fromstart-upstoscale-ups:
opportunities and open problems for static and dynamic pro-
gramanalysis. In2018IEEE18thInternationalWorkingConference
on Source Code Analysis and Manipulation (SCAM), pages 1–23.
IEEE,2018.
[289] AnthonyFinkelstein,MarkHarman,AfshinMansouri,JianRen,
andYuanyuanZhang. Asearchbasedapproachtofairnessana-
lysisinrequirementsassignmentstoaidnegotiation,mediation
and decision making. Requirements Engineering, 14(4):231–245,
2009.
[290] Jie Zhang, Lingming Zhang, Dan Hao, Meng Wang, and
LuZhang. Dopseudotestsuitesleadtoinflatedcorrelationin
measuringtesteffectiveness? InProc.ICST,pages252–263,2019.
[291] Karl Weiss, Taghi M Khoshgoftaar, and DingDing Wang. A
surveyoftransferlearning. JournalofBigdata,3(1):9,2016.
[292] Shin NAKAJIMA. Quality assurance of machine learning soft-
ware. In2018IEEE7thGlobalConferenceonConsumerElectronics
(GCCE),pages601–604.IEEE,2018.