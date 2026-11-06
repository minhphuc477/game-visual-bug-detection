---
title: "Survey of Video Game Testing ACM CSUR"
author: "Politowski"
year: "2021"
source_file: "Politowski_2021_Survey_of_Video_Game_Testing_ACM_CSUR.pdf"
source_sha256: "bf143a45698b2f293240e7c5f81d2ec19badfdf91a2be09e3921f752b992c13e"
converted_at: "2026-11-06T15:44:22.853842+00:00"
markitdown_version: "0.1.9"
char_count: 94980
---
1202
raM
11
]ES.sc[
1v13460.3012:viXra
A Survey of Video Game Testing
Cristiano Politowski Fabio Petrillo Yann-Gae¨l Gue´he´neuc
Concordia University Universite´ du Que´bec a` Chicoutimi Concordia University
Montreal, QC, Canada Chicoutimi, QC, Canada Montreal, QC, Canada
c polito@encs.concordia.ca fabio@petrillo.com yann-gael.gueheneuc@concordia.ca
Abstract—Video-game projects are notorious for having day- Thus,likewithanypieceofsoftware,todeliverhigh-quality
one bugs, no matter how big their budget or team size. The games, game developers must test their games rigorously
qualityofagameisessentialforitssuccess.Thisqualitycouldbe
duringtheirdevelopment.Intraditionalsoftwaredevelopment,
assessedandensuredthroughtesting.However,tothebestofour
tests are considered essential (unit, component, integration,
knowledge,littleisknownaboutvideo-gametesting.Inthispaper,
we want to understand how game developers perform game or end-to-end tests), and so is their automation [1]. Yet, to
testing.Weinvestigate, througha survey, theacademic andgray the best of our knowledge,there exists no comprehensiveand
literaturetoidentifyandreportonexistingtestingprocessesand systematic report on how game developers test (or not) their
how they could automate them. We found that game developers
games.Thus,weaskthequestion:“Whatisthetestingprocess
rely,almostexclusively,uponmanualplay-testingandthetesters’ in game development?”
intrinsic knowledge. We conclude that current testing processes
fall short because of their lack of automation, which seems to To answer this question, we study the field of testing in
be the natural next step to improve the quality of games while game development by surveying the processes, techniques,
maintainingcosts. However, thecurrent game-testing techniques gaps,concerns,andpoint-of-viewsusingtwodifferentsources:
may not generalize to different types of games.
(1) the academic literature (journal and conference papers,
books, and theses) and (2) the gray literature (presentations
I. INTRODUCTION
in well-knownconferences,blogposts fromgamedevelopers,
In the game industry, the first impression is of utmost and video-game postmortems).
importance; therefore, only high-quality games can expect to We report that manual game-play testing, a form of end-
succeed. In December of 2020, the game “Cyberpunk2077”1 to-end testing also called play-testing, is the primary testing
was released after seven years of development2, hundreds of technique used by game developers. Automate play-testing
millions of dollars3, multiple delays4, and high expectations. sessionsisdifficult,whichleadtodevelopershiringspecialised
Upon release, it immediately received strong criticism for testers to manually play-test their games, resulting in a game
its “buggy state” and, no long after, it was even removed industrythatreliesalmostexclusivelyuponmanuallabourand
from the PlayStation Store5 because it was not delivering the human expertise to test their games.
expectedexperiencetoitsusers,causingrevenuelossandother We conclude that the automation of video-game testing
collateral effects, like loss of prestige and good-will for the requiresresearchandtoolsthatgamedeveloperscan integrate
company CD Projekt Red6. intotheirtestingprocesses.Therefore,allowingthemtocreate
Many observers in industry and academia ponder how a more systematic, repeatable, and reliable games, while game
companywithareputationforqualitygames7,likeCDProjekt
testers focus on player-centered aspects of the games, like
Red, with no shortage of money, time, skill, and experience game play or aesthetics.
couldreleasea gamewith suchpoorquality.These observers, The paper is structured as follows: Section II describes the
aswellaspersonnelfromthecompanyitself,blamethescope, method we used. Section III shows the results of our analysis
the management, and the lack of testing8 for the poor quality of the academic literature. Section IV shows the results of
ofthegame.AccordingtothecompanyCEO,MarcinIwin´ski, our study of the gray literature. Section V discusses our
“Every change and improvement needed to be tested, and as results. Section VI describes threats to validity of our study.
it turned out, our testing did not show a big part of the issues Section VII concludes the paper with future work.
you experienced while playing the game”9.
II. SURVEY METHOD
1https://www.cyberpunk.net/ca/en/
Our approach is based on categories of reliability of the
2https://www.youtube.com/watch?v=cGmWwFpNIHg
literature[2],withwhiteliterature,peer-reviewedpapers,isthe
3http://bit.ly/2M41lHG
4http://bit.ly/39M5mbV most reliable, followed by three gray literature tiers: first-tier,
5https://www.playstation.com/en-ca/cyberpunk-2077-refunds/ books,bookschapters,governmentreports;secondtier,annual
6https://en.cdprojektred.com/ reports,newsarticles,videos,presentations,Wikiarticles;and,
7Thepreviousgamereleasedbythesamecompany,“TheWitcher3”,was
third tier, blogs, emails, tweets, letters.
considered agreatsuccess:http://bit.ly/3ipMHqs.
8http://bloom.bg/2LNtNhc Weconsidered:(1)academicliterature,journal,conference,
9http://bit.ly/39N8epd and workshop papers, books and theses, and (2) gray litera-

ture,presentationsinwell-knownconferences,blogpostsfrom – We searched for talks about testing in game-developer
game developers, and video-game postmortems. We did not conferences. We read/watched presentations and sum-
observeanyduplicationorextension(journalpapersextending marized the points related to game testing.
explicitlyconferencepaperswithnewmaterial).Weperformed • Media specialized in game development
the search for academic and gray literature on 2019/06/21.
– WesearchedforarticlesabouttestingonWebsitesand
blogs about game development. We selected the most
A. Academic Literature
relevant and summarized the main points.
We used two sources of academic documents: Scopus10 We also searched specialized forums. We searched Stack-
and Engineering Village11. The query was: (test OR testing Exchange13 for questions with tags “testing”14 and found 79
OR verification OR validation OR qa OR ”quality assurance” questions but without relevant answers, about hardware com-
OR debugging OR prototyping) AND (game OR video-game patibility (11 questions), game-play balancing (10 questions),
OR ”video game” OR ”digital game”) AND NOT (gamifica- and network testing (8 questions).
tion OR ”serious games” OR education OR teaching) AND Finally, we queried Google Search: test* AND game
LIMIT-TO(LANGUAGE,”English”).Afterthe inclusionand AND development -job -course -company and
exclusion criteria, the query yields 327 papers. used the five first result pages. We found 100 Web sites
The inclusion and exclusion selection criteria were: (blogs, forums, companies, papers, and courses) but they
• Inclusion criteria: were irrelevant and–or did not add new information.
– Papers must be about video game development; III. RESULTS -ACADEMIC LITERATURE
– Papers must be about or discuss testing;
A. Game testing and its particularities
• Exclusion criteria:
The game industry has different characteristics compared
– Papers not written in English;
to traditional software development. It is a junction between
– Papers about gamification;
design, business and software engineering [4]. In traditional
– Papers about serious games;
software development, the product’s objective is to provide
– Papers about using games for educational purposes;
a service while the game’s goal is the entertainment [5].
– Papers about using games for medical purposes.
Traditional software products, called “productivity applica-
We did not set and use any quality criteria.
tions”, are designed to accomplish one or more tasks as
a) Filtering: Title Reading: We read the title of each of necessary elements of a non-entertainment endeavour (e.g.
327 papers and divided them int game development and–or business endeavours) [6]. On the other hand, a game is more
testing. After that filtering, we obtained 71 papers. than software as it must enthrall the user with its mechanics,
b) Filtering: Abstract Reading: We read the abstracts of despite its foundation relying on a well-written software [7].
the 71 papers and rejected or accepted them based on our Finally, game software aims to provide an experience rather
criteria. We kept 38 papers. than say productivity, and these cause divergences on the
c) Coding: Full Reading: We read all 38 papers, taking adopted practices [8].
notes of the relevant subjects and references according to Game developmentconsists of iteration of experimentation
the grounded theory technique and selected the most relevant while embracing the changes as the key for a good game de-
papers for the snowballing, 8 papers. signistheconstantexperimentationofnewfeaturesinsteadof
d) Snowballing: We performed a complete snowballing stick with a set of requirements[9]. Since game development
process, backwardsand forward,on the 8 papers,re-checking requirements are continually changing (volatile and mutable
the title and abstract of each paper again to verify the paper’s [10]), developerspreferto embracethe change,as said by the
relevance. The final dataset12 included 96 papers. developer:“Why should we bother with strict decisions when
we can make a prototype in two hours to test things out?”
B. Gray Literature [11].Therefore,gamedevelopmentemphasizesevaluatinguser
experiences and using the feedback to drive design iterations
For the gray literature, we used the same inclusion and
[8], although some authors report a balance between planned
exclusion criteria than the academic papers. We used three
activities and improvised ones [12].
main sources of gray literature:
Some games have a particular way of profiting and, there-
• Postmortems of video-game projects
fore, different ways to manage their development life-cycle.
– We used a database of postmortems [3] and kept only For example, mobile games are not designed to be sold once,
the ones related to testing. We analyzed each one of but to keep changing (balancing the gameplay) and evolving
them and extracted the root cause of the problems.
(adding new features) constantly depending on the audience
• Conferences on game development needs and behaviour [13]. Regarding the quality, software
quality can be determined by how well the product performs
10www.scopus.com
11www.engineeringvillage.com 13gamedev.stackexchange.com
12Thedatasetisavailableathttps://github.com/game-dev-database/game-testing. 14https://gamedev.stackexchange.com/questions/tagged/testing

its intended functions. For game software, this includes the Finally,gamedevelopersfinditdifficulttoreusetheircode,
quality of the player’s experience plus how well the game have less pressure on evolving their systems’ architecture,
features are implemented [14]. and are less able to overview the requirements of a project
|         |          |          |     |         |      |                  |     | correctly. | Furthermore, |     | they report | more | difficulties |     | in per- |
| ------- | -------- | -------- | --- | ------- | ---- | ---------------- | --- | ---------- | ------------ | --- | ----------- | ---- | ------------ | --- | ------- |
| 1) Game | testers: | Gameplay |     | testers | have | the heavy-dutyof |     |            |              |     |             |      |              |     |         |
finding bugs and any other abnormality in the game. Game forming automated unit tests than non-game developers [26].
|                |      |      |         |     |           |           |     | More particularities |     | in  | game testing | are | described | by  | Santos, |
| -------------- | ---- | ---- | ------- | --- | --------- | --------- | --- | -------------------- | --- | --- | ------------ | --- | --------- | --- | ------- |
| testers should | test | game | quality | by  | verifying | gameplay, |     | logi-                |     |     |              |     |           |     |         |
cal consistency, observability, progressive thinking, reasoning Magalhaes,Capretz,etal.[10],likerequirementsanalysis,test
ability, and exhaustively testing features, game strategy, and planning, test design and execution.
functionality [15]. Therefore, testers should understand the 3) Test automation: There are significant differences be-
principlesandthe characteristicsbehindgamesandespecially tween games and non-gamesregarding game developers’ dif-
understand the game development context [10]. ficultiestowriteautomatedtests[26].Thereislessautomation
Despite their usefulness, testers are often treated as less in game testing, for different reasons shown in Table I.
importantcomparedtothedevelopersandgamedesigners[5],
| [16]. Often, | they | work | in non-desirable |     |     | conditions | [16], | and |     |     |     |     |     |     |     |
| ------------ | ---- | ---- | ---------------- | --- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
TABLEI
the setup of game testing is cumbersome for the developer. DIFFICULTIESINTESTAUTOMATIONFORGAMES.
| Testing | changes | will take | longer | as  | the programmer |     | needs | to  |     |     |     |     |     |     |     |
| ------- | ------- | --------- | ------ | --- | -------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
setuptheproperconditionswithinthegameworldtoexercise Difficulty Description
thatcodepath[17].Findingbugsisrepetitive,time-consuming Coupling Itishardtowritetheautomationgiventhecouplingbetween
and challenging for human testers, which could cause testers theuserinterface (UI)andgamemechanics [13],[19],[25].
| to overlook | defects | [18]. |     |     |     |     |     |       |        |          |             |     |          |       |              |
| ----------- | ------- | ----- | --- | --- | --- | --- | --- | ----- | ------ | -------- | ----------- | --- | -------- | ----- | ------------ |
|             |         |       |     |     |     |     |     | Scope | Trying | to cover | all “paths” | of  | the game | could | restrict the |
gamedesign[10],[19],sometimesseenascontrarytoagility
| 2) Game | testing: | Testing |     | games | have | some | different | as- |            |     |               |            |       |       |            |
| ------- | -------- | ------- | --- | ----- | ---- | ---- | --------- | --- | ---------- | --- | ------------- | ---------- | ----- | ----- | ---------- |
|         |          |         |     |       |      |      |           |     | preventing |     | the fast pace | of changes | [18], | [25]. | Developers |
pects compared to testing traditional software [19]. Video believethattheycannotcovereverything,duethelargesearch
gamesarenotconsideredproductivitysoftware;theyaretested spaceofpossiblegamestates[25],thereforetheeffortisnot
worth[18].
| less intensely | on       | accuracy | and        | more    | intensely   | on          | the         | overall    |                              |     |                          |       |                          |     |             |
| -------------- | -------- | -------- | ---------- | ------- | ----------- | ----------- | ----------- | ---------- | ---------------------------- | --- | ------------------------ | ----- | ------------------------ | --- | ----------- |
|                |          |          |            |         |             |             |             | Randomness | Thenon-determinism           |     | on                       | games | (multi-threading,        |     | distributed |
| experience     | [20].    | This     | type of    | testing | is referred |             | to gameplay |            |                              |     |                          |       |                          |     |             |
|                |          |          |            |         |             |             |             |            | computing,                   |     | artificial intelligence, |       | and randomness)          |     | make it     |
| testing,       | which is | the way  | developers |         | assess      | the quality |             | of the     |                              |     |                          |       |                          |     |             |
|                |          |          |            |         |             |             |             |            | hardtohardtoassertthecorrect |     |                          |       | behavior[18],[19].Inthis |     |             |
game [21] and it is preferredin detrimentof other techniques caseisa“emergent software” asits randomness isafeature
|            |       |       |          |     |          |     |          |     | and | players’   | surprise is | desirable | [9]. You  | need | access to |
| ---------- | ----- | ----- | -------- | --- | -------- | --- | -------- | --- | --- | ---------- | ----------- | --------- | --------- | ---- | --------- |
| [19], [22] | as it | gives | the team | the | feedback | in  | the form | of  |     |            |             |           |           |      |           |
|            |       |       |          |     |          |     |          |     | the | randomness | part of     | the game, | otherwise | you  | may never |
“enjoymentheuristics” [23]. Accordingly,test managementis reproduce thebugproperly[14].
| more ad-hoc     | in          | game   | development, |       | relying        | heavily    |          | on the  |                                                    |            |                 |                |               |             |            |
| --------------- | ----------- | ------ | ------------ | ----- | -------------- | ---------- | -------- | ------- | -------------------------------------------------- | ---------- | --------------- | -------------- | ------------- | ----------- | ---------- |
|                 |             |        |              |       |                |            |          | Changes | It is                                              | difficult  | to keep         | the automation | as            | the game    | design     |
| usability       | tests with  | users, | not          | on    | the documented |            | test     | plans   |                                                    |            |                 |                |               |             |            |
|                 |             |        |              |       |                |            |          |         | change                                             | too        | often, even     | core mechanics |               | [10], [27], | making     |
|                 |             |        |              |       |                |            |          |         | its documentation                                  |            | becoming        | obsolete       | too           | fast [9].   | Also, the  |
| or predefined   | test        | cases  | [24].        |       |                |            |          |         |                                                    |            |                 |                |               |             |            |
|                 |             |        |              |       |                |            |          |         | source                                             | code       | is temporary    | and            | highly likely | to          | change as  |
| The game        | development |        | process      |       | involves       | iterations |          | around  |                                                    |            |                 |                |               |             |            |
|                 |             |        |              |       |                |            |          |         | development                                        |            | progresses[18]. |                |               |             |            |
| experiments,and |             | it is  | expected     | that  | the game’s     | code       | becomes  |         |                                                    |            |                 |                |               |             |            |
|                 |             |        |              |       |                |            |          | Cost    | Asoftwareengineeringismoreexpensivecomparedtogame- |            |                 |                |               |             |            |
| “throwable”     | [13],       | making | the          | tests | obsolete.      | This       | practice | is      |                                                    |            |                 |                |               |             |            |
|                 |             |        |              |       |                |            |          |         | play                                               | testers    | [18], [19].     | The cost       | of hiring     | new         | developers |
|                 |             |        |              |       |                |            |          |         | to write                                           | additional | lines           | of code        | into a        | game        | to support |
| not unusual     | as the      | game   | industry     | is    | famous         | for        | creating | new     |                                                    |            |                 |                |               |             |            |
automation(aswellaswritingscriptsandothertestutilities,
codewitheachnewtitle.Evenwhenthe“same”engineorcore
interfaces, andsoon)canbemorethanitwouldcosttopay
| code is | reused for | a new | game, | that | engine | or  | code is | often |       |         |             |        |         |            |         |
| ------- | ---------- | ----- | ----- | ---- | ------ | --- | ------- | ----- | ----- | ------- | ----------- | ------ | ------- | ---------- | ------- |
|         |            |       |       |      |        |     |         |       | human | testers | [14]. Also, | manual | re-test | after code | changes |
modified, repaired, and improved upon [14]. These iterations (newbuild)areexpensive duetoreproducibility issues[18].
leadtochangesinhowthegamewasconceptualized,designed Time Programmers usually don’t test their games. They usually
|           |             |              |     |     |          |          |          |     | don’t | have  | time to do     | so [14] | or they believe    | that | writing |
| --------- | ----------- | ------------ | --- | --- | -------- | -------- | -------- | --- | ----- | ----- | -------------- | ------- | ------------------ | ---- | ------- |
| and coded | [12].       | Late changes |     | are | allowed  | and even | expected |     |       |       |                |         |                    |      |         |
|           |             |              |     |     |          |          |          |     | tests | takes | time away from | the     | actual development |      | process |
| [24] with | playtesting | inspiring    |     | new | features | [25].    |          |     |       |       |                |         |                    |      |         |
[18].
| Gameshave | differenttypesof |     |     | requirements[6]. |     |     | Traditional |            |           |     |            |              |      |        |          |
| --------- | ---------------- | --- | --- | ---------------- | --- | --- | ----------- | ---------- | --------- | --- | ---------- | ------------ | ---- | ------ | -------- |
|           |                  |     |     |                  |     |     |             | Fun-factor | Capturing | the | “fun” with | an automated | test | is not | possible |
test planning methods cannot satisfy the fun (entertainment [18]asgametestingishumancentricandhumanbehavioris
and excitement) requirements [13]. Also, measures related difficulttoautomate[10].Also,itishardtoautomategames
wheremanyeventsarehappeningsimultaneously.Therefore,
| to fun, | entertainment, |     | gameplay |     | and other | user | experience |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | -------- | --- | --------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
automation isusedmainlyinsimpletests[10].
| aspects | could be | too | complex | to plan | and | evaluate | software |      |                                                    |     |     |     |     |     |     |
| ------- | -------- | --- | ------- | ------- | --- | -------- | -------- | ---- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- |
|         |          |     |         |         |     |          |          | Code | Automatedtestingcodemaynotbebug-free,norbereusable |     |     |     |     |     |     |
testing [10]. The main difference between testing a game and from one game to another, or from one platform to another
regular software lies in the game requirements and the scope [18]. Game developers have more difficulties than other
definitions of the project [10]. developers whenreusingcode[26].
Testingsessionsarebasedmostlyonblack-boxtestingwith
human testers [15]. Despite the differences, testing in games Despitethedifficultiesinapplyingautomatingtestsingame
ismandatory,asstatedbythisdeveloper:“Ifatestercomesto development,thereare somebenefitsofdoingit, forexample,
say that this does not work, there is not fun in it, you really reproducibility, quality, fewer bugs, better test focus, game
cannot leave that in the game, you have to fix it” [11]. “ stability, and fewer human testers [18].

B. Game testing concerns d) Definedesignpatternsfor gamedevelopment: As the
As the workload for gameplay testing is tiresome [16], GoFpatterns[33]arespecific forOOsystems, gamedevelop-
mentpatternsare goodpractices specific for gamegenres[9].
the testers often got motion sickness by constant re-playing
the games [19]. In this sense, automation can reduce the Aside from game design patterns, which other patterns, more
relatedtosourcecodeandmoresimilartotraditionalsoftware,
burden on both developers and human testers, however it
could be applied when building a game? How the quality of
also can introduce cost to game production, and it required
programmers with a specialized focus on automated testing code in games influence the game’s functional requirements?
e) Create an universal game design language: The cre-
[18]. At the same time, the lack of test automation in game
ation of a “universal game design language” could allow the
development “hurts” the bug fixing process as it becomes
game developers reuse/extend a feature from game to game
harder to reproduce the steps [19].
[9].Candevelopersinterchangeablydevelopagameregardless
Game developers overlook the SE practices. On testing,
of the tools (game engine)?
this happens because low-level testing is neglected for the
sake of gameplay testing [19]. Regarding automated game IV. RESULTS -GRAY LITERATURE
testing, few studios use test automation alleging causes like
A. Postmortems of video-game projects
development time, staff size, or little knowledge about these
We used a database of postmortemproblemsprovidedby a
tools[22].Usabilitytestsandframeworksarealsousedwithin
previouswork[34].Amongalltheproblems,only4%(50out
game development, but they are tailored specifically for the
of1,035)areabouttesting.Thelistoftest-relatedpostmortems
game domain [28]. Even pair and test-first programming,two
is available on-line15, whose problems Table II summarizes.
practiceswellestablishedintraditionalsoftwaredevelopment,
were not largely used by game companies [29].
In game development, software working according to its TABLEII
SUMMARYOFTHETESTINGPROBLEMSFOUNDINTHEPOSTMORTEMS.
functional requirements is not enough; the game must be
appealing for the user [30]. This appeal involves balancing Problem N
the gameplay, which is unique in game development and a
Insufficient testing 22
challenge for the developers [6]. Processandtestingplans issues 18
Creatingvideogamesisacomplextask.Thegameindustry Specificproject requirements 13
Feedback 7
is on the edge of technical complexity. On top of that, the
Scope 6
field of game development is hard to assess considering the Reproducibility 2
restrictions of proprietary code [9]. Logging 2
Noin-houseQA 2
C. Game testing challenges Combinatorial explosion 1
Bugfixing 1
a) Add game testing sooner to development pipeline:
Game studios start testing for User Experience of games
Insufficienttesting is the most common problem quoted by
too late in the development life cycle, sometimes as late as
game developers. Eight postmortems cite lack of test as a
beta, which means that most of the feedback obtained from
problem (PM#4, PM#19, PM#33, PM#35, PM#38, PM#43,
the tests is unlikely to have an impact on the final game
PM#45, PM#49). Five mention that more testing was need in
[31]. Keygameconceptsshouldalso be testing beforerelease
the early phases of the development (PM#5, PM#6, PM#21,
so the reactions of the players can be verified [32]. Every
PM#22, PM#39) while two others in later phases (PM#7,
aspectofagameshouldbetestedduringthedevelopmentand
PM#11). Lack of unit testing (PM#17) and regression testing
production phases. The most important aspect of testing for
(PM#18)werealsocitedaswellasbetatesting(PM#39),most
gamedevelopersistointegratetestingaspartoftheproduction
ofitbecauseoftimeconstraints(PM#9,PM#24,PM#26),and
phase to improve efficiency. To ensure the delivery of quality
play-testingingeneral(PM#34).Finally,developersalsomen-
gamestothemarket,developersmustconsiderdifferenttesting
tioned problemsregardingtesting-tools setup, like continuous
options during the production phase [15].
integration, testing systems, and automation (PM#6, PM#28).
b) Instrument the game with meaningfullogs and create
Lackofunittestingandwrongdecisionsforthetestingplan
tools to visualize the events: Combine playtesting with play
are well exemplified by the following quote:
analytics and advanced visualizations (e.g., using synthetic,
“In the end, we slipped to the side of not having as
procedurally generated game worlds to visualize game play
many unit tests as we would have liked. (...) By the
data sets and temporal relationships) [30].
time we noticed those problems and wanted to start
c) Addautomatingtestingsuitableforgamedevelopment
adding tests, it was too late because some of that
domain: The use of manual testing and the challenges with
coderelied onnon-unittest friendly APIslike UIKit
automated testing in game systems highlight the need for a
or Box2d. (...) We even shipped with a few off edge
new set of methodologies to ease the developers’ ability to
cases that we knew were buggy but we didn’t dare
identifymalfunctionsandtoenableautomatictestingactivities
fix weeks before submission.” – Postmortem PM#17
forgames.Studiesshouldinvestigatenewrecord–replaytools,
automated test-data generators, etc. [26]. 15https://github.com/game-dev-database/game-testing

The benefits of automated tests are illustrated by: stack, and all the item abilities will affect [him] in
“With automated tests QA could have focused on some way, so there were so many variables to keep
other tasks and we would faster know if a certain track of that all the testing in the world couldn’t
map or feature were broken when running the au- have prepared us for launch. (...) In order to fully
tomated tests” while “Without automated testing, test all the variableswe had in place, it would have
every bug fix had a greater potential of introducing taken hundreds of testers several days of extensive
hidden bugs into the game, and this cost us a lot of play time to fully debug this [game] – there were
time when regression issues weren’t identified until bugsthatactuallytook 100,000+peoplefour weeks
long after they were introduced.” – Postmortems to find due to how buried and rare some of them
PM#6 and PM#28 were.” – Postmortem PM#15
Specific projects’ requirements were heavily stressed by
B. Conferences on game development
game developers. Support for multiple platforms and its dif-
We searched for talks in conferences specialized in game
ficulties were the requirements mentioned the most (PM#5,
PM#12, PM#18, PM#30, PM#31, PM#36). Testing multi- development like GDC16 and Digital Dragons17. Table III
shows the most relevant talks about game testing.
player and–or online gamesis difficultfor developers(PM#2,
PM#46, PM#47, PM#49, PM#50). Other issues related to
outdated video drivers (PM#30) and stress test (PM#42). TABLEIII
Game developers also cited problems with test plans and
CONFERENCESONGAMEDEVELOPMENT.
processes. Game developers complained that QA can block a
Title Url
development team (PM#3, PM#40). The test strategies were
CASE-1 Smart Bots for Better Games: Rein- https://bit.ly/2Hi5lyJ
considered problems in many games (PM#1, PM#2, PM#19,
forcementLearninginProduction
PM#29, PM#37, PM#45). Other problems were the overes- CASE-2 Automated Testing and Profiling for https://bit.ly/37hf3w1
timation/underestimation of the time and effort necessary to ’CallofDuty’
CASE-3 Automated Testing and Instant Re- https://bit.ly/2vuuSlS
test(PM#2,PM#17,PM#27,PM#41,PM#44,PM#47,PM#49,
playsinRetroCityRampage
PM#50).Estimationissuesregardingtheinfrastructure,mostly CASE-4 It’sRainingNewContent:Successful https://bit.ly/31KNk5I
hardware concerns, were also mentioned by game developers RapidTestIterations
CASE-5 AutomatedTestingofGameplayFea- https://bit.ly/2ONBFh8
(PM#6, PM#8, PM#20).
turesinSeaofThieves
Problems with poor feedback and testing sessions were
mentioned for several game projects (PM#9, PM#11, PM#16,
1) [CASE-1] Smart Bots for Better Games: Reinforcement
PM#22, PM#30, PM#39, PM#45), e.g.:
Learning in Production: Ubisoft18 showcased their use of
“Most beta testers are young people who have a
ReinforcementLearning(RL)inproductiontotestgameswith
lot of time on their hands; that’s great for finding
botsthat can evolvewhile playing.RL hasbeen applied/stud-
bugs, but it can also be a problem because some
ied mainly in two areas of game development: improving AI
of them lack perspective.” and “I mean the kind of
behaviorand creating test assistants. The formergot attention
testing that finds bugs, not suggests new features.”
when the OpenAI team trained bots on Dota 2 (OpenAI
Postmortems PM#12 and # PM#46 Five)19. The latter approach uses agents to test games, which
Some game projects have too large a scope to be properly has been used by Ubisoft in Triple-A games like Far Cry:
tested.Scopeisanissuealsocitedbygamedevelopers(PM#6, New Dawn (2019), which has an open world, and Rainbow
PM#14, PM#23, PM#26, PM#38, PM#41) Six Siege (2015), which is multiplayer.
Other problems related to the reproducibility of the bugs The author also described three techniques to train agents
(PM#13, PM#25) and bug-fixing (PM#3), logging prob- using RL: learning from pixels [35], [36], from states [37],
lems (PM#25, PM#30), lack of in-house QA team (PM#28, [38], and from simulation [39].
PM#40), and the complexity of game mechanics (PM#15). 2) [CASE-2] Automated Testing and Profiling for Call of
The reproducibility problem is exemplified by: Duty: Electronic Arts (EA) is a large company that develops
“Thearenabugwassubtle,althoughtheresultswere and publishes games. EA has many studios working on dif-
not, and was not easy to reproduce. We were dimly ferent games. The talk was about the franchise Call of Duty,
aware that the bug existed, but its frequency was which receives a new iteration almost every year since 2003.
unclear. Because of the difficulty in reproducing it, The team developed a tool called Compass, designed to
the scope of testing the rest of the game and the keeptrackofbuilds/testing.TheteamworkflowwithCompass
smallsize ofthe QA team,the bug wasnotproperly consisted of five different checks during the development of
identified.” – Postmortem PM#13 the game: continuous integration (CI) module, “all maps”
The problems with game scope, game mechanics, and in-
sufficient testing are well exemplified by the following quote:
16https://www.gdconf.com/
17http://digitaldragons.pl/
“[the game] had 100 items and five playable char- 18https://ubisoft.com
acters. 70 percent of the items in [the character] 19https://openai.com/projects/five/

testing, nightly tests, and maintenance. The tool work with search Gamasutra for anything related to game and testing
the help of game-play testing. For example, when testers find since 2010: test* AND game site:gamasutra.com
a place with a low frame-rate, the tool record this location, after:2010. From the results, we retrieved the first 50
adds more characters and collects metrics automatically. articles, excluded non-relevant articles from their titles and
3) [CASE-3] Automated Testing and Instant Replays in their contents, and retained the four articles in Table IV.
| Retro City | Rampage: |     | The author | used | automated |     | testing |     |     |     |     |     |     |     |     |
| ---------- | -------- | --- | ---------- | ---- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
techniques to test his indie game, with a small scope. His TABLEIV
solution was to record the inputs, in log files, and have the GAMASUTRAARTICLES
| enginere-play |     | them.It allowed |     | him to | track | downbugsusing |     |     |       |     |     |     |     |     |     |
| ------------- | --- | --------------- | --- | ------ | ----- | ------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|               |     |                 |     |        |       |               |     | #   | Title |     |     |     | URL |     |     |
asimpledifftoolontheoutputfiles.Advantagesofthisinput–
recordapproachare:automatedQA,easytodealwithmultiple MEDIA-1 TestingforGameDevelopment https://ubm.io/35jhuNl
|            |     |                |      |           |     |       |     | MEDIA-2 | Differences | between |     | Software | https://ubm.io/37ygEOj |     |     |
| ---------- | --- | -------------- | ---- | --------- | --- | ----- | --- | ------- | ----------- | ------- | --- | -------- | ---------------------- | --- | --- |
| platforms, | and | easy to narrow | down | game-play |     | bugs. |     |         |             |         |     |          |                        |     |     |
TestingandGameTesting
The author also suggested that the game code should be MEDIA-3 Unittestinginvideogames https://ubm.io/2ZOtZPR
deterministic; the same inputs should yield the same outputs. MEDIA-4 Automated Testing: Building A https://ubm.io/2SWY2U2
|            |     |              |          |     |           |                |     |     | Flexible | GameSolver |     |     |     |     |     |
| ---------- | --- | ------------ | -------- | --- | --------- | -------------- | --- | --- | -------- | ---------- | --- | --- | --- | --- | --- |
| Otherwise, | the | input–record | approach |     | will deal | with different |     |     |          |            |     |     |     |     |     |
outputseverytime,defeatingitspurpose.Asidefrombuilding
a deterministic game engine, other things to consider are: 1) [MEDIA-1] Testing for Game Development: In this
initializing all variables, creating own (controllable) random article, the author argues that video games, aside of being
method, and splitting each instance that controls different big and complex,are also software with emergentbehavior20,
modules of the game. Finally, especially for multi-platform i.e.,unpredictable.Moreover,thecomplexgamelogicand the
games, floating-point computations may differ, which might unpredictabilityofthe usersmakeit difficulttoguaranteethat
| yield different |     | behaviors. |     |     |     |     |     | games will | “react | gracefully”. |     |     |     |     |     |
| --------------- | --- | ---------- | --- | --- | --- | --- | --- | ---------- | ------ | ------------ | --- | --- | --- | --- | --- |
4) [CASE-4] It’s Raining New Content: Successful Rapid Aside of these difficulties, testing games benefits develop-
Test Iterations: Riot is the company developing League of ers, e.g., by generating knowledge about the games. Testing
Legends, which had 11 million daily players and 5 million is important because a game with bugs is not fun to play.
concurrentplayersatthetimeofthetalk.Thus,onebug,evena Yet, automatedtesting is hardto achieveand doesnotreplace
smallglitch,couldaffectmillions.Thus,theycreatedaprocess
|     |     |     |     |     |     |     |     | manual testing, |     | but removes | repetitive |     | (regression) | testing. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ----------- | ---------- | --- | ------------ | -------- | --- |
with which testing is carried carefully in different steps to TheauthoralsostatesthatTDD,acommonwaytodevelop
| detect/prevent |     | bugs. |     |     |     |     |     |             |           |       |     |             |     |                  |     |
| -------------- | --- | ----- | --- | --- | --- | --- | --- | ----------- | --------- | ----- | --- | ----------- | --- | ---------------- | --- |
|                |     |       |     |     |     |     |     | traditional | software, | might | not | be suitable |     | when prototyping |     |
Their process consists in daily play-tests with continuous gamesduetotheconstantchangesinthegamedesign.Finally,
delivery that uses days instead of weeks. They also use the addition of new features should take precedence over bug
| automated | tests | for performance |     | and integration |     | testing, | with |               |                  |     |     |       |      |              |     |
| --------- | ----- | --------------- | --- | --------------- | --- | -------- | ---- | ------------- | ---------------- | --- | --- | ----- | ---- | ------------ | --- |
|           |       |                 |     |                 |     |          |      | fixing, i.e., | developersshould |     | not | spend | time | and efforton | an  |
ad-hoc scripts to test the game loop and front end. game that may not even be fun to play.
| 5) [CASE-5] |     | Automated | Testing | of  | Gameplay | Features | in  |              |     |             |     |         |          |         |     |
| ----------- | --- | --------- | ------- | --- | -------- | -------- | --- | ------------ | --- | ----------- | --- | ------- | -------- | ------- | --- |
|             |     |           |         |     |          |          |     | 2) [MEDIA-2] |     | Differences |     | between | Software | Testing | and |
SeaofThieves:
RareisthedeveloperofSeaofThieves,using Game Testing: The author discusses the differences between
UnrealEngine.Theyusedtheenginefeaturestoaddtestscases
|              |        |                 |     |      |          |      |        | testing games | and | traditional |     | software. | He  | argues that | black |
| ------------ | ------ | --------------- | --- | ---- | -------- | ---- | ------ | ------------- | --- | ----------- | --- | --------- | --- | ----------- | ----- |
| at different | levels | of abstraction. |     | Rare | has more | than | 23,000 |               |     |             |     |           |     |             |       |
boxtestingandautomationisthesameforsoftwareandgame.
tests and 100,000asset auditchecks. With this automatedtest However, he lists some particularities of game testing:
| process,theymanagedtokeepa |     |     |     | constantnumberofbugsand |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
avoid working overtime. They divided the test into: • User-Experience (UX) testing is not the same as fun-
factor testing;
| • Actor     | testing   | (70%):       | This        | type of      | tests           | uses the   | Actor |           |         |            |              |        |             |                  |          |
| ----------- | --------- | ------------ | ----------- | ------------ | --------------- | ---------- | ----- | --------- | ------- | ---------- | ------------ | ------ | ----------- | ---------------- | -------- |
|             |           |              |             |              |                 |            |       | • Balance | testing | needs      | a            | vast   | knowledge   | of               | the game |
| class       | of Unreal | Engine       | to          | have lighter | tests           | compared   | to    |           |         |            |              |        |             |                  |          |
|             |           |              |             |              |                 |            |       | design    | and     | the target | audience;    |        |             |                  |          |
| integration |           | tests, which | have        | heavy        | dependenciesand |            | do    |           |         |            |              |        |             |                  |          |
|             |           |              |             |              |                 |            |       | • Testing | the     | game world | or           | some   | level       | can be automated |          |
| not         | scale     | well;        |             |              |                 |            |       |           |         |            |              |        |             |                  |          |
|             |           |              |             |              |                 |            |       | in unique |         | ways, such | as           | having | bots moving |                  | randomly |
| • Unit      | testing   | (23%):       | This is     | the most     | basic           | test unit; |       |           |         |            |              |        |             |                  |          |
|             |           |              |             |              |                 |            |       | through   | the     | game world | to           | see    | if they     | get stuck;       |          |
| • Map       | testing   | (5%):        | These tests | load         | portions        | of the     | game  |           |         |            |              |        |             |                  |          |
|             |           |              |             |              |                 |            |       | • AI      | testing | requires   | that         | the    | testers     | understand       | what     |
| and         | check     | a small      | action,     | like the     | interaction     | between    |       |           |         |            |              |        |             |                  |          |
|             |           |              |             |              |                 |            |       | triggers  | the     | behavior   | of different |        | types       | of non-playable  |          |
| some        | actors    | and objects; |             |              |                 |            |       |           |         |            |              |        |             |                  |          |
characters(NPC)andhowthesetriggerscanbeconfused
| Screenshot    |             | testing     | (1%):            | This type    | of      | tests is used | to    |                                                       |     |               |        |           |                          |      |             |
| ------------- | ----------- | ----------- | ---------------- | ------------ | ------- | ------------- | ----- | ----------------------------------------------------- | --- | ------------- | ------ | --------- | ------------------------ | ---- | ----------- |
| •             |             |             |                  |              |         |               |       | by different                                          |     | parameters;   |        |           |                          |      |             |
| check         | the         | rendering   | output;          |              |         |               |       |                                                       |     |               |        |           |                          |      |             |
|               |             |             |                  |              |         |               |       | • Multiplayer/Networktestingrequiresmanyplayerssimul- |     |               |        |           |                          |      |             |
| • Performance |             | testing     | (less than       | 1%):         | These   | tests monitor |       |                                                       |     |               |        |           |                          |      |             |
|               |             |             |                  |              |         |               |       | taneously                                             |     | in the game   | world, | with      | computer-controlled      |      |             |
| the           | frame-rate  | of the      | game             | and eventual |         | bottlenecks.  |       |                                                       |     |               |        |           |                          |      |             |
|               |             |             |                  |              |         |               |       | opponents                                             |     | and different | game   | servers.  |                          |      |             |
| C. Media      | specialized | in          | game development |              |         |               |       |                                                       |     |               |        |           |                          |      |             |
|               |             |             |                  |              |         |               |       | 20“Behaviorofasystemthatisnotexplicitly               |     |               |        |           | describedbythebehaviorof |      |             |
| Gamasutra     |             | is a portal | on               | everything   | related | to            | video |                                                       |     |               |        |           |                          |      |             |
|               |             |             |                  |              |         |               |       | the components                                        | of  | the system,   | and is | therefore | unexpected               | to a | designer or |
games and game development. We use Google Search to observer”(http://wiki.c2.com/?EmergentBehavior).

3) [MEDIA-3] Unit testing in video games: In this article, Implications - Game and software testers must work
the author discusses some concerns related to unit tests in together as a team: In game development, testers are profes-
game projects. He stated that he worked on Triple-A projects sionalswithspecificskillsetsrelatedtogametesting,andthey
that lasted more than 3 year, with 20 developers, and without are not engineers in general. Therefore, they write, automate,
a single unit test. Most developers were highly specialized, or script source code-related tests. They deal with games as
working only on a tiny fraction of the whole project; for black-boxes.Thus,thetestteamshouldincludeengineerswho
example, terrain rendering, network, UI, game-play, etc. can automate tests.
4) [MEDIA-4] Automated Testing: Building A Flexible Testing in game development is mostly22 done by a QA
Game Solver: This article is one more example of an ad- team.Thisprofessionalsassess gamesasblackboxes,playing
hoc solution to automate game testing. They used a script the role of users (players), stressing the games as intended
describing the goals of each game level and a brute-force for their users. Game developers deal with coding tasks, like
goals21.
algorithm to reach these Although this solution is game-enginedevelopment.Drawinga parallelwith traditional
well-suitedfortheirgame,thereareproblemswithhard-coded softwaredevelopment,gamedevelopersshouldbe therespon-
test scripts, for examples: sible for creating and executing tests. Thus, testing in game
• Linear testing: actions are always in the same order; projects should include game developers with knowledge of
thesourcecodeandgametesterswithknowledgeofthegames.
| • Cross | quests: | a   | test script | cannot | take | into | account |     |     |     |     |     |     |     |     |
| ------- | ------- | --- | ----------- | ------ | ---- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
variations or optional side quests; As with traditional software development, studios might
• Up to date:if developers“forget”to reportmodifications ignore testing for reasons like scope, budget, and time. In
to the adventure, the scripts may fail; these cases, coverage of the games might not be a good
• Dependent upon development completion: it is difficult metric to follow. Still, game developers should pursue ways
to test until the complete adventure is implemented; toautomatizethetestingprocess,butalsoprovidewaysto aid
• Logic: a change to a quest in one chapter may impact the game testers in their task.
| another | part | of the | game. |     |     |     |     |            |     |            |     |         |             |     |          |
| ------- | ---- | ------ | ----- | --- | --- | --- | --- | ---------- | --- | ---------- | --- | ------- | ----------- | --- | -------- |
|         |      |        |       |     |     |     |     | C. Finding | #3: | Automation |     | in game | development |     | is over- |
V. DISCUSSION
|     |     |     |     |     |     |     |     | looked, | as it relies | on  | manual | human | testers |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------ | ----- | ------- | --- | --- |
A. Finding#1:Thetestingstrategiesshouldtakeintoaccount
|                     |     |         |          |     |                  |     |          | Observations |            | - Automation |          | in         | video-game | testing | is not  |
| ------------------- | --- | ------- | -------- | --- | ---------------- | --- | -------- | ------------ | ---------- | ------------ | -------- | ---------- | ---------- | ------- | ------- |
| the particularities |     | of game | projects |     | wrt. traditional |     | software |              |            |              |          |            |            |         |         |
|                     |     |         |          |     |                  |     |          | common:      | Automation |              | is often | overlooked |            | because | of cou- |
Observations - Game development process has partic- pling, scope, randomness, cost, requirements, time, domain
| ularities:  | The | majority        | of  | the researchers |     | agree       | that game |               |                  |     |          |      |            |     |             |
| ----------- | --- | --------------- | --- | --------------- | --- | ----------- | --------- | ------------- | ---------------- | --- | -------- | ---- | ---------- | --- | ----------- |
|             |     |                 |     |                 |     |             |           | restrictions, | non-reusable     |     | code.    | Yet, | automation |     | has many    |
| development | has | particularities |     | compared        | to  | traditional | soft-     |               |                  |     |          |      |            |     |             |
|             |     |                 |     |                 |     |             |           | benefits:     | reproducibility, |     | quality, | bug  | reduction, |     | better test |
ware development, mostly because of the final product goal: focus, game stability.
| software | as a “productivity” |     |     | product | and video | game | as an |              |     |        |               |     |         |      |        |
| -------- | ------------------- | --- | --- | ------- | --------- | ---- | ----- | ------------ | --- | ------ | ------------- | --- | ------- | ---- | ------ |
|          |                     |     |     |         |           |      |       | Implications |     | - Lack | of automation |     | demands | more | (from) |
“entertainement”product.Thesedifferencesreflectontheway human testers: In game development, the concern (and bud-
| the process  | of developing   |          | a    | game     | is conducted, | mainly           | with      |              |                                             |     |              |             |           |        |            |
| ------------ | --------------- | -------- | ---- | -------- | ------------- | ---------------- | --------- | ------------ | ------------------------------------------- | --- | ------------ | ----------- | --------- | ------ | ---------- |
|              |                 |          |      |          |               |                  |           | get) mostly  | focuses                                     | on  | play-testing |             | the game. | Thanks | deep-      |
| requirements | and             | addition | of   | features | along         | the development. |           |              |                                             |     |              |             |           |        |            |
|              |                 |          |      |          |               |                  |           | learning     | algorithms,                                 |     | there are    | initiatives | to        | train  | agents and |
| Implications |                 | - New    | game | testing  | methods       | are              | neces-    |              |                                             |     |              |             |           |        |            |
|              |                 |          |      |          |               |                  |           | play test    | the games.                                  |     | It is still  | too         | early for | proper | adoption   |
| sary: These  | particularities |          | of   | game     | development   |                  | should be |              |                                             |     |              |             |           |        |            |
|              |                 |          |      |          |               |                  |           | (i.e.,usinga | standardsolution),butitisindeedastepforward |     |              |             |           |        |            |
taken in consideration when devising a testing strategy for to mitigate the burdenof the repetitivetasks that game testers
| a game        | project.  | Applying | traditional |       | testing     | strategies, | e.g.       |            |     |        |          |              |     |                 |     |
| ------------- | --------- | -------- | ----------- | ----- | ----------- | ----------- | ---------- | ---------- | --- | ------ | -------- | ------------ | --- | --------------- | --- |
|               |           |          |             |       |             |             |            | have to    | do. |        |          |              |     |                 |     |
| high emphasis | on        | unit     | testing     | using | Test Driven | Development |            |            |     |        |          |              |     |                 |     |
| (TDD),        | to a game | project  |             | might | not bring   | the         | expected   |            |     |        |          |              |     |                 |     |
|               |           |          |             |       |             |             |            | D. Finding | #4: | Search | for the  | “fun-factor” |     | and “balancing” |     |
| benefits.     | Yet, new  | testing  | strategies  |       | should      | be the      | results of |            |     |        |          |              |     |                 |     |
|               |           |          |             |       |             |             |            | the game   | are | mainly | executed | by game-play |     | testers         |     |
theconvergenceofwell-knownsoftwaretestingstrategies,like
unit testing, continuous integration (CI), and TDD. Finally, Observations - Game testing employs exclusive tech-
these particularities do not justify using only manual testing. niques: According to the academic papers, there are testing
|            |     |      |         |        |                |     |          | techniquesexclusive |         | for | game       | development,mostly |        |      | related to |
| ---------- | --- | ---- | ------- | ------ | -------------- | --- | -------- | ------------------- | ------- | --- | ---------- | ------------------ | ------ | ---- | ---------- |
| B. Finding | #2: | Game | testers | should | work alongside |     | software |                     |         |     |            |                    |        |      |            |
|            |     |      |         |        |                |     |          | game-play           | testing | and | the search | for                | fun or | game | balancing. |
testers to complement one another skills However, these new techniques are poorly explained or too
Observations - Game testers are not software testers: abstract, making them hard to implement and automate. Like
Game testers are mostly game-play testers, responsible for regression testing or smoke testing, some techniques are
searching bugs and assessing the game experience, i.e., the knownfor their use in traditionalsoftware development.Still,
fun factor. Although they are usually not considered part of in game development, the approaches are different, relying
thedevelopmentteamandhavepoorworkingconditions,their more on game testing.
| feedback | is fundamental |     | to the | success | of games. |     |     |              |      |             |             |     |                 |     |               |
| -------- | -------------- | --- | ------ | ------- | --------- | --- | --- | ------------ | ---- | ----------- | ----------- | --- | --------------- | --- | ------------- |
|          |                |     |        |         |           |     |     | 22Especially | with | independent | developers, |     | teams sometimes |     | cannot afford |
21https://www.youtube.com/watch?v=yXXTJ EKOIQ aseparated QAteamandmustthemselves testthegames.

Implications - Techniques performed only by gameplay b) Implications-Testingandgameplaytestingshouldnot
testers: The search for the fun-factor is not the only thing be delayed: The non-linearityand randomnessof most of the
that game testers do. They also use their skills and empirical games nowadays, makes it hard to cover essential cases of a
knowledge to investigate the games intelligently. These tech- game. The scope—the world, the variables, the randomness,
niques are hard to automate. the paths—are too much to cover. Developers have concerns
|     |     |     |     |     |     |     |     | regardingthe |     | lackof testing.Testers |     | needthe |     | gameartifactin |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------------------- | --- | ------- | --- | -------------- | --- |
E. Finding#5:There isnoone-size-fits-alltestingprocessfor a “playable” version to perform their assessments. However,
giventhetightdeadlines,thisplayablebuildisonlyaccessible
| game projects |     | as the | games | differ | greatly |     |     |                          |     |     |                        |     |     |     |            |
| ------------- | --- | ------ | ----- | ------ | ------- | --- | --- | ------------------------ | --- | --- | ---------------------- | --- | --- | --- | ---------- |
|               |     |        |       |        |         |     |     | late in development.Game |     |     | developersshouldstrive |     |     |     | to release |
Observations-Bigstudiosusead-hoctestingtechniques: incremental builds to game testers.
| Big studios | with | resources |     | can | develop | testing | processes |     |     |     |     |     |     |     |     |
| ----------- | ---- | --------- | --- | --- | ------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
VI. THREATS
| tailored | for their | needs,     | well | suited     | for specific | games.     | Small   |     |      |         |         |              |     |          |       |
| -------- | --------- | ---------- | ---- | ---------- | ------------ | ---------- | ------- | --- | ---- | ------- | ------- | ------------ | --- | -------- | ----- |
|          |           |            |      |            |              |            |         | a)  | Hard | to find | trusted | information: |     | The most | chal- |
| studios  | rely on   | creativity | and  | customized |              | techniques | to test |     |      |         |         |              |     |          |       |
their games. The lack of well-defined strategies is evident, lenging aspect of this study was finding trusted information
even when using of-the-shelves engines like Unreal, develop- about video-game development. We saw biased data even in
ers must devise their own testing strategies. academic papers. Moreover, video-game studios are secretive
|              |            |       |          |           |            |              |            | about their | processes | and         | practices. | We  | tried        | to mitigate | this     |
| ------------ | ---------- | ----- | -------- | --------- | ---------- | ------------ | ---------- | ----------- | --------- | ----------- | ---------- | --- | ------------ | ----------- | -------- |
| Implications |            | - The | use      | of ad-hoc | techniques |              | shows that |             |           |             |            |     |              |             |          |
|              |            |       |          |           |            |              |            | challenge   | by        | using three | sources    | of  | information: |             | academic |
| there is     | no testing |       | standard | for       | game       | development: | Big        |             |           |             |            |     |              |             |          |
studios can build tailored systems that are well integrated papers, technical blogs and talks, and postmortem data.
|            |                       |     |     |     |         |         |          | b)  | Academic | studies | diverge | greatly: |     | Studies | about |
| ---------- | --------------------- | --- | --- | --- | ------- | ------- | -------- | --- | -------- | ------- | ------- | -------- | --- | ------- | ----- |
| into their | developmentpipelines. |     |     |     | As game | studios | struggle | to  |          |         |         |          |     |         |       |
reach the release date, commonalities among different game games and software engineering discuss mainly the differ-
|                          |     |               |             |         |                        |            |             | ences between             |            | systems  | and    | games, while | AI              | papers | focus on   |
| ------------------------ | --- | ------------- | ----------- | ------- | ---------------------- | ---------- | ----------- | ------------------------- | ---------- | -------- | ------ | ------------ | --------------- | ------ | ---------- |
| types should             | be  | investigated, |             | so that | working                | strategies | could       |                           |            |          |        |              |                 |        |            |
|                          |     |               |             |         |                        |            |             | machine-learningmodelsfor |            |          |        | mastering    | the game.       | Few    | papers     |
| reused/tailored          |     | for specific  |             | games.  |                        |            |             |                           |            |          |        |              |                 |        |            |
|                          |     |               |             |         |                        |            |             | show an                   | end-to-end | solution |        | for testing  | games.          |        |            |
|                          |     |               |             |         |                        |            |             | Our choice                |            | of using | only   | titles and   | abstract        | to     | classify a |
| F. Finding               | #6: | The           | acknowledge |         | importance             | of         | testing by  |                           |            |          |        |              |                 |        |            |
|                          |     |               |             |         |                        |            |             | paper as                  | relevant   | may      | have   | led us to    | reject          | (many) | relevant   |
| gamestudiosshouldopenthe |     |               |             | doorfor | open-sourceinitiatives |            |             |                           |            |          |        |              |                 |        |            |
|                          |     |               |             |         |                        |            |             | ones. However,            |            | these    | papers | should       | have reappeared |        | during     |
|                          |     |               |             |         |                        |            |             | the snowballing           |            | process  | (from  | 71 to 38     | to 96).         |        |            |
| Observations             |     | -             | Game        | studios | are aware              | of         | testing im- |                           |            |          |        |              |                 |        |            |
portance: Although not common, there are advanced testing c) Absence of a common field: Academic studies are
techniques adopted by big companies. All projects described spread across computer science (new algorithms), software
|             |            |     |          |     |             |     |             | engineering | (tools | and | processes), | video-game |     | design | (game |
| ----------- | ---------- | --- | -------- | --- | ----------- | --- | ----------- | ----------- | ------ | --- | ----------- | ---------- | --- | ------ | ----- |
| in the gray | literature |     | (Section | IV) | implemented |     | a different |             |        |     |             |            |     |        |       |
testing technique,so it can be better applied to its game type. play,aesthetics),andmachinelearning(trainingagents).Thus,
|           |        |     |            |      |            |     |          | points of | view | and vocabularies |     | vary | greatly. | We  | kept this |
| --------- | ------ | --- | ---------- | ---- | ---------- | --- | -------- | --------- | ---- | ---------------- | --- | ---- | -------- | --- | --------- |
| This fact | allows | us  | to believe | that | developers | are | aware of |           |      |                  |     |      |          |     |           |
the importance of discover new techniques to test the game study focusedonsoftware engineering,butintersections/over-
and not rely only on play-testing sessions. We observed that laps and contradictions still exist.
| differentstudiesapply |     |     | ad-hocgametesting |     |     | strategies, | varying |     |     |      |            |     |     |     |     |
| --------------------- | --- | --- | ----------------- | --- | --- | ----------- | ------- | --- | --- | ---- | ---------- | --- | --- | --- | --- |
|                       |     |     |                   |     |     |             |         |     |     | VII. | CONCLUSION |     |     |     |     |
accordingtogamegenres(FPS,RPG,Sports,etc),gametypes
|              |         |        |             |                      |            |       |          | No matterhow  |     | largeare      | theirbudgetsorteam |            |         | sizes, | video- |
| ------------ | ------- | ------ | ----------- | -------------------- | ---------- | ----- | -------- | ------------- | --- | ------------- | ------------------ | ---------- | ------- | ------ | ------ |
| (2D, 3D),    | revenue | models |             | (game-as-a-service), |            | etc.  |          |               |     |               |                    |            |         |        |        |
|              |         |        |             |                      |            |       |          | game projects |     | are notorious |                    | for having | day-one | bugs.  | Some   |
| Implications |         | -      | The testing |                      | importance | shows | that the |               |     |               |                    |            |         |        |        |
gamescanrecover,likeNoMan’sSkythathadproblemswith
| game industry |               | should | invest | on      | open-source | initiatives |          | to      |          |           |     |           |     |            |       |
| ------------- | ------------- | ------ | ------ | ------- | ----------- | ----------- | -------- | ------- | -------- | --------- | --- | --------- | --- | ---------- | ----- |
|               |               |        |        |         |             |             |          | missing | features | at launch | but | recovered | its | reputation | after |
| spread        | the knowledge |        | and    | advance | the         | field:      | The game |         |          |           |     |           |     |            |       |
manyupdatesalongtheyears23,whileothersareforgotten,like
| industry  | should    | learn     | from | traditional | software | initiatives | and     |             |         |            |              |            |          |                |            |
| --------- | --------- | --------- | ---- | ----------- | -------- | ----------- | ------- | ----------- | ------- | ---------- | ------------ | ---------- | -------- | -------------- | ---------- |
|           |           |           |      |             |          |             |         | Anthem,     | which   | also had   | bugs         | at launch  | but      | which          | developers |
| invest in | sharing   | knowledge |      | among       | game     | developers, | so that |             |         |            |              |            |          |                |            |
|           |           |           |      |             |          |             |         | preferredto | rewrite | it         | entirely24,  | finally    | ending   | up canceled25. |            |
| the field | can grown | faster.   |      |             |          |             |         |             |         |            |              |            |          |                |            |
|           |           |           |      |             |          |             |         | In this     | paper,  | we studied |              | video game | projects | by             | investi-   |
|           |           |           |      |             |          |             |         | gating game | testing | in         | the academic |            | and gray | literature.    | We         |
G. Finding #7: Issues like lack of plan and poor testing surveyed processes, techniques, gaps, concerns, and point-of-
| coverage | call         | for game | testing | to      | be performed | early            |     |          |            |     |      |            |      |       |           |
| -------- | ------------ | -------- | ------- | ------- | ------------ | ---------------- | --- | -------- | ---------- | --- | ---- | ---------- | ---- | ----- | --------- |
|          |              |          |         |         |              |                  |     | views to | understand | how | game | developers | test | their | projects. |
|          |              |          |         |         |              |                  |     | The main | findings   | are | as   | follows:   |      |       |           |
| a)       | Observations |          | - Lack  | of plan | and          | testing coverage | are |          |            |     |      |            |      |       |           |
the main problems: The most common issues gathered from 1) Testing strategies must consider the particularities of
|     |     |     |     |     |     |     |     | game | projects; | unlike | traditional |     | software | (Section | V-A); |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --------- | ------ | ----------- | --- | -------- | -------- | ----- |
video-gamepostmortemsindicatethatgamedevelopersdonot
|            |         |      |               |     |      |          |         | 2) Game    | testers | should | work  | along           | with software |       | testers to |
| ---------- | ------- | ---- | ------------- | --- | ---- | -------- | ------- | ---------- | ------- | ------ | ----- | --------------- | ------------- | ----- | ---------- |
| plan ahead | testing | and, | consequently, |     | test | coverage | is low. |            |         |        |       |                 |               |       |            |
|            |         |      |               |     |      |          |         | complement |         | each   | other | skills (Section |               | V-B); |            |
Moreover,thespecificrequirementsoftheprojectarelistedas
| the main | cause | of difficulties |     | in adding | proper | testing | during |     |     |     |     |     |     |     |     |
| -------- | ----- | --------------- | --- | --------- | ------ | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
23http://bit.ly/3isBBkn.
thedevelopment.Otherproblemsarerelatedtofeedbackfrom
24http://bit.ly/3ir9PF3
the testers and project’s scope. 25https://www.pcgamer.com/anthem-next-cancelled/

| 3) Automation |     | is overlooked; |     | game testing | currently | relies |              |     |               |      |       |         |      |              |
| ------------- | --- | -------------- | --- | ------------ | --------- | ------ | ------------ | --- | ------------- | ---- | ----- | ------- | ---- | ------------ |
|               |     |                |     |              |           |        | [9] C. Lewis | and | J. Whitehead, | “The | whats | and the | whys | of games and |
softwareengineering,”inProceedingofthe1stinternationalworkshop
| mostly        | on human | testers | (Section     | V-C);   |          |          |            |                     |              |               |                              |                |     |                |
| ------------- | -------- | ------- | ------------ | ------- | -------- | -------- | ---------- | ------------------- | ------------ | ------------- | ---------------------------- | -------------- | --- | -------------- |
|               |          |         |              |         |          |          | on Games   |                     | and software | engineering   | -                            | GAS 11,        | ACM | Press, 2011,   |
| 4) The search |          | for the | “fun-factor” | and     | “game    | balance” | is         |                     |              |               |                              |                |     |                |
|               |          |         |              |         |          |          | pp.1–4,    | ISBN:9781450305785. |              |               | DOI:10.1145/1984674.1984676. |                |     |                |
| mainly        | executed | by      | game-play    | testers | (Section | V-D);    |            |                     |              |               |                              |                |     |                |
|               |          |         |              |         |          |          | [10] R. E. | S. Santos,          | C. V.        | C. Magalhaes, |                              | L. F. Capretz, |     | J. S. Correia- |
5) There is no one-size-fits-all testing process for game Neto, F. Q. B. da Silva, and A. Saher, “Computer games are se-
|          |        |      |       |                |          |       | rious | business | and so | is their | quality,” | in Proceedings |     | of the 12th |
| -------- | ------ | ---- | ----- | -------------- | -------- | ----- | ----- | -------- | ------ | -------- | --------- | -------------- | --- | ----------- |
| projects | as the | game | types | differ greatly | (Section | V-E); |       |          |        |          |           |                |     |             |
ACM/IEEEInternationalSymposiumonEmpiricalSoftwareEngineer-
6) Game studios acknowledge the importance of testing, ing andMeasurement -ESEM18,ACMPress, 2018, pp.1–10. DOI:
opportunity for open-source initiatives (Section V-F); 10.1145/3239235.3268923.
|     |     |     |     |     |     |     | [11] J. Kasurinen, |     | R. Laine, | and | K. Smolander, |     | “How | applicable |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --------- | --- | ------------- | --- | ---- | ---------- |
7) Issueslikelackofplanandpoortestingcoveragecallfor
|     |     |     |     |     |     |     | is ISO/IEC |     | 29110 in | game | software | development?” |     | In Product- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ---- | -------- | ------------- | --- | ----------- |
game testing to be performed early (Section V-G); Focused Software Process Improvement, vol. 7983 LNCS, Springer
|     |     |     |     |     |     |     | Berlin | Heidelberg, | 2013, | pp. | 5–19, ISBN: | 9783642392580. |     | DOI: |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | ----- | --- | ----------- | -------------- | --- | ---- |
Weconcludethatautomatingthevideo-gametestingprocess
|     |     |     |     |     |     |     | 10.1007/978-3-642-39259-7 |     |     | 4.  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
is the natural next step. However, developers and researchers [12] P. Stacey and J. Nandhakumar, “A temporal perspective of the
lack processes, frameworks, and tools to help them with computer game development process,” Information Systems Journal,
|                  |     |         |           |            |      |          | vol. | 19, no. | 5, pp. | 479–497, | Sep. 2009, | ISSN: | 1350-1917. | DOI: |
| ---------------- | --- | ------- | --------- | ---------- | ---- | -------- | ---- | ------- | ------ | -------- | ---------- | ----- | ---------- | ---- |
| test automation. | It  | results | in ad-hoc | techniques | that | are hard |      |         |        |          |            |       |            |      |
10.1111/j.1365-2575.2007.00273.x.
| to generalize | on  | different | game | types. | Yet, testing | is the |     |     |     |     |     |     |     |     |
| ------------- | --- | --------- | ---- | ------ | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
[13] M.MozgovoyandE.Pyshkin,“Acomprehensiveapproachtoquality
key to quality games, and automation makes game quality assurance in a mobile game project,” in Proceedings of the 14th
CentralandEasternEuropeanSoftwareEngineeringConferenceRus-
sustainable.
|           |       |         |           |      |        |             | sia            | on ZZZ | - CEE-SECR                   | 18, | ACM Press, | 2018, | pp. | 1–8, ISBN: |
| --------- | ----- | ------- | --------- | ---- | ------ | ----------- | -------------- | ------ | ---------------------------- | --- | ---------- | ----- | --- | ---------- |
| In future | work, | we want | to expand | this | survey | into a com- |                |        |                              |     |            |       |     |            |
|           |       |         |           |      |        |             | 9781450361767. |        | DOI:10.1145/3290621.3290835. |     |            |       |     |            |
plete,systematicmappingoftheacademicandgrayliterature, [14] C. P. Schultz, R. Bryant, and T. Langdell, Game Testing All in One
|            |          |            |         |           |     |           | (Game | Development | Series). | Course | Technology |     | PTR, | 2005, p. 520, |
| ---------- | -------- | ---------- | ------- | --------- | --- | --------- | ----- | ----------- | -------- | ------ | ---------- | --- | ---- | ------------- |
| with clear | research | questions, | quality | criteria, | and | including |       |             |          |        |            |     |      |               |
ISBN:1592003737.
| topic(in)dependentclassifications,like |     |     |     | publicationtrends.We |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
[15] S.Aleem,L.F.Capretz,andF.Ahmed,“CriticalSuccessFactorstoIm-
willcomparethecontentsandtrendsoftheacademicandgray provetheGameDevelopmentProcessfromaDeveloper’sPerspective,”
literature, in particular separating processes and techniques. JournalofComputerScienceandTechnology,vol.31,no.5,pp.925–
|     |     |     |     |     |     |     | 950,2016, |     | ISSN:1000-9000. | DOI:10.1007/s11390-016-1673-z. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------------- | ------------------------------ | --- | --- | --- | --- |
We will also focus on practical techniques to automate the [16] J. Schreier, Quality Assured: What It’s Re-
game testing, allowing designers, programmers, and game ally Like To Test Games For A Living,
testers to work together. https://kotaku.com/quality-assured-what-it-s-really-like-to-play-games-fo-1720053842,
|     |     |     |     |     |     |     | Accessed:     | 2019-07-18. |             |     |        |      |             |        |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------- | ----------- | --- | ------ | ---- | ----------- | ------ |
|     |     |     |     |     |     |     | [17] J. Blow, | “Game       | Development |     | Harder | Than | You Think,” | Queue, |
REFERENCES
|     |     |     |     |     |     |     | vol. | 1, no. | 10, p. | 28, Feb. | 2004, | ISSN: | 1542-7730. | DOI: |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------ | ------ | -------- | ----- | ----- | ---------- | ---- |
[1] D. Spinellis, “State-of-the-Art Software Testing,” IEEE 10.1145/971564.971590.
Software, vol. 34, no. 5, 2017, ISSN: 1937-4194. DOI: [18] S.Hooper,“AutomatedTestingandValidationofComputerGraphics
10.1109/MS.2017.3571564. ImplementationsforCross-platformGameDevelopment,”M.S.thesis,
[2] R.J.Adams,P.Smart,andA.S.Huff,“Shadesofgrey:Guidelinesfor Auckland University ofTechnology, 2017.
workingwiththegreyliteratureinsystematicreviewsformanagement [19] E. Murphy-Hill, T. Zimmermann, and N. Nagappan, “Cowboys,
and organizational studies,” International Journal of Management ankle sprains, and keepers of quality: How is video game devel-
Reviews,vol.19,no.4,pp.432–454, 2017. opment different from software development?” In Proceedings of
[3] C. Politowski, F. Petrillo, G. C. Ullmann, J. de Andrade Werly, and the 36th International Conference on Software Engineering - ICSE
Y.-G.Gue´he´neuc,Datasetofvideogamedevelopmentproblems,2020. 2014, ACM Press, 2014, pp. 1–11, ISBN: 978-1-4503-2756-5. DOI:
| arXiv:2001.00491[cs.SE]. |     |     |     |     |     |     | 10.1145/2568225.2568226. |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- |
[4] S. Hyrynsalmi, E. Klotins, M. Unterkalmsteiner, T. Gorschek, N. [20] M. Shelley, “On the Feasibility of using Use Case Maps for the
Tripathi,L.B.Pompermaier,andR.Prikladnicki,“WhatisaMinimum PreventionofSequenceBreakinginVideoGames,”Ph.D.dissertation,
Viable (Video) Game?” In 17th IFIP WG 6.11 Conference on e- Carleton University, 2013, ISBN:9780494946374.
Business, e-Services, and e-Society, I3E 2018, vol. 11195, Springer- [21] R. Ramadan and B. Hendradjaya, “Development of game testing
Verlag GmbH, Oct. 2018, pp. 217–231, ISBN: 3030021300. DOI: methodformeasuringgamequality,”in2014InternationalConference
10.1007/978-3-030-02131-3. on Data and Software Engineering (ICODSE), IEEE, Nov. 2014,
[5] J.Kasurinen,M.Palacin-Silva,andE.Vanhala,“WhatConcernsGame pp.1–6, ISBN:9781479979967. DOI:10.1109/icodse.2014.7062694.
Developers?AStudyonGameDevelopmentProcesses,Sustainability [22] J. Musil, A. Schweda, D. Winkler, and S. Biffl, “A Survey on the
and Metrics,” International Workshop on Emerging Trends in Soft- StateofthePracticeinVideoGameSoftwareDevelopment,”Institute
ware Metrics, WETSoM, pp. 15–21, 2017, ISSN: 2327-0969. DOI: of Software Technology and Interactive Systems, Tech. Rep. March,
| 10.1109/WETSoM.2017.3. |     |     |     |     |     |     | 2010,p.13. |     |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
[6] D. Callele, P. Dueck, K. Wnuk, and P. Hynninen, “Experience re- [23] A. Ampatzoglou andI. Stamelos, “Software engineering research for
quirements in video games: Definition and testability,” 2015 IEEE computer games: A systematic review,” Information and Software
23rd International Requirements Engineering Conference, RE 2015 - Technology, vol.52,no.9,pp.888–901,Sep.2010,ISSN:0950-5849.
Proceedings, pp.324–333,2015. DOI:10.1109/RE.2015.7320449. DOI:10.1016/j.infsof.2010.05.004.
[7] C. M. Kanode and H. M. Haddad, “Software engineering challenges [24] J.KasurinenandK.Smolander,“Whatdogamedeveloperstestintheir
in game development,” in 2009 Sixth International Conference on products?”Proceedingsofthe8thACM/IEEEInternationalSymposium
InformationTechnology:NewGenerations,IEEE,2009,pp.260–265, on Empirical Software Engineering and Measurement (ESEM’14),
ISBN:9780769535968. DOI:10.1109/itng.2009.74. pp.1–10,2014, ISSN:1949-3770. DOI:10.1145/2652524.2652525.
[8] A. Osborne O’Hagan, G. Coleman, and R. V. O’Connor, “Soft- [25] H.-r. Ruonala, “Agile Game Development: A Systematic Literature
ware Development Processes for Games: A Systematic Literature Review,” M.S. thesis, University of Helsinki, Faculty of Science,
Review,” Communications in Computer and Information Science, Department ofComputerScience, 2016.
vol. 425, no. June, pp. 182–193, 2014, ISSN: 1865-0929. DOI: [26] L. Pascarella, F. Palomba, M. Di Penta, and A. Bacchelli, “How
10.1007/978-3-662-43896-1 16. is video game development different from software development in
|     |     |     |     |     |     |     | open | source?”     | In Proceedings |     | - International |       | Conference   | on Soft- |
| --- | --- | --- | --- | --- | --- | --- | ---- | ------------ | -------------- | --- | --------------- | ----- | ------------ | -------- |
|     |     |     |     |     |     |     | ware | Engineering, | Gothenburg,    |     | Sweden,         | 2018, | pp. 392–402. | DOI:     |
10.1145/3196398.3196418.

[27] J. Kasurinen, J.-P. Strande´n, and K. Smolander, “What do game
developersexpectfromdevelopmentanddesigntools?”InProceedings
of the 17th International Conference on Evaluation and Assessment
in Software Engineering - EASE 13, ACM Press, 2013, p. 36, ISBN:
9781450318488. DOI:10.1145/2460999.2461004.
[28] A.I.WangandN.Nordmark,“SoftwareArchitecturesandtheCreative
Processes inGame Development,” Entertainment Computing –ICEC
2014,vol.8770,pp.272–285,2014.DOI:10.1007/978-3-662-45212-7.
[29] J. Koutonen and M. Leppa¨nen, “How are agile methods and
practices deployed in video game development? a survey into
finnish game studios,” in Lecture Notes in Business Information
Processing, Springer Berlin Heidelberg, 2013, pp. 135–149. DOI:
10.1007/978-3-642-38314-4 10.
[30] W.ScacchiandK.M.Cooper,“ResearchChallengesattheIntersection
ofComputerGamesandSoftwareEngineering,”ComputerGamesand
Software...,no.Fdg,2015.
[31] V.Paakkanen,“UserExperienceofGameDevelopmentEnvironments:
Can making games be as fun as playing them?” M.S. thesis, Aalto
University SchoolofScience, 2014.
[32] M. Washburn, P. Sathiyanarayanan, M. Nagappan, T. Zimmermann,
and C. Bird, “What went right and what went wrong: An analysis
of 155 postmortems from game development,” in Proceedings of
the 38th International Conference on Software Engineering Com-
panion - ICSE 16, ACM Press, 2016, ISBN: 9781450342056. DOI:
10.1145/2889160.2889253.
[33] E.Gamma,R.Helm,R.Johnson,andJ.M.Vlissides,DesignPatterns:
Elements of Reusable Object-Oriented Software, 1st ed. Addison-
WesleyProfessional, 1994, ISBN:0201633612.
[34] C.Politowski,F.Petrillo,G.C.Ullmann,andY.-G.Gue´he´neuc,Game
industryproblems:Anextensive analysis ofthegrayliterature, 2021.
eprint:2009.02440.
[35] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G.
Bellemare, A. Graves, M. Riedmiller, A. K. Fidjeland, G. Ostrovski,
S.Petersen,C.Beattie,A.Sadik,I.Antonoglou,H.King,D.Kumaran,
D.Wierstra,S.Legg,andD.Hassabis,“Human-level controlthrough
deep reinforcement learning,” Nature, vol. 518, pp. 529–533, 2015,
ISSN:00280836.
[36] J.Harmer,L.Gissle´n, H.Holst,J.Bergdahl, T.Olsson,K.Sjo¨o¨,and
M.Nordin,“Imitation learningwithconcurrent actions in3dgames,”
CoRR,vol.abs/1803.05402, 2018.
[37] D.Horgan, J.Quan, D.Budden, G.Barth-Maron, M.Hessel, H.van
Hasselt, and D. Silver, “Distributed prioritized experience replay,” in
InternationalConferenceonLearningRepresentations,2018.[Online].
Available: https://openreview.net/forum?id=H1Dy---0Z.
[38] Y.Zhao,I.Borovikov,A.Beirami,J.Rupert,C.Somers,J.Harder,F.
deMesentierSilva,J.Kolen,J.Pinto,R.Pourabolghasem,H.Chaput,
J.Pestrak,M.Sardari,L.Lin,N.Aghdaie,andK.A.Zaman,“Winning
isn’teverything:Traininghuman-likeagentsforplaytesting andgame
AI,”CoRR,vol.abs/1903.10545, 2019.
[39] R.Lowe,Y.Wu,A.Tamar,J.Harb,P.Abbeel,andI.Mordatch,“Multi-
agent actor-critic for mixed cooperative-competitive environments,”
CoRR,vol.abs/1706.02275, 2017.