UNDER REVIEW 

1 

# On the Element-Wise Representation and Reasoning in Zero-Shot Image Recognition: A Systematic Survey 

Jingcai Guo, _Member, IEEE,_ Zhijie Rao, Zhi Chen, _Member, IEEE,_ Song Guo, _Fellow, IEEE,_ Jingren Zhou, _Fellow, IEEE,_ and Dacheng Tao, _Fellow, IEEE_ 

**Abstract** —Zero-shot image recognition (ZSIR) aims to recognize and reason in unseen domains by learning generalized knowledge from limited data in the seen domain. The gist of ZSIR is constructing a well-aligned mapping between the input visual space and the target semantic space, which is a bottom-up paradigm inspired by the process by which humans observe the world. In recent years, ZSIR has witnessed significant progress on a broad spectrum, from theory to algorithm design, as well as widespread applications. However, to the best of our knowledge, there remains a lack of a systematic review of ZSIR from an element-wise perspective, _i.e._ , learning fine-grained elements of data and their inferential associations. To fill the gap, this paper thoroughly investigates recent advances in element-wise ZSIR and provides a sound basis for its future development. Concretely, we first integrate three basic ZSIR tasks, _i.e._ , object recognition, compositional recognition, and foundation model-based open-world recognition, into a unified element-wise paradigm and provide a detailed taxonomy and analysis of the main approaches. Next, we summarize the benchmarks, covering technical implementations, standardized datasets, and some more details as a library [link]. Last, we sketch out related applications, discuss vital challenges, and suggest potential future directions. 

**Index Terms** —Zero-Shot Learning, Pattern Recognition, Representation Learning, Image Processing, Computer Vision. 

✦ 

## **1 INTRODUCTION** 

W techniques, automated image recognition models areITH the continuous advancement of deep learning gradually becoming comparable to or even better than humans. The success relies on ingenious network architectures and, more importantly, massive data along with accurate annotations. However, the deficiencies are also obvious. On the one hand, the cost of data collection can be huge. For example, despite being a representative largescale dataset, ImageNet [1] contains 14 million images with 21,814 categories, whose coverage is still far fewer than real-world scenarios, _i.e._ , a conservative estimate suggests that there are at least 3 million species only for the board ‘ _Insect_ ’ category. On the other hand, image samples of some categories, such as rare/extinct species, rare medical cases, and privacy-sensitive data, are usually limited or even unavailable. Moreover, the requirement for modern deep models has also become more complex, not only to know what an object is but also to describe its accurate states [2], [3], e.g. the ‘ _Sliced_ ’ apple and an ‘ _Old_ ’ dog, etc. 

_Jingcai Guo and Zhijie Rao are with Department of Computing, The Hong Kong Polytechnic University, Hong Kong SAR, China (e-mail: jcjingcai.guo@polyu.edu.hk, zhijie96.rao@connect.polyu.hk)._ 

_Zhi Chen is with School of Electrical Engineering and Computer Science, The University of Queensland, Brisbane QLD 4072, Australia (e-mail: zhi.chen@uq.edu.au)._ 

_Song Guo is with Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Hong Kong SAR, China (e-mail: songguo@cse.ust.hk)._ 

_Jingren Zhou is with Alibaba Group, Hangzhou 311121, China (e-mail: jingren.zhou@alibaba-inc.com)._ 

_Dacheng Tao is with College of Computing and Data Science, Nanyang Technological University, Singapore (e-mail: dacheng.tao@ntu.edu.sg)._ 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0001-15.png)


<!-- Start of picture text -->
(a) Zero-Shot Object Recognition (b) Zero-Shot Compositional Recognition<br>  (1))   (1))<br>(ll) Test Phase (ll) Test Phase<br>(c) Foundation model-Based Open-world Recognition<br>contrastive<br>generation<br>(1 ) Pre-training Phase (ll) Zero-Shot Adaptation<br><!-- End of picture text -->

Fig. 1. Three tasks of ZSIR: (a) ZSOR utilizes shared attributes/texts to identify unseen categories; (b) ZSCR infers unseen compositions by learning from seen objects and states; and (c) FBOR exploits the broad fundamentals learned by pre-trained VLMs to implement zeroshot recognition directly in downstream tasks. 

The superposition of states and objects incurs a geometrical increase in the difficulty of data collection and annotation. In recent years, more and more interests have moved from coarse- to fine-grained scenarios to endow models with the ability to discriminate microscopic characteristics that mimic the human recognition process [4], [5]. For example, one can identify ‘ _Zebra_ ’ by recognizing an animal with ‘ _blackand-white_ ’ (color) and ‘ _stripes_ ’ (physical trait), implying that human cognition of upper concepts can be converted into 

UNDER REVIEW 

2 

the dismantling and reconstruction of base _elements_ and further motivate the development of element-wise learning (EWL) in image recognition tasks. Concretely, the objective of EWL is to construct a bottom-up paradigm by executing element-wise representation and reasoning, _i.e._ , a pyramidal knowledge architecture from micro to macro, attribute to object, and local to global. In particular, elements are carriers of properties [6], which describe the meta concepts of samples. The concepts or descriptors conveyed by an element vary depending on the specific tasks, like concrete components, e.g., ‘ _Wings_ ’ in recognizing bird species [7], or abstract descriptions, e.g., ‘ _Studying_ in recognizing scenes [8]. 

Employing element-wise representation to capture discriminative elements is already customary for fine-grained classification task [4], [5], [9] and has also been proven effective in many other areas, such as face recognition [10], image retrieval [11], and visual question answering [12]. On top of that, element-wise reasoning is employed to assemble a complex set of elements to achieve the recognition. The very early stage began with systematic and structured combinational logic such as predicate logic, boolean logic, and so on [13], and then researchers explored the relationship between combinational elements and objects in visual recognition tasks [14], [15]. Afterward, modern technologies are also designed to follow the idea of combinational reasoning, such as deformable network [16] and graph [17]. 

Zero-shot image recognition (ZSIR), as a well-defined visual-to-semantics mapping problem adapted for unseen domains, has attracted increasing attention in most recent years and made profound progress [18]. ZSIR employs texts/words as the medium to bridge the image visual disparity between seen and unseen categories, thus generalizing the models to recognize unseen domains. Simply put, the visual features are compressed into the shared semantics, and the model unifies the shared semantics and visual features of the seen categories to reason images from unseen categories. Compared to other low-shot schemes such as few-shot learning [19] and one-shot learning [20], ZSIR reduces the data requirement to zero, thus completely releasing the data collection and annotation pressure. Moreover, compared to another similar open-world problem, _i.e._ , out-of-distribution (OOD) detection [21], ZSIR is designed to assign precise labels for unseen data instead of simply categorizing them as OOD samples, which is usually more favorable in real-world applications. 

In practice, ZSIR and EWL are highly compatible in the recognition process that well-mimics the way humans observe the world, _i.e._ , learning the basics through finegrained visual-to-semantics interaction to identify concepts. Moreover, ZSIR can also be inherently considered as a natural extension of EWL towards the open-environment scenarios, _i.e._ , infer unseen categories with novel combinations of learned base elements. Therefore, their integration can provide a powerful and promising solution for real open-environment deployment. However, existing studies on ZSIR and EWL are usually fragmented and independent of each other, lacking a systematic investigation that summarizes their integration with a unified paradigm. Although some related reviews [22]–[24] have been presented for ZSIR in recent years, they do not delve in-depth into element-wise techniques. Worse still, existing reviews focus only on zero- 

shot object recognition, which is only one subtask of current ZSIR, and thus are constrained from sufficiently presenting the holistic portrait of ZSIR. To fill the gap, we conduct an extensive survey to thoroughly investigate recent advances in the development of element-wise ZSIR approaches and attempt to integrate the three mainstream tasks of ZSIR, including object recognition, compositional recognition, and foundation model-based open-world recognition, to provide a unified and more comprehensive review. 

In summary, our contributions are four-fold: 

- We, for the first time, integrate three mainstream ZSIR tasks, _i.e._ , object recognition, compositional recognition, and foundation model-based openworld recognition, to provide a comprehensive review from an element-wise perspective. 

- We discuss the differences and synergies of different ZSIR tasks and analyze the key challenges. We summarize related cutting-edge techniques and provide a new taxonomy of element-wise ZSIR. 

- We collect and summarize some benchmarks, including implementations, datasets, and some more details, as a library for follow-up research. 

- We present the widespread applications, discuss vital challenges and suggest potential future directions. 

## **2 OVERVIEW** 

### **2.1 Mainstream Tasks** 

### _2.1.1 Zero-Shot Object Recognition_ 

Classic zero-shot learning (ZSL) is the most common setting for ZSIR [18], addressing the challenge of classifying images that come from novel unseen categories without observing any prior visual samples before [18]. In ZSL, the annotations such as attributes, words/sentences, or semantic embeddings ( _i.e._ , we use _semantics_ uniformly later) are shared to describe categories at a high level. During training, only image samples of seen categories are available, while the model is trained to recognize unseen categories. Hence, the shared semantics serve as the crucial link between seen and unseen categories. To fully adapt to real-world scenarios, generalized ZSL (GZSL) [22] further extends the above setting to a more realistic one by requiring both seen and unseen categories to be jointly recognized during inference. Most recent studies encompass both ZSL and GZSL settings and are collectively referred to as zero-shot object recognition (ZSOR) in this survey ( _i.e._ , top-left of Fig. 1). 

### _2.1.2 Zero-Shot Compositional Recognition_ 

Another critical capability in the recent ZSL research is to describe the sample’s relevant states, such as recognizing whether an apple is sliced or raw instead of simply classifying it as an object. Such capability is essential for developing models with a deeper understanding of the world and is also a key component in building human-like intelligence [25]. Inspired by it, compositional learning has emerged in ZSL to explore combinational reasoning capabilities [2], [3], [26]. Concretely, the model is trained from image samples and their corresponding compositional states and objects, and is expected to recognize both seen and novel unseen compositions during inference. In particular, 

UNDER REVIEW 

3 

each state and object appears at least once during training. The classic setting assumes that the labels’ prior is available, _i.e._ , some state-object compositions are filtered out, speeding up the inference. In contrast, the open-world setting [27] extends compositional ZSL by expanding the inference scope to the full set, _i.e._ , every state-object composition counts. Therefore, many irrational combinations can occur, and the model is expected to cull out on its own. We collectively refer to them as zero-shot compositional recognition (ZSCR) in this survey ( _i.e._ , top-right of Fig. 1). 

### _2.1.3 Foundation Model-Based Open-World Recognition_ 

Both ZSOR and ZSCR fall short of achieving complete openness when faced with the open-world scenario, as their objectives and predictions remain fixed and well-defined. A critical question arises: can models learn broad and foundational knowledge and adapt seamlessly to unknown tasks? The advent of large vision-language pre-trained models (VLMs) [28], [29] offers a promising solution. These models focus on broad vision-language interactions, learning vast amounts of elemental knowledge without a specific goal, _i.e._ , much like humans learn about the world through observation. Remarkably, they exhibit excellent zero-shot generalization ability, performing well on various unseen domain image recognition tasks without further training. This capability has found wide applications, particularly in low-shot scenarios [30], [31]. However, recent studies [32], [33] suggest that the zero-shot potential of VLMs is not fully realized. In response, foundation model-based open-world recognition (FBOR) has been developed to push such a limit in foundation models ( _i.e._ , bottom of Fig. 1). 

### **2.2 Comparison** 

_i) Differences._ ZSOR and ZSCR both run in relatively narrow environments, _i.e._ , the categories to be predicted are known. Despite some studies proposing open-world ZSCR, the essence is only to extend the label set from a subset to the full set. FBOR, on the other hand, is task-agnostic, with the need to learn a wider range of knowledge ahead of time to cope with unknown challenges. In general, the element annotations of ZSOR are usually larger and more detailed, while ZSCR contains only individual state and object (category) annotations. On the other hand, the element annotations of ZSOR are category-level and thus may shift on individual instances, while the annotations of ZSCR are instance-level. Moreover, the goal of ZSOR is to recognize objects composed of different attributes, whereas the goal of ZSCR is to recognize combinations composed of different states and objects. _ii) Commonalities._ As mentioned earlier, element-wise representation and reasoning are motivation shared by several tasks, _i.e._ , learning the visual metaconcepts corresponding to text annotations, and then conducting combinational reasoning to recognize novel upperlevel concepts. In addition, many techniques are common across several tasks, such as attention mechanism, graph modeling, etc., which we will discuss further in Sect. 6.3. 

### **2.3 Challenge** 

### _2.3.1 Fine-Grained Visual Analysis_ 

Element-wise ZSIR requires detailed visual anatomy to echo the semantics and capture underlying meta concepts. 

ZSIR has fine-grained semantic information to describe the element-wise characteristics. However, due to huge costs, images in hand typically lack enough element-wise annotations. Therefore, semantics and visual local clues are usually learned in a weakly supervised manner, and their matching accuracy cannot be fully guaranteed. Worse still, irrelevant clues, such as the backgrounds, can inevitably interfere with the learning quality. To address these issues, recent studies incorporated fine-grained visual analysis into ZSIR and have made certain progress, particularly in accuracy improvement. Studies of such kind mainly involve visual localization [34], [35], visual representation [36], [37], and visual-semantics correlation modeling [38], [39]. However, based on our observation, three challenges still hinder the fine-grained visual analysis in ZSIR, including _i) Elements Complexity, i.e._ , the number of element-wise annotations tends to be larger compared to category-wise annotations, and the corresponding visual features are much more subtle [7], [40]. In addition, the processing of abstract attributes is also a challenge due to the difficulty of finding the corresponding explicit visual clues; _ii) Visual Occlusion and Overlap, i.e._ , visual occlusion occurs between objects and backgrounds or between elements and elements, which may result in the absence of critical visual clues. Besides, visual overlap refers to multiple semantic expressiveness of the same visual clues [41]. For example, the model can hardly completely decouple the visual clues of ‘ _red_ ’ and ‘ _car_ ’ when recognizing a red car; and _ii) Visual Interaction, i.e._ , the independent semantics of visual clues can be vague or even ambiguous. For example, if a piece of skin is cut off from a cow’s trunk, it is hard to recognize which part or even which species the skin comes from. Thus, the semantic meaning of visual clues can also depend on the whole to varying degrees. 

### _2.3.2 Domain Sift_ 

Domain shift is a long-standing challenge in ZSIR, which refers to the distribution bias ( _i.e._ , towards seen categories) of visual features when mapped into semantic space [42]. The inducement of domain shift is the absence of visual prior in unseen categories, which makes the models favor too much on seen categories and thus learn biased mapping functions [43]. It further misleads the model in recognizing the embeddings of samples of unseen categories as somewhat seen categories that hinder the model’s generalization ability. Meanwhile, some other factors can also aggravate the domain shift problem. First, different imaging mechanisms cause variational views, lightings, backgrounds, etc. [44], and thus, the visual characteristics can be diverse even for samples of the same category. Domain adaptation and generalization [44]–[46] partially mitigates this issue in general recognition tasks, while ZSIR is much more challenging since domain shift and unknown prediction need to be accommodated at the same time. Second and more troublesomely, context dependency, _i.e._ , objects or states expressing the same semantic information may present very different visual characterizations in different contexts [47], [48]. For example, the object ‘ _tail_ ’ appears hairy and straight on a _horse_ but smooth and curly on a _pig_ , and the state ‘ _old_ ’ presents itself as the metallic luster of rust on a _car_ , while as the wrinkled skin on a _person_ . 

UNDER REVIEW 

4 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0004-02.png)


<!-- Start of picture text -->
Zero-Shot Prediction Test-Time Adaptation Unsupervised Adaptation<br>Cross Attention Network Design<br>Foundation model-Based<br>Prototype Learning Open-world Recognition Attention Separation<br>Local Visual Attention Visual-Attribute Matching Decoupling Representation Cross Attention<br>Element-Wise Zero-Shot<br>Data Manipulation Visual Component Analysis Relationship Modeling Graph Modeling<br>Image Recognition<br>Graph Modeling Contrastive Embedding<br>Attribute Component Analysis Dependency Modeling<br>Attribute Enhancement Feature Optimization<br>Attribute Refinement Technical Details Application Future Directions Aid Classification<br>Object Recognition<br>Compositional Recognition<br><!-- End of picture text -->

Fig. 2. An overview of the organization and taxonomy of this survey. 

### **2.4 Organization** 

To sum up, Fig. 2 outlines the overall organization as well as the taxonomy of this survey. Concretely, Sect. 3 first covers ZSOR techniques, including problem formulation and key algorithms. Similarly, Sect. 4 reviews ZSCR, and Sect. 5 introduces FBOR. Then, Sect. 6 details technical implementations, standardized datasets, and shared techniques. Sect. 7 explores widespread applications, and Sect. 8 suggests potential future directions. 

## **3 ZERO-SHOT OBJECT RECOGNITION** 

### **3.1 Problem Formulation** 

Given the seen domain _D_<sup>_s_</sup> = _{_ ( _x_<sup>_s_</sup> _, y_<sup>_s_</sup> _, a_<sup>_s_</sup> ) _|x_<sup>_s_</sup> _∈X_<sup>_s_</sup> _, y_<sup>_s_</sup> _∈ Y_<sup>_s_</sup> _, a_<sup>_s_</sup> _∈A_<sup>_s_</sup> _}_ , where _X_<sup>_s_</sup> , _Y_<sup>_s_</sup> , and _A_<sup>_s_</sup> denote visual samples, category labels, and semantics (e.g., a set of attributes), and similarly, let _D_<sup>_u_</sup> = _{_ ( _x_<sup>_u_</sup> _, y_<sup>_u_</sup> _, a_<sup>_u_</sup> ) _|x_<sup>_u_</sup> _∈X_<sup>_u_</sup> _, y_<sup>_u_</sup> _∈Y_<sup>_u_</sup> _, a_<sup>_u_</sup> _∈ A_<sup>_u_</sup> _}_ denote the unseen domain. Notably, _a_<sup>_s_</sup> _∪ a_<sup>_u_</sup> _∈_ R<sup>_m×k_</sup> are class-level semantics annotations, where _m_ denotes the number of categories and _k_ is the number of attributes. Without loss of generality, the task of ZSOR can be modeled as learning a mapping/relational function Ψ : _X →A_ , wherein _X_<sup>_u_</sup> is strictly inaccessible for training. During inference, the learned function Ψ is applied to recognize samples from the unseen domain only, _i.e._ , ZSL, or from both seen and unseen domains, _i.e._ , Generalized ZSL (GZSL). 

The success of ZSOR relies on the shared attribute between _A_<sup>_s_</sup> and _A_<sup>_u_</sup> , which act as the bridge between seen and unseen domains. The intuitive idea is to learn the visual representations corresponding to attributes, which is the notion of element-wise learning. However, due to the single target and relatively closed environment of object recognition, learning for Ψ can be transformed into a plain class-wise distribution matching problem. Class-wise distribution matching concerns neither the discrepancies of the bottom attributes nor the variations of fine-grained vision. It treats both visual and attribute features as a whole, and the objective is to reduce the distributional distance between the two to learn an unbiased mapping function. Mainstream techniques include semantic space design, generative approach, and regularization. Semantic space design is to search for a suitable low-dimensional space that perfectly 

matches visual and attribute embeddings [43], [49]. The generative approach is to simulate the visual features of unseen classes [50], [51] by training a generator that produces visual features based on attributes with the help of networks such as GANs [52]–[54], VAEs [55], [56] and generative flows [57], [58]. Regularization is imposing constraints to improve the mapping performance or robustness of the model. For example, Liu et al. [59] use an information entropy loss to reduce uncertainty. Despite the impressive results achieved by these methods, they provide limited insights for microoperations and bottom-up analyses and are, therefore, out of the scope of this survey. The readers can refer to other related surveys [23], [24] for a deeper understanding. 

Depending on the concrete elements the method operates on, we categorize the element-wise techniques into three broad categories, _i.e._ , _Visual Component Analysis_ , _VisualAttribute Matching_ , and _Attribute Component Analysis_ . Then, the methods are further categorized into different subcategories based on the specific techniques they use. 

### **3.2 Visual Component Analysis** 

Visual component analysis is the refined dissection of an image or its features, involving localization, modeling, and so on. Images often contain a large amount of redundant information, only a few of which are decisive for discrimination. At the same time, images lack fine-grained annotations. Therefore, the goal of visual component analysis is to reduce the interference of irrelevant information as well as noise, and prompt the model to focus on those critical visual parts. Commonly used methods can be classified into the following three sub-categories: _Local Visual Attention_ , _Data Manipulation_ , and _Graph Modeling_ . 

### _3.2.1 Local Visual Attention_ 

Attention mechanisms are effective to improve efficiency and accuracy in many visual tasks by mimicking human focuses. Motivated by this, local visual attention is to utilize the attention mechanism to identify the most valuable visual regions and reduce the influence of background or irrelevant regions. Specifically, local visual attention generates multiple masks for visual features. Each mask is a normalized weight matrix that reveals a significant region. Enhanced 

UNDER REVIEW 

5 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0005-02.png)


<!-- Start of picture text -->
Backbone Attention Network Feature<br>Mask Multiply Enhanced Feature<br><!-- End of picture text -->

Fig. 3. A schematic diagram of local visual attention. Visual features are passed through a sub-network to generate multiple masks, which are then multiplied to obtain enhanced features. 

features can be obtained by weighting the original features using mask, thus improving the discriminability (Fig. 3). Suppose that _x ∈_ R<sup>_C×H×W_</sup> denotes the visual feature, where _C_ , _H_ , and _W_ are the channel, height, and weight, respectively. Let _M_ = _F_ ( _x_ ) represents the attention mask, where _F_ denotes a small learnable network, e.g., 1 _×_ 1 convolutional network, and _M ∈_ R<sup>_N×H×W_</sup> denotes _N_ attention masks. Afterward, multiplying the masks with the original features yields _N_ regional features, which can be expressed as: 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0005-05.png)


<!-- Start of picture text -->
xregion =  {xm 1 , xm 2 , ..., xmN }, (1)<br><!-- End of picture text -->

where _xregion ∈_ R<sup>_N×C×H×W_</sup> and [ _m_ 1 _, m_ 2 _, ..., mN_ ] = _M, mi ∈_ R<sup>_H×W_</sup> . How to use these regional features to improve model’s performance. AREN [35] considers certain mask learned regions to be unimportant and therefore adopts an adaptive threshold to further filter out unimportant information, _i.e._ , region features smaller than the threshold are set to 0. RSAN [60] expects the regions learned by each mask to correspond to the attributes one by one. It uses max-pooling to get the representative value in each region feature and concatenates them into a onedimensional vector, after which it uses Mean Squared Error Loss to minimize the distance between this vector and the attribute embedding. Considering the existence of topological relationships between regions, RGEN [36] introduces graph modeling to maintain their potential connections. 

### _3.2.2 Data Manipulation_ 

Data manipulation has a same objective as local visual attention, _i.e._ , to search and localize the most critical regions. The difference is that the latter works at the feature space, whereas the former works at the image level. An intuitive approach is employing detection techniques to recognize parts of an object, such as a bird’s head, body, and claws. The detection network can provide coordinates for multiple parts simultaneously, allowing image patches to be cropped accordingly or deep features to be localized. This method introduces fine-grained semantic information that enhances the model’s classification ability [61], [62]. Additionally, it boosts the performance of generative methods, which often struggle with capturing fine-grained visual differences. For example, AGAA [63] utilizes a detector to extract region information that is fed into a discriminator, along with class 

embeddings generated by a generator. However, this technique is limited in practice since the detector’s performance heavily depends on part-level visual annotations, which are often impractical to obtain. 

To alleviate this problem, a series of unsupervised detection methods have been proposed. LDF [64] employs a coordinate generating network that generates coordinates directly from image features. Specifically, suppose _x ∈_ R<sup>_C×H×W_</sup> is the visual feature, and the coordinate can be expressed as: 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0005-11.png)


<!-- Start of picture text -->
Z = [ zh, zw, zl ] =  F ( x ) , (2)<br><!-- End of picture text -->

where _F_ is a learnable network. _Z_ is the window, _zh, zw_ denote the coordinates, and _zl_ denotes the length of the region. After that, the regions located at the coordinates are zoomed in and re-fed to the classification network. SGMA [34] incorporates local visual attention techniques to coordinates generation. Furthermore, SR2E [65] and ERPCNet [66] introduce the reinforcement learning paradigm, which induce the cropping behavior of the model by setting up special rewards and penalties to obtain the most discriminative sub-image. POPRNet [67] takes unsupervised detection technique. It generates multiple proposal regions for an image and then sorts and selects Top-K region features based on category confidence. ZSLViT [68] utilizes the patch split mechanism of ViT [69] to get multiple region features and later filters the key visual regions by calculating the attention weights between the regional and class tokens. 

Unlike the above approaches, to capture the key visual semantic embeddings, VGSE-SMO [70] takes a patch clustering approach. It utilizes an unsupervised segmentation algorithm to decompose images into multiple patches, after which individual patches are linked to class labels via a classification network. By doing so, the model can implicitly learn the relationship between classes and fine-grained visual patches that align better with each other. 

### _3.2.3 Graph Modeling_ 

Visual region localization helps models focus on important local features but often overlooks the potential relationships between regions. For example, a bird’s body parts are biologically connected, and treating them independently can cause semantic ambiguity due to a narrowed field of view. Sharing information between regions can mitigate this by preserving essential semantic context. Graph modeling techniques are well suited for handling such irregular non-geometric data with a structured message propagation mechanism [17]. In recent years, with the birth and development of graph convolutional networks (GCNs) [71], graph modeling techniques have been widely used in various computer vision tasks. 

Regional visual features are natural graph nodes and thus can be well embedded in graph modeling techniques. For example, GKU [37] constructs a graph for each sample to capture fine-grained local structural relationships. They redefine the visual-semantic mapping problem as a graphsemantic mapping problem, thus suppressing the influence of partial visual domain shift. However, GKU requires the dataset to be supported by fine-grained regional annotations. Without the supervision of manual annotations, RIAE [72] incorporates all regions into the graph node set. 

UNDER REVIEW 

6 

To mine the relationships between regions, it introduces cosine similarity to measure the weight of an edge between any two region nodes. GNDAN [73], on the other hand, first locates the visual regions corresponding to the attributes with cross attention techniques, and then later uses the graph for modeling. 

### **3.3 Visual-Attribute Matching** 

The goal of visual-attribute matching is to align visual features with their corresponding attributes by learning finegrained, element-wise representations through the pairing of visual-attribute embeddings. Unlike visual component analysis, this approach explicitly focuses on interacting with attributes, allowing for a better perception of subtle attribute variations and improved generalization to unseen domains. This text-driven visual learning aligns more closely with human learning patterns and presents a greater challenge. Current methods in this area can be categorized into two sub-categories: _Cross Attention_ and _Prototype Learning_ . 

### _3.3.1 Cross Attention_ 

Cross attention allows for the simultaneous processing of different sources of information and efficient modeling of their dependencies. Among them, dot product attention, due to its high computational efficiency and low space cost, is widely applied in many advanced models such as Transformer [74]. The core of dot product attention is to compute the similarity between query and key-value pairs to assign attention weights, and the similarity measure is the dot product of vectors. Given a query series _Q_ , a key series _K_ and a value series _V_ , the attention score can be formulated as: 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0006-07.png)


<!-- Start of picture text -->
Attention ( Q, K, V  ) =  softmax ( QK T ) V, (3)<br>√ dk<br><!-- End of picture text -->

where _dk_ denotes the dimension of the key vector used to scale the dot product result. When _Q_ , _K_ , and _V_ all come from the same input series, the attention score learns the dependencies between the parts of the series, _i.e._ , self-attention. When there are two different input series involved in the computation, the attention score learns the dependencies between the different series, _i.e._ , cross attention. 

To uncover the interactions between attributes and visual regions, the cross attention technique is naturally introduced into ZSOR (Fig. 4). For example, DAZLE [38] proposes a dense attention technique that assigns weights to each region based on attributes. Specifically, it utilizes the features output from the last layer of the convolutional network and treats each point on the feature as a region. The similarity between attributes and regions is then computed with cross attention. Suppose _x ∈_ R<sup>_C×r_</sup> denotes the visual feature with _r_ = _H × W_ regions. Let _a ∈_ R<sup>_d×m_</sup> denote the attribute vector, where _m_ is the number of attributes, and _d_ is the vector dimension. The cross attention score is calculated as: 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0006-10.png)


<!-- Start of picture text -->
exp( a T wx )<br>Attention ( a, x ) = (4)<br>� r exp( a T wx ) x,<br><!-- End of picture text -->

where _w ∈_ R<sup>_d×C_</sup> is a learnable matrix that ensures the visual and attribute vectors are in the same dimension space. 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0006-12.png)


<!-- Start of picture text -->
have pink head<br>have black beak<br>have white wing<br>Backbone Mapping Function Region Feature<br>Attribute Embedding Attention Map<br><!-- End of picture text -->

Fig. 4. A schematic diagram of cross attention. Attribute embeddings and region features compute similarity to obtain multiple attention maps. 

The weighted visual features reflect attribute preferences. After that, the attention scores of all the attributes are used for classification. GEM [75] employs the same approach, however it retains the maximum attention scores with maxpooling during classification. Composer [76] synthesizes the features of unseen classes with critical regions identified by attention mechanism, while AREES [77] exploits the regional features to improve the performance. 

Some studies resort to ViT [69] to model dependencies between vision and attributes [78]–[80]. The essential cross attention mechanism is identical. The difference is that ViT divides the image into patches, each of which is considered a visual region. In addition, bidirectional attention is explored in depth. It is important to know not only which region the attribute is attending to, but also which attribute the region is attending to. Based on this idea, several methods are developed. For example, MSDN [81] proposes a mutual distillation network to align attribute-region attention. Ge et al. [47] also integrate bidirectional attention techniques to improve the visual-attribute matching ability of the model. 

### _3.3.2 Prototype Learning_ 

The gist of prototype learning is to perform tasks like classification and regression using a set of representative samples, known as prototypes [82] to regularize the learning process. A prototype is a standardized example that captures the essence of a category or type, such as the mean vector of a set of vectors or the center of mass of a distribution. Prototype learning mimics human analogical reasoning by drawing conclusions based on typical examples. Its main advantage is its robustness in handling complex data distributions, particularly when there is overlap or imbalance between data categories. As a result, prototype learning is considered to be more effective for tasks like out-ofdistribution detection [83] and low-shot learning [84]. 

For visual-attribute matching, there is semantic overlap in the visual region. The same region may contribute to multiple attributes. Although cross attention is able to measure the contribution value by similarity, the lack of an explicit means of visual decoupling may lead to pseudo-correlation of visual-attributes. Therefore, learning a separate visual prototype for each attribute is a promising solution. When 

UNDER REVIEW 

7 

the prototype is acquired, the visual region can decide which attribute it belongs to by calculating the distance between the region vector and the prototype. It can be observed that cross attention discovers pairing relations through the similarity between the attribute and visual embeddings, while prototype learning discovers visualattribute pairing relations indirectly through the similarity between the embeddings of samples and prototypes. 

APN [85] first introduces prototype learning to visualattribute matching. It initializes a learnable prototype vector for each attribute and then calculates the similarity between the visual region and the prototype. After that, the largest region vector is taken as the attribute vector, and then regresses with the attribute embedding. In addition, it incorporates a decorrelation loss [86] to ensure the independence between individual attributes. DPPN [87] considers that the prototype possesses a seen-domain preference, which cannot capture the delicate instance-level attribute shift. Therefore, it is necessary to equip each instance with exclusive attribute prototypes. It proposes a progressive attribute localization method, which dynamically adjusts the prototype by locating attributes through the prototype while updating the prototype in turn. In addition, some other methods [47], [88]–[91] also achieve favorable results by using prototype learning. 

### **3.4 Attribute Component Analysis** 

Attributes serve as the crucial link between seen/unseen classes and provide essential supervisory signals for learning fine-grained visual representations. Consequently, the quality of the attribute space largely determines the upper limit of a recognition system’s performance. However, most attributes are manually created or pre-trained without proper adjustment, resulting in redundancy, noise, and unstructured relationships. To address this, attribute component analysis aims to optimize the attribute space through methods such as _Attribute Enhancement_ and _Refinement_ . 

### _3.4.1 Attribute Enhancement_ 

Attribute enhancement aims to optimize attribute embeddings to improve their discriminability, using techniques like key attribute localization and attribute space optimization. Key attribute localization functions similarly to visual attention, identifying and focusing on the most critical parts. The cross attention mechanism mentioned in Equation 4 is one of the attribute localization techniques, just changing the input sequences. In addition, LFGAA [92] designs a latent guided attention module. It assumes that each image has different attention for attributes and, therefore, introduces multiple subnetworks to generate exclusive attribute weights for each image. Attribute space optimization adjusts pre-trained attribute embeddings to reduce semantic overlap that affects discrimination, especially in finegrained datasets. For instance, many bird species share similar attributes, which makes distinguishing them challenging. For this reason, AREES [77] delineates the attribute embeddings with similar semantic distances into a cluster by K-means clustering algorithm, and the attributes in each cluster are subtracted from the cluster’s center of mass, _i.e._ , the mean vector, to obtain the enhanced attribute vector. APNet [93] introduces graph modeling to discover the logical 

relationships between classes and updates the attributes by propagating the attribute features of neighboring nodes. 

### _3.4.2 Attribute Refinement_ 

Since attributes are typically annotated by humans, the value they add from a human perspective to deep learning is uncertain. Attribute refinement seeks to address this by examining the design of attribute annotations, though few studies exist on the topic. MCZSL [94] points out that the quality of manual annotations is uncontrollable and time-consuming. Therefore, it attempts to design an automated attribute annotation scheme. Specifically, it obtains attribute descriptions from online media such as Wikipedia and designs a series of filtering strategies to filter out inappropriate attributes. DEDN [95] proposes a divide-andconquer attribute learning scheme. It argues that attribute annotations are confusing and lead to semantic asymmetry problems. For example, for the attributes describing scenes, _{studying, swimming}_ and _{stone, tree}_ are not in the same dimension, with the former denoting function and the latter denoting object. Therefore, it designs a dual expert network in which one expert network focuses on processing attribute information in different dimensions. 

## **4 ZERO-SHOT COMPOSITIONAL RECOGNITION** 

### **4.1 Problem Formulation** 

Suppose _S_ = _{s_ 1 _, s_ 2 _, ..., sn}_ is a set containing _n_ state elements and _O_ = _{o_ 1 _, o_ 2 _, ..., om}_ is a set containing _m_ object elements. Then a compositional set can be obtained as _Y_ = _{_ ( _s_ 1 _, o_ 1) _,_ ( _s_ 1 _, o_ 2) _, ...,_ ( _sn, om_ ) _|s ∈S, o ∈O}_ , which containing _n × m_ compositions. Now we have a seen domain _D_<sup>_s_</sup> = _{_ ( _x_<sup>_s_</sup> _, y_<sup>_s_</sup> ) _|x_<sup>_s_</sup> _∈X_<sup>_s_</sup> _, y_<sup>_s_</sup> _∈Y_<sup>_s_</sup> _}_ , where _X_<sup>_s_</sup> denotes the training image set and _Y_<sup>_s_</sup> _⊆Y_ is the label set. Similarly, we have an unseen domain denoted by _D_<sup>_u_</sup> = _{_ ( _x_<sup>_u_</sup> _, y_<sup>_u_</sup> ) _|x_<sup>_u_</sup> _∈X_<sup>_u_</sup> _, y_<sup>_u_</sup> _∈Y_<sup>_u_</sup> _}_ , where _X_<sup>_u_</sup> denotes the test image set and _Y_<sup>_u_</sup> _⊆Y_ is the label set. Data in the seen and unseen domains are disjoint, _i.e._ , _X_<sup>_s_</sup> _∩ X_<sup>_u_</sup> = _ϕ_ and _Y_<sup>_s_</sup> _∩ Y_<sup>_u_</sup> = _ϕ_ . The objective of ZSCR is to generalize to the unseen domain by learning the element-wise knowledge in the seen domain. Specifically, for closed-world compositional recognition, the goal is to learn a mapping function Ψ : _X →Y_<sup>_s_</sup> _∪Y_<sup>_u_</sup> , wherein _X_<sup>_u_</sup> is strictly inaccessible for training. Typically, the size of _Y_<sup>_s_</sup> _∪Y_<sup>_u_</sup> is smaller than that of _Y_ since some compositions are not feasible. For openworld compositional recognition [27], the goal is to learn a mapping function Ψ : _X →Y_ , assuming that which compositions are infeasible is unknown. 

We divide the cutting-edge techniques of ZSCR into three categories based on their core components, including _Decoupling Representation_ , _Dependency Modeling_ , and _Relationship Modeling_ . We then further split the sub-categories based on specific technical details or targets of action. 

### **4.2 Decoupling Representation** 

A common baseline approach involves mapping images to deep semantic space, computing similarity to text embeddings, and optimizing with cross-entropy loss. The goal is to learn the posterior probability _p_ ( _y|ψ_ ( _x_ )), where _y_ = ( _s, o_ ) and _ψ_ is a function mapping the image into the semantic 

UNDER REVIEW 

8 

space. This approach leads to model simplifying optimization by learning direct correspondences between visual features and labels, often missing independent effects of states and objects. For example, if the model has only seen _sliced apple_ , it may tightly associate _sliced_ with _apple_ and fail to recognize _sliced orange_ . An alternative is to separately predict the labels for states and objects to avoid semantic interference, known as decoupling representation. This approach aims to disentangle states and objects, encouraging the model to learn independent visual representations. By separately recognizing states and objects, the model can better generalize to new compositions. Decoupling representation focuses on learning posterior probabilities _p_ ( _s|ψs_ ( _x_ )) and _p_ ( _o|ψo_ ( _x_ )), where _ψs_ and _ψo_ are mapping functions. Mainstream approaches can be categorized as: _Network Design_ and _Attention Separation_ . 

### _4.2.1 Network Design_ 

Many studies resort to modifying the network structure to decompose visual features. Nan et al. [96] add two subnetworks at the bottom of the backbone network to extract state and object features, respectively, and then each predicts the corresponding labels and is trained with cross-entropy loss. CASUAL [41] employs a similar network structure. The difference is that it introduces a text-to-image mapping network that reverse maps text embeddings into visual space. Meanwhile, it uses the Hilbert-Schmidt Information Criterion, which is a non-parametric method for estimating the statistical dependence between samples of two random variables, to optimize training for ensuring state and object independence. ProtoProp [97] uses a prototypical network to learn independent representations. Specifically, regional features of images and prototypes of objects and states are computed for similarity and later optimized with crossentropy loss. Hu et al. [98] propose a two-layer decoupling network. First, three sub-networks are used to extract state, object, and composition features, respectively. In the second layer, the state and object features are fed into a reorganization network to synthesize into a composition, while the composition feature is fed into two other sub-networks for further decoupling. CAILA [99] uses CLIP as a visual coder, which inserts three adapters in the middle of the network to capture the state, object, and composition semantic information, respectively. It is worth mentioning that the three-branch network has become a common infrastructure for most approaches, _i.e._ , three sub-networks extract state, object, and composition visual features, respectively [100]. 

### _4.2.2 Attention Separation_ 

The motivation for attention separation is to dissect semantic features by capturing the parts of objects and states attended to separately. OADis [101] introduces a crosssample attention mechanism to refine features. It equips each sample with two companion samples, one with the same object and different state, and the other with the same state and different object. Afterwards, cross attention is performed with the corresponding samples separately to refine the semantic features. ADE [102] adopts a similar training paradigm. Unlike pre-matched pairs, Jing et al. [103] utilize image retrieval techniques to find suitable matching samples for object and state branches, after which 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0008-07.png)


<!-- Start of picture text -->
monkey<br>Middle Layer brown<br>Object-Guided Attention<br>Object/State Extracter<br><!-- End of picture text -->

Fig. 5. A schematic diagram of dependency modeling [107]. Object information is used as a signal to guide the extraction process of state features. 

they are used to enhance the representations. Zhang et al. [104] propose a gradient-based attention decomposition method. They view compositional recognition as a domain generalization problem, and one of the solutions is to learn domain-invariant features. To this end, they measure the variation of features by evaluating the difference in the back-propagation gradients of sample pairs to recognize the domain-invariant part. DFSP [105] firstly decouples text embeddings by prototype computation and, after that, uses the text embeddings and image features for cross-attention to decompose the visual features. Similarly, Troika [106] fuses multi-path prompt and cross attention to optimize text embeddings. 

### **4.3 Dependency Modeling** 

Decoupling techniques pursue the pure semantic representations while mitigating the bias toward seen compositional concepts, introducing the bias toward the single concept, _i.e._ , state or object. This bias comes from the fact that the same concept is represented differently in diverse contexts. Due to the existence of complex acting mechanisms in the real world, such as physical systems and biochemical reactions, the visual presentation of the same state on various objects varies greatly. For example, _old_ is represented as metal rust spots on _car_ , while it is shown as skin wrinkles on _person_ . Obviously, concise text annotations cannot capture such subtle differences, and the independent visual representations learned by the model from the seen domain are biased, hindering the recognition accuracy of the unseen domain. To address this problem, many studies are devoted to modeling the dependency relationship between states and objects. By introducing a priori information about states or objects to correct each other’s semantic representations or classification confidence, they can be better generalized to the unseen domain. In short, the goal of dependency modeling is to learn the conditional probabilities _p_ ( _s|ψs_ ( _x_ ) _, o_ ) and _p_ ( _o|ψo_ ( _x_ ) _, s_ ). The relevant technologies, according to the implementation objectives, can be categorized into _Feature Optimization_ and _Aid Classification_ . 

### _4.3.1 Feature Optimization_ 

The goal of feature optimization is to adjust each other’s feature representations by leveraging the semantic relevance of states and objects. Decoupled state/object features are expected to capture dependent semantic details while maintaining their discriminative semantic information. Visual feature optimization corrects the visual embedding distribution to avoid overfitting the seen domain caused by the model focusing on a single visual feature. For example, 

UNDER REVIEW 

9 

Panda et al. [108] set up multiple encoders between the state and object branching networks to transmit object features to the state network to model the dependency of the state on the object. The same idea is taken by CoT [107], which uses object information as cueing signals while introducing an attention-based method to capture state-related visual features (Fig. 5). Another approach is to optimize text features. Since text annotations are usually pre-extracted, they can hardly perceive dependency relationships. To this end, Nagarajan et al. [6] model states as operators, _i.e._ , encode the state as a mapping function rather than an embedding, and thus explicitly learn the semantic embedding of an object ”after it has been operated on”. SymNet [109] introduces two sub-networks, the decoupling network and the coupling network, which are used to learn independent and compositional representations of objects and states. CANet [110] recognizes the object labels of an image first and then corrects the text embedding of the state by using the object text embedding as a priori condition. 

### _4.3.2 Aid Classification_ 

Compared to adjusting the feature distribution, aid classification aims to directly introduce semantic information of objects/states to make the classifier more discriminative. In earlier work, Chen et al. [2] utilize support vector machines (SVMs) for compositional recognition. They learn the weights of SVMs by capturing state dependencies on objects and generalize to unseen compositions. SAD-SP [111] takes an intuitive approach by introducing an attention module in addition to the conventional decoupling network. State features are used to predict object soft labels and vice versa. The predicted soft labels are then used to weigh the predicted output of the conventional network. ProCC [112] performs information exchange at each layer of the state/object classifier. Specifically, it passes the output of one layer of the state classifier through a one-dimensional convolution and softmax, and then the output of the corresponding layer of the object classifier is multiplied with it and used as the input of the next layer, and vice versa. 

### **4.4 Relationship Modeling** 

Dependency modeling promotes the generalizability of models by exploring the intrinsic one-to-one state-object connections. Naturally, we wonder whether many-to-many complex mesh relationships, _i.e._ , interactions between multiple objects or states, contribute to model performance. Such relationships describe the latent logical relations of elements in the real world due to various factors, such as subject affiliation, visual similarity, co-occurrence, etc. To name a few, we would spontaneously categorize _broccoli_ and _spinach_ , separating _beef_ since they belong to different subjects; a _fork_ and a _spoon_ are more visually similar than an _umbrella_ , and also they have a higher probability of cooccurrence. Intuitively, an understanding of these relations facilitates logical inference. It is because humans have a remarkable ability to draw analogies, make connections, and imagine, thus reasoning and recognizing by tapping into the relationships between different elements. When we see a _furry black bear_ and know the similarities between _polar bears_ and _black bears_ , it is easy to migrate the state of _furry_ to 

_polar bears_ . Driven by this idea, relationship modeling aims to enhance the inference and representation capabilities of models by uncovering and maintaining potential relationships between states and objects. The dominant techniques can be summarized as _Cross Attention_ , _Graph modeling_ , and _Contrastive Embedding_ . 

### _4.4.1 Cross Attention_ 

To model the relationship, cross attention is used to capture similarities between text embeddings and thus correct text representations. BMPNet [113] introduces the cross attention mechanism to improve independent object/state representations. Specifically, for a state, the attention weights of the state and other states are first computed, and then the attention weights of an object are computed, resulting in an enhanced state representation. The object ditto. Unlike object/state relational modeling, CAPE [114] aims to reveal co-occurrence relations between compositions. It adapts the compositional features by calculating the attention weights between the text embeddings of the compositions. 

### _4.4.2 Graph Modeling_ 

As mentioned in the previous section, graphs are excellent tools for structured data and thus can be well adapted to the relationship modeling task. In earlier work, Cruz et al. [13] develop a logic tree to model relations between states and objects. They want the model to learn the notion of connectives such as _{and, or, not}_ to understand the potential connections between nouns. CGE [115] models the entire set of objects and the set of states. It treats each object and state as a graph node and then identifies edges between nodes by the composition labels. Graph convolutional network is later introduced to propagate the information. CVGAE [116] expects the model to be able to determine on its own whether there is a connection between objects and states and thus be adaptable to the open-world compositional recognition task. It designs a reconstruction task where the reconstruction network recovers the adjacency matrix based on latent variables. GIPCOL [117], on the other hand, fuses prompt learning and graph modeling. It employs CLIP as the backbone and takes the graph-encoded text embeddings as prompts to train. The graph neural network is involved in the learning process, thereby optimizing the text embeddings to fit the task better. 

### _4.4.3 Contrastive Embedding_ 

Contrastive embedding utilizes contrastive learning to optimize the semantic space and implicitly learn the relationships between samples. Contrastive learning [118], as a representative unsupervised learning method, demonstrates powerful semantic representational ability. It aims at clustering similar samples together and separating different samples. The learning mode is to constrain the semantic distance by comparing positive and negative examples, and the learned semantic distance reflects the affinity between the samples, _i.e._ , the semantic relationship. Therefore, many areas exploit contrast learning to optimize semantic embeddings. Unlike the attention mechanism and graph modeling described above, contrast learning does not predefine the relationship between samples explicitly but rather 

UNDER REVIEW 

10 

iteratively adjusts the semantic distances between samples to place them in appropriate positions. The performance of contrast learning largely depends on the number and quality of negative examples, and therefore, negative sampling is another critical aspect of contrastive learning. 

Wei et al. [48] propose a quintuplet loss to optimize the text embedding space. Specifically, they use a sub-network to synthesize state and object texts into compositions. After that, the label of an image is used as a positive example and supplemented with three negative examples for contrastive learning. The negative examples are text compositions with the same state but different objects, the same object but different states, and different objects and states with the target image. SCEN [119] performs contrastive learning in the visual semantic space. It defines two databases to sample the negative examples, one with the same state as the target image but with different objects, and the other with the same object but with different states. After that, contrastive learning is implemented in the decoupled state/object embedding space. Yang et al. [120] adopt a similar approach to explore the relations among states or objects. Meanwhile, they introduce instance-level contrast learning to optimize the compositional embedding space. 

### **4.5 Other Categories** 

In addition to the above mainstream techniques, many other studies provide unique perspectives to address the problem of compositional recognition. For example, TMN [26] presents a gated network that recognizes different compositions by injecting state and object information into the network to determine the switching of pathways. Similarly, TAFE-Net [121] proposes a task-aware learning paradigm that guides the studying process by using task information as cues. Some methods are devoted to analyzing the imbalance issue. MUST [122] argues that the difficulty of recognizing elements varies, e.g., _mashed banana_ is hard to be identified as _banana_ while relatively easy to be identified as _mashed_ . For this reason, it introduces a weighted loss to balance the effects of different elements. ProLT [123], on the other hand, points out that the data imbalance problem caused by different sample sizes of elements affects the recognition accuracy. To this end, it similarly proposes a novel weighted loss to solve this problem. CDS-CZSL [124] argues that for an object, the importance of different states is different. For example, _sliced_ is more important than _red_ for _strawberry_ , cause _red_ is a more general state that can be reflected in a wide range of categories. In this regard, it first highlights those important states by clustering and contrasting, and then a specificity-refined primitive loss is implemented. Moreover, several studies develop new tasks to address larger challenges [125], [126]. 

## **5 FOUNDATION MODEL-BASED OPEN-WORLD RECOGNITION** 

### **5.1 Problem Description** 

Large Vision-Language Models (VLMs) are advanced deep learning models that seamlessly integrate visual and language processing capabilities [127]. By analyzing extensive datasets of image-text pairs, these models learn the intricate 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0010-09.png)


<!-- Start of picture text -->
minimize entropy<br>dog<br>pig<br>···<br>learnable prompt cat<br>Text/Visual Encoder Locked Parameters<br><!-- End of picture text -->

Fig. 6. A schematic diagram of test-time prompt learning [133]. Adjust the prompt by minimizing the entropy of the output. 

relationships between vision and language, allowing them to understand and generate detailed language descriptions of image content [28]. VLMs are renowned for their robust cross-modal understanding and nuanced element perception, which make them particularly effective for zero-shot adaptation tasks. It is only necessary to associate the text description with the class name of the downstream recognition task, e.g., _a photo of a [class]_ , to achieve the purpose of classification and yield excellent results. However, recent studies suggest the capabilities of VLMs have not been fully exploited. Thus the foundation model-based open-world recognition receives more attention. 

To provide a deep understanding of this topic, we first compare several prominent VLM-related research tasks. First, _Better VLMs_ explores to improve the pre-training process of VLMs. The motivation for most studies stems from two aspects, _i.e._ , data efficiency and learning efficiency. Data-efficient pre-training aims to reduce the data required while preserving strong representations [29], [128], since large datasets, like CLIP’s 400 million image-text pairs, are resource-heavy. Learning-efficient pre-training is to explore better alternative training methods like reconstruction [129], generation [130]. Next, _Few-Shot Adaptation and OOD Detection_ , in which the former involves fine-tuning pre-trained VLMs with limited labeled data to create specialized models for specific tasks [30], [31], which the latter aims to identify samples not belonging to the target categories [131], [132]. Note that the OOD does not need to recognize the specific category of the foreign samples. Notably, both fewshot adaptation and OOD detection require labeled data to support fine-tuning VLMs. In contrast, _Zero-Shot Adaptation_ releases this limitation. It consists of three basic tasks that apply VLMs to open environment recognition tasks under different constraints, including _i) Zero-shot Prediction_ : with only the category names of the task known and without any image data applying VLMs to the downstream task; _ii) Test-time Adaptation_ : know the category names of the task and allow adjustments at the online testing phase; and _iii) Unsupervised Adaptation_ : Know the category names of the task and have part or entire of the unlabeled test data in advance. In this survey, we refer to the three tasks of zero-shot adaptation, i.e., _i)_ , _ii)_ and _iii)_ , as the category of foundation model-based open recognition. 

UNDER REVIEW 

11 

### **5.2 Zero-Shot Prediction** 

VLMs have powerful zero-shot prediction capabilities. For a specific task, simply editing the category names into the prompt, e.g., _a photo of [class]_ , enables direct classification without fine-tuning. However, there is a performance gap between such a deployment and a model that is fully supervised and trained on the downstream task. To address this issue, zero-shot prediction presents promising solutions. A prevalent solution is to design better prompts. The commonly used _a photo of [class]_ , while intuitive, is missing a lot of detailed information. For this reason, Menon et al. [32] propose to use a large language model such as GPT-3 [134] to generate multiple word descriptions for classes. In the testing time, the similarity between the image sample and each word description is calculated, and the mean value is taken as the discriminative basis. CuPL [135] has a similar idea, which uses this description directly as the prompt for testing. CHiLS [136] also adopts a large language model, which generates multiple subclasses for each category and uses their combined similarity as the discriminative basis. APPLe [137] uses the GPT-3 descriptions to initialize prompt prototypes as the category classifiers. Unlike the design of prompt, SuS-X [138] uses Diffusion [139] to pre-generate multiple pseudo-visual samples for each class, which serves as a support set to assist the judgment at the testing time. CALIP [33] takes the perspective of embedding space, and it introduces the attention mechanism to capture the correlation between text embeddings and visual embeddings, which effectively improves the zero-shot generalization capability. 

### **5.3 Test-Time Adaptation** 

The purpose of Test-Time Adaptation (TTA) is to dynamically adjust the model to progressively adapt to the downstream task during the testing process. The mainstream schemes are categorized into prompt adaptation and cache bank. Prompt adaptation is a technique that combines prompt learning and TTA. During testing, the prompt is set as learnable parameters and the parameters of the model are fixed. The model continuously optimizes the prompt representation and thus adapts to the target task. TPT [133] first presents this concept by augmenting the test image into multiple views and then filtering out those with low confidence. The confidence outputs of the remaining augmented samples are averaged as the final prediction, and at the same time, the information entropy is minimized to train the prompt (Fig. 6). This paradigm provides a basic template for subsequent research on prompt adaptation. DiffTPT [140] argues that the augmentation approach of TPT lacks diversity and, therefore, introduces the diffusion model to generate richer samples for the test image. PromptAlign [141] argues that adjusting the prompt should be done while aligning the distribution of the target and pre-training data. Therefore it introduces additional loss to align the statistics of target and pre-training data, _i.e._ , mean and variance. SwapPrompt [142] and DART [143] use the exponential moving average algorithm to update the prompt. 

The goal of the Cache bank is to store the tested samples to improve the performance of subsequent tests. An 

intuitive approach is to cache the previous high-confidence samples as the support set to be queried by subsequent samples. DMN-ZS [144] introduces an attention mechanism to compute the similarity between the new test samples and the support set to obtain the weighted features. TDA [145] sets up two cache banks to store the one-hot labels and the negative soft labels of the reliable samples, respectively. The new test samples interact with them to generate predictions. Zhang et al. [146] employ a cache bank to save highconfidence samples from learning high-quality prompts. In addition, MTA [147] proposes a new loss function to optimize visual features in the semantic space. 

### **5.4 Unsupervised Adaptation** 

Unsupervised adaptation is suitable for offline testing environments where some or all test data is available. Although there are no labels available, image samples can provide a priori information to help better prediction. Existing research combines different algorithms to address this problem. UPL [148] fuses prompt learning and self-supervised learning to learn prompt representations through a small number of high-quality pseudo-labels. MUST [149] incorporates image reconstruction techniques to facilitate the model’s understanding of visual information. InMaP [150] introduces prototype learning, which mines a set of visual prototypes from the visual space to replace the text embeddings for prediction. LaFTer [151] trains a text classifier and then uses it to classify images and trains the image encoder with pseudo-labels. ZLaP [152] presents a label propagation algorithm to assign labels to images. In addition, CLIPPR [153] introduces a label distribution prior to predicting the data of the target domain. 

## **6 TECHNICAL DETAILS** 

### **6.1 Standardized Datasets** 

In Table 1, we list the commonly used standardized datasets for three tasks ZSOR, ZSCR, and FBOR, respectively. Specifically, there are 8 commonly used datasets used for ZSOR, including fine-grained datasets such as CUB [7], which is a bird dataset; SUN [8], which is a scene dataset, and coarsegrained datasets such as AWA [156], which is a dataset of various types of animals. Most of the datasets contain detailed attribute annotations. Note that Flowers102 [154] and NABirds [155] do not have attribute annotations. Flowers102 contains textual descriptions, _i.e._ , each image is described by several sentences. NABirds has region annotations, which mark the parts of the bird and are typically used in visual component analysis methods. For ZSCR, there are 6 commonly used datasets. Different from ZSOR, the column _[Class/Attr.]_ indicates the number of objects and the number of states they contain. It can be seen that their compositional sizes cover different orders of magnitude, ranging from 3 _/_ 8 (AO-CLEVr [41]), which means up to 24 compositions, to 674 _/_ 413 (C-GQA [115]), which means 278,362 compositions. Last, we show 15 commonly used datasets for FBOR that cover different categories and different data sizes. ImageNet [1] includes data with up to 1000 categories, while EuroSAT [169] and CIFAR-10 [170] have only 10 categories. The data types are also diverse, including 

UNDER REVIEW 

12 

TABLE 1 

A list of commonly used benchmark datasets for zero-shot image recognition. 

|**Dataset**|**Year**|**Images**|**Class/Attr.**|**Download**|
|---|---|---|---|---|
||Zero-Sho|t Object Rec|ognition||
|CUB [7]|2011|11,788|200/312|[Link]|
|Flowers102 [154]|2008|8,189|102/-|[Link]|
|SUN [8]|2012|14,340|717/102|[Link]|
|NABirds [155]|2015|48,562|1011/-|[Link]|
|DeepFashion [40]|2016|289,222|46/1000|[Link]|
|<br>AWA [156]|2013|30,475|50/85|[Link]|
|<br>AWA2 [22]|2018|37,322|50/85|[Link]|
|<br>APY [157]|2009|15,339|32/64|[Link]|
|<br>Zer|o-Shot Co|mpositional|Recognition||
|UT-Zappos [158]|2014|50,025|12/16|[Link]|
|<br>MIT-States [159]|2015|53,753|245/115|[Link]|
|C-GQA [115]|2021|39,298|674/413|[Link]|
|AO-CLEVr [41]|2020|180,000|3/8|[Link]|
|<br>VAW-CZSL [160]|2022|92,583|541/440|[Link]|
|Clothing16K|2020|16170|8/9|[Link]|
|Foundatio|n model-|,<br>Based Open|-world Recogni|tion|
|ImageNet [1]|2009|1,431,167|1000|[Link]|
|<br>Caltech101 [161]|2004|9,145|101|[Link]|
|<br>Caltech256 [162]|2007|20,607|256|[Link]|
|<br>SUN397 [163]|2010|108,753|397|[Link]|
|<br>Food101 [164]|2014|101,000|101|[Link]|
|<br>Flowers102 [154]|2008|8,189|102|[Link]|
|<br>StanfordCars [165]|2013|16,185|197|[Link]|
|FGVCAircraft [166]|2013|10,000|100|[Link]|
|<br>OxfordPets [167]|2012|7,349|37|[Link]|
|DTD [168]|2014|5,640|47|[Link]|
|<br>EuroSAT [169]|2019|27,000|10|[Link]|
|<br>Country211 [28]|2021|64,300|211|[Link]|
|<br>CIFAR-10 [170]|2009|60,000|10|[Link]|
|<br>CIFAR-100 [170]|2009|60,000|100|[Link]|
|<br>Bid[171]|2014|49829|500|[Lik]|
|rsnap||,||n|
|<br>_[Class/Attr.] means th_<br>|_e number_<br>|_of classes and_<br>|_attributes for ZS_<br>|_OR, objects and_<br>|
|_states for ZSCR, class_<br>_in the corresponding r_|_es for FBO_<br>_epository._|_R. Click the _|_[link] to check m_|_ore information_|



food [164], flowers [154], pets [167], transportation [165], [166], etc. They are also fine-grained datasets. In addition, DTD [168] is a texture dataset, and EuroSAT [169] is a remote sensing dataset. 

### **6.2 Implementation** 

To facilitate the deep understanding and fast reusing of ZSIR approaches, this survey further provides the implementation details of most representative methods in Tables 2, 3, and 4. Specifically, Table 2 and 3 show the implementation details of the related studies of ZSOR and ZSCR, including the backbone, auxiliary, dataset, and code addresses. It can be seen that commonly used backbones include ResNet [176], VGG [177], GoogleNet [178], AlexNet [179], ViT [69], and CLIP [28]. _[Auxiliary]_ refers to additional information such as region-level annotations. We provide the dataset and code address to facilitate access to the performance of the method as well as its implementation. Finally, we label the study with up to two keywords based on the specific technique used. 

In Table 4, we show more details of the related work in foundation model-based open-world recognition. We list their visual and text encoders, as well as auxiliary information. GPT-3 [134] and Diffusion [139] are the exotic models. _[Statistic]_ denotes the mean and variance of the pre-training data. _[Distribution]_ denotes the prior distribution of labels. We also provide their code repositories for quick reference. 

### **6.3 Shared Technologies** 

It can be seen from Tables 2, 3, and 4 that some techniques are common across the three tasks. We further discuss these shared techniques to reveal more commonalities between these tasks. In particular, attention is the most commonly used technique, distributed across almost every sub-direction in the three tasks. This suggests that attention techniques are extremely generalizable and can be applied to different task goals and with different research motivations. In ZSOR, attention is used to localize key visual regions [35], [36], model visual-text correlations [38], [39], [81], and localize key attributes [92]. In ZSCR, attention is used to model object and state correlations [101], [104], [107], and enhance representations [113], [114]. In FBOR, attention is used to capture correlations between images and text [33]. Prototype learning is another more generalized technique. In ZSOR, prototypes are used to represent attributes [85], [87]. In ZSCR, prototypes are used to represent objects and states [97], [105]. In FBOR, prototypes are used to replace the embedding of prompts in deep space [150]. Graph and contrast learning are the more commonly used techniques in ZSOR and ZSCR. The graph is used to model the topological relationships between visual regions in ZSOR [37], [72], while in ZSCR, it is used to capture the logical relationships between individual objects and states [115], [116]. Contrast learning is used in ZSOR to optimize attribute embeddings [79], while in ZSCR, it is used to untangle and model semantic relations [48], [119]. In FBOR, thanks to the robust zero-shot performance of VLMs, fine-tuning prompts become a popular approach [133], [142]. Similarly, in ZSCR, some methods with CLIP as the backbone introduce prompt learning [105], [117], which effectively improves the performance of the model. 

## **7 APPLICATION** 

In recent years, besides image recognition, element-wise zero-shot techniques have been applied in a wide range of areas and developed synergistically. We ketch out some following related applications. 

### **7.1 Language and Text** 

Language, as one of the main media used by humans, has always received attention from researchers. Due to label pressures, zero-shot generalization is also a long-standing direction in language studies [180]. In recent years, large language models have been developed rapidly [181], and they can respond to human conversations fluently, showing their powerful zero-shot reasoning ability. Meanwhile, some studies [182] proposed fine-tuning schemes for language models to improve the zero-shot performance. In some specific tasks, zero-shot techniques have been widely applied to solve the problem of insufficient data samples, such as machine translation [183], question answering [184], etc. In addition, zero-shot techniques also play an important role in text analysis, such as sentiment classification [185], topic classification [186], etc., which is extremely helpful for research in sociology, psychology, and other disciplines. Meanwhile, the collection and labeling of text samples is a huge obstacle, and zero-shot generalization offers a promising solution [187]. Moreover, recent studies, such as named 

UNDER REVIEW 

13 

TABLE 2 

More details on selected advances for zero-shot object recognition. 

|**Topic**|**Tax.**|**Name**|**Venue**|**Year**|**Backbone**|**Aux.**|**KeyWords**|**Dataset**|**Code**|
|---|---|---|---|---|---|---|---|---|---|
||isual|LH2B [62]<br>S2GA [61]<br>AGAA [63]<br>LDF [64]<br>AREN [35]<br>SGMA [34]<br>CANZSL [53]<br>RGEN [36]<br>SDGZSL [56]|CVPR<br>NeurIPS<br>CVPR<br>CVPR<br>CVPR<br>NeurIPS<br>WACV<br>ECCV<br>ICCV|2017<br>2018<br>2018<br>2018<br>2019<br>2019<br>2020<br>2020<br>2021|VGG16<br>VGG16<br>VGG16<br>GNet, VGG19<br>ResNet101<br>VGG19<br>VGG16<br>ResNet101<br>ResNet101|Region<br>Region<br>Region<br>-<br>-<br>-<br>Region<br>-<br>-|Detection<br>Detection<br>Detection<br>Crop<br>Attention<br>Crop<br>Consistency<br>Attention, Graph<br>Disentangling|CUB, NAB<br>CUB, NAB<br>CUB, NAB<br>CUB, AWA<br>CUB, SUN,AWA2, APY<br>CUB, FLO, AWA<br>CUB, NAB<br>CUB, SUN, AwA2, APY<br>CUB, AWA2, APY, FLO|[Link]<br>[Link]<br>[Link]<br>[Link]<br>[Link]<br>[Link]<br>[Link]<br>-<br>[Link]|
||V|RSAN [60]|CIKM|2021|ResNet101|-|Attention|CUB, SUN, AWA2|-|
|||SR2E [65]<br>|AAAI<br>|2021<br>|ResNet101<br>|-|Crop<br>|CUB, SUN, AWA2, APY<br>|-<br>|
|||VGSE-SMO [70]|CVPR|2022|ResNet50|-|Crop, Clustering|CUB, SUN, AWA2|[Link]|
|on||GSMFlow [57]|TMM|2022|ResNet101|-|Generation Shifts|CUB, AWA2, APY, FLO|[Link]|
|iti||ERPCNet [66]|TCSVT|2022|ResNet101|-|Crop|CUB, SUN, AWA2, APY|-|
|gn||GKU [37]|AAAI|2023|ResNet34|Region|Graph|CUB, NAB|-|
|co||EOPA [172]<br>|TPAMI<br>|2023<br>|ANet, ResNet50<br>|-|Graph<br>|CUB, SUN, FLO, AWA2<br>|-<br>|
|Re||POPRNet [67]|TIP|2024|ResNet101|-|Crop|CUB, SUN, AWA2|[Link]|
|ct||ZSLViT [68]|CVPR|2024|ViT-B|-|Attention|CUB, SUN, AWA2|-|
|bje||DAZLE [38]|CVPR|2020|ResNet101|-|Attention|CUB, SUN, AWA2, DEP|[Link]|
|O||Composer [76]<br>|NeurIPS<br>|2020|ResNet101|-|Attention, Generation|CUB, SUN, AWA2, DEP<br>|[Link]<br>|
|ot||APN [85]|NeurIPS|2020|ResNet101|-|Prototype|CUB, SUN, AWA2|[Link]|
|Sh||GEM [75]|CVPR|2021|ResNet101|Region|Attention|CUB, SUN, AWA2|[Link]|
|o-||DPPN [87]|NeurIPS|2021|ResNet101|-|Prototype|CUB, SUN, AWA2, APY|[Link]|
|er|te|LAPE [173]|TCSVT|2022|ResNet101|-|Attention|CUB, SUN, AWA2, APY|-|
|Z|bu|RIAE [72]|IS|2022|ResNet101|-|Attention, Graph|CUB, SUN, AWA2|-|
||tri|DPDN [47]|MM|2022|ResNet101|-|Attention, Prototype|CUB, SUN, AWA2|-|
||At|GNDAN [73]|TNNLS|2022|ResNet101|-|Attention, Graph|CUB, SUN, AWA2|[Link]|
||l-|AREES [77]|TNNLS|2022|ResNet101|-|Attention, Generation|CUB, SUN, AWA, AWA2, APY|-|
||sua|MSDN [81]<br>|CVPR<br>|2022<br>|ResNet101<br>|-|Attention<br>|CUB, SUN, AWA2<br>|[Link]<br>|
||Vi|TransZero [39]<br>|AAAI<br>|2022|ResNet101|-|Attention|CUB, SUN, AWA2<br>|[Link]<br>|
|||I2DFormer [78]|NeurIPS|2022|ViT-B|-|Attention|CUB, FLO, AWA2|[Link]|
|||DUET [79]|AAAI|2023|ViT-B|-|Attention, Contrast|CUB, SUN, AWA2|[Link]|
|||PSVMA [80]|CVPR|2023|ViT-B|-|Attention|CUB, SUN, AWA2|[Link]|
|||HRT [174]|PR|2023|ResNet101|-|Attention|CUB, SUN, AWA2|-|
|||CC-ZSL [89]|TCSVT|2023|ResNet101|-|Prototype, Contrast|CUB, SUN, AWA2|[Link]|
|||CoAR-ZSL [90]|TNNLS|2023|R101, ViT-L|-|Attention, Prototype|CUB, SUN, AWA2|[Link]|
|||GIRL [88]|IS|2023|ResNet101|-|Prototype|CUB, SUN, AWA2, APY|[Link]|
||te|MCZSL [94]<br>|CVPR<br>|2016<br>|VGG16<br>|Region|Crop<br>|CUB<br>|-<br>|
||bu|LFGAA [92]<br>|ICCV<br>|2019<br>|GNet, R101, V19<br>|-|Attention<br>|CUB, SUN, AWA2<br>|[Link]|
||tri|APNet [93]|AAAI|2020|ResNet101|-|Graph|CUB, SUN, AWA, AWA2, APY|-|
||At|DEDN [95]|IJCAI|2024|ResNet101|-|Attention, Distillation|CUB, SUN, AWA2|[Link]|
|_[Tax.] m_|_eans ta_|_xonomy. [Aux.] mean_|_s auxiliary. [_|_GNet] me_|_ans GoogleNet, [ANe_|_t] means A_|_lexNet, [R101] means ResN_|_et101, [V19] means VGG19._||



_[Region] means region-level annotations. [FLO] means Flowers102, [NAB] means NABirds, [DEP] means DeepFashion. Click the [link] to check more information in the corresponding repository._ 

TABLE 3 

More details on selected advances for zero-shot compositional recognition. 

|**Topic**|**Tax.**|**Name**|**Venue**|**Year**|**Backbone**|**KeyWords**|**Dataset**|**Code**|
|---|---|---|---|---|---|---|---|---|
|n|Decoupling|Nan et al. [96]<br>CAUSAL [41]<br>ProtoProp [97]<br>OADis [101]<br>Zhang et al. [104]<br>DECA [100]<br>DRANet [175]<br>ADE [102]<br>DFSP [105]<br>|AAAI<br>NeurIPS<br>NeurIPS<br>CVPR<br>ECCV<br>TMM<br>ICCV<br>CVPR<br>CVPR<br>|2019<br>2020<br>2021<br>2022<br>2022<br>2022<br>2023<br>2023<br>2023<br>|ResNet18<br>ResNet18<br>ResNet18<br>ResNet18<br>ResNet18<br>ResNet18<br>ResNet18<br>ViT-B<br>CLIP<br>|Contrast<br>Mapping Function<br>Prototype, Graph<br>Attention<br>Attention<br>Mapping<br>Attention<br>Attention<br>Attention, Prototype<br>|UTZ, MIT<br>UTZ, AOC<br>UTZ, AOC, CGQ<br>UTZ, MIT, VAW<br>UTZ, AOC, CLO<br>UTZ, MIT<br>UTZ, MIT, CGQ<br>UTZ, CGQ, CLO<br>UTZ, MIT, CGQ<br>|-<br>[Link]<br>[Link]<br>[Link]<br>[Link]<br>[Link]<br>-<br>[Link]<br>[Link]<br>|
|o||Hu et al. [98]|AAAI|2023|ResNet18|Contrast|UTZ, CGQ|[Link]|
|gniti||CAILA [99]<br>Jing et al. [103]<br>|WACV<br>AAAI<br>|2024<br>2024<br>|CLIP<br>CLIP<br>|Mapping<br>Attention<br>|UTZ, MIT, CGQ, VAW<br>UTZ, MIT, CGQ<br>|[Link]<br>-<br>|
|eco||Troika [106]|CVPR|2024|CLIP|Attention|UTZ, MIT, CGQ|[Link]|
|nal R|ncy|Nagarajan et al. [6]<br>SymNet [109]|ECCV<br>CVPR|2018<br>2020|ResNet18<br>ResNet18|Contrast<br>Mapping Function|UTZ, MIT<br>UTZ, MIT|[Link]<br>[Link]|
|sitio|ende|SAD-SP [111]<br>CoT [107]|TPAMI<br>ICCV|2023<br>2023|ResNet18<br>ResNet18, ViT-B|Mapping Function<br>Attention|UTZ, MIT, CGQ<br>MIT, CGQ, VAW|-<br>[Link]|
|mpo|Dep|CANet [110]<br>Panda et al. [108]|CVPR<br>PR|2023<br>2024|ResNet18<br>ResNet18|Mapping Function<br>Graph|UTZ, MIT, CGQ<br>UTZ, MIT, CGQ|[Link]<br>-|
|Co||ProCC [112]|AAAI|2024|ResNet18|Mapping Function|UTZ, MIT, CGQ|[Link]|
|ot||Wei et al. [48]|ICCV|2019|ResNet18|Contrast|UTZ, MIT|-|
|Sh|ip|BMPNet [113]|TMM|2021|ResNet18|Attention|UTZ, MIT|[Link]|
|ro-|sh|CGE [115]<br>|CVPR<br>|2021<br>|ResNet18<br>|Graph<br>|UTZ, MIT, CGQ<br>|[Link]<br>|
|Ze|on|SCEN [119]|CVPR|2022|ResNet18|Contrast|UTZ, MIT, CGQ|[Link]|
||ati|CVGAE [116]<br>|MM<br>|2022<br>|ResNet18<br>|Graph<br>|UTZ, MIT, CGQ<br>|[Link]|
||el|CAPE [114]|WACV|2023|ResNet18|Attention|UTZ, MIT, CGQ|-|
||R|Yang et al. [120]<br>|TMM|2023|ResNet18|contrast<br>|UTZ, MIT||
|||GIPCOL [117]|WACV|2024|CLIP|Graph|UTZ, MIT, CGQ|[Link]|
||rs|TMN [26]<br>|ICCV<br>|2019<br>|ResNet18<br>|Gated Network<br>|UTZ, MIT<br>|[Link]<br>|
||e|MUST [122]|PR|2024|ResNet18|Weighted Loss|UTZ, MIT, CGQ|[Link]|
||th|ProLT [123]|AAAI|2024|ResNet18, CLIP|Weighted Loss|UTZ, MIT, CGQ|-|
||O|CDS-CZSL [124]|CVPR|2024|CLIP|Weighted Loss|UTZ, MIT, CGQ|-|
|_[UTZ] _<br>_Clothin_|_means _<br>_g16K. C_|_UT-Zsppos, [MIT] means _<br>_lick the [link] to check mo_|_MIT-States, _<br>_re informatio_|_[CGQ] _<br>_n in the _|_means C-GQA, [AO_<br> _corresponding reposit_|_C] means AO-CLEVr, [VA_<br>_ory._|_W] means VAW-CZSL, [CL_|_O] means_|



TABLE 4 

#### More details on selected advances for fundation model-based open-world recognition. 

|**Topic**|**Name**|**Venue**|**Year**|**VEncoder**|**TEncoder**|**Auxiliary**|**Contribution**|**Code**|
|---|---|---|---|---|---|---|---|---|
|ZSP|Menon et al. [32]<br>APPLe [137]<br>CuPL [135]<br>SuS-X [138]<br>CHiLS [136]<br>CALIP [33]|arXiv<br>arXiv<br>ICCV<br>ICCV<br>ICML<br>AAAI|2022<br>2023<br>2023<br>2023<br>2023<br>2023|ViT-B<sup>_†_</sup>, ViT-L<sup>_†_</sup><br>ViT-L/14<br>ViT-L/14<br>ResNet50<br>ViTL/14@336px<br>ResNet50|Transformer<br>Transformer<br>Transformer<br>Transformer<br>Transformer<br>Transformer|GPT-3<br>GPT-3<br>GPT-3<br>Diffusion<br>GPT-3<br>-|Generate description words according to category names.<br>Propose prompt prototype learning by initializing from description sentences.<br>Generate description sentences according to category names.<br>Generate visual support set with Diffusion.<br>Generate sub-class names according to category names.<br>Propose attention interaction of image and text embeddings.|-<br>-<br>[Link]<br>[Link]<br>[Link]<br>[Link]|
|TTA|TPT [133]<br>DiffTPT [140]<br>PromptAlign [141]<br>SwapPrompt [142]<br>Zhang et al. [146]<br>DART [143]<br>TDA [145]<br>MTA [147]<br>DMN-ZS [144]|NeurIPS<br>ICCV<br>NeurIPS<br>NeurIPS<br>AAAI<br>AAAI<br>CVPR<br>CVPR<br>CVPR|2022<br>2023<br>2023<br>2023<br>2024<br>2024<br>2024<br>2024<br>2024|ResNet50, ViT-B/16<br>ResNet50, ViT-B/16<br>ViT-B/16, ViT-B/32<br>ResNet50<br>ViT-B/16<br>ViT-B/16<br>ResNet50, ViT-B/16<br>ViT-B/16<br>ResNet50, ViT-B/16|Transformer<br>Transformer<br>Transformer<br>Transformer<br>Transformer<br>Transformer<br>Transformer<br>Transformer<br>Transformer|-<br>Diffusion<br>Statistic<br>-<br>-<br>-<br>-<br>-<br>-|Propose test-time prompt adaptation.<br>Propose to augment image with Diffusion.<br>Align the distributions of test and pre-training set.<br>Update the prompt using exponential moving average.<br>Introduce multiple manual prompts.<br>Learn a separate prompt for each class.<br>Two cache banks are set up to store hard and soft labels.<br>Improve visual representation in the embedding space.<br>Cache high-confidence samples for subsequentpredictions.|[Link]<br>[Link]<br>[Link]<br>-<br>-<br>-<br>[Link]<br>[Link]<br>[Link]|
|UA|CLIPPR [153]<br>UPL [148]<br>MUST [149]<br>InMaP [150]<br>LaFTer [151]<br>ZLaP [152]|arXiv<br>arXiv<br>ICLR<br>NeurIPS<br>NeurIPS<br>CVPR|2022<br>2022<br>2023<br>2023<br>2023<br>2024|ViT-B/32<br>ResNet50<br>ViT-B/16, ViT-L/14<br>ResNet50, ViT-B/16<br>ViT-B/32<br>ResNet50, ViT-B/16|Transformer<br>Transformer<br>Transformer<br>Transformer<br>Transformer<br>Transformer|Distribution<br>-<br>-<br>-<br>GPT-3<br>-|Predicted label aligns a priori label distribution.<br>Select high-confidence samples for fine-tuning.<br>Introduce visual reconstruction and teacher-student model.<br>Learn visual prototypes in the embedding space.<br>Train a text classifier to categorize images.<br>Introduce a labelpropagation algorithm.|[Link]<br>[Link]<br>[Link]<br>-<br>-<br>[Link]|
|_[ZSP] _<br>_ViT-B/_|_means zero-shot predicti_<br>_16. [ViT-L_<sup>_†_</sup>_]: ViT-L/14, V_|_on. [TTA] m_<br>_iT-L/14@33_|_eans test-_<br>_6px. [Stat_|_time adaptation. [UA] m_<br>_istic] means the mean an_|_eans unsupervis_<br>_d variance of pret_|_ed adaptation. [_<br>_rained dataset. [_|_VEncoder] means visual encoder. [TEncoder] means text encoder. [ViT-B_<sup>_†_</sup>_]: ViT-B/32,_<br>_Distribution] means the label distribution. Click the [link] to check more information in_||



_[ZSP] means zero-shot prediction. [TTA] means test-time adaptation. [UA] means unsupervised adaptation. ViT-B/16. [ViT-L_<sup>_†_</sup> _]: ViT-L/14, ViT-L/14@336px. [Statistic] means the mean and variance of pretrained dataset. [Distribution] means the label distribution. Click the the corresponding repository._ 

UNDER REVIEW 

14 

entity recognition [187] and information retrieval [188], also extensively rely on zero-shot ability. 

### **7.2 Scene Understanding** 

Scene understanding is a topic based on image recognition but is more challenging. Instead of assigning a label to an entire image, it usually identifies and localizes multiple elements in an image. For example, multi-label recognition task [189] requires simultaneous recognition of multiple objects in an image. In contrast, object detection [190], [191] and semantic segmentation [192], [193] are two more complex and practical tasks. Object detection requires identifying and localizing multiple objects in an image, while semantic segmentation is a pixel-level classification task that requires assigning labels to each pixel according to semantic information. Scene understanding is an important research topic, which is not only the basis for AI to understand the world but also a key part of deployment to industrial scenarios. Related technologies are needed in a variety of scenarios, such as autonomous driving, medical diagnostic assistance, security monitoring, retail, and so on. However, they also require more detailed annotation and larger data for training than image recognition. Therefore, incorporating zero-shot learning into scene understanding has become an attractive direction in recent years. For example, zeroshot object detection [194]–[196] and zero-shot semantic segmentation [197]–[199] are dedicated to the deployment of models in the open world. 

### **7.3 3D Vision** 

With the increasing maturity of 3D sensors, the cost of acquiring 3D vision data has dropped significantly [200]. Compared with traditional 2D images, 3D visual data contains important depth information and, therefore, can provide richer semantic information. 3D vision data has a wide range of applications, covering automatic driving, medical diagnosis, remote sensing, etc. Correspondingly, research on 3D vision data has also received more and more attention. However, compared with 2D data, the acquisition and labeling cost of 3D data is more expensive. Therefore, many researches integrate the concept of zero-shot into 3D tasks, such as point cloud classification [201], [202], object detection [203], and semantic segmentation [204]. In addition to semantic recognition tasks, some studies are also exploring the application of zero-shot learning to tasks such as generation [205], style transfer [206], and synthesis [207], [208]. There are also some studies that have explored indepth on special tasks, such as human pose estimation [209], shape correspondence [210], and so on. 

However, the number and type of anomaly samples are often insufficient. Some studies resort to zero-shot learning to solve this problem. In addition, zero-shot techniques have been applied in many special tasks to alleviate the low-data problem as well as to enhance the generalization ability of the model, such as action recognition [214], image retrieval [215], and video classification [216]. 

## **8 FUTURE DIRECTIONS** 

Zero-shot learning contributes powerful technical solutions for automated recognition in the open environment. Meanwhile, research based on element-wise representation and reasoning has driven the rapid development and wide application of zero-shot technology. Despite the remarkable achievements, there are still some potential limitations that have not been deeply explored. In this section, we share our perspectives on future research directions. 

### **8.1 Continual Zero-Shot Learning** 

Existing studies are based on closed systems to design solutions. However, in reality, there are a large number of growing systems with dynamically changing environments and goals. For example, for zero-shot object recognition, attributes and categories may be progressively inflated. Early in the observation phase, fewer attributes are accessible, followed by a steady stream of new attribute annotations added. Similarly, the detected categories may increase over time forward. It is difficult for existing schemes to handle such dynamic recognition tasks, and continual learning has come a long way in this regard [217]. However, simply transplanting techniques from continual learning to zeroshot recognition tasks suffers from deviation. Therefore, fusing continual learning and zero-shot learning will further increase the value of applications to real-world scenarios. 

### **8.2 Multi-label Compositional Recognition** 

Zero-shot compositional recognition allows the model to not only learn to recognize objects but also to describe their state. However, current research is limited to a single object and single state. A robust compositional recognition system should have the ability to recognize multiple objects as well as multiple states. For a single object, the recognition system should describe its state from multiple perspectives to provide more detailed information [3]. For multiple objects, their individual states, as well as their interactions, relationships, etc., should be described [218]. Expanding from single labels to multiple labels is a tough choice, but it is an inescapable step toward building a smarter recognition system. 

### **7.4 Ohters** 

Zero-shot learning offers promising solutions for many specific application scenarios. For example, medical and remote sensing images are much more difficult to collect than natural images due to sample scarcity and data protection. Therefore, the research on zero-shot medical image [211] recognition and remote sensing image [212] recognition has been developed rapidly in recent years. Anomaly detection [213] plays a key role in securing many industrial fields. 

### **8.3 VLMs with Downstream Fine-Grained Annotations** 

The power of VLMs in the open world has been demonstrated by the fact that it requires only the names of the categories in the downstream task to accomplish zero-shot inference. Meanwhile, fine-grained annotations can improve the zero-shot inference performance of VLMs [32], [135]. What happens if VLMs are combined with downstream exclusive attribute annotations, such as attribute texts or 

UNDER REVIEW 

15 

state descriptions? There are a number of issues that deserve deeper investigation, including domain shift between pretrained text embeddings of VLMs and downstream text, fine-grained visual-text matching, catastrophic forgetting, and so on. 

### **8.4 Annotation Cost and Quality** 

Element-wise schemes in zero-shot object recognition typically require extensive refined attribute annotations, especially for visual-attribute matching schemes. However, the attribute-level annotations are time- and labor-intensive compared to class-level labeling. Worse still, once they settle into concrete real-world scenarios, such as industrial inspection or medical pathology, the expert knowledge can be a bottleneck, which further raises the labor cost. In addition, attribute engineering is a complex crossover field. Even attributes annotated by experienced experts do not guarantee benefits for deep learning, which implies that highquality attribute annotations require professionals with dual knowledge of both specific domains and deep learning. Despite some studies attempting to make breakthroughs in the field of automated annotation [94], it is clear that there is still a long way to go. 

### **8.5 Deployment Cost** 

Compared to class-wise semantic modeling, many elementwise schemes have to process a higher density of information, which introduces a more luxurious deployment cost. Such cost is reflected in bloated network structures and high computational complexity _in the deployment phase_ . As a result, they are unfriendly to edge tasks and mini-endpoints, which have to trade off performance and memory [219]. However, they can be more favorable to a scenario associated with resource-constrained devices due to the low or even zero data requirements. Such a scenario can also well align with ubiquitous devices and data in real-world applications. Therefore, it is promising to investigate ondevice-friendly element-wise algorithms. 

al. [221] introduce adversarial attack technique into zeroshot models. The interplay between model attacks and defenses has been a long-standing topic. Attackers aim to weaken models at minimal cost, while defenders strive to develop more robust representations to resist these perturbations. This dynamic process of learning from each other leads to continuous progress, offering a new perspective on combating domain shift. 

### **8.8 Poor Theoretical Foundation** 

The development of zero-shot learning is established on the beautiful hypothesis that deep neural networks can reason logically like humans [18], [22]. As mentioned, we can learn to identify basic elements and recognize new concepts by combining and reasoning about them. Nevertheless, there are not many solid theories on the compatibility between human reasoning and machine inductive ability, leading to a lack of explainability. Meanwhile, some flaws also challenge the plausibility of the hypothesis, such as the correspondence between abstract attributes and vision. Rigorous theoretical guidance is at the helm of a field moving forward, and it is of great prospective to dive into the mysterious black box in the future. 

## **9 CONCLUSION** 

We provide a comprehensive exposition of three major tasks in the field of zero-shot image recognition that share the notion of element-wise representation and reasoning. Specifically, we show the background, commonalities, and challenges faced by several tasks. Then related recent techniques are meticulously categorized and explained. At the same time, we provide specific technical details, including datasets, training details, code repository addresses, and more. Finally, we show the wide range of applications of element-wise zero-shot learning and look at future directions. 

## **REFERENCES** 

### **8.6 Unified Framework** 

Zero-shot studies share many common techniques, such as attention, graph modeling, and so on. However, barriers between them still exist due to the different goals and contexts of the tasks. A technique and framework that is versatile across all fields is lacking. However, the significance of such a unified framework for both academia and application is immense [220]. The quest for a unified framework means exploring more commonalities across zero-shot tasks and thinking about the operational mechanisms of the entire realm from the ground-up principles. From a realistic point of view, a mature intelligence should be able to handle multiple tasks at the same time. 

### **8.7 Robust Representation Learning** 

Despite some solutions have been proposed [91] to tackle with domain shift, there is a lack of quantitative assessments regarding their resistance to interference. Consequently, the robustness of existing representation methods in realworld environments remains uncertain. Recently, Shafiee et 

- [1] J. Deng, W. Dong, R. Socher, L.-J. Li, K. Li, and L. Fei-Fei, “Imagenet: A large-scale hierarchical image database,” in _CVPR_ . Ieee, 2009, pp. 248–255. 1, 6.1, 1 

- [2] C.-Y. Chen and K. Grauman, “Inferring analogous attributes,” in _CVPR_ , 2014, pp. 200–207. 1, 2.1.2, 4.3.2 

- [3] I. Misra, A. Gupta, and M. Hebert, “From red wine to red tomato: Composition with context,” in _CVPR_ , 2017, pp. 1792–1801. 1, 2.1.2, 8.2 

- [4] Z. Yang, T. Luo, D. Wang, Z. Hu, J. Gao, and L. Wang, “Learning to navigate for fine-grained classification,” in _ECCV_ , 2018, pp. 420–435. 1 

- [5] Z. Akata, S. Reed, D. Walter, H. Lee, and B. Schiele, “Evaluation of output embeddings for fine-grained image classification,” in _CVPR_ , 2015, pp. 2927–2936. 1 

- [6] T. Nagarajan and K. Grauman, “Attributes as operators: factorizing unseen attribute-object compositions,” in _ECCV_ , 2018, pp. 169–185. 1, 4.3.1, 3 

- [7] C. Wah, S. Branson, P. Welinder, P. Perona, and S. Belongie, “The caltech-ucsd birds-200-2011 dataset,” 2011. 1, 2.3.1, 6.1, 1 

- [8] G. Patterson and J. Hays, “Sun attribute database: Discovering, annotating, and recognizing scene attributes,” in _CVPR_ . IEEE, 2012, pp. 2751–2758. 1, 6.1, 1 

- [9] X.-S. Wei, Y.-Z. Song, O. Mac Aodha, J. Wu, Y. Peng, J. Tang, J. Yang, and S. Belongie, “Fine-grained image analysis with deep learning: A survey,” _IEEE TPAMI_ , vol. 44, no. 12, pp. 8927–8948, 2021. 1 

UNDER REVIEW 

16 

- [10] J. Wang, Y. Cheng, and R. S. Feris, “Walk and learn: Facial attribute representation learning from egocentric video and contextual data,” in _CVPR_ , 2016, pp. 2295–2304. 1 

- [11] A. Kovashka, D. Parikh, and K. Grauman, “Whittlesearch: Image search with relative attribute feedback,” in _CVPR_ . IEEE, 2012, pp. 2973–2980. 1 

- [12] Q. Wu, C. Shen, P. Wang, A. Dick, and A. Van Den Hengel, “Image captioning and visual question answering based on attributes and external knowledge,” _IEEE TPAMI_ , vol. 40, no. 6, pp. 1367– 1381, 2017. 1 

- [13] R. Santa Cruz, B. Fernando, A. Cherian, and S. Gould, “Neural algebra of classifiers,” in _WACV_ . IEEE, 2018, pp. 729–737. 1, 4.4.2 

- [14] I. Biederman, “Recognition-by-components: a theory of human image understanding.” _Psychological review_ , vol. 94, no. 2, p. 115, 1987. 1 

- [15] D. D. Hoffman and W. A. Richards, “Parts of recognition,” in _Readings in Computer Vision_ . Elsevier, 1987, pp. 227–242. 1 

- [16] P. Felzenszwalb, D. McAllester, and D. Ramanan, “A discriminatively trained, multiscale, deformable part model,” in _CVPR_ . Ieee, 2008, pp. 1–8. 1 

- [17] P. W. Battaglia, J. B. Hamrick, V. Bapst, A. Sanchez-Gonzalez, V. Zambaldi, M. Malinowski, A. Tacchetti, D. Raposo, A. Santoro, R. Faulkner _et al._ , “Relational inductive biases, deep learning, and graph networks,” _arXiv_ , 2018. 1, 3.2.3 

- [18] C. H. Lampert, H. Nickisch, and S. Harmeling, “Learning to detect unseen object classes by between-class attribute transfer,” in _CVPR_ . IEEE, 2009, pp. 951–958. 1, 2.1.1, 8.8 

- [19] Y. Wang, Q. Yao, J. T. Kwok, and L. M. Ni, “Generalizing from a few examples: A survey on few-shot learning,” _ACM computing surveys (csur)_ , vol. 53, no. 3, pp. 1–34, 2020. 1 

- [20] N. O’Mahony, S. Campbell, A. Carvalho, L. Krpalkova, G. V. Hernandez, S. Harapanahalli, D. Riordan, and J. Walsh, “Oneshot learning for custom identification tasks; a review,” _Procedia Manufacturing_ , vol. 38, pp. 186–193, 2019. 1 

- [21] J. Yang, K. Zhou, Y. Li, and Z. Liu, “Generalized out-ofdistribution detection: A survey,” _IJCV_ , pp. 1–28, 2024. 1 

- [22] Y. Xian, C. H. Lampert, B. Schiele, and Z. Akata, “Zero-shot learning—a comprehensive evaluation of the good, the bad and the ugly,” _IEEE TPAMI_ , vol. 41, no. 9, pp. 2251–2265, 2018. 1, 2.1.1, 1, 8.8 

- [23] W. Wang, V. W. Zheng, H. Yu, and C. Miao, “A survey of zeroshot learning: Settings, methods, and applications,” _ACM TIST_ , vol. 10, no. 2, pp. 1–37, 2019. 1, 3.1 

- [24] F. Pourpanah, M. Abdar, Y. Luo, X. Zhou, R. Wang, C. P. Lim, X.-Z. Wang, and Q. J. Wu, “A review of generalized zero-shot learning methods,” _IEEE TPAMI_ , vol. 45, no. 4, pp. 4051–4070, 2022. 1, 3.1 

- [25] B. M. Lake, T. D. Ullman, J. B. Tenenbaum, and S. J. Gershman, “Building machines that learn and think like people,” _Behavioral and brain sciences_ , vol. 40, p. e253, 2017. 2.1.2 

- [26] S. Purushwalkam, M. Nickel, A. Gupta, and M. Ranzato, “Taskdriven modular networks for zero-shot compositional learning,” in _ICCV_ , 2019, pp. 3593–3602. 2.1.2, 4.5, 3 

- [27] M. Mancini, M. F. Naeem, Y. Xian, and Z. Akata, “Open world compositional zero-shot learning,” in _CVPR_ , 2021, pp. 5222–5230. 2.1.2, 4.1 

- [28] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark _et al._ , “Learning transferable visual models from natural language supervision,” in _ICML_ . PMLR, 2021, pp. 8748–8763. 2.1.3, 5.1, 1, 6.2 

- [29] C. Jia, Y. Yang, Y. Xia, Y.-T. Chen, Z. Parekh, H. Pham, Q. Le, Y.-H. Sung, Z. Li, and T. Duerig, “Scaling up visual and visionlanguage representation learning with noisy text supervision,” in _ICML_ . PMLR, 2021, pp. 4904–4916. 2.1.3, 5.1 

- [30] K. Zhou, J. Yang, C. C. Loy, and Z. Liu, “Learning to prompt for vision-language models,” _IJCV_ , vol. 130, no. 9, pp. 2337–2348, 2022. 2.1.3, 5.1 

- [31] ——, “Conditional prompt learning for vision-language models,” in _CVPR_ , 2022, pp. 16 816–16 825. 2.1.3, 5.1 

- [32] S. Menon and C. Vondrick, “Visual classification via description from large language models,” _arXiv_ , 2022. 2.1.3, 5.2, 4, 8.3 

- [33] Z. Guo, R. Zhang, L. Qiu, X. Ma, X. Miao, X. He, and B. Cui, “Calip: Zero-shot enhancement of clip with parameter-free attention,” in _AAAI_ , vol. 37, no. 1, 2023, pp. 746–754. 2.1.3, 5.2, 6.3, 4 

- [34] Y. Zhu, J. Xie, Z. Tang, X. Peng, and A. Elgammal, “Semanticguided multi-attention localization for zero-shot learning,” _NeurIPS_ , vol. 32, 2019. 2.3.1, 3.2.2, 2 

- [35] G.-S. Xie, L. Liu, X. Jin, F. Zhu, Z. Zhang, J. Qin, Y. Yao, and L. Shao, “Attentive region embedding network for zero-shot learning,” in _CVPR_ , 2019, pp. 9384–9393. 2.3.1, 3.2.1, 6.3, 2 

- [36] G.-S. Xie, L. Liu, F. Zhu, F. Zhao, Z. Zhang, Y. Yao, J. Qin, and L. Shao, “Region graph embedding network for zero-shot learning,” in _ECCV_ . Springer, 2020, pp. 562–580. 2.3.1, 3.2.1, 6.3, 2 

- [37] J. Guo, S. Guo, Q. Zhou, Z. Liu, X. Lu, and F. Huo, “Graph knows unknowns: Reformulate zero-shot learning as sample-level graph recognition,” in _AAAI_ , vol. 37, no. 6, 2023, pp. 7775–7783. 2.3.1, 3.2.3, 6.3, 2 

- [38] D. Huynh and E. Elhamifar, “Fine-grained generalized zero-shot learning via dense attribute-based attention,” in _CVPR_ , 2020, pp. 4483–4493. 2.3.1, 3.3.1, 6.3, 2 

- [39] S. Chen, Z. Hong, Y. Liu, G.-S. Xie, B. Sun, H. Li, Q. Peng, K. Lu, and X. You, “Transzero: Attribute-guided transformer for zeroshot learning,” in _AAAI_ , vol. 36, no. 1, 2022, pp. 330–338. 2.3.1, 6.3, 2 

- [40] Z. Liu, P. Luo, S. Qiu, X. Wang, and X. Tang, “Deepfashion: Powering robust clothes recognition and retrieval with rich annotations,” in _CVPR_ , 2016, pp. 1096–1104. 2.3.1, 1 

- [41] Y. Atzmon, F. Kreuk, U. Shalit, and G. Chechik, “A causal view of compositional zero-shot recognition,” _NeurIPS_ , vol. 33, pp. 1462– 1473, 2020. 2.3.1, 4.2.1, 6.1, 1, 3 

- [42] Y. Fu, T. M. Hospedales, T. Xiang, and S. Gong, “Transductive multi-view zero-shot learning,” _IEEE TPAMI_ , vol. 37, no. 11, pp. 2332–2345, 2015. 2.3.2 

- [43] H. Jiang, R. Wang, S. Shan, and X. Chen, “Transferable contrastive network for generalized zero-shot learning,” in _ICCV_ , 2019, pp. 9765–9774. 2.3.2, 3.1 

- [44] K. Zhou, Z. Liu, Y. Qiao, T. Xiang, and C. C. Loy, “Domain generalization: A survey,” _IEEE TPAMI_ , vol. 45, no. 4, pp. 4396– 4415, 2022. 2.3.2 

- [45] Y. Ganin and V. Lempitsky, “Unsupervised domain adaptation by backpropagation,” in _ICML_ . PMLR, 2015, pp. 1180–1189. 2.3.2 

- [46] Z. Rao, J. Guo, L. Tang, Y. Huang, X. Ding, and S. Guo, “Srcd: Semantic reasoning with compound domains for single-domain generalized object detection,” _arXiv_ , 2023. 2.3.2 

- [47] J. Ge, H. Xie, S. Min, P. Li, and Y. Zhang, “Dual part discovery network for zero-shot learning,” in _ACM MM_ , 2022, pp. 3244– 3252. 2.3.2, 3.3.1, 3.3.2, 2 

- [48] K. Wei, M. Yang, H. Wang, C. Deng, and X. Liu, “Adversarial finegrained composition learning for unseen attribute-object recognition,” in _ICCV_ , 2019, pp. 3741–3749. 2.3.2, 4.4.3, 6.3, 3 

- [49] B. Romera-Paredes and P. Torr, “An embarrassingly simple approach to zero-shot learning,” in _ICML_ . PMLR, 2015, pp. 2152– 2161. 3.1 

- [50] Y. Xian, T. Lorenz, B. Schiele, and Z. Akata, “Feature generating networks for zero-shot learning,” in _CVPR_ , 2018, pp. 5542–5551. 3.1 

- [51] V. K. Verma, G. Arora, A. Mishra, and P. Rai, “Generalized zeroshot learning via synthesized examples,” in _CVPR_ , 2018, pp. 4281–4289. 3.1 

- [52] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. WardeFarley, S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial networks,” _Communications of the ACM_ , vol. 63, no. 11, pp. 139–144, 2020. 3.1 

- [53] Z. Chen, J. Li, Y. Luo, Z. Huang, and Y. Yang, “Canzsl: Cycleconsistent adversarial networks for zero-shot learning from natural language,” in _WCACV_ , 2020, pp. 874–883. 3.1, 2 

- [54] Z. Chen, S. Wang, J. Li, and Z. Huang, “Rethinking generative zero-shot learning: An ensemble learning perspective for recognising visual patches,” in _ACM MM_ , 2020, pp. 3413–3421. 3.1 

- [55] D. P. Kingma and M. Welling, “Auto-encoding variational bayes,” _arXiv_ , 2013. 3.1 

- [56] Z. Chen, Y. Luo, R. Qiu, S. Wang, Z. Huang, J. Li, and Z. Zhang, “Semantics disentangling for generalized zero-shot learning,” in _ICCV_ , 2021, pp. 8712–8720. 3.1, 2 

- [57] Z. Chen, Y. Luo, S. Wang, J. Li, and Z. Huang, “Gsmflow: Generation shifts mitigating flow for generalized zero-shot learning,” _IEEE TMM_ , vol. 25, pp. 5374–5385, 2022. 3.1, 2 

- [58] Z. Chen, Y. Luo, S. Wang, R. Qiu, J. Li, and Z. Huang, “Mitigating generation shifts for generalized zero-shot learning,” in _ACM MM_ , 2021, pp. 844–852. 3.1 

UNDER REVIEW 

17 

- [59] S. Liu, M. Long, J. Wang, and M. I. Jordan, “Generalized zeroshot learning with deep calibration network,” _NeurIPS_ , vol. 31, 2018. 3.1 

- [60] Z. Wang, Y. Gou, J. Li, Y. Zhang, and Y. Yang, “Region semantically aligned network for zero-shot learning,” in _CIKM_ , 2021, pp. 2080–2090. 3.2.1, 2 

- [61] Z. Ji, Y. Fu, J. Guo, Y. Pang, Z. M. Zhang _et al._ , “Stacked semanticsguided attention model for fine-grained zero-shot learning,” _NeurIPS_ , vol. 31, 2018. 3.2.2, 2 

- [62] M. Elhoseiny, Y. Zhu, H. Zhang, and A. Elgammal, “Link the head to the” beak”: Zero shot learning from noisy text description at part precision,” in _CVPR_ , 2017, pp. 5640–5649. 3.2.2, 2 

- [63] Y. Zhu, M. Elhoseiny, B. Liu, X. Peng, and A. Elgammal, “A generative adversarial approach for zero-shot learning from noisy texts,” in _CVPR_ , 2018, pp. 1004–1013. 3.2.2, 2 

- [64] Y. Li, J. Zhang, J. Zhang, and K. Huang, “Discriminative learning of latent features for zero-shot recognition,” in _CVPR_ , 2018, pp. 7463–7471. 3.2.2, 2 

- [65] J. Ge, H. Xie, S. Min, and Y. Zhang, “Semantic-guided reinforced region embedding for generalized zero-shot learning,” in _AAAI_ , vol. 35, no. 2, 2021, pp. 1406–1414. 3.2.2, 2 

- [66] Y. Li, Z. Liu, L. Yao, X. Wang, J. McAuley, and X. Chang, “An entropy-guided reinforced partial convolutional network for zero-shot learning,” _IEEE TCSVT_ , vol. 32, no. 8, pp. 5175–5186, 2022. 3.2.2, 2 

- [67] M. Liu, C. Zhang, H. Bai, and Y. Zhao, “Part-object progressive refinement network for zero-shot learning,” _IEEE TIP_ , 2024. 3.2.2, 2 

- [68] S. Chen, W. Hou, S. Khan, and F. S. Khan, “Progressive semanticguided vision transformer for zero-shot learning,” in _CVPR_ , 2024, pp. 23 964–23 974. 3.2.2, 2 

- [69] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly _et al._ , “An image is worth 16x16 words: Transformers for image recognition at scale,” _arXiv_ , 2020. 3.2.2, 3.3.1, 6.2 

- [70] W. Xu, Y. Xian, J. Wang, B. Schiele, and Z. Akata, “Vgse: Visually-grounded semantic embeddings for zero-shot learning,” in _CVPR_ , 2022, pp. 9316–9325. 3.2.2, 2 

- [71] T. N. Kipf and M. Welling, “Semi-supervised classification with graph convolutional networks,” _arXiv_ , 2016. 3.2.3 

- [72] Z. Hu, H. Zhao, J. Peng, and X. Gu, “Region interaction and attribute embedding for zero-shot learning,” _IS_ , vol. 609, pp. 984– 995, 2022. 3.2.3, 6.3, 2 

- [73] S. Chen, Z. Hong, G. Xie, Q. Peng, X. You, W. Ding, and L. Shao, “Gndan: Graph navigated dual attention network for zero-shot learning,” _IEEE TNNLS_ , vol. 35, no. 4, pp. 4516–4529, 2022. 3.2.3, 2 

- [74] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” _NeurIPS_ , vol. 30, 2017. 3.3.1 

- [75] Y. Liu, L. Zhou, X. Bai, Y. Huang, L. Gu, J. Zhou, and T. Harada, “Goal-oriented gaze estimation for zero-shot learning,” in _CVPR_ , 2021, pp. 3794–3803. 3.3.1, 2 

- [76] D. Huynh and E. Elhamifar, “Compositional zero-shot learning via fine-grained dense feature composition,” _NeurIPS_ , vol. 33, pp. 19 849–19 860, 2020. 3.3.1, 2 

- [77] Y. Liu, Y. Dang, X. Gao, J. Han, and L. Shao, “Zero-shot learning with attentive region embedding and enhanced semantics,” _IEEE TNNLS_ , vol. 35, no. 3, pp. 4220–4231, 2022. 3.3.1, 3.4.1, 2 

- [78] M. F. Naeem, Y. Xian, L. V. Gool, and F. Tombari, “I2dformer: Learning image to document attention for zero-shot image classification,” _NeurIPS_ , vol. 35, pp. 12 283–12 294, 2022. 3.3.1, 2 

- [79] Z. Chen, Y. Huang, J. Chen, Y. Geng, W. Zhang, Y. Fang, J. Z. Pan, and H. Chen, “Duet: Cross-modal semantic grounding for contrastive zero-shot learning,” in _AAAI_ , vol. 37, no. 1, 2023, pp. 405–413. 3.3.1, 6.3, 2 

- [80] M. Liu, F. Li, C. Zhang, Y. Wei, H. Bai, and Y. Zhao, “Progressive semantic-visual mutual adaption for generalized zero-shot learning,” in _CVPR_ , 2023, pp. 15 337–15 346. 3.3.1, 2 

- [81] S. Chen, Z. Hong, G.-S. Xie, W. Yang, Q. Peng, K. Wang, J. Zhao, and X. You, “Msdn: Mutually semantic distillation network for zero-shot learning,” in _CVPR_ , 2022, pp. 7612–7621. 3.3.1, 6.3, 2 

- [82] H.-M. Yang, X.-Y. Zhang, F. Yin, and C.-L. Liu, “Robust classification with convolutional prototype learning,” in _CVPR_ , 2018, pp. 3474–3482. 3.3.2 

- [83] J. Liu, Y. Ren, W. Li, Y. Zheng, and C. Wang, “Improving out-ofdistribution detection with margin-based prototype learning,” in _ICONIP_ . Springer, 2023, pp. 149–160. 3.3.2 

- [84] K. Wang, J. H. Liew, Y. Zou, D. Zhou, and J. Feng, “Panet: Fewshot image semantic segmentation with prototype alignment,” in _ICCV_ , 2019, pp. 9197–9206. 3.3.2 

- [85] W. Xu, Y. Xian, J. Wang, B. Schiele, and Z. Akata, “Attribute prototype network for zero-shot learning,” _NeurIPS_ , vol. 33, pp. 21 969–21 980, 2020. 3.3.2, 6.3, 2 

- [86] D. Jayaraman, F. Sha, and K. Grauman, “Decorrelating semantic visual attributes by resisting the urge to share,” in _CVPR_ , 2014, pp. 1629–1636. 3.3.2 

- [87] C. Wang, S. Min, X. Chen, X. Sun, and H. Li, “Dual progressive prototype network for generalized zero-shot learning,” _NeurIPS_ , vol. 34, pp. 2936–2948, 2021. 3.3.2, 6.3, 2 

- [88] T. Guo, J. Liang, and G.-S. Xie, “Group-wise interactive region learning for zero-shot recognition,” _IS_ , vol. 642, p. 119135, 2023. 3.3.2, 2 

- [89] D. Cheng, G. Wang, N. Wang, D. Zhang, Q. Zhang, and X. Gao, “Discriminative and robust attribute alignment for zero-shot learning,” _IEEE TCSVT_ , vol. 33, no. 8, pp. 4244–4256, 2023. 3.3.2, 2 

- [90] Y. Du, M. Shi, F. Wei, and G. Li, “Boosting zero-shot learning via contrastive optimization of attribute representations,” _IEEE TNNLS_ , 2023. 3.3.2, 2 

- [91] Z. Chen, P. Zhang, J. Li, S. Wang, and Z. Huang, “Zero-shot learning by harnessing adversarial samples,” in _ACM MM_ , 2023, pp. 4138–4146. 3.3.2, 8.7 

- [92] Y. Liu, J. Guo, D. Cai, and X. He, “Attribute attention for semantic disambiguation in zero-shot learning,” in _ICCV_ , 2019, pp. 6698– 6707. 3.4.1, 6.3, 2 

- [93] L. Liu, T. Zhou, G. Long, J. Jiang, and C. Zhang, “Attribute propagation network for graph zero-shot learning,” in _AAAI_ , vol. 34, no. 04, 2020, pp. 4868–4875. 3.4.1, 2 

- [94] Z. Akata, M. Malinowski, M. Fritz, and B. Schiele, “Multi-cue zero-shot learning with strong supervision,” in _CVPR_ , 2016, pp. 59–68. 3.4.2, 2, 8.4 

- [95] Z. Rao, J. Guo, X. Lu, J. Liang, J. Zhang, H. Wang, K. Wei, and X. Cao, “Dual expert distillation network for generalized zeroshot learning,” in _IJCAI_ , 2024. 3.4.2, 2 

- [96] Z. Nan, Y. Liu, N. Zheng, and S.-C. Zhu, “Recognizing unseen attribute-object pair with generative model,” in _AAAI_ , vol. 33, no. 01, 2019, pp. 8811–8818. 4.2.1, 3 

- [97] F. Ruis, G. Burghouts, and D. Bucur, “Independent prototype propagation for zero-shot compositionality,” _NeurIPS_ , vol. 34, pp. 10 641–10 653, 2021. 4.2.1, 6.3, 3 

- [98] X. Hu and Z. Wang, “Leveraging sub-class discimination for compositional zero-shot learning,” in _AAAI_ , vol. 37, no. 1, 2023, pp. 890–898. 4.2.1, 3 

- [99] Z. Zheng, H. Zhu, and R. Nevatia, “Caila: Concept-aware intralayer adapters for compositional zero-shot learning,” in _WCACV_ , 2024, pp. 1721–1731. 4.2.1, 3 

- [100] C. Z.-S. Learning, “A decomposable causal view of compositional zero-shot learning,” 2022. 4.2.1, 3 

- [101] N. Saini, K. Pham, and A. Shrivastava, “Disentangling visual embeddings for attributes and objects,” in _CVPR_ , 2022, pp. 13 658– 13 667. 4.2.2, 6.3, 3 

- [102] S. Hao, K. Han, and K.-Y. K. Wong, “Learning attention as disentangler for compositional zero-shot learning,” in _CVPR_ , 2023, pp. 15 315–15 324. 4.2.2, 3 

- [103] C. Jing, Y. Li, H. Chen, and C. Shen, “Retrieval-augmented primitive representations for compositional zero-shot learning,” in _AAAI_ , vol. 38, no. 3, 2024, pp. 2652–2660. 4.2.2, 3 

- [104] T. Zhang, K. Liang, R. Du, X. Sun, Z. Ma, and J. Guo, “Learning invariant visual representations for compositional zero-shot learning,” in _ECCV_ . Springer, 2022, pp. 339–355. 4.2.2, 6.3, 3 

- [105] X. Lu, S. Guo, Z. Liu, and J. Guo, “Decomposed soft prompt guided fusion enhancing for compositional zero-shot learning,” in _CVPR_ , 2023, pp. 23 560–23 569. 4.2.2, 6.3, 3 

- [106] S. Huang, B. Gong, Y. Feng, M. Zhang, Y. Lv, and D. Wang, “Troika: Multi-path cross-modal traction for compositional zeroshot learning,” in _CVPR_ , 2024, pp. 24 005–24 014. 4.2.2, 3 

- [107] H. Kim, J. Lee, S. Park, and K. Sohn, “Hierarchical visual primitive experts for compositional zero-shot learning,” in _ICCV_ , 2023, pp. 5675–5685. 5, 4.3.1, 6.3, 3 

UNDER REVIEW 

18 

- [108] A. Panda and D. P. Mukherjee, “Compositional zero-shot learning using multi-branch graph convolution and cross-layer knowledge sharing,” _PR_ , vol. 145, p. 109916, 2024. 4.3.1, 3 

- [109] Y.-L. Li, Y. Xu, X. Mao, and C. Lu, “Symmetry and group in attribute-object compositions,” in _CVPR_ , 2020, pp. 11 316–11 325. 4.3.1, 3 

- [110] Q. Wang, L. Liu, C. Jing, H. Chen, G. Liang, P. Wang, and C. Shen, “Learning conditional attributes for compositional zeroshot learning,” in _CVPR_ , 2023, pp. 11 197–11 206. 4.3.1, 3 

- [111] Z. Liu, Y. Li, L. Yao, X. Chang, W. Fang, X. Wu, and A. El Saddik, “Simple primitives with feasibility-and contextualitydependence for open-world compositional zero-shot learning,” _IEEE TPAMI_ , 2023. 4.3.2, 3 

- [112] F. Huo, W. Xu, S. Guo, J. Guo, H. Wang, Z. Liu, and X. Lu, “Procc: Progressive cross-primitive compatibility for open-world compositional zero-shot learning,” in _AAAI_ , vol. 38, no. 11, 2024, pp. 12 689–12 697. 4.3.2, 3 

- [113] Z. Xu, G. Wang, Y. Wong, and M. S. Kankanhalli, “Relationaware compositional zero-shot learning for attribute-object pair recognition,” _IEEE TMM_ , vol. 24, pp. 3652–3664, 2021. 4.4.1, 6.3, 3 

- [114] M. G. Z. A. Khan, M. F. Naeem, L. Van Gool, A. Pagani, D. Stricker, and M. Z. Afzal, “Learning attention propagation for compositional zero-shot learning,” in _WCACV_ , 2023, pp. 3828– 3837. 4.4.1, 6.3, 3 

- [115] M. F. Naeem, Y. Xian, F. Tombari, and Z. Akata, “Learning graph embeddings for compositional zero-shot learning,” in _CVPR_ , 2021, pp. 953–962. 4.4.2, 6.1, 1, 6.3, 3 

- [116] M. U. Anwaar, Z. Pan, and M. Kleinsteuber, “On leveraging variational graph embeddings for open world compositional zero-shot learning,” in _ACM MM_ , 2022, pp. 4645–4654. 4.4.2, 6.3, 3 

- [117] G. Xu, J. Chai, and P. Kordjamshidi, “Gipcol: Graph-injected soft prompting for compositional zero-shot learning,” in _WCACV_ , 2024, pp. 5774–5783. 4.4.2, 6.3, 3 

- [118] A. Jaiswal, A. R. Babu, M. Z. Zadeh, D. Banerjee, and F. Makedon, “A survey on contrastive self-supervised learning,” _Technologies_ , vol. 9, no. 1, p. 2, 2020. 4.4.3 

- [119] X. Li, X. Yang, K. Wei, C. Deng, and M. Yang, “Siamese contrastive embedding network for compositional zero-shot learning,” in _CVPR_ , 2022, pp. 9326–9335. 4.4.3, 6.3, 3 

- [120] Y. Yang, R. Pan, X. Li, X. Yang, and C. Deng, “Dual-stream contrastive learning for compositional zero-shot recognition,” _IEEE TMM_ , vol. 26, pp. 1909–1919, 2023. 4.4.3, 3 

- [121] X. Wang, F. Yu, R. Wang, T. Darrell, and J. E. Gonzalez, “Tafe-net: Task-aware feature embeddings for low shot learning,” in _CVPR_ , 2019, pp. 1831–1840. 4.5 

- [122] C. Jiang, Q. Ye, S. Wang, Y. Shen, Z. Zhang, and H. Zhang, “Mutual balancing in state-object components for compositional zero-shot learning,” _PR_ , vol. 152, p. 110451, 2024. 4.5, 3 

- [123] C. Jiang and H. Zhang, “Revealing the proximate long-tail distribution in compositional zero-shot learning,” in _AAAI_ , vol. 38, no. 3, 2024, pp. 2498–2506. 4.5, 3 

- [124] Y. Li, Z. Liu, H. Chen, and L. Yao, “Context-based and diversitydriven specificity in compositional zero-shot learning,” in _CVPR_ , 2024, pp. 17 037–17 046. 4.5, 3 

- [125] S. Karthik, M. Mancini, and Z. Akata, “Kg-sp: Knowledge guided simple primitives for open world compositional zero-shot learning,” in _CVPR_ , 2022, pp. 9336–9345. 4.5 

- [126] X. Hu and Z. Wang, “A dynamic learning method towards realistic compositional zero-shot learning,” in _AAAI_ , vol. 38, no. 3, 2024, pp. 2265–2273. 4.5 

- [127] J. Zhang, J. Huang, S. Jin, and S. Lu, “Vision-language models for vision tasks: A survey,” _IEEE TPAMI_ , 2024. 5.1 

- [128] Q. Cui, B. Zhou, Y. Guo, W. Yin, H. Wu, O. Yoshie, and Y. Chen, “Contrastive vision-language pre-training with limited resources,” in _ECCV_ . Springer, 2022, pp. 236–253. 5.1 

- [129] A. Singh, R. Hu, V. Goswami, G. Couairon, W. Galuba, M. Rohrbach, and D. Kiela, “Flava: A foundational language and vision alignment model,” in _CVPR_ , 2022, pp. 15 638–15 650. 5.1 

- [130] R. Huang, Y. Long, J. Han, H. Xu, X. Liang, C. Xu, and X. Liang, “Nlip: Noise-robust language-image pre-training,” in _AAAI_ , vol. 37, no. 1, 2023, pp. 926–934. 5.1 

- [131] S. Esmaeilpour, B. Liu, E. Robertson, and L. Shu, “Zero-shot outof-distribution detection based on the pre-trained model clip,” in _AAAI_ , vol. 36, no. 6, 2022, pp. 6568–6576. 5.1 

- [132] H. Wang, Y. Li, H. Yao, and X. Li, “Clipn for zero-shot ood detection: Teaching clip to say no,” in _ICCV_ , 2023, pp. 1802–1812. 5.1 

- [133] M. Shu, W. Nie, D.-A. Huang, Z. Yu, T. Goldstein, A. Anandkumar, and C. Xiao, “Test-time prompt tuning for zero-shot generalization in vision-language models,” _NeurIPS_ , vol. 35, pp. 14 274–14 289, 2022. 6, 5.3, 6.3, 4 

- [134] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell _et al._ , “Language models are few-shot learners,” _NeurIPS_ , vol. 33, pp. 1877– 1901, 2020. 5.2, 6.2 

- [135] S. Pratt, I. Covert, R. Liu, and A. Farhadi, “What does a platypus look like? generating customized prompts for zero-shot image classification,” in _ICCV_ , 2023, pp. 15 691–15 701. 5.2, 4, 8.3 

- [136] Z. Novack, J. McAuley, Z. C. Lipton, and S. Garg, “Chils: Zeroshot image classification with hierarchical label sets,” in _ICML_ . PMLR, 2023, pp. 26 342–26 362. 5.2, 4 

- [137] Z. Chen, “Don’t paint everyone with the same brush: Adaptive prompt prototype learning for vision-language models.” 5.2, 4 

- [138] V. Udandarao, A. Gupta, and S. Albanie, “Sus-x: Training-free name-only transfer of vision-language models,” in _ICCV_ , 2023, pp. 2725–2736. 5.2, 4 

- [139] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, “High-resolution image synthesis with latent diffusion models,” in _CVPR_ , 2022, pp. 10 684–10 695. 5.2, 6.2 

- [140] C.-M. Feng, K. Yu, Y. Liu, S. Khan, and W. Zuo, “Diverse data augmentation with diffusions for effective test-time prompt tuning,” in _ICCV_ , 2023, pp. 2704–2714. 5.3, 4 

- [141] J. Abdul Samadh, M. H. Gani, N. Hussein, M. U. Khattak, M. M. Naseer, F. Shahbaz Khan, and S. H. Khan, “Align your prompts: Test-time prompting with distribution alignment for zero-shot generalization,” _NeurIPS_ , vol. 36, 2024. 5.3, 4 

- [142] X. Ma, J. Zhang, S. Guo, and W. Xu, “Swapprompt: Test-time prompt adaptation for vision-language models,” _NeurIPS_ , vol. 36, 2024. 5.3, 6.3, 4 

- [143] Z. Liu, H. Sun, Y. Peng, and J. Zhou, “Dart: Dual-modal adaptive online prompting and knowledge retention for test-time adaptation,” in _AAAI_ , vol. 38, no. 13, 2024, pp. 14 106–14 114. 5.3, 4 

- [144] Y. Zhang, W. Zhu, H. Tang, Z. Ma, K. Zhou, and L. Zhang, “Dual memory networks: A versatile adaptation approach for visionlanguage models,” in _CVPR_ , 2024, pp. 28 718–28 728. 5.3, 4 

- [145] A. Karmanov, D. Guan, S. Lu, A. El Saddik, and E. Xing, “Efficient test-time adaptation of vision-language models,” in _CVPR_ , 2024, pp. 14 162–14 171. 5.3, 4 

- [146] D.-C. Zhang, Z. Zhou, and Y.-F. Li, “Robust test-time adaptation for zero-shot prompt tuning,” in _AAAI_ , vol. 38, no. 15, 2024, pp. 16 714–16 722. 5.3, 4 

- [147] M. Zanella and I. Ben Ayed, “On the test-time zero-shot generalization of vision-language models: Do we really need prompt learning?” in _CVPR_ , 2024, pp. 23 783–23 793. 5.3, 4 

- [148] T. Huang, J. Chu, and F. Wei, “Unsupervised prompt learning for vision-language models,” _arXiv_ , 2022. 5.4, 4 

- [149] J. Li, S. Savarese, and S. C. Hoi, “Masked unsupervised selftraining for label-free image classification,” _arXiv_ , 2022. 5.4, 4 

- [150] Q. Qian, Y. Xu, and J. Hu, “Intra-modal proxy learning for zeroshot visual categorization with clip,” _NeurIPS_ , vol. 36, 2024. 5.4, 6.3, 4 

- [151] M. J. Mirza, L. Karlinsky, W. Lin, H. Possegger, M. Kozinski, R. Feris, and H. Bischof, “Lafter: Label-free tuning of zeroshot classifier using language and unlabeled image collections,” _NeurIPS_ , vol. 36, 2024. 5.4, 4 

- [152] Y. Kalantidis, G. Tolias _et al._ , “Label propagation for zero-shot classification with vision-language models,” in _CVPR_ , 2024, pp. 23 209–23 218. 5.4, 4 

- [153] J. Kahana, N. Cohen, and Y. Hoshen, “Improving zero-shot models with label distribution priors,” _arXiv_ , 2022. 5.4, 4 

- [154] M.-E. Nilsback and A. Zisserman, “Automated flower classification over a large number of classes,” in _ICVGIP_ . IEEE, 2008, pp. 722–729. 6.1, 1 

- [155] G. Van Horn, S. Branson, R. Farrell, S. Haber, J. Barry, P. Ipeirotis, P. Perona, and S. Belongie, “Building a bird recognition app and large scale dataset with citizen scientists: The fine print in finegrained dataset collection,” in _CVPR_ , 2015, pp. 595–604. 6.1, 1 

- [156] C. H. Lampert, H. Nickisch, and S. Harmeling, “Attribute-based classification for zero-shot visual object categorization,” _IEEE TPAMI_ , vol. 36, no. 3, pp. 453–465, 2013. 6.1, 1 

UNDER REVIEW 

19 

- [157] A. Farhadi, I. Endres, D. Hoiem, and D. Forsyth, “Describing objects by their attributes,” in _CVPR_ . IEEE, 2009, pp. 1778–1785. 1 

- [158] A. Yu and K. Grauman, “Fine-grained visual comparisons with local learning,” in _CVPR_ , 2014, pp. 192–199. 1 

- [159] P. Isola, J. J. Lim, and E. H. Adelson, “Discovering states and transformations in image collections,” in _CVPR_ , 2015, pp. 1383– 1391. 1 

- [160] N. Saini, K. Pham, and A. Shrivastava, “Disentangling visual embeddings for attributes and objects,” in _CVPR_ , June 2022, pp. 13 658–13 667. 1 

- [161] L. Fei-Fei, R. Fergus, and P. Perona, “Learning generative visual models from few training examples: An incremental bayesian approach tested on 101 object categories,” in _CVPRW_ . IEEE, 2004, pp. 178–178. 1 

- [162] G. Griffin, A. Holub, P. Perona _et al._ , “Caltech-256 object category dataset,” Technical Report 7694, California Institute of Technology Pasadena, Tech. Rep., 2007. 1 

- [163] J. Xiao, J. Hays, K. A. Ehinger, A. Oliva, and A. Torralba, “Sun database: Large-scale scene recognition from abbey to zoo,” in _CVPR_ . IEEE, 2010, pp. 3485–3492. 1 

- [164] L. Bossard, M. Guillaumin, and L. Van Gool, “Food-101–mining discriminative components with random forests,” in _ECCV_ . Springer, 2014, pp. 446–461. 1, 6.1 

- [165] J. Krause, J. Deng, M. Stark, and L. Fei-Fei, “Collecting a largescale dataset of fine-grained cars,” 2013. 1, 6.1 

- [166] S. Maji, E. Rahtu, J. Kannala, M. Blaschko, and A. Vedaldi, “Finegrained visual classification of aircraft,” _arXiv_ , 2013. 1, 6.1 

- [167] O. M. Parkhi, A. Vedaldi, A. Zisserman, and C. Jawahar, “Cats and dogs,” in _CVPR_ . IEEE, 2012, pp. 3498–3505. 1, 6.1 

- [168] M. Cimpoi, S. Maji, I. Kokkinos, S. Mohamed, and A. Vedaldi, “Describing textures in the wild,” in _CVPR_ , 2014, pp. 3606–3613. 1, 6.1 

- [169] P. Helber, B. Bischke, A. Dengel, and D. Borth, “Eurosat: A novel dataset and deep learning benchmark for land use and land cover classification,” _IEEE JSTAEORS_ , vol. 12, no. 7, pp. 2217–2226, 2019. 6.1, 1 

- [170] A. Krizhevsky, G. Hinton _et al._ , “Learning multiple layers of features from tiny images,” 2009. 6.1, 1 

- [171] T. Berg, J. Liu, S. Woo Lee, M. L. Alexander, D. W. Jacobs, and P. N. Belhumeur, “Birdsnap: Large-scale fine-grained visual categorization of birds,” in _CVPR_ , 2014, pp. 2011–2018. 1 

- [172] X. Chen, X. Deng, Y. Lan, Y. Long, J. Weng, Z. Liu, and Q. Tian, “Explanatory object part aggregation for zero-shot learning,” _IEEE TPAMI_ , 2023. 2 

- [173] Z. Wang, Y. Gou, J. Li, L. Zhu, and H. T. Shen, “Languageaugmented pixel embedding for generalized zero-shot learning,” _IEEE TCSVT_ , vol. 33, no. 3, pp. 1019–1030, 2022. 2 

- [174] D. Cheng, G. Wang, B. Wang, Q. Zhang, J. Han, and D. Zhang, “Hybrid routing transformer for zero-shot learning,” _PR_ , vol. 137, p. 109270, 2023. 2 

- [175] Y. Li, Z. Liu, S. Jha, and L. Yao, “Distilled reverse attention network for open-world compositional zero-shot learning,” in _ICCV_ , 2023, pp. 1782–1791. 3 

- [176] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in _CVPR_ , 2016, pp. 770–778. 6.2 

- [177] K. Simonyan and A. Zisserman, “Very deep convolutional networks for large-scale image recognition,” _arXiv_ , 2014. 6.2 

- [178] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. Reed, D. Anguelov, D. Erhan, V. Vanhoucke, and A. Rabinovich, “Going deeper with convolutions,” in _CVPR_ , 2015, pp. 1–9. 6.2 

- [179] A. Krizhevsky, I. Sutskever, and G. E. Hinton, “Imagenet classification with deep convolutional neural networks,” _NeurIPS_ , vol. 25, 2012. 6.2 

- [180] Y. Hou, J. Zhang, Z. Lin, H. Lu, R. Xie, J. McAuley, and W. X. Zhao, “Large language models are zero-shot rankers for recommender systems,” in _ECIR_ . Springer, 2024, pp. 364–381. 7.1 

- [181] T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa, “Large language models are zero-shot reasoners,” _NeurIPS_ , vol. 35, pp. 22 199–22 213, 2022. 7.1 

- [182] J. Wei, M. Bosma, V. Y. Zhao, K. Guu, A. W. Yu, B. Lester, N. Du, A. M. Dai, and Q. V. Le, “Finetuned language models are zeroshot learners,” _arXiv_ , 2021. 7.1 

- [183] M. Johnson, M. Schuster, Q. V. Le, M. Krikun, Y. Wu, Z. Chen, N. Thorat, F. Vi´egas, M. Wattenberg, G. Corrado _et al._ , “Google’s multilingual neural machine translation system: Enabling zeroshot translation,” _TACL_ , vol. 5, pp. 339–351, 2017. 7.1 

- [184] J. Baek, A. F. Aji, and A. Saffari, “Knowledge-augmented language model prompting for zero-shot knowledge graph question answering,” _arXiv_ , 2023. 7.1 

- [185] P. Kumar, K. Pathania, and B. Raman, “Zero-shot learning based cross-lingual sentiment analysis for sanskrit text with insufficient labeled data,” _Applied Intelligence_ , vol. 53, no. 9, pp. 10 096–10 113, 2023. 7.1 

- [186] Q. Chen, W. Wang, K. Huang, and F. Coenen, “Zero-shot text classification via knowledge graph embedding for social media data,” _IEEE IoT-J_ , vol. 9, no. 12, pp. 9205–9213, 2021. 7.1 

- [187] M. S. Bari, S. Joty, and P. Jwalapuram, “Zero-resource crosslingual named entity recognition,” in _AAAI_ , vol. 34, no. 05, 2020, pp. 7415–7423. 7.1 

- [188] N. Thakur, N. Reimers, A. R¨uckl´e, A. Srivastava, and I. Gurevych, “Beir: A heterogenous benchmark for zero-shot evaluation of information retrieval models,” _arXiv_ , 2021. 7.1 

- [189] D. Huynh and E. Elhamifar, “A shared multi-attention framework for multi-label zero-shot learning,” in _CVPR_ , 2020, pp. 8776–8786. 7.2 

- [190] S. Ren, K. He, R. Girshick, and J. Sun, “Faster r-cnn: Towards realtime object detection with region proposal networks,” _NeurIPS_ , vol. 28, 2015. 7.2 

- [191] W. Liu, D. Anguelov, D. Erhan, C. Szegedy, S. Reed, C.-Y. Fu, and A. C. Berg, “Ssd: Single shot multibox detector,” in _ECCV_ . Springer, 2016, pp. 21–37. 7.2 

- [192] J. Long, E. Shelhamer, and T. Darrell, “Fully convolutional networks for semantic segmentation,” in _CVPR_ , 2015, pp. 3431–3440. 7.2 

- [193] A. Kirillov, E. Mintun, N. Ravi, H. Mao, C. Rolland, L. Gustafson, T. Xiao, S. Whitehead, A. C. Berg, W.-Y. Lo _et al._ , “Segment anything,” in _ICCV_ , 2023, pp. 4015–4026. 7.2 

- [194] A. Bansal, K. Sikka, G. Sharma, R. Chellappa, and A. Divakaran, “Zero-shot object detection,” in _ECCV_ , 2018, pp. 384–400. 7.2 

- [195] S. Rahman, S. Khan, and F. Porikli, “Zero-shot object detection: Learning to simultaneously recognize and localize novel concepts,” in _ACCV_ . Springer, 2018, pp. 547–563. 7.2 

- [196] Z. Li, L. Yao, X. Zhang, X. Wang, S. Kanhere, and H. Zhang, “Zero-shot object detection with textual descriptions,” in _AAAI_ , vol. 33, no. 01, 2019, pp. 8690–8697. 7.2 

- [197] Z. Gu, S. Zhou, L. Niu, Z. Zhao, and L. Zhang, “Context-aware feature generation for zero-shot semantic segmentation,” in _ACM MM_ , 2020, pp. 1921–1929. 7.2 

- [198] D. Huynh, J. Kuen, Z. Lin, J. Gu, and E. Elhamifar, “Open-vocabulary instance segmentation via robust cross-modal pseudo-labeling,” in _CVPR_ , 2022, pp. 7020–7031. 7.2 

- [199] S. He, H. Ding, and W. Jiang, “Primitive generation and semanticrelated alignment for universal zero-shot segmentation,” in _CVPR_ , 2023, pp. 11 238–11 247. 7.2 

- [200] Y. Guo, H. Wang, Q. Hu, H. Liu, L. Liu, and M. Bennamoun, “Deep learning for 3d point clouds: A survey,” _IEEE TPAMI_ , vol. 43, no. 12, pp. 4338–4364, 2020. 7.3 

- [201] M. F. Naeem, E. P. Ornek,<sup>¨</sup> Y. Xian, L. Van Gool, and F. Tombari, “3d compositional zero-shot learning with decompositional consensus,” in _ECCV_ . Springer, 2022, pp. 713–730. 7.3 

- [202] A. Cheraghian, S. Rahman, T. F. Chowdhury, D. Campbell, and L. Petersson, “Zero-shot learning on 3d point cloud objects and beyond,” _IJCV_ , vol. 130, no. 10, pp. 2364–2384, 2022. 7.3 

- [203] D. Zhang, D. Liang, H. Yang, Z. Zou, X. Ye, Z. Liu, and X. Bai, “Sam3d: Zero-shot 3d object detection via segment anything model,” _arXiv_ , 2023. 7.3 

- [204] A. Abdelreheem, I. Skorokhodov, M. Ovsjanikov, and P. Wonka, “Satr: Zero-shot semantic segmentation of 3d shapes,” in _ICCV_ , 2023, pp. 15 166–15 179. 7.3 

- [205] R. Liu, R. Wu, B. Van Hoorick, P. Tokmakov, S. Zakharov, and C. Vondrick, “Zero-1-to-3: Zero-shot one image to 3d object,” in _ICCV_ , 2023. 7.3 

- [206] K. Liu, F. Zhan, Y. Chen, J. Zhang, Y. Yu, A. El Saddik, S. Lu, and E. P. Xing, “Stylerf: Zero-shot 3d style transfer of neural radiance fields,” in _CVPR_ , 2023, pp. 8338–8348. 7.3 

- [207] J. Xu, X. Wang, W. Cheng, Y.-P. Cao, Y. Shan, X. Qie, and S. Gao, “Dream3d: Zero-shot text-to-3d synthesis using 3d shape prior and text-to-image diffusion models,” in _CVPR_ , 2023, pp. 20 908– 20 918. 7.3 

- [208] L. Li and A. Dai, “Genzi: Zero-shot 3d human-scene interaction generation,” in _CVPR_ , 2024, pp. 20 465–20 474. 7.3 

UNDER REVIEW 

20 

- [209] Z. Jiang, Z. Zhou, L. Li, W. Chai, C.-Y. Yang, and J.-N. Hwang, “Back to optimization: Diffusion-based zero-shot 3d human pose estimation,” in _WCACV_ , 2024, pp. 6142–6152. 7.3 

- [210] A. Abdelreheem, A. Eldesokey, M. Ovsjanikov, and P. Wonka, “Zero-shot 3d shape correspondence,” in _SIGGRAPH_ , 2023, pp. 1–11. 7.3 

- [211] S. Javed, A. Mahmood, I. I. Ganapathi, F. A. Dharejo, N. Werghi, and M. Bennamoun, “Cplip: Zero-shot learning for histopathology with comprehensive vision-language alignment,” in _CVPR_ , 2024, pp. 11 450–11 459. 7.4 

- [212] X. Li, C. Wen, Y. Hu, and N. Zhou, “Rs-clip: Zero shot remote sensing scene classification via contrastive vision-language supervision,” _IJAEOG_ , vol. 124, p. 103497, 2023. 7.4 

- [213] A. Li, C. Qiu, M. Kloft, P. Smyth, M. Rudolph, and S. Mandt, “Zero-shot anomaly detection via batch normalization,” _NeurIPS_ , vol. 36, 2024. 7.4 

- [214] S. Chen and D. Huang, “Elaborative rehearsal for zero-shot action recognition,” in _ICCV_ , 2021, pp. 13 638–13 647. 7.4 

- [215] S. Wang, J. Chang, Z. Wang, H. Li, W. Ouyang, and Q. Tian, “Content-aware rectified activation for zero-shot fine-grained image retrieval,” _IEEE TPAMI_ , 2024. 7.4 

- [216] M. Hong, X. Zhang, G. Li, and Q. Huang, “Fine-grained feature generation for generalized zero-shot video classification,” _IEEE TIP_ , vol. 32, pp. 1599–1612, 2023. 7.4 

- [217] L. Wang, X. Zhang, H. Su, and J. Zhu, “A comprehensive survey of continual learning: theory, method and application,” _IEEE TPAMI_ , 2024. 8.1 

- [218] F. Zhou, S. Huang, B. Liu, and D. Yang, “Multi-label image classification via category prototype compositional learning,” _IEEE TCSVT_ , vol. 32, no. 7, pp. 4513–4525, 2021. 8.2 

- [219] J. Guo, Q. Zhou, R. Li, X. Lu, Z. Liu, J. Chen, X. Xie, and J. Zhang, “Parsnets: A parsimonious orthogonal and low-rank linear networks for zero-shot learning,” _IJCAI_ , 2023. 8.5 

- [220] S. Rahman, S. Khan, and F. Porikli, “A unified approach for conventional zero-shot, generalized zero-shot, and few-shot learning,” _IEEE TIP_ , vol. 27, no. 11, pp. 5652–5667, 2018. 8.6 

- [221] N. Shafiee and E. Elhamifar, “Zero-shot attribute attacks on finegrained recognition models,” in _ECCV_ . Springer, 2022, pp. 262– 282. 8.7 

**Jingcai Guo** (Member, IEEE) is currently a Research Assistant Professor with Department of Computing, The Hong Kong Polytechnic University, Hong Kong SAR, where he received his Ph.D. in Dec. 2020. Prior to that, he received his M.E. from Waseda University (2015), Japan, and his B.E. from Sichuan University (2013), China, all in Computer Science. He is interested in Low-shot AI, which targets learning/modeling with limited resources in terms of data, computing capability, and their derivative applications. Topics include zero/few-shot learning, representation learning, federated learning, and model compression. He is currently serving as Associate Editor for IEEE Open Journal of the Computer Society and Guest Editor for IEEE Transactions on Computational Social Systems. He has served as Area Chair, Senior PC, and Session Chair for prestigious conferences like ICML, ACM-MM, AAAI, IJCAI, ICME, and VTC. 

**Zhijie Rao** (Student Member, IEEE) received the B.E. degree from Beijing University of Posts and Telecommunications, China, in 2019, and the M.S. degree from Xiamen University, China, in 2023. He is currently working towards the Ph.D. degree at Department of Computing, The Hong Kong Polytechnic University, Hong Kong SAR. His research interest spans transfer learning and edge AI, with a particular focus on zero/few-shot learning, domain adaptation/generalization, and deployment/training of foundation models. 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0020-17.png)


**Zhi Chen** (Member, IEEE) received the M.S. and Ph.D. degrees from the University of Queensland, Australia, in 2018 and 2023, respectively. He is currently a Postdoctoral Research Fellow with the School of Electrical Engineering and Computer Science at the University of Queensland, Australia. His research interests include zero-shot learning, multimedia understanding, computer vision, and generative modeling. 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0020-19.png)


**Song Guo** (Fellow, IEEE) is currently a Chair Professor in the Department of Computer Science and Engineering at the Hong Kong University of Science and Technology, Hong Kong SAR. His research interests are mainly in machine learning, edge AI, big data, mobile computing, and distributed systems. He is a Fellow of the Canadian Academy of Engineering, a Fellow of the IEEE, and a Member of Academia Europaea. He has served for IEEE Computer Society on Fellow Evaluation Committee, Transactions Operations Committee, Editor-in-Chief Search Committee, etc. He is the current Editor-in-Chief of IEEE Open Journal of the Computer Society and has been on the editorial board of various prestigious IEEE journals. He has also been chair of organizing and technical committees of numerous international conferences. Prof. Guo was the recipient of the 2020 Best Paper Award for IEEE Transactions on Computers, 2019 IEEE TCBD Best Conference Paper Award, 2018 IEEE TCGCC Best Magazine Paper Award, 2019 and 2017 IEEE Systems Journal Annual Best Paper Award, and other 8 Best Paper Awards from IEEE/ACM conferences. He was the recipient of 2024 Edward J. McCluskey Technical Achievement Award. 

**Jingren Zhou** (Fellow, IEEE) received the PhD degree in computer science from Columbia University. He is currently the senior vice president with Alibaba Group and Chief Technology Officer with Alibaba Cloud. He has authored or co-authored dozens of papers in top conferences and journals in his research areas, which include machine learning algorithm platforms, query processing, large-scale distributed systems, optimization of distributed databases, and data processing methods based on largescale distributed systems, and holds several patented inventions of key technologies in the industry. He is a Fellow of IEEE. 

**Dacheng Tao** (Fellow, IEEE) is currently a Distinguished University Professor in the College of Computing and Data Science at Nanyang Technological University, Singapore. He mainly applies statistics and mathematics to artificial intelligence and data science, and his research is detailed in one monograph and over 200 publications in prestigious journals and proceedings at leading conferences, with best paper awards, best student paper awards, and test-oftime awards. His publications have been cited 


![](images/Wang_2024_Action_Conditioned_Spatiotemporal_Video_Glitch_Transformers.pdf-0020-23.png)


over 131K times and have an h-index of 175 in Google Scholar. He received the 2015 and 2020 Australian Eureka Prize, the 2018 IEEE ICDM Research Contributions Award, and the 2021 IEEE Computer Society McCluskey Technical Achievement Award. He is a Fellow of the Australian Academy of Science, AAAS, ACM, and IEEE. 

