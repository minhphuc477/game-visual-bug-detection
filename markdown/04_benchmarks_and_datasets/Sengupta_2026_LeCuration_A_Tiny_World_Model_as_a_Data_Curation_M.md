---
title: "LeCuration A Tiny World Model as a Data Curation M"
author: "Sengupta"
year: "2026"
source_file: "04_benchmarks_and_datasets/Sengupta_2026_LeCuration_A_Tiny_World_Model_as_a_Data_Curation_M.pdf"
source_sha256: "87f932932408a6b7d38dff7a816d0b2168e44a54b0ceb02598bdc152b02e97a0"
converted_at: "2026-11-06T15:12:50.891564+00:00"
markitdown_version: "0.1.9"
char_count: 26683
---
| LeCuration: |     | A   | Tiny | World | Model |     | as  | a Data | Curation |
| ----------- | --- | --- | ---- | ----- | ----- | --- | --- | ------ | -------- |
Multi-Tool
NirmitDesai∗
|     | MayankSengupta |     |     |     |     | EricSong | KunalSawarkar |     |     |
| --- | -------------- | --- | --- | --- | --- | -------- | ------------- | --- | --- |
AIntropyAI
6202 tcO 7  ]GL.sc[  1v58290.0162:viXra Abstract
ManyapplicationsofphysicalAIrunwithinfiniteorclosedphysicalworldswitha
|     | limitedsetofphysicallawsgoverningobjectbehavior.      |     |     |     |     |     | Examplesincluderobots |     |           |
| --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --------------------- | --- | --------- |
|     | workinginawarehouseandagentsmovingaroundinavideogame. |     |     |     |     |     |                       |     | Inorderto |
betterorganize,filter,andcuratedataforphysicalAIapplications,weproposeanew
approachcenteredontheuniquesettingsandphysicallawsofindividualdatasets.
|     | WetrainLeCuration,   |     | asmallworldmodelintendedtoserveasadatacuration |     |        |     |            |        |           |
| --- | -------------------- | --- | ---------------------------------------------- | --- | ------ | --- | ---------- | ------ | --------- |
|     | tool for a separate, |     | larger downstream                              |     | model. | To  | build this | model, | we choose |
LeWorldModel(LeWM)(Maesetal.,2026)asourlatentencoderandpredictor,
|     | adding a diffusion |     | transformer                                     | (DiT) | decoder | to  | add visuals | to autoregressive |     |
| --- | ------------------ | --- | ----------------------------------------------- | ----- | ------- | --- | ----------- | ----------------- | --- |
|     | gameplayrollout.   |     | Wefindthattheembeddingsofthismodelcanbeusedasan |       |         |     |             |                   |     |
anomalydetectionsignalandasacontent-basedclusteringheuristic,andthatauto-
regressivelypredictingthegamestatewiththismodelallowsustoqualitatively
|     | check for action-state               |     | consistency. |     | This paper | presents                     | a   | qualitative, | proof-of- |
| --- | ------------------------------------ | --- | ------------ | --- | ---------- | ---------------------------- | --- | ------------ | --------- |
|     | conceptcasestudyonCS:GOgameplaydata; |     |              |     |            | wedonotyetreportquantitative |     |              |           |
curationmetricsordownstreamtrainingresults,whichweidentifyasthekeynext
step.
1 Introduction
Intelligentlycuratingdatapriortotrainingiskeytoensuringahighqualitymodel,especiallyfor
use cases in physical AI. The straightforward alternative, feeding a model everything, teaches it
thefulldistributionofthesourcedata,includingitsdegeneratecorners. Filteringbyhanddoesnot
scale. Rule-basedfiltersrequireaccesstothephysicsenginestate,whichishiddeninmostcasesor
impossibletoaccessifyourphysicsengineistherealworld. Mostimportantly,itisimpossibleto
understandtheeffectofacurateddatasetwithouttrainingamodelonit. Therefore,weneedasmall,
quicklytrainablecurationthathaslearnedenoughaboutadatasettocharacterizeit,identifyingwhat
istypical,whatisrare,andwhatissurprising.
WetrainsuchamodelonCounter-Strike: GlobalOffensive(CS:GO)gameplayrecordings. LeCura-
tionisadeliberatelysmallmodel: theencoderhasroughly2Mparameters,thepredictorroughly
13M.Bytrainingitonthisdatasetinamatterofhours,weallowthemodeltoproducerepresentations
andpredictionsthataresemanticallymeaningfulenoughtodrivecurationdecisionsatscale. Ontop
ofthis,webuiltadiffusiondecoderasavisualizationtool,lettingusdecodeembeddingsbackto
pixelstoinspectwhatthemodelhaslearned.
Concretely,thispaper’scontributionsare:(1)anadaptationofLeWMintoacompact,quickly-trained
curationtooloperatingonaTAESDlatentspace(Sec.2); (2)aqualitativedemonstrationthatits
embeddingsorganizegameplayfootageintosemanticallycoherentclustersusableforrebalancing
and degenerate-content filtering (Sec. 3); and (3) an unsupervised anomaly signal, derived from
autoregressiveembeddingdivergence,thatflagsframeswherethepredictor’sexpectationandthe
observedframedisagree(Sec.4). Weemphasizethatthisisaproof-of-conceptstudy: wevalidate
∗Correspondingauthor:nirmit.desai@aintropy.ai.
Preprint.

theseprimitivesqualitativelyonasingleCS:GOmap,andwehavenotyettrainedadownstream
modelonLeCuration-curateddataorestablishedquantitativemetricsforanyofthethreeprimitives
above;wediscussthisscopeexplicitlyinSec.5.
1.1 BackgroundandPriorWork
TheJEPAmodeltrainingparadigmhasbeenappliedalmostexclusivelytotwosettings.
• Thefirstisvisualcontrolandrobotplanning: V-JEPA2(Assranetal.,2025)trainsonoverone
millionhoursofinternetvideotoenablezero-shotrobotmanipulationbyplanninginlatentspace;
Causal-JEPA(Nametal.,2026)introducesobject-levellatentinterventionstolearncausalworld
structure;JEPA-basedLiDARmodels(ZhuandChoromanska,2026)applythesameframeworkto
spatiotemporaloccupancyforecastingforautonomousdriving.
• The second is representation learning for downstream classification and video understanding:
I-JEPA,V-JEPA,andVL-JEPAallframepredictionasapretexttaskforlearningtransferablevisual
features.
Ineverycase,theJEPAmodelistheendconsumerofitsownrepresentations.Thelearnedembeddings
and predictions are used either to plan the model’s own actions or to evaluate the model’s own
performanceonabenchmarktask. Incontrast,thispaperinvestigatestheapplicationofthelearned
representationsfordatacurationtasks.
1.2 MainContribution
The inspiration of LeCuration is LeWorldModel (LeWM) (Maes et al., 2026). LeWM’s central
contributionisastableend-to-endJEPAthattrainsdirectlyfromrawpixelsusingonlytwolossterms:
anext-embeddingpredictionlossandaSketchIsotropicGaussianRegularizer(SIGReg)thatprevents
representationcollapsewithoutstop-gradients, frozenencoders, orexponentialmovingaverages.
Muchliketherestoftheworksinthespace,LeWMispresentedentirelyasaplanningandcontrol
model. Givenagoalframe,thepredictoroptimizesasequenceofactionswhosepredictedlatent
trajectoryminimizesdistancetothegoalembedding.
Wedecidedtobuildonthisarchitectureforthreemainreasons:
1. Atroughly15Mparameters,itisamongthemostcompactworldmodelsthathavedemonstrated
competitiveperformanceoncontinuouscontrolbenchmarks. Thesmallerthemodel,thefasterit
trains,andthemorepracticalitistoadaptittonewdatasetsifitisdeployedinproduction.
2. Theauthorsestablishthemodel’srichlatent-spacepropertiesintheirablations. Physicalquantity
probingshowsthatagentposition,objectlocation,andobjectorientationarelinearlyrecoverable
from the CLS embedding (which is trained to be the overall per-frame world state). Surprise
evaluationshowsthatthemodelassignshigherpredictionerrortophysicallyimplausibleevents
(teleportingobjects)thantomatchedvisualperturbationsthatdonotviolatephysics. Additionally,
temporal path straightening shows that latent trajectories become increasingly linear during
training,apropertytheauthorsarguereflectstheemergenceofasmooth,locallyEuclideanworld
model.
3. LeWMisnotjustasingle-frameencodermodel. Whileeachframeisindeedindividuallyencoded
tothelatentspace,thepredictormoduleofLeWMactuallyusesahistoryof6previousvectors
beforepredictingthenextlatentworldstate. Thisallowsthemodeltounderstandthekinematics
ofdomain-specificdata,predictingworldstatenotjustfromposition,butalsofromvelocity.
WemodifyLeWMforafundamentallydifferentuse: asadatacurationtoolforaseparate,larger
downstreammodel,ratherthanasaplanner. LeCurationdoesnotplanactionsandisnotevaluatedon
anycontrolbenchmark. Instead,itsembeddingsandpredictoroutputsareusedtoanalyzethetraining
corpora.
Throughthisadaptation,weuncoverseveralinterestingproperties. Byclusteringtheembeddings,we
findthatwecanqualitativelyseparatetrainingdataintovisuallyandsemanticallydistinctgroups,
suchasframesfromdifferentmaplocationsandcameraframings(Sec.3);wehavenotmeasured
this against ground-truth location or orientation labels. We can also run the predictor module
autoregressivelyandcomparethepredictionswiththeencodedgroundtruthtofindanypossible
2

Figure1:ThefullarchitectureofLeCuration.FramesarecompressedtoStableDiffusionlatentsusing
TAESD,whicharethenencodedasworldstatevectorsbythelatentencoder. Thelatentpredictor
takes6pastworldstatesandthenextactionvectortopredictthenextworldstate,whichissupervised
byencodingthenextgroundtruthframeasaworldstate. TheDiffusionDecodergeneratesTAESD
latentsforeachgameplayframeindividually,conditionedonlyonthepredictedworldstate. These
aredecodedtoRGBframesbytheTAESDdecoder.
anomaliesorunexpectedshiftsindata. Inaddition,webuildadiffusiontransformer(DiT)decoderto
recovergameplayframesconditionedonautoregressiveCLStokensoutputbythepredictormodule.
Byfeedingastartingframeandasequenceofactions(keypushes)intothemodel,weareableto
reconstructnear-photorealisticgameplayvideofromonlyasequenceof196-dimensionalworld-state
vectors, showing that despite its small size and very quick training time, LeCuration can indeed
modelthelawsofaphysicsengine.
2 ArchitectureandTraining
WhilewetakeinspirationfromboththearchitectureandtrainingrecipeofLeWM,wemakemajor
modifications,asshowninFigure1,toimprovetrainingspeedandfitourgoalsofapplyingittodata
curationproblems.
2.1 StableDiffusion/TAESDLatentSpace
LeWMencodesdirectlyfrompixels. Wedecidetoinsteadmapourentiredatasettoamuchsmaller
intermediatelatentrepresentationbeforeanytraining. Wechoosetousethesameautoencoderas
Stable Diffusion (Rombach et al., 2021), as it has been standard practice, and is able to do 48×
compressionwhilelosingrelativelyfewimportantdetails. However,theautoencoderusedbyStable
Diffusionhas74Mparameters,andamuchmoreefficientalternative,calledTinyAutoEncoderfor
StableDiffusion(TAESD)(Bohan,2023),accomplishestheexactsametaskatafractionofthecost.
DistilledfromthestandardStableDiffusionautoencoder,TAESDonlyhas2.4Mparametersanda
singleforwardpassisroughly20×fasterthanthatoftheoriginalautoencoderonthesamedevice
(Bohan,2023).
Ourdatasetisthuscompressedfrom224×224×3framesto4×28×28TAESDlatents. Eachframe
hasacorrespondingactionvector,whichisa51-dimensionalone-hotencodedvectorrepresenting
thekeyspressedatthatframe(keypresses,mousemovements,andsoon).
2.2 LatentEncoderandPredictor
ThelatentencoderandpredictorwereinspiredbyLeWMbutadaptedtotheTAESDlatentspace.
The Latent Encoder is a patch-ViT operating on TAESD latents (patch size 4, 49 spatial patches
plus a CLS token [the world state], projected to 196 dimensions via 4 transformer layers). For
eachgameplayframe,itproducesasingle196-dimensionalworldstatee (theCLStoken)that
t+1
summarizestheframe’scontent. Thepatchtokensarediscardedaftereachforwardpass.
3

Thelatentpredictorisacausaltransformer(512hiddendimension,8layers,16heads)thattakesa
slidingwindowhistoryof6frameembeddingsplusactionembeddingsandpredictsthenextframe’s
embedding. Actionsareprojectedto196dimensionsbyasmallactionembedderbeforebeingfed
tothepredictor. Theactionembedderisa1d-convolution(kernel_size=10,stride=1)followedbya
2-layerMLP(hidden_dim=768)whichtransformsthe51-dimensionalone-hotencodedactionvector
intoa196-dimembedding.
Ateachautoregressivestepthepredictoroutputsworldstateeˆ : itsexpectationofwhatthenext
t+1
frameshouldlooklikeinembeddingspace,giventherecentcontextandtheactiontaken. Thequality
ofthisprediction—andinparticularthegapbetweeneˆ andtheobservede —istheprimary
t+1 t+1
curationsignal.
2.3 DiffusionTransformerDecoder
A Diffusion Transformer (DiT) Decoder (512 hidden dimension, 8 layers, CFG dropout 0.1) is
trainedtodenoiseTAESDlatentsconditionedonthefrozenCLSembedding. Thisletsusdecode
anyembeddingbacktopixelstovisuallyinspectwhattheencoderhascaptured. Allfiguresshowing
renderedframesusethisdecoder. ItistrainedafterJEPApre-trainingandplaysnoroleinthecuration
pipeline.
2.4 TrainingRecipe
Wepre-encodeandshardallframesinthedatasetasTAESDlatents. Performingthisforwardpass
exactlyonceperframenotonlysavesredundantcompute,butslashesI/Ocost,as(1)48×lessdata
is fetched per training step and (2) compressing the dataset allows us to fit all of the frames and
corresponding actions on disk, so that we don’t have to repeatedly fetch batches from our cloud
bucket.
LikeallJEPAarchitectures,LeCurationtrainingisself-supervised:thepredictor’soutputiscompared
againstastop-gradienttargetproducedbyaslowEMAcopyoftheencoder(EMAdecay0.9999).
Foraframeatarbitrarytimesteptinagameplaysequence,thelossiscalculatedas:
L=MSE(e ,eˆ )+λ·SigReg(e ) (1)
t−6:t t−6:t t
wheree andeˆ aretheworldstatesembeddedfromthegroundtruthhistoryandnextframes
t−6:t t−6:t
andtheworldstatesforthesameframesaspredictedbythelatentpredictor,respectively. SIGRegis
shortforSketchIsotropicGaussianRegularizer,whichpreventsrepresentationcollapsebypushing
the embedding distribution toward an isotropic Gaussian. We use the regularization coefficient
λ=0.09asrecommendedbytheLeWMauthors. Nolabels,nocollisionannotations,nophysics
supervision—justgameplayvideoandactions.
Therearetwostagesoftrainingforthelatentencoderandpredictor.
• First, we pre-train the encoder on randomly sampled frame-action pair sequences, asking the
encoder to find the world state of 6 history frames and the predictor to predict only the next
immediateworldstate. Thisallowstheencodertoforminitialrepresentationsforthetrainingdata.
• Next,wedosupervisedauto-regressivepost-training,where,startingfromawindowof6frames,
weaskthepredictortoauto-regressivelyrolloutwordstatesforthenext50frames,comparing
themwiththeworldstatesencodeddirectlyfromthegroundtruthframes. Weuseadiscountfactor
of1.03toemphasizeframesfurtheraway. Thissignificantlyimprovesthequalityoflongerrollouts
fromthepredictor,andalsoallowstheencodertorefineitsworldstateembeddings.
Nopartofthemodelisfrozenineitherofthesetwostages. Pre-trainingtakes120minutesfor300
epochs,andpost-trainingtakes60minutesfor20epochs. Wedefineanepochtobe1600batches,
ratherthanafullpassthroughtheentiredataset. Pre-trainingbatchsizeis32andpost-trainingis
16. Abatchdenotes7frame-actionpairsinpre-training(6historyframes+1currentframe)and56
frame-actionpairsinpost-training.
FortheDiTdecoder,weembeddedTAESDlatentsfromthedatasetasworldstateswiththetrained
latentencoder,andtrainedthedecodertogeneratetheTAESDlatentsconditionedoneachworld
state. Thisway,theDiTdecoderperformanceisunabletoaffecttheworldmodelquality. Thisstep
wasalsoveryfast(30minsfor600epochs).
4

2.5 DatasetandCompute
ThedatasetinourexperimentsinthispaperiscomposedofCS:GOgameplayrecordingsofvarious
skilllevelsrestrictedexclusivelytothede_dust2map. Thedatawasprovidedanonymouslybyour
datapartner. Bothframesandkeypressesaresampledat16Hz. Nocurationorepisodefilteringis
appliedattrainingtime;themodelcanbeusedforcurationapplicationsafterbeingtrainedonthe
full,uncuratedset. TheideaistotrainLeCurationonanytrainingcorpusandthenapplyittocurate
sample-efficienttrainingsets.
Allexperimentswereconductedonaruntimewitha40GBNvidiaA100GPUaccessedthrough
GoogleCloudPlatform(GCP).OurdatawasalsostoredinGCPbuckets.
3 Evaluation: EmbeddingandPredictorQuality
We qualitatively evaluate the embedding and predictor outputs in the context of addressing the
commondatacurationchallenges.
3.1 SortingtheDatasetbyClusteringEmbeddings
WeextractedonemillionCLSembeddingsfromthetrainingcorpusandranUMAP+HDBSCANto
clusterthem. Theclusterscorrespondtorecognizablegameplaysituations—longopensightlines,
close-quarterinteriors,smoke-obscuredviews,playersilhouettesatdoorframes—withoutanyseman-
ticlabelshavingbeenprovided. Theself-supervisedpredictionobjectivehasorganizedthespaceby
content,notbypixelstatistics.
Thisclusterstructureprovidesdirectcurationprimitives. Rebalancing: over-representedclusters
(commoncorridorwalks,staticstandoffs)canbedownsampledatepisodeselectiontimetoimprove
trainingdiversity. Degenerate-contentfiltering: clusterscorrespondingtoloadingscreens,spectator
views,andscopeviews(thefirstrowofFigure2)orheavilycompressedframescanbeeasilyfiltered
out,withoutper-framelabels.
3.2 Auto-regressiveNearest-NeighborRetrieval
Totestwhethertheembeddinggeometryismeaningfulindependentlyofthegenerativedecoder,we
rananearest-neighborretrievalexperiment. Ateachstepofanauto-regressiverollout,insteadof
renderingthepredictedembeddingwiththeDiT,wesnapittoitsnearestneighbor(byEuclidean
distance)inthe1M-framesubsetofourtrainingdata. Wedecodeandappendthecorresponding
TAESDlatentthroughtheVAEdirectlytogeneratethevideo. Iftheembeddingspaceiscoherent,
theretrievedframeshouldbevisuallyconsistentwithwhatthemodelpredicted.
The retrieved frames match the ground-truth sequence in scene context, player orientation, and
lighting—thepredictor’soutputlandsnearrealframesshowingtherightkindofgameplaysituation
2. Thisconfirmsthat(1)theembeddinggeometrycapturesgenuinesemantics,and(2)a1M-frame
database is dense enough to serve as a retrieval corpus. It also suggests a lightweight curation
primitive: selectingtrainingframesbyproximitytoatargetembedding,withoutrunningtheDiTat
all.
Studyingtheworldstateswithnearest-neighborretrievalallowedustofindsomeofitsweaknesses.
A major weakness is that the weapon in the player’s hand is often misrepresented. This can be
seeninthethirdrowofFigure2,wherethelocationandcameraanglesoftheclusteredframesare
obviouslythesame,buttheweaponisnot. Whenplayinganauto-regressivelypredictedsequence
of nearest-neighbor snapped frames, the weapon type often flickers in the player’s hand. This is
likelybecausetheweapontakesupsignificantlylessspaceonthescreenthanthesurroundingscene,
meaningithasamuchsmallereffectonthefinallossvalue. Also, theactioninputsthatinvolve
theweapon,firing,andswitching,aremuchlesscommonthanmovingaroundandturning. Thisis
thekindofresultthatprovestheusefulnessoftrainingasmallscoutmodel. Ifweweretotraina
largermodelafterwards,wewouldknowtocreateacuratedfinetuningsetthatoversamplesweapon
switchesandfiringtoimproveaccuracyinthisaspect.
2https://drive.google.com/file/d/1p-f8nqGOt85z5uXaiNs9Cu-JBPv1rJ1l
5

Figure2: FramessampledfromthedatasetafterHDBSCANclustering. Eachrowisonecluster
of world states in the latent space. Visual coherence within rows and clear differences between
rowsconfirmthatthelearnedembeddingsrecoversemanticallymeaningfulgroupingsofgameplay
footagewithoutanymanualannotation. Additionally,thefirstrowdemonstrateshowwecansiftout
anomalousclusters(in-scopeviews)withouthavingtosearchforthemspecifically.
3.3 UsingClustersforCoverage-BasedCuration
Weusedtheper-episodeembeddingcentroidstoselecttrainingepisodesbyfarthest-firsttraversal
(maximizingspreadinthe196-dimensionalspace). Byconstruction,coverage-maximizingselection
producesamorediversetrainingcorpuswithlessredundancythanrandomsampling. Wehavenot
yettrainedadownstreamworldmodelonthesesubsets,sowedonotyetknowwhetherthistranslates
intocomparabledownstreamqualityatareducedtrainingbudget;validatingthisisthemostimportant
openquestionraisedbythiswork(seeSec.5).
Rare-trajectory upsampling selects episodes occupying sparse embedding regions (high average
distancetok-nearestneighbors). Theseframesrepresentsituationsthemodelhasseenfewexamples
of, and we hypothesize that they would carry disproportionate training signal for a downstream
modelifupsampled;wehavenotyettestedthishypothesis. Weplantosharetheresultsoftraininga
largerworldmodeloncoverage-andrarity-curatedsubsets,comparedagainstrandom-samplingand
full-corpusbaselines,infuturework.
4 PredictorQualityandAnomalyDetectionviaEmbeddingDivergence
Thepredictor’susefulnessforcurationgoesbeyondproducingembeddingsforretrieval. Thevideoin
Figure3iscreatedbystartingwithaqueueof6groundtruthframes,encodingthemwiththelatent
6

encoder,andauto-regressivelygeneratingworldstatesuntiltheendofthegroundtruthclip. Each
worldstateisdecodedbytheDiTtogeneratethevideo. Duringauto-regressiverollout,wetrack
theEuclideandistancebetweenthepredictor’soutputandtheworldstateencodeddirectlyfromthe
ground-truthframeateachstep:
d =∥eˆ −e ∥
t t t 2
whereeˆ isthepredictor’sforecastande istheworldstateoftheactualobservedframeatstept.
t t
Whentherolloutproceedsnormally—predictablecameramotion,standardplayermovement—d
t
stays low. When the rollout reaches a frame that differs substantially from what the predictor
expected, d spikes. We interpret these spikes as candidate moments of surprise: abrupt events,
t
unusualtrajectories,orphysicalinteractionsoutsidethemodel’slearneddistribution. Wenotethata
spikeisnotonitsowndiagnosticofthecause: itcanalsoarisefromaccumulatedrollouterroror
fromout-of-distributionactions,andwehavenotyetdefinedaquantitativethresholdormetricfor
distinguishingthesecasesorforselectingwhichhigh-d framestodiscardversusoversample. We
t
treatd asacandidatesignalforfurtherinvestigationratherthanavalidatedcurationrule,anddiscuss
t
thislimitationfurtherinSec.5.
Figure3: Animatedembeddingdivergenceduringautoregressiverollout. Left: ground-truthCS:GO
frame. Center: EachpredictedworldstatedecodedbacktoanRGBframeusingtheDiT.Right:
Euclideandistanced =∥eˆ −e ∥ .Spikesidentifyframeswherethepredictor’sexpectationdiverges
t t t 2
fromreality,providinganunsupervisedanomalysignalderivedentirelyfromtheworldmodel’sown
predictions.
Figure3showshowthelatentpredictor’sworldstatesdivergewhenarareorconfusingsetofactions
istaken3. Thesceneteleportstoadifferentpartofthemap,butsnapsbacktothecorrectlocation
afterabout350frames. ThisperiodofdivergenceisclearlyvisibleonthegraphinFigure3.
This anomaly signal is entirely learned. It emerges purely from the gap between predicted and
observedembeddings. Frameswithhighd arecandidatesforanomaly-basedcuration: eithertobe
t
excluded(iftheyrepresentdegenerategameplay)oroversampled(iftheyrepresentrarebutphysically
meaningfulinteractionsthatamorerobustdownstreammodelneedstocaptureaccurately).
Thepredictiveworldmodelisitselfthedetector: anythingthatsurprisesthepredictorregistersas
highd . Thecurrentlimitationisthatthesignalisnotphysics-specific. Aplayertakinganunusual
t
path,anabruptcutintherecording,andagenuinewall-collisioneventallproduced spikes. Isolating
t
physics-causeddivergencefromothercauses—suchaseliminatingsceneswithdoublejumps—would
require a model pretrained on a wide corpus of real-world data, not just gameplay data, and is a
directionforfuturework.
5 DiscussionandLimitations
Thecentralclaimofthisworkisthatasmalldomain-trainedpredictiveworldmodelisausefultool
fordatacuration. Theencoder(2Mparameters)andpredictor(13Mparameters)togetherrepresenta
tinyfractionofthedownstreamDIAMOND-style(Alonsoetal.,2024)worldmodeltheyarecurating
datafor. Yettheyprovide:
• Asemanticallyorganizedembeddingspacethatclustersgameplaybycontentwithoutlabels.
• Aqualitativesignalofwhichaspectsofthedataneedtobeoversampledforalargerdownstream
model.
3https://drive.google.com/file/d/1vbJ9v4vKoFvI21PR7D1jFkBlQbWtAGWc
7

• A learned, dataset-specific anomaly signal from embedding divergence during autoregressive
rollout.
Thecostofrunningthiscurationmodeloverthefulltrainingcorpusisnegligiblecomparedtotraining
thedownstreamworldmodel. Embeddingextractionisasingleforwardpassperframe;anomaly
scoringisanadditionalforwardpassofthepredictor. Bothcanbecachedandreusedacrossany
numberofdownstreamcurationexperimentswithoutretraining.
Themainlimitationisphysicsspecificity: theembeddingsandpredictionsencodeappearanceand
motioncontinuity,notphysicalplausibility. Closingthatgap—movingfromamodelthatdetects
whatisvisuallysurprisingtoonethatdetectswhatisphysicallyimplausible—isanaturalnextstep
andthesubjectofongoingwork.
Additionally,wewanttotestthecapabilitiesofthismodelonalargerandmorevariedset,preferably
fromrealworlddataratherthangameplay. Anidealdatasetwouldberoboticmanipulationcorpora,
whichhavevideoandexactrobotactionsforawidevarietyoftasksandsettings. Thiswouldpresent
amuchgreaterchallengetotheLeCurationmodelandshowitsfullpotentialfordatacurationin
thephysicalAIspace. Weareconfidentthatourapproach,oncerefined,canintroduceaparadigm
shiftinthesourcingandcuratingofdataforalltypesofmodels,andweareexcitedtoseewherethe
industrytakesitfromhere.
References
LucasMaesetal.LeWorldModel: StableEnd-to-EndJoint-EmbeddingPredictiveArchitecturefrom
Pixels.arXiv:2603.19312,2026.
Robin Rombach et al. High-Resolution Image Synthesis with Latent Diffusion Models.
arXiv:2112.10752,2021.
Ollin Boer Bohan. Tiny AutoEncoder for Stable Diffusion. https://github.com/madebyollin/taesd,
2023.
YannLeCun.APathTowardsAutonomousMachineIntelligence.OpenReview,2022.
MahmoudAssranetal.V-JEPA2: Self-SupervisedVideoModelsEnableUnderstanding,Prediction
andPlanning.arXiv:2506.09985,2025.
HeejeongNametal.Causal-JEPA:LearningWorldModelsthroughObject-LevelLatentInterventions.
arXiv:2602.11389,2026.
HaoranZhu,AnnaChoromanska.Self-SupervisedJEPA-basedWorldModelsforLiDAROccupancy
CompletionandForecasting.arXiv:2602.12540,2026.
EloiAlonso,AdamJelley,NicolasVincent,ThomasMatthews,SamDevlin,andVarunKompella.
DiffusionforWorldModeling: VisualDetailsMatterinAtari.AdvancesinNeuralInformation
ProcessingSystems(NeurIPS),2024.
A ComparingNearest-NeighborRetrievalandDiTOutput
The DiT was designed to be completely separate from the core world model, namely the latent
encoderandpredictor,andserveonlyasavisualizationtool. WefoundthataDiTwasnotstrictly
necessaryasavisualizationtooloncethemodelsawenoughofourdata. Atthatpoint,wefoundthat
wecouldrandomlysample1millionframesfromourdatasetandcreateanearestneighborretrieval
indexfromtheirworldstateembeddings. Bysnappingautoregressivelygeneratedworldstateswith
theirnearestneighboraswedidinSection3.2,wewereabletocreatemoreinterpretablerollout
videos(mainlybecausetherealframesfetchedfromthedatasetwereclearerthanthosegeneratedby
theDiT).
Thisallowedustobetterunderstandsomeofthedivergencepoints. Forexample,ifthegroundtruth
videoshowedafellowplayerpassingbyandobscuringalargesectionofthescreen,thiscouldcause
adivergence. TheDiTwouldnotbeabletoclearlydepictthepassingplayer,assuchsceneswere
rareinitstrainingdata.
8

However,forfuturework,wewouldrecommendusingbothaDiTandnearest-neighborretrievalto
understandgeneratedvideo. Nearest-neighborretrievalonlyworkedwellforthisdatasetbecauseall
thescenescomefromthesamerelativelysmallandclosedmap(de_dust2). Itmaystillhelpmake
interpretablegeneratedvideosinothercases,butwithamorevarieddatasetaDiTwouldbehelpful
indecodingandinterpolatingworldstatesthatrepresentricherdata.
B CodeandData
• Allcodeforthisprojectisavailableat: https://drive.google.com/file/d/1YDHDfSfwi6VOp4wXA
8OXajeyIgH5G39u.
• Theexactdatasetweusedisnotavailabletothepublic,asitwasprovidedtousbyananonymous
datapartner. However,averysimilarCounter-Strikedataset(fromthegameCounter-Strike2)in
theexactsameformatasourdatasetispublic: https://huggingface.co/datasets/TeaPearce/CounterS
trike_Deathmatch.
9