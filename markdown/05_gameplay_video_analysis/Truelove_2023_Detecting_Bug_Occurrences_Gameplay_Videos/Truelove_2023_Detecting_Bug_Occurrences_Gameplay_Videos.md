# **Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay** 

# **Videos** 

ANDREW TRUELOVE, Donald Bren School of Information and Computer Sciences, University of California, Irvine, USA 

SHIYUE RONG, Donald Bren School of Information and Computer Sciences, University of California, Irvine, USA EDUARDO SANTANA DE ALMEIDA, Institute of Computing, Federal University of Bahia (IC-UFBA), Brazil IFTEKHAR AHMED, Donald Bren School of Information and Computer Sciences, University of California, Irvine, USA 

The presence of bugs in video games can bring significant consequences for developers. To avoid these consequences, developers can leverage gameplay videos to identify and fix these bugs. Video hosting websites such as YouTube provide access to millions of game videos, including videos that depict bug occurrences, but the large amount of content can make finding bug instances challenging. We present an automated approach that uses machine learning to predict whether a segment of a gameplay video contains the depiction of a bug. We analyzed 4,412 segments of 198 gameplay videos to predict whether a segment contains an instance of a bug. Additionally, we investigated how our approach performs when applied across different specific genres of video games and on videos from the same game. We also analyzed the videos in the dataset to investigate what characteristics of the visual features might explain the classifier’s prediction. Finally, we conducted a user study to examine the benefits of our automated approach against a manual analysis. Our findings indicate that our approach is effective at detecting segments of a video that contain bugs, achieving a high F1 score of 0.88, outperforming the current state-of-the-art technique for bug classification of gameplay video segments. 

### **ACM Reference Format:** 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed. 2023. Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos. 1, 1 (November 2023), 23 pages. https://doi.org/10.1145/nnnnnnn.nnnnnnn 

## **1 INTRODUCTION** 

The video game industry is a multi-billion dollar industry, expected to exceed $211 billion in revenue by 2025 [34]. Illustrating this fact, in 2018, the video game _Grand Theft Auto V_ was the most profitable media title of all time, having earned an estimated $6 billion in revenue [16]. Due to such financial impact, presence of bugs in these video games are consequential for developers. For example, when development studio CD Projekt Red released _Cyberpunk 2077_ in December of 2020, the prevalence of bugs led to a widespread negative reception [10], the removal of the game from digital storefronts [19], and a 41% drop in the company’s stock price [25]. 

Authors’ addresses: Andrew Truelove, Donald Bren School of Information and Computer Sciences, University of California, Irvine, Donald Bren Hall, Irvine, CA, USA, 92697-3425, truelova@uci.edu; Shiyue Rong, Donald Bren School of Information and Computer Sciences, University of California, Irvine, Donald Bren Hall, Irvine, CA, USA, 92697-3425, shiyuer@uci.edu; Eduardo Santana de Almeida, Institute of Computing, Federal University of Bahia (IC-UFBA), Avenida Milton Santos, s/n - Ondina Campus, PAF 2, Salvador, Bahia, Brazil, 40.170-110, esa@rise.com.br; Iftekhar Ahmed, Donald Bren School of Information and Computer Sciences, University of California, Irvine, 2438 ISEB, Irvine, CA, USA, 92697-3440, iftekha@uci.edu. 

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. 

© 2023 Association for Computing Machinery. 

Manuscript submitted to ACM 

Manuscript submitted to ACM 

1 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 

2 

To avoid these kinds of negative impacts, it has become common practice for game developers to apply updates to their games in order to fix bugs after the game is released; for example, over one third of the big-budget games released in 2014 received a day-one update [33]. This is because games can be complex, with “enormous alternative ways that players can execute the software, differently from individuals using a software with a well-defined number of actions” [39]; this complexity can lead to difficulties in thoroughly testing for all possible bugs. As such, game developers have become increasingly interested in leveraging gameplay videos to help identify bugs that have persisted into a game’s release [29]. Gameplay videos are useful for developers, because they offer a wide range of information such as the state of the game at the time a bug appeared, the audio content at the time of the bug, the visual content at the time of the bug, etc. [29]. Gameplay videos are often easily accessible as well; video hosting services such as YouTube [4] and Twitch [3] allow users to upload, stream, and view gameplay videos, including videos depicting the occurrences of bugs [29]. Gaming videos are particularly popular on these sites; 2020, for example, saw the number of active gaming channels on YouTube surpass 40 million [49]. While these videos can provide developers with useful information about bugs, the large amount of video content on sites like YouTube create difficulties in locating relevant footage of bug incidents [29]. Aside from the quantity of videos available on the platform, there is also the issue of individual video length. For example, the most liked non-live gaming video on YouTube in 2020 was over 18 minutes long [21, 49], and prior research on the Twitch video platform found that gameplay videos from popular streamers frequently lasted between “two and eight hours in length” [41]. In cases like these, it is not enough to know that a video contains a bug. Rather, a developer needs to know when the bug actually occurs. Otherwise, they would need to watch the video in its entire duration to locate the bug, which becomes burdensome when multiple videos with long lengths are involved. 

In this paper, we propose a novel automated approach to split a video of gameplay into smaller segments and predict which segments depict the occurrence of bugs. We also perform a preliminary analysis to explain which characteristics of the video frame images are more likely to have an association with the occurrence of bugs. Our approach improves upon prior work by Guglielmi et al., which focused on devising an approach to identify segments of YouTube videos that depict anomalies in gameplay videos and classify the segment based on whether it contained the presence of a game bug [22]. While their approach relied on the presence of certain keywords in the video’s transcript to locate relevant buggy segments, our approach is able to identify and classify segments regardless of the content of the transcript text. Additionally, our classifier outperforms their best-performing classifier configuration when run on our dataset of video segments. 

In addition to the classification task, we also perform the novel task of conducting an analysis on frames from the bug-depicting segments in our dataset to identify characteristics of gameplay videos that appear to have an association with bugs. Developers are more likely to use a machine learning tool if they feel they can trust the model, and the ability to explain a model’s predictions is an important aspect of establishing that trust [36]. Additionally, determining specific objects or behaviors from these video segments can inform developers on what kinds of game scenarios may be particularly bug-prone. This knowledge can be used to investigate additional videos that depict similar material and to bolster testing to better target these scenarios. In our analysis, we wanted to identify the elements from the video frame that a model believed to be important in making a prediction, the relationship between those highlighted elements and the depicted bug, and the characteristics and patterns that the model seemed to pick up on more frequently. 

For our study, we selected 198 buggy game videos from YouTube and automatically split them into 4,412 video segments. We extracted textual transcript information and visual information from these segments for use as features, as these features have been used for video classification tasks in prior research [9]. We train a collection of neural network-based classification models with the aim of predicting whether a video segment shows the occurrence of a Manuscript submitted to ACM 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 

3 

bug. Additionally, we evaluated the models on subsets of our dataset containing only video segments from games of the same genre as well as datasets where all segments were from the same game. We also run the technique by Guglielmi et al. on all our datasets as a baseline and compare its performance with the performance of our classifiers. We then analyze video frames in our dataset using LIME superpixel explanations [36] in order to identify characteristics of game images that can help explain the classifier’s prediction. Finally, we conduct a user study to evaluate the benefits of our framework when compared to manual analysis. 

Our research questions are as follows: 

**RQ1** : How well does our tool perform in predicting bug occurrences in gameplay videos? 

**RQ2** : How does the tool perform when trained on footage from different genres of video games? 

**RQ3** : How does the tool perform while predicting bug occurrences across games? 

**RQ4** : Is it possible to identify which characteristics of visual video frames have an association with the prediction of a bug? 

**RQ5** : What benefits are brought to developers using our tool in identifying buggy gameplay segments in videos over a manual analysis? 

The rest of our work is structured as follows. In Section 2, we review related works that are similar to our research problem. In Section 3, we describe the process of developing our automated bug identification approach approach, including our data preparation procedure (3.1), our classification models used with the different training sets (3.2), our superpixel explanations (3.3), our video attributes (3.4), and our user study (3.5). Then, in Section 4, we present the results to our research questions, including the evaluation of our different bug identification models. Section 5 provides a discussion of our findings, including implications for both researchers and practitioners. We go over threats to validity in Section 6, and finally, we present our conclusions in Section 7. 

Our contributions in the paper are as follows: 

- An automated tool that uses machine learning to predict whether a segment of a gameplay video contains the depiction of a bug through the sole use of features from the video itself. 

- A dataset comprised of 4,412 gameplay video segments from 198 different game videos. 

- An analysis of characteristics from the gameplay videos that help explain which characteristics are likely to have an association with bugs. 

## **2 RELATED WORK** 

Prior work has focused on analyzing game videos in order to extract particular information, including information relating to bugs. For example, Lin et al. developed a method to identify game play videos that showcase bugs; their method involved an analysis of metadata for videos on both YouTube and Steam [29]. Their method was was able to achieve precisions of over 0.90 when evaluated on a set of 1,400 known buggy videos [29]. Lewis et al. created a taxonomy for video game bugs by examining online game play videos and reading online articles related to game bugs [28]. Amiriparian et al. developed a technique to analyze game audio from YouTube game videos with the purpose of identifying the genre of the game being played [7]. An evaluation of their method returned “an accuracy of up to 66.9% unweighted average recall using tenfold cross-validation” [7]. Shah et al. developed an approach for training a convolutional neural network model to generate automated commentary from a given input video [40]. They trained the model using features from YouTube videos–specifically, for each video they extracted the frame images from the video and the transcript of the video’s commentary [40]. Taesiri et al. developed a method for querying videos of game 

Manuscript submitted to ACM 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 

4 

bugs in order to match them with a relevant gameplay video from a dataset [46]. The approach involved taking a textual input query describing a particular object or event; the approach then identified image frames in the dataset with a high similarity score with the query, returning the videos that were most likely to depict they subject of the query [46]. The authors’ proposed this technique could be used to search for and identify gameplay videos that depict certain types of bugs (i.e., a query asking for “a person stuck in a horse’ returns a video depicting that specific type of bug) [46]. Guglielmi et al. introduced GELID, an autommated approach to extract segments from gameplay videos related to bugs [22]. To approach is designed to return meaningful video information by (i) extracting relevant segments of a video likely to contain a bug, (ii) automatically classifying the segments as informative or non-informative with respect to the presence of a bug (as well as, in the informative case, the type of bug being depicted), and (iii) groups the segments based on the context in which the bug appears (e.g., the game location or level), as well as (iv) grouping based on the type of bug being depicted [22]. While GELID was able to identify informative segments, their classifier was only able to achieve an average F1 score of 0.63 for binary bug classification across their test datsets, which the authors concluded were not satisfactory results [22]. 

Our work is distinguishable from these works in the sense that none of these works seek to identify the timestamps at which bugs appear in gameplay videos. Amiriparian et al. and Shah et al. were interested in problems other than game bugs [7, 40]. Lewis et al. looked at the types of bugs that appeared in gameplay videos, not when they appeared [28]. Taesiri et al. focused on returning videos that depicted the objects or events requested in the query, but their approach did not return information about when exactly in the video the queried information appeared [46]. Additionally, the approach was specifically evaluated on a specific type of bug–’game physics’ bugs–and its effectiveness on identifying other types of bugs was not examined [46]. Our approach is not strictly intended with a particular type of bug in mind. While Lin et al. were also engaged in identifying the presence of bugs in game videos, their identification method primarily determines whether a video showcases a bug and does not provide any time specification information [29]. A two-minute video and a two-hour video could return the same positive result, requiring a manual analysis of the video to identify when the bug appears [29]. Additionally, the features used for their classifier were extracted from video metadata, which included the video title, description, and tags [29]. While this approach can help developers identify videos that might showcase a bug, the method is lacking when that metadata is absent or unrelated to bugs, such as in the case of a video in which a bug appears in gameplay, but it is not necessarily the main focus of the video. By contrast, our approach used features directly from the video itself, meaning that extraction of additional metadata is not necessary. 

The work by Guglielmi et al. is likely the closest work to ours, since it is also focused on automatically identifying bugs from segments of gameplay videos as one of its steps [22]. Our work can be distinguished in a few ways, however. First, the process they used for their classification involved discarding or excluding segments that did not contain certain keywords in their transcripts from their data [22]. As such, their approach may not be geared towards handling segments lacking these keywords. On the other hand, our approach is designed so that it can process video segments regardless of the contents of the transcript text. Additionally, our work can be distinguished in the sense that we focused on using different models trained on specific subsets of video game segments, including a general dataset of segments, datasets containing only segments from the same game genre, and segments from the same individual game. While Guglielmi et al. tested their models on three datasets with each set containing segments from a single game, this generalized and genre-level analysis are not considered [22]. Finally, the authors acknowledged that the performance of the binary GELID classifier was not satisfactory, achieving an average F1 score of only 0.63 for the positive class across 

Manuscript submitted to ACM 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 

5 

the three game-level test sets and a top F1 score of 0.68 [22]. The authors state the need for future research to devise improved techniques that can yield more satisfactory results [22]. 

Some research on game videos has looked specifically at identifying the occurrence of certain events in the videos. Ringer et al. created a technique to detect highlights from video game streams by analyzing both game footage and footage of the streamer as they played [37]. They found that this combination of features was able to effectively identify highlights in game streams for the game _Player Unknown’s Battlegrounds_ [37]. Roohi et al. created an annotation system to detect the emotions of game streamers over time through a neural network-based analysis of “facial expressions, video transcript sentiment, voice emotion, and low-level audio features (pitch, loudness)” and achieved accuracy scores that reached as high as 70.7% [38]. Song et al. created a database of audiovisual data relating to player frustration when playing a game [42]. The authors extracted these features from recorded footage of participants playing a game and created a model to automatically detect moments of player frustration [42]. This model achieved an unweighted average recall score of 60.3% [42]. 

These works are distinguished from ours in the sense that none of them are searching for occurrences of bugs. Additionally, these works all incorporated footage of the player on some level into their techniques, which is not required for our approach. 

Cooper et al. devised a technique to detect duplicate bugs within video-based bug reports [17]. Their technique was able to identify “duplicate video-based bug reports within the top-2 candidate videos for 83%” of the evaluated tasks [17]. This work differs from ours in a couple of ways. First, the technique presented in this paper is not specific to games; it was evaluated on a set of six Android apps from a variety of categories such as productivity and finance [17]. Second, the purpose of this technique is duplicate detection; rather than identifying whether a given video contains a bug, it instead returns a ranked list of other videos, where higher ranked videos “are more likely to show the same bug” as the input video [17]. 

An additional body of research has explored bug identification and prevention in the domain of video games. Truelove et al. expanded on the bug type taxonomy created by Lewis at al. [28] and investigated the types of bugs that are fixed in game updates [47]. They also surveyed game developers about the challenges they associated with the appearance of bugs [47]. Survey respondents mentioned difficulties with reproducing bugs [47]. Looking at the issue of load testing video games, Tufano et al. implemented reinforcement learning to “train an agent able to play the game as a human” in order to identify bugs, particularly bugs related to drops in game performance [48]. They found that their trained model was able to outperform a model that was only trained to play the game [48]. 

Our work is distinct from these works in the sense that neither work investigates gameplay videos. Truelove et al. focused on bugs described in game updates rather than on bug identification [47]. While Tufano et al. looked at bug identification, this identification was done through the use of a reinforcement learning agent to simulate a human tester rather than through any video analysis [48]. 

## **3 METHODOLOGY** 

The following sections detail the research methodology of our study. Section 3.1 explains the video data we collected and the feature extraction techniques we applied. Section 3.2 describes the classification models we created. Section 3.3 looks at an analysis of the videos we examined, and Section 3.4 describes our user study. Figure 1 shows a summary outline of our methodology. 

Manuscript submitted to ACM 

6 

- Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0006-02.png)


<!-- Start of picture text -->
Data Preparation Classification Models Evaluation<br>Video Collection RQ1:Combined Feature<br>Data Importance<br>Video RQ2: Game RQ4: Superpixel<br>Segmentation Genres Explanations<br>ExtractionFeature Action Sports RQ5: User Study<br>Transcript Visual RQ3: Single<br>Games<br>Ark: Survival FIFA 17<br>Evolved<br><!-- End of picture text -->

Fig. 1. An outline of our methodology 

## **3.1 Data Preparation** 

_3.1.1 Video Collection._ Our dataset that we used to train and test our classification models was comprised of game play videos uploaded to YouTube. Prior work from Lin et al. had provided a dataset of online videos that showcased a bug [29]. We extracted the YouTube videos from this dataset for our study. Additionally, we also found a selection of bug videos from a cursory search of YouTube. This cursory search was performed through a simple keyword search, using terms that Lin et al. found to have a relation with bugs in games in their study [29], including “’bug”, “glitch”, and “hack”. Combining the videos from these two sources gave us an initial body of 891 game play videos. We then took a randomly selected sub-sample of these videos. Using a 95% confidence interval with a 5% margin of error, we selected 269 videos. 

The next step was to divide the videos into segments. This division helped better identify the time in a video at which a bug appears, since using a model to classify a segment provides a more specific time frame than classifying the entire video. A segment also provides a possible start time and end time that would be found with a buggy segment as described by Lin. et al in their discussion of future work in bug identification in game videos [29]. When it came to how to divide the videos into segments, we looked to YouTube’s video caption feature. YouTube allows users to add captions to their videos; the uploader of a video can either create the captions manually, or they can use YouTube’s auto-caption feature to automatically generate captions from the video’s speech [35]. If captions are enabled, users will see the captions appear on the screen as they view the video [35]. In addition to displaying the captions on the video, users also have access to a pane on the video page that lists a transcript of all captions in the video, which are paired alongside the timestamps at which the captions appear [23]. Figure 2 shows an example of this caption transcript as it appears on the YouTube page for one of the videos from our dataset [43]. Users can utilize this pane to download the transcript information for videos [23]. 

Because we wanted to use the transcripts of a video as a feature in our classifier, we decided to split our videos into smaller video segments based on the timestamps of the captions (see Section 3.1.2 for a deeper explanation of the transcript features, including the rationale for their inclusion). For the video from Figure 2, we split the video so that the first segment ran from the start of the video to the 0:06 mark, the second video segment began at the 0:06 mark and ran until the 00:13 timestamp, and so on. We decided to establish a minimum length of five seconds for each video Manuscript submitted to ACM 

7 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 

segment in our dataset. In the event that a segment was less than 5 seconds, we combined it with the shortest adjacent segment. This was done iteratively to account for instances in which a newly combined segment was still less than 5 seconds long. 

Since not all videos on YouTube make use of captions, however, we could not rely on YouTube as the sole source for video transcripts. For videos with no provided captions, we used Otter.ai, a service that automatically generates captions for videos [1]. Past research evaluating Otter’s caption generation have reported high levels of transcript accuracy for videos, reaching as high as 99.7% [32]. Uploading videos to Otter.ai produced transcripts documents similar to those from YouTube, each one consisting of a timestamp and the words spoken at that time. We used the timestamps from the Otter transcripts to split the videos in the same way done for the videos with YouTube captions. 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0007-04.png)


<!-- Start of picture text -->
Transcript<br>0:00 yes please you drop it down uh Mac no<br>0:06 I'm not near you I'm in the Couture<br>0:08 I'm sure you down south when we get in<br>0:13 onebuildingvillageyeahIseetherock<br>0:22 ohwhere did thatcomefrom sleepboy<br>0:27 fromtheleftall rightwe'reready<br><!-- End of picture text -->

Fig. 2. YouTube Transcript Example 

One of the authors and two students then labelled the segments in our dataset based on whether the segment depicted the occurrence of a bug. Out of the 4,412 labelled segments in the dataset, there were fewer than 20 instances of disagreement. During the course of our labelling, we discarded videos from our dataset that did not actually contain any gameplay footage, and videos that were no longer publicly available on YouTube. In all, we ended up collected and labelling 4,412 video segments from 198 videos. 

_3.1.2 Feature Extraction._ Our features came from two different information sources: the video transcripts and the visual data from the video images. 

**Video Transcript Features:** Prior research has incorporated video transcripts as a feature source for video classification tasks (e.g., [13, 22, 30]). To process the transcript text into our feature set, we followed the approach taken by Shah et al., who used the Universal Sentence Encoder [12] to encode the transcript text of YouTube videos into 512-length numerical vectors [40]. Though Shah et al. used these features to train a generative model rather than a classifier, we followed their approach because the the source of textual features they used were highly similar to ours; the authors also collected the transcripts of YouTube videos and used the provided timestamps to split the transcript text into phrases [40]. We used the Universal Sentence Encoder to encode the transcript text of each video segment into a 512-length numerical vector. Each element in the vector was treated as an individual feature for our classifier. 

Manuscript submitted to ACM 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 

8 

**Visual Features:** Our process for extracting the visual features from the video segments was broadly modeled after the process utilized by Cooper et al., who used visual features for the task of duplicate detection in videos of bug reports, and were able to identify duplicates within the top-2 ranked candidate videos for 83% of tasks [17]. Our process follows the general steps they used and involves extracting and comparing frame images from our video dataset with one another. First, we extracted frame images from all the video segments at a rate of one frame per second. For each frame, we then used SimCLR [15], which was also used by Cooper et al. [17], to extract feature information from the image. More specifically, the output of the SimCLR feature extractor for every image is a vector of length 64. 

While it would be possible to use these extracted vectors as features directly, these vectors represent individual frames, and our classifier was intended to work on segments of a video, i.e., on a sequence of multiple frames, meaning we needed a way to aggregate these frame vectors to represent the entire video segment. Following the example of Cooper et al., we combined a Bag-of-Visual-Words approach with a TF-IDF approach [17]. This approach has been shown to have work with high performance in prior papers [17, 27]. The frame feature vectors were clustered, and the centroids of these clusters were then used to represent a different visual word [17]. The frame image vectors in each video were then compared with the centroids, and through this we calculated a term frequency/document frequency measure for every centroid in the set. 

For our data, we used two different approaches to cluster our frame images. The first approach closely followed Cooper et al., where we simply used a _k_ -means algorithm to automatically generate our clusters and calculate the respective centroids. For our other approach, instead of using an automatic algorithm, we manually clustered our frames together so that all frames from the same video segment were grouped with one another. For the video segments that were labelled as depicting a bug, we manually examined the segment and extracted the frame in which the bug first manifests, and this frame was selected as that segment cluster’s centroid. We decided to manually cluster frames in the same segment together to better help our models compare the more nuanced characteristics of buggy and non-buggy frames from the same video segment. This approach also helped ensure that the centroid image actually corresponded to the occurrence of a bug. A bug is by definition a break from the intended game experience, which meant buggy frames were frequently outliers compared to the other frames in that segment under the automatic approach. Manually identifying buggy centroids ensured that our models would investigate the characteristics of these buggy frames. 

Once our cluster sets were formed, we indexed the video segments in our data by comparing each frame to the centroids in our sets. For each frame in a video, the feature vector was matched to the closest centroid using cosine similarity [50]. To obtain the final visual features, a TF-IDF calculation occurs for every centroid in the BOVW. Where the term frequency (TF) is the frequency at which a centroid image is matched with a frame in the specific video segment, and the inverse document frequency corresponds with the number of times the centroid matched with a frame in the entire data set [17]. This results in a vector for each video with a length equal to the number of clusters in the BOVW. When we manually grouped the frames by the segment, we ended up with 5,035 clusters. When using the automatic _k_ -means approach, we made sure to keep the same number of clusters for comparison. Each element of the vector was treated as an individual feature for the classification model. 

## **3.2 Classification Models** 

For our classification model, we made use of a number of different model types, including: 

- NeuralNetFastAI [24], 

- lightGBM [26], 

Manuscript submitted to ACM 

9 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 

- XGBoost [14], 

- Linear Model [6], 

- Random Forest [5], and 

- A Weighted Ensemble that combined all our model types through ensemble selection [11] 

We performed parameter tuning as well for our models, applying different learning rates, numbers of epochs, etc. We ran our classifier on our full dataset of all video segments, but we also wanted to see how a classifier would perform on smaller, more specialized datasets. The motivation for narrowing our focus in this respect was largely due to how diverse the game industry has become. The player view (any by extension, the visual and audio content) can vary significantly depending on the type of game being played. As an example, Figures 3 and 4 shows screenshots from two different games captured by videos in our dataset ([18, 20]). Figure 3 is from _Arma 3_ , and Figure 4 is from _NHL 16_ . In a game like _Arma 3_ , the player is given a first-person perspective from behind the player character. The player’s view is more-or-less constrained to the view of the player character. In a game like _NHL 16_ , however, the player view is high above the game world, allowing the player to see several characters at once. 

The differences in the player’s view between these games suggest that classification models using video features might perform better if they are trained and run on a subset of videos showing similar types of game play. In order to test this notion, we also trained and tested our models on different subsets of our dataset. The subsets are described in the following subsections. 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0009-08.png)


Fig. 3. _Arma 3_ Screenshot 

_3.2.1 Game Genres._ Out of the 198 videos in our dataset, 96 were for games that simulated a real world sport. The remaining 102 videos were from games that heavily revolved around combat, such as shooting or attacking with handheld weapons. As such, we split the games depicted in these videos to two categories: sports games and action games. Of our 4,412 total video segments, 2,772 segments were from sports games and 1,589 were from action games. We created two data subsets for each of these game genres. 

Manuscript submitted to ACM 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 

10 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0010-02.png)


<!-- Start of picture text -->
CFLY4WCS 4 3RD:25.4<br>POWERPLAY0:17<br><!-- End of picture text -->

Fig. 4. _NHL 16_ Screenshot 

_3.2.2 Individual Games._ Since we were already splitting our segment dataset by game genre, we were curious about going one step further and examining if it was possible to train and test models on a single game. Doing so could be useful for developers who only work with a single game. A model specialized on a single game may be better able to recognize the unique characteristics of that game. Two evaluate this question, we took the two primary game genres we identified and found the game within each genre with the most segments in our data. The sports game with the most video segments was _FIFA 17_ with 952 segments. The action game with the most video segments was _Ark: Survival Evolved_ with 694 segments. We extracted these segments and created two data subsets for each of these two games. 

## **3.3 Explaining Predictions** 

In addition to developing our classifiers, we also wanted to investigate the possible reasons why a classifier might decide to predict whether a video segment contained a bug. As such, we used LIME [36] to identify superpixels–the specific regions of pixels in the image that supposedly held importance to the classifier when it made its prediction [36, 44]. To generate these superpixels, we used the Inception v3 image model [45] and fine-tuned it using the training data that was used to train our classifiers. We then tested the model on the buggy video segments from our test set and generated the superpixel maps. We examined the resulting maps to identify possible patterns in the superpixel regions the model identified. These patterns might provide insights into what characteristics of an image seem to have an association with bugs. 

## **3.4 Video Attributes** 

Going back to Figures 3 and 4, the idea that differences between particular games or genres might affect the performance of our models led us to consider whether any of those differences might be apparent in other parts of our data. In that sense, we also decided to examine the bug occurrence patterns in our dataset of videos to investigate whether there was any relation between the type of game and the patterns in which bugs appear in videos. To further explore the characteristics of different genres of video games, we defined following five attributes for a single video: Manuscript submitted to ACM 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 

11 

**Total Number of Segments** : As explained in subsection 3.1.1, we divided videos into several segments based on the transcript and timestamp feature. This attribute counts the total number of segments of a game video after division. **Number of Buggy Segments** : Based on the prediction results, this attribute counts the total number of segments labeled as "showing bugs" for a single game video. 

**Buggy Segment Ratio** : To compare if one video is more likely to have a bug than other videos, we normalized each video’s count of buggy segments by its total counts of buggy segments. This attribute calculates the number of buggy segments divided by total number of segments, returning the buggy segment ratio for each video. 

**Start Time Ratio** : We also wanted to study if videos from different games varied regarding the time at which the first bug appeared (i.e., do bugs tend to appear earlier in action game videos than in sports game videos?). Identifying potential patterns in when bugs might appear can provide an additional layer of information to developers to supplement the identification models. The start time Ratio attribute calculates the start time of the first buggy segment divided by the total duration of the video. The units of time were in seconds. 

**Number of Gaps** . It is possible that consecutive buggy segments were talking about the same bug. Therefore, it was also important to identify discrete buggy segments in a video. To achieve this, this attribute counts the number of gaps between two subsets of consecutive buggy segments. For example, if a video has a labeled sequence 0 _,_ 1 _,_ 1 _,_ 0 _,_ 0 _,_ 0 _,_ 1 _,_ 0 _,_ 0 _,_ 1 and 1 indicates the buggy segments, the number of gaps will be 2 in this case, as there are two consecutive sequences with 0 bounded by 1. 

Based on the game genre categorization from subsection 3.2.1, our goal was to check if there was any difference for each attribute stated above between two genres. In total, we have 102 action games and 96 sports games. First, for each attribute, we checked whether their values were normally distributed using a Kolmogorov Smirnov test [31]. Since the p-values were all larger than 0 _._ 05, we concluded that all values were normally distributed. Then, we conducted the parametric two sample t-test to check if there was any difference between action games and sports games for each attribute. For _Start Time Ratio_ and _Number of Gaps_ , we excluded videos with no buggy segments, which resulted in 69 number of videos for both genres. Then, we followed the same procedure to check if the value of these two attributes are normally distributed, and then conduct the two sample t-test on each of them between action games and sports games. 

## **3.5 User Study** 

To evaluate the performance of our identification approach, we conducted a user study to examine the time and accuracy of humans manually searching for bugs. Participants were given a form containing five links to videos in our dataset. They were asked watch each video and to mark the start times and end times of any buggy moments they witnessed. All participants were graduate students. In total, we received 17 responses for each of the selected five links. 

For each video, we collected a list of start time and end time buggy segments pairs from the participants. Then, we mapped these buggy segments to the actual division of segments from subsection 3.1.1. To get the correct mapping, we checked if the actual buggy segment is the subset of one of the user inputted start time and end time pairs. If the user inputted time window is a subset of the actual buggy segment, we would also mark the time window of the actual buggy segment as buggy, so that the information would be consistent between user study and the mining result. Next, we followed the same calculation procedure of attributes stated in subsection 3.4. Since not all attributes are meaningful in this comparison, and there is an redundancy between _Number of Buggy Segments_ and _Buggy Segment Ratio_ in the correlation aspect. In general, we selected two attributes for statistical analysis: _Start Time Ratio_ , and _Buggy_ 

Manuscript submitted to ACM 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 

12 

_Segment Ratio_ . To compare user study and mining result on the selected five videos, we combined the study result from the 17 participants by calculating the average for each selected attribute grouped by videos. 

## **4 RESULTS** 

To evaluate the performance of our tool in RQ1, we took our dataset of 4,412 video segments we collected from Section 3.1.1 and randomly split the segments into a training set and a testing set. A portion of this training set was then excised and used as a validation set during the classifier training. When evaluating the tool’s performance on segments from specific game genres (RQ2) and for individual games (RQ3), we used the subset datasets described in Sections 3.2.1 and 3.2.2. Specifically, we created four subset datasets of our original dataset. For the genre analysis we created a dataset of _Action_ game segments and a dataset of _Sports_ game segments. For the individual game analysis, we created a dataset containing only video segments from the game _Ark: Survival Evolved_ and a dataset containing only video segments from the game _FIFA 17_ . We split each of these subset datasets into training and testing sets and ran them through our classifiers as well. 

As a baseline, we implement the technique from Guglielmi et al. called GELID and run it on our main dataset as well as each of the subset datasets [22]. Specifically, we run the segment classification step of GELID. Guglielmi et al. tested different configurations of features and classifiers on their test data [22]; we use the configuration that achieved the highest performance in their paper and evaluate this configuration’s performance on on our data. 

In this section we report our results for the research questions. 

## **4.1 RQ1: How well does our tool perform in predicting bug occurrences in gameplay videos?** 

Our goal was to identify bug occurrences from gameplay videos collected from YouTube. Table 1 shows the results of our classification models on our full set of test data. For the dataset using features from our manually designed segment clusters, the Linear Regression model performed the best, achieving an F1 score of 0.87. The automatically clustered dataset attained a marginally higher F1 score of 0.88, however. It achieved this score with the Weighted Ensemble model. These two classifiers both significantly outperform GELID, which only achieved an F1 score of 0.31 when run on our dataset. Our best-performing configuration outperformed GELID by 57 points. 

**~~�~~ � Observation 1:** The Weighted Ensemble model from the automatically clustered segment configuration achieved the highest performance with an F1 score of 0.88, outperforming GELID by 57 points. **~~�~~ �** 

## **4.2 RQ2: How does the tool perform when trained on footage from different genres of video games?** 

Table 2 presents the performance on the classifiers on the _Action_ games subset dataset and the _Sports_ game subset dataset. With the _Action_ models, the top performing model was the Weighted Ensemble model trained on the manually clustered dataset. This model achieved an F1 score of 0.84. For the _Sports_ models, the best performance was also from the Weighted Ensemble model, though this time it was the one trained on the automatically clustered dataset. This model earned an F1 score of 0.90. 

For the _Action_ models, the top models from the automatic dataset were NeuralNetFastAI and the Weighted Ensemble, which both achieved an F1 score of 0.64, though this is score is a full 20 points lower than the top model from the manual set. There was a noteworthy difference in the top _Sports_ models as well; the Linear Regression model that achieved a top F1 score of 0.80, which is still 10 points lower than the top manual model. All clustering configurations Manuscript submitted to ACM 

13 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 

|Technique|Best Model|F1|Precision|Recall|
|---|---|---|---|---|
||NeuralNetFastAI|0.77|0.67|0.91|
||LightGBM|0.78|0.95|0.67|
||XGBoost|0.38|0.57|0.28|
||Linear Regression|0.87|0.91|0.84|
|Manual Clustering|RandomForest|0.82|0.98|0.71|
||ExtraTrees|0.82|0.98|0.70|
||CatBoost|0.75|0.98|0.60|
||KNeighbors|0.64|0.62|0.67|
||Weighted Ensemble|0.84|0.80|0.88|
||NeuralNetFastAI|0.78|0.67|0.92|
||LightGBM|0.77|0.98|0.64|
||XGBoost|0.36|0.82|0.23|
||Linear Regression|0.86|0.93|0.80|
|Automatic Clustering|RandomForest|0.81|1.00|0.68|
||ExtraTrees|0.81|1.00|0.67|
||CatBoost|0.71|1.00|0.55|
||KNeighbors|0.61|0.66|0.56|
||Weighted Ensemble|**0.88**|0.91|0.85|
|GELID||0.31|0.34|0.28|



Table 1. Performance of the different classification on the full dataset 

for both genre subset datasets still outperform GELID, however, with the top _Action_ model outperforming GELID by 58 points and the top _Sports_ model outperforming it by 66 points. 

The performance of the top models saw modest improvement when moving from the full dataset to the _Sports_ games subset dataset, going from 0.88 in Table 1 to 0.90 in Table 2. On the other hand, there was a drop in the top model performance when going from the full dataset to the _Action_ game subset dataset, where the top F1 score was only 0.84. Using a model trained specifically on video segments from within a single game genre did not appear to lead to a universal performance boost when tested on other video segments from the same game genre. 

**~~�~~ � Observation 2:** For the _Action_ game subset dataset, the top-performing model achieved an F1 score of 0.84. For the _Sports_ games, the top model achieved an F1 score of 0.90, outperforming GELID by 58 points and 66 points, respectively. **~~�~~ �** 

**Video Attributes** : We also wanted to check if there was any difference between the video attributes between action and sports games (see Section 3.4 for details). We found that there were statistically significant differences on the buggy ratio and start time ratio between two genres with a small cohen’s D effect size (0.36). Action game videos tended to have a greater buggy ratio and earlier start times compared to sports game videos. The means of the action games buggy ratio and start time ratio were 0 _._ 43, and 0 _._ 18, respectively, while sports games had a mean of 0 _._ 29, and 0 _._ 27, respectively. 

## **4.3 RQ3: How does the tool perform when trained on footage from a single game?** 

Table 3 presents the performance of the classifiers on the _Ark: Survival Evolved_ subset dataset and the _FIFA 17_ subset dataset. With _Ark: Survival Evolved_ , the highest overall performing model was the Weighted Ensemble model that was trained on the automatically clustered dataset, achieving an F1 score of 0.73. For _FIFA 17_ , the Weighted Ensemble model 

Manuscript submitted to ACM 

14 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 

|Game Genre|Technique|Best Model|F1|Precision|Recall|
|---|---|---|---|---|---|
|||NeuralNetFastAI|0.83|0.84|0.82|
|||LightGBM|0.75|0.98|0.60|
|||XGBoost|0.60|0.71|0.52|
|||Linear Regression|0.82|0.92|0.74|
||Manual Clustering|RandomForest<br>|0.76|0.95|0.63|
|||ExtraTrees|0.76|0.95|0.63|
|||CatBoost|0.70|1.00|0.54|
|||KNeighbors|0.64|0.49|0.91|
|||Weighted Ensemble|**0.84**|0.87|0.82|
|_Action_||NeuralNetFastAI|0.64|0.71|0.59|
|||LightGBM|0.13|0.70|0.07|
|||XGBoost|0.07|0.25|0.04|
|||Linear Regression|0.48|0.79|0.35|
||Automatic Clustering|RandomForest|0.04|1.00|0.02|
|||ExtraTrees|0.00|0.00|0.00|
|||CatBoost<br>|0.02|1.00|0.01|
|||KNeighbors|0.25|0.93|0.15|
|||Weighted Ensemble|0.64|0.71|0.59|
||GELID||0.26|0.33|0.21|
|||NeuralNetFastAI|0.70|0.60|0.84|
|||LightGBM|0.72|0.93|0.59|
|||XGBoost|0.33|0.70|0.22|
|||Linear Regression<br>|0.80|0.95|0.69|
||Manual Clustering|RandomForest|0.75|1.00|0.60|
|||ExtraTrees|0.75|1.00|0.60|
|||CatBoost|0.60|0.97|0.44|
|||KNeighbors|0.24|1.00|0.14|
|||Weighted Ensemble<br>|0.79|0.82|0.77|
|_Sports_||NeuralNetFastAI|0.84|0.80|0.90|
|||LightGBM|0.26|0.93|0.15|
|||XGBoost|0.28|0.79|0.17|
|||Linear Regression|0.84|0.89|0.80|
||Automatic Clustering|RandomForest|0.80|1.00|0.67|
|||ExtraTrees|0.80|1.00|0.67|
|||CatBoost|0.82|1.00|0.69|
|||KNeighbors|0.46|0.90|0.31|
|||Weighted Ensemble|**0.90**|0.92|0.89|
||GELID||0.24|0.24|0.24|



Table 2. Performance of classification techniques on the _Action_ and _Sports_ games subsets 

from the manually clustered dataset attained a top F1 score of 0.91. For the _Ark: Survival Evolved_ subset dataset, the top-performing model outperformed GELID by 44 points. Notably, for the _FIFA 17_ subset dataset, GELID attained an F1 score of 0.62; our top model outperformed GELID by 29 points. This is smaller gain compared to the other datasets, but GELID’s performance on this data was still well below what was achieved by our top-performing _FIFA 17_ model. 

The F1 score for the _FIFA 17_ model saw a very marginal increase over the top F1 score achieved for sports games in general, going from 0.90 in Table 2 to 0.91 in Table 3. On the other hand, training and testing specifically on _Ark:_ Manuscript submitted to ACM 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 

15 

_Survival Evolved_ did not end up leading to improved performance over training and testing on action games more generally; instead the top F1 score in Table 2 dropped from 0.84 to the 0.73 seen in Table 3. At this point there does not appear to be a clear upward or downward trend in performance when continuing to move from a more general domain to a more specific one. 

**~~�~~ Observation 3:** For the _Ark: Survival Evolved_ subset dataset, the top-performing model achieved an F1 score of 0.73. For the _FIFA 17_ subset dataset, the top model achieved an F1 score of 0.91, outperforming GELID by 44 points and 29 points, respectively. **~~�~~** 

**�** 

**�** 

## **4.4 RQ4: Is it possible to identify which characteristics of visual video frames have an association with the prediction of a bug?** 

We performed a feature importance analysis on our prediction models and found that the visual frame features consistently held a significantly greater amount of importance over the transcript features across our different models and training sets. However, when it comes to explaining our models’ predictions, there is not much insight to be gleaned from the fact that a particular cluster in our Bag-of-Visual-Words set had a slightly higher TF-IDF than another. This is why we look to the generated pixel maps for this part of our analysis. 

Figure 5 shows an example of one of the pixel maps we got from our image model. The top image was a centroid image from one of our video segments. It was manually selected as a centroid after we verified that the frame did indeed depict a bug–the hockey player is stiff on the ice and unnaturally sliding down the rink. The resulting mapping indicates which parts of the image the model believed to have an effect on the ultimate decision to predict whether it contained a bug or not. The regions in green are areas that apparently had a positive influence on the model’s classification, while the areas in red are the sports that worked against the ultimate decision. For this paper, we are not specifically concerned over whether an area is red or green as much as we are interested in what areas end up being covered at all. In this instance, the majority of the sliding player is covered in green, indicating that something about the appearance of this character led to the prediction’s classification. 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0015-09.png)



![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0015-10.png)


Fig. 5. Original Game Image (left) and the pixel mapping (right) 

We examined the buggy segment centroids in our test data, categorizing them into three groups: frame images where the bug can be identified by looking at the frame on its own; frame images where the bug becomes apparent when comparing it to an adjacent frame, and frame images where the image does not relay any information about the type of bug being experienced. We put these frame images through the model, and examined them to try and identify any noteworthy patterns. Such patterns might provide insight into whether certain characteristics of images may have 

Manuscript submitted to ACM 

16 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 

|Game Title|Technique|Classification Model|F1|Precision|Recall|
|---|---|---|---|---|---|
|||NeuralNetFastAI|0.64|0.60|0.69|
|||LightGBM|0.13|0.50|0.08|
|||XGBoost|0.16|0.17|0.15|
|||Linear Regression|0.43|0.73|0.31|
||Manual Clustering|RandomForest<br>|0.00|0.00|0.00|
|||ExtraTrees|0.00|0.00|0.00|
|||CatBoost|0.00|0.00|0.00|
|||KNeighbors|0.33|0.20|1.00|
|||Weighted Ensemble|0.64|0.60|0.69|
|_Ark: Survival Evolved_||NeuralNetFastAI|0.64|0.60|0.69|
|||LightGBM|0.00|0.00|0.00|
|||XGBoost|0.31|0.46|0.23|
|||Linear Regression|0.41|0.88|0.27|
||Automatic Clustering|RandomForest|0.00|0.00|0.00|
|||ExtraTrees|0.00|0.00|0.00|
|||CatBoost<br>|0.00|0.00|0.00|
|||KNeighbors|0.44|0.29|0.92|
|||Weighted Ensemble|**0.73**|0.69|0.77|
||GELID||0.29|0.27|0.31|
|||NeuralNetFastAI|0.88|0.82|0.94|
|||LightGBM|0.79|0.89|0.71|
|||XGBoost|0.64|0.82|0.53|
|||Linear Regression<br>|0.90|1.00|0.82|
||Manual Clustering|RandomForest|0.81|0.96|0.71|
|||ExtraTrees|0.81|0.96|0.71|
|||CatBoost|0.80|0.92|0.71|
|||KNeighbors|0.74|0.74|0.74|
|||Weighted Ensemble<br>|**0.91**|0.94|0.88|
|_FIFA 17_||NeuralNetFastAI|0.85|0.79|0.91|
|||LightGBM|0.79|0.89|0.71|
|||XGBoost|0.62|0.81|0.50|
|||Linear Regression|0.88|0.91|0.85|
||Automatic Clustering|RandomForest|0.77|0.96|0.65|
|||ExtraTrees|0.77|0.96|0.65|
|||CatBoost|0.80|0.92|0.71|
|||KNeighbors|0.43|0.83|0.29|
|||Weighted Ensemble|0.88|0.88|0.88|
||GELID||0.62|0.55|0.71|



Table 3. Performance of classification techniques on the Ark: Survival Evolved and FIFA 17 subsets 

an association with the presence if bugs. In this section, we present a few simple patterns that we noticed during our examination. 

**Closely Gathered Characters:** We found that the model had a tendency to highlight sections where multiple characters are positioned close together, such as in the example from Figure 6a, where two soccer players are unnaturally squished up together–the two players are highlighted green where they make contact with each other. While most examples involved human characters, it was possible for other types of characters to be highlighted as well, such as the Manuscript submitted to ACM 

17 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 

tightly packed dinosaurs in Figure 6b. Overall, the model seemed to have a sensitivity to people and to a lesser extent, animal characters. 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0017-03.png)



![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0017-04.png)


(a) Soccer players gathered closely 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0017-06.png)



![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0017-07.png)



![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0017-08.png)


<!-- Start of picture text -->
(b) Bunched up dinosaurs<br><!-- End of picture text -->

Fig. 6. Mappings of closely gathered characters 

**Bold Shapes & Straight Lines:** This is an instance of the model perhaps not currently being optimized to handle certain types of images. More specifically, it seemed to get distracted by bold shapes and prominent straight lines in the absence of other more intricate objects in the frame. This was more common in sports games, since there were multiple instances in which the pixel mapping ended up following field and boundary lines, as seen in Figure 7a. The model also had this problem in frame images featuring prominent UI elements and menus; as seen in Figure 7b, the mapping seems to be more interested in fitting around the shape of the UI box than with the information depicted within it (which in this case is the actual source of the bug). 

**The Sliding Goalie:** For whatever reason, there were a noteworthy number of bugs in our dataset specifically involving players in hockey games (usually the goalie) being able to slide around the rink while sitting or laying down in unusual positions, as seen back in Figure 5 or in 8a. And for whatever reason, the model seemed to be able to identify those sliding goalies with a decent level of consistency. In fact, the most prominent example of the model missing a sliding goalie can be seen in Figure 8b. In this example, the goalie is not covered by any pixel maps, but it could be because this image is also an example of closely gathered characters. Perhaps the Sliding Goalie has a lower level of importance in comparison. 

Manuscript submitted to ACM 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 

18 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0018-02.png)



![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0018-03.png)


- (a) Mapping that follows lines on the field 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0018-05.png)


<!-- Start of picture text -->
960<br>BAS<br><!-- End of picture text -->


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0018-06.png)


(b) Mapping that follows shape of UI box 

Fig. 7. Mappings showing an inclination to follow lines and shapes 

- **4.5 RQ5: What benefits are brought to developers using our tool in identifying buggy game play segments in videos over a manual analysis?** 

To answer this question, we wanted to investigate if there was any benefit to using our tool for buggy segment detection besides high efficiency compared to manual analysis. 

**bservation 4:** Our results show that participants on an average gave smaller buggy ratio (0 _._ 60) compared to the automated approach (0 _._ 77). Our results also show that participants on average had a higher start time ratio 0 _._ 21) when compared to the automated approach (0 _._ 14) 

The buggy ratio results indicate that manual analysis is more likely to miss important information for buggy segment detection. The start time ratio results mean that participants on average took longer to identify the first buggy segment (see Section 3.3 for a definition of buggy ratio and start time ratio). 

## **5 DISCUSSION** 

In this section we discuss our results and their implications for researchers and practitioners. 

## **5.1 For Researchers** 

**Predictor Performance:** Our results indicate that our prediction models are capable of predicting whether a bug is presented in a video segment. When tested on our dataset from Section 4.1, the top models returned F1 scores of 0.87 and 0.88. Even after creating smaller subset datasets at the genre level and at the game level in Sections 4.2 and 4.3, Manuscript submitted to ACM 

19 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0019-02.png)


<!-- Start of picture text -->
HON<br><!-- End of picture text -->


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0019-03.png)


(a) Mapping over the Sliding Goalie 


![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0019-05.png)



![](images/Truelove_2023_Detecting_Bug_Occurrences_Gameplay_Videos.pdf-0019-06.png)


(b) Mapping that favors closely gathered characters over the Sliding Goalie 

Fig. 8. Mappings for the Sliding Goalie 

the top models still returned F1 scores of at least 0.70. The worst performance came from the models for _Ark: Survival Evolved_ , where the highest F1 score by any model across either clustering technique was 0.73. This could be due to the fact that, as the domain becomes more specific, the data might be more focused, but the number of data points decrease as well. This dataset only had 694 total video segments; if more video segments were added to this dataset in the future, this kind of evaluation might show improved results. 

Overall, however, the models produced promising performance results, significantly outperforming the prior stateof-the-art, GELID, across all datasets. One likely reason for this outperformance is likely due to the fact that GELID was designed to work specifically on videos that contained certain keywords in their transcripts [22]. Because our video segment dataset was constructed without any restrictions on the content of the video transcripts, it is likely that GELID was unable to account for transcripts that fell outside the scope of what it was created for. For future work, researchers can look to devising techniques to even further improve the results of our classification framework. They might investigate the differences between the subsets of game videos, such as why sports games seemed to return better scores than action games and why _FIFA 17_ seemed to fare better than _Ark: Survival Evolved_ . Additionally, researchers can implement our automated approach in order to identify buggy segments of gameplay videos into their own research tasks on game bugs. Future work might examine the characteristics of these buggy segments or the types of bugs that appear in these segments. 

**Superpixels:** The analysis of the superpixel maps was preliminary in nature. We wanted to investigate what kinds of objects the model was more likely to highlight and in what contexts. For example, the model seemed to have a tendency to highlight people, preferably people who are in groups. The most notable exception to this general observation is 

Manuscript submitted to ACM 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 

20 

in Figure 7a where the superpixels appeared to effectively ignore the players on the soccer field and instead ended following along with the various boundary lines. This could be explained by the difference in game view. The view in Figure 7a is considerably further away from the people seen in the other images. Future researchers may choose to explore some of the nuances between different video images and what effect these nuances might have on the model’s ability to correctly classify the presence of bugs. 

**User Study:** Our findings indicate that our automated bug identification models tend to achieve better performance than manual analysis. For future researchers, they could implement our approach on different kinds of game videos to study if there exist differences in the distribution of buggy segments based on other attributes of the game videos. For instance, they could study how the length of the video, the game play platform, and game genres affect the attributes we extracted. Because we only performed our user study with five videos, there is still room for future work to examine some of these other characteristics when comparing model performance with user studies. 

## **5.2 For Practitioners** 

**Predictor Performance:** Practitioners can use our bug prediction framework to help identify bugs in videos. Game developers wishing to apply our prediction framework to a narrow set of videos will likely still experience a high level of performance based on the results of our study. The fact that the prediction results may or may not improve as the dataset becomes more specific may be particularly relevant to practitioners, since they are more likely to be interested in detecting bugs in games that they actively work on rather than over a range of different games. Practitioners may not be interested in manually designating clusters and buggy centroids, so the fact that the models still work with high performance even when using automatically generated clusters is certainly helpful. Additionally, the results of our user study indicate that our framework provides benefits pertaining to accuracy and time saved when compared to manual analysis. Overall, the tool we built could facilitate the whole process of issue tracking, while maintaining the high accuracy of prediction results. 

**Superpixels:** Practitioners may be interested in running the superpixel pipeline on videos of their games since they are likely to have more domain knowledge about these games, and as such, may be better able to identify when a superpixel map is highlighting something significant. 

## **6 THREATS TO VALIDITY** 

Though we structured our study to eliminate the possible effects of random noise and avoid introducing bias, it is still possible that our mitigation strategies may not have been effective. This section reviews the threats to the validity of our study 

The dataset used for the study contains game videos from YouTube as the single source. It is possible that game videos from other media platforms may have a different distribution in terms of buggy segments. Since all videos are collected from YouTube, our findings may be limited to game videos posted through YouTube. However, we believe that the collected dataset covers a wide range of video games which is sampled more than adequately for addressing this threat. 

To fully understand the context of each video besides visual information, we also used the encoded transcript as a feature for training our classifiers. It is possible that the caption auto-generation tools on YouTube and Otter.ai could not address the context properly. Though the effectiveness of our classifier is limited by the current state-of-art technology of speech-to-text software, we believe that our labelling results are only likely to be improved as the technology evolves. To get deeper insight on the labelling results, we conducted multiple statistical tests to compare attributes between Manuscript submitted to ACM 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 

21 

different game genres, as well as the user study and mining results. These tests would increase the chance of getting Type I error. To mitigate this threat, we did the Bonferroni correction [8]. 

For the segmentation of videos, it is possible that the approach we used to split the videos might not have returned the best performance. We automatically split the videos based on the timestamps from the transcript, such as those presented in Figure 2. We used this automated approach to minimize disruptive splits in the videos. While this approach did split phrases into multiple segments, it managed to avoid more awkward splits, such as splits in the middle of a word. Furthermore, the prior state-of-the-art from Guglielmi et al. also used the transcript timestamps in order to divide videos into segments [22]. It is also possible that the timestamp and captions in the transcripts were inaccurate to each other (e.g., spoken language appearing in a different segment than what the transcript specified). We did not experience any inaccuracies when we labelled our segments, however. 

From the user study result, it is always possible that the participants misinterpreted the context of the video and mistakenly perceived one buggy segment as there are no bugs included. To mitigate this threat, we conducted a pilot study with students who have some experience playing video games. The selected five videos for the user study were updated based on the findings of this pilot study. However, our findings through the user study may not be generalizable due to the small selected sample size, as there are only five videos. Since the user study is conducted to triangulate our mining result and the selected videos do cover a wide range of pattern on buggy segment distributions, we believe that this will not negatively impact our findings. 

## **7 CONCLUSION** 

In this paper, we introduced an automated approach based on machine learning to identify whether a segment of a gameplay video contains occurrences of bugs. The approach was evaluated using a dataset comprised of 4,412 video segments from 198 gameplay videos collected from YouTube. We trained and tested multiple machine learning models with these video segments, deriving features from the transcript text and the visual content. Testing our models returned a top F1 score of 0.88, indicating that this is a promising approach to identifying the presence of bugs in gameplay segments. Additionally, we found that training and testing models on video segments from the same genre of game still produced high F1 scores for both game genres evaluated (0.84 for action and 0.90 for sports). Performance was still high when training and testing models with video segments from a single game (0.73 for _Ark: Survival Evolved_ and 0.91 for _FIFA 17_ ). In all cases, our approach significantly outperformed the prior state-of-the-art for classifying buggy segments of gameplay videos. Furthermore, we performed a superpixel analysis to identify possible patterns in the content of frame images that may hold importance to the classifier. Finally, we conducted a preliminary user study that indicated that our approach can identify buggy segments sooner and with greater accuracy than manual analysis. 

For future work, we intend to expand the scope of the genres and games used to train the models. Evaluation of models trained on additional video sets may reveal aspects of these videos that have an association with bugs. We also plan to explore the superpixel pipeline further. 

## **8 DATA AVAILABILITY** 

The research artifacts for this study are available publicly at the companion website [2]. We intend to make the data and our analysis scripts publicly available upon publication of the paper. 

## **REFERENCES** 

[1] “Otter.ai,” https://otter.ai/login, accessed: Nov. 14, 2023. 

Manuscript submitted to ACM 

Andrew Truelove, Shiyue Rong, Eduardo Santana de Almeida, and Iftekhar Ahmed 

22 

- [2] “Supplementary material for “Finding the needle in a haystack: Detecting bug occurrences in gameplay videos”,” https://github.com/gameplay-bugstudy/data, accessed: Mar. 1, 2023. 

- [3] “Twitch,” https://www.twitch.tv/, accessed: Nov. 12, 2023. 

- [4] “Youtube,” https://www.youtube.com/, accessed: Nov. 12, 2023. 

- [5] “sklearn.ensemble.randomforestclassifier,” https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html, 2023, accessed: Oct. 30, 2023. 

- [6] “sklearn.linear_model.logisticregression,” https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html, 2023, accessed: Oct. 30, 2023. 

- [7] S. Amiriparian, N. Cummins, M. Gerczuk, S. Pugachevskiy, S. Ottl, and B. Schuller, ““Are You Playing a Shooter Again?!” Deep Representation Learning for Audio-Based Video Game Genre Recognition,” _IEEE Transactions on Games_ , vol. 12, no. 2, pp. 145–154, 2019, publisher: IEEE. 

- [8] Y. Benjamini and D. Yekutieli, “The control of the false discovery rate in multiple testing under dependency,” _Annals of statistics_ , pp. 1165–1188, 2001. 

- [9] D. Brezeale and D. J. Cook, “Automatic video classification: A survey of the literature,” _IEEE Transactions on Systems, Man, and Cybernetics, Part C (Applications and Reviews)_ , vol. 38, no. 3, pp. 416–430, 2008. 

- [10] N. Carpenter, “Cd Projekt has blown years’ worth of goodwill in a week,” https://www.polygon.com/22178913/cyberpunk-2077-launch-controversycd-projekt, Dec. 2020, accessed: Nov. 5, 2023. 

- [11] R. Caruana, A. Niculescu-Mizil, G. Crew, and A. Ksikes, “Ensemble selection from libraries of models,” in _Proceedings of the twenty-first international conference on Machine learning_ , 2004, p. 18. 

- [12] D. Cer, Y. Yang, S.-y. Kong, N. Hua, N. Limtiaco, R. S. John, N. Constant, M. Guajardo-Céspedes, S. Yuan, C. Tar, and others, “Universal sentence encoder,” _arXiv preprint arXiv:1803.11175_ , 2018. 

- [13] H. Chatbri, K. McGuinness, S. Little, J. Zhou, K. Kameyama, P. Kwan, and N. E. O’Connor, “Automatic MOOC video classification using transcript features and convolutional neural networks,” in _Proceedings of the 2017 ACM Workshop on Multimedia-based Educational and Knowledge Technologies for Personalized and Social Online Training_ , 2017, pp. 21–26. 

- [14] T. Chen and C. Guestrin, “Xgboost: A scalable tree boosting system,” in _Proceedings of the 22nd acm sigkdd international conference on knowledge discovery and data mining_ , 2016, pp. 785–794. 

- [15] T. Chen, S. Kornblith, M. Norouzi, and G. Hinton, “A simple framework for contrastive learning of visual representations,” in _International conference on machine learning_ . PMLR, 2020, pp. 1597–1607. 

- [16] M. A. Cherney, “This violent videogame has made more money than any movie ever,” https://www.marketwatch.com/story/this-violent-videogamehas-made-more-money-than-any-movie-ever-2018-04-06, Apr. 2018, accessed: Oct. 10, 2023. 

- [17] N. Cooper, C. Bernal-Cárdenas, O. Chaparro, K. Moran, and D. Poshyvanyk, “It takes two to tango: Combining visual and textual information for detecting duplicate video-based bug reports,” in _2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE)_ . IEEE, 2021, pp. 957–969. 

- [18] crogeek, “My Arma 3 has started glitching ( @ EUTW ),” https://youtu.be/ale8JK5qyis, Jan. 2016, accessed: Nov. 2, 2023. 

- [19] J. Dornbush, “Sony removes Cyberpunk 2077 from PS Store, will offer refunds to PlayStation players who already bought it,” https://www.ign.com/ articles/sony-removing-cyberpunk-2077-from-ps-store-will-offer-refunds-to-playstation-players-who-already-bought-it, Dec. 2020, accessed: Nov. 11, 2023. 

- [20] EA NHL Clips, “Weird NHL 16 glitch,” https://youtu.be/Dg8PGt-ecrc, Jan. 2016, accessed: Nov. 3, 2022. 

- [21] Fernanfloo, “I get bald !! - Ninjala | Fernanfloo,” https://youtu.be/nnHOFsLztt4, Jul. 2020, accessed: Oct. 28, 2023. 

- [22] E. Guglielmi, S. Scalabrino, G. Bavota, and R. Oliveto, “Using gameplay videos for detecting issues in video games,” _Empirical Software Engineering_ , vol. 28, no. 6, p. 136, 2023. 

- [23] T. Hollett, “How to save transcripts from YouTube videos,” https://davescomputertips.com/how-to-save-transcripts-from-youtube-videos/, Jan. 2018, accessed: Sep. 22, 2023. 

- [24] J. Howard and S. Gugger, “Fastai: a layered api for deep learning,” _Information_ , vol. 11, no. 2, p. 108, 2020. 

- [25] M. Isaac and K. Browning, “Cyberpunk 2077 was supposed to be the biggest video game of the year. What happened?” https://www.nytimes.com/ 2020/12/19/style/cyberpunk-2077-video-game-disaster.html, Dec. 2020, accessed: Nov. 8, 2023. 

- [26] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T.-Y. Liu, “Lightgbm: A highly efficient gradient boosting decision tree,” _Advances in neural information processing systems_ , vol. 30, 2017. 

- [27] G. Kordopatis-Zilos, S. Papadopoulos, I. Patras, and I. Kompatsiaris, “Fivr: Fine-grained incident video retrieval,” _IEEE Transactions on Multimedia_ , vol. 21, no. 10, pp. 2638–2652, 2019. 

- [28] C. Lewis, J. Whitehead, and N. Wardrip-Fruin, “What went wrong: a taxonomy of video game bugs,” in _Proceedings of the fifth international conference on the foundations of digital games_ , 2010, pp. 108–115. 

- [29] D. Lin, C.-P. Bezemer, and A. E. Hassan, “Identifying gameplay videos that exhibit bugs in computer games,” _Empirical Software Engineering_ , vol. 24, no. 6, pp. 4006–4033, 2019. 

- [30] Y. Liu, X. Feng, and Z. Zhou, “Multimodal video classification with stacked contractive autoencoders,” _Signal Processing_ , vol. 120, pp. 761–766, 2016. 

- [31] F. J. Massey Jr, “The kolmogorov-smirnov test for goodness of fit,” _Journal of the American statistical Association_ , vol. 46, no. 253, pp. 68–78, 1951. 

- [32] P. Millett, “Accuracy of speech-to-text captioning for students who are deaf or hard of hearing.” _Journal of Educational, Pediatric & (Re) Habilitative Audiology_ , vol. 25, 2021. 

Manuscript submitted to ACM 

Finding the Needle in a Haystack: Detecting Bug Occurrences in Gameplay Videos 

23 

- [33] E. Narcisse, “More than a third of 2014’s big-budget games got day-one patches,” https://kotaku.com/more-than-a-third-of-2014-s-big-budgetgames-got-day-on-1686398805, Feb. 2015, accessed: Sep. 14, 2023. 

- [34] Newzoo, “The games market in 2022: The year in numbers,” https://newzoohq.medium.com/the-games-market-in-2022-the-year-in-numbersf686da582178, Dec. 2022, accessed: Oct. 18, 2023. 

- [35] B. Parton, “Video captions for online courses: Do YouTube’s auto-generated captions meet deaf students’ needs?” _Journal of Open, Flexible, and Distance Learning_ , vol. 20, no. 1, pp. 8–18, 2016, publisher: Distance Education Association of New Zealand. 

- [36] M. T. Ribeiro, S. Singh, and C. Guestrin, “"Why should I trust you?" Explaining the predictions of any classifier,” in _Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining_ , 2016, pp. 1135–1144. 

- [37] C. Ringer and M. A. Nicolaou, “Deep unsupervised multi-view detection of video game stream highlights,” in _Proceedings of the 13th International Conference on the Foundations of Digital Games_ , 2018, pp. 1–6. 

- [38] S. Roohi, E. D. Mekler, M. Tavast, T. Blomqvist, and P. Hämäläinen, “Recognizing emotional expression in game streams,” in _Proceedings of the Annual Symposium on Computer-Human Interaction in Play_ , 2019, pp. 301–311. 

- [39] R. E. Santos, C. V. Magalhães, L. F. Capretz, J. S. Correia-Neto, F. Q. da Silva, and A. Saher, “Computer games are serious business and so is their quality: Particularities of software testing in game development from the perspective of practitioners,” in _Proceedings of the 12th ACM/IEEE International Symposium on Empirical Software Engineering and Measurement_ , 2018, pp. 1–10. 

- [40] S. Shah, M. Guzdial, and M. O. Riedl, “Automated let’s play commentary,” _arXiv preprint arXiv:1909.02195_ , 2019. 

- [41] M. Sjöblom, M. Törhönen, J. Hamari, and J. Macey, “The ingredients of twitch streaming: Affordances of game streams,” _Computers in Human Behavior_ , vol. 92, pp. 20–28, 2019. 

- [42] M. Song, Z. Yang, A. Baird, E. Parada-Cabaleiro, Z. Zhang, Z. Zhao, and B. Schuller, “Audiovisual analysis for recognising frustration during game-play: Introducing the multimodal game frustration database,” in _2019 8th International Conference on Affective Computing and Intelligent Interaction (ACII)_ . IEEE, 2019, pp. 517–523. 

- [43] SpicyCat, “Playerunknown’s battlegrounds blatant cheats?ez hacks? ft. boxfresh & pj,” https://youtu.be/dAgLbg2-wOg, Jul. 2017, accessed: Sep. 2, 2023. 

- [44] D. Stutz, A. Hermans, and B. Leibe, “Superpixels: An evaluation of the state-of-the-art,” _Computer Vision and Image Understanding_ , vol. 166, pp. 1–27, 2018. 

- [45] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan, V. Vanhoucke, and A. Rabinovich, “Going deeper with convolutions,” in _Proceedings of the IEEE conference on computer vision and pattern recognition_ , 2015, pp. 1–9. 

- [46] M. R. Taesiri, F. Macklon, and C.-P. Bezemer, “Clip meets gamephysics: Towards bug identification in gameplay videos using zero-shot transfer learning,” in _Proceedings of the 19th International Conference on Mining Software Repositories_ , 2022, pp. 270–281. 

- [47] A. Truelove, E. S. de Almeida, and I. Ahmed, “We’ll fix it in post: What do bug fixes in video game update notes tell us?” in _2021 IEEE/ACM 43rd International Conference on Software Engineering (ICSE)_ . IEEE, 2021, pp. 736–747. 

- [48] R. Tufano, S. Scalabrino, L. Pascarella, E. Aghajani, R. Oliveto, and G. Bavota, “Using reinforcement learning for load testing of video games,” _arXiv preprint arXiv:2201.06865_ , 2022. 

- [49] R. Watt, “2020 is YouTube Gaming’s biggest year, ever: 100B watch time hours,” https://blog.youtube/news-and-events/youtube-gaming-2020, Dec. 2020, accessed: Aug. 30, 2023. 

- [50] J. Ye, “Cosine similarity measures for intuitionistic fuzzy sets and their applications,” _Mathematical and computer modelling_ , vol. 53, no. 1-2, pp. 91–97, 2011. 

Manuscript submitted to ACM 

