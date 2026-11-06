AUTOMATING ARTIFACT DETECTION IN VIDEO GAMES 

**Parmida Davarmanesh Kuanhao Jiang Tingting Ou** University of Michigan, Ann Arbor University of Pennsylvania Johns Hopkins University `pdavar@umich.edu kuanhaoj@seas.upenn.edu tou2@jhu.edu` 

**Artem Vysogorets Stanislav Ivashkevich Max Kiehn Shantanu H. Joshi** New York University AMD, Inc. AMD, Inc. UCLA `amv458@nyu.edu Stanislav.Ivashkevich@amd.com max.kiehn@amd.com s.joshi@g.ucla.edu` 

## **Nicholas Malaya** 

AMD Research 

```
nicholas.malaya@amd.com
```

December 1, 2020 

# **ABSTRACT** 

In spite of advances in gaming hardware and software, gameplay is often tainted with graphics errors, glitches, and screen artifacts. This proof of concept study presents a machine learning approach for automated detection of graphics corruptions in video games. Based on a sample of representative screen corruption examples, the model was able to identify 10 of the most commonly occurring screen artifacts with reasonable accuracy. 

Feature representation of the data included discrete Fourier transforms, histograms of oriented gradients, and graph Laplacians. Various combinations of these features were used to train machine learning models that identify individual classes of graphics corruptions and that later were assembled into a single mixed experts “ensemble” classifier. The ensemble classifier was tested on heldout test sets, and produced an accuracy of 84% on the games it had seen before, and 69% on games it had never seen before. 

**_K_ eywords** Video Games, Games, Glitch, Artifact, Automation, Dataset, Glitch Detection, Computer Vision 

# **1 Introduction** 

More than 65% of Americans play video games on at least one type of device [1]. Furthermore, the combined gaming industry produced a revenue of $120B in 2019, a 4% increase from 2018 [2]. For these games to be immersive, gameplay must remain high-quality and error-free. While games may contain various defects and issues, graphical corruption and visual artifacts are some of the largest complaints from users [3]. These artifacts typically occur due to software or hardware errors that alter visual appearance of the game or its individual frames. Figure 1 shows some examples of such corruptions observed in real games. 

In this paper, we conducted a proof of concept study to automate the detection of graphical artifacts. This is a novel problem that, if solved, would lead to significant quality improvement and enhanced experience for consumers of images and video. Currently, artifact detection is a labor intensive process where glitches are reported individually by users who experience them [4]. This process is manual and time consuming, and a large number of users typically choose not to report these glitches, resulting in a number of unreported and unresolved issues. Furthermore, even if these glitches are reported in large scales, it still takes a lot of human effort to sort and catalogue these them. The first implication of automating this process is that there is no need for human intervention. Once a glitch occurs, it will be automatically captured and sent to the corresponding company for correction. Second, with increased knowledge of the 

A PREPRINT - DECEMBER 1, 2020 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0002-01.png)


Figure 1: Examples of video game artifacts (images are courtesy of AMD). 

source and cause of glitches, this automated software will be able to catch and correct the glitch before it is displayed to the user, resulting in an uninterrupted and smooth gameplay experience. To the best of the authors’ knowledge, no existing work has systematically synthesized glitches in images, cataloged and labeled them, and proposed an automated solution for detecting them. 

The contributions of this paper are as follows: 

1. Creation of the open source software, called _Glitchify_ , for reproducing a basket of common gaming artifacts. 

2. Generation of a labeled large dataset consisting of 50,000 normal and glitched gaming images. 

3. Using dimensionality reduction and feature extraction techniques on gaming images and building an ensemble model to classify gaming images to automate the process of artifact detection. 

# **2 Gaming Artifact Creation** 

Automating artifact detection, just like any other classification task, requires large amounts of data (e.g. labelled corrupted frames). There are no publicly available large-scale databases which provide this. Therefore, we created a large dataset of real images from game plays and injected different types of graphics artifacts to obtain glitched images. Specifically, we focused on the artifacts that are caused by software defects, as hardware artifacts which are highly content related are produced during rendering in the GPU and are thus much more challenging to reproduce. This data generation was implemented in an open source software _Glitchify_ which is publicly available at `https: //github.com/AMD-RIPS/ST-2019` . 

The prototype for our synthetic data was a limited collection of corrupted images provided by AMD that were representative of graphic artifacts observed frequently during gameplay. The _Glitchify_ software then artificially generated images with different types of corruption, designed to closely mimic what was observed in the sample set. Unlike artifacts shown in Figure 1, some of the images in the sample appeared to also have content-related artifacts. These content-related glitches depend upon the objects and their interactions in scenes and are thus difficult to represent and resolve. Since these glitches would further require video segmentation and object recognition techniques for detection, they are not addressed in the paper. 

2 

A PREPRINT - DECEMBER 1, 2020 

## **2.1 Types of Reproduced Artifacts** 

To reproduce different artifacts, we defined 10 different classes of corruptions based on their appearances. Gameplay data was obtained from publicly available YouTube videos. The dimension of the images or frames extracted from gameplay videos was set to 1920 _×_ 1080 pixels. These different kinds of artifacts are described below. 

## **2.1.1 Shader Artifacts** 

The shader program within a GPU performs frame rendering and determines various surface properties such as texture, reflection and lightning[5]. For our work, _shader_ artifacts are marked by the presence of polygonal shapes of different colors that either blend together or display gradual fading in certain directions. This glitch (Figure 2) was reproduced by choosing a random number of points in random positions of the image as the starting point and then setting a random number of edges to form a polygon. We then chose a random color close to that of the initial point, and reassign the pixel values in that polygon by slowly changing the color and reducing the intensity of the color. 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0003-05.png)



![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0003-06.png)


<!-- Start of picture text -->
DUBSTEPZZ<br><!-- End of picture text -->

Figure 2: _Shader_ corruption: actual (left) and reproduced with _Glitchify_ (right). 

## **2.1.2 Shapes Artifacts** 

Random polygonal monocolor shapes are also common in video games, especially in first-person shooting games. _Shapes_ artifacts tend to appear in the darker part of the frames. We reproduced this artifact (Figure 3) by choosing a random staring point in the darkest rectangular region (of random size within a certain range) of the image, and drawing a random number of dark thin polygons out of that point. 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0003-10.png)


<!-- Start of picture text -->
WIGAME<br>MATCHMAKING<br>SELECT CHARACTERT<br>OPTIONS<br><!-- End of picture text -->


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0003-11.png)


Figure 3: _Shapes_ : actual (left) and reproduced with _Glitchify_ (right). 

## **2.1.3 Discoloration Artifacts** 

_Discoloration_ artifacts manifest as bright spots in images that are colored differently. This artifact (Figure 4) was reproduced by changing the color of pixels. For example, one could set the red component of the pixel to a predefined value above or below a certain threshold. 

## **2.1.4 Morse Code Pattern** 

The morse code pattern (shown in Figure 5) appears when memory cells on a graphic card become stuck and display their stuck values on the screen rather than displaying the true image. Running a GPU at a higher speed than it was 

3 

A PREPRINT - DECEMBER 1, 2020 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0004-01.png)



![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0004-02.png)


Figure 4: _Discoloration_ : actual (left) and reproduced with _Glitchify_ (right). 

designed for, or at a high temperature, may result in such corruption. To reproduce this type of artifact, we add morse-code-like patterns to random locations in the frame, as shown in Figure 5. 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0004-05.png)



![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0004-06.png)


Figure 5: _Morse Code Pattern_ : actual (left) and reproduced with _Glitchify_ (right). 

## **2.1.5 Dotted Lines Artifacts** 

_Dotted Lines_ artifacts are often hard to recognize unless one magnifies the corrupted images. The _Dotted Lines_ either have random slopes and positions in the input frames, or they can be radial lines emanating from a single point. To generate the random _Dotted Lines_ artifacts (Figure 6), a random color is first determined. Then _N dotted lines_ of this color replace the original pixel values of the image, where _N_ is randomly chosen from a uniform distribution. We chose the starting point of each line segment such that it does not lie close to the edges of the image. The radial _Dotted Lines_ are different from the random _Dotted Lines_ in that they originate from a single point and _M_ dotted line segments of the image are replaced with new pixel values, where _M_ is chosen from a uniform distribution. 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0004-10.png)



![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0004-11.png)



![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0004-12.png)


Figure 6: _Dotted Lines_ : actual corrupted image provided by AMD (leftmost), our reproduced corrupted image with random lines of green color (middle) and radial lines of red color (rightmost). 

## **2.1.6 Parallel Lines** 

_Parallel Lines_ artifacts are visually discernible, where the corrupted images may contain lines, where the color of each line segment is the pixel color of the starting point of the line. To reproduce the _Parallel Lines_ artifact (Figure 7), _N_ parallel lines in the image are replaced by new pixel values, where _N ∼ Uniform_ (60 _,_ 100) _._ The angle between each 

4 

A PREPRINT - DECEMBER 1, 2020 

line and the horizontal axis is Θ such that Θ _∼ Uniform_ (10 _,_ 35). We choose the starting point _P_ = ( _x_ 0 _, y_ 0) of each parallel line such that _x_ 0 _∈_ [0 _._ 3 _·_ 1920 _,_ 0 _._ 6 _·_ 1920] and _y_ 0 _∈_ [0 _._ 2 _·_ 1080 _,_ 0 _._ 8 _·_ 1080]. Each parallel line has a thickness _t_ such that _t ∼ Uniform_ (1 _,_ 3). 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0005-02.png)



![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0005-03.png)


Figure 7: _Parallel Lines_ : actual (left) and reproduced with _Glitchify_ (right). 

## **2.1.7 Triangulation** 

_Triangulation_ typically occurs in intensive 3D games, where surfaces are rendered by little triangles that form triangle meshes. Due to graphic defects, such triangular meshes are displayed at a coarse resolution and incorrectly colored, instead of smoothly rendered. To reproduce this artifact (Figure 8), we divide the image into triangular sections and color each triangle with the average of all the pixels within. 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0005-07.png)



![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0005-08.png)


Figure 8: Triangulation: actual (left) and reproduced with _Glitchify_ (right). 

## **2.1.8 Line pixelation** 

_Line pixelation_ is characterized by noisy stripes with random orientations and positions on the image. To capture the distribution (pixel intensity variations) in this artifact, we insert a random number of noisy stripes with random orientations and positions in addition to randomly positioned halos around some pixels. This artifact appears at the very bottom of the left image in figure (Figure 9). 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0005-12.png)



![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0005-13.png)


Figure 9: Line pixelation: actual (left) and reproduced with _Glitchify_ (right). 

5 

A PREPRINT - DECEMBER 1, 2020 

## **2.1.9 Screen Stuttering** 

_Screen stuttering_ occurs when neighboring columns and rows of the image are swapped. We reproduce the _Screen stuttering_ artifact (Figure 10) by swapping neighboring columns and rows in one direction, and then swapping the neighboring rows and then columns in the other direction respectively. 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0006-03.png)



![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0006-04.png)


Figure 10: Screen stuttering: actual (left) and reproduced with _Glitchify_ (right). 

## **2.1.10** **_Screen tearing_** 

_Screen tearing_ occurs when two consecutive frames in a video are rendered in same image. Therefore, part of the image shows the scene at a certain point in time, while the other part of the same image shows that scene at a later time. To reproduce this artifact, we select two frames in a video that are 100 frames apart from each other, and then randomly replace some rows (or columns) of the first frame with the corresponding rows (or columns) of the second frame (Figure 11). 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0006-08.png)



![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0006-09.png)


Figure 11: _Screen tearing_ : actual (left) and reproduced with _Glitchify_ (right). 

# **3 Feature Extraction** 

Since we extracted high-quality colored images (1920 _×_ 1080 pixels), the dimensions of the images were too large to be used directly by machine learning algorithms. Therefore, the following methods were used to extract low dimensional features from images. 

## **3.1 Discrete Fourier Transform** 

The two-dimensional Discrete Fourier Transform (DFT) is often used to process two-dimensional discrete signals such as images. Given a one-channel signal _f_ ( _x, y_ ) with dimensions _M × N_ , its DFT _F_ ( _u, v_ ) is given by 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0006-15.png)


<!-- Start of picture text -->
M − 1 N − 1<br>1<br>F ( u, v ) = � � f ( x, y ) e − 2 iπ ux M e − 2 iπ v N y , (1)<br>√ MN x =0 y =0<br><!-- End of picture text -->

where _u_ and _v_ are the spectral coordinates. 

6 

A PREPRINT - DECEMBER 1, 2020 

The original signal can be extracted from _F_ ( _u, v_ ) via inverse Fourier transform: 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0007-02.png)


<!-- Start of picture text -->
M − 1 N − 1<br>1<br>f ( x, y ) = � � F ( u, v ) e 2 iπ ux M e 2 iπ v N y . (2)<br>√ MN u =0 v =0<br><!-- End of picture text -->

The rationale behind considering DFT as a feature for the graphics artifact classification is that several types of artifacts (e.g. morse code, _Parallel Lines_ , etc.) exhibit periodic patterns that could be best identified in the frequency domain. Previous studies provide evidence of successful application of this technique to the detection of periodic patterns in signals [6]. Additionally, most graphics corruptions have sharp edges and fine structure, which finds reflection in the high-frequency components. 

## **3.2 Histogram of Oriented Gradients (HoG)** 

Histogram of oriented gradients is a feature used in computer vision to detect edges in an image [7]. An _M × N_ color image can be represented using three functions _R, G, B_ : R<sup>_M×N_</sup> _→ R_ that map each coordinate to the corresponding red, green, and blue color intensity value, respectively. The gradient of the functions at each coordinate can be approximated by applying discrete derivative masks at each coordinate. 

The image is then divided into small patches, and the magnitude and orientation of gradients within each patch are computed and summarized by a histogram of gradients containing _n_ bins corresponding to angles 0 _, n_<sup>_<u>π</u>,_</sup><sup><u>2</u></sup> _n_<sup>_<u>π</u>, . . . ,_</sup><sup><u>(</u></sup><sup>_n−_</sup> _n_<sup>1)</sup><sup>_π_</sup> . For each gradient with magnitude _m_ and orientation _θ_ , we select the two consecutive bins (here we consider the last bin and the first bin to be consecutive) such that _θ_ lies in the range determined by the two bins. Suppose the two selected bins correspond to angles _θ_ 1 and _θ_ 2, then the values go to the two bins are<sup>_mn|θ_</sup> _π_<sup>_−θ_1</sup><sup>_<u>|</u>_</sup> and<sup>_mn|θ_</sup> _π_<sup>_−θ_2</sup><sup>_<u>|</u>_</sup> , respectively. Finally, we normalize the histograms and then concatenate them together to form a feature descriptor of the entire image. 

## **3.3 Pixel-wise Anomaly Measure** 

Given an image, we approximate the distribution of red, green, and blue intensities, and then assign each individual pixel an anomaly score based on how much the pixel’s intensity deviates from the estimated global distribution [8]. This process can be done using graph-based method described below [9] as follows. 

Consider an undirected, weighted graph _G_ = ( _V, E_ ) composed of a vertex set _V_ = _{r, g, b}_ corresponding to the three color intensities, and an edge set _E_ specified by ( _a, b, wab_ ), where _a, b ∈ V_ , and _wab ∈_ R<sup>+</sup> is the edge weight between vertices _a_ and _b_ . In our case, the edge weights are defined as: 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0007-10.png)


<!-- Start of picture text -->
1 1 1<br>wrg = (3)<br>1 + � µr−αµg �2 , w rb = 1 + � µr−α µb �2 , w gb = 1 + � µg−α µb �2<br><!-- End of picture text -->

where _α_ =<sup>_<u>µa</u>_</sup><sup><u>+</u></sup><sup>_<u>µ</u>_</sup> 3<sup>_<u>g</u>_</sup><sup><u>+</u></sup><sup>_<u>µb</u>_</sup> and _µr, µg, µb_ are the average red, green, and blue intensities in the image, respectively. From the adjacency matrix _W_ , the combinatorial graph Laplacian matrix _L_ = _D − W_ can be computed, where _D_ is the degree matrix defined by: 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0007-12.png)


<!-- Start of picture text -->
k =1 wak if  a  =  b<br>D ( a, b ) = 0 otherwise (4)<br>�� n<br><!-- End of picture text -->

Finally, we normalize the Laplacian matrix _L_<sup>_∗_</sup> = _D_<sup>_−_</sup> 2<sup><u>1</u></sup> _LD_<sup>_−_</sup><sup><u>1</u></sup> 2 and define an anomaly measure for each pixel _x_ in the image by: _δ_ ( _x_ ) = _s_<sup>_T_</sup> _L_<sup>_∗_</sup> _s,_ 

where _s ∈_ R<sup>3</sup> is the color intensity of _x_ . 

## **3.4 Randomized Principal Component Analysis** 

Principal component analysis (PCA) is a commonly used dimensionality reduction technique in machine learning and statistics [10]. It attempts to find directions, or principal components, that maximizes the variance of projected data. Data projected onto the space determined by the first several principal components are used as a low dimensional 

7 

A PREPRINT - DECEMBER 1, 2020 

representation of the original data matrix. 

Principal components are often computed via singular value decomposition (SVD) [11] since the principle components are exactly the normalized right singular vectors of the data matrix. However, computing the exact value of SVD takes _O_ ( _mn_ min( _m, n_ )) time, where ( _m, n_ ) is the dimension of the data matrix. Therefore it is computationally infeasible to find the exact decomposition to our high dimensional data matrix. Instead, we apply randomized power iteration SVD algorithm described in [12, 13]. 

# **4 Classification** 

For each artifact, we explored various combinations of feature representations and classification algorithms, and picked the best performing combination as a specialized classifier for that artifact. We then combined these specialized classifiers into an ensemble model as they are shown to perform better than any single individual classifier (figure 12) [14]. The following section provides a brief overview of the justification behind the feature/model combinations that we hand selected. 

## **4.1 Feature and Model Selection** 

Given the nature of each artifact, we only considered those feature representation/classifier combinations that seemed capable of capturing that artifact. For example, there are no repetitive patterns in _Screen tearing_ artifacts so we did not use Fourier transform to represent this artifact. The set of potential classifiers consisted of Convolutional Neural Networks (CNN), Logistic Regression (LR), Random Forest (RF), Support Vector Classifier (SVC), and Linear Discriminant Analysis (LDA). We used accuracy, recall, and precision in that order as evaluation metrics of our models. Additionally, if two models had similar performances, we picked the one with the lowest training time. It is important to note that if in the process of testing a feature/classifier combination on a given artifact we reached accuracy, recall, and precision rates higher than %90 on the test set, we did not try other combinations on that artifact. 

- **Resize** _→_ **CNN** : Convolutional Neural Networks are deep learning classifiers for computer vision tasks. CNNs are typically not capable of performing well on large images, so we had to resize the images. Our CNN had the architecture of Convolution _→_ Maxpool _→_ Convolution _→_ Maxpool _→_ Softmax. We did not perform hyperparameter tuning, however, it is a promising future direction to pursue. We tried this combination on artifacts that were still detectable after resizing: _Parallel Lines_ , _Shapes_ , _Shader_ , and _Discoloration_ . For the artifacts with a repetitive pattern, we added a Fourier transform step prior to resizing the image as the transformed image will have distinctive features that are more dominant than in the original image, especially after the image has been resized. The **Fourier Transform** _→_ **Resize** _→_ **CNN** combination was used on every artifact except for _Parallel Lines_ , _Screen Tearing_ , and _Discoloration_ . 

- **Fourier Transform** _→_ **Resize** _→_ ( **PCA** ) _→_ **SVC, LDA, LR** : Given that the classification models in this category are shallow and do not take in images as input, we either used PCA as a dimensionality reduction technique, or we flattened the image into a one dimensional vector before handing the to the classifiers. Also, since our transformed images were still too large, we downsized the images before the application of PCA or flattening. Fourier transform was used as a first step because in most artifacts, the transformed image has more distinctive and less localized visual features than the original image. We used this combination on every artifact except for _Screen Tearing_ and _Discoloration_ . 

- **Resize** _→_ ( **HOG** ) _→_ **SVC, LDA, LR** : This is similar to the above combination, with the difference that HOG is used instead of PCA. We tried this combination on artifacts that would have distinctive straight edges in their appearance which HOG is good at capturing: _Screen Tearing_ , _Shapes_ , _Shader_ , _Line Pixelation_ . 

- **Anomaly Measure** _→_ ( **HOG** ) _→_ **Threshold** : This computationally cheap combination produced good results on artifacts that typically have sharp color contrasts with the neighboring pixels. We tried this on all artifacts except for _Triangulation_ , _Screen Tearing_ , and _Discoloration_ . 

Table 2 illustrates the best performing feature representation and classifier combinations that were used for each artifact. We discovered that even though CNNs and random forests are widely and successfully used in computer vision and classification tasks respectively, Logistic Regression outperforms them in most of our artifact detection tasks, especially given their relatively low training time. We used Logistic Regression model provided by the sklearn package[15] and used their default arguments; that is _L_ 2 norm for penalization and a regularization strength of _c_ = 1 _._ 0. As with LR, we used the sklearn SVC model (RBF kernel) to perform binary classification of the extracted features. 

8 

A PREPRINT - DECEMBER 1, 2020 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0009-01.png)


<!-- Start of picture text -->
ParallelLines<br>Classifier<br>Data<br>ScreenTearing<br>Feature Classifier Logistic<br>Representation ： Regression<br>y'e{0, 1}<br>MorseCode<br>Classifier<br>ci e RM<br>for i = 1...N z'eR 10<br><!-- End of picture text -->

Figure 12: The Architecture of the Ensemble Model. The input consists of _N_ observations with _M_ features. The ensemble produces a binary output of “normal" or “corrupted”. 

# **5 Training and Testing of the Ensemble** 

Here we describe the data used for our experiments and the training process of the ensemble in three stages. In training stage I we trained the specialized classifiers for each glitch, that is, the components of our ensemble just like any other ensemble. For combining the results of the specialized classifiers, using the OR logic - which is the most basic combining method - did not seem reasonable for our application, therefore we used a Logistic Regression instead [16, 17]. That is because, if some of our specialized classifiers happened to have a pattern in false classifications - for example when the _Screen tearing_ and _Shader_ models tend to label a normal image as corrupted while no other specialized classifier would - the Logistic Regression has a much better tendency to capture that than the OR logic. Therefore, we used training stage II to train the ensemble Logistic Regression. Finally, to test the generalizabilty of our classifier to new games, we tested the ensemble on a dataset consisting of games that have never been seen by either the specialized classifier or the ensemble Logistic Regression. These three stages are explained in detail in the following paragraphs. 

## **5.1 Data** 

We applied _Glitchify_ to generate the artifacts described previously, to obtain a large dataset for training. The initial, uncorrupted images were collected by downloading long (2-6 hour) gameplay videos from 30 different games. We then extracted around 2,000 images from each game until we had a total of 50,000 images. After extracting all the images, we visually inspected all of the images to make sure they appeared glitch-free. We then added all the 12 different types of artifacts to half of the images, leaving the other half unchanged and labeled them as normal (glitch-free) images. 

We split this dataset of 50,000 images into three: A, B and C consisting of approximately 35,000, 7,500 and 7,500 images respectively . Dataset A consisted of gaming images from 24 games and was the largest dataset of the three. It was used to train specialized classifiers. Each specialized classifier was responsible for capturing only one type of graphic corruption. Dataset B contains gaming images from 3 games distinct from those in Dataset A, and it is used to train a Logistic Regression model that combines the outputs from the specialized classifiers and makes a final prediction on whether the input image is corrupted or not. Dataset C is the holdout dataset which is reserved for testing of the ensemble model. All of the data 

## **5.2 Training Stage I** 

During this stage, we trained the specialized classifiers. For this training procedure, we extracted images from 24 games (dataset _A_ in Table 1), labeled 2400 of these images as normal (artifact-free) and applied _Glitchify_ to the rest, obtaining around 1,500 corrupted frames per artifact. It should be noted that the training sets for each of the specialized classifiers were mutually exclusive (they did not share any normal images in common). A variety of models introduced in sections 4 were paired with features from section 3 and trained as binary classifiers for each artifact type. We used a 50 _/_ 50 train-test split of the data. The best-performing feature/model combinations were chosen based on the accuracy and recall and are recorded in table 2. The performance of these specialized classifiers on the test set (i.e. on familiar games) is shown in figure 13. 

9 

A PREPRINT - DECEMBER 1, 2020 

||Game|Dataset|Stage of Usage|
|---|---|---|---|
|1|Ancestor Legacy|||
|2|Control|||
|3|Detroit: Become Human|||
|4|Devil May Cry 5|||
|5|Dirt Rally 2|||
|6|Far Cry 5|||
|7|Final Fantasy|||
|8|Hollow Knight (2d)|||
|9|GTA|||
|10|Overcooked<br>|||
|11|League of Legends|||
|12|Assassin’s Creed|||
|13|Star Control: Origins|A|Training Stage I|
|14|Total War: 3 Kingdoms|||
|15|Star Craft 2|||
|16|Unravel 2|||
|17|Kingdom Come|||
|18|Metro Exodus|||
|19|Need For Speed Payback|||
|20|Mutant Year Zero|||
|21|Rage 2|||
|22|Resident Evil|||
|23|Strange Brigade|||
|24|The Sinking City|||
|25|Battlefield|||
|26|i<br>DOTA 2|B|Training Stage II|
|27|Hob|||
|28|Civilization 6|||
|29|Crackdown 3|C|Ensemble Testing|
|30|Forza Horizon|||



Table 1: Best performing feature representation/classifier combination for each artifact. 

## **5.3 Training Stage II** 

After training the specialized classifiers, we form an ensemble by training an LR model that takes the concatenated outputs of the specialized classifiers as input, and outputs a 0 (normal) or 1 (corrupted). To ensure generalizability across games, our dataset for this training stage comprised of 3 games (dataset _B_ in Table 1) that were _never seen_ by the specialized classifiers. The dataset for this stage consisted of 1650 normal images and 150 images of each type of artifact. A 75 _/_ 25 train-test split was applied to the data. At this stage, all of the specialized classifiers are shown normal images in addition to all types of artifacts. The performance of the specialized classifiers on the test set (i.e. on new games) is reported in figure 14. Given that the real-world application of this ensemble is expected to work well on games that have not been seen before, we did not train the Logistic Regression on familiar games. 

## **5.4 Testing the Ensemble** 

The goal of this stage is to measure the generalizability of the ensemble model as a whole across different games. The dataset for this testing stage comprised of 3 games that are never seen by the ensemble (dataset C in Table 1), with 1650 normal images and 1800 corrupted images, which is 150 for each artifact type. The results are reported in figure 15. 

10 

A PREPRINT - DECEMBER 1, 2020 

|Artifact|Feature Representation|Classifier|
|---|---|---|
|_Shapes_|FT + Resize|LR|
|Line pixelation|Anomaly Measure + Dilation|Threshold|
|_Shader_|Resize + HOG|LR|
|Morse code|FT + Resize|SVC|
|_Parallel Lines_|FT + Resize + PCA|LR|
|Dotted line|FT + Resize + PCA|LR|
|Stuttering|FT + Resize + PCA|LR|
|Triangulation|FT + Resize + PCA|LDA|
|_Discoloration_|FT + Resize + PCA|LR|
|_Screen tearing_|Resize + HOG|LR|



Table 2: Best performing feature representation/ classifier combination for each artifact 

# **6 Results** 

## **6.1 Evaluation Metrics** 

To evaluate the performance of our models, we used three different metrics: accuracy, precision and recall. We refer to corrupted images as _positive_ and normal images as _negative_ . 

## **6.2 Performance of our Model on Familiar Games** 

We first tested the performance of the specialized classifiers and the ensemble model on familiar games. Figure 13 illustrates the performance of the specialized classifiers on familiar games where we used the held out test set from training stage I (dataset A). Figure 15 illustrates the performance of the ensemble Logistic Regression on familiar games where we used the heldout test set from training stage II (dataset B). 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0011-08.png)


<!-- Start of picture text -->
Accuracy Precision Recall<br>0.75<br>0.5<br>0.25<br>iangulationarallel Lines Screen Tearing<br><!-- End of picture text -->

Figure 13: The performance of individual classifiers on a test set consisting of familiar games. 

## **6.3 Performance of our Model on New Games** 

An important metric in assessing artifact detection models is generalizability. In our case, generalizability refers to the ability of the model to perform well on images extracted from games that have not been encountered before. We will measure both the generalizability of the ensemble Logistic Regression and that of the specialized classifiers. 

11 

A PREPRINT - DECEMBER 1, 2020 

In training stage 2, even though the Logistic Regression model is trained using the games in dataset B, the specialized classifiers have never seen any image from dataset B. Therefore we used images from dataset B to test and evaluate the generalizability of the specialized classifiers. We also tested the generalizability of the ensemble model on dataset C which neither the ensemble model nor the individual classifiers have seen before, and obtained an accuracy of 69%. Figure 14 shows the testing results of each individual classifier. 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0012-02.png)


<!-- Start of picture text -->
Accuracy Precision Recall<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>del<br>sh sh<br>arallel Lines rse Code<br>reen<br>Triangulation<br>Figure 14: The performance of individual classifiers on a test set consisting of new games.<br>Accuracy Precision Recall<br>0.75<br>0.50<br>0.25<br>0.00<br>LR (Familiar Games) LR (New Games)<br><!-- End of picture text -->

Figure 15: Ensemble logistic regression on new vs. familiar Games 

# **7 Discussion** 

We now discuss possible interpretations of our results in addition to their limitations and sources of possible bias. One fundamental concern relates to our generated dataset and its representation of the actual graphics corruptions that occur during gameplay. First, our approach in developing the _Glitchify_ program consisted of classifying artifacts into categories based on their appearance, however, the viability of this procedure is debatable. Although the structure and design of _Screen tearing_ and stuttering were sufficiently understood and formally expressed, our definition of _Shader_ / _Shapes_ and _Line pixelation_ artifacts, however, might be too narrow to capture all of the variations of these 

12 

A PREPRINT - DECEMBER 1, 2020 

corruptions seen in reality. This discrepancy might be responsible for some bias present in our artificial dataset, which in turn affects all further results. Second, another data-related concern comes from the frames we extracted from games to feed into _Glitchify_ . We require that all these frames are normal, i.e. do no contain any corruptions, before the application of _Glitchify_ . To ensure this holds, we manually processed collected images in an attempt to perform a first-order quality check. Due to surrealistic contents of most games, working with individual frames rather that a continuous and dynamic gameplay makes it harder, if not impossible, to correctly discriminate between unwanted artifacts and intentional design. Figure 16 displays examples of such images. 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0013-02.png)


Figure 16: Normal images that look corrupted when taken outside the context of the game. The image on the left has stuttering patterns in the top left section of the frame. The image on the right has green glitchy patterns in the left section of the frame. 

Regarding the individual models, the accuracy on the test set drops from training stage 1 (figure 13) to training stage 2 (Table 14). This is mainly due to the fact the models in training stage 2 have never seen the games they are being tested on. In other words, the number and variation of the games in dataset A were not sufficient to ensure generalizabilty of the specialized classifiers across different games. One season for getting a high number of false negatives (contributing to low precision and accuracy) is that the artifacts that were added through _Glitchify_ are too subtle, as we can see in figure 17. 

In this application, however, the recall rate is the most important metric to consider as it is crucial to make sure that during gameplay, we detect as many corrupted images as possible so we can fix them. In training stage 2, we can see that most models produce good recalls on games they have never seen, showing a good degree of generalizability. The artifacts comprising _Discoloration_ and _Screen tearing_ have relatively low recall scores in training stage 2 (0.66 and 0.5 respectively) versus 0.95 and 0.80 in training stage 1, demonstrating that those models overfit the training data and are not generalizable to new games. These two artifacts are especially challenging, because as we can see in figure 18, it is possible for images to have a natural separation line or color gradients which will end up confusing the _Screen tearing_ and _Discoloration_ classifiers respectively. 

We speculate that the low accuracy score we have obtained on the heldout test set is due to the “glitchy" look of one of the games we have included in dataset C (Crackdown 3). 

# **8 Conclusion** 

In this proof of concept study, we developed a set of algorithms and software that automatically detects graphics corruption in frames from video games. Based on a sample of screen corruption examples provided by AMD, 10 of the most common content-unrelated artifacts were selected, described, and then recreated with the _Glitchify_ program. With the help of _Glitchify_ , a dataset of 50,000 images was created by adding 10 different types of artifacts to normal frames extracted from 34 modern video games. Each of the 10 forms of corruption was used to train a basket of models that included Logistic Regression, Support Vector Machines, and Linear Discriminant Analysis. The output probabilities of these individual classifiers were used for training a mixed experts Logistic Regression model intended to carry out the final classification decision. The overall accuracy on the _Glitchify_ -produced test set based on games unseen during training is 69%. 

Overall, this study has demonstrated several important results. The accuracy of the models trained on _Glitchify_ indicates that synthetic generation of defects can be an efficient mechanism to train models to identify real corruption. Put another 

13 

A PREPRINT - DECEMBER 1, 2020 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0014-01.png)


Figure 17: Visualization of False Negatives. Both of these images are corrupted through _Glitchify_ . The left image has a _Shapes_ artifact which is subtly visible in the top left corner inside the red circle. The right image has a _Shapes_ artifact which is hardly visible inside the red circle. 


![](images/Davarmanesh_2020_Automating_Artifact_Detection_in_Video_Games.pdf-0014-03.png)


Figure 18: Visualization of False Positives. On the left, we have a horizontal separation line, causing the _Screen tearing_ classifier to label this image as “corrupted". On the right, we have a green color gradient (in form of a hexagonal), causing the _Shader_ classifier label this image as “corrupted". 

way, the simple models for synthetic corruption described previously accurately represented some of the actual defects that occur in software or hardware. This hints that synthetic data can be used to efficiently train machine learning models for visual corruption. This result should be explored more generally. If true, this is an important result, because this is an effective means of generating labelled data _en masse_ , and circumventing the need for large, labelled datasets. 

Another important contribution of this work is demonstrating that a basket of models can be used as an efficient classifier of visual defects. No single model outperformed the others for identifying all forms of corruption. The efficacy of ’mixture of experts’ approaches are well-understood in other domains in machine learning, but to the authors’ knowledge, have not been previously demonstrated in the visual corruption domain. We note that Generative Adversarial Networks could be used in the future for artifact creation. We did not use them in this work owing to the limited and small number of real world artifact examples available to us, as GANs are computationally expensive and require large amounts of data to achieve superior performance. 

There are a few points that were not the main focus of this paper but could improve the results. First, we found that contrary to our assumptions, LR (a shallow model) outperformed CNN (a deep learning model for image classification) in most if not all of the cases. We expect that a larger dataset for the purpose of training in addition to a more exhaustive hyperparameter tuning would prove benefical to the use of CNNs. Second, we did not perform any significance testing to see which feature/model combination performs the best. Adding this step to analysis would certainly make it more rigorous. Lastly, we did not consider the possibility of having multiple kinds of artifacts in the same image. For example, it is possible to have _Stuttering_ and _Screen Tearing_ appear in a single frame, but it was not among the primary goals of this paper to be able to catch such artifact combinations. While we realize this is a preliminary work, we believe that this work is a good starting point that can help facilitate future research on the topic of automating artifact detection which would in turn lead to significant quality improvement of video games followed by an increase in gaming revenue. In addition to individual frames, the model we have created is able to work on videos and capture glitches in real time gameplay as we demonstrate in a short demo here: `https://youtu.be/AiZ0Dae7jW4` . Further work needs to be 

14 

A PREPRINT - DECEMBER 1, 2020 

done in order to improve the accuracy of our classifier as well as potentially fixing the artifact before it is displayed to the user. 

# **References** 

- [1] 2019 Essential Facts About the Computer and Video Game Industry kernel description, 2019. 

- [2] Dean Takahashi. Superdata: Games hit $120.1 billion in 2019, with fortnite topping $1.8 billion, Jan 2020. 

- [3] Chris Lewis, Jim Whitehead, and Noah Wardrip-Fruin. What went wrong: a taxonomy of video game bugs. In _Proceedings of the fifth international conference on the foundations of digital games_ , pages 108–115. ACM, 2010. 

- [4] Sanctuary conduit pixelated screen bug., 2019. 

- [5] Victor Moya, Carlos Gonzalez, Jordi Roca, Agustin Fernandez, and Roger Espasa. Shader performance analysis on a modern gpu architecture. In _Proceedings of the 38th annual IEEE/ACM International Symposium on Microarchitecture_ , pages 355–364. IEEE Computer Society, 2005. 

- [6] Timofey S. Chernov, Vitali M. Kliatskine, and Dmitry P. Nikolaev. A method of periodic pattern detection on document images. In _ECMS_ , 2015. 

- [7] N. Dalal and B. Triggs. Histograms of oriented gradients for human detection. In _2005 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR’05)_ , volume 1, pages 886–893 vol. 1, June 2005. 

- [8] Ning Ma, Yu Peng, Shaojun Wang, and Philip Leong. An unsupervised deep hyperspectral anomaly detector. _Sensors_ , 18:693, 02 2018. 

- [9] Francesco Verdoja and Marco Grangetto. Graph Laplacian for Image Anomaly Detection. _arXiv e-prints_ , page arXiv:1802.09843, Feb 2018. 

- [10] Laurens van der Maaten, Eric Postma, and H Herik. Dimensionality reduction: A comparative review. _Journal of Machine Learning Research - JMLR_ , 10, 01 2007. 

- [11] Michael E. Wall, Andreas Rechtsteiner, and Luis Rocha. Singular value decomposition and principal component analysis. _In A Practical Approach to Microarray Data Analysis_ , 5, 09 2002. 

- [12] Nathan Halko, Per-Gunnar Martinsson, and Joel A. Tropp. Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions. _SIAM Review_ , 53:217–288, 01 2011. 

- [13] N. Benjamin Erichson, Sergey Voronin, Steven L. Brunton, and J. Nathan Kutz. Randomized matrix decompositions using r. _ArXiv_ , abs/1608.02148, 2016. 

- [14] Thomas G. Dietterich. Ensemble methods in machine learning. In _Multiple Classifier Systems_ , pages 1–15, Berlin, Heidelberg, 2000. Springer Berlin Heidelberg. 

- [15] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay. Scikit-learn: Machine learning in Python. _Journal of Machine Learning Research_ , 12:2825–2830, 2011. 

- [16] Maurice J Schmeits and Kees J Kok. A comparison between raw ensemble output,(modified) bayesian model averaging, and extended logistic regression using ecmwf ensemble precipitation reforecasts. _Monthly Weather Review_ , 138(11):4199–4211, 2010. 

- [17] Heri Kuswanto, Ayu Asfihani, Yogi Sarumaha, and Hayato Ohwada. Logistic regression ensemble for predicting customer defection with very large sample size. _Procedia Computer Science_ , 72:86 – 93, 2015. The Third Information Systems International Conference 2015. 

15 

